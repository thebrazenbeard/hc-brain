# Action Planning and Selection

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: remapped from PR #4 `action/README.md`. External effect authorization/execution remains owned by canonical `kinesis/ACTION_GATEWAY.md`.

## Purpose

This contract builds internal action candidates and plans from goals, world/body models, procedural memory, constraints, and predicted consequences.

```text
GOAL
!= ACTION_CANDIDATE
!= SELECTED_ACTION
!= AUTHORIZED_EFFECT
!= MOTOR_COMMAND
!= VERIFIED_EFFECT
```

## Candidate contents

A candidate may carry:

- goal/referent;
- proposed action sequence or policy;
- predicted consequences;
- assumptions and evidence refs;
- body/effector requirements;
- resource/energy/time cost;
- uncertainty and competing plans;
- reversibility/consequence class;
- authority/safety prerequisites;
- fallback, abort, and replanning criteria.

## Planning inputs

Planning may recruit world-model prediction, procedural memory, body schema, chronology, social models, affect, conation, values/commitments, metacognition, and current resource state through a task-local coalition.

Simulated consequences remain hypotheses.

```text
SIMULATED_EFFECT != OBSERVED_EFFECT
```

## Selection boundary

Action arbitration may select a candidate under current evidence and concerns while preserving unresolved uncertainty or losing alternatives. Selection forwards an `ActionCandidate` to the canonical action gateway; it does not create permission.

## Closed loop

```text
candidate
→ select
→ authorize/withhold
→ motor/effect plan
→ execute if allowed
→ observe consequence
→ compare prediction
→ revise world/body/procedural models where eligible
```

## Failure modes

- plan reported as execution;
- procedural fluency bypasses authority;
- simulation written as observation/history;
- stale body capability used;
- irreversible effect planned without consequence classification;
- abort/failure evidence ignored;
- selected action treated as epistemic proof that its assumptions were true.
