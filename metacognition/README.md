# Metacognition

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`metacognition/` monitors and reasons about the HC's own cognitive processes: confidence, uncertainty, strategy quality, knowledge gaps, resource use, error patterns, and when to seek additional evidence or change approach.

Metacognition is self-monitoring of cognition, not a second little mind watching the first.

## Core capabilities

- estimate confidence/uncertainty;
- detect unresolved conflict;
- identify missing knowledge/capability;
- monitor strategy performance;
- detect repeated error or loop behavior;
- decide when broader coalition recruitment is warranted;
- decide when external evidence/tool use would materially help;
- distinguish observed result from inferred explanation;
- track whether a prediction/intervention actually discriminated hypotheses;
- initiate bounded review/recovery strategies.

## Confidence discipline

Confidence should be tied to evidence/model state rather than prose fluency, salience, or repetition.

## Strategy monitoring

A metacognitive trace may record:

- task/context;
- strategy attempted;
- assumptions;
- evidence obtained;
- outcome;
- residual uncertainty;
- error class;
- recommendation: continue / expand / revise / stop / seek evidence.

## Tool/external-compute decision

Metacognition may decide that external compute/search/retrieval would improve the task. That decision routes through the appropriate HC interface and does not outsource ownership of the task or self-state.

## Error awareness

The system should be able to represent:

```text
I_DO_NOT_KNOW
I_AM_UNCERTAIN
MY_CURRENT_MODEL_CONFLICTS
MY_LAST_ACTION_FAILED
MY_EVIDENCE_IS_STALE
MY_STRATEGY_IS_NOT_WORKING
```

as legitimate operational states.

## Failure modes

- confidence inferred from eloquence;
- endless self-analysis starving the primary task;
- metacognitive monitor becoming a universal executive;
- uncertainty hidden to satisfy an output schema;
- repeated failure rationalized instead of triggering strategy change;
- self-critique automatically trusted without external/task evidence.
