# Cognition

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`cognition/` defines generic mechanisms for constructing, comparing, revising, and acting on models of a situation. It is not a single thinker node and does not own truth, identity, or all executive control.

## Core capabilities

- maintain competing hypotheses rather than forcing one explanation too early;
- generate predictions and expected consequences;
- compare hypotheses against evidence;
- select discriminating observations/interventions where allowed;
- reason over causal, temporal, relational, quantitative, and procedural structure;
- plan across multiple steps and interruptions;
- allocate bounded working resources;
- surface uncertainty, conflict, and model inadequacy;
- learn from consequence without silently rewriting source evidence.

## Capability-before-mechanism rule

A named cognitive mechanism earns architectural status only when it addresses a stated capability/failure and survives comparison with simpler alternatives.

```text
capability
→ evidence contract
→ candidate mechanism
→ adversarial test / ablation
→ keep | split | demote | remove
```

Cognitive nouns are not self-justifying modules.

## Hypothesis state

A candidate hypothesis should be able to carry:

- proposition/referent;
- scope/context;
- supporting/opposing evidence refs;
- confidence/support;
- predictions;
- assumptions;
- alternatives;
- currentness;
- status: `ACTIVE`, `WEAKENED`, `REJECTED`, `SUPERSEDED`, `UNRESOLVED`, `CONFLICT`.

Rejected hypotheses may remain historically retrievable without remaining live candidates.

## Truth, value, and resources

The subsystem must preserve:

```text
EVIDENCE_SUPPORT != DESIRABILITY != COMPUTE_PRIORITY
```

A desired outcome does not become more probable because it is desired. A high-priority computation does not make its conclusion more true.

## World-model revision

New evidence should update a model through an explicit transition:

```text
prior model
+ new observation/evidence
+ source/currentness assessment
→ revised candidate model(s)
→ consequence/prediction update
```

If evidence does not discriminate candidates, preserve multiple candidates.

## Intervention boundary

Cognition may propose an intervention because different hypotheses predict different outcomes. Proposal is not authority to act.

```text
DISCRIMINATING_ACTION_CANDIDATE
→ action/authority gate
→ execute | withhold | defer
```

## Coalition behavior

Cognition should form task-local coalitions with only the required specialist systems: semantics, memory, perception, quantitative reasoning, social cognition, action planning, assurance, etc.

No permanent master coalition is required.

## Failure modes

- mechanism name treated as proof of necessity;
- one hypothesis retained despite unresolved competing evidence;
- evaluator terminology promoted into internal ontology without need;
- desired answer biasing truth estimate;
- action capability mistaken for action authority;
- stale model retained after a direct correction/new observation;
- complexity added before a simpler approach fails.

## Interfaces

Consumes typed `SIGNAL`, `EVIDENCE`, `STATE`, and retrieved memory traces.

Produces candidate hypotheses, predictions, plans, discriminating-action candidates, uncertainty/conflict state, and proposals for learning/plasticity.
