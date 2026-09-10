from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, Iterable, Optional, Tuple
import uuid


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


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


@dataclass
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


@dataclass
class EffectReceipt:
    action_id: str
    state: EffectState
    reason: str
    epoch: int
    authority_grant_id: Optional[str]
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
        supersedes_tuple = tuple(dict.fromkeys(supersedes))
        for record_id in supersedes_tuple:
            prior = self._records.get(record_id)
            if prior is None:
                raise ValueError(f"unknown superseded record: {record_id}")
            if prior.logical_key != logical_key:
                raise ValueError("supersession cannot cross logical record scope")

        record = MemoryRecord(
            record_id=_id("mem"),
            logical_key=logical_key,
            payload=payload,
            epistemic_class=epistemic_class,
            supersedes=supersedes_tuple,
            source_refs=tuple(source_refs),
        )
        self._records[record.record_id] = record
        return record

    def current(self, logical_key: Tuple[str, str, str, str]) -> CurrentProjection:
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
        return CurrentProjection(
            status=ProjectionStatus.CURRENT,
            logical_key=logical_key,
            head_ids=head_ids,
            payload=heads[0].payload,
        )


class ReferenceKernel:
    """Minimal executable invariant kernel, not a cognition engine."""

    def __init__(self) -> None:
        self.epoch = 0
        self.evidence: Dict[str, EvidenceRecord] = {}
        self.routed_events: Dict[str, RoutedEvent] = {}
        self.incorporated_event_ids: set[str] = set()
        self.memory = CurrentMemory()
        self.authority_grants: Dict[str, AuthorityGrant] = {}
        self.effect_receipts: Dict[str, EffectReceipt] = {}

    @staticmethod
    def now() -> datetime:
        return datetime.now(timezone.utc)

    def observe(
        self,
        *,
        producer: str,
        payload: Any,
        event_time: Optional[datetime] = None,
        source_refs: Iterable[str] = (),
        effect_action_id: Optional[str] = None,
    ) -> EvidenceRecord:
        if (
            effect_action_id is not None
            and effect_action_id not in self.effect_receipts
        ):
            raise ValueError("effect-linked observation references unknown action")
        now = self.now()
        record = EvidenceRecord(
            evidence_id=_id("ev"),
            producer=producer,
            epistemic_class=EpistemicClass.OBSERVATION,
            payload=payload,
            event_time=event_time or now,
            record_time=now,
            source_refs=tuple(source_refs),
            effect_action_id=effect_action_id,
        )
        self.evidence[record.evidence_id] = record
        return record

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

        parents = tuple(parent_ids)
        if not parents:
            raise ValueError("derived state requires at least one causal parent")
        missing = [parent for parent in parents if parent not in self.evidence]
        if missing:
            raise ValueError(f"unknown causal parents: {missing}")

        inherited_sources = []
        for parent in parents:
            inherited_sources.extend(self.evidence[parent].source_refs)
        combined_sources = tuple(dict.fromkeys((*inherited_sources, *source_refs)))
        now = self.now()
        record = EvidenceRecord(
            evidence_id=_id("ev"),
            producer=producer,
            epistemic_class=epistemic_class,
            payload=payload,
            event_time=now,
            record_time=now,
            parent_ids=parents,
            source_refs=combined_sources,
            influence_roles=tuple(influence_roles),
        )
        self.evidence[record.evidence_id] = record
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
        event = RoutedEvent(
            event_id=_id("route"),
            source=source,
            audience=audience,
            payload=payload,
            priority=priority,
            parent_ids=tuple(parent_ids),
            authority_ref=authority_ref,
        )
        self.routed_events[event.event_id] = event
        return event

    def incorporate_routed_event(self, event_id: str) -> None:
        if event_id not in self.routed_events:
            raise ValueError(f"unknown routed event: {event_id}")
        self.incorporated_event_ids.add(event_id)

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
        basis = tuple(basis_refs)
        if not basis:
            raise ValueError("authority registration requires an explicit basis reference")
        if expires_at <= valid_from:
            raise ValueError("grant expiry must follow valid_from")
        grant = AuthorityGrant(
            grant_id=_id("grant"),
            grantor=grantor,
            grantee=grantee,
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=basis,
            provenance=tuple(provenance),
            issued_epoch=self.epoch,
            valid_from=valid_from,
            expires_at=expires_at,
        )
        self.authority_grants[grant.grant_id] = grant
        return grant

    def revoke_grant(
        self,
        grant_id: str,
        *,
        revoked_at: Optional[datetime] = None,
    ) -> None:
        grant = self.authority_grants[grant_id]
        grant.revoked_at = revoked_at or self.now()

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
        return EffectCandidate(
            action_id=_id("action"),
            origin=origin,
            action_scope=action_scope,
            target_scope=target_scope,
            payload=payload,
            authority_grant_id=authority_grant_id,
            planned_epoch=self.epoch,
            parent_ids=tuple(parent_ids),
        )

    def request_effect(
        self,
        candidate: EffectCandidate,
        *,
        now: Optional[datetime] = None,
    ) -> EffectReceipt:
        existing = self.effect_receipts.get(candidate.action_id)
        if existing is not None:
            return existing

        current_time = now or self.now()

        if candidate.planned_epoch != self.epoch:
            receipt = EffectReceipt(
                action_id=candidate.action_id,
                state=EffectState.BLOCKED,
                reason="STALE_PLAN_EPOCH",
                epoch=self.epoch,
                authority_grant_id=candidate.authority_grant_id,
            )
            self.effect_receipts[candidate.action_id] = receipt
            return receipt

        if candidate.authority_grant_id is None:
            receipt = EffectReceipt(
                action_id=candidate.action_id,
                state=EffectState.BLOCKED,
                reason="MISSING_AUTHORITY",
                epoch=self.epoch,
                authority_grant_id=None,
            )
            self.effect_receipts[candidate.action_id] = receipt
            return receipt

        grant = self.authority_grants.get(candidate.authority_grant_id)
        if grant is None:
            receipt = EffectReceipt(
                action_id=candidate.action_id,
                state=EffectState.BLOCKED,
                reason="UNKNOWN_AUTHORITY",
                epoch=self.epoch,
                authority_grant_id=candidate.authority_grant_id,
            )
            self.effect_receipts[candidate.action_id] = receipt
            return receipt

        allowed, reason = grant.allows(
            grantee=candidate.origin,
            action_scope=candidate.action_scope,
            target_scope=candidate.target_scope,
            now=current_time,
            current_epoch=self.epoch,
        )
        receipt = EffectReceipt(
            action_id=candidate.action_id,
            state=EffectState.REQUESTED if allowed else EffectState.BLOCKED,
            reason=reason,
            epoch=self.epoch,
            authority_grant_id=candidate.authority_grant_id,
            dispatch_attempts=1 if allowed else 0,
        )
        self.effect_receipts[candidate.action_id] = receipt
        return receipt

    def _confirmation_observation(
        self,
        action_id: str,
        confirmation_evidence_id: str,
    ) -> EvidenceRecord:
        evidence = self.evidence.get(confirmation_evidence_id)
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
        receipt = self.effect_receipts[action_id]
        if receipt.state != EffectState.REQUESTED:
            raise ValueError("only a requested effect can be confirmed")
        self._confirmation_observation(action_id, confirmation_evidence_id)
        receipt.state = (
            EffectState.CONFIRMED if succeeded else EffectState.FAILED_CONFIRMED
        )
        receipt.reason = (
            "EFFECT_CONFIRMED" if succeeded else "EFFECT_FAILURE_CONFIRMED"
        )
        receipt.confirmation_evidence_id = confirmation_evidence_id
        return receipt

    def restart(self) -> int:
        self.epoch += 1
        for receipt in self.effect_receipts.values():
            if receipt.state == EffectState.REQUESTED:
                receipt.state = EffectState.UNRESOLVED_AFTER_RESTART
                receipt.reason = "OUTCOME_REQUIRES_RECONCILIATION"
        return self.epoch

    def reconcile_after_restart(
        self,
        action_id: str,
        *,
        confirmed_outcome: Optional[bool],
        confirmation_evidence_id: Optional[str] = None,
    ) -> EffectReceipt:
        receipt = self.effect_receipts[action_id]
        if receipt.state != EffectState.UNRESOLVED_AFTER_RESTART:
            raise ValueError("effect is not unresolved after restart")
        if confirmed_outcome is None:
            return receipt
        if confirmation_evidence_id is None:
            raise ValueError("confirmed reconciliation requires outcome evidence")
        self._confirmation_observation(action_id, confirmation_evidence_id)
        receipt.state = (
            EffectState.CONFIRMED
            if confirmed_outcome
            else EffectState.FAILED_CONFIRMED
        )
        receipt.reason = (
            "EFFECT_CONFIRMED_AFTER_RECONCILIATION"
            if confirmed_outcome
            else "EFFECT_FAILURE_CONFIRMED_AFTER_RECONCILIATION"
        )
        receipt.confirmation_evidence_id = confirmation_evidence_id
        return receipt
