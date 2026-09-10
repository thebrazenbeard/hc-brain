from __future__ import annotations

from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from hc_kernel import (
    AuthorityGrant,
    CurrentMemory,
    EffectCandidate,
    EffectReceipt,
    EffectState,
    EpistemicClass,
    EvidenceRecord,
    MemoryRecord,
    ReferenceKernel,
    RoutedEvent,
)


JOURNAL_SCHEMA_VERSION = 2
GENESIS_HASH = "0" * 64
VALID_OPEN_MODES = {"recover", "inspect"}


class JournalIntegrityError(RuntimeError):
    pass


class ReadOnlyInspectionError(RuntimeError):
    pass


def _iso(value: datetime) -> str:
    if value.tzinfo is None:
        raise ValueError("journaled datetimes must be timezone-aware")
    return value.isoformat()


def _parse_dt(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise JournalIntegrityError("journal contains timezone-naive datetime")
    return parsed


class JournaledCurrentMemory(CurrentMemory):
    def __init__(self, owner: "DurableReferenceKernel") -> None:
        super().__init__()
        self._owner = owner

    def append(
        self,
        *,
        logical_key,
        payload,
        epistemic_class,
        supersedes=(),
        source_refs=(),
    ):
        self._owner._ensure_writable()
        self._owner._ensure_jsonable(payload)
        record = super().append(
            logical_key=logical_key,
            payload=payload,
            epistemic_class=epistemic_class,
            supersedes=supersedes,
            source_refs=source_refs,
        )
        try:
            self._owner._record("MEMORY_RECORD_UPSERT", self._owner._memory_data(record))
        except Exception:
            self._records.pop(record.record_id, None)
            raise
        return record


class DurableReferenceKernel(ReferenceKernel):
    """Append-journaled reference slice.

    `mode="recover"` reconstructs state and, for a non-empty journal, advances
    the recovery epoch before returning the kernel to a caller. `mode="inspect"`
    reconstructs a read-only snapshot without changing currentness or writing to
    the journal.

    The hash chain detects accidental or unauthenticated modification. It is not
    a signature/MAC and therefore is not evidence against an attacker able to
    rewrite and re-hash the whole journal.
    """

    def __init__(
        self,
        journal_path: str | os.PathLike[str],
        *,
        mode: str = "recover",
    ) -> None:
        if mode not in VALID_OPEN_MODES:
            raise ValueError(f"mode must be one of {sorted(VALID_OPEN_MODES)}")
        super().__init__()
        self.journal_path = Path(journal_path)
        self.open_mode = mode
        self.memory = JournaledCurrentMemory(self)
        self._next_seq = 0
        self._last_hash = GENESIS_HASH
        had_events = self._load_existing()
        if had_events and mode == "recover":
            self._advance_recovery_epoch()

    @property
    def read_only(self) -> bool:
        return self.open_mode == "inspect"

    def _ensure_writable(self) -> None:
        if self.read_only:
            raise ReadOnlyInspectionError(
                "inspect mode is read-only; reopen in recover mode to mutate state"
            )

    @staticmethod
    def _ensure_jsonable(payload: Any) -> None:
        try:
            json.dumps(payload, ensure_ascii=False, sort_keys=True)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "durable reference-kernel payload must be JSON-serializable"
            ) from exc

    @staticmethod
    def _canonical_bytes(body: dict[str, Any]) -> bytes:
        return json.dumps(
            body,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")

    def _record(self, event_type: str, data: dict[str, Any]) -> None:
        self._ensure_writable()
        self._ensure_jsonable(data)
        body = {
            "schema_version": JOURNAL_SCHEMA_VERSION,
            "seq": self._next_seq,
            "event_type": event_type,
            "epoch": self.epoch,
            "data": data,
            "prev_hash": self._last_hash,
        }
        digest = hashlib.sha256(self._canonical_bytes(body)).hexdigest()
        envelope = dict(body)
        envelope["entry_hash"] = digest

        self.journal_path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(
            envelope,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        with self.journal_path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line + "\n")
            handle.flush()
            os.fsync(handle.fileno())

        self._last_hash = digest
        self._next_seq += 1

    def _load_existing(self) -> bool:
        if not self.journal_path.exists():
            return False
        text = self.journal_path.read_text(encoding="utf-8")
        if not text:
            return False

        expected_seq = 0
        expected_prev = GENESIS_HASH
        for line_number, raw_line in enumerate(text.splitlines(), start=1):
            try:
                envelope = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                raise JournalIntegrityError(
                    f"invalid JSON at journal line {line_number}"
                ) from exc

            required = {
                "schema_version",
                "seq",
                "event_type",
                "epoch",
                "data",
                "prev_hash",
                "entry_hash",
            }
            if set(envelope) != required:
                raise JournalIntegrityError(
                    f"journal line {line_number} has unexpected/missing fields"
                )
            if envelope["schema_version"] != JOURNAL_SCHEMA_VERSION:
                raise JournalIntegrityError(
                    f"unsupported journal schema at line {line_number}: "
                    f"{envelope['schema_version']!r}"
                )
            if not isinstance(envelope["epoch"], int) or envelope["epoch"] < 0:
                raise JournalIntegrityError(
                    f"invalid event epoch at journal line {line_number}"
                )
            if envelope["seq"] != expected_seq:
                raise JournalIntegrityError(
                    f"journal sequence discontinuity at line {line_number}"
                )
            if envelope["prev_hash"] != expected_prev:
                raise JournalIntegrityError(
                    f"journal hash-chain predecessor mismatch at line {line_number}"
                )

            body = {key: envelope[key] for key in required if key != "entry_hash"}
            digest = hashlib.sha256(self._canonical_bytes(body)).hexdigest()
            if digest != envelope["entry_hash"]:
                raise JournalIntegrityError(
                    f"journal entry hash mismatch at line {line_number}"
                )

            self._apply_event(
                event_type=envelope["event_type"],
                data=envelope["data"],
                event_epoch=envelope["epoch"],
            )
            expected_prev = digest
            expected_seq += 1

        self._last_hash = expected_prev
        self._next_seq = expected_seq
        return True

    def _apply_event(
        self,
        *,
        event_type: str,
        data: dict[str, Any],
        event_epoch: int,
    ) -> None:
        if event_type == "EPOCH_SET":
            new_epoch = data.get("epoch")
            if not isinstance(new_epoch, int):
                raise JournalIntegrityError("epoch transition is not an integer")
            if new_epoch != event_epoch:
                raise JournalIntegrityError("epoch envelope/data mismatch")
            if new_epoch != self.epoch + 1:
                raise JournalIntegrityError("epoch transition is not contiguous")
            self.epoch = new_epoch
            return

        if event_epoch != self.epoch:
            raise JournalIntegrityError(
                "non-transition journal event does not match current replay epoch"
            )

        if event_type == "EVIDENCE_RECORD_UPSERT":
            evidence_id = data["evidence_id"]
            if evidence_id in self.evidence:
                raise JournalIntegrityError("evidence identity rewritten in append journal")
            epistemic_class = EpistemicClass(data["epistemic_class"])
            parent_ids = tuple(data["parent_ids"])
            if epistemic_class == EpistemicClass.OBSERVATION:
                if parent_ids:
                    raise JournalIntegrityError(
                        "raw observation cannot replay with causal evidence parents"
                    )
            else:
                if not parent_ids:
                    raise JournalIntegrityError(
                        "derived/inferred/predicted evidence has no causal parent"
                    )
                missing = [parent for parent in parent_ids if parent not in self.evidence]
                if missing:
                    raise JournalIntegrityError(
                        f"evidence replay references unknown parents: {missing}"
                    )
            effect_action_id = data.get("effect_action_id")
            if effect_action_id is not None and effect_action_id not in self.effect_receipts:
                raise JournalIntegrityError(
                    "effect-linked observation references unknown requested effect"
                )
            record = EvidenceRecord(
                evidence_id=evidence_id,
                producer=data["producer"],
                epistemic_class=epistemic_class,
                payload=data["payload"],
                event_time=_parse_dt(data["event_time"]),
                record_time=_parse_dt(data["record_time"]),
                parent_ids=parent_ids,
                source_refs=tuple(data["source_refs"]),
                influence_roles=tuple(data["influence_roles"]),
                effect_action_id=effect_action_id,
            )
            self.evidence[record.evidence_id] = record
            return

        if event_type == "ROUTED_EVENT_UPSERT":
            event_id = data["event_id"]
            if event_id in self.routed_events:
                raise JournalIntegrityError("routed event identity rewritten in append journal")
            event = RoutedEvent(
                event_id=event_id,
                source=data["source"],
                audience=data["audience"],
                payload=data["payload"],
                priority=int(data["priority"]),
                parent_ids=tuple(data["parent_ids"]),
                authority_ref=data.get("authority_ref"),
            )
            self.routed_events[event.event_id] = event
            return

        if event_type == "ROUTED_EVENT_INCORPORATED":
            event_id = data["event_id"]
            if event_id not in self.routed_events:
                raise JournalIntegrityError(
                    "incorporation references unknown routed event"
                )
            self.incorporated_event_ids.add(event_id)
            return

        if event_type == "MEMORY_RECORD_UPSERT":
            record_id = data["record_id"]
            if record_id in self.memory._records:
                raise JournalIntegrityError("memory record identity rewritten in append journal")
            record = MemoryRecord(
                record_id=record_id,
                logical_key=tuple(data["logical_key"]),
                payload=data["payload"],
                epistemic_class=EpistemicClass(data["epistemic_class"]),
                supersedes=tuple(data["supersedes"]),
                source_refs=tuple(data["source_refs"]),
            )
            for predecessor in record.supersedes:
                prior = self.memory._records.get(predecessor)
                if prior is None:
                    raise JournalIntegrityError(
                        "memory supersession references unknown record"
                    )
                if prior.logical_key != record.logical_key:
                    raise JournalIntegrityError(
                        "journaled supersession crosses logical scope"
                    )
            self.memory._records[record.record_id] = record
            return

        if event_type == "AUTHORITY_GRANT_UPSERT":
            basis_refs = tuple(data["basis_refs"])
            if not basis_refs:
                raise JournalIntegrityError("authority grant has no explicit basis")
            valid_from = _parse_dt(data["valid_from"])
            expires_at = _parse_dt(data["expires_at"])
            if expires_at <= valid_from:
                raise JournalIntegrityError("authority grant has invalid validity interval")
            issued_epoch = int(data["issued_epoch"])
            if issued_epoch < 0 or issued_epoch > event_epoch:
                raise JournalIntegrityError("authority grant has impossible issued epoch")
            revoked_at = (
                _parse_dt(data["revoked_at"])
                if data.get("revoked_at") is not None
                else None
            )
            grant = AuthorityGrant(
                grant_id=data["grant_id"],
                grantor=data["grantor"],
                grantee=data["grantee"],
                action_scope=data["action_scope"],
                target_scope=data["target_scope"],
                basis_refs=basis_refs,
                provenance=tuple(data["provenance"]),
                issued_epoch=issued_epoch,
                valid_from=valid_from,
                expires_at=expires_at,
                revoked_at=revoked_at,
            )
            prior = self.authority_grants.get(grant.grant_id)
            if prior is not None:
                immutable_prior = (
                    prior.grantor,
                    prior.grantee,
                    prior.action_scope,
                    prior.target_scope,
                    prior.basis_refs,
                    prior.provenance,
                    prior.issued_epoch,
                    prior.valid_from,
                    prior.expires_at,
                )
                immutable_new = (
                    grant.grantor,
                    grant.grantee,
                    grant.action_scope,
                    grant.target_scope,
                    grant.basis_refs,
                    grant.provenance,
                    grant.issued_epoch,
                    grant.valid_from,
                    grant.expires_at,
                )
                if immutable_prior != immutable_new:
                    raise JournalIntegrityError(
                        "authority upsert rewrites immutable grant semantics"
                    )
                if prior.revoked_at is not None and grant.revoked_at != prior.revoked_at:
                    raise JournalIntegrityError("revocation history was rewritten")
                if prior.revoked_at is None and grant.revoked_at is None:
                    raise JournalIntegrityError("authority upsert makes no valid state transition")
            self.authority_grants[grant.grant_id] = grant
            return

        if event_type == "EFFECT_RECEIPT_UPSERT":
            receipt = EffectReceipt(
                action_id=data["action_id"],
                state=EffectState(data["state"]),
                reason=data["reason"],
                epoch=int(data["epoch"]),
                authority_grant_id=data.get("authority_grant_id"),
                dispatch_attempts=int(data["dispatch_attempts"]),
                confirmation_evidence_id=data.get("confirmation_evidence_id"),
            )
            if receipt.epoch < 0 or receipt.epoch > event_epoch:
                raise JournalIntegrityError("effect receipt has impossible originating epoch")
            prior = self.effect_receipts.get(receipt.action_id)
            if prior is None:
                if receipt.state not in {EffectState.BLOCKED, EffectState.REQUESTED}:
                    raise JournalIntegrityError("effect receipt begins in impossible state")
                if receipt.state == EffectState.REQUESTED:
                    if receipt.dispatch_attempts != 1:
                        raise JournalIntegrityError(
                            "requested effect must have exactly one request/dispatch handoff marker"
                        )
                    if receipt.authority_grant_id is None:
                        raise JournalIntegrityError("requested effect has no authority reference")
                    if receipt.authority_grant_id not in self.authority_grants:
                        raise JournalIntegrityError("requested effect references unknown grant")
                elif receipt.dispatch_attempts != 0:
                    raise JournalIntegrityError("blocked effect cannot claim dispatch attempt")
            else:
                allowed = {
                    EffectState.REQUESTED: {
                        EffectState.CONFIRMED,
                        EffectState.FAILED_CONFIRMED,
                        EffectState.UNRESOLVED_AFTER_RESTART,
                    },
                    EffectState.UNRESOLVED_AFTER_RESTART: {
                        EffectState.CONFIRMED,
                        EffectState.FAILED_CONFIRMED,
                    },
                }
                if receipt.state not in allowed.get(prior.state, set()):
                    raise JournalIntegrityError(
                        f"invalid effect transition {prior.state.value}->{receipt.state.value}"
                    )
                if receipt.authority_grant_id != prior.authority_grant_id:
                    raise JournalIntegrityError("effect transition rewrites authority reference")
                if receipt.epoch != prior.epoch:
                    raise JournalIntegrityError("effect transition rewrites originating epoch")
                if receipt.dispatch_attempts != prior.dispatch_attempts:
                    raise JournalIntegrityError("effect transition rewrites attempt count")

            if receipt.state in {EffectState.CONFIRMED, EffectState.FAILED_CONFIRMED}:
                evidence_id = receipt.confirmation_evidence_id
                if evidence_id is None:
                    raise JournalIntegrityError("confirmed effect has no outcome evidence")
                evidence = self.evidence.get(evidence_id)
                if evidence is None:
                    raise JournalIntegrityError("confirmed effect references unknown evidence")
                if evidence.epistemic_class != EpistemicClass.OBSERVATION:
                    raise JournalIntegrityError("confirmed effect is not based on observation")
                if evidence.effect_action_id != receipt.action_id:
                    raise JournalIntegrityError(
                        "confirmed effect evidence is not bound to the action"
                    )
            elif receipt.confirmation_evidence_id is not None:
                raise JournalIntegrityError(
                    "non-confirmed effect unexpectedly carries confirmation evidence"
                )

            self.effect_receipts[receipt.action_id] = receipt
            return

        raise JournalIntegrityError(f"unknown journal event type: {event_type}")

    @staticmethod
    def _evidence_data(record: EvidenceRecord) -> dict[str, Any]:
        return {
            "evidence_id": record.evidence_id,
            "producer": record.producer,
            "epistemic_class": record.epistemic_class.value,
            "payload": record.payload,
            "event_time": _iso(record.event_time),
            "record_time": _iso(record.record_time),
            "parent_ids": list(record.parent_ids),
            "source_refs": list(record.source_refs),
            "influence_roles": list(record.influence_roles),
            "effect_action_id": record.effect_action_id,
        }

    @staticmethod
    def _route_data(event: RoutedEvent) -> dict[str, Any]:
        return {
            "event_id": event.event_id,
            "source": event.source,
            "audience": event.audience,
            "payload": event.payload,
            "priority": event.priority,
            "parent_ids": list(event.parent_ids),
            "authority_ref": event.authority_ref,
        }

    @staticmethod
    def _memory_data(record: MemoryRecord) -> dict[str, Any]:
        return {
            "record_id": record.record_id,
            "logical_key": list(record.logical_key),
            "payload": record.payload,
            "epistemic_class": record.epistemic_class.value,
            "supersedes": list(record.supersedes),
            "source_refs": list(record.source_refs),
        }

    @staticmethod
    def _grant_data(grant: AuthorityGrant) -> dict[str, Any]:
        return {
            "grant_id": grant.grant_id,
            "grantor": grant.grantor,
            "grantee": grant.grantee,
            "action_scope": grant.action_scope,
            "target_scope": grant.target_scope,
            "basis_refs": list(grant.basis_refs),
            "provenance": list(grant.provenance),
            "issued_epoch": grant.issued_epoch,
            "valid_from": _iso(grant.valid_from),
            "expires_at": _iso(grant.expires_at),
            "revoked_at": _iso(grant.revoked_at) if grant.revoked_at else None,
        }

    @staticmethod
    def _receipt_data(receipt: EffectReceipt) -> dict[str, Any]:
        return {
            "action_id": receipt.action_id,
            "state": receipt.state.value,
            "reason": receipt.reason,
            "epoch": receipt.epoch,
            "authority_grant_id": receipt.authority_grant_id,
            "dispatch_attempts": receipt.dispatch_attempts,
            "confirmation_evidence_id": receipt.confirmation_evidence_id,
        }

    def observe(self, **kwargs) -> EvidenceRecord:
        self._ensure_writable()
        self._ensure_jsonable(kwargs.get("payload"))
        record = super().observe(**kwargs)
        try:
            self._record("EVIDENCE_RECORD_UPSERT", self._evidence_data(record))
        except Exception:
            self.evidence.pop(record.evidence_id, None)
            raise
        return record

    def derive(self, **kwargs) -> EvidenceRecord:
        self._ensure_writable()
        self._ensure_jsonable(kwargs.get("payload"))
        record = super().derive(**kwargs)
        try:
            self._record("EVIDENCE_RECORD_UPSERT", self._evidence_data(record))
        except Exception:
            self.evidence.pop(record.evidence_id, None)
            raise
        return record

    def route(self, **kwargs) -> RoutedEvent:
        self._ensure_writable()
        self._ensure_jsonable(kwargs.get("payload"))
        event = super().route(**kwargs)
        try:
            self._record("ROUTED_EVENT_UPSERT", self._route_data(event))
        except Exception:
            self.routed_events.pop(event.event_id, None)
            raise
        return event

    def incorporate_routed_event(self, event_id: str) -> None:
        self._ensure_writable()
        already = event_id in self.incorporated_event_ids
        super().incorporate_routed_event(event_id)
        if already:
            return
        try:
            self._record("ROUTED_EVENT_INCORPORATED", {"event_id": event_id})
        except Exception:
            self.incorporated_event_ids.discard(event_id)
            raise

    def register_grant(self, **kwargs) -> AuthorityGrant:
        self._ensure_writable()
        grant = super().register_grant(**kwargs)
        try:
            self._record("AUTHORITY_GRANT_UPSERT", self._grant_data(grant))
        except Exception:
            self.authority_grants.pop(grant.grant_id, None)
            raise
        return grant

    def revoke_grant(self, grant_id: str, **kwargs) -> None:
        self._ensure_writable()
        grant = self.authority_grants[grant_id]
        previous = grant.revoked_at
        super().revoke_grant(grant_id, **kwargs)
        try:
            self._record("AUTHORITY_GRANT_UPSERT", self._grant_data(grant))
        except Exception:
            grant.revoked_at = previous
            raise

    def request_effect(self, candidate: EffectCandidate, **kwargs) -> EffectReceipt:
        self._ensure_writable()
        existed = candidate.action_id in self.effect_receipts
        receipt = super().request_effect(candidate, **kwargs)
        if existed:
            return receipt
        try:
            self._record("EFFECT_RECEIPT_UPSERT", self._receipt_data(receipt))
        except Exception:
            self.effect_receipts.pop(candidate.action_id, None)
            raise
        return receipt

    def confirm_effect(self, action_id: str, **kwargs) -> EffectReceipt:
        self._ensure_writable()
        receipt = self.effect_receipts[action_id]
        previous = (
            receipt.state,
            receipt.reason,
            receipt.confirmation_evidence_id,
        )
        result = super().confirm_effect(action_id, **kwargs)
        try:
            self._record("EFFECT_RECEIPT_UPSERT", self._receipt_data(result))
        except Exception:
            receipt.state, receipt.reason, receipt.confirmation_evidence_id = previous
            raise
        return result

    def reconcile_after_restart(self, action_id: str, **kwargs) -> EffectReceipt:
        self._ensure_writable()
        receipt = self.effect_receipts[action_id]
        previous = (
            receipt.state,
            receipt.reason,
            receipt.confirmation_evidence_id,
        )
        result = super().reconcile_after_restart(action_id, **kwargs)
        if previous == (
            result.state,
            result.reason,
            result.confirmation_evidence_id,
        ):
            return result
        try:
            self._record("EFFECT_RECEIPT_UPSERT", self._receipt_data(result))
        except Exception:
            receipt.state, receipt.reason, receipt.confirmation_evidence_id = previous
            raise
        return result

    def _advance_recovery_epoch(self) -> int:
        self._ensure_writable()
        prior_epoch = self.epoch
        self.epoch += 1
        try:
            self._record("EPOCH_SET", {"epoch": self.epoch})
        except Exception:
            self.epoch = prior_epoch
            raise

        for receipt in list(self.effect_receipts.values()):
            if receipt.state == EffectState.REQUESTED:
                prior_state = receipt.state
                prior_reason = receipt.reason
                receipt.state = EffectState.UNRESOLVED_AFTER_RESTART
                receipt.reason = "OUTCOME_REQUIRES_RECONCILIATION"
                try:
                    self._record("EFFECT_RECEIPT_UPSERT", self._receipt_data(receipt))
                except Exception:
                    receipt.state = prior_state
                    receipt.reason = prior_reason
                    raise
        return self.epoch

    def restart(self) -> int:
        return self._advance_recovery_epoch()
