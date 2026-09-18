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


def _bounded_confidence(value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError("confidence must be within [0, 1]")
    return value


def _nonempty_strings(values: Iterable[str], field: str) -> Tuple[str, ...]:
    result = tuple(values)
    if any(not isinstance(value, str) or not value for value in result):
        raise ValueError(f"{field} must contain non-empty strings")
    return result


class CausalSupport(str, Enum):
    OBSERVATIONAL = "OBSERVATIONAL"
    TEMPORAL_PREDICTIVE = "TEMPORAL_PREDICTIVE"
    INTERVENTION_SUPPORTED = "INTERVENTION_SUPPORTED"
    COUNTERFACTUAL_SUPPORTED = "COUNTERFACTUAL_SUPPORTED"
    MECHANISM_SUPPORTED = "MECHANISM_SUPPORTED"
    UNRESOLVED = "UNRESOLVED"


class ModelLifecycle(str, Enum):
    PROPOSED = "PROPOSED"
    ACTIVE = "ACTIVE"
    SUPPORTED = "SUPPORTED"
    WEAKENED = "WEAKENED"
    CONTRADICTED = "CONTRADICTED"
    SUPERSEDED = "SUPERSEDED"
    REOPENED = "REOPENED"
    RETIRED = "RETIRED"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class ModelHypothesis:
    model_id: str
    target: str
    relation: str
    confidence: float
    source_evidence_ids: Tuple[str, ...]
    support: CausalSupport
    evidence: EvidenceRecord
    lifecycle: ModelLifecycle = ModelLifecycle.ACTIVE
    supersedes: Tuple[str, ...] = ()


@dataclass(frozen=True)
class Forecast:
    forecast_id: str
    model_id: str
    target: str
    expected: Any
    horizon: str
    confidence: float
    evidence: EvidenceRecord
    parent_evidence_ids: Tuple[str, ...]
    parent_forecast_ids: Tuple[str, ...]
    observed_ancestor_ids: Tuple[str, ...]
    generated_ancestor_ids: Tuple[str, ...]
    assumptions: Tuple[str, ...] = ()
    action_conditional: bool = False
    status: str = "ACTIVE"


@dataclass(frozen=True)
class Simulation:
    simulation_id: str
    goal: str
    model_id: str
    base_evidence_ids: Tuple[str, ...]
    hypothetical_modifications: Any
    generated_outcomes: Any
    confidence: float
    evidence: EvidenceRecord
    provenance: str = "SIMULATED"


@dataclass(frozen=True)
class ActionRehearsal:
    rehearsal_id: str
    forecast: Forecast
    action_candidate: EffectCandidate


@dataclass(frozen=True)
class ForecastReconciliation:
    forecast_id: str
    observation_evidence_id: str
    matched: bool
    status: str
    descendant_forecast_ids: Tuple[str, ...]


class WorldModelRuntime:
    """Bounded HC world-model/prediction reference slice.

    Models and forecasts remain derived/generated evidence. Nothing here writes
    simulated events into lived/current memory or authorizes external effects.
    """

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self.models: dict[str, ModelHypothesis] = {}
        self.forecasts: dict[str, Forecast] = {}
        self.simulations: dict[str, Simulation] = {}
        self._serial = 0

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    def _require_evidence(self, evidence_ids: Iterable[str]) -> Tuple[str, ...]:
        ids = _nonempty_strings(evidence_ids, "evidence_ids")
        missing = [eid for eid in ids if eid not in self.kernel.evidence]
        if missing:
            raise ValueError(f"unknown evidence ids: {missing}")
        return ids

    def propose_model(
        self,
        *,
        model_id: str,
        target: str,
        relation: str,
        confidence: float,
        source_evidence_ids: Iterable[str],
        support: CausalSupport = CausalSupport.UNRESOLVED,
        supersedes: Iterable[str] = (),
    ) -> ModelHypothesis:
        if not model_id or not target or not relation:
            raise ValueError("model_id, target, and relation are required")
        if model_id in self.models:
            raise ValueError("duplicate model_id")
        confidence = _bounded_confidence(confidence)
        sources = self._require_evidence(source_evidence_ids)
        supersedes_tuple = _nonempty_strings(supersedes, "supersedes")
        for predecessor in supersedes_tuple:
            if predecessor not in self.models:
                raise ValueError(f"unknown superseded model: {predecessor}")
        evidence = self.kernel.derive(
            producer="cognition:world-model",
            epistemic_class=EpistemicClass.INFERRED,
            payload={
                "object_type": "WORLD_MODEL_HYPOTHESIS",
                "model_id": model_id,
                "target": target,
                "relation": relation,
                "confidence": confidence,
                "causal_support": support.value,
            },
            parent_ids=sources,
            influence_roles=("WORLD_MODEL",),
        )
        model = ModelHypothesis(
            model_id=model_id,
            target=target,
            relation=relation,
            confidence=confidence,
            source_evidence_ids=sources,
            support=support,
            evidence=evidence,
            supersedes=supersedes_tuple,
        )
        self.models[model_id] = model
        return model

    def models_for_target(self, target: str) -> Tuple[ModelHypothesis, ...]:
        return tuple(
            model for model in self.models.values()
            if model.target == target and model.lifecycle != ModelLifecycle.RETIRED
        )

    def revise_model(
        self,
        model_id: str,
        *,
        new_model_id: str,
        relation: str,
        confidence: float,
        source_evidence_ids: Iterable[str],
        support: Optional[CausalSupport] = None,
    ) -> ModelHypothesis:
        prior = self.models.get(model_id)
        if prior is None:
            raise ValueError("unknown model")
        if prior.lifecycle == ModelLifecycle.SUPERSEDED:
            raise ValueError("model already superseded")
        self.models[model_id] = replace(prior, lifecycle=ModelLifecycle.SUPERSEDED)
        try:
            successor = self.propose_model(
                model_id=new_model_id,
                target=prior.target,
                relation=relation,
                confidence=confidence,
                source_evidence_ids=source_evidence_ids,
                support=support or prior.support,
                supersedes=(model_id,),
            )
        except Exception:
            self.models[model_id] = prior
            raise
        return successor

    def _forecast_ancestry(
        self,
        *,
        parent_evidence_ids: Tuple[str, ...],
        parent_forecast_ids: Tuple[str, ...],
    ) -> tuple[Tuple[str, ...], Tuple[str, ...], Optional[float]]:
        observed: list[str] = []
        generated: list[str] = []
        ancestor_confidence: Optional[float] = None

        for eid in parent_evidence_ids:
            evidence = self.kernel.evidence[eid]
            if evidence.epistemic_class == EpistemicClass.OBSERVATION:
                observed.append(eid)
            else:
                generated.append(eid)

        for fid in parent_forecast_ids:
            forecast = self.forecasts.get(fid)
            if forecast is None:
                raise ValueError(f"unknown parent forecast: {fid}")
            generated.append(fid)
            observed.extend(forecast.observed_ancestor_ids)
            generated.extend(forecast.generated_ancestor_ids)
            ancestor_confidence = (
                forecast.confidence if ancestor_confidence is None
                else min(ancestor_confidence, forecast.confidence)
            )

        return (
            tuple(dict.fromkeys(observed)),
            tuple(dict.fromkeys(generated)),
            ancestor_confidence,
        )

    def forecast(
        self,
        *,
        model_id: str,
        target: str,
        expected: Any,
        horizon: str,
        confidence: float,
        parent_evidence_ids: Iterable[str] = (),
        parent_forecast_ids: Iterable[str] = (),
        assumptions: Iterable[str] = (),
        action_conditional: bool = False,
    ) -> Forecast:
        model = self.models.get(model_id)
        if model is None:
            raise ValueError("unknown model")
        if model.lifecycle in {ModelLifecycle.RETIRED, ModelLifecycle.SUPERSEDED}:
            raise ValueError("inactive model cannot produce a current forecast")
        confidence = _bounded_confidence(confidence)
        evidence_ids = self._require_evidence(parent_evidence_ids)
        forecast_ids = _nonempty_strings(parent_forecast_ids, "parent_forecast_ids")
        if not evidence_ids and not forecast_ids:
            raise ValueError("forecast requires evidence or forecast ancestry")
        observed, generated, ancestor_ceiling = self._forecast_ancestry(
            parent_evidence_ids=evidence_ids,
            parent_forecast_ids=forecast_ids,
        )
        if ancestor_ceiling is not None:
            confidence = min(confidence, ancestor_ceiling)

        parent_ids = list(evidence_ids)
        parent_ids.extend(self.forecasts[fid].evidence.evidence_id for fid in forecast_ids)
        evidence = self.kernel.derive(
            producer="cognition:world-model",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={
                "object_type": "FORECAST",
                "model_id": model_id,
                "target": target,
                "expected": expected,
                "horizon": horizon,
                "confidence": confidence,
                "action_conditional": bool(action_conditional),
            },
            parent_ids=tuple(parent_ids),
            influence_roles=("PREDICTION",),
        )
        forecast = Forecast(
            forecast_id=self._id("forecast"),
            model_id=model_id,
            target=target,
            expected=expected,
            horizon=horizon,
            confidence=confidence,
            evidence=evidence,
            parent_evidence_ids=evidence_ids,
            parent_forecast_ids=forecast_ids,
            observed_ancestor_ids=observed,
            generated_ancestor_ids=generated,
            assumptions=_nonempty_strings(assumptions, "assumptions"),
            action_conditional=bool(action_conditional),
        )
        self.forecasts[forecast.forecast_id] = forecast
        return forecast

    def simulate_counterfactual(
        self,
        *,
        goal: str,
        model_id: str,
        base_evidence_ids: Iterable[str],
        hypothetical_modifications: Any,
        generated_outcomes: Any,
        confidence: float,
    ) -> Simulation:
        if model_id not in self.models:
            raise ValueError("unknown model")
        base = self._require_evidence(base_evidence_ids)
        confidence = _bounded_confidence(confidence)
        evidence = self.kernel.derive(
            producer="cognition:simulation",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={
                "object_type": "COUNTERFACTUAL_SIMULATION",
                "goal": goal,
                "model_id": model_id,
                "hypothetical_modifications": hypothetical_modifications,
                "generated_outcomes": generated_outcomes,
                "confidence": confidence,
                "provenance": "SIMULATED",
            },
            parent_ids=base,
            influence_roles=("SIMULATION", "COUNTERFACTUAL"),
        )
        simulation = Simulation(
            simulation_id=self._id("simulation"),
            goal=goal,
            model_id=model_id,
            base_evidence_ids=base,
            hypothetical_modifications=hypothetical_modifications,
            generated_outcomes=generated_outcomes,
            confidence=confidence,
            evidence=evidence,
        )
        self.simulations[simulation.simulation_id] = simulation
        return simulation

    def rehearse_action(
        self,
        *,
        model_id: str,
        action_scope: str,
        target_scope: str,
        payload: Any,
        predicted_outcome: Any,
        confidence: float,
        parent_evidence_ids: Iterable[str],
    ) -> ActionRehearsal:
        forecast = self.forecast(
            model_id=model_id,
            target=target_scope,
            expected=predicted_outcome,
            horizon="ACTION_CONDITIONAL",
            confidence=confidence,
            parent_evidence_ids=parent_evidence_ids,
            assumptions=(f"if action {action_scope} is taken",),
            action_conditional=True,
        )
        candidate = self.kernel.plan_effect(
            origin="cognition:planner",
            action_scope=action_scope,
            target_scope=target_scope,
            payload=payload,
            authority_grant_id=None,
            parent_ids=(forecast.evidence.evidence_id,),
        )
        return ActionRehearsal(
            rehearsal_id=self._id("rehearsal"),
            forecast=forecast,
            action_candidate=candidate,
        )

    def forecast_state(self, forecast_id: str) -> Forecast:
        forecast = self.forecasts.get(forecast_id)
        if forecast is None:
            raise ValueError("unknown forecast")
        return forecast

    def _descendants_of(self, forecast_id: str) -> Tuple[str, ...]:
        descendants: list[str] = []
        frontier = [forecast_id]
        while frontier:
            parent = frontier.pop()
            direct = [
                candidate.forecast_id
                for candidate in self.forecasts.values()
                if parent in candidate.parent_forecast_ids
            ]
            for child in direct:
                if child not in descendants:
                    descendants.append(child)
                    frontier.append(child)
        return tuple(descendants)

    def reconcile_forecast(
        self,
        forecast_id: str,
        *,
        observation_evidence_id: str,
        matched: bool,
    ) -> ForecastReconciliation:
        forecast = self.forecast_state(forecast_id)
        observation = self.kernel.evidence.get(observation_evidence_id)
        if observation is None:
            raise ValueError("unknown observation evidence")
        if observation.epistemic_class != EpistemicClass.OBSERVATION:
            raise ValueError("forecast reconciliation requires raw observation")
        descendants = self._descendants_of(forecast_id)
        status = "CONFIRMED_WITHIN_SCOPE" if matched else "CONTRADICTED"
        self.forecasts[forecast_id] = replace(forecast, status=status)
        if not matched:
            for descendant_id in descendants:
                child = self.forecasts[descendant_id]
                self.forecasts[descendant_id] = replace(
                    child,
                    status="STALE_REEVALUATE",
                )
        return ForecastReconciliation(
            forecast_id=forecast_id,
            observation_evidence_id=observation_evidence_id,
            matched=bool(matched),
            status=status,
            descendant_forecast_ids=descendants,
        )
