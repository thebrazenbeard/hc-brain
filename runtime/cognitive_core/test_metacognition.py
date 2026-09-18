import unittest

from runtime.reference_kernel.hc_kernel import EffectState, EpistemicClass, ReferenceKernel
from runtime.cognitive_core.metacognition import (
    CognitiveMonitorState,
    MetacognitiveRuntime,
    Recommendation,
)


class MetacognitiveRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = MetacognitiveRuntime(self.kernel)
        self.obs = self.kernel.observe(
            producer="sensor:test",
            payload={"signal": "ambiguous"},
        )

    def test_monitor_state_is_derived_not_observed_truth(self):
        trace = self.runtime.assess(
            task_id="task:1",
            strategy="interpret",
            parent_evidence_ids=(self.obs.evidence_id,),
            confidence=0.55,
            uncertainty=0.45,
        )
        self.assertEqual(trace.evidence.epistemic_class, EpistemicClass.DERIVED)
        self.assertEqual(trace.state, CognitiveMonitorState.UNCERTAIN)
        self.assertEqual(trace.recommendation, Recommendation.SEEK_EVIDENCE)

    def test_conflict_recommends_broader_arbitration_not_forced_answer(self):
        trace = self.runtime.assess(
            task_id="task:conflict",
            strategy="semantic-arbitration",
            parent_evidence_ids=(self.obs.evidence_id,),
            confidence=0.50,
            uncertainty=0.50,
            conflict=True,
        )
        self.assertEqual(trace.state, CognitiveMonitorState.MODEL_CONFLICT)
        self.assertEqual(trace.recommendation, Recommendation.EXPAND_COALITION)

    def test_repeated_failure_recommends_strategy_revision(self):
        for _ in range(2):
            self.runtime.record_strategy_outcome(
                task_id="task:repeat",
                strategy="route-a",
                success=False,
                evidence_ids=(self.obs.evidence_id,),
            )
        trace = self.runtime.assess(
            task_id="task:repeat",
            strategy="route-a",
            parent_evidence_ids=(self.obs.evidence_id,),
            confidence=0.6,
            uncertainty=0.4,
        )
        self.assertEqual(trace.state, CognitiveMonitorState.STRATEGY_FAILING)
        self.assertEqual(trace.recommendation, Recommendation.REVISE_STRATEGY)

    def test_stale_evidence_recommends_refresh(self):
        trace = self.runtime.assess(
            task_id="task:stale",
            strategy="predict",
            parent_evidence_ids=(self.obs.evidence_id,),
            confidence=0.8,
            uncertainty=0.2,
            evidence_stale=True,
        )
        self.assertEqual(trace.state, CognitiveMonitorState.EVIDENCE_STALE)
        self.assertEqual(trace.recommendation, Recommendation.SEEK_EVIDENCE)

    def test_exhausted_budget_recommends_stop_without_effect_authority(self):
        trace = self.runtime.assess(
            task_id="task:budget",
            strategy="search",
            parent_evidence_ids=(self.obs.evidence_id,),
            confidence=0.4,
            uncertainty=0.6,
            resource_budget_remaining=0.0,
        )
        self.assertEqual(trace.state, CognitiveMonitorState.BUDGET_EXHAUSTED)
        self.assertEqual(trace.recommendation, Recommendation.STOP)
        candidate = self.runtime.recommend_external_action(
            trace.trace_id,
            action_scope="search",
            target_scope="external-tool",
            payload={"query": "more evidence"},
        )
        self.assertIsNone(candidate.authority_grant_id)
        receipt = self.kernel.request_effect(candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)

    def test_assessment_requires_actual_evidence_lineage(self):
        with self.assertRaises(ValueError):
            self.runtime.assess(
                task_id="task:none",
                strategy="guess",
                parent_evidence_ids=(),
                confidence=0.9,
                uncertainty=0.1,
            )

    def test_monitor_does_not_rewrite_parent_evidence(self):
        before = self.kernel.evidence[self.obs.evidence_id]
        self.runtime.assess(
            task_id="task:1",
            strategy="interpret",
            parent_evidence_ids=(self.obs.evidence_id,),
            confidence=0.2,
            uncertainty=0.8,
        )
        after = self.kernel.evidence[self.obs.evidence_id]
        self.assertEqual(before, after)
        self.assertEqual(after.epistemic_class, EpistemicClass.OBSERVATION)


if __name__ == "__main__":
    unittest.main()
