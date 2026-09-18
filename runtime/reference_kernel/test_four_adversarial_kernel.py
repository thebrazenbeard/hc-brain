from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel
from hc_kernel import EffectCandidate, EffectState, EpistemicClass, ReferenceKernel

UTC = timezone.utc


class FourAdversarialReferenceKernelTests(unittest.TestCase):
    """Regression gates grown from Four's HC 0058 counterexamples.

    These gates preserve Four's original invariants and add Noah-side attacks
    found while repairing the same authority/admission boundary.
    """

    def setUp(self):
        self.t0 = datetime(2026, 9, 10, 18, 0, tzinfo=UTC)

    def _kernel(self):
        return ReferenceKernel(clock=lambda: self.t0)

    @staticmethod
    def _register(kernel, valid_from, expires_at):
        return kernel.register_grant(
            grantor="authority-fixture",
            grantee="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            basis_refs=("fixture-basis",),
            provenance=("four-adversarial",),
            valid_from=valid_from,
            expires_at=expires_at,
        )

    @staticmethod
    def _candidate(kernel, grant_id):
        return kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant_id,
        )

    def test_expired_authority_cannot_be_reactivated_by_caller_backdating(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=10),
            self.t0 - timedelta(seconds=1),
        )
        candidate = self._candidate(kernel, grant.grant_id)

        with self.assertRaises(TypeError):
            kernel.request_effect(candidate, now=self.t0 - timedelta(minutes=5))

        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "EXPIRED_AUTHORITY")

    def test_revoked_authority_cannot_be_reactivated_by_caller_backdating(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=10),
            self.t0 + timedelta(minutes=10),
        )
        kernel.revoke_grant(
            grant.grant_id,
            revoked_at=self.t0 - timedelta(seconds=1),
        )
        candidate = self._candidate(kernel, grant.grant_id)

        with self.assertRaises(TypeError):
            kernel.request_effect(candidate, now=self.t0 - timedelta(seconds=30))

        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "REVOKED_AUTHORITY")

    def test_same_action_id_with_different_candidate_semantics_fails_closed(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=1),
            self.t0 + timedelta(minutes=10),
        )
        original = self._candidate(kernel, grant.grant_id)
        first = kernel.request_effect(original)
        self.assertEqual(first.state, EffectState.REQUESTED)

        collision = EffectCandidate(
            action_id=original.action_id,
            origin="different-origin",
            action_scope="UNAUTHORIZED_EFFECT",
            target_scope="different-target",
            payload={"command": "different"},
            authority_grant_id=None,
            planned_epoch=kernel.epoch,
            parent_ids=(),
        )
        with self.assertRaises(ValueError):
            kernel.request_effect(collision)

    def test_same_action_id_collision_fails_closed_after_durable_reopen(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            first = DurableReferenceKernel(journal, clock=lambda: self.t0)
            grant = self._register(
                first,
                self.t0 - timedelta(minutes=1),
                self.t0 + timedelta(minutes=10),
            )
            original = self._candidate(first, grant.grant_id)
            first.request_effect(original)

            second = DurableReferenceKernel(journal, clock=lambda: self.t0)
            collision = EffectCandidate(
                action_id=original.action_id,
                origin=original.origin,
                action_scope=original.action_scope,
                target_scope=original.target_scope,
                payload={"command": "different"},
                authority_grant_id=original.authority_grant_id,
                planned_epoch=original.planned_epoch,
                parent_ids=original.parent_ids,
            )
            with self.assertRaises(ValueError):
                second.request_effect(collision)

    def test_observation_payload_is_detached_from_original_caller_object(self):
        kernel = self._kernel()
        caller_payload = {"reading": 1, "nested": {"value": "original"}}
        record = kernel.observe(
            producer="sensor",
            payload=caller_payload,
            source_refs=("sensor-1",),
        )

        caller_payload["reading"] = 999
        caller_payload["nested"]["value"] = "mutated"

        self.assertEqual(record.payload["reading"], 1)
        self.assertEqual(record.payload["nested"]["value"], "original")

    def test_admitted_record_payload_cannot_be_mutated_through_returned_reference(self):
        kernel = self._kernel()
        record = kernel.observe(
            producer="sensor",
            payload={"nested": {"value": "original"}},
            source_refs=("sensor-1",),
        )

        with self.assertRaises(TypeError):
            record.payload["nested"]["value"] = "mutated"

        self.assertEqual(
            kernel.evidence[record.evidence_id].payload["nested"]["value"],
            "original",
        )

    def test_authority_grant_cannot_be_rewritten_after_registration(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=1),
            self.t0 + timedelta(minutes=10),
        )

        with self.assertRaises(FrozenInstanceError):
            grant.action_scope = "UNBOUNDED_EFFECT"
        with self.assertRaises(FrozenInstanceError):
            grant.expires_at = self.t0 + timedelta(days=365)

        stored = kernel.authority_grants[grant.grant_id]
        self.assertEqual(stored.action_scope, "MOTOR_EFFECT")
        self.assertEqual(stored.expires_at, self.t0 + timedelta(minutes=10))

    def test_effect_receipt_cannot_be_rewritten_by_caller(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=1),
            self.t0 + timedelta(minutes=10),
        )
        candidate = self._candidate(kernel, grant.grant_id)
        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.REQUESTED)

        with self.assertRaises(FrozenInstanceError):
            receipt.state = EffectState.CONFIRMED
        with self.assertRaises(FrozenInstanceError):
            receipt.dispatch_attempts = 999

        stored = kernel.effect_receipts[candidate.action_id]
        self.assertEqual(stored.state, EffectState.REQUESTED)
        self.assertEqual(stored.dispatch_attempts, 1)

    def test_public_authority_effect_and_evidence_maps_are_read_only(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=1),
            self.t0 + timedelta(minutes=10),
        )
        candidate = self._candidate(kernel, grant.grant_id)
        kernel.request_effect(candidate)
        observation = kernel.observe(producer="sensor", payload={"value": 1})

        with self.assertRaises(TypeError):
            kernel.authority_grants[grant.grant_id] = grant
        with self.assertRaises(TypeError):
            kernel.effect_receipts[candidate.action_id] = kernel.effect_receipts[
                candidate.action_id
            ]
        with self.assertRaises(TypeError):
            kernel.evidence[observation.evidence_id] = observation

    def test_epoch_cannot_be_rewound_through_public_api(self):
        kernel = self._kernel()
        grant = self._register(
            kernel,
            self.t0 - timedelta(minutes=1),
            self.t0 + timedelta(minutes=10),
        )
        kernel.restart()
        self.assertEqual(kernel.epoch, 1)

        with self.assertRaises(AttributeError):
            kernel.epoch = grant.issued_epoch

        candidate = kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "STALE_AUTHORITY_EPOCH")

    def test_current_projection_preserves_epistemic_and_source_classification(self):
        kernel = self._kernel()
        key = ("world", "weather", "next", "shared")
        source = kernel.observe(
            producer="sensor",
            payload={"clouds": True},
            source_refs=("camera-1",),
        )
        prediction = kernel.derive(
            producer="cognition",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={"future": "rain"},
            parent_ids=(source.evidence_id,),
        )
        kernel.memory.append(
            logical_key=key,
            payload=prediction.payload,
            epistemic_class=prediction.epistemic_class,
            source_refs=prediction.source_refs,
        )

        projection = kernel.memory.current(key)
        self.assertEqual(projection.epistemic_class, EpistemicClass.PREDICTION)
        self.assertIn("camera-1", projection.source_refs)

    def test_durable_payload_snapshot_and_replay_are_immutable(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            caller_payload = {"reading": 1, "nested": {"value": "original"}}
            record = kernel.observe(
                producer="sensor",
                payload=caller_payload,
                source_refs=("sensor-1",),
            )

            caller_payload["reading"] = 999
            caller_payload["nested"]["value"] = "mutated"

            live_payload = kernel.evidence[record.evidence_id].payload
            replayed = DurableReferenceKernel(
                journal,
                mode="inspect",
                clock=lambda: self.t0,
            )
            replayed_payload = replayed.evidence[record.evidence_id].payload

            self.assertEqual(live_payload, replayed_payload)
            self.assertEqual(live_payload["reading"], 1)
            self.assertEqual(live_payload["nested"]["value"], "original")
            with self.assertRaises(TypeError):
                replayed_payload["nested"]["value"] = "mutated-after-replay"

    def test_durable_kernel_accepts_its_own_frozen_payload_for_memory_admission(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            record = kernel.observe(
                producer="sensor",
                payload={"value": 1},
                source_refs=("sensor-1",),
            )
            memory = kernel.memory.append(
                logical_key=("world", "sensor", "state", "shared"),
                payload=record.payload,
                epistemic_class=record.epistemic_class,
                source_refs=record.source_refs,
            )
            self.assertEqual(memory.payload["value"], 1)

    def test_timezone_naive_grant_boundaries_fail_closed(self):
        kernel = self._kernel()
        naive = datetime(2026, 9, 10, 18, 0)
        with self.assertRaises(ValueError):
            self._register(kernel, naive, naive + timedelta(minutes=10))


if __name__ == "__main__":
    unittest.main()
