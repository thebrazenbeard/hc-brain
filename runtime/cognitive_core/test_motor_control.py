import unittest

from runtime.reference_kernel.hc_kernel import EffectState, EpistemicClass, ReferenceKernel
from runtime.cognitive_core.homeostasis_somatics import BodySchemaRuntime
from runtime.cognitive_core.motor_control import (
    MotorControlRuntime,
    MotorPlanState,
    SkillState,
)


class MotorControlRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.body = BodySchemaRuntime(self.kernel)
        self.runtime = MotorControlRuntime(self.kernel, self.body)

    def _calibrate_arm(self, reach=1.0):
        obs = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"arm": "neutral"},
        )
        return self.body.calibrate(
            morphology={"segments": ["arm"]},
            pose={"arm": "neutral"},
            actuator_capabilities={
                "arm": {
                    "reach": reach,
                    "max_effort": 1.0,
                    "max_speed": 1.0,
                }
            },
            evidence_ids=(obs.evidence_id,),
            confidence=0.9,
        )

    def test_uncalibrated_body_blocks_motor_plan(self):
        with self.assertRaises(ValueError):
            self.runtime.plan_movement(
                effector="arm",
                target={"distance": 0.5},
                action_scope="reach",
                target_scope="object",
                payload={"target": "object"},
            )

    def test_motor_plan_is_derived_candidate_bound_to_body_schema(self):
        schema = self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        self.assertEqual(plan.state, MotorPlanState.PLANNED)
        self.assertEqual(plan.body_schema_id, schema.schema_id)
        self.assertEqual(plan.evidence.epistemic_class, EpistemicClass.DERIVED)

    def test_unreachable_target_fails_before_action_candidate(self):
        self._calibrate_arm(reach=0.5)
        with self.assertRaises(ValueError):
            self.runtime.plan_movement(
                effector="arm",
                target={"distance": 0.8},
                action_scope="reach",
                target_scope="object",
                payload={"target": "object"},
            )
        self.assertEqual(self.runtime.plans, {})

    def test_motor_plan_produces_effect_candidate_without_authority(self):
        self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        self.assertIsNone(plan.action_candidate.authority_grant_id)
        receipt = self.kernel.request_effect(plan.action_candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "MISSING_AUTHORITY")

    def test_body_schema_change_makes_preexisting_plan_stale(self):
        self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        obs2 = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"arm": "raised"},
        )
        self.body.update_pose(
            pose={"arm": "raised"},
            evidence_ids=(obs2.evidence_id,),
            confidence=0.9,
        )
        checked = self.runtime.validate_plan(plan.plan_id)
        self.assertEqual(checked.state, MotorPlanState.STALE_BODY_SCHEMA)

    def test_trajectory_prediction_is_not_current_pose(self):
        self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        trajectory = self.runtime.predict_trajectory(
            plan.plan_id,
            waypoints=(
                {"distance": 0.2},
                {"distance": 0.5},
            ),
            confidence=0.8,
        )
        self.assertEqual(trajectory.evidence.epistemic_class, EpistemicClass.PREDICTION)
        self.assertEqual(trajectory.status, "PREDICTED_TRAJECTORY")

    def test_local_stabilization_is_bounded_to_registered_effector(self):
        self._calibrate_arm()
        self.runtime.register_local_stabilizer(
            effector="arm",
            max_adjustment=0.2,
            basis_refs=("safety:arm-stabilizer",),
        )
        adjustment = self.runtime.plan_local_stabilization(
            effector="arm",
            adjustment=0.1,
            reason_refs=("sensor:pose-error",),
        )
        self.assertEqual(adjustment.status, "PLANNED_LOCAL_STABILIZATION_NO_EFFECT")
        self.assertEqual(dict(self.kernel.effect_receipts), {})
        with self.assertRaises(PermissionError):
            self.runtime.plan_local_stabilization(
                effector="leg",
                adjustment=0.1,
                reason_refs=("sensor:pose-error",),
            )

    def test_observed_motor_outcome_can_create_skill_candidate(self):
        self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        outcome = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"reach": "successful"},
        )
        skill = self.runtime.record_observed_outcome(
            plan.plan_id,
            observation_evidence_id=outcome.evidence_id,
            success=True,
        )
        self.assertEqual(skill.state, SkillState.CANDIDATE)
        self.assertIn(outcome.evidence_id, skill.source_evidence_ids)

    def test_simulated_outcome_cannot_qualify_motor_skill(self):
        self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        simulated = self.kernel.derive(
            producer="cognition:simulation",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={"reach": "successful"},
            parent_ids=(plan.evidence.evidence_id,),
        )
        with self.assertRaises(ValueError):
            self.runtime.record_observed_outcome(
                plan.plan_id,
                observation_evidence_id=simulated.evidence_id,
                success=True,
            )

    def test_skill_consolidation_requires_explicit_basis(self):
        self._calibrate_arm()
        plan = self.runtime.plan_movement(
            effector="arm",
            target={"distance": 0.5},
            action_scope="reach",
            target_scope="object",
            payload={"target": "object"},
        )
        outcome = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"reach": "successful"},
        )
        skill = self.runtime.record_observed_outcome(
            plan.plan_id,
            observation_evidence_id=outcome.evidence_id,
            success=True,
        )
        with self.assertRaises(ValueError):
            self.runtime.consolidate_skill(skill.skill_id, basis_refs=())
        consolidated = self.runtime.consolidate_skill(
            skill.skill_id,
            basis_refs=("evaluation:repeated-success",),
        )
        self.assertEqual(consolidated.state, SkillState.CONSOLIDATED)


if __name__ == "__main__":
    unittest.main()
