from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import Any, Callable, Iterable, Optional, Tuple

from durable_kernel import DurableReferenceKernel, JournalIntegrityError
from hc_kernel import (
    AuthorityGrant,
    EffectState,
    ReferenceKernel,
    _require_aware,
    _require_string,
    _string_tuple,
)

RECOVERY_FENCE_EVENT = "RECOVERY_FENCE"
AUTHORITY_POLICY_PROVENANCE_PREFIX = "authority-issuance-policy:"


@dataclass(frozen=True)
class AuthorityIssuanceRequest:
    """Immutable semantic subject presented to an authority-issuance policy."""

    principal: str
    grantee: str
    action_scope: str
    target_scope: str
    basis_refs: tuple[str, ...]
    valid_from: datetime
    expires_at: datetime
    observed_at: datetime
    current_epoch: int


AuthorityIssuanceValidator = Callable[[AuthorityIssuanceRequest], bool]


def _normalize_authority_issuer_capabilities(registrations: Any) -> Tuple[Tuple[object, str], ...]:
    if registrations is None:
        return ()
    entries = registrations.items() if hasattr(registrations, "items") else registrations
    normalized: list[tuple[object, str]] = []
    try:
        for capability, principal in entries:
            if capability is None or isinstance(capability, (bool, int, float, complex, str, bytes, tuple, frozenset)):
                raise ValueError("authority issuer capabilities must be opaque object handles")
            if not isinstance(principal, str) or not principal:
                raise ValueError("authority issuer principal IDs must be non-empty strings")
            if any(capability is prior for prior, _ in normalized):
                raise ValueError("authority issuer capability is registered more than once")
            normalized.append((capability, principal))
    except (TypeError, ValueError) as exc:
        if isinstance(exc, ValueError):
            raise
        raise ValueError("authority issuer capabilities must be iterable capability/principal pairs") from exc
    return tuple(normalized)


class _AuthorityIssuerBoundary:
    _authority_issuer_capabilities: Tuple[Tuple[object, str], ...]
    _authority_issuance_validator: Optional[AuthorityIssuanceValidator]
    _authority_issuance_policy_id: Optional[str]

    def _set_authority_issuer_boundary(self, registrations: Any, validator: Optional[AuthorityIssuanceValidator], policy_id: Optional[str]) -> None:
        if validator is not None and not callable(validator):
            raise ValueError("authority issuance validator must be callable")
        if validator is not None and (not isinstance(policy_id, str) or not policy_id.strip()):
            raise ValueError("authority issuance policy ID must be configured with validator")
        if validator is None and policy_id is not None:
            raise ValueError("authority issuance policy ID requires validator")
        self._authority_issuer_capabilities = _normalize_authority_issuer_capabilities(registrations)
        self._authority_issuance_validator = validator
        self._authority_issuance_policy_id = policy_id.strip() if isinstance(policy_id, str) else None

    def _principal_for_authority_capability(self, source_capability: object) -> Optional[str]:
        for capability, principal in self._authority_issuer_capabilities:
            if source_capability is capability:
                return principal
        return None

    def _require_authority_principal(self, source_capability: object) -> str:
        principal = self._principal_for_authority_capability(source_capability)
        if principal is None:
            raise ValueError("authority issuer capability is not registered")
        return principal

    def _build_issuance_request(
        self,
        *,
        principal: str,
        grantee: str,
        action_scope: str,
        target_scope: str,
        basis_refs: Iterable[str],
        valid_from: datetime,
        expires_at: datetime,
    ) -> AuthorityIssuanceRequest:
        principal = _require_string(principal, "principal")
        grantee = _require_string(grantee, "grantee")
        action_scope = _require_string(action_scope, "action_scope")
        target_scope = _require_string(target_scope, "target_scope")
        basis_tuple = _string_tuple(basis_refs, "basis_refs")
        if not basis_tuple:
            raise ValueError("authority registration requires an explicit basis reference")
        valid_from = _require_aware(valid_from, "valid_from")
        expires_at = _require_aware(expires_at, "expires_at")
        if expires_at <= valid_from:
            raise ValueError("grant expiry must follow valid_from")
        observed_at = self.now()
        return AuthorityIssuanceRequest(
            principal=principal,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis_tuple,
            valid_from=valid_from,
            expires_at=expires_at,
            observed_at=observed_at,
            current_epoch=self._epoch,
        )

    def _require_issuance_policy(self, request: AuthorityIssuanceRequest) -> str:
        validator = self._authority_issuance_validator
        policy_id = self._authority_issuance_policy_id
        if validator is None or policy_id is None:
            raise ValueError("authority issuance policy is not configured")
        if not validator(request):
            raise ValueError("authority issuance policy denied grant")
        return policy_id

    @staticmethod
    def _bind_policy_provenance(provenance: Iterable[str], policy_id: str) -> tuple[str, ...]:
        values = _string_tuple(provenance, "provenance")
        if any(value.startswith(AUTHORITY_POLICY_PROVENANCE_PREFIX) for value in values):
            raise ValueError("caller cannot supply reserved authority issuance policy provenance")
        marker = f"{AUTHORITY_POLICY_PROVENANCE_PREFIX}{policy_id}"
        return values + (marker,)


class GovernedReferenceKernelV2(_AuthorityIssuerBoundary, ReferenceKernel):
    def __init__(self, *, authority_issuer_capabilities: Any = None, authority_issuance_validator: Optional[AuthorityIssuanceValidator] = None, authority_issuance_policy_id: Optional[str] = None, **kwargs: Any) -> None:
        self._set_authority_issuer_boundary(authority_issuer_capabilities, authority_issuance_validator, authority_issuance_policy_id)
        super().__init__(**kwargs)

    def register_grant(self, *, source_capability: object, grantee: str, action_scope: str, target_scope: str, basis_refs: Iterable[str], valid_from, expires_at, provenance: Iterable[str] = ()) -> AuthorityGrant:
        principal = self._require_authority_principal(source_capability)
        request = self._build_issuance_request(
            principal=principal,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis_refs,
            valid_from=valid_from,
            expires_at=expires_at,
        )
        policy_id = self._require_issuance_policy(request)
        bound_provenance = self._bind_policy_provenance(provenance, policy_id)
        return ReferenceKernel.register_grant(
            self,
            grantor=request.principal,
            grantee=request.grantee,
            action_scope=request.action_scope,
            target_scope=request.target_scope,
            basis_refs=request.basis_refs,
            valid_from=request.valid_from,
            expires_at=request.expires_at,
            provenance=bound_provenance,
        )

    def revoke_grant(self, grant_id: str, *, source_capability: object, revoked_at=None) -> None:
        principal = self._require_authority_principal(source_capability)
        grant = self._authority_grants[grant_id]
        if principal != grant.grantor:
            raise ValueError("authority revoker does not own this grant")
        ReferenceKernel.revoke_grant(self, grant_id, revoked_at=revoked_at)


class GovernedDurableReferenceKernelV2(_AuthorityIssuerBoundary, DurableReferenceKernel):
    def __init__(self, journal_path, *, authority_issuer_capabilities: Any = None, authority_issuance_validator: Optional[AuthorityIssuanceValidator] = None, authority_issuance_policy_id: Optional[str] = None, **kwargs: Any) -> None:
        # Validate the live authority boundary before durable recovery can mutate the journal.
        self._set_authority_issuer_boundary(authority_issuer_capabilities, authority_issuance_validator, authority_issuance_policy_id)
        super().__init__(journal_path, **kwargs)

    def register_grant(self, *, source_capability: object, grantee: str, action_scope: str, target_scope: str, basis_refs: Iterable[str], valid_from, expires_at, provenance: Iterable[str] = ()) -> AuthorityGrant:
        self._ensure_writable()
        principal = self._require_authority_principal(source_capability)
        request = self._build_issuance_request(
            principal=principal,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis_refs,
            valid_from=valid_from,
            expires_at=expires_at,
        )
        policy_id = self._require_issuance_policy(request)
        bound_provenance = self._bind_policy_provenance(provenance, policy_id)
        grant = ReferenceKernel.register_grant(
            self,
            grantor=request.principal,
            grantee=request.grantee,
            action_scope=request.action_scope,
            target_scope=request.target_scope,
            basis_refs=request.basis_refs,
            valid_from=request.valid_from,
            expires_at=request.expires_at,
            provenance=bound_provenance,
        )
        try:
            self._record("AUTHORITY_GRANT_UPSERT", self._grant_data(grant))
        except Exception:
            self._authority_grants.pop(grant.grant_id, None)
            raise
        return grant

    def revoke_grant(self, grant_id: str, *, source_capability: object, revoked_at=None) -> None:
        self._ensure_writable()
        principal = self._require_authority_principal(source_capability)
        previous = self._authority_grants[grant_id]
        if principal != previous.grantor:
            raise ValueError("authority revoker does not own this grant")
        ReferenceKernel.revoke_grant(self, grant_id, revoked_at=revoked_at)
        updated = self._authority_grants[grant_id]
        if updated == previous:
            return
        try:
            self._record("AUTHORITY_GRANT_UPSERT", self._grant_data(updated))
        except Exception:
            self._authority_grants[grant_id] = previous
            raise

    def _validate_recovery_fence(self, data: dict[str, Any], *, event_epoch: int) -> tuple[int, int, tuple[str, ...]]:
        if set(data) != {"from_epoch", "to_epoch", "requested_action_ids"}:
            raise ValueError("recovery fence has unexpected/missing fields")
        from_epoch, to_epoch = data["from_epoch"], data["to_epoch"]
        if type(from_epoch) is not int or type(to_epoch) is not int:
            raise ValueError("recovery fence epochs must be integers")
        if event_epoch != from_epoch or self._epoch != from_epoch:
            raise ValueError("recovery fence does not match current replay epoch")
        if to_epoch != from_epoch + 1:
            raise ValueError("recovery fence epoch is not contiguous")
        requested = _string_tuple(data["requested_action_ids"], "requested_action_ids")
        if requested != tuple(sorted(requested)) or len(set(requested)) != len(requested):
            raise ValueError("recovery fence requested_action_ids must be unique canonical order")
        expected = tuple(sorted(action_id for action_id, receipt in self._effect_receipts.items() if receipt.state == EffectState.REQUESTED))
        if requested != expected:
            raise ValueError("recovery fence requested_action_ids must exactly match current REQUESTED receipts")
        for action_id in requested:
            if self._effect_receipts[action_id].epoch != from_epoch:
                raise ValueError("recovery fence includes REQUESTED receipt from a different epoch")
        return from_epoch, to_epoch, requested

    def _apply_valid_recovery_fence(self, *, to_epoch: int, requested_action_ids: tuple[str, ...]) -> None:
        self._epoch = to_epoch
        for action_id in requested_action_ids:
            receipt = self._effect_receipts[action_id]
            self._effect_receipts[action_id] = replace(receipt, state=EffectState.UNRESOLVED_AFTER_RESTART, reason="OUTCOME_REQUIRES_RECONCILIATION")

    def _apply_event(self, *, event_type: str, data: dict[str, Any], event_epoch: int) -> None:
        if event_type != RECOVERY_FENCE_EVENT:
            return super()._apply_event(event_type=event_type, data=data, event_epoch=event_epoch)
        try:
            _, to_epoch, requested = self._validate_recovery_fence(data, event_epoch=event_epoch)
        except ValueError as exc:
            raise JournalIntegrityError(str(exc)) from exc
        self._apply_valid_recovery_fence(to_epoch=to_epoch, requested_action_ids=requested)

    def _advance_recovery_epoch(self) -> int:
        self._ensure_writable()
        from_epoch = self._epoch
        requested = tuple(sorted(action_id for action_id, receipt in self._effect_receipts.items() if receipt.state == EffectState.REQUESTED))
        data = {"from_epoch": from_epoch, "to_epoch": from_epoch + 1, "requested_action_ids": list(requested)}
        _, to_epoch, validated_requested = self._validate_recovery_fence(data, event_epoch=from_epoch)
        self._record(RECOVERY_FENCE_EVENT, data)
        self._apply_valid_recovery_fence(to_epoch=to_epoch, requested_action_ids=validated_requested)
        return self._epoch
