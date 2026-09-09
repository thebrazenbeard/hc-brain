# Metacognition

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: remapped from PR #4 `metacognition/README.md` into canonical `cognition/`.

## Purpose

Metacognition monitors and reasons about HC cognitive processes: confidence, uncertainty, strategy quality, knowledge gaps, resource use, error patterns, and whether to continue, broaden, revise, stop, or seek evidence.

Metacognition is not a second mind observing the first and is not a universal executive.

## Core capabilities

- estimate confidence/uncertainty;
- detect unresolved conflict and stale evidence;
- identify missing knowledge/capability;
- monitor strategy and coalition performance;
- detect repeated failure, deadlock, or loop behavior;
- recommend coalition expansion or contraction;
- decide when retrieval/external evidence would materially improve the task;
- distinguish observed outcome from inferred explanation;
- track whether an experiment/intervention actually discriminated hypotheses;
- initiate bounded review/recovery proposals.

## Confidence discipline

Confidence must derive from evidence/model state and calibration, not fluency, salience, repetition, or self-assertion.

## Metacognitive trace

A trace may record:

- task/context;
- strategy attempted;
- assumptions;
- evidence cut;
- outcome;
- residual uncertainty/conflict;
- resource cost;
- error/failure class;
- recommendation: continue | expand | revise | stop | seek evidence | recover.

## External-evidence boundary

A metacognitive process may decide that external search, compute, retrieval, or measurement would help. That routes through HC-owned interfaces; it does not outsource ownership of the cognitive task or allow external output to bypass evidence admission.

## Operational uncertainty states

```text
UNKNOWN
UNCERTAIN
CONFLICT
STALE_EVIDENCE
STRATEGY_FAILURE
ACTION_FAILURE
INSUFFICIENT_CAPABILITY
```

These are legitimate states, not defects to hide for output fluency.

## Failure modes

- confidence inferred from eloquence;
- endless self-analysis starving the primary task;
- monitor promoted into master executive;
- uncertainty hidden to satisfy a renderer;
- repeated failure rationalized instead of changing strategy;
- self-critique trusted without task/evidence support;
- metacognitive recommendation treated as effect authority.
