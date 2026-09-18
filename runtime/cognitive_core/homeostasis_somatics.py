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


class InternalSignalState(str, Enum):
    AGREEMENT = "AGREEMENT"
    SENSOR_CONFLICT = "SENSOR_CONFLICT"
    CALIBRATION_SUSPECT = "CALIBRATION_SUSPECT"
    SOURCE_UNAVAILABLE = "SOURCE_UNAVAILABLE"
    STALE_STATE = "STALE_STATE"
    SATURATED = "SATURATED"
    FAULTED = "FAULTED"
    UNRESOLVED = "UNRESOLVED"


class RegulatoryTimescale(str, Enum):
    FAST_PROTECTIVE = "FAST_PROTECTIVE"
    SHORT_REGULATORY = "SHORT_REGULATORY"
    SLOW_MODULATORY = "SLOW_MODULATORY"
    RECOVERY_AND_PLASTICITY = "RECOVERY_AND_PLASTICITY"


@dataclass(frozen=True)
class InteroceptiveObservation:
    observation_id: str
    channel: str
    source: str
    value: float
    units: str
    reliability: float
    evidence: EvidenceRecord
    signal_state: InternalSignalState = InternalSignalState.AGREEMENT


@dataclass(frozen=True)
class PhysiologicalEstimate:
    estimate_id: str
    variable: str
    value: float
    confidence: float
    observation_ids: Tuple[str, ...]
    evidence: EvidenceRecord
    signal_state: InternalSignalState


@dataclass(frozen=True)
class RegulatoryTarget:
    target_id: str
    variable: str
    minimum: float
    maximum: float
    basis_refs: Tuple[str, ...]
    supersedes: Tuple[str, ...] = ()


@dataclass(frozen=True)
class RegulatoryError:
    error_id: str
    estimate_id: str
    target_id: str
    magnitude: float
    direction: str
    urgency: float
    evidence: EvidenceRecord


@dataclass(frozen=True)
class RegulatoryModulation:
    modulation_id: str
    error_id: str
    arousal_pressure: float
    threat_pressure: float
    negative_valence_pressure: float
    source_refs: Tuple[str, ...]
    evidence: EvidenceRecord


@dataclass(frozen=True)
class RegulatoryRequest:
    request_id: str
    error_id: str
    effect_scope: str
    target_scope: str
    timescale: RegulatoryTimescale
    urgency: float
    action_candidate: EffectCandidate


@dataclass(frozen=True)
class ProtectiveScope:
    effect_scope: str
    target_scope: str
    minimum: float
    maximum: float
    basis_refs: Tuple[str, ...]


@dataclass(frozen=True)
class ProtectiveDecision:
    decision_id: str
    effect_scope: str
    target_scope: str
    value: float
    reason_refs: Tuple[str, ...]
    status: str = "APPLIED_LOCAL_PROTECTIVE"


class RegulatoryRuntime:
    """Bounded HC homeostasis/interoception reference slice."""

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self.observations: dict[str, InteroceptiveObservation] = {}
        self.estimates: dict[str, PhysiologicalEstimate] = {}
        self.targets: dict[str, RegulatoryTarget] = {}
        self.errors: dict[str, RegulatoryError] = {}
        self.requests: dict[str, RegulatoryRequest] = {}
        self.protective_scopes: dict[tuple[str, str], ProtectiveScope] = {}
        self.protective_history: list[ProtectiveDecision] = []
        self._serial = 0

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    def observe_internal(
        self,
        *,
        channel: str,
        source: str,
        value: float,
        units: str,
        reliability: float,
        signal_state: InternalSignalState = InternalSignalState.AGREEMENT,
    ) -> InteroceptiveObservation:
        if not channel or not source or not units:
            raise ValueError("channel, source, and units are required")
        reliability = _bounded(reliability, "reliability")
        value = float(value)
        evidence = self.kernel.observe(
            producer=source,
            payload={
                "object_type": "INTEROCEPTIVE_OBSERVATION",
                "channel": channel,
                "value": value,
                "units": units,
                "reliability": reliability,
                "signal_state": signal_state.value,
            },
        )
        observation = InteroceptiveObservation(
            observation_id=self._id("interoception"),
            channel=channel,
            source=source,
            value=value,
            units=units,
            reliability=reliability,
            evidence=evidence,
            signal_state=signal_state,
        )
        self.observations[observation.observation_id] = observation
        return observation

    def estimate(
        self,
        *,
        variable: str,
        observation_ids: Iterable[str],
        conflict_threshold: float = 0.25,
    ) -> PhysiologicalEstimate:
        ids = _strings(observation_ids, "observation_ids")
        if not ids:
            raise ValueError("physiological estimate requires observations")
        conflict_threshold = _bounded(conflict_threshold, "conflict_threshold")
        records = []
        for oid in ids:
            record = self.observations.get(oid)
            if record is None:
                raise ValueError(f"unknown internal observation: {oid}")
            if record.channel != variable:
                raise ValueError("observation channel does not match estimate variable")
            records.append(record)

        total_weight = sum(item.reliability for item in records)
        if total_weight <= 0.0:
            value = sum(item.value for item in records) / len(records)
            confidence = 0.0
        else:
            value = sum(item.value * item.reliability for item in records) / total_weight
            confidence = sum(item.reliability for item in records) / len(records)

        spread = max(item.value for item in records) - min(item.value for item in records)
        signal_state = (
            InternalSignalState.SENSOR_CONFLICT
            if len(records) > 1 and spread > conflict_threshold
            else InternalSignalState.AGREEMENT
        )
        if signal_state == InternalSignalState.SENSOR_CONFLICT:
            confidence *= 0.5

        evidence = self.kernel.derive(
            producer="homeostasis-interoception:estimator",
            epistemic_class=EpistemicClass.INFERRED,
            payload={
                "object_type": "PHYSIOLOGICAL_ESTIMATE",
                "variable": variable,
                "value": value,
                "confidence": confidence,
                "signal_state": signal_state.value,
            },
            parent_ids=tuple(item.evidence.evidence_id for item in records),
            influence_roles=("INTEROCEPTIVE_FUSION",),
        )
        estimate = PhysiologicalEstimate(
            estimate_id=self._id("phys-estimate"),
            variable=variable,
            value=value,
            confidence=confidence,
            observation_ids=ids,
            evidence=evidence,
            signal_state=signal_state,
        )
        self.estimates[estimate.estimate_id] = estimate
        return estimate

    def set_target(
        self,
        *,
        variable: str,
        minimum: float,
        maximum: float,
        basis_refs: Iterable[str],
        supersedes: Iterable[str] = (),
    ) -> RegulatoryTarget:
        if not variable:
            raise ValueError("target variable is required")
        minimum = float(minimum)
        maximum = float(maximum)
        if maximum < minimum:
            raise ValueError("target maximum must be >= minimum")
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("regulatory target requires basis_refs")
        supersedes_tuple = _strings(supersedes, "supersedes")
        for target_id in supersedes_tuple:
            if target_id not in self.targets:
                raise ValueError(f"unknown superseded target: {target_id}")
        target = RegulatoryTarget(
            target_id=self._id("reg-target"),
            variable=variable,
            minimum=minimum,
            maximum=maximum,
            basis_refs=basis,
            supersedes=supersedes_tuple,
        )
        self.targets[target.target_id] = target
        return target

    def revise_target(
        self,
        target_id: str,
        *,
        minimum: float,
        maximum: float,
        basis_refs: Iterable[str],
    ) -> RegulatoryTarget:
        prior = self.targets.get(target_id)
        if prior is None:
            raise ValueError("unknown regulatory target")
        return self.set_target(
            variable=prior.variable,
            minimum=minimum,
            maximum=maximum,
            basis_refs=basis_refs,
            supersedes=(target_id,),
        )

    def compute_error(
        self,
        *,
        estimate_id: str,
        target_id: str,
    ) -> RegulatoryError:
        estimate = self.estimates.get(estimate_id)
        target = self.targets.get(target_id)
        if estimate is None or target is None:
            raise ValueError("unknown estimate or target")
        if estimate.variable != target.variable:
            raise ValueError("estimate and target variable mismatch")
        if estimate.value < target.minimum:
            direction = "LOW"
            magnitude = target.minimum - estimate.value
        elif estimate.value > target.maximum:
            direction = "HIGH"
            magnitude = estimate.value - target.maximum
        else:
            direction = "WITHIN_RANGE"
            magnitude = 0.0
        span = max(target.maximum - target.minimum, 1e-9)
        urgency = min(1.0, magnitude / span)
        evidence = self.kernel.derive(
            producer="homeostasis-interoception:regulator",
            epistemic_class=EpistemicClass.DERIVED,
            payload={
                "object_type": "REGULATORY_ERROR",
                "estimate_id": estimate_id,
                "target_id": target_id,
                "magnitude": magnitude,
                "direction": direction,
                "urgency": urgency,
            },
            parent_ids=(estimate.evidence.evidence_id,),
            influence_roles=("HOMEOSTATIC_ERROR",),
            source_refs=target.basis_refs,
        )
        error = RegulatoryError(
            error_id=self._id("reg-error"),
            estimate_id=estimate_id,
            target_id=target_id,
            magnitude=magnitude,
            direction=direction,
            urgency=urgency,
            evidence=evidence,
        )
        self.errors[error.error_id] = error
        return error

    def build_affective_modulation(self, error_id: str) -> RegulatoryModulation:
        error = self.errors.get(error_id)
        if error is None:
            raise ValueError("unknown regulatory error")
        pressure = min(1.0, error.urgency)
        evidence = self.kernel.derive(
            producer="homeostasis-interoception:modulation",
            epistemic_class=EpistemicClass.DERIVED,
            payload={
                "object_type": "REGULATORY_MODULATION",
                "error_id": error_id,
                "arousal_pressure": pressure,
                "threat_pressure": pressure,
                "negative_valence_pressure": pressure * 0.5,
            },
            parent_ids=(error.evidence.evidence_id,),
            influence_roles=("AFFECT_MODULATION", "HOMEOSTATIC_PRESSURE"),
        )
        return RegulatoryModulation(
            modulation_id=self._id("reg-modulation"),
            error_id=error_id,
            arousal_pressure=pressure,
            threat_pressure=pressure,
            negative_valence_pressure=pressure * 0.5,
            source_refs=(error.evidence.evidence_id,),
            evidence=evidence,
        )

    def propose_regulation(
        self,
        *,
        error_id: str,
        effect_scope: str,
        target_scope: str,
        payload: Any,
        timescale: RegulatoryTimescale,
    ) -> RegulatoryRequest:
        error = self.errors.get(error_id)
        if error is None:
            raise ValueError("unknown regulatory error")
        candidate = self.kernel.plan_effect(
            origin="homeostasis-interoception",
            action_scope=effect_scope,
            target_scope=target_scope,
            payload=payload,
            authority_grant_id=None,
            parent_ids=(error.evidence.evidence_id,),
        )
        request = RegulatoryRequest(
            request_id=self._id("reg-request"),
            error_id=error_id,
            effect_scope=effect_scope,
            target_scope=target_scope,
            timescale=timescale,
            urgency=error.urgency,
            action_candidate=candidate,
        )
        self.requests[request.request_id] = request
        return request

    def register_protective_scope(
        self,
        *,
        effect_scope: str,
        target_scope: str,
        minimum: float,
        maximum: float,
        basis_refs: Iterable[str],
    ) -> ProtectiveScope:
        if not effect_scope or not target_scope:
            raise ValueError("protective effect and target scope are required")
        if not target_scope.startswith("internal:"):
            raise ValueError("standing protective authority is local/internal only")
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("protective scope requires basis_refs")
        minimum = float(minimum)
        maximum = float(maximum)
        if maximum < minimum:
            raise ValueError("protective maximum must be >= minimum")
        scope = ProtectiveScope(
            effect_scope=effect_scope,
            target_scope=target_scope,
            minimum=minimum,
            maximum=maximum,
            basis_refs=basis,
        )
        self.protective_scopes[(effect_scope, target_scope)] = scope
        return scope

    def apply_local_protective_effect(
        self,
        *,
        effect_scope: str,
        target_scope: str,
        value: float,
        reason_refs: Iterable[str],
    ) -> ProtectiveDecision:
        scope = self.protective_scopes.get((effect_scope, target_scope))
        if scope is None:
            raise PermissionError("effect is outside registered local protective scope")
        value = float(value)
        if not scope.minimum <= value <= scope.maximum:
            raise PermissionError("protective value is outside safety envelope")
        reasons = _strings(reason_refs, "reason_refs")
        if not reasons:
            raise ValueError("protective decision requires reason_refs")
        decision = ProtectiveDecision(
            decision_id=self._id("protective-decision"),
            effect_scope=effect_scope,
            target_scope=target_scope,
            value=value,
            reason_refs=reasons,
        )
        self.protective_history.append(decision)
        return decision


@dataclass(frozen=True)
class BodySchemaState:
    schema_id: str
    morphology: Mapping[str, Any]
    pose: Mapping[str, Any]
    actuator_capabilities: Mapping[str, Any]
    calibration_confidence: float
    calibration_status: str
    source_evidence_ids: Tuple[str, ...]


@dataclass(frozen=True)
class ReachabilityPrediction:
    prediction_id: str
    target: Mapping[str, Any]
    confidence: float
    evidence: EvidenceRecord
    status: str = "PREDICTED_REACHABILITY"


class BodySchemaRuntime:
    """Morphology-neutral somatic/body-schema reference slice."""

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self._serial = 0
        self._history: list[BodySchemaState] = []
        self.current_schema = BodySchemaState(
            schema_id=self._id("body-schema"),
            morphology={},
            pose={},
            actuator_capabilities={},
            calibration_confidence=0.0,
            calibration_status="UNCALIBRATED",
            source_evidence_ids=(),
        )
        self._history.append(self.current_schema)

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    @property
    def history(self) -> Tuple[BodySchemaState, ...]:
        return tuple(self._history)

    def _observed_evidence(self, evidence_ids: Iterable[str]) -> Tuple[str, ...]:
        ids = _strings(evidence_ids, "evidence_ids")
        if not ids:
            raise ValueError("body calibration requires observed evidence")
        for eid in ids:
            evidence = self.kernel.evidence.get(eid)
            if evidence is None:
                raise ValueError(f"unknown body evidence: {eid}")
            if evidence.epistemic_class != EpistemicClass.OBSERVATION:
                raise ValueError("lived body calibration requires observed somatic evidence")
        return ids

    def calibrate(
        self,
        *,
        morphology: Mapping[str, Any],
        pose: Mapping[str, Any],
        actuator_capabilities: Mapping[str, Any],
        evidence_ids: Iterable[str],
        confidence: float,
    ) -> BodySchemaState:
        ids = self._observed_evidence(evidence_ids)
        confidence = _bounded(confidence, "confidence")
        state = BodySchemaState(
            schema_id=self._id("body-schema"),
            morphology=dict(morphology),
            pose=dict(pose),
            actuator_capabilities=dict(actuator_capabilities),
            calibration_confidence=confidence,
            calibration_status="CALIBRATED",
            source_evidence_ids=ids,
        )
        self.current_schema = state
        self._history.append(state)
        return state

    def update_pose(
        self,
        *,
        pose: Mapping[str, Any],
        evidence_ids: Iterable[str],
        confidence: float,
    ) -> BodySchemaState:
        if self.current_schema.calibration_status != "CALIBRATED":
            raise ValueError("body schema must be calibrated before pose update")
        ids = self._observed_evidence(evidence_ids)
        confidence = _bounded(confidence, "confidence")
        state = replace(
            self.current_schema,
            schema_id=self._id("body-schema"),
            pose=dict(pose),
            calibration_confidence=confidence,
            source_evidence_ids=tuple(
                dict.fromkeys((*self.current_schema.source_evidence_ids, *ids))
            ),
        )
        self.current_schema = state
        self._history.append(state)
        return state

    def predict_reachability(
        self,
        *,
        target: Mapping[str, Any],
        confidence: float,
    ) -> ReachabilityPrediction:
        if self.current_schema.calibration_status != "CALIBRATED":
            raise ValueError("reachability requires calibrated body schema")
        confidence = _bounded(confidence, "confidence")
        parent_ids = self.current_schema.source_evidence_ids
        evidence = self.kernel.derive(
            producer="somatics:body-schema",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={
                "object_type": "REACHABILITY_PREDICTION",
                "target": dict(target),
                "confidence": confidence,
                "body_schema_id": self.current_schema.schema_id,
            },
            parent_ids=parent_ids,
            influence_roles=("BODY_SCHEMA", "AFFORDANCE_PREDICTION"),
        )
        return ReachabilityPrediction(
            prediction_id=self._id("reachability"),
            target=dict(target),
            confidence=confidence,
            evidence=evidence,
        )
