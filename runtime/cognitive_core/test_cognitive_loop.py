import unittest

from runtime.reference_kernel.hc_kernel import EffectState, EpistemicClass, ReferenceKernel
from runtime.cognitive_core.cognitive_loop import (
    AffectState,
    Concern,
    CognitiveRuntime,
    ConcernState,
)


class CognitiveRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = CognitiveRuntime(self.kernel)

    def test_observation_becomes_inferred_hypothesis_and_working_memory(self):
        result = self.runtime.process_observation(
            producer="sensor:vision",
            payload={"object": "door", "state": "closed"},
            concept_id="concept:door-state",
            proposition="the door is closed",
            confidence=0.82,
            novelty=0.4,
        )
        self.assertEqual(result.observation.epistemic_class, EpistemicClass.OBSERVATION)
        self.assertEqual(result.interpretation.epistemic_class, EpistemicClass.INFERRED)
        self.assertEqual(result.interpretation.parent_ids, (result.observation.evidence_id,))
        current = self.kernel.memory.current(result.working_memory.logical_key)
        self.assertEqual(current.epistemic_class, EpistemicClass.INFERRED)
        self.assertEqual(current.payload["proposition"], "the door is closed")

    def test_affect_and_concern_raise_salience_without_changing_confidence(self):
        base = self.runtime.process_observation(
            producer="sensor:test",
            payload={"cue": "x"},
            concept_id="concept:x",
            proposition="x is present",
            confidence=0.61,
            novelty=0.2,
        )
        self.runtime.set_affect(AffectState(valence=-0.4, arousal=0.9, threat=0.8, source_refs=("body:1",)))
        self.runtime.set_concern(
            Concern(
                concern_id="concern:protect",
                target_concept="concept:x",
                strength=0.9,
                state=ConcernState.PRESENT,
                provenance=("commitment:1",),
            )
        )
        modulated = self.runtime.process_observation(
            producer="sensor:test",
            payload={"cue": "x"},
            concept_id="concept:x",
            proposition="x is present",
            confidence=0.61,
            novelty=0.2,
        )
        self.assertGreater(modulated.attention.score, base.attention.score)
        self.assertEqual(modulated.interpretation.payload["confidence"], 0.61)

    def test_action_candidate_is_not_authorization(self):
        self.runtime.set_concern(
            Concern(
                concern_id="concern:inspect",
                target_concept="concept:door",
                strength=0.8,
                state=ConcernState.PRESENT,
                provenance=("task:1",),
            )
        )
        result = self.runtime.process_observation(
            producer="sensor:vision",
            payload={"door": "closed"},
            concept_id="concept:door",
            proposition="door is closed",
            confidence=0.9,
            novelty=0.5,
            action_options=(
                {"action_scope": "inspect", "target_scope": "door", "payload": {"mode": "visual"}},
            ),
        )
        self.assertIsNotNone(result.action_candidate)
        self.assertIsNone(result.action_candidate.authority_grant_id)
        receipt = self.kernel.request_effect(result.action_candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "MISSING_AUTHORITY")

    def test_coalition_is_bounded_and_expires(self):
        result = self.runtime.process_observation(
            producer="sensor:test",
            payload={"x": 1},
            concept_id="concept:x",
            proposition="x",
            confidence=0.7,
            novelty=0.5,
        )
        cid = result.coalition.coalition_id
        self.assertIn(cid, self.runtime.active_coalitions)
        self.runtime.advance_cycle()
        self.assertNotIn(cid, self.runtime.active_coalitions)

    def test_salient_event_creates_memory_candidate_not_deep_memory_admission(self):
        result = self.runtime.process_observation(
            producer="sensor:test",
            payload={"surprise": True},
            concept_id="concept:surprise",
            proposition="unexpected event occurred",
            confidence=0.75,
            novelty=1.0,
            contradiction=0.8,
        )
        self.assertIsNotNone(result.memory_candidate)
        self.assertEqual(self.runtime.deep_memory, ())
        self.assertEqual(result.memory_candidate.status, "CANDIDATE")

    def test_repeated_route_proposes_plasticity_but_does_not_commit_it(self):
        last = None
        for _ in range(3):
            last = self.runtime.process_observation(
                producer="sensor:test",
                payload={"pattern": "repeat"},
                concept_id="concept:repeat",
                proposition="repeat pattern",
                confidence=0.7,
                novelty=0.3,
            )
        self.assertIsNotNone(last.plasticity_candidate)
        self.assertEqual(last.plasticity_candidate.status, "PROPOSED")
        self.assertEqual(self.runtime.committed_plasticity, ())

    def test_self_relevance_creates_candidate_without_mutating_identity(self):
        result = self.runtime.process_observation(
            producer="sensor:self",
            payload={"capability": "changed"},
            concept_id="concept:self-capability",
            proposition="my capability may have changed",
            confidence=0.55,
            novelty=0.7,
            self_relevance=True,
        )
        self.assertIsNotNone(result.self_model_candidate)
        self.assertEqual(self.runtime.self_model, {})
        self.assertEqual(result.self_model_candidate.status, "CANDIDATE")

    def test_correction_supersedes_only_same_current_memory_scope(self):
        first = self.runtime.process_observation(
            producer="sensor:test",
            payload={"state": "old"},
            concept_id="concept:state",
            proposition="state is old",
            confidence=0.7,
            novelty=0.2,
        )
        other = self.runtime.process_observation(
            producer="sensor:test",
            payload={"state": "other"},
            concept_id="concept:other",
            proposition="other remains",
            confidence=0.7,
            novelty=0.2,
        )
        corrected = self.runtime.process_observation(
            producer="sensor:test",
            payload={"state": "new"},
            concept_id="concept:state",
            proposition="state is new",
            confidence=0.95,
            novelty=0.4,
            contradiction=1.0,
            correction=True,
        )
        current = self.kernel.memory.current(first.working_memory.logical_key)
        other_current = self.kernel.memory.current(other.working_memory.logical_key)
        self.assertEqual(current.payload["proposition"], "state is new")
        self.assertEqual(other_current.payload["proposition"], "other remains")
        self.assertIn(first.working_memory.record_id, corrected.working_memory.supersedes)


    def test_deep_memory_admission_is_explicit_and_requires_basis(self):
        result = self.runtime.process_observation(
            producer="sensor:test",
            payload={"event": "important"},
            concept_id="concept:important",
            proposition="important event",
            confidence=0.8,
            novelty=1.0,
            contradiction=0.7,
        )
        with self.assertRaises(ValueError):
            self.runtime.admit_deep_memory(result.memory_candidate, basis_refs=())
        admitted = self.runtime.admit_deep_memory(
            result.memory_candidate,
            basis_refs=("policy:memory-admission",),
        )
        self.assertEqual(admitted.status, "ADMITTED")
        self.assertEqual(len(self.runtime.deep_memory), 1)

    def test_self_model_requires_explicit_admission_basis(self):
        result = self.runtime.process_observation(
            producer="sensor:self",
            payload={"skill": "new"},
            concept_id="concept:self-skill",
            proposition="I may have learned a skill",
            confidence=0.7,
            novelty=0.8,
            self_relevance=True,
        )
        with self.assertRaises(ValueError):
            self.runtime.admit_self_model(result.self_model_candidate, basis_refs=())
        assertion = self.runtime.admit_self_model(
            result.self_model_candidate,
            basis_refs=("evidence:qualified-self-test",),
        )
        self.assertEqual(assertion["proposition"], "I may have learned a skill")
        self.assertIn("concept:self-skill", self.runtime.self_model)

    def test_plasticity_commit_requires_basis_and_changes_future_routing_only(self):
        last = None
        for _ in range(3):
            last = self.runtime.process_observation(
                producer="sensor:test",
                payload={"pattern": "learnable"},
                concept_id="concept:learnable",
                proposition="learnable pattern",
                confidence=0.66,
                novelty=0.6,
            )
        before_priority = last.routed_event.priority
        with self.assertRaises(ValueError):
            self.runtime.commit_plasticity(last.plasticity_candidate, basis_refs=())
        committed = self.runtime.commit_plasticity(
            last.plasticity_candidate,
            basis_refs=("evaluation:route-benefit",),
        )
        self.assertEqual(committed.status, "COMMITTED")
        after = self.runtime.process_observation(
            producer="sensor:test",
            payload={"pattern": "learnable"},
            concept_id="concept:learnable",
            proposition="learnable pattern",
            confidence=0.66,
            novelty=0.6,
        )
        self.assertGreaterEqual(after.routed_event.priority, before_priority)
        self.assertEqual(after.interpretation.payload["confidence"], 0.66)

    def test_affect_decays_without_new_driving_input(self):
        self.runtime.set_affect(
            AffectState(valence=-0.5, arousal=1.0, threat=0.8, source_refs=("body:1",))
        )
        before = self.runtime.affect
        self.runtime.advance_cycle()
        after = self.runtime.affect
        self.assertLess(after.arousal, before.arousal)
        self.assertLess(after.threat, before.threat)

    def test_concern_lifecycle_is_traceable(self):
        concern = Concern(
            concern_id="concern:learn",
            target_concept="concept:learn",
            strength=0.7,
            state=ConcernState.PRESENT,
            provenance=("task:learn",),
        )
        self.runtime.set_concern(concern)
        updated = self.runtime.transition_concern(
            "concern:learn",
            ConcernState.INTENTION_CANDIDATE,
            reason_refs=("reason:opportunity",),
        )
        self.assertEqual(updated.state, ConcernState.INTENTION_CANDIDATE)
        history = self.runtime.concern_history("concern:learn")
        self.assertEqual(
            [item.state for item in history],
            [ConcernState.PRESENT, ConcernState.INTENTION_CANDIDATE],
        )

    def test_concern_lifecycle_rejects_invalid_shortcut(self):
        concern = Concern(
            concern_id="concern:learn",
            target_concept="concept:learn",
            strength=0.7,
            state=ConcernState.PRESENT,
            provenance=("task:learn",),
        )
        self.runtime.set_concern(concern)
        with self.assertRaises(ValueError):
            self.runtime.transition_concern(
                "concern:learn",
                ConcernState.EXECUTING,
                reason_refs=("reason:shortcut",),
            )


    def test_semantic_ambiguity_preserves_competing_hypotheses(self):
        result = self.runtime.process_competing_interpretations(
            producer="sensor:audio",
            payload={"utterance": "bank"},
            concept_id="concept:bank",
            hypotheses=(
                ("bank means financial institution", 0.62),
                ("bank means river edge", 0.57),
            ),
        )
        self.assertEqual(result.status, "AMBIGUOUS")
        self.assertIsNone(result.selected_evidence_id)
        self.assertEqual(len(result.interpretations), 2)
        self.assertTrue(
            all(item.epistemic_class == EpistemicClass.INFERRED for item in result.interpretations)
        )
        current = self.kernel.memory.current(result.working_memory.logical_key)
        self.assertEqual(current.payload["status"], "AMBIGUOUS")
        self.assertEqual(len(current.payload["alternatives"]), 2)

    def test_semantic_arbitration_selects_clear_winner_without_promoting_truth_class(self):
        result = self.runtime.process_competing_interpretations(
            producer="sensor:audio",
            payload={"utterance": "bank"},
            concept_id="concept:bank",
            hypotheses=(
                ("bank means financial institution", 0.90),
                ("bank means river edge", 0.40),
            ),
        )
        self.assertEqual(result.status, "SELECTED")
        self.assertIsNotNone(result.selected_evidence_id)
        selected = next(
            item for item in result.interpretations
            if item.evidence_id == result.selected_evidence_id
        )
        self.assertEqual(selected.epistemic_class, EpistemicClass.INFERRED)

    def test_capabilities_start_present_but_developing(self):
        state = self.runtime.capability_state("semantics")
        self.assertEqual(state.presence, "PRESENT")
        self.assertEqual(state.activation, "DEVELOPING")
        self.assertEqual(state.maturity, "LEARNING")
        self.assertEqual(state.health, "NOMINAL")

    def test_capability_qualification_requires_basis_and_preserves_history(self):
        with self.assertRaises(ValueError):
            self.runtime.qualify_capability("semantics", basis_refs=())
        qualified = self.runtime.qualify_capability(
            "semantics",
            basis_refs=("qualification:semantic-scope-v1",),
        )
        self.assertEqual(qualified.activation, "ACTIVE")
        self.assertEqual(qualified.maturity, "STABLE_WITHIN_SCOPE")
        history = self.runtime.capability_history("semantics")
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].activation, "DEVELOPING")
        self.assertEqual(history[1].activation, "ACTIVE")


if __name__ == "__main__":
    unittest.main()
