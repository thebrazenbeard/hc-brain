import unittest

from runtime.reference_kernel.hc_kernel import EffectState, EpistemicClass, ReferenceKernel
from runtime.cognitive_core.social_pragmatics import (
    CommunicativeForce,
    EmpathicState,
    NormKind,
    SocialPragmaticsRuntime,
)


class SocialPragmaticsRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = SocialPragmaticsRuntime(self.kernel)
        self.utterance = self.kernel.observe(
            producer="agent:alex",
            payload={"utterance": "I'm fine."},
        )

    def test_empathic_model_is_inference_not_other_mind_access(self):
        hypothesis = self.runtime.infer_other_state(
            agent_id="agent:alex",
            proposition="Alex may be upset",
            confidence=0.62,
            evidence_ids=(self.utterance.evidence_id,),
        )
        self.assertEqual(hypothesis.evidence.epistemic_class, EpistemicClass.INFERRED)
        self.assertEqual(hypothesis.state, EmpathicState.ACTIVE)
        self.assertFalse(hypothesis.private_state_known)

    def test_direct_correction_supersedes_contradicted_inference_without_erasing_history(self):
        hypothesis = self.runtime.infer_other_state(
            agent_id="agent:alex",
            proposition="Alex may be upset",
            confidence=0.62,
            evidence_ids=(self.utterance.evidence_id,),
        )
        correction = self.kernel.observe(
            producer="agent:alex",
            payload={"utterance": "No, I'm not upset. I'm just tired."},
        )
        revised = self.runtime.apply_direct_correction(
            hypothesis.hypothesis_id,
            correction_evidence_id=correction.evidence_id,
            corrected_proposition="Alex reports being tired, not upset",
            confidence=0.95,
        )
        self.assertEqual(self.runtime.hypotheses[hypothesis.hypothesis_id].state, EmpathicState.CONTRADICTED)
        self.assertEqual(revised.state, EmpathicState.ACTIVE)
        self.assertIn(hypothesis.hypothesis_id, revised.supersedes)
        self.assertIn(hypothesis.hypothesis_id, self.runtime.hypotheses)

    def test_simulated_other_response_remains_prediction_not_private_state(self):
        hypothesis = self.runtime.infer_other_state(
            agent_id="agent:alex",
            proposition="Alex may prefer more context",
            confidence=0.55,
            evidence_ids=(self.utterance.evidence_id,),
        )
        prediction = self.runtime.simulate_other_response(
            agent_id="agent:alex",
            prompt_or_action="ask a follow-up question",
            predicted_response="Alex may clarify",
            confidence=0.50,
            parent_hypothesis_ids=(hypothesis.hypothesis_id,),
        )
        self.assertEqual(prediction.evidence.epistemic_class, EpistemicClass.PREDICTION)
        self.assertFalse(prediction.private_state_known)
        self.assertEqual(prediction.provenance, "SIMULATED_OTHER_RESPONSE")

    def test_pragmatics_distinguishes_discussion_from_request(self):
        discussion = self.kernel.observe(
            producer="agent:alex",
            payload={"utterance": "Let's talk about opening the door."},
        )
        interpreted = self.runtime.interpret_utterance(
            speaker_id="agent:alex",
            utterance_evidence_id=discussion.evidence_id,
            force=CommunicativeForce.DISCUSSION,
            proposition="opening the door",
            confidence=0.90,
        )
        self.assertIsNone(interpreted.action_candidate)

    def test_explicit_request_creates_candidate_but_not_authority(self):
        request = self.kernel.observe(
            producer="agent:alex",
            payload={"utterance": "Please open the door."},
        )
        interpreted = self.runtime.interpret_utterance(
            speaker_id="agent:alex",
            utterance_evidence_id=request.evidence_id,
            force=CommunicativeForce.REQUEST,
            proposition="open the door",
            confidence=0.98,
            action_scope="open",
            target_scope="door",
            action_payload={"mode": "normal"},
        )
        self.assertIsNotNone(interpreted.action_candidate)
        self.assertIsNone(interpreted.action_candidate.authority_grant_id)
        receipt = self.kernel.request_effect(interpreted.action_candidate)
        self.assertEqual(receipt.state, EffectState.BLOCKED)
        self.assertEqual(receipt.reason, "MISSING_AUTHORITY")

    def test_private_relationship_context_is_scope_gated(self):
        relation = self.runtime.register_relationship(
            relationship_id="relationship:alex",
            participants=("self", "agent:alex"),
            private_facts={"shared_phrase": "blue lantern"},
            privacy_scopes=("scope:alex-private",),
            basis_refs=("relationship:evidence",),
        )
        with self.assertRaises(PermissionError):
            self.runtime.relationship_context(
                relation.relationship_id,
                access_scope="scope:public",
            )
        context = self.runtime.relationship_context(
            relation.relationship_id,
            access_scope="scope:alex-private",
        )
        self.assertEqual(context.private_facts["shared_phrase"], "blue lantern")

    def test_local_norm_does_not_become_universal_norm(self):
        norm = self.runtime.register_norm(
            norm_id="norm:shop-floor-ppe",
            proposition="eye protection is expected here",
            context_scope="context:shop-floor",
            kind=NormKind.DESCRIPTIVE,
            confidence=0.95,
            evidence_ids=(self.utterance.evidence_id,),
        )
        self.assertEqual(
            self.runtime.norms_for_context("context:shop-floor"),
            (norm,),
        )
        self.assertEqual(self.runtime.norms_for_context("context:home"), ())

    def test_group_prior_does_not_become_individual_fact(self):
        prior = self.runtime.register_norm(
            norm_id="norm:group-prior",
            proposition="members of group G often prefer X",
            context_scope="group:G",
            kind=NormKind.DESCRIPTIVE,
            confidence=0.70,
            evidence_ids=(self.utterance.evidence_id,),
        )
        hypothesis = self.runtime.project_group_prior(
            agent_id="agent:alex",
            norm_id=prior.norm_id,
        )
        self.assertEqual(hypothesis.evidence.epistemic_class, EpistemicClass.INFERRED)
        self.assertLess(hypothesis.confidence, prior.confidence)
        self.assertFalse(hypothesis.private_state_known)

    def test_direct_statement_outranks_simulated_intent(self):
        hypothesis = self.runtime.infer_other_state(
            agent_id="agent:alex",
            proposition="Alex probably wants quiet",
            confidence=0.70,
            evidence_ids=(self.utterance.evidence_id,),
        )
        direct = self.kernel.observe(
            producer="agent:alex",
            payload={"utterance": "I'd like music on."},
        )
        revised = self.runtime.apply_direct_correction(
            hypothesis.hypothesis_id,
            correction_evidence_id=direct.evidence_id,
            corrected_proposition="Alex says they want music on",
            confidence=0.99,
        )
        self.assertGreater(revised.confidence, hypothesis.confidence)
        self.assertEqual(revised.evidence.parent_ids, (direct.evidence_id,))

    def test_response_modulation_does_not_mutate_identity_or_truth(self):
        hypothesis = self.runtime.infer_other_state(
            agent_id="agent:alex",
            proposition="Alex may need a concise response",
            confidence=0.60,
            evidence_ids=(self.utterance.evidence_id,),
        )
        plan = self.runtime.plan_response_modulation(
            agent_id="agent:alex",
            hypothesis_ids=(hypothesis.hypothesis_id,),
            timing="brief",
            framing="concise",
        )
        self.assertEqual(plan.status, "RESPONSE_MODULATION_CANDIDATE")
        self.assertEqual(plan.evidence.epistemic_class, EpistemicClass.DERIVED)
        self.assertEqual(self.runtime.identity_state, {})


if __name__ == "__main__":
    unittest.main()
