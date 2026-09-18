import unittest

from runtime.reference_kernel.hc_kernel import EffectState, EpistemicClass, ReferenceKernel
from runtime.cognitive_core.world_model import (
    CausalSupport,
    ModelLifecycle,
    WorldModelRuntime,
)


class WorldModelRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = WorldModelRuntime(self.kernel)
        self.obs = self.kernel.observe(
            producer="sensor:environment",
            payload={"temperature": 20},
        )
        self.model = self.runtime.propose_model(
            model_id="model:temperature",
            target="temperature",
            relation="temperature trends upward",
            confidence=0.70,
            source_evidence_ids=(self.obs.evidence_id,),
            support=CausalSupport.OBSERVATIONAL,
        )

    def test_model_is_inferred_structure_not_world_state(self):
        self.assertEqual(self.model.evidence.epistemic_class, EpistemicClass.INFERRED)
        self.assertEqual(self.model.lifecycle, ModelLifecycle.ACTIVE)
        self.assertEqual(self.model.source_evidence_ids, (self.obs.evidence_id,))

    def test_forecast_is_prediction_with_observed_ancestry(self):
        forecast = self.runtime.forecast(
            model_id=self.model.model_id,
            target="temperature",
            expected={"value": 22},
            horizon="PT1H",
            confidence=0.65,
            parent_evidence_ids=(self.obs.evidence_id,),
        )
        self.assertEqual(forecast.evidence.epistemic_class, EpistemicClass.PREDICTION)
        self.assertIn(self.obs.evidence_id, forecast.observed_ancestor_ids)
        self.assertEqual(forecast.generated_ancestor_ids, ())

    def test_descendant_forecast_inherits_generated_ancestry_and_confidence_ceiling(self):
        first = self.runtime.forecast(
            model_id=self.model.model_id,
            target="temperature",
            expected={"value": 22},
            horizon="PT1H",
            confidence=0.65,
            parent_evidence_ids=(self.obs.evidence_id,),
        )
        second = self.runtime.forecast(
            model_id=self.model.model_id,
            target="temperature",
            expected={"value": 24},
            horizon="PT2H",
            confidence=0.95,
            parent_forecast_ids=(first.forecast_id,),
        )
        self.assertIn(first.forecast_id, second.generated_ancestor_ids)
        self.assertIn(self.obs.evidence_id, second.observed_ancestor_ids)
        self.assertLessEqual(second.confidence, first.confidence)

    def test_counterfactual_remains_simulated_and_does_not_write_history(self):
        before = len(self.kernel.memory.records)
        simulation = self.runtime.simulate_counterfactual(
            goal="test cooling intervention",
            model_id=self.model.model_id,
            base_evidence_ids=(self.obs.evidence_id,),
            hypothetical_modifications={"cooling": "enabled"},
            generated_outcomes={"temperature": 18},
            confidence=0.60,
        )
        self.assertEqual(simulation.provenance, "SIMULATED")
        self.assertEqual(simulation.evidence.epistemic_class, EpistemicClass.PREDICTION)
        self.assertEqual(len(self.kernel.memory.records), before)

    def test_rehearsal_creates_action_candidate_without_authority(self):
        plan = self.runtime.rehearse_action(
            model_id=self.model.model_id,
            action_scope="cool",
            target_scope="room",
            payload={"setpoint": 18},
            predicted_outcome={"temperature": 18},
            confidence=0.70,
            parent_evidence_ids=(self.obs.evidence_id,),
        )
        self.assertIsNone(plan.action_candidate.authority_grant_id)
        self.assertTrue(plan.forecast.action_conditional)
        receipt = self.kernel.request_effect(plan.action_candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "MISSING_AUTHORITY")

    def test_contradicted_forecast_marks_descendants_for_reevaluation_without_deleting_history(self):
        first = self.runtime.forecast(
            model_id=self.model.model_id,
            target="temperature",
            expected={"value": 22},
            horizon="PT1H",
            confidence=0.65,
            parent_evidence_ids=(self.obs.evidence_id,),
        )
        second = self.runtime.forecast(
            model_id=self.model.model_id,
            target="temperature",
            expected={"value": 24},
            horizon="PT2H",
            confidence=0.60,
            parent_forecast_ids=(first.forecast_id,),
        )
        actual = self.kernel.observe(
            producer="sensor:environment",
            payload={"temperature": 19},
        )
        reconciliation = self.runtime.reconcile_forecast(
            first.forecast_id,
            observation_evidence_id=actual.evidence_id,
            matched=False,
        )
        self.assertEqual(reconciliation.status, "CONTRADICTED")
        self.assertEqual(self.runtime.forecast_state(first.forecast_id).status, "CONTRADICTED")
        self.assertEqual(self.runtime.forecast_state(second.forecast_id).status, "STALE_REEVALUATE")
        self.assertIn(first.forecast_id, self.runtime.forecasts)

    def test_model_revision_preserves_superseded_model(self):
        new_obs = self.kernel.observe(
            producer="sensor:environment",
            payload={"temperature": 19},
        )
        revised = self.runtime.revise_model(
            self.model.model_id,
            new_model_id="model:temperature-v2",
            relation="temperature is stable",
            confidence=0.80,
            source_evidence_ids=(new_obs.evidence_id,),
        )
        self.assertEqual(self.runtime.models[self.model.model_id].lifecycle, ModelLifecycle.SUPERSEDED)
        self.assertEqual(revised.lifecycle, ModelLifecycle.ACTIVE)
        self.assertIn(self.model.model_id, revised.supersedes)

    def test_rival_models_can_coexist_without_forced_unique_truth(self):
        rival = self.runtime.propose_model(
            model_id="model:temperature-rival",
            target="temperature",
            relation="temperature is stable",
            confidence=0.68,
            source_evidence_ids=(self.obs.evidence_id,),
            support=CausalSupport.OBSERVATIONAL,
        )
        rivals = self.runtime.models_for_target("temperature")
        self.assertEqual({item.model_id for item in rivals}, {self.model.model_id, rival.model_id})
        self.assertTrue(all(item.lifecycle == ModelLifecycle.ACTIVE for item in rivals))


if __name__ == "__main__":
    unittest.main()
