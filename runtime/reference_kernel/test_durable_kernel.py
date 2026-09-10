from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel, JournalIntegrityError
from hc_kernel import EpistemicClass, EffectState, ProjectionStatus

UTC = timezone.utc


class DurableReferenceKernelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.journal = Path(self.tempdir.name) / "hc.jsonl"
        self.now = datetime(2026, 9, 10, 19, 0, tzinfo=UTC)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def _grant(self, kernel):
        return kernel.register_grant(
            grantor="authority-fixture",
            grantee="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            basis_refs=("fixture-basis",),
            provenance=("durable-test",),
            valid_from=self.now - timedelta(minutes=1),
            expires_at=self.now + timedelta(minutes=10),
        )

    def test_memory_and_ambiguity_survive_reopen(self):
        first = DurableReferenceKernel(self.journal)
        key = ("world", "object-1", "state", "shared")
        a = first.memory.append(
            logical_key=key,
            payload={"state": "A"},
            epistemic_class=EpistemicClass.OBSERVATION,
        )
        b = first.memory.append(
            logical_key=key,
            payload={"state": "B"},
            epistemic_class=EpistemicClass.OBSERVATION,
        )
        self.assertEqual(first.memory.current(key).status, ProjectionStatus.AMBIGUOUS)

        second = DurableReferenceKernel(self.journal)
        projection = second.memory.current(key)
        self.assertEqual(projection.status, ProjectionStatus.AMBIGUOUS)
        self.assertEqual(set(projection.head_ids), {a.record_id, b.record_id})

    def test_derived_evidence_lineage_survives_reopen(self):
        first = DurableReferenceKernel(self.journal)
        obs = first.observe(
            producer="optics",
            payload={"object": "ball"},
            source_refs=("camera-1",),
        )
        pred = first.derive(
            producer="cognition",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={"next": "move"},
            parent_ids=(obs.evidence_id,),
            influence_roles=("WORLD_MODEL_INPUT",),
        )

        second = DurableReferenceKernel(self.journal)
        restored = second.evidence[pred.evidence_id]
        self.assertEqual(restored.epistemic_class, EpistemicClass.PREDICTION)
        self.assertEqual(restored.parent_ids, (obs.evidence_id,))
        self.assertIn("camera-1", restored.source_refs)

    def test_requested_effect_becomes_unresolved_on_reopen_and_is_not_redispatched(self):
        first = DurableReferenceKernel(self.journal)
        grant = self._grant(first)
        candidate = first.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        receipt = first.request_effect(candidate, now=self.now)
        self.assertEqual(receipt.state, EffectState.REQUESTED)
        self.assertEqual(receipt.dispatch_attempts, 1)

        second = DurableReferenceKernel(self.journal)
        restored = second.effect_receipts[candidate.action_id]
        self.assertEqual(restored.state, EffectState.UNRESOLVED_AFTER_RESTART)
        self.assertEqual(restored.dispatch_attempts, 1)

        replay = second.request_effect(candidate, now=self.now)
        self.assertIs(replay, restored)
        self.assertEqual(replay.state, EffectState.UNRESOLVED_AFTER_RESTART)
        self.assertEqual(replay.dispatch_attempts, 1)

        fresh_candidate = second.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "other"},
            authority_grant_id=grant.grant_id,
        )
        old_authority = second.request_effect(fresh_candidate, now=self.now)
        self.assertEqual(old_authority.state, EffectState.BLOCKED)
        self.assertEqual(old_authority.reason, "STALE_AUTHORITY_EPOCH")

    def test_confirmed_effect_remains_confirmed_after_reopen(self):
        first = DurableReferenceKernel(self.journal)
        grant = self._grant(first)
        candidate = first.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        first.request_effect(candidate, now=self.now)
        observation = first.observe(
            producer="somatics",
            payload={"arm_position": "moved"},
            source_refs=("proprioception",),
            effect_action_id=candidate.action_id,
        )
        first.confirm_effect(
            candidate.action_id,
            succeeded=True,
            confirmation_evidence_id=observation.evidence_id,
        )

        second = DurableReferenceKernel(self.journal)
        restored = second.effect_receipts[candidate.action_id]
        self.assertEqual(restored.state, EffectState.CONFIRMED)
        self.assertEqual(restored.confirmation_evidence_id, observation.evidence_id)

    def test_corrupted_entry_hash_fails_closed(self):
        kernel = DurableReferenceKernel(self.journal)
        kernel.observe(producer="optics", payload={"x": 1})
        lines = self.journal.read_text(encoding="utf-8").splitlines()
        envelope = json.loads(lines[-1])
        envelope["data"]["payload"]["x"] = 2
        lines[-1] = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        self.journal.write_text("\n".join(lines) + "\n", encoding="utf-8")

        with self.assertRaises(JournalIntegrityError):
            DurableReferenceKernel(self.journal)

    def test_sequence_discontinuity_fails_closed(self):
        kernel = DurableReferenceKernel(self.journal)
        kernel.observe(producer="optics", payload={"x": 1})
        lines = self.journal.read_text(encoding="utf-8").splitlines()
        envelope = json.loads(lines[-1])
        envelope["seq"] = 9
        body = {key: envelope[key] for key in envelope if key != "entry_hash"}
        import hashlib
        digest = hashlib.sha256(
            json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        envelope["entry_hash"] = digest
        lines[-1] = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        self.journal.write_text("\n".join(lines) + "\n", encoding="utf-8")

        with self.assertRaises(JournalIntegrityError):
            DurableReferenceKernel(self.journal)

    def test_unserializable_payload_rejected_before_state_mutation(self):
        kernel = DurableReferenceKernel(self.journal)
        with self.assertRaises(ValueError):
            kernel.observe(producer="optics", payload={1, 2, 3})
        self.assertEqual(kernel.evidence, {})
        self.assertFalse(self.journal.exists())

    def test_reconciled_outcome_is_durable(self):
        first = DurableReferenceKernel(self.journal)
        grant = self._grant(first)
        candidate = first.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        first.request_effect(candidate, now=self.now)

        second = DurableReferenceKernel(self.journal)
        observation = second.observe(
            producer="somatics",
            payload={"arm_position": "moved"},
            source_refs=("proprioception",),
            effect_action_id=candidate.action_id,
        )
        second.reconcile_after_restart(
            candidate.action_id,
            confirmed_outcome=True,
            confirmation_evidence_id=observation.evidence_id,
        )

        third = DurableReferenceKernel(self.journal)
        restored = third.effect_receipts[candidate.action_id]
        self.assertEqual(restored.state, EffectState.CONFIRMED)


if __name__ == "__main__":
    unittest.main()
