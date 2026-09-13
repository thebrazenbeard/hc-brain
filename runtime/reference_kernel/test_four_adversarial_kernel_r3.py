from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel
from hc_kernel import EffectState, ReferenceKernel

UTC = timezone.utc


class EqualCapability:
    def __hash__(self):
        return 1

    def __eq__(self, other):
        return True


class FourAdversarialReferenceKernelR3Tests(unittest.TestCase):
    """Regression gates for live outcome-source authenticity after HC 0067."""

    def setUp(self):
        self.t0 = datetime(2026, 9, 13, 20, 0, tzinfo=UTC)

    def _grant(self, kernel):
        return kernel.register_grant(
            grantor="authority-fixture",
            grantee="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            basis_refs=("fixture-basis",),
            valid_from=self.t0 - timedelta(minutes=1),
            expires_at=self.t0 + timedelta(minutes=10),
        )

    def _request(self, kernel, grant_id):
        candidate = kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant_id,
        )
        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.REQUESTED)
        return candidate

    def test_live_outcome_requires_possession_of_registered_capability(self):
        trusted = object()
        counterfeit = object()
        kernel = ReferenceKernel(
            clock=lambda: self.t0,
            outcome_source_capabilities={trusted: "actuator-sensor"},
            outcome_source_validator=lambda producer, grant: (
                producer == "actuator-sensor"
                and grant.action_scope == "MOTOR_EFFECT"
                and grant.target_scope == "arm"
            ),
        )
        candidate = self._request(kernel, self._grant(kernel).grant_id)

        with self.assertRaises(ValueError):
            kernel.observe_effect_outcome(
                source_capability=counterfeit,
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )
        self.assertEqual(len(kernel.evidence), 0)

        outcome = kernel.observe_effect_outcome(
            source_capability=trusted,
            payload={"position": "moved"},
            effect_action_id=candidate.action_id,
        )
        self.assertEqual(outcome.producer, "actuator-sensor")
        confirmed = kernel.confirm_effect(
            candidate.action_id,
            succeeded=True,
            confirmation_evidence_id=outcome.evidence_id,
        )
        self.assertEqual(confirmed.state, EffectState.CONFIRMED)

    def test_capability_resolution_uses_identity_not_equality(self):
        trusted = EqualCapability()
        counterfeit = EqualCapability()
        kernel = ReferenceKernel(
            clock=lambda: self.t0,
            outcome_source_capabilities={trusted: "actuator-sensor"},
            outcome_source_validator=lambda producer, grant: producer == "actuator-sensor",
        )
        candidate = self._request(kernel, self._grant(kernel).grant_id)

        with self.assertRaises(ValueError):
            kernel.observe_effect_outcome(
                source_capability=counterfeit,
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )

    def test_registered_capability_does_not_bypass_scope_policy(self):
        trusted = object()
        kernel = ReferenceKernel(
            clock=lambda: self.t0,
            outcome_source_capabilities={trusted: "actuator-sensor"},
            outcome_source_validator=lambda producer, grant: False,
        )
        candidate = self._request(kernel, self._grant(kernel).grant_id)

        with self.assertRaises(ValueError):
            kernel.observe_effect_outcome(
                source_capability=trusted,
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )

    def test_durable_outcome_records_capability_derived_producer_and_replays(self):
        trusted = object()
        validator = lambda producer, grant: producer == "actuator-sensor"
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(
                journal,
                clock=lambda: self.t0,
                outcome_source_capabilities={trusted: "actuator-sensor"},
                outcome_source_validator=validator,
            )
            candidate = self._request(kernel, self._grant(kernel).grant_id)
            outcome = kernel.observe_effect_outcome(
                source_capability=trusted,
                payload={"position": "moved"},
                effect_action_id=candidate.action_id,
            )
            kernel.confirm_effect(
                candidate.action_id,
                succeeded=True,
                confirmation_evidence_id=outcome.evidence_id,
            )

            inspection = DurableReferenceKernel(
                journal,
                mode="inspect",
                clock=lambda: self.t0,
                outcome_source_validator=validator,
            )
            restored = inspection.evidence[outcome.evidence_id]
            self.assertEqual(restored.producer, "actuator-sensor")
            self.assertEqual(
                inspection.effect_receipts[candidate.action_id].state,
                EffectState.CONFIRMED,
            )


if __name__ == "__main__":
    unittest.main()
