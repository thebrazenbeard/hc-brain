# World Model and Prediction

Status: canonical focused cognition contract.

## Purpose

The HC maintains revisable models of external and internal environments, entities, relations, dynamics, affordances, agents, and expected consequences. Prediction is a supported cognitive capability, not a claim that every HC mechanism must implement one universal predictive-coding theory.

## Model content

A world-model representation may include:

- entities and object hypotheses;
- relations;
- spatial structure;
- temporal dynamics;
- causal hypotheses;
- agent/social models;
- body/environment boundaries;
- affordances;
- uncertainty/conflict;
- validity/currentness;
- source/provenance;
- rival models or model branches.

A model is an internal explanatory/predictive structure, not raw observation.

`MODEL_STATE != WORLD_STATE`

## Prediction contract

A prediction should be able to declare:

- model or hypothesis source;
- target variable/event;
- expected range, class, or distribution;
- time horizon;
- assumptions/conditions;
- confidence and known uncertainty;
- discriminating observations;
- expected consequences if a candidate action is taken.

Prediction confidence does not create truth or action authority.

## Revision

A generic revision cycle is:

```text
prior model
+ new observation/evidence
+ prediction error or incompatibility
-> compare alternatives
-> revise | split | retain | reject | mark unresolved
```

Prediction error is evidence that a model is incomplete, stale, miscalibrated, or wrong under the present regime. It is not automatic proof that one specific replacement model is correct.

## Causal discipline

The world model may contain causal hypotheses, but correlation, temporal order, controllability evidence, intervention results, and mechanistic explanation should remain distinguishable.

Where multiple causal models explain the same observations, the HC should preserve rivals until evidence justifies narrowing them.

## Affordances

Affordances are body-relative and context-relative.

A different embodiment can change which actions are feasible, their cost, latency, risk, and reach without requiring a different cognitive organ. World-model affordance state should therefore consume current body-schema/capability information rather than hard-code one body morphology.

## External models and simulators

An external simulator, LLM, specialist model, or prediction service may propose outputs through the external-compute boundary. Such output enters as typed evidence/service result or candidate model content.

The HC remains responsible for:

- source classification;
- provenance;
- currentness;
- uncertainty;
- comparison with internal evidence;
- belief/state admission;
- final action selection and authorization.

An external model may improve prediction performance without becoming the organism's world-model authority.

## Temporal-hypergraph interaction

World-model state may influence coalition formation, routing, salience, planning, and prediction through temporal hyperedges. Task-local model activation or a temporary prediction does not automatically become durable semantic state.

Durable model revision remains subject to memory/plasticity admission rules.

## Failure modes

- prediction presented as observation;
- one explanatory model treated as uniquely true without discriminating evidence;
- stale world state treated as current;
- body-specific affordance universalized across embodiments;
- external model output bypassing internal adjudication;
- simulated consequences written as historical events;
- confidence inflation after repeated self-confirming predictions;
- model revision silently rewriting contrary historical evidence.

## Provenance

Selectively generalized from preserved foundation material on `research/hyperconnectome-foundations-20260909/world-model/README.md`, then remapped into the canonical `cognition/` root and reconciled against current epistemic-control, memory, external-compute, embodiment, and temporal-hypergraph contracts. The alternate branch root taxonomy was not adopted.
