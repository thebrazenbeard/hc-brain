from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
from types import MappingProxyType
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel, JournalIntegrityError
from hc_kernel import EffectCandidate, EffectState, ReferenceKernel

UTC = timezone.utc


class FourAdversarialReferenceKernelR2Tests(unittest.TestCase):
    """Regression gates for Four's HC 0061 surviving counterexamples."""

    def setUp(self):
        self.t0 = datetime(2026, 9, 11, 8, 0, tzinfo=UTC)

    def _kernel(self, **kwargs):
        return ReferenceKernel(clock=lambda: self.t0, **kwargs)

    @staticmethod
    def _register(kernel):
        return kernel.register_grant(
            grantor="authority-fixture",
            grantee="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            basis_refs=("fixture-basis",),
            provenance=("four-adversarial-r2",),
            valid_from=datetime(2026, 9, 11, 7, 59, tzinfo=UTC),
            expires_at=datetime(2026, 9, 11, 8, 10, tzinfo=UTC),
        )

    @staticmethod
    def _candidate(kernel, grant_id, payload=None):
        return kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"} if payload is None else payload,
            authority_grant_id=grant_id,
        )

    def test_prewrapped_mappingproxy_is_recursively_detached(self):
        nested = {"value": 1}
        wrapped = MappingProxyType({"nested": nested})
        kernel = self._kernel()
        record = kernel.observe(producer="sensor", payload=wrapped)

        nested["value"] = 999

        self.assertEqual(record.payload["nested"]["value"], 1)
        self.assertEqual(
            kernel.evidence[record.evidence_id].payload["nested"]["value"],
            1,
        )

    def test_revocation_timestamp_is_monotone_one_way(self):
        kernel = self._kernel()
        grant = self._register(kernel)
        first_revocation = self.t0 - timedelta(seconds=1)
        kernel.revoke_grant(grant.grant_id, revoked_at=first_revocation)

        with self.assertRaises(ValueError):
            kernel.revoke_grant(
                grant.grant_id,
                revoked_at=self.t0 + timedelta(minutes=5),
            )

        candidate = self._candidate(kernel, grant.grant_id)
        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "REVOKED_AUTHORITY")
        self.assertEqual(
            kernel.authority_grants[grant.grant_id].revoked_at,
            first_revocation,
        )

    def test_durable_revocation_rewrite_is_rejected_before_append(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            grant = self._register(kernel)
            first_revocation = self.t0 - timedelta(seconds=1)
            kernel.revoke_grant(grant.grant_id, revoked_at=first_revocation)
            before = journal.read_bytes()

            with self.assertRaises(ValueError):
                kernel.revoke_grant(
                    grant.grant_id,
                    revoked_at=self.t0 + timedelta(minutes=5),
                )

            self.assertEqual(journal.read_bytes(), before)
            inspection = DurableReferenceKernel(
                journal,
                mode="inspect",
                clock=lambda: self.t0,
            )
            self.assertEqual(
                inspection.authority_grants[grant.grant_id].revoked_at,
                first_revocation,
            )

    def test_payload_admission_rejects_non_string_mapping_keys(self):
        kernel = self._kernel()
        with self.assertRaises(ValueError):
            kernel.observe(producer="sensor", payload={1: "x"})

    def test_direct_effect_candidate_rejects_non_string_mapping_keys(self):
        kernel = self._kernel()
        grant = self._register(kernel)
        candidate = EffectCandidate(
            action_id="action-key-collision",
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={1: "x"},
            authority_grant_id=grant.grant_id,
            planned_epoch=kernel.epoch,
        )
        with self.assertRaises(ValueError):
            kernel.request_effect(candidate)

    def test_payload_admission_rejects_non_finite_numbers(self):
        kernel = self._kernel()
        with self.assertRaises(ValueError):
            kernel.observe(producer="sensor", payload={"reading": float("nan")})
        with self.assertRaises(ValueError):
            kernel.plan_effect(
                origin="kinesis",
                action_scope="MOTOR_EFFECT",
                target_scope="arm",
                payload={"command": float("inf")},
                authority_grant_id=None,
            )

    def test_generic_observation_cannot_bind_effect_confirmation(self):
        kernel = self._kernel()
        grant = self._register(kernel)
        candidate = self._candidate(kernel, grant.grant_id)
        kernel.request_effect(candidate)

        with self.assertRaises(ValueError):
            kernel.observe(
                producer="attacker",
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )

    def test_effect_outcome_admission_uses_kernel_trust_policy(self):
        untrusted_kernel = self._kernel()
        grant = self._register(untrusted_kernel)
        candidate = self._candidate(untrusted_kernel, grant.grant_id)
        untrusted_kernel.request_effect(candidate)
        admit = getattr(untrusted_kernel, "observe_effect_outcome", None)
        self.assertIsNotNone(admit)
        with self.assertRaises(ValueError):
            admit(
                producer="actuator-sensor",
                payload={"arm_position": "moved"},
                effect_action_id=candidate.action_id,
            )

        trusted_kernel = self._kernel(
            outcome_source_validator=lambda producer, authority: (
                producer == "actuator-sensor"
                and authority.action_scope == "MOTOR_EFFECT"
                and authority.target_scope == "arm"
            )
        )
        trusted_grant = self._register(trusted_kernel)
        trusted_candidate = self._candidate(trusted_kernel, trusted_grant.grant_id)
        trusted_kernel.request_effect(trusted_candidate)

        with self.assertRaises(ValueError):
            trusted_kernel.observe_effect_outcome(
                producer="attacker",
                payload={"claimed": "done"},
                effect_action_id=trusted_candidate.action_id,
            )

        outcome = trusted_kernel.observe_effect_outcome(
            producer="actuator-sensor",
            payload={"arm_position": "moved"},
            effect_action_id=trusted_candidate.action_id,
        )
        receipt = trusted_kernel.confirm_effect(
            trusted_candidate.action_id,
            succeeded=True,
            confirmation_evidence_id=outcome.evidence_id,
        )
        self.assertEqual(receipt.state, EffectState.CONFIRMED)

    def test_durable_replay_revalidates_effect_outcome_source_policy(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            validator = lambda producer, authority: (
                producer == "actuator-sensor"
                and authority.action_scope == "MOTOR_EFFECT"
                and authority.target_scope == "arm"
            )
            kernel = DurableReferenceKernel(
                journal,
                clock=lambda: self.t0,
                outcome_source_validator=validator,
            )
            grant = self._register(kernel)
            candidate = self._candidate(kernel, grant.grant_id)
            kernel.request_effect(candidate)
            kernel.observe_effect_outcome(
                producer="actuator-sensor",
                payload={"arm_position": "moved"},
                effect_action_id=candidate.action_id,
            )

            lines = journal.read_text(encoding="utf-8").splitlines()
            envelope = json.loads(lines[-1])
            self.assertEqual(
                envelope["event_type"],
                "EFFECT_OUTCOME_RECORD_UPSERT",
            )
            envelope["data"]["producer"] = "attacker"
            body = {
                key: value
                for key, value in envelope.items()
                if key != "entry_hash"
            }
            envelope["entry_hash"] = hashlib.sha256(
                json.dumps(
                    body,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                    allow_nan=False,
                ).encode("utf-8")
            ).hexdigest()
            lines[-1] = json.dumps(
                envelope,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            journal.write_text("\n".join(lines) + "\n", encoding="utf-8")

            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(
                    journal,
                    mode="inspect",
                    clock=lambda: self.t0,
                    outcome_source_validator=validator,
                )


if __name__ == "__main__":
    unittest.main()
