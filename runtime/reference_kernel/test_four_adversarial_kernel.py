from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel
from hc_kernel import (
    EffectCandidate,
    EffectState,
    EpistemicClass,
    ReferenceKernel,
)

UTC = timezone.utc


class FourAdversarialReferenceKernelTests(unittest.TestCase):
    """Independent regression fixtures for HC 0055 findings.

    These tests encode required secure behavior rather than the behavior of the
    2026-09-10 failing implementation cut. They are expected to fail against
    hc_kernel.py blob e48355da01482cc6ca709928214ad61c9998249e.
    """

    def setUp(self) -> None:
        self.t0 = datetime(2026, 9, 10, 18, 0, tzinfo=UTC)

    @staticmethod
    def _register(
        kernel: ReferenceKernel,
        *,
        valid_from: datetime,
        expires_at: datetime,
    ):
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
    def _candidate(kernel: ReferenceKernel, grant_id: str):
        return kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant_id,
        )

    def test_expired_authority_cannot_be_reactivated_by_caller_backdating(self):
        kernel = ReferenceKernel()
        grant = self._register(
            kernel,
            valid_from=self.t0 - timedelta(minutes=10),
            expires_at=self.t0 - timedelta(seconds=1),
        )
        candidate = self._candidate(kernel, grant.grant_id)

        try:
            receipt = kernel.request_effect(
                candidate,
                now=self.t0 - timedelta(minutes=5),
            )
        except TypeError:
            # A repaired production API may remove caller-controlled `now`.
            return

        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertNotEqual(receipt.reason, "AUTHORIZED")

    def test_revoked_authority_cannot_be_reactivated_by_caller_backdating(self):
        kernel = ReferenceKernel()
        grant = self._register(
            kernel,
            valid_from=self.t0 - timedelta(minutes=10),
            expires_at=self.t0 + timedelta(minutes=10),
        )
        kernel.revoke_grant(
            grant.grant_id,
            revoked_at=self.t0 - timedelta(seconds=1),
        )
        candidate = self._candidate(kernel, grant.grant_id)

        try:
            receipt = kernel.request_effect(
                candidate,
                now=self.t0 - timedelta(seconds=30),
            )
        except TypeError:
            return

        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertNotEqual(receipt.reason, "AUTHORIZED")

    def test_same_action_id_with_different_candidate_semantics_fails_closed(self):
        kernel = ReferenceKernel()
        grant = self._register(
            kernel,
            valid_from=self.t0 - timedelta(minutes=1),
            expires_at=self.t0 + timedelta(minutes=10),
        )
        original = self._candidate(kernel, grant.grant_id)
        first = kernel.request_effect(original, now=self.t0)
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

        try:
            second = kernel.request_effect(collision, now=self.t0)
        except (ValueError, RuntimeError):
            return

        self.assertNotEqual(second.state, EffectState.REQUESTED)
        self.assertNotEqual(second.reason, "AUTHORIZED")

    def test_observation_payload_is_immutable_after_admission(self):
        kernel = ReferenceKernel()
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

    def test_current_projection_preserves_epistemic_and_source_classification(self):
        kernel = ReferenceKernel()
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

        if hasattr(projection, "epistemic_class"):
            projected_class = projection.epistemic_class
            projected_sources = getattr(projection, "source_refs", ())
        elif hasattr(projection, "selected_record"):
            selected = projection.selected_record
            projected_class = selected.epistemic_class
            projected_sources = selected.source_refs
        else:
            self.fail(
                "current-state projection exposes payload/head IDs without "
                "epistemic/source classification"
            )

        self.assertEqual(projected_class, EpistemicClass.PREDICTION)
        self.assertIn("camera-1", projected_sources)

    def test_durable_live_and_replayed_payload_remain_identical_after_caller_mutation(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal)
            caller_payload = {"reading": 1, "nested": {"value": "original"}}
            record = kernel.observe(
                producer="sensor",
                payload=caller_payload,
                source_refs=("sensor-1",),
            )

            caller_payload["reading"] = 999
            caller_payload["nested"]["value"] = "mutated"

            live_payload = kernel.evidence[record.evidence_id].payload
            replayed = DurableReferenceKernel(journal, mode="inspect")
            replayed_payload = replayed.evidence[record.evidence_id].payload

            self.assertEqual(live_payload, replayed_payload)
            self.assertEqual(live_payload["reading"], 1)
            self.assertEqual(live_payload["nested"]["value"], "original")


if __name__ == "__main__":
    unittest.main()
