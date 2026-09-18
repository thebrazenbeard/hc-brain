import unittest

from runtime.reference_kernel.hc_kernel import EffectState, EpistemicClass, ReferenceKernel
from runtime.cognitive_core.homeostasis_somatics import (
    BodySchemaRuntime,
    InternalSignalState,
    RegulatoryRuntime,
    RegulatoryTimescale,
)


class RegulatoryRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = RegulatoryRuntime(self.kernel)

    def test_internal_observation_estimate_and_error_remain_distinct(self):
        obs = self.runtime.observe_internal(
            channel="hydration",
            source="sensor:hydration-a",
            value=0.42,
            units="fraction",
            reliability=0.9,
        )
        target = self.runtime.set_target(
            variable="hydration",
            minimum=0.55,
            maximum=0.75,
            basis_refs=("policy:hydration-range",),
        )
        estimate = self.runtime.estimate(
            variable="hydration",
            observation_ids=(obs.observation_id,),
        )
        error = self.runtime.compute_error(
            estimate_id=estimate.estimate_id,
            target_id=target.target_id,
        )
        self.assertEqual(obs.evidence.epistemic_class, EpistemicClass.OBSERVATION)
        self.assertEqual(estimate.evidence.epistemic_class, EpistemicClass.INFERRED)
        self.assertEqual(error.evidence.epistemic_class, EpistemicClass.DERIVED)
        self.assertGreater(error.magnitude, 0.0)
        self.assertEqual(error.direction, "LOW")

    def test_sensor_disagreement_remains_explicit(self):
        a = self.runtime.observe_internal(
            channel="temperature",
            source="sensor:t-a",
            value=0.20,
            units="normalized",
            reliability=0.9,
        )
        b = self.runtime.observe_internal(
            channel="temperature",
            source="sensor:t-b",
            value=0.90,
            units="normalized",
            reliability=0.9,
        )
        estimate = self.runtime.estimate(
            variable="temperature",
            observation_ids=(a.observation_id, b.observation_id),
            conflict_threshold=0.25,
        )
        self.assertEqual(estimate.signal_state, InternalSignalState.SENSOR_CONFLICT)
        self.assertLess(estimate.confidence, 0.9)

    def test_urgency_does_not_authorize_external_action(self):
        obs = self.runtime.observe_internal(
            channel="energy",
            source="sensor:energy",
            value=0.10,
            units="fraction",
            reliability=1.0,
        )
        target = self.runtime.set_target(
            variable="energy",
            minimum=0.60,
            maximum=0.90,
            basis_refs=("policy:energy-range",),
        )
        estimate = self.runtime.estimate(
            variable="energy",
            observation_ids=(obs.observation_id,),
        )
        error = self.runtime.compute_error(
            estimate_id=estimate.estimate_id,
            target_id=target.target_id,
        )
        request = self.runtime.propose_regulation(
            error_id=error.error_id,
            effect_scope="obtain-energy",
            target_scope="external-environment",
            payload={"request": "food"},
            timescale=RegulatoryTimescale.SHORT_REGULATORY,
        )
        self.assertGreater(request.urgency, 0.0)
        self.assertIsNone(request.action_candidate.authority_grant_id)
        receipt = self.kernel.request_effect(request.action_candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "MISSING_AUTHORITY")

    def test_local_protective_control_is_narrow_and_cannot_expand_scope(self):
        self.runtime.register_protective_scope(
            effect_scope="thermal-throttle",
            target_scope="internal:compute",
            minimum=0.0,
            maximum=1.0,
            basis_refs=("safety:thermal-envelope",),
        )
        decision = self.runtime.apply_local_protective_effect(
            effect_scope="thermal-throttle",
            target_scope="internal:compute",
            value=0.8,
            reason_refs=("sensor:thermal-critical",),
        )
        self.assertEqual(decision.status, "APPLIED_LOCAL_PROTECTIVE")
        with self.assertRaises(PermissionError):
            self.runtime.apply_local_protective_effect(
                effect_scope="thermal-throttle",
                target_scope="external:building",
                value=0.8,
                reason_refs=("sensor:thermal-critical",),
            )

    def test_target_change_requires_explicit_provenance(self):
        target = self.runtime.set_target(
            variable="temperature",
            minimum=0.35,
            maximum=0.55,
            basis_refs=("policy:temperature-v1",),
        )
        with self.assertRaises(ValueError):
            self.runtime.revise_target(
                target.target_id,
                minimum=0.40,
                maximum=0.60,
                basis_refs=(),
            )
        revised = self.runtime.revise_target(
            target.target_id,
            minimum=0.40,
            maximum=0.60,
            basis_refs=("policy:temperature-v2",),
        )
        self.assertEqual(revised.supersedes, (target.target_id,))
        self.assertIn(target.target_id, self.runtime.targets)


class BodySchemaRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = BodySchemaRuntime(self.kernel)

    def test_body_schema_begins_uncalibrated_and_morphology_neutral(self):
        state = self.runtime.current_schema
        self.assertEqual(state.calibration_status, "UNCALIBRATED")
        self.assertEqual(state.morphology, {})
        self.assertEqual(state.calibration_confidence, 0.0)

    def test_calibration_requires_observed_somatic_evidence(self):
        obs = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"joint": "elbow", "angle": 45},
        )
        schema = self.runtime.calibrate(
            morphology={"segments": ["upper-arm", "forearm"]},
            pose={"elbow_angle": 45},
            actuator_capabilities={"elbow": {"range": [0, 135]}},
            evidence_ids=(obs.evidence_id,),
            confidence=0.8,
        )
        self.assertEqual(schema.calibration_status, "CALIBRATED")
        self.assertEqual(schema.calibration_confidence, 0.8)

    def test_predicted_evidence_cannot_masquerade_as_lived_calibration(self):
        obs = self.kernel.observe(producer="sensor:test", payload={"seed": True})
        pred = self.kernel.derive(
            producer="cognition:simulation",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={"elbow_angle": 90},
            parent_ids=(obs.evidence_id,),
        )
        with self.assertRaises(ValueError):
            self.runtime.calibrate(
                morphology={"segments": ["arm"]},
                pose={"elbow_angle": 90},
                actuator_capabilities={},
                evidence_ids=(pred.evidence_id,),
                confidence=0.7,
            )

    def test_pose_update_preserves_calibration_and_source_lineage(self):
        obs = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"joint": "elbow", "angle": 45},
        )
        first = self.runtime.calibrate(
            morphology={"segments": ["arm"]},
            pose={"elbow_angle": 45},
            actuator_capabilities={},
            evidence_ids=(obs.evidence_id,),
            confidence=0.8,
        )
        obs2 = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"joint": "elbow", "angle": 70},
        )
        updated = self.runtime.update_pose(
            pose={"elbow_angle": 70},
            evidence_ids=(obs2.evidence_id,),
            confidence=0.9,
        )
        self.assertEqual(updated.morphology, first.morphology)
        self.assertIn(obs2.evidence_id, updated.source_evidence_ids)
        self.assertEqual(updated.pose["elbow_angle"], 70)

    def test_reachability_is_prediction_not_current_body_fact(self):
        obs = self.kernel.observe(
            producer="sensor:proprioception",
            payload={"joint": "arm", "state": "ready"},
        )
        self.runtime.calibrate(
            morphology={"segments": ["arm"]},
            pose={"arm": "neutral"},
            actuator_capabilities={"arm": {"reach": 1.0}},
            evidence_ids=(obs.evidence_id,),
            confidence=0.8,
        )
        reach = self.runtime.predict_reachability(
            target={"distance": 0.8},
            confidence=0.75,
        )
        self.assertEqual(reach.evidence.epistemic_class, EpistemicClass.PREDICTION)
        self.assertEqual(reach.status, "PREDICTED_REACHABILITY")


class EmbodiedCognitionIntegrationTests(unittest.TestCase):
    def test_regulatory_pressure_modulates_salience_without_changing_confidence(self):
        from runtime.cognitive_core.cognitive_loop import CognitiveRuntime
        cognitive = CognitiveRuntime(ReferenceKernel())
        regulatory = RegulatoryRuntime(cognitive.kernel)

        baseline = cognitive.process_observation(
            producer="sensor:task",
            payload={"cue": "work"},
            concept_id="concept:work",
            proposition="work cue present",
            confidence=0.63,
            novelty=0.2,
        )

        obs = regulatory.observe_internal(
            channel="energy",
            source="sensor:energy",
            value=0.10,
            units="fraction",
            reliability=1.0,
        )
        target = regulatory.set_target(
            variable="energy",
            minimum=0.60,
            maximum=0.90,
            basis_refs=("policy:energy-range",),
        )
        estimate = regulatory.estimate(
            variable="energy",
            observation_ids=(obs.observation_id,),
        )
        error = regulatory.compute_error(
            estimate_id=estimate.estimate_id,
            target_id=target.target_id,
        )
        modulation = regulatory.build_affective_modulation(error.error_id)
        cognitive.apply_regulatory_modulation(modulation)

        modulated = cognitive.process_observation(
            producer="sensor:task",
            payload={"cue": "work"},
            concept_id="concept:work",
            proposition="work cue present",
            confidence=0.63,
            novelty=0.2,
        )
        self.assertGreater(modulated.attention.score, baseline.attention.score)
        self.assertEqual(modulated.interpretation.payload["confidence"], 0.63)

    def test_body_prediction_lineage_reaches_world_model_without_becoming_observation(self):
        from runtime.cognitive_core.world_model import CausalSupport, WorldModelRuntime
        kernel = ReferenceKernel()
        body = BodySchemaRuntime(kernel)
        world = WorldModelRuntime(kernel)

        proprio = kernel.observe(
            producer="sensor:proprioception",
            payload={"arm": "neutral"},
        )
        body.calibrate(
            morphology={"segments": ["arm"]},
            pose={"arm": "neutral"},
            actuator_capabilities={"arm": {"reach": 1.0}},
            evidence_ids=(proprio.evidence_id,),
            confidence=0.8,
        )
        reach = body.predict_reachability(
            target={"distance": 0.8},
            confidence=0.75,
        )
        model = world.propose_model(
            model_id="model:reach-plan",
            target="reach-success",
            relation="reachable targets are more likely to succeed",
            confidence=0.70,
            source_evidence_ids=(proprio.evidence_id,),
            support=CausalSupport.OBSERVATIONAL,
        )
        forecast = world.forecast(
            model_id=model.model_id,
            target="reach-success",
            expected={"success": True},
            horizon="ACTION_CONDITIONAL",
            confidence=0.95,
            parent_evidence_ids=(reach.evidence.evidence_id,),
            action_conditional=True,
        )
        self.assertIn(proprio.evidence_id, forecast.observed_ancestor_ids)
        self.assertIn(reach.evidence.evidence_id, forecast.generated_ancestor_ids)
        self.assertLessEqual(forecast.confidence, 0.75)
        self.assertEqual(reach.evidence.epistemic_class, EpistemicClass.PREDICTION)


if __name__ == "__main__":
    unittest.main()
