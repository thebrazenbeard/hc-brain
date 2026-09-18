from __future__ import annotations

import hashlib
import json
import math
import uuid
from collections.abc import Mapping as ABCMapping
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import Enum
from types import MappingProxyType
from typing import Any, Callable, Dict, Iterable, Mapping, Optional, Tuple


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def _freeze_payload(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("reference-kernel payload must contain finite numbers")
        return value
    if isinstance(value, ABCMapping):
        frozen = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError("reference-kernel mapping keys must be strings")
            frozen[key] = _freeze_payload(item)
        return MappingProxyType(
            frozen
        )
    if isinstance(value, (list, tuple)):
        return tuple(_freeze_payload(item) for item in value)
    raise ValueError("reference-kernel payload must be JSON-like immutable data")


def _jsonable_payload(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("reference-kernel payload must contain finite numbers")
        return value
    if isinstance(value, ABCMapping):
        result = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError("reference-kernel mapping keys must be strings")
            result[key] = _jsonable_payload(item)
        return result
    if isinstance(value, (list, tuple)):
        return [_jsonable_payload(item) for item in value]
    raise ValueError("reference-kernel payload must be JSON-like immutable data")


def _require_aware(value: datetime, label: str) -> datetime:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{label} must be timezone-aware")
    return value


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a string")
    return value


def _optional_string(value: Any, label: str) -> Optional[str]:
    if value is None:
        return None
    return _require_string(value, label)


def _string_tuple(values: Iterable[Any], label: str) -> Tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{label} must be an iterable of strings")
    try:
        result = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{label} must be an iterable of strings") from exc
    if any(not isinstance(item, str) for item in result):
        raise ValueError(f"{label} must contain only strings")
    return result


def _logical_key(value: Iterable[Any]) -> Tuple[str, str, str, str]:
    result = _string_tuple(value, "logical_key")
    if len(result) != 4:
        raise ValueError("logical_key must contain exactly four string components")
    return result  # type: ignore[return-value]


def _normalize_outcome_source_capabilities(
    registrations: Any,
) -> Tuple[Tuple[object, str], ...]:
    if registrations is None:
        return ()
    entries = (
        registrations.items()
        if isinstance(registrations, ABCMapping)
        else registrations
    )
    normalized = []
    try:
        for entry in entries:
            capability, producer = entry
            if capability is None or isinstance(
                capability,
                (bool, int, float, complex, str, bytes, tuple, frozenset),
            ):
                raise ValueError(
                    "outcome source capabilities must be opaque object handles"
                )
            if not isinstance(producer, str) or not producer:
                raise ValueError("outcome source producer IDs must be non-empty strings")
            if any(capability is prior_capability for prior_capability, _ in normalized):
                raise ValueError("outcome source capability is registered more than once")
            normalized.append((capability, producer))
    except (TypeError, ValueError) as exc:
        if isinstance(exc, ValueError):
            raise
        raise ValueError(
            "outcome source capabilities must be iterable capability/producer pairs"
        ) from exc
    return tuple(normalized)


def _candidate_fingerprint(candidate: "EffectCandidate") -> str:
    _require_string(candidate.action_id, "candidate.action_id")
    _require_string(candidate.origin, "candidate.origin")
    _require_string(candidate.action_scope, "candidate.action_scope")
    _require_string(candidate.target_scope, "candidate.target_scope")
    authority_grant_id = _optional_string(
        candidate.authority_grant_id, "candidate.authority_grant_id"
    )
    parent_ids = _string_tuple(candidate.parent_ids, "candidate.parent_ids")
    body = {
        "origin": candidate.origin,
        "action_scope": candidate.action_scope,
        "target_scope": candidate.target_scope,
        "payload": _jsonable_payload(candidate.payload),
        "authority_grant_id": authority_grant_id,
        "planned_epoch": candidate.planned_epoch,
        "parent_ids": list(parent_ids),
    }
    try:
        encoded = json.dumps(
            body,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("effect candidate must be canonically JSON-serializable") from exc
    return hashlib.sha256(encoded).hexdigest()


class EpistemicClass(str, Enum):
    OBSERVATION = "OBSERVATION"
    DERIVED = "DERIVED"
    INFERRED = "INFERRED"
    PREDICTION = "PREDICTION"


class ProjectionStatus(str, Enum):
    MISSING = "MISSING"
    CURRENT = "CURRENT"
    AMBIGUOUS = "AMBIGUOUS"


class EffectState(str, Enum):
    BLOCKED = "BLOCKED"
    REQUESTED = "REQUESTED"
    CONFIRMED = "CONFIRMED"
    FAILED_CONFIRMED = "FAILED_CONFIRMED"
    UNRESOLVED_AFTER_RESTART = "UNRESOLVED_AFTER_RESTART"


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    producer: str
    epistemic_class: EpistemicClass
    payload: Any
    event_time: datetime
    record_time: datetime
    parent_ids: Tuple[str, ...] = ()
    source_refs: Tuple[str, ...] = ()
    influence_roles: Tuple[str, ...] = ()
    effect_action_id: Optional[str] = None


@dataclass(frozen=True)
class RoutedEvent:
    event_id: str
    source: str
    audience: str
    payload: Any
    priority: int
    parent_ids: Tuple[str, ...] = ()
    authority_ref: Optional[str] = None


@dataclass(frozen=True)
class MemoryRecord:
    record_id: str
    logical_key: Tuple[str, str, str, str]
    payload: Any
    epistemic_class: EpistemicClass
    supersedes: Tuple[str, ...] = ()
    source_refs: Tuple[str, ...] = ()


@dataclass(frozen=True)
class CurrentProjection:
    status: ProjectionStatus
    logical_key: Tuple[str, str, str, str]
    head_ids: Tuple[str, ...]
    payload: Any = None
    epistemic_class: Optional[EpistemicClass] = None
    source_refs: Tuple[str, ...] = ()


@dataclass(frozen=True)
class AuthorityGrant:
    grant_id: str
    grantor: str
    grantee: str
    action_scope: str
    target_scope: str
    basis_refs: Tuple[str, ...]
    provenance: Tuple[str, ...]
    issued_epoch: int
    valid_from: datetime
    expires_at: datetime
    revoked_at: Optional[datetime] = None

    def allows(
        self,
        *,
        grantee: str,
        action_scope: str,
        target_scope: str,
        now: datetime,
        current_epoch: int,
    ) -> Tuple[bool, str]:
        if self.issued_epoch != current_epoch:
            return False, "STALE_AUTHORITY_EPOCH"
        if self.revoked_at is not None and self.revoked_at <= now:
            return False, "REVOKED_AUTHORITY"
        if now < self.valid_from:
            return False, "AUTHORITY_NOT_YET_VALID"
        if now >= self.expires_at:
            return False, "EXPIRED_AUTHORITY"
        if self.grantee != grantee:
            return False, "GRANTEE_SCOPE_MISMATCH"
        if self.action_scope != action_scope:
            return False, "ACTION_SCOPE_MISMATCH"
        if self.target_scope != target_scope:
            return False, "TARGET_SCOPE_MISMATCH"
        return True, "AUTHORIZED"


@dataclass(frozen=True)
class EffectCandidate:
    action_id: str
    origin: str
    action_scope: str
    target_scope: str
    payload: Any
    authority_grant_id: Optional[str]
    planned_epoch: int
    parent_ids: Tuple[str, ...] = ()


@dataclass(frozen=True)
class EffectReceipt:
    action_id: str
    state: EffectState
    reason: str
    epoch: int
    authority_grant_id: Optional[str]
    candidate_fingerprint: Optional[str] = None
    dispatch_attempts: int = 0
    confirmation_evidence_id: Optional[str] = None


class CurrentMemory:
    """Append-oriented current-state projection with explicit supersession."""

    def __init__(self) -> None:
        self._records: Dict[str, MemoryRecord] = {}

    @property
    def records(self) -> Dict[str, MemoryRecord]:
        return dict(self._records)

    def append(
        self,
        *,
        logical_key: Tuple[str, str, str, str],
        payload: Any,
        epistemic_class: EpistemicClass,
        supersedes: Iterable[str] = (),
        source_refs: Iterable[str] = (),
    ) -> MemoryRecord:
        logical_key = _logical_key(logical_key)
        supersedes_tuple = tuple(
            dict.fromkeys(_string_tuple(supersedes, "supersedes"))
        )
        source_refs_tuple = _string_tuple(source_refs, "source_refs")
        for record_id in supersedes_tuple:
            prior = self._records.get(record_id)
            if prior is None:
                raise ValueError(f"unknown superseded record: {record_id}")
            if prior.logical_key != logical_key:
                raise ValueError("supersession cannot cross logical record scope")

        record = MemoryRecord(
            record_id=_id("mem"),
            logical_key=logical_key,
            payload=_freeze_payload(payload),
            epistemic_class=epistemic_class,
            supersedes=supersedes_tuple,
            source_refs=source_refs_tuple,
        )
        self._records[record.record_id] = record
        return record

    def current(self, logical_key: Tuple[str, str, str, str]) -> CurrentProjection:
        logical_key = _logical_key(logical_key)
        scoped = [r for r in self._records.values() if r.logical_key == logical_key]
        if not scoped:
            return CurrentProjection(
                status=ProjectionStatus.MISSING,
                logical_key=logical_key,
                head_ids=(),
            )

        superseded = {
            predecessor
            for record in scoped
            for predecessor in record.supersedes
        }
        heads = [r for r in scoped if r.record_id not in superseded]
        head_ids = tuple(sorted(r.record_id for r in heads))
        if len(heads) != 1:
            return CurrentProjection(
                status=ProjectionStatus.AMBIGUOUS,
                logical_key=logical_key,
                head_ids=head_ids,
            )
        head = heads[0]
        return CurrentProjection(
            status=ProjectionStatus.CURRENT,
            logical_key=logical_key,
            head_ids=head_ids,
            payload=head.payload,
            epistemic_class=head.epistemic_class,
            source_refs=head.source_refs,
        )


class ReferenceKernel:
    """Minimal executable invariant kernel, not a cognition engine."""

    def __init__(
        self,
        *,
        clock: Optional[Callable[[], datetime]] = None,
        outcome_source_validator: Optional[Callable[[str, AuthorityGrant], bool]] = None,
        outcome_source_capabilities: Any = None,
    ) -> None:
        self._epoch = 0
        self._evidence: Dict[str, EvidenceRecord] = {}
        self._routed_events: Dict[str, RoutedEvent] = {}
        self._incorporated_event_ids: set[str] = set()
        self.memory = CurrentMemory()
        self._authority_grants: Dict[str, AuthorityGrant] = {}
        self._effect_receipts: Dict[str, EffectReceipt] = {}
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self._outcome_source_validator = outcome_source_validator
        self._outcome_source_capabilities = _normalize_outcome_source_capabilities(
            outcome_source_capabilities
        )

    @property
    def epoch(self) -> int:
        return self._epoch

    @property
    def evidence(self) -> Mapping[str, EvidenceRecord]:
        return MappingProxyType(self._evidence)

    @property
    def routed_events(self) -> Mapping[str, RoutedEvent]:
        return MappingProxyType(self._routed_events)

    @property
    def incorporated_event_ids(self) -> frozenset[str]:
        return frozenset(self._incorporated_event_ids)

    @property
    def authority_grants(self) -> Mapping[str, AuthorityGrant]:
        return MappingProxyType(self._authority_grants)

    @property
    def effect_receipts(self) -> Mapping[str, EffectReceipt]:
        return MappingProxyType(self._effect_receipts)

    def now(self) -> datetime:
        return _require_aware(self._clock(), "kernel clock")

    def _producer_for_source_capability(self, source_capability: object) -> Optional[str]:
        for capability, producer in self._outcome_source_capabilities:
            if source_capability is capability:
                return producer
        return None

    def observe(
        self,
        *,
        producer: str,
        payload: Any,
        event_time: Optional[datetime] = None,
        source_refs: Iterable[str] = (),
        effect_action_id: Optional[str] = None,
    ) -> EvidenceRecord:
        if effect_action_id is not None:
            raise ValueError(
                "generic observations cannot bind effect outcomes; "
                "use observe_effect_outcome"
            )
        return self._observe_record(
            producer=producer,
            payload=payload,
            event_time=event_time,
            source_refs=source_refs,
        )

    def _observe_record(
        self,
        *,
        producer: str,
        payload: Any,
        event_time: Optional[datetime] = None,
        source_refs: Iterable[str] = (),
        effect_action_id: Optional[str] = None,
    ) -> EvidenceRecord:
        producer = _require_string(producer, "producer")
        source_refs_tuple = _string_tuple(source_refs, "source_refs")
        effect_action_id = _optional_string(effect_action_id, "effect_action_id")
        if effect_action_id is not None and effect_action_id not in self._effect_receipts:
            raise ValueError("effect-linked observation references unknown action")
        now = self.now()
        if event_time is not None:
            _require_aware(event_time, "event_time")
        record = EvidenceRecord(
            evidence_id=_id("ev"),
            producer=producer,
            epistemic_class=EpistemicClass.OBSERVATION,
            payload=_freeze_payload(payload),
            event_time=event_time or now,
            record_time=now,
            source_refs=source_refs_tuple,
            effect_action_id=effect_action_id,
        )
        self._evidence[record.evidence_id] = record
        return record

    def observe_effect_outcome(
        self,
        *,
        source_capability: object,
        payload: Any,
        effect_action_id: str,
        event_time: Optional[datetime] = None,
        source_refs: Iterable[str] = (),
    ) -> EvidenceRecord:
        producer = self._producer_for_source_capability(source_capability)
        if producer is None:
            raise ValueError("effect outcome source capability is not registered")
        receipt = self._effect_receipts.get(effect_action_id)
        if receipt is None:
            raise ValueError("effect-linked observation references unknown action")
        if receipt.state not in {
            EffectState.REQUESTED,
            EffectState.UNRESOLVED_AFTER_RESTART,
        }:
            raise ValueError("effect outcome cannot bind to the current effect state")
        grant = self._authority_grants.get(receipt.authority_grant_id)
        if grant is None:
            raise ValueError("effect outcome references unknown authority")
        validator = self._outcome_source_validator
        if validator is None or not validator(producer, grant):
            raise ValueError("effect outcome source is not trusted")
        return self._observe_record(
            producer=producer,
            payload=payload,
            event_time=event_time,
            source_refs=source_refs,
            effect_action_id=effect_action_id,
        )

    def derive(
        self,
        *,
        producer: str,
        epistemic_class: EpistemicClass,
        payload: Any,
        parent_ids: Iterable[str],
        influence_roles: Iterable[str] = (),
        source_refs: Iterable[str] = (),
    ) -> EvidenceRecord:
        if epistemic_class == EpistemicClass.OBSERVATION:
            raise ValueError("derived state cannot be relabeled as raw observation")
        producer = _require_string(producer, "producer")
        parents = _string_tuple(parent_ids, "parent_ids")
        influence_roles_tuple = _string_tuple(influence_roles, "influence_roles")
        source_refs_tuple = _string_tuple(source_refs, "source_refs")
        if not parents:
            raise ValueError("derived state requires at least one causal parent")
        missing = [parent for parent in parents if parent not in self._evidence]
        if missing:
            raise ValueError(f"unknown causal parents: {missing}")
        inherited_sources = []
        for parent in parents:
            inherited_sources.extend(self._evidence[parent].source_refs)
        combined_sources = tuple(
            dict.fromkeys((*inherited_sources, *source_refs_tuple))
        )
        now = self.now()
        record = EvidenceRecord(
            evidence_id=_id("ev"),
            producer=producer,
            epistemic_class=epistemic_class,
            payload=_freeze_payload(payload),
            event_time=now,
            record_time=now,
            parent_ids=parents,
            source_refs=combined_sources,
            influence_roles=influence_roles_tuple,
        )
        self._evidence[record.evidence_id] = record
        return record

    def route(
        self,
        *,
        source: str,
        audience: str,
        payload: Any,
        priority: int = 0,
        parent_ids: Iterable[str] = (),
        authority_ref: Optional[str] = None,
    ) -> RoutedEvent:
        source = _require_string(source, "route.source")
        audience = _require_string(audience, "route.audience")
        parent_ids_tuple = _string_tuple(parent_ids, "route.parent_ids")
        authority_ref = _optional_string(authority_ref, "route.authority_ref")
        event = RoutedEvent(
            event_id=_id("route"),
            source=source,
            audience=audience,
            payload=_freeze_payload(payload),
            priority=priority,
            parent_ids=parent_ids_tuple,
            authority_ref=authority_ref,
        )
        self._routed_events[event.event_id] = event
        return event

    def incorporate_routed_event(self, event_id: str) -> None:
        event_id = _require_string(event_id, "event_id")
        if event_id not in self._routed_events:
            raise ValueError(f"unknown routed event: {event_id}")
        self._incorporated_event_ids.add(event_id)

    def register_grant(
        self,
        *,
        grantor: str,
        grantee: str,
        action_scope: str,
        target_scope: str,
        basis_refs: Iterable[str],
        valid_from: datetime,
        expires_at: datetime,
        provenance: Iterable[str] = (),
    ) -> AuthorityGrant:
        grantor = _require_string(grantor, "grantor")
        grantee = _require_string(grantee, "grantee")
        action_scope = _require_string(action_scope, "action_scope")
        target_scope = _require_string(target_scope, "target_scope")
        basis = _string_tuple(basis_refs, "basis_refs")
        provenance_tuple = _string_tuple(provenance, "provenance")
        if not basis:
            raise ValueError("authority registration requires an explicit basis reference")
        _require_aware(valid_from, "valid_from")
        _require_aware(expires_at, "expires_at")
        if expires_at <= valid_from:
            raise ValueError("grant expiry must follow valid_from")
        grant = AuthorityGrant(
            grant_id=_id("grant"),
            grantor=grantor,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis,
            provenance=provenance_tuple,
            issued_epoch=self._epoch,
            valid_from=valid_from,
            expires_at=expires_at,
        )
        self._authority_grants[grant.grant_id] = grant
        return grant

    def revoke_grant(
        self,
        grant_id: str,
        *,
        revoked_at: Optional[datetime] = None,
    ) -> None:
        grant_id = _require_string(grant_id, "grant_id")
        grant = self._authority_grants[grant_id]
        when = revoked_at or self.now()
        _require_aware(when, "revoked_at")
        if grant.revoked_at is not None:
            if grant.revoked_at != when:
                raise ValueError("authority revocation is immutable once set")
            return
        self._authority_grants[grant_id] = replace(grant, revoked_at=when)

    def plan_effect(
        self,
        *,
        origin: str,
        action_scope: str,
        target_scope: str,
        payload: Any,
        authority_grant_id: Optional[str],
        parent_ids: Iterable[str] = (),
    ) -> EffectCandidate:
        origin = _require_string(origin, "origin")
        action_scope = _require_string(action_scope, "action_scope")
        target_scope = _require_string(target_scope, "target_scope")
        authority_grant_id = _optional_string(
            authority_grant_id, "authority_grant_id"
        )
        parent_ids_tuple = _string_tuple(parent_ids, "parent_ids")
        return EffectCandidate(
            action_id=_id("action"),
            origin=origin,
            action_scope=action_scope,
            target_scope=target_scope,
            payload=_freeze_payload(payload),
            authority_grant_id=authority_grant_id,
            planned_epoch=self._epoch,
            parent_ids=parent_ids_tuple,
        )

    def request_effect(self, candidate: EffectCandidate) -> EffectReceipt:
        fingerprint = _candidate_fingerprint(candidate)
        existing = self._effect_receipts.get(candidate.action_id)
        if existing is not None:
            if existing.candidate_fingerprint != fingerprint:
                raise ValueError("action_id collision with different candidate semantics")
            return existing

        current_time = self.now()
        if candidate.planned_epoch != self._epoch:
            receipt = EffectReceipt(
                action_id=candidate.action_id,
                state=EffectState.BLOCKED,
                reason="STALE_PLAN_EPOCH",
                epoch=self._epoch,
                authority_grant_id=candidate.authority_grant_id,
                candidate_fingerprint=fingerprint,
            )
            self._effect_receipts[candidate.action_id] = receipt
            return receipt
        if candidate.authority_grant_id is None:
            receipt = EffectReceipt(
                action_id=candidate.action_id,
                state=EffectState.BLOCKED,
                reason="MISSING_AUTHORITY",
                epoch=self._epoch,
                authority_grant_id=None,
                candidate_fingerprint=fingerprint,
            )
            self._effect_receipts[candidate.action_id] = receipt
            return receipt
        grant = self._authority_grants.get(candidate.authority_grant_id)
        if grant is None:
            receipt = EffectReceipt(
                action_id=candidate.action_id,
                state=EffectState.BLOCKED,
                reason="UNKNOWN_AUTHORITY",
                epoch=self._epoch,
                authority_grant_id=candidate.authority_grant_id,
                candidate_fingerprint=fingerprint,
            )
            self._effect_receipts[candidate.action_id] = receipt
            return receipt
        allowed, reason = grant.allows(
            grantee=candidate.origin,
            action_scope=candidate.action_scope,
            target_scope=candidate.target_scope,
            now=current_time,
            current_epoch=self._epoch,
        )
        receipt = EffectReceipt(
            action_id=candidate.action_id,
            state=EffectState.REQUESTED if allowed else EffectState.BLOCKED,
            reason=reason,
            epoch=self._epoch,
            authority_grant_id=candidate.authority_grant_id,
            candidate_fingerprint=fingerprint,
            dispatch_attempts=1 if allowed else 0,
        )
        self._effect_receipts[candidate.action_id] = receipt
        return receipt

    def _confirmation_observation(
        self,
        action_id: str,
        confirmation_evidence_id: str,
    ) -> EvidenceRecord:
        evidence = self._evidence.get(confirmation_evidence_id)
        if evidence is None:
            raise ValueError("unknown confirmation evidence")
        if evidence.epistemic_class != EpistemicClass.OBSERVATION:
            raise ValueError("reference kernel requires observed outcome evidence")
        if evidence.effect_action_id != action_id:
            raise ValueError("confirmation evidence is not bound to this action")
        return evidence

    def confirm_effect(
        self,
        action_id: str,
        *,
        succeeded: bool,
        confirmation_evidence_id: str,
    ) -> EffectReceipt:
        receipt = self._effect_receipts[action_id]
        if receipt.state != EffectState.REQUESTED:
            raise ValueError("only a requested effect can be confirmed")
        self._confirmation_observation(action_id, confirmation_evidence_id)
        result = replace(
            receipt,
            state=(EffectState.CONFIRMED if succeeded else EffectState.FAILED_CONFIRMED),
            reason=("EFFECT_CONFIRMED" if succeeded else "EFFECT_FAILURE_CONFIRMED"),
            confirmation_evidence_id=confirmation_evidence_id,
        )
        self._effect_receipts[action_id] = result
        return result

    def restart(self) -> int:
        self._epoch += 1
        for action_id, receipt in list(self._effect_receipts.items()):
            if receipt.state == EffectState.REQUESTED:
                self._effect_receipts[action_id] = replace(
                    receipt,
                    state=EffectState.UNRESOLVED_AFTER_RESTART,
                    reason="OUTCOME_REQUIRES_RECONCILIATION",
                )
        return self._epoch

    def reconcile_after_restart(
        self,
        action_id: str,
        *,
        confirmed_outcome: Optional[bool],
        confirmation_evidence_id: Optional[str] = None,
    ) -> EffectReceipt:
        receipt = self._effect_receipts[action_id]
        if receipt.state != EffectState.UNRESOLVED_AFTER_RESTART:
            raise ValueError("effect is not unresolved after restart")
        if confirmed_outcome is None:
            return receipt
        if confirmation_evidence_id is None:
            raise ValueError("confirmed reconciliation requires outcome evidence")
        self._confirmation_observation(action_id, confirmation_evidence_id)
        result = replace(
            receipt,
            state=(
                EffectState.CONFIRMED
                if confirmed_outcome
                else EffectState.FAILED_CONFIRMED
            ),
            reason=(
                "EFFECT_CONFIRMED_AFTER_RECONCILIATION"
                if confirmed_outcome
                else "EFFECT_FAILURE_CONFIRMED_AFTER_RECONCILIATION"
            ),
            confirmation_evidence_id=confirmation_evidence_id,
        )
        self._effect_receipts[action_id] = result
        return result
