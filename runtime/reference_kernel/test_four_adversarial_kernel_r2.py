from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import MappingProxyType
import hashlib
import json
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel, JournalIntegrityError
from hc_kernel import EpistemicClass, EffectCandidate, EffectState, ReferenceKernel

UTC = timezone.utc


class FourAdversarialReferenceKernelR2Tests(unittest.TestCase):
    """Regression gates for Four's HC 0061 surviving counterexamples."""

    def setUp(self):
        self.t0 = datetime(2026, 9, 11, 8, 0, tzinfo=UTC)
        self.actuator_capability = object()

    def _kernel(self, **kwargs):
        kwargs.setdefault(
            "outcome_source_capabilities",
            ((self.actuator_capability, "actuator-sensor"),),
        )
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

    def test_durable_idempotent_revocation_does_not_append_a_noop(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            grant = self._register(kernel)
            first_revocation = self.t0 - timedelta(seconds=1)
            kernel.revoke_grant(grant.grant_id, revoked_at=first_revocation)
            before = journal.read_bytes()

            kernel.revoke_grant(grant.grant_id, revoked_at=first_revocation)

            self.assertEqual(journal.read_bytes(), before)

    def test_durable_effect_outcome_admission_is_trusted_and_replayable(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            validator = lambda producer, authority: producer == "actuator-sensor"
            kernel = DurableReferenceKernel(
                journal,
                clock=lambda: self.t0,
                outcome_source_validator=validator,
                outcome_source_capabilities=(
                    (self.actuator_capability, "actuator-sensor"),
                ),
            )
            grant = self._register(kernel)
            candidate = self._candidate(kernel, grant.grant_id)
            kernel.request_effect(candidate)

            with self.assertRaises(ValueError):
                kernel.observe(
                    producer="attacker",
                    payload={"claimed": "done"},
                    effect_action_id=candidate.action_id,
                )
            with self.assertRaises(ValueError):
                kernel.observe_effect_outcome(
                    source_capability=object(),
                    payload={"claimed": "done"},
                    effect_action_id=candidate.action_id,
                )

            outcome = kernel.observe_effect_outcome(
                source_capability=self.actuator_capability,
                payload={"position": "moved"},
                effect_action_id=candidate.action_id,
            )
            confirmed = kernel.confirm_effect(
                candidate.action_id,
                succeeded=True,
                confirmation_evidence_id=outcome.evidence_id,
            )
            self.assertEqual(confirmed.state, EffectState.CONFIRMED)

            inspection = DurableReferenceKernel(
                journal,
                mode="inspect",
                clock=lambda: self.t0,
                outcome_source_validator=validator,
                outcome_source_capabilities=(
                    (self.actuator_capability, "actuator-sensor"),
                ),
            )
            self.assertEqual(
                inspection.effect_receipts[candidate.action_id].state,
                EffectState.CONFIRMED,
            )

    def test_rehashed_untrusted_effect_outcome_is_rejected_on_replay(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            validator = lambda producer, authority: producer == "actuator-sensor"
            kernel = DurableReferenceKernel(
                journal,
                clock=lambda: self.t0,
                outcome_source_validator=validator,
                outcome_source_capabilities=(
                    (self.actuator_capability, "actuator-sensor"),
                ),
            )
            grant = self._register(kernel)
            candidate = self._candidate(kernel, grant.grant_id)
            kernel.request_effect(candidate)

            kernel._record(
                "EVIDENCE_RECORD_UPSERT",
                {
                    "evidence_id": "forged-outcome",
                    "producer": "actuator-sensor",
                    "epistemic_class": "OBSERVATION",
                    "payload": {"claimed": "done"},
                    "event_time": self.t0.isoformat(),
                    "record_time": self.t0.isoformat(),
                    "parent_ids": [],
                    "source_refs": [],
                    "influence_roles": [],
                    "effect_action_id": candidate.action_id,
                },
            )
            lines = journal.read_text(encoding="utf-8").splitlines()
            envelope = json.loads(lines[-1])
            envelope["data"]["producer"] = "attacker"
            body = {
                key: value for key, value in envelope.items() if key != "entry_hash"
            }
            envelope["entry_hash"] = hashlib.sha256(
                json.dumps(
                    body,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            lines[-1] = json.dumps(
                envelope,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            journal.write_text("\n".join(lines) + "\n", encoding="utf-8")

            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(
                    journal,
                    mode="inspect",
                    clock=lambda: self.t0,
                    outcome_source_validator=validator,
                )

    def test_bound_effect_outcome_replay_requires_source_policy(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            validator = lambda producer, authority: producer == "actuator-sensor"
            kernel = DurableReferenceKernel(
                journal,
                clock=lambda: self.t0,
                outcome_source_validator=validator,
                outcome_source_capabilities=(
                    (self.actuator_capability, "actuator-sensor"),
                ),
            )
            grant = self._register(kernel)
            candidate = self._candidate(kernel, grant.grant_id)
            kernel.request_effect(candidate)
            outcome = kernel.observe_effect_outcome(
                source_capability=self.actuator_capability,
                payload={"position": "moved"},
                effect_action_id=candidate.action_id,
            )
            kernel.confirm_effect(
                candidate.action_id,
                succeeded=True,
                confirmation_evidence_id=outcome.evidence_id,
            )

            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(
                    journal,
                    mode="inspect",
                    clock=lambda: self.t0,
                )

    def test_bound_effect_replay_rejects_non_observation_evidence(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            validator = lambda producer, authority: producer == "actuator-sensor"
            kernel = DurableReferenceKernel(
                journal,
                clock=lambda: self.t0,
                outcome_source_validator=validator,
            )
            parent = kernel.observe(producer="sensor", payload={"x": 1})
            grant = self._register(kernel)
            candidate = self._candidate(kernel, grant.grant_id)
            kernel.request_effect(candidate)

            kernel._record(
                "EVIDENCE_RECORD_UPSERT",
                {
                    "evidence_id": "forged-derived-outcome",
                    "producer": "actuator-sensor",
                    "epistemic_class": "DERIVED",
                    "payload": {"claimed": "done"},
                    "event_time": self.t0.isoformat(),
                    "record_time": self.t0.isoformat(),
                    "parent_ids": [parent.evidence_id],
                    "source_refs": [],
                    "influence_roles": ["FORGED"],
                    "effect_action_id": candidate.action_id,
                },
            )

            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(
                    journal,
                    mode="inspect",
                    clock=lambda: self.t0,
                    outcome_source_validator=validator,
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
                source_capability=self.actuator_capability,
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
                source_capability=object(),
                payload={"claimed": "done"},
                effect_action_id=trusted_candidate.action_id,
            )

        outcome = trusted_kernel.observe_effect_outcome(
            source_capability=self.actuator_capability,
            payload={"arm_position": "moved"},
            effect_action_id=trusted_candidate.action_id,
        )
        receipt = trusted_kernel.confirm_effect(
            trusted_candidate.action_id,
            succeeded=True,
            confirmation_evidence_id=outcome.evidence_id,
        )
        self.assertEqual(receipt.state, EffectState.CONFIRMED)

    def test_live_outcome_source_capability_is_required_and_producer_is_derived(self):
        registered_capability = object()
        spoofed_capability = object()
        kernel = self._kernel(
            outcome_source_validator=lambda producer, authority: (
                producer == "actuator-sensor"
            ),
            outcome_source_capabilities=(
                (registered_capability, "actuator-sensor"),
            ),
        )
        grant = self._register(kernel)
        candidate = self._candidate(kernel, grant.grant_id)
        kernel.request_effect(candidate)

        with self.assertRaises(ValueError):
            kernel.observe_effect_outcome(
                source_capability=spoofed_capability,
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )

        with self.assertRaises(TypeError):
            kernel.observe_effect_outcome(
                producer="actuator-sensor",
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )

        outcome = kernel.observe_effect_outcome(
            source_capability=registered_capability,
            payload={"position": "moved"},
            effect_action_id=candidate.action_id,
        )
        self.assertEqual(outcome.producer, "actuator-sensor")

    def test_live_outcome_source_capability_does_not_bypass_source_policy(self):
        registered_capability = object()
        kernel = self._kernel(
            outcome_source_validator=lambda producer, authority: False,
            outcome_source_capabilities=(
                (registered_capability, "actuator-sensor"),
            ),
        )
        grant = self._register(kernel)
        candidate = self._candidate(kernel, grant.grant_id)
        kernel.request_effect(candidate)

        with self.assertRaises(ValueError):
            kernel.observe_effect_outcome(
                source_capability=registered_capability,
                payload={"claimed": "done"},
                effect_action_id=candidate.action_id,
            )
        self.assertEqual(kernel.evidence, {})


    def test_evidence_lineage_fields_reject_non_string_items(self):
        kernel = self._kernel()
        with self.assertRaises(ValueError):
            kernel.observe(
                producer="sensor",
                payload={"x": 1},
                source_refs=({"uri": "sensor://a"},),
            )

        parent = kernel.observe(producer="sensor", payload={"x": 1})
        with self.assertRaises(ValueError):
            kernel.derive(
                producer="cognition",
                epistemic_class=EpistemicClass.DERIVED,
                payload={"x": 2},
                parent_ids=(parent.evidence_id,),
                influence_roles=({"role": "MODEL"},),
            )


    def test_authority_refs_reject_non_string_items(self):
        kernel = self._kernel()
        with self.assertRaises(ValueError):
            kernel.register_grant(
                grantor="authority",
                grantee="kinesis",
                action_scope="MOTOR_EFFECT",
                target_scope="arm",
                basis_refs=({"ticket": "A"},),
                valid_from=self.t0 - timedelta(minutes=1),
                expires_at=self.t0 + timedelta(minutes=5),
            )
        with self.assertRaises(ValueError):
            kernel.register_grant(
                grantor="authority",
                grantee="kinesis",
                action_scope="MOTOR_EFFECT",
                target_scope="arm",
                basis_refs=("basis",),
                provenance=({"issuer": "owner"},),
                valid_from=self.t0 - timedelta(minutes=1),
                expires_at=self.t0 + timedelta(minutes=5),
            )


    def test_memory_and_route_lineage_reject_non_string_items(self):
        kernel = self._kernel()
        with self.assertRaises(ValueError):
            kernel.memory.append(
                logical_key=("world", {"id": 1}, "state", "shared"),
                payload={"v": 1},
                epistemic_class=EpistemicClass.OBSERVATION,
            )
        with self.assertRaises(ValueError):
            kernel.memory.append(
                logical_key=("world", "x", "state", "shared"),
                payload={"v": 1},
                epistemic_class=EpistemicClass.OBSERVATION,
                source_refs=({"source": "A"},),
            )
        with self.assertRaises(ValueError):
            kernel.route(
                source="router",
                audience="consumer",
                payload={"x": 1},
                parent_ids=({"parent": "bad"},),
            )


    def test_effect_candidate_lineage_rejects_non_string_items(self):
        kernel = self._kernel()
        grant = self._register(kernel)
        with self.assertRaises(ValueError):
            kernel.plan_effect(
                origin="kinesis",
                action_scope="MOTOR_EFFECT",
                target_scope="arm",
                payload={"command": "move"},
                authority_grant_id=grant.grant_id,
                parent_ids=({"parent": "bad"},),
            )
        direct = EffectCandidate(
            action_id="action-bad-parent",
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
            planned_epoch=kernel.epoch,
            parent_ids=({"parent": "bad"},),
        )
        with self.assertRaises(ValueError):
            kernel.request_effect(direct)


    @staticmethod
    def _rewrite_last_journal_entry(journal, mutate):
        lines = journal.read_text(encoding="utf-8").splitlines()
        envelope = json.loads(lines[-1])
        mutate(envelope["data"])
        body = {key: value for key, value in envelope.items() if key != "entry_hash"}
        envelope["entry_hash"] = hashlib.sha256(
            json.dumps(
                body,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        lines[-1] = json.dumps(
            envelope,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        journal.write_text("\n".join(lines) + "\n", encoding="utf-8")


    def test_replay_rejects_non_string_evidence_source_refs(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            kernel.observe(
                producer="sensor",
                payload={"x": 1},
                source_refs=("sensor://a",),
            )
            self._rewrite_last_journal_entry(
                journal,
                lambda data: data.__setitem__(
                    "source_refs", [{"uri": "attacker://mutated"}]
                ),
            )
            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(
                    journal,
                    mode="inspect",
                    clock=lambda: self.t0,
                )


    def test_replay_rejects_non_string_authority_refs(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            self._register(kernel)
            self._rewrite_last_journal_entry(
                journal,
                lambda data: data.__setitem__(
                    "basis_refs", [{"ticket": "mutated"}]
                ),
            )
            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(
                    journal,
                    mode="inspect",
                    clock=lambda: self.t0,
                )


    def test_replay_rejects_non_string_memory_refs(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            kernel.memory.append(
                logical_key=("world", "x", "state", "shared"),
                payload={"v": 1},
                epistemic_class=EpistemicClass.OBSERVATION,
                source_refs=("source-A",),
            )
            self._rewrite_last_journal_entry(
                journal,
                lambda data: data.__setitem__(
                    "source_refs", [{"source": "mutated"}]
                ),
            )
            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(journal, mode="inspect", clock=lambda: self.t0)


    def test_replay_rejects_non_string_route_lineage(self):
        with tempfile.TemporaryDirectory() as tempdir:
            journal = Path(tempdir) / "kernel.jsonl"
            kernel = DurableReferenceKernel(journal, clock=lambda: self.t0)
            kernel.route(
                source="router",
                audience="consumer",
                payload={"x": 1},
                parent_ids=("parent-A",),
            )
            self._rewrite_last_journal_entry(
                journal,
                lambda data: data.__setitem__(
                    "parent_ids", [{"parent": "mutated"}]
                ),
            )
            with self.assertRaises(JournalIntegrityError):
                DurableReferenceKernel(journal, mode="inspect", clock=lambda: self.t0)


if __name__ == "__main__":
    unittest.main()
