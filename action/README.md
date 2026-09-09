# Action Planning and Selection

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`action/` converts goals, predictions, body/world models, procedural memory, and current constraints into internal action candidates/plans.

External actuation is handled by HC-owned `interfaces/kinesis/` after authority/safety gating.

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

May include:

- goal/ref;
- proposed action sequence/policy;
- expected consequences;
- body/effector requirements;
- resource cost;
- uncertainty;
- reversible/irreversible classification;
- safety/authority requirements;
- alternatives;
- evidence/model refs;
- fallback/abort criteria.

## Planning

Planning may use:

- procedural memory;
- world-model simulation;
- current body schema;
- temporal constraints;
- social consequences;
- affect/conation;
- values/commitments;
- assurance requirements.

Simulated consequences remain hypothetical until observed.

## Selection

Action arbitration selects from currently eligible candidates. Selected actions still pass through required authority/effect gates before reaching kinesis or another output interface.

## Observation loop

Executed actions feed consequence evidence back through body/environment interfaces for model revision, procedural learning, and memory.

## Failure modes

- internal plan treated as external execution;
- procedural fluency bypasses authority;
- simulation result stored as observed consequence;
- stale body capabilities used;
- irreversible action lacks stronger assurance;
- failure/abort signals ignored during execution.
