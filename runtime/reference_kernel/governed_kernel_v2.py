from __future__ import annotations

from dataclasses import replace
from typing import Any, Iterable, Optional, Tuple

from durable_kernel import DurableReferenceKernel, JournalIntegrityError
from hc_kernel import (
    AuthorityGrant,
    EffectState,
    ReferenceKernel,
    _string_tuple,
)


RECOVERY_FENCE_EVENT = "RECOVERY_FENCE"


def _normalize_authority_issuer_capabilities(
    registrations: Any,
) -> Tuple[Tuple[object, str], ...]:
    """Normalize host-registered opaque authority issuer handles.

    This is deliberately the same *kind* of narrow in-process capability
    boundary used by the R4 outcome-source repair. It does not claim
    cryptographic identity or process isolation.
    """

    if registrations is None:
        return ()
    entries = registrations.items() if hasattr(registrations, "items") else registrations
    normalized: list[tuple[object, str]] = []
    try:
        for entry in entries:
            capability, principal = entry
            if capability is None or isinstance(
                capability,
                (bool, int, float, complex, str, bytes, tuple, frozenset),
            ):
                raise ValueError(
                    "authority issuer capabilities must be opaque object handles"
                )
            if not isinstance(principal, str) or not principal:
                raise ValueError(
                    "authority issuer principal IDs must be non-empty strings"
                )
            if any(capability is prior for prior, _ in normalized):
                raise ValueError(
                    "authority issuer capability is registered more than once"
                )
            normalized.append((capability, principal))
    except (TypeError, ValueError) as exc:
        if isinstance(exc, ValueError):
            raise
        raise ValueError(
            "authority issuer capabilities must be iterable capability/principal pairs"
        ) from exc
    return tuple(normalized)


class _AuthorityIssuerBoundary:
    _authority_issuer_capabilities: Tuple[Tuple[object, str], ...]

    def _set_authority_issuer_capabilities(self, registrations: Any) -> None:
        self._authority_issuer_capabilities = _normalize_authority_issuer_capabilities(
            registrations
        )

    def _principal_for_authority_capability(
        self, source_capability: object
    ) -> Optional[str]:
        for capability, principal in self._authority_issuer_capabilities:
            if source_capability is capability:
                return principal
        return None

    def _require_authority_principal(self, source_capability: object) -> str:
        principal = self._principal_for_authority_capability(source_capability)
        if principal is None:
            raise ValueError("authority issuer capability is not registered")
        return principal


class GovernedReferenceKernelV2(_AuthorityIssuerBoundary, ReferenceKernel):
    """ReferenceKernel with capability-authenticated authority mutation.

    The capability authenticates the in-process principal identity used by this
    narrow reference slice. It does not by itself prove that the principal has
    unrestricted jurisdiction to mint every possible grant class/scope.
    """

    def __init__(
        self,
        *,
        authority_issuer_capabilities: Any = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._set_authority_issuer_capabilities(authority_issuer_capabilities)

    def register_grant(
        self,
        *,
        source_capability: object,
        grantee: str,
        action_scope: str,
        target_scope: str,
        basis_refs: Iterable[str],
        valid_from,
        expires_at,
        provenance: Iterable[str] = (),
    ) -> AuthorityGrant:
        principal = self._require_authority_principal(source_capability)
        return ReferenceKernel.register_grant(
            self,
            grantor=principal,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis_refs,
            valid_from=valid_from,
            expires_at=expires_at,
            provenance=provenance,
        )

    def revoke_grant(
        self,
        grant_id: str,
        *,
        source_capability: object,
        revoked_at=None,
    ) -> None:
        principal = self._require_authority_principal(source_capability)
        grant = self._authority_grants[grant_id]
        if principal != grant.grantor:
            raise ValueError("authority revoker does not own this grant")
        ReferenceKernel.revoke_grant(
            self,
            grant_id,
            revoked_at=revoked_at,
        )


class GovernedDurableReferenceKernelV2(_AuthorityIssuerBoundary, DurableReferenceKernel):
    """Durable V2 slice with governed authority mutation and atomic recovery fence."""

    def __init__(
        self,
        journal_path,
        *,
        authority_issuer_capabilities: Any = None,
        **kwargs: Any,
    ) -> None:
        # `_load_existing()` may call our overridden recovery path through the
        # base constructor, but recovery fencing itself does not depend on live
        # issuer handles. Register those handles after durable reconstruction.
        self._authority_issuer_capabilities = ()
        super().__init__(journal_path, **kwargs)
        self._set_authority_issuer_capabilities(authority_issuer_capabilities)

    def register_grant(
        self,
        *,
        source_capability: object,
        grantee: str,
        action_scope: str,
        target_scope: str,
        basis_refs: Iterable[str],
        valid_from,
        expires_at,
        provenance: Iterable[str] = (),
    ) -> AuthorityGrant:
        self._ensure_writable()
        principal = self._require_authority_principal(source_capability)
        grant = ReferenceKernel.register_grant(
            self,
            grantor=principal,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis_refs,
            valid_from=valid_from,
            expires_at=expires_at,
            provenance=provenance,
        )
        try:
            self._record("AUTHORITY_GRANT_UPSERT", self._grant_data(grant))
        except Exception:
            self._authority_grants.pop(grant.grant_id, None)
            raise
        return grant

    def revoke_grant(
        self,
        grant_id: str,
        *,
        source_capability: object,
        revoked_at=None,
    ) -> None:
        self._ensure_writable()
        principal = self._require_authority_principal(source_capability)
        previous = self._authority_grants[grant_id]
        if principal != previous.grantor:
            raise ValueError("authority revoker does not own this grant")
        ReferenceKernel.revoke_grant(
            self,
            grant_id,
            revoked_at=revoked_at,
        )
        updated = self._authority_grants[grant_id]
        if updated == previous:
            return
        try:
            self._record("AUTHORITY_GRANT_UPSERT", self._grant_data(updated))
        except Exception:
            self._authority_grants[grant_id] = previous
            raise

    def _validate_recovery_fence(
        self,
        data: dict[str, Any],
        *,
        event_epoch: int,
    ) -> tuple[int, int, tuple[str, ...]]:
        required = {"from_epoch", "to_epoch", "requested_action_ids"}
        if set(data) != required:
            raise ValueError("recovery fence has unexpected/missing fields")

        from_epoch = data["from_epoch"]
        to_epoch = data["to_epoch"]
        if type(from_epoch) is not int or type(to_epoch) is not int:
            raise ValueError("recovery fence epochs must be integers")
        if event_epoch != from_epoch or self._epoch != from_epoch:
            raise ValueError("recovery fence does not match current replay epoch")
        if to_epoch != from_epoch + 1:
            raise ValueError("recovery fence epoch is not contiguous")

        requested = _string_tuple(
            data["requested_action_ids"], "requested_action_ids"
        )
        if requested != tuple(sorted(requested)) or len(set(requested)) != len(requested):
            raise ValueError(
                "recovery fence requested_action_ids must be unique canonical order"
            )

        expected = tuple(
            sorted(
                action_id
                for action_id, receipt in self._effect_receipts.items()
                if receipt.state == EffectState.REQUESTED
            )
        )
        if requested != expected:
            raise ValueError(
                "recovery fence requested_action_ids must exactly match current REQUESTED receipts"
            )

        for action_id in requested:
            receipt = self._effect_receipts[action_id]
            if receipt.epoch != from_epoch:
                raise ValueError(
                    "recovery fence includes REQUESTED receipt from a different epoch"
                )
        return from_epoch, to_epoch, requested

    def _apply_valid_recovery_fence(
        self,
        *,
        to_epoch: int,
        requested_action_ids: tuple[str, ...],
    ) -> None:
        self._epoch = to_epoch
        for action_id in requested_action_ids:
            receipt = self._effect_receipts[action_id]
            self._effect_receipts[action_id] = replace(
                receipt,
                state=EffectState.UNRESOLVED_AFTER_RESTART,
                reason="OUTCOME_REQUIRES_RECONCILIATION",
            )

    def _apply_event(
        self,
        *,
        event_type: str,
        data: dict[str, Any],
        event_epoch: int,
    ) -> None:
        if event_type != RECOVERY_FENCE_EVENT:
            return super()._apply_event(
                event_type=event_type,
                data=data,
                event_epoch=event_epoch,
            )
        try:
            _, to_epoch, requested = self._validate_recovery_fence(
                data,
                event_epoch=event_epoch,
            )
        except ValueError as exc:
            raise JournalIntegrityError(str(exc)) from exc
        self._apply_valid_recovery_fence(
            to_epoch=to_epoch,
            requested_action_ids=requested,
        )

    def _advance_recovery_epoch(self) -> int:
        self._ensure_writable()
        from_epoch = self._epoch
        requested = tuple(
            sorted(
                action_id
                for action_id, receipt in self._effect_receipts.items()
                if receipt.state == EffectState.REQUESTED
            )
        )
        data = {
            "from_epoch": from_epoch,
            "to_epoch": from_epoch + 1,
            "requested_action_ids": list(requested),
        }
        _, to_epoch, validated_requested = self._validate_recovery_fence(
            data,
            event_epoch=from_epoch,
        )

        # Durability precedes in-memory semantic promotion. If `_record` fails,
        # the current epoch and receipts remain unchanged.
        self._record(RECOVERY_FENCE_EVENT, data)
        self._apply_valid_recovery_fence(
            to_epoch=to_epoch,
            requested_action_ids=validated_requested,
        )
        return self._epoch
