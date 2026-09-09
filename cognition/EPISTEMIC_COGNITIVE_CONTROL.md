# Epistemic Cognitive Control

Status: identity-neutral template architecture synthesis.

## Purpose

The cognition subsystem needs a control model for maintaining competing hypotheses, deciding what observation would reduce uncertainty, separating prediction from explanation, and preventing a high-performing shortcut from becoming a prematurely reified world model.

This design synthesizes reusable mechanisms from Noema, ABIL, UNVTRSLR, Semantic Atlas, and multi-perspective arbitration patterns.

## Core cognitive loop

A generic HC cognitive cycle should support:

`observe -> encode evidence -> generate hypotheses -> predict -> compare -> choose discriminating observation/intervention -> update -> arbitrate -> plan -> act or abstain`

The loop must permit passive observation, active experimentation, social interaction, and purely internal simulation without assuming that every environment exposes the same action affordances.

## Hypothesis population

The cognitive core should maintain a bounded but revisable population of hypotheses rather than one unconstrained narrative.

Each hypothesis should carry:

- stable ID;
- claim family;
- scope;
- generative/predictive model or executable constraints where available;
- supporting evidence;
- contradicting evidence;
- unresolved observations;
- expected discriminators;
- complexity/cost estimate;
- provenance;
- uncertainty;
- lifecycle state.

Recommended lifecycle:

- `PROPOSED`
- `ACTIVE`
- `SUPPORTED`
- `WEAKENED`
- `CONTRADICTED`
- `SUPERSEDED`
- `REOPENED`
- `RETIRED`
- `UNRESOLVED`

A retired model remains historical evidence and may be reopened if the regime changes.

## Rival adequacy

`NONE_OF_DECLARED_RIVALS` is an escape hatch, not proof that the hypothesis family is adequate.

The cognitive core should distinguish:

- `REJECTION_ESCAPE_PRESENT`
- `STRUCTURED_ALTERNATIVE_STRESS_NOT_ESTABLISHED`
- `STRUCTURED_ALTERNATIVE_STRESS_TESTED`
- `RIVAL_FAMILY_MISSPECIFICATION_DETECTED`
- `BEST_SUPPORTED_AMONG_DECLARED_RIVALS_ONLY`

Open-ended cognition cannot generally prove that all plausible models have been enumerated. Strong conclusions should remain bound to the actual rival set and tested regimes.

## Prediction, explanation, and control

Three capabilities must remain separable:

1. `PREDICTIVE_COMPETENCE` — forecast future observations;
2. `EXPLANATORY_MODEL` — represent reusable relationships that organize observations;
3. `CONTROL_COMPETENCE` — choose actions that reliably influence outcomes.

A system may predict without causal understanding, control by exploiting correlations, or explain without having actuation capability.

## Correlation and causality

The runtime should track whether a learned relation is:

- observational association;
- temporally predictive;
- intervention-supported;
- counterfactually supported;
- mechanism-supported;
- unresolved.

When intervention is impossible or unsafe, the system should preserve the causal uncertainty rather than relabel correlation as cause.

## Regime and drift detection

The world model should assume that learned relationships may change.

Useful state includes:

- current inferred regime;
- known historical regimes;
- regime-transition evidence;
- sensor/proxy reliability;
- drift score by relation rather than one global drift scalar;
- hypotheses reopened because of drift;
- stable invariants that survived the shift.

A formerly reliable proxy can become misleading. Drift detection should therefore be able to lower reliance on a feature without deleting its historical usefulness.

## Discriminating information selection

When several live hypotheses make different predictions, cognition should prefer observations or interventions that maximize expected discrimination subject to cost, risk, authority, and reversibility.

Candidate evaluation dimensions:

- expected information gain;
- physical/operational risk;
- reversibility;
- energy/time cost;
- social cost;
- privacy cost;
- action authority;
- sensor confidence;
- downstream learning value.

The highest information-gain action is not automatically authorized.

## Multi-perspective cognition

Complex questions may be evaluated by specialized cognitive facets or transient coalitions. Their outputs should be snapshot-bound perspectives rather than independent truths.

An arbitration record should bind:

- question/task state;
- snapshot digest or equivalent state binding;
- contributing perspectives;
- disagreements;
- shared evidence;
- decision/rationale;
- unresolved minority hypotheses;
- decision confidence;
- reopening conditions.

This supports distributed cognition without a permanent master interpreter.

## Semantic and pragmatic boundary

Cognition may propose meanings, but semantic canon and pragmatic interaction state remain separate subsystems.

`COGNITIVE_HYPOTHESIS != SEMANTIC_ADJUDICATION`

`PREDICTED_INTENT != PRAGMATIC_FACT`

Likewise, a chosen plan does not itself authorize kinesis.

`PLAN != ACTION_AUTHORITY`

## Memory interaction

The cognitive core should query both active and archival memory through provenance-preserving interfaces. Retrieval should return:

- content;
- source;
- temporal scope;
- lifecycle/currentness;
- evidence class;
- uncertainty;
- privacy/access scope;
- retrieval relevance.

Retrieval relevance is not truth or currentness.

## Failure modes

- single-hypothesis lock-in;
- reward/policy shortcuts mistaken for world models;
- explaining only after observing outcome;
- fresh IID data mistaken for discriminating evidence;
- treating model confidence as environment certainty;
- forgetting regime changes;
- collapsing multi-perspective disagreement into a hidden majority vote;
- allowing cognitive conclusions to bypass semantic, authority, safety, or action gates.

## Evidence boundary

This is an architecture synthesis for persistent predictive cognition. It does not establish that any chosen internal representation is uniquely correct or sufficient for general intelligence.
