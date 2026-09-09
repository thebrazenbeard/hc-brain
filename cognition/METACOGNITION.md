# Metacognition

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `cognition/`, metacognition monitors and reasons about the HC's own cognitive processes: confidence, uncertainty, strategy quality, knowledge gaps, resource use, error patterns, and when broader evidence or a different approach is needed.

Metacognition is self-monitoring of cognition, not a second little mind watching the first and not a universal executive.

## Core capabilities

- estimate confidence and uncertainty;
- detect unresolved conflict;
- identify missing knowledge/capability;
- monitor strategy performance;
- detect repeated error or loop behavior;
- propose broader coalition recruitment;
- identify when external evidence/tool use could materially help;
- distinguish observed result from inferred explanation;
- track whether a prediction/intervention discriminated competing hypotheses;
- propose bounded review/recovery strategies.

## Confidence discipline

Confidence should be tied to evidence/model state rather than prose fluency, salience, repetition, or self-assertion.

```text
FLUENCY != CONFIDENCE_EVIDENCE
REPETITION != CORROBORATION
```

## Metacognitive trace

A metacognitive trace may record:

- task/context;
- strategy attempted;
- assumptions;
- evidence obtained;
- outcome;
- residual uncertainty;
- error/failure class;
- resource cost;
- recommendation: continue / expand / revise / stop / seek evidence.

The trace is evidence about a cognitive process, not automatic truth about why that process behaved as it did.

## External-compute/tool decision

Metacognition may conclude that external search, retrieval, compute, or specialist services would improve a task. That decision routes through HC-owned interfaces and does not outsource ownership of belief, self-state, memory admission, or final action selection.

## Legitimate uncertainty states

The architecture should be able to represent states equivalent to:

```text
UNKNOWN
UNCERTAIN
UNRESOLVED_CONFLICT
CURRENT_MODEL_INADEQUATE
LAST_ACTION_FAILED
EVIDENCE_STALE
STRATEGY_NOT_WORKING
```

without forcing premature certainty merely to satisfy an output format.

## Resource bound

Metacognitive monitoring consumes resources and must itself be subject to salience, task, and termination constraints. Reflection should expand when it improves diagnosis or decision quality and terminate when it ceases to add value.

## Temporal-hypergraph role

Metacognitive processes may be recruited into a coalition when uncertainty, conflict, failure, or high consequence warrants them. They need not participate equally in every cognitive event.

## Failure modes

- confidence inferred from eloquence;
- endless self-analysis starves the primary task;
- metacognitive monitor becomes a universal executive;
- uncertainty is hidden to satisfy a renderer/schema;
- repeated failure is rationalized instead of triggering strategy change;
- self-critique is automatically trusted without task/evidence support;
- a retrospective explanation is misreported as direct causal observation.

## Provenance

Reconciled from PR #4 `metacognition/README.md` into the canonical `cognition/` root.