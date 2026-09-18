from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable, Tuple

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


class CognitiveMonitorState(str, Enum):
    NOMINAL = "NOMINAL"
    UNCERTAIN = "UNCERTAIN"
    MODEL_CONFLICT = "MODEL_CONFLICT"
    STRATEGY_FAILING = "STRATEGY_FAILING"
    EVIDENCE_STALE = "EVIDENCE_STALE"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


class Recommendation(str, Enum):
    CONTINUE = "CONTINUE"
    SEEK_EVIDENCE = "SEEK_EVIDENCE"
    EXPAND_COALITION = "EXPAND_COALITION"
    REVISE_STRATEGY = "REVISE_STRATEGY"
    STOP = "STOP"


@dataclass(frozen=True)
class StrategyOutcome:
    outcome_id: str
    task_id: str
    strategy: str
    success: bool
    evidence_ids: Tuple[str, ...]


@dataclass(frozen=True)
class MetacognitiveTrace:
    trace_id: str
    task_id: str
    strategy: str
    confidence: float
    uncertainty: float
    state: CognitiveMonitorState
    recommendation: Recommendation
    evidence: EvidenceRecord
    parent_evidence_ids: Tuple[str, ...]
    conflict: bool
    evidence_stale: bool
    resource_budget_remaining: float


class MetacognitiveRuntime:
    """Bounded monitor over cognitive process state, not a universal executive."""

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self.traces: dict[str, MetacognitiveTrace] = {}
        self.strategy_outcomes: list[StrategyOutcome] = []
        self._serial = 0

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    def _evidence_ids(self, ids: Iterable[str]) -> Tuple[str, ...]:
        result = tuple(ids)
        if not result:
            raise ValueError("metacognitive assessment requires evidence lineage")
        if any(not isinstance(eid, str) or not eid for eid in result):
            raise ValueError("parent_evidence_ids must contain non-empty strings")
        missing = [eid for eid in result if eid not in self.kernel.evidence]
        if missing:
            raise ValueError(f"unknown parent evidence: {missing}")
        return result

    def record_strategy_outcome(
        self,
        *,
        task_id: str,
        strategy: str,
        success: bool,
        evidence_ids: Iterable[str],
    ) -> StrategyOutcome:
        if not task_id or not strategy:
            raise ValueError("task_id and strategy are required")
        evidence = self._evidence_ids(evidence_ids)
        outcome = StrategyOutcome(
            outcome_id=self._id("strategy-outcome"),
            task_id=task_id,
            strategy=strategy,
            success=bool(success),
            evidence_ids=evidence,
        )
        self.strategy_outcomes.append(outcome)
        return outcome

    def _failure_count(self, task_id: str, strategy: str) -> int:
        return sum(
            1 for item in self.strategy_outcomes
            if item.task_id == task_id
            and item.strategy == strategy
            and not item.success
        )

    def assess(
        self,
        *,
        task_id: str,
        strategy: str,
        parent_evidence_ids: Iterable[str],
        confidence: float,
        uncertainty: float,
        conflict: bool = False,
        evidence_stale: bool = False,
        resource_budget_remaining: float = 1.0,
    ) -> MetacognitiveTrace:
        if not task_id or not strategy:
            raise ValueError("task_id and strategy are required")
        parents = self._evidence_ids(parent_evidence_ids)
        confidence = _bounded(confidence, "confidence")
        uncertainty = _bounded(uncertainty, "uncertainty")
        budget = _bounded(resource_budget_remaining, "resource_budget_remaining")

        failures = self._failure_count(task_id, strategy)
        if budget <= 0.0:
            state = CognitiveMonitorState.BUDGET_EXHAUSTED
            recommendation = Recommendation.STOP
        elif conflict:
            state = CognitiveMonitorState.MODEL_CONFLICT
            recommendation = Recommendation.EXPAND_COALITION
        elif failures >= 2:
            state = CognitiveMonitorState.STRATEGY_FAILING
            recommendation = Recommendation.REVISE_STRATEGY
        elif evidence_stale:
            state = CognitiveMonitorState.EVIDENCE_STALE
            recommendation = Recommendation.SEEK_EVIDENCE
        elif uncertainty >= 0.40:
            state = CognitiveMonitorState.UNCERTAIN
            recommendation = Recommendation.SEEK_EVIDENCE
        else:
            state = CognitiveMonitorState.NOMINAL
            recommendation = Recommendation.CONTINUE

        evidence = self.kernel.derive(
            producer="cognition:metacognition",
            epistemic_class=EpistemicClass.DERIVED,
            payload={
                "object_type": "METACOGNITIVE_TRACE",
                "task_id": task_id,
                "strategy": strategy,
                "confidence": confidence,
                "uncertainty": uncertainty,
                "state": state.value,
                "recommendation": recommendation.value,
                "failure_count": failures,
                "conflict": bool(conflict),
                "evidence_stale": bool(evidence_stale),
                "resource_budget_remaining": budget,
            },
            parent_ids=parents,
            influence_roles=("METACOGNITIVE_MONITORING",),
        )
        trace = MetacognitiveTrace(
            trace_id=self._id("metacognitive-trace"),
            task_id=task_id,
            strategy=strategy,
            confidence=confidence,
            uncertainty=uncertainty,
            state=state,
            recommendation=recommendation,
            evidence=evidence,
            parent_evidence_ids=parents,
            conflict=bool(conflict),
            evidence_stale=bool(evidence_stale),
            resource_budget_remaining=budget,
        )
        self.traces[trace.trace_id] = trace
        return trace

    def recommend_external_action(
        self,
        trace_id: str,
        *,
        action_scope: str,
        target_scope: str,
        payload: Any,
    ) -> EffectCandidate:
        trace = self.traces.get(trace_id)
        if trace is None:
            raise ValueError("unknown metacognitive trace")
        return self.kernel.plan_effect(
            origin="cognition:metacognition",
            action_scope=action_scope,
            target_scope=target_scope,
            payload=payload,
            authority_grant_id=None,
            parent_ids=(trace.evidence.evidence_id,),
        )
