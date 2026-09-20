from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Any, Iterable, Mapping, Tuple

from runtime.reference_kernel.hc_kernel import (
    EffectCandidate,
    EpistemicClass,
    EvidenceRecord,
    ReferenceKernel,
)
from runtime.cognitive_core.homeostasis_somatics import BodySchemaRuntime


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


class MotorPlanState(str, Enum):
    PLANNED = "PLANNED"
    STALE_BODY_SCHEMA = "STALE_BODY_SCHEMA"
    BLOCKED = "BLOCKED"


class SkillState(str, Enum):
    CANDIDATE = "CANDIDATE"
    CONSOLIDATED = "CONSOLIDATED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class MotorPlan:
    plan_id: str
    effector: str
    target: Mapping[str, Any]
    action_scope: str
    target_scope: str
    payload: Any
    body_schema_id: str
    evidence: EvidenceRecord
    action_candidate: EffectCandidate
    state: MotorPlanState = MotorPlanState.PLANNED


@dataclass(frozen=True)
class TrajectoryPrediction:
    trajectory_id: str
    plan_id: str
    waypoints: Tuple[Mapping[str, Any], ...]
    confidence: float
    evidence: EvidenceRecord
    status: str = "PREDICTED_TRAJECTORY"


@dataclass(frozen=True)
class LocalStabilizer:
    effector: str
    max_adjustment: float
    basis_refs: Tuple[str, ...]


@dataclass(frozen=True)
class LocalStabilization:
    adjustment_id: str
    effector: str
    adjustment: float
    reason_refs: Tuple[str, ...]
    status: str = "APPLIED_LOCAL_STABILIZATION"


@dataclass(frozen=True)
class MotorSkill:
    skill_id: str
    effector: str
    action_scope: str
    source_plan_ids: Tuple[str, ...]
    source_evidence_ids: Tuple[str, ...]
    evidence: EvidenceRecord
    state: SkillState = SkillState.CANDIDATE
    basis_refs: Tuple[str, ...] = ()


class MotorControlRuntime:
    """Bounded HC kinesis/motor-learning reference slice."""

    def __init__(self, kernel: ReferenceKernel, body: BodySchemaRuntime) -> None:
        self.kernel = kernel
        self.body = body
        self.plans: dict[str, MotorPlan] = {}
        self.trajectories: dict[str, TrajectoryPrediction] = {}
        self.stabilizers: dict[str, LocalStabilizer] = {}
        self.stabilization_history: list[LocalStabilization] = []
        self.skills: dict[str, MotorSkill] = {}
        self._serial = 0

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    def _current_effector_capability(self, effector: str) -> Mapping[str, Any]:
        schema = self.body.current_schema
        if schema.calibration_status != "CALIBRATED":
            raise ValueError("motor planning requires calibrated body schema")
        capability = schema.actuator_capabilities.get(effector)
        if not isinstance(capability, Mapping):
            raise ValueError("unknown or unavailable effector")
        return capability

    def _validate_target(self, effector: str, target: Mapping[str, Any]) -> None:
        capability = self._current_effector_capability(effector)
        distance = target.get("distance")
        if distance is not None:
            distance = float(distance)
            reach = capability.get("reach")
            if reach is None:
                raise ValueError("effector reach is unknown")
            if distance < 0.0 or distance > float(reach):
                raise ValueError("target is outside calibrated effector reach")

    def plan_movement(
        self,
        *,
        effector: str,
        target: Mapping[str, Any],
        action_scope: str,
        target_scope: str,
        payload: Any,
    ) -> MotorPlan:
        if not effector or not action_scope or not target_scope:
            raise ValueError("effector, action scope, and target scope are required")
        self._validate_target(effector, target)
        schema = self.body.current_schema
        if not schema.source_evidence_ids:
            raise ValueError("calibrated body schema lacks evidence lineage")

        evidence = self.kernel.derive(
            producer="kinesis:motor-planner",
            epistemic_class=EpistemicClass.DERIVED,
            payload={
                "object_type": "MOTOR_PLAN",
                "effector": effector,
                "target": dict(target),
                "action_scope": action_scope,
                "target_scope": target_scope,
                "body_schema_id": schema.schema_id,
            },
            parent_ids=schema.source_evidence_ids,
            influence_roles=("MOTOR_PLANNING", "BODY_SCHEMA"),
        )
        candidate = self.kernel.plan_effect(
            origin="kinesis",
            action_scope=action_scope,
            target_scope=target_scope,
            payload=payload,
            authority_grant_id=None,
            parent_ids=(evidence.evidence_id,),
        )
        plan = MotorPlan(
            plan_id=self._id("motor-plan"),
            effector=effector,
            target=dict(target),
            action_scope=action_scope,
            target_scope=target_scope,
            payload=payload,
            body_schema_id=schema.schema_id,
            evidence=evidence,
            action_candidate=candidate,
        )
        self.plans[plan.plan_id] = plan
        return plan

    def validate_plan(self, plan_id: str) -> MotorPlan:
        plan = self.plans.get(plan_id)
        if plan is None:
            raise ValueError("unknown motor plan")
        if self.body.current_schema.schema_id != plan.body_schema_id:
            plan = replace(plan, state=MotorPlanState.STALE_BODY_SCHEMA)
            self.plans[plan_id] = plan
        return plan

    def predict_trajectory(
        self,
        plan_id: str,
        *,
        waypoints: Iterable[Mapping[str, Any]],
        confidence: float,
    ) -> TrajectoryPrediction:
        plan = self.validate_plan(plan_id)
        if plan.state != MotorPlanState.PLANNED:
            raise ValueError("stale or blocked motor plan cannot produce current trajectory")
        confidence = _bounded(confidence, "confidence")
        waypoint_tuple = tuple(dict(point) for point in waypoints)
        if not waypoint_tuple:
            raise ValueError("trajectory requires at least one waypoint")
        for point in waypoint_tuple:
            self._validate_target(plan.effector, point)
        evidence = self.kernel.derive(
            producer="kinesis:trajectory-predictor",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={
                "object_type": "MOTOR_TRAJECTORY_PREDICTION",
                "plan_id": plan_id,
                "waypoints": waypoint_tuple,
                "confidence": confidence,
                "body_schema_id": plan.body_schema_id,
            },
            parent_ids=(plan.evidence.evidence_id,),
            influence_roles=("MOTOR_PREDICTION",),
        )
        trajectory = TrajectoryPrediction(
            trajectory_id=self._id("trajectory"),
            plan_id=plan_id,
            waypoints=waypoint_tuple,
            confidence=confidence,
            evidence=evidence,
        )
        self.trajectories[trajectory.trajectory_id] = trajectory
        return trajectory

    def register_local_stabilizer(
        self,
        *,
        effector: str,
        max_adjustment: float,
        basis_refs: Iterable[str],
    ) -> LocalStabilizer:
        self._current_effector_capability(effector)
        max_adjustment = float(max_adjustment)
        if max_adjustment <= 0.0:
            raise ValueError("max_adjustment must be positive")
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("local stabilizer requires basis_refs")
        stabilizer = LocalStabilizer(
            effector=effector,
            max_adjustment=max_adjustment,
            basis_refs=basis,
        )
        self.stabilizers[effector] = stabilizer
        return stabilizer

    def apply_local_stabilization(
        self,
        *,
        effector: str,
        adjustment: float,
        reason_refs: Iterable[str],
    ) -> LocalStabilization:
        stabilizer = self.stabilizers.get(effector)
        if stabilizer is None:
            raise PermissionError("no registered local stabilizer for effector")
        adjustment = float(adjustment)
        if abs(adjustment) > stabilizer.max_adjustment:
            raise PermissionError("local stabilization exceeds registered envelope")
        reasons = _strings(reason_refs, "reason_refs")
        if not reasons:
            raise ValueError("local stabilization requires reason_refs")
        item = LocalStabilization(
            adjustment_id=self._id("stabilization"),
            effector=effector,
            adjustment=adjustment,
            reason_refs=reasons,
        )
        self.stabilization_history.append(item)
        return item

    def record_observed_outcome(
        self,
        plan_id: str,
        *,
        observation_evidence_id: str,
        success: bool,
    ) -> MotorSkill:
        plan = self.plans.get(plan_id)
        if plan is None:
            raise ValueError("unknown motor plan")
        outcome = self.kernel.evidence.get(observation_evidence_id)
        if outcome is None:
            raise ValueError("unknown motor outcome evidence")
        if outcome.epistemic_class != EpistemicClass.OBSERVATION:
            raise ValueError("motor-skill evidence must be observed, not simulated")
        evidence = self.kernel.derive(
            producer="kinesis:motor-learning",
            epistemic_class=EpistemicClass.DERIVED,
            payload={
                "object_type": "MOTOR_SKILL_CANDIDATE",
                "plan_id": plan_id,
                "effector": plan.effector,
                "action_scope": plan.action_scope,
                "success": bool(success),
            },
            parent_ids=(plan.evidence.evidence_id, observation_evidence_id),
            influence_roles=("MOTOR_LEARNING",),
        )
        skill = MotorSkill(
            skill_id=self._id("motor-skill"),
            effector=plan.effector,
            action_scope=plan.action_scope,
            source_plan_ids=(plan_id,),
            source_evidence_ids=(observation_evidence_id,),
            evidence=evidence,
        )
        self.skills[skill.skill_id] = skill
        return skill

    def consolidate_skill(
        self,
        skill_id: str,
        *,
        basis_refs: Iterable[str],
    ) -> MotorSkill:
        skill = self.skills.get(skill_id)
        if skill is None:
            raise ValueError("unknown motor skill")
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("motor-skill consolidation requires basis_refs")
        consolidated = replace(
            skill,
            state=SkillState.CONSOLIDATED,
            basis_refs=basis,
        )
        self.skills[skill_id] = consolidated
        return consolidated
