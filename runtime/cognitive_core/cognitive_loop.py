from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Any, Mapping, Optional, Tuple

from runtime.reference_kernel.hc_kernel import (
    EffectCandidate,
    EpistemicClass,
    EvidenceRecord,
    MemoryRecord,
    ProjectionStatus,
    ReferenceKernel,
    RoutedEvent,
)


def _bounded(value: float, low: float = 0.0, high: float = 1.0) -> float:
    value = float(value)
    if value < low or value > high:
        raise ValueError(f"value {value} outside [{low}, {high}]")
    return value


class ConcernState(str, Enum):
    EMERGING = "EMERGING"
    PRESENT = "PRESENT"
    INTENTION_CANDIDATE = "INTENTION_CANDIDATE"
    INTENDED = "INTENDED"
    COMMITTED = "COMMITTED"
    EXECUTING = "EXECUTING"
    SATISFIED = "SATISFIED"
    ABANDONED = "ABANDONED"
    REVISED = "REVISED"
    REVOKED = "REVOKED"
    BLOCKED = "BLOCKED"
    UNRESOLVED = "UNRESOLVED"


ACTIVE_CONCERN_STATES = {
    ConcernState.EMERGING,
    ConcernState.PRESENT,
    ConcernState.INTENTION_CANDIDATE,
    ConcernState.INTENDED,
    ConcernState.COMMITTED,
    ConcernState.EXECUTING,
    ConcernState.UNRESOLVED,
}

ALLOWED_CONCERN_TRANSITIONS = {
    ConcernState.EMERGING: {ConcernState.PRESENT, ConcernState.REVISED, ConcernState.REVOKED},
    ConcernState.PRESENT: {ConcernState.INTENTION_CANDIDATE, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.BLOCKED, ConcernState.UNRESOLVED, ConcernState.ABANDONED},
    ConcernState.INTENTION_CANDIDATE: {ConcernState.INTENDED, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.BLOCKED, ConcernState.UNRESOLVED, ConcernState.ABANDONED},
    ConcernState.INTENDED: {ConcernState.COMMITTED, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.BLOCKED, ConcernState.UNRESOLVED, ConcernState.ABANDONED},
    ConcernState.COMMITTED: {ConcernState.EXECUTING, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.BLOCKED},
    ConcernState.EXECUTING: {ConcernState.SATISFIED, ConcernState.ABANDONED, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.BLOCKED},
    ConcernState.REVISED: {ConcernState.PRESENT, ConcernState.INTENTION_CANDIDATE, ConcernState.REVOKED},
    ConcernState.BLOCKED: {ConcernState.PRESENT, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.ABANDONED},
    ConcernState.UNRESOLVED: {ConcernState.PRESENT, ConcernState.REVISED, ConcernState.REVOKED, ConcernState.BLOCKED},
}


@dataclass(frozen=True)
class AffectState:
    valence: float = 0.0
    arousal: float = 0.0
    threat: float = 0.0
    source_refs: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not -1.0 <= float(self.valence) <= 1.0:
            raise ValueError("valence must be within [-1, 1]")
        _bounded(self.arousal)
        _bounded(self.threat)


@dataclass(frozen=True)
class Concern:
    concern_id: str
    target_concept: str
    strength: float
    state: ConcernState
    provenance: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.concern_id or not self.target_concept:
            raise ValueError("concern identity and target_concept are required")
        _bounded(self.strength)


@dataclass(frozen=True)
class AttentionFrame:
    attention_id: str
    target_evidence_id: str
    score: float
    reasons: Tuple[str, ...]
    expires_at_cycle: int


@dataclass(frozen=True)
class Coalition:
    coalition_id: str
    purpose: str
    active_members: Tuple[str, ...]
    created_cycle: int
    expires_after_cycle: int
    status: str = "ACTIVE"


@dataclass(frozen=True)
class MemoryCandidate:
    candidate_id: str
    source_refs: Tuple[str, ...]
    memory_class: str
    salience: float
    basis_refs: Tuple[str, ...] = ()
    status: str = "CANDIDATE"


@dataclass(frozen=True)
class PlasticityCandidate:
    candidate_id: str
    route_key: str
    evidence_count: int
    basis_refs: Tuple[str, ...] = ()
    status: str = "PROPOSED"


@dataclass(frozen=True)
class SelfModelCandidate:
    candidate_id: str
    concept_id: str
    proposition: str
    confidence: float
    source_refs: Tuple[str, ...]
    status: str = "CANDIDATE"


@dataclass(frozen=True)
class CapabilityState:
    capability: str
    presence: str = "PRESENT"
    activation: str = "DEVELOPING"
    maturity: str = "LEARNING"
    health: str = "NOMINAL"
    basis_refs: Tuple[str, ...] = ()


@dataclass(frozen=True)
class SemanticArbitrationResult:
    observation: EvidenceRecord
    interpretations: Tuple[EvidenceRecord, ...]
    status: str
    selected_evidence_id: Optional[str]
    coalition: Coalition
    working_memory: MemoryRecord


@dataclass(frozen=True)
class CognitiveCycleResult:
    observation: EvidenceRecord
    interpretation: EvidenceRecord
    attention: AttentionFrame
    coalition: Coalition
    routed_event: RoutedEvent
    working_memory: MemoryRecord
    memory_candidate: Optional[MemoryCandidate]
    action_candidate: Optional[EffectCandidate]
    plasticity_candidate: Optional[PlasticityCandidate]
    self_model_candidate: Optional[SelfModelCandidate]


class CognitiveRuntime:
    """First executable HC cognitive-integration slice.

    This composes the invariant ReferenceKernel. It intentionally stops at
    candidates for deep memory, plasticity, identity change, and external
    effects; those require separate admission/authority transitions.
    """

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self._cycle = 0
        self._serial = 0
        self._affect = AffectState()
        self._concerns: dict[str, Concern] = {}
        self._concern_history: dict[str, list[Concern]] = {}
        self._active_coalitions: dict[str, Coalition] = {}
        self._route_counts: dict[str, int] = {}
        self._durable_route_weights: dict[str, float] = {}
        self._deep_memory: list[MemoryCandidate] = []
        self._committed_plasticity: list[PlasticityCandidate] = []
        self._self_model: dict[str, Any] = {}
        self._self_model_history: list[dict[str, Any]] = []
        capability_names = (
            "cognition",
            "semantics",
            "salience-attention",
            "current memory storage",
            "deep memory storage",
            "affect",
            "self identity",
            "volitions-conations",
            "integration-arbitration",
            "routing instructions with neuroplasticity",
        )
        self._capabilities = {
            name: CapabilityState(capability=name) for name in capability_names
        }
        self._capability_history = {
            name: [state] for name, state in self._capabilities.items()
        }

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    @property
    def active_coalitions(self) -> Mapping[str, Coalition]:
        return dict(self._active_coalitions)

    @property
    def affect(self) -> AffectState:
        return self._affect

    @property
    def deep_memory(self) -> Tuple[MemoryCandidate, ...]:
        return tuple(self._deep_memory)

    @property
    def committed_plasticity(self) -> Tuple[PlasticityCandidate, ...]:
        return tuple(self._committed_plasticity)

    @property
    def self_model(self) -> Mapping[str, Any]:
        return dict(self._self_model)

    def capability_state(self, capability: str) -> CapabilityState:
        state = self._capabilities.get(capability)
        if state is None:
            raise ValueError("unknown capability")
        return state

    def capability_history(self, capability: str) -> Tuple[CapabilityState, ...]:
        if capability not in self._capabilities:
            raise ValueError("unknown capability")
        return tuple(self._capability_history[capability])

    def qualify_capability(
        self,
        capability: str,
        *,
        basis_refs: Tuple[str, ...],
    ) -> CapabilityState:
        if not basis_refs:
            raise ValueError("capability qualification requires basis_refs")
        current = self.capability_state(capability)
        qualified = replace(
            current,
            activation="ACTIVE",
            maturity="STABLE_WITHIN_SCOPE",
            basis_refs=tuple(dict.fromkeys((*current.basis_refs, *basis_refs))),
        )
        self._capabilities[capability] = qualified
        self._capability_history[capability].append(qualified)
        return qualified

    def set_affect(self, state: AffectState) -> None:
        self._affect = state

    def set_concern(self, concern: Concern) -> None:
        self._concerns[concern.concern_id] = concern
        history = self._concern_history.setdefault(concern.concern_id, [])
        if not history or history[-1] != concern:
            history.append(concern)

    def concern_history(self, concern_id: str) -> Tuple[Concern, ...]:
        return tuple(self._concern_history.get(concern_id, ()))

    def transition_concern(
        self,
        concern_id: str,
        new_state: ConcernState,
        *,
        reason_refs: Tuple[str, ...],
    ) -> Concern:
        if not reason_refs:
            raise ValueError("concern transition requires reason_refs")
        current = self._concerns.get(concern_id)
        if current is None:
            raise ValueError("unknown concern")
        allowed = ALLOWED_CONCERN_TRANSITIONS.get(current.state, set())
        if new_state not in allowed:
            raise ValueError(f"invalid concern transition: {current.state} -> {new_state}")
        updated = replace(
            current,
            state=new_state,
            provenance=tuple(dict.fromkeys((*current.provenance, *reason_refs))),
        )
        self.set_concern(updated)
        return updated

    def advance_cycle(self) -> None:
        self._cycle += 1
        self._active_coalitions = {
            cid: coalition
            for cid, coalition in self._active_coalitions.items()
            if coalition.expires_after_cycle > self._cycle
        }
        if self._affect.arousal or self._affect.threat or self._affect.valence:
            self._affect = AffectState(
                valence=self._affect.valence * 0.90,
                arousal=self._affect.arousal * 0.85,
                threat=self._affect.threat * 0.85,
                source_refs=self._affect.source_refs,
            )

    def admit_deep_memory(
        self,
        candidate: Optional[MemoryCandidate],
        *,
        basis_refs: Tuple[str, ...],
    ) -> MemoryCandidate:
        if candidate is None:
            raise ValueError("memory admission requires a candidate")
        if not basis_refs:
            raise ValueError("deep-memory admission requires basis_refs")
        admitted = replace(
            candidate,
            basis_refs=tuple(basis_refs),
            status="ADMITTED",
        )
        self._deep_memory.append(admitted)
        return admitted

    def admit_self_model(
        self,
        candidate: Optional[SelfModelCandidate],
        *,
        basis_refs: Tuple[str, ...],
    ) -> Mapping[str, Any]:
        if candidate is None:
            raise ValueError("self-model admission requires a candidate")
        if not basis_refs:
            raise ValueError("self-model admission requires basis_refs")
        assertion = {
            "concept_id": candidate.concept_id,
            "proposition": candidate.proposition,
            "confidence": candidate.confidence,
            "source_refs": candidate.source_refs,
            "basis_refs": tuple(basis_refs),
        }
        self._self_model[candidate.concept_id] = assertion
        self._self_model_history.append(dict(assertion))
        return dict(assertion)

    def commit_plasticity(
        self,
        candidate: Optional[PlasticityCandidate],
        *,
        basis_refs: Tuple[str, ...],
    ) -> PlasticityCandidate:
        if candidate is None:
            raise ValueError("plasticity commit requires a candidate")
        if not basis_refs:
            raise ValueError("plasticity commit requires basis_refs")
        committed = replace(
            candidate,
            basis_refs=tuple(basis_refs),
            status="COMMITTED",
        )
        self._committed_plasticity.append(committed)
        learned_weight = min(2.0, 1.0 + 0.25 * candidate.evidence_count)
        self._durable_route_weights[candidate.route_key] = max(
            self._durable_route_weights.get(candidate.route_key, 1.0),
            learned_weight,
        )
        return committed

    def _concern_strength(self, concept_id: str) -> float:
        strengths = [
            concern.strength
            for concern in self._concerns.values()
            if concern.target_concept == concept_id
            and concern.state in ACTIVE_CONCERN_STATES
        ]
        return max(strengths, default=0.0)

    def _salience(
        self,
        *,
        novelty: float,
        contradiction: float,
        uncertainty: float,
        concern_strength: float,
    ) -> tuple[float, Tuple[str, ...]]:
        novelty = _bounded(novelty)
        contradiction = _bounded(contradiction)
        uncertainty = _bounded(uncertainty)
        affect_pressure = max(self._affect.arousal, self._affect.threat)
        score = min(
            1.0,
            0.35 * novelty
            + 0.25 * contradiction
            + 0.15 * uncertainty
            + 0.15 * concern_strength
            + 0.10 * affect_pressure,
        )
        reasons = []
        if novelty:
            reasons.append("NOVELTY")
        if contradiction:
            reasons.append("CORRECTION_OR_CONTRADICTION")
        if uncertainty:
            reasons.append("UNCERTAINTY")
        if concern_strength:
            reasons.append("ACTIVE_CONCERN")
        if affect_pressure:
            reasons.append("AFFECT_MODULATION")
        return score, tuple(reasons)

    def _coalition_members(
        self,
        *,
        concern_strength: float,
        self_relevance: bool,
    ) -> Tuple[str, ...]:
        members = [
            "cognition",
            "semantics",
            "salience-attention",
            "current memory storage",
            "integration-arbitration",
        ]
        if self._affect.arousal or self._affect.threat or self._affect.valence:
            members.append("affect")
        if concern_strength:
            members.append("volitions-conations")
        if self_relevance:
            members.append("self identity")
        return tuple(members)

    def process_competing_interpretations(
        self,
        *,
        producer: str,
        payload: Any,
        concept_id: str,
        hypotheses: Tuple[Tuple[str, float], ...],
        resolution_margin: float = 0.15,
    ) -> SemanticArbitrationResult:
        if len(hypotheses) < 2:
            raise ValueError("semantic arbitration requires at least two hypotheses")
        resolution_margin = _bounded(resolution_margin)
        observation = self.kernel.observe(producer=producer, payload=payload)
        interpretations = []
        for proposition, confidence in hypotheses:
            confidence = _bounded(confidence)
            interpretations.append(
                self.kernel.derive(
                    producer="semantics",
                    epistemic_class=EpistemicClass.INFERRED,
                    payload={
                        "concept_id": concept_id,
                        "proposition": proposition,
                        "confidence": confidence,
                        "status": "CANDIDATE",
                    },
                    parent_ids=(observation.evidence_id,),
                    influence_roles=("SEMANTIC_INTERPRETATION",),
                )
            )
        ranked = sorted(
            interpretations,
            key=lambda item: float(item.payload["confidence"]),
            reverse=True,
        )
        margin = float(ranked[0].payload["confidence"]) - float(ranked[1].payload["confidence"])
        selected_evidence_id = ranked[0].evidence_id if margin >= resolution_margin else None
        status = "SELECTED" if selected_evidence_id is not None else "AMBIGUOUS"
        coalition = Coalition(
            coalition_id=self._id("coalition"),
            purpose=f"semantic-arbitration:{concept_id}",
            active_members=(
                "cognition",
                "semantics",
                "pragmatics",
                "current memory storage",
                "resolver",
                "integration-arbitration",
            ),
            created_cycle=self._cycle,
            expires_after_cycle=self._cycle + 1,
        )
        self._active_coalitions[coalition.coalition_id] = coalition
        working_memory = self.kernel.memory.append(
            logical_key=("cognitive_core", "semantic_arbitration", concept_id, "current"),
            payload={
                "status": status,
                "selected_evidence_id": selected_evidence_id,
                "alternatives": tuple(
                    {
                        "evidence_id": item.evidence_id,
                        "proposition": item.payload["proposition"],
                        "confidence": item.payload["confidence"],
                    }
                    for item in interpretations
                ),
                "coalition_id": coalition.coalition_id,
            },
            epistemic_class=EpistemicClass.INFERRED,
            source_refs=tuple(item.evidence_id for item in interpretations),
        )
        return SemanticArbitrationResult(
            observation=observation,
            interpretations=tuple(interpretations),
            status=status,
            selected_evidence_id=selected_evidence_id,
            coalition=coalition,
            working_memory=working_memory,
        )

    def process_observation(
        self,
        *,
        producer: str,
        payload: Any,
        concept_id: str,
        proposition: str,
        confidence: float,
        novelty: float = 0.0,
        contradiction: float = 0.0,
        uncertainty: float = 0.0,
        correction: bool = False,
        self_relevance: bool = False,
        action_options: Tuple[Mapping[str, Any], ...] = (),
    ) -> CognitiveCycleResult:
        confidence = _bounded(confidence)
        concern_strength = self._concern_strength(concept_id)

        observation = self.kernel.observe(
            producer=producer,
            payload=payload,
        )
        interpretation = self.kernel.derive(
            producer="semantics",
            epistemic_class=EpistemicClass.INFERRED,
            payload={
                "concept_id": concept_id,
                "proposition": proposition,
                "confidence": confidence,
                "status": "CANDIDATE",
            },
            parent_ids=(observation.evidence_id,),
            influence_roles=("SEMANTIC_INTERPRETATION",),
        )

        salience, reasons = self._salience(
            novelty=novelty,
            contradiction=contradiction,
            uncertainty=uncertainty,
            concern_strength=concern_strength,
        )
        attention = AttentionFrame(
            attention_id=self._id("attention"),
            target_evidence_id=interpretation.evidence_id,
            score=salience,
            reasons=reasons,
            expires_at_cycle=self._cycle + 1,
        )

        coalition = Coalition(
            coalition_id=self._id("coalition"),
            purpose=f"interpret:{concept_id}",
            active_members=self._coalition_members(
                concern_strength=concern_strength,
                self_relevance=self_relevance,
            ),
            created_cycle=self._cycle,
            expires_after_cycle=self._cycle + 1,
        )
        self._active_coalitions[coalition.coalition_id] = coalition

        route_key = "observation->semantics->salience->current-memory"
        route_weight = self._durable_route_weights.get(route_key, 1.0)
        routed_event = self.kernel.route(
            source="semantics",
            audience="coalition:" + coalition.coalition_id,
            payload={
                "concept_id": concept_id,
                "attention_score": salience,
                "coalition_members": coalition.active_members,
                "route_weight": route_weight,
            },
            priority=round(min(1.0, salience * route_weight) * 9),
            parent_ids=(interpretation.evidence_id,),
        )

        logical_key = (
            "cognitive_core",
            "semantic_hypothesis",
            concept_id,
            "current",
        )
        supersedes: Tuple[str, ...] = ()
        if correction:
            current = self.kernel.memory.current(logical_key)
            if current.status == ProjectionStatus.CURRENT:
                supersedes = current.head_ids

        working_memory = self.kernel.memory.append(
            logical_key=logical_key,
            payload={
                "concept_id": concept_id,
                "proposition": proposition,
                "confidence": confidence,
                "attention_score": salience,
                "attention_reasons": reasons,
                "coalition_id": coalition.coalition_id,
            },
            epistemic_class=EpistemicClass.INFERRED,
            supersedes=supersedes,
            source_refs=(observation.evidence_id, interpretation.evidence_id),
        )

        memory_candidate = None
        if salience >= 0.50 or self_relevance:
            memory_candidate = MemoryCandidate(
                candidate_id=self._id("memory-candidate"),
                source_refs=(working_memory.record_id, interpretation.evidence_id),
                memory_class="EPISODIC_OR_SEMANTIC_CANDIDATE",
                salience=salience,
            )

        action_candidate = None
        if action_options and concern_strength > 0.0:
            option = action_options[0]
            action_candidate = self.kernel.plan_effect(
                origin="cognitive_core",
                action_scope=str(option["action_scope"]),
                target_scope=str(option["target_scope"]),
                payload=option.get("payload"),
                authority_grant_id=None,
                parent_ids=(interpretation.evidence_id,),
            )

        count = self._route_counts.get(route_key, 0) + 1
        self._route_counts[route_key] = count
        plasticity_candidate = None
        if count >= 3:
            plasticity_candidate = PlasticityCandidate(
                candidate_id=self._id("plasticity-candidate"),
                route_key=route_key,
                evidence_count=count,
            )

        self_model_candidate = None
        if self_relevance:
            self_model_candidate = SelfModelCandidate(
                candidate_id=self._id("self-model-candidate"),
                concept_id=concept_id,
                proposition=proposition,
                confidence=confidence,
                source_refs=(interpretation.evidence_id,),
            )

        return CognitiveCycleResult(
            observation=observation,
            interpretation=interpretation,
            attention=attention,
            coalition=coalition,
            routed_event=routed_event,
            working_memory=working_memory,
            memory_candidate=memory_candidate,
            action_candidate=action_candidate,
            plasticity_candidate=plasticity_candidate,
            self_model_candidate=self_model_candidate,
        )
