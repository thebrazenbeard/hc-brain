# Action Planning and Selection

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: remapped from Draft PR #4 `action/README.md` into the canonical `cognition/` root.

## Purpose

This contract converts goals, predictions, body/world models, procedural memory, and current constraints into internal action candidates and plans.

External actuation remains a separate HC-owned kinesis/interface operation after required arbitration, authority, and safety gating.

## Core separation

```text
GOAL
!= ACTION_CANDIDATE
!= SELECTED_ACTION
!= AUTHORIZED_EFFECT
!= MOTOR_COMMAND
!= VERIFIED_EFFECT
```

## Action candidate

A candidate may include:

- goal/reference;
- proposed action sequence or policy;
- expected consequences;
- body/effector requirements;
- resource cost;
- uncertainty;
- reversible/irreversible classification;
- safety/authority requirements;
- alternatives;
- evidence/model refs;
- fallback/abort criteria.

## Planning inputs

Planning may use procedural memory, world-model simulation, current body schema, temporal constraints, social consequences, affect/conation, values/commitments, and assurance requirements.

Simulated consequences remain hypothetical until observed.

## Selection

Action arbitration selects from currently eligible candidates. Selection does not itself authorize an external effect.

## Consequence loop

Executed actions feed consequence evidence back through body/environment interfaces for model revision, procedural learning, calibration, and memory.

## Failure modes

- plan treated as execution;
- procedural fluency bypasses authority;
- simulation stored as observed consequence;
- stale body capabilities used;
- irreversible action lacks required assurance;
- failure/abort signals ignored during execution.
