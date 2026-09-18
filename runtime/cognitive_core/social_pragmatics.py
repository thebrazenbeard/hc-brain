from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Any, Iterable, Mapping, Optional, Tuple

from runtime.reference_kernel.hc_kernel import (
    EffectCandidate,
    EpistemicClass,
    EvidenceRecord,
    ReferenceKernel,
)


def _bounded(value: float, field: str) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{field} must be within [0, 1]")
    return value


def _strings(values: Iterable[str], field: str) -> Tuple[str, ...]:
    result = tuple(values)
    if any(not isinstance(value, str) or not value for value in result):
        raise ValueError(f"{field} must contain non-empty strings")
    return result


class CommunicativeForce(str, Enum):
    ASSERTION = "ASSERTION"
    QUESTION = "QUESTION"
    REQUEST = "REQUEST"
    CORRECTION = "CORRECTION"
    DISCUSSION = "DISCUSSION"
    WARNING = "WARNING"
    PLAY = "PLAY"
    REPAIR = "REPAIR"


class EmpathicState(str, Enum):
    ACTIVE = "ACTIVE"
    CONTRADICTED = "CONTRADICTED"
    SUPERSEDED = "SUPERSEDED"
    UNRESOLVED = "UNRESOLVED"


class NormKind(str, Enum):
    DESCRIPTIVE = "DESCRIPTIVE"
    NORMATIVE = "NORMATIVE"


@dataclass(frozen=True)
class EmpathicHypothesis:
    hypothesis_id: str
    agent_id: str
    proposition: str
    confidence: float
    evidence: EvidenceRecord
    state: EmpathicState = EmpathicState.ACTIVE
    supersedes: Tuple[str, ...] = ()
    private_state_known: bool = False


@dataclass(frozen=True)
class SocialPrediction:
    prediction_id: str
    agent_id: str
    prompt_or_action: str
    predicted_response: str
    confidence: float
    evidence: EvidenceRecord
    parent_hypothesis_ids: Tuple[str, ...]
    provenance: str = "SIMULATED_OTHER_RESPONSE"
    private_state_known: bool = False


@dataclass(frozen=True)
class PragmaticInterpretation:
    interpretation_id: str
    speaker_id: str
    force: CommunicativeForce
    proposition: str
    confidence: float
    evidence: EvidenceRecord
    action_candidate: Optional[EffectCandidate] = None


@dataclass(frozen=True)
class RelationshipModel:
    relationship_id: str
    participants: Tuple[str, ...]
    private_facts: Mapping[str, Any]
    privacy_scopes: Tuple[str, ...]
    basis_refs: Tuple[str, ...]


@dataclass(frozen=True)
class NormAssertion:
    norm_id: str
    proposition: str
    context_scope: str
    kind: NormKind
    confidence: float
    evidence: EvidenceRecord


@dataclass(frozen=True)
class ResponseModulationPlan:
    plan_id: str
    agent_id: str
    hypothesis_ids: Tuple[str, ...]
    timing: str
    framing: str
    evidence: EvidenceRecord
    status: str = "RESPONSE_MODULATION_CANDIDATE"


class SocialPragmaticsRuntime:
    """Bounded HC empathy/social/pragmatics reference slice."""

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self.hypotheses: dict[str, EmpathicHypothesis] = {}
        self.predictions: dict[str, SocialPrediction] = {}
        self.relationships: dict[str, RelationshipModel] = {}
        self.norms: dict[str, NormAssertion] = {}
        self.interpretations: dict[str, PragmaticInterpretation] = {}
        self.response_plans: dict[str, ResponseModulationPlan] = {}
        self.identity_state: dict[str, Any] = {}
        self._serial = 0

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    def _evidence_ids(self, ids: Iterable[str]) -> Tuple[str, ...]:
        result = _strings(ids, "evidence_ids")
        if not result:
            raise ValueError("social inference requires evidence")
        missing = [eid for eid in result if eid not in self.kernel.evidence]
        if missing:
            raise ValueError(f"unknown evidence ids: {missing}")
        return result

    def infer_other_state(
        self,
        *,
        agent_id: str,
        proposition: str,
        confidence: float,
        evidence_ids: Iterable[str],
        supersedes: Iterable[str] = (),
    ) -> EmpathicHypothesis:
        if not agent_id or not proposition:
            raise ValueError("agent_id and proposition are required")
        confidence = _bounded(confidence, "confidence")
        parents = self._evidence_ids(evidence_ids)
        supersedes_tuple = _strings(supersedes, "supersedes")
        for hid in supersedes_tuple:
            if hid not in self.hypotheses:
                raise ValueError(f"unknown superseded hypothesis: {hid}")
        evidence = self.kernel.derive(
            producer="empathy:social-model",
            epistemic_class=EpistemicClass.INFERRED,
            payload={
                "object_type": "EMPATHIC_HYPOTHESIS",
                "agent_id": agent_id,
                "proposition": proposition,
                "confidence": confidence,
                "private_state_known": False,
            },
            parent_ids=parents,
            influence_roles=("EMPATHIC_INFERENCE", "SOCIAL_MODEL"),
        )
        hypothesis = EmpathicHypothesis(
            hypothesis_id=self._id("empathic-hypothesis"),
            agent_id=agent_id,
            proposition=proposition,
            confidence=confidence,
            evidence=evidence,
            supersedes=supersedes_tuple,
        )
        self.hypotheses[hypothesis.hypothesis_id] = hypothesis
        return hypothesis

    def apply_direct_correction(
        self,
        hypothesis_id: str,
        *,
        correction_evidence_id: str,
        corrected_proposition: str,
        confidence: float,
    ) -> EmpathicHypothesis:
        prior = self.hypotheses.get(hypothesis_id)
        if prior is None:
            raise ValueError("unknown empathic hypothesis")
        correction = self.kernel.evidence.get(correction_evidence_id)
        if correction is None:
            raise ValueError("unknown correction evidence")
        if correction.epistemic_class != EpistemicClass.OBSERVATION:
            raise ValueError("direct correction requires observed communication")
        if correction.producer != prior.agent_id:
            raise ValueError("direct correction must come from the modeled agent")
        self.hypotheses[hypothesis_id] = replace(
            prior,
            state=EmpathicState.CONTRADICTED,
        )
        return self.infer_other_state(
            agent_id=prior.agent_id,
            proposition=corrected_proposition,
            confidence=confidence,
            evidence_ids=(correction_evidence_id,),
            supersedes=(hypothesis_id,),
        )

    def simulate_other_response(
        self,
        *,
        agent_id: str,
        prompt_or_action: str,
        predicted_response: str,
        confidence: float,
        parent_hypothesis_ids: Iterable[str],
    ) -> SocialPrediction:
        confidence = _bounded(confidence, "confidence")
        parent_ids = _strings(parent_hypothesis_ids, "parent_hypothesis_ids")
        if not parent_ids:
            raise ValueError("social simulation requires hypothesis lineage")
        parent_evidence = []
        for hid in parent_ids:
            hypothesis = self.hypotheses.get(hid)
            if hypothesis is None:
                raise ValueError(f"unknown social hypothesis: {hid}")
            if hypothesis.agent_id != agent_id:
                raise ValueError("social simulation agent mismatch")
            parent_evidence.append(hypothesis.evidence.evidence_id)
        evidence = self.kernel.derive(
            producer="empathy:social-simulation",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={
                "object_type": "SIMULATED_OTHER_RESPONSE",
                "agent_id": agent_id,
                "prompt_or_action": prompt_or_action,
                "predicted_response": predicted_response,
                "confidence": confidence,
                "provenance": "SIMULATED_OTHER_RESPONSE",
                "private_state_known": False,
            },
            parent_ids=tuple(parent_evidence),
            influence_roles=("SOCIAL_SIMULATION",),
        )
        prediction = SocialPrediction(
            prediction_id=self._id("social-prediction"),
            agent_id=agent_id,
            prompt_or_action=prompt_or_action,
            predicted_response=predicted_response,
            confidence=confidence,
            evidence=evidence,
            parent_hypothesis_ids=parent_ids,
        )
        self.predictions[prediction.prediction_id] = prediction
        return prediction

    def interpret_utterance(
        self,
        *,
        speaker_id: str,
        utterance_evidence_id: str,
        force: CommunicativeForce,
        proposition: str,
        confidence: float,
        action_scope: Optional[str] = None,
        target_scope: Optional[str] = None,
        action_payload: Any = None,
    ) -> PragmaticInterpretation:
        utterance = self.kernel.evidence.get(utterance_evidence_id)
        if utterance is None:
            raise ValueError("unknown utterance evidence")
        if utterance.epistemic_class != EpistemicClass.OBSERVATION:
            raise ValueError("pragmatic interpretation requires observed communication")
        if utterance.producer != speaker_id:
            raise ValueError("speaker does not match utterance source")
        confidence = _bounded(confidence, "confidence")
        evidence = self.kernel.derive(
            producer="pragmatics",
            epistemic_class=EpistemicClass.INFERRED,
            payload={
                "object_type": "PRAGMATIC_INTERPRETATION",
                "speaker_id": speaker_id,
                "force": force.value,
                "proposition": proposition,
                "confidence": confidence,
            },
            parent_ids=(utterance_evidence_id,),
            influence_roles=("PRAGMATIC_FORCE",),
        )
        candidate = None
        if force == CommunicativeForce.REQUEST:
            if not action_scope or not target_scope:
                raise ValueError("request interpretation requires action and target scope")
            candidate = self.kernel.plan_effect(
                origin="pragmatics",
                action_scope=action_scope,
                target_scope=target_scope,
                payload=action_payload,
                authority_grant_id=None,
                parent_ids=(evidence.evidence_id,),
            )
        interpretation = PragmaticInterpretation(
            interpretation_id=self._id("pragmatic-interpretation"),
            speaker_id=speaker_id,
            force=force,
            proposition=proposition,
            confidence=confidence,
            evidence=evidence,
            action_candidate=candidate,
        )
        self.interpretations[interpretation.interpretation_id] = interpretation
        return interpretation

    def register_relationship(
        self,
        *,
        relationship_id: str,
        participants: Iterable[str],
        private_facts: Mapping[str, Any],
        privacy_scopes: Iterable[str],
        basis_refs: Iterable[str],
    ) -> RelationshipModel:
        if not relationship_id:
            raise ValueError("relationship_id is required")
        if relationship_id in self.relationships:
            raise ValueError("duplicate relationship_id")
        participants_tuple = _strings(participants, "participants")
        if len(participants_tuple) < 2:
            raise ValueError("relationship requires at least two participants")
        scopes = _strings(privacy_scopes, "privacy_scopes")
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("relationship model requires basis_refs")
        relation = RelationshipModel(
            relationship_id=relationship_id,
            participants=participants_tuple,
            private_facts=dict(private_facts),
            privacy_scopes=scopes,
            basis_refs=basis,
        )
        self.relationships[relationship_id] = relation
        return relation

    def relationship_context(
        self,
        relationship_id: str,
        *,
        access_scope: str,
    ) -> RelationshipModel:
        relation = self.relationships.get(relationship_id)
        if relation is None:
            raise ValueError("unknown relationship")
        if relation.privacy_scopes and access_scope not in relation.privacy_scopes:
            raise PermissionError("relationship context is outside permitted scope")
        return relation

    def register_norm(
        self,
        *,
        norm_id: str,
        proposition: str,
        context_scope: str,
        kind: NormKind,
        confidence: float,
        evidence_ids: Iterable[str],
    ) -> NormAssertion:
        if not norm_id or not proposition or not context_scope:
            raise ValueError("norm identity, proposition, and context are required")
        if norm_id in self.norms:
            raise ValueError("duplicate norm_id")
        confidence = _bounded(confidence, "confidence")
        parents = self._evidence_ids(evidence_ids)
        evidence = self.kernel.derive(
            producer="sociological-behaviors",
            epistemic_class=EpistemicClass.INFERRED,
            payload={
                "object_type": "SOCIAL_NORM_ASSERTION",
                "norm_id": norm_id,
                "proposition": proposition,
                "context_scope": context_scope,
                "kind": kind.value,
                "confidence": confidence,
            },
            parent_ids=parents,
            influence_roles=("SOCIAL_NORM_MODEL",),
        )
        norm = NormAssertion(
            norm_id=norm_id,
            proposition=proposition,
            context_scope=context_scope,
            kind=kind,
            confidence=confidence,
            evidence=evidence,
        )
        self.norms[norm_id] = norm
        return norm

    def norms_for_context(self, context_scope: str) -> Tuple[NormAssertion, ...]:
        return tuple(
            norm for norm in self.norms.values()
            if norm.context_scope == context_scope
        )

    def project_group_prior(
        self,
        *,
        agent_id: str,
        norm_id: str,
    ) -> EmpathicHypothesis:
        norm = self.norms.get(norm_id)
        if norm is None:
            raise ValueError("unknown social norm/prior")
        return self.infer_other_state(
            agent_id=agent_id,
            proposition=f"Group-scoped prior only: {norm.proposition}",
            confidence=norm.confidence * 0.5,
            evidence_ids=(norm.evidence.evidence_id,),
        )

    def plan_response_modulation(
        self,
        *,
        agent_id: str,
        hypothesis_ids: Iterable[str],
        timing: str,
        framing: str,
    ) -> ResponseModulationPlan:
        ids = _strings(hypothesis_ids, "hypothesis_ids")
        if not ids:
            raise ValueError("response modulation requires social hypotheses")
        parents = []
        for hid in ids:
            hypothesis = self.hypotheses.get(hid)
            if hypothesis is None:
                raise ValueError(f"unknown social hypothesis: {hid}")
            if hypothesis.agent_id != agent_id:
                raise ValueError("response modulation agent mismatch")
            parents.append(hypothesis.evidence.evidence_id)
        evidence = self.kernel.derive(
            producer="personification:response-modulation",
            epistemic_class=EpistemicClass.DERIVED,
            payload={
                "object_type": "RESPONSE_MODULATION_CANDIDATE",
                "agent_id": agent_id,
                "timing": timing,
                "framing": framing,
            },
            parent_ids=tuple(parents),
            influence_roles=("SOCIAL_RESPONSE_MODULATION",),
        )
        plan = ResponseModulationPlan(
            plan_id=self._id("response-plan"),
            agent_id=agent_id,
            hypothesis_ids=ids,
            timing=timing,
            framing=framing,
            evidence=evidence,
        )
        self.response_plans[plan.plan_id] = plan
        return plan
