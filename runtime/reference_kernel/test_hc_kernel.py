from datetime import datetime, timedelta, timezone
import unittest

from hc_kernel import EpistemicClass, EffectState, ProjectionStatus, ReferenceKernel

UTC = timezone.utc


class ReferenceKernelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 10, 18, 0, tzinfo=UTC)
        self.kernel = ReferenceKernel(
            clock=lambda: self.now,
            outcome_source_validator=lambda producer, authority: (
                producer == "somatics"
            ),
        )

    def _grant(self, action_scope="MOTOR_EFFECT", target_scope="arm"):
        return self.kernel.register_grant(
            grantor="authority-fixture",
            grantee="kinesis",
            action_scope=action_scope,
            target_scope=target_scope,
            basis_refs=("fixture-basis",),
            provenance=("unit-test",),
            valid_from=self.now - timedelta(minutes=1),
            expires_at=self.now + timedelta(minutes=10),
        )

    def test_authority_registration_requires_explicit_basis(self):
        with self.assertRaises(ValueError):
            self.kernel.register_grant(
                grantor="authority-fixture",
                grantee="kinesis",
                action_scope="MOTOR_EFFECT",
                target_scope="arm",
                basis_refs=(),
                valid_from=self.now - timedelta(minutes=1),
                expires_at=self.now + timedelta(minutes=10),
            )

    def test_routed_high_priority_event_does_not_authorize_effect(self):
        routed = self.kernel.route(
            source="salience-attention",
            audience="kinesis",
            payload={"urge": "move"},
            priority=100,
        )
        self.assertNotIn(routed.event_id, self.kernel.incorporated_event_ids)

        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=None,
            parent_ids=(routed.event_id,),
        )
        receipt = self.kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "MISSING_AUTHORITY")

    def test_prediction_cannot_be_relabeled_as_observation(self):
        observation = self.kernel.observe(
            producer="optics",
            payload={"object": "ball"},
            source_refs=("camera-1",),
        )
        prediction = self.kernel.derive(
            producer="cognition",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={"next": "ball_moves"},
            parent_ids=(observation.evidence_id,),
            influence_roles=("WORLD_MODEL_INPUT",),
        )
        self.assertEqual(prediction.epistemic_class, EpistemicClass.PREDICTION)
        self.assertIn(observation.evidence_id, prediction.parent_ids)
        self.assertIn("camera-1", prediction.source_refs)

        with self.assertRaises(ValueError):
            self.kernel.derive(
                producer="cognition",
                epistemic_class=EpistemicClass.OBSERVATION,
                payload={"bad": True},
                parent_ids=(observation.evidence_id,),
            )

    def test_current_projection_fails_closed_on_competing_heads(self):
        key = ("identity", "self", "name", "private")
        first = self.kernel.memory.append(
            logical_key=key,
            payload="A",
            epistemic_class=EpistemicClass.OBSERVATION,
        )
        second = self.kernel.memory.append(
            logical_key=key,
            payload="B",
            epistemic_class=EpistemicClass.OBSERVATION,
        )
        projection = self.kernel.memory.current(key)
        self.assertEqual(projection.status, ProjectionStatus.AMBIGUOUS)
        self.assertEqual(set(projection.head_ids), {first.record_id, second.record_id})

        resolved = self.kernel.memory.append(
            logical_key=key,
            payload="C",
            epistemic_class=EpistemicClass.DERIVED,
            supersedes=(first.record_id, second.record_id),
        )
        projection = self.kernel.memory.current(key)
        self.assertEqual(projection.status, ProjectionStatus.CURRENT)
        self.assertEqual(projection.head_ids, (resolved.record_id,))
        self.assertEqual(projection.payload, "C")
        self.assertEqual(projection.epistemic_class, EpistemicClass.DERIVED)

    def test_supersession_cannot_cross_logical_scope(self):
        first = self.kernel.memory.append(
            logical_key=("world", "x", "state", "shared"),
            payload=1,
            epistemic_class=EpistemicClass.OBSERVATION,
        )
        with self.assertRaises(ValueError):
            self.kernel.memory.append(
                logical_key=("world", "y", "state", "shared"),
                payload=2,
                epistemic_class=EpistemicClass.DERIVED,
                supersedes=(first.record_id,),
            )

    def test_expired_authority_blocks_effect_request(self):
        grant = self.kernel.register_grant(
            grantor="authority-fixture",
            grantee="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            basis_refs=("fixture-basis",),
            valid_from=self.now - timedelta(minutes=10),
            expires_at=self.now - timedelta(seconds=1),
        )
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        receipt = self.kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "EXPIRED_AUTHORITY")

    def test_revocation_after_planning_blocks_effect_request(self):
        grant = self._grant()
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        self.kernel.revoke_grant(
            grant.grant_id,
            revoked_at=self.now - timedelta(seconds=1),
        )
        receipt = self.kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "REVOKED_AUTHORITY")

    def test_requested_effect_is_not_confirmed_effect(self):
        grant = self._grant()
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        requested = self.kernel.request_effect(candidate)
        self.assertEqual(requested.state, EffectState.REQUESTED)

        confirmation = self.kernel.observe_effect_outcome(
            producer="somatics",
            payload={"arm_position": "moved"},
            source_refs=("proprioception",),
            effect_action_id=candidate.action_id,
        )
        confirmed = self.kernel.confirm_effect(
            candidate.action_id,
            succeeded=True,
            confirmation_evidence_id=confirmation.evidence_id,
        )
        self.assertEqual(confirmed.state, EffectState.CONFIRMED)

    def test_unrelated_observation_cannot_confirm_effect(self):
        grant = self._grant()
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        self.kernel.request_effect(candidate)
        unrelated = self.kernel.observe(
            producer="somatics",
            payload={"temperature": 37},
            source_refs=("thermistor",),
        )
        with self.assertRaises(ValueError):
            self.kernel.confirm_effect(
                candidate.action_id,
                succeeded=True,
                confirmation_evidence_id=unrelated.evidence_id,
            )

    def test_duplicate_request_does_not_redispatch(self):
        grant = self._grant()
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        first = self.kernel.request_effect(candidate)
        second = self.kernel.request_effect(candidate)
        self.assertIs(first, second)
        self.assertEqual(first.dispatch_attempts, 1)

    def test_restart_marks_inflight_effect_unresolved_and_blocks_replay(self):
        grant = self._grant()
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        requested = self.kernel.request_effect(candidate)
        self.assertEqual(requested.state, EffectState.REQUESTED)

        self.kernel.restart()
        unresolved = self.kernel.effect_receipts[candidate.action_id]
        self.assertEqual(unresolved.state, EffectState.UNRESOLVED_AFTER_RESTART)

        repeated = self.kernel.request_effect(candidate)
        self.assertIs(repeated, unresolved)
        self.assertEqual(repeated.dispatch_attempts, 1)

        old_grant_candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "new_action"},
            authority_grant_id=grant.grant_id,
        )
        retry_receipt = self.kernel.request_effect(old_grant_candidate)
        self.assertEqual(retry_receipt.state, EffectState.BLOCKED)
        self.assertEqual(retry_receipt.reason, "STALE_AUTHORITY_EPOCH")

    def test_pre_restart_plan_is_stale_after_restart(self):
        grant = self._grant()
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope="MOTOR_EFFECT",
            target_scope="arm",
            payload={"command": "move"},
            authority_grant_id=grant.grant_id,
        )
        self.kernel.restart()
        receipt = self.kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "STALE_PLAN_EPOCH")


if __name__ == "__main__":
    unittest.main()
