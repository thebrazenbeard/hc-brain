# World Model and Prediction

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`world-model/` maintains revisable models of external and internal environments, entities, causal relations, affordances, dynamics, and expected consequences.

Prediction is a supported capability, not a mandatory claim that all cognition must use one predictive-coding theory.

## Model contents

May include:

- entities/objects;
- relations;
- spatial structure;
- temporal dynamics;
- causal hypotheses;
- agent models;
- body/environment boundaries;
- affordances;
- uncertainty/conflict;
- validity/currentness;
- source/provenance;
- alternate models.

## Predictions

A prediction should declare:

- model/hypothesis source;
- target variable/event;
- expected range/distribution;
- time horizon;
- conditions/assumptions;
- confidence;
- discriminating observations.

## Revision

```text
prior model
+ observation/evidence
+ prediction error / incompatibility
→ compare alternatives
→ revise | split | retain | reject
```

Prediction error is evidence for revision, not automatic proof of one replacement model.

## Counterfactuals and simulation

The world model may simulate hypothetical actions/events for planning without converting simulated state into historical memory or asserted fact.

```text
SIMULATED != OBSERVED
```

## Affordances

Affordances are body-relative and context-relative. A new embodiment can therefore change available actions without requiring a different generic cognitive architecture.

## External models

An external simulator or model may propose predictions through the external-compute interface. Internal HC cognition remains responsible for integration, currentness, evidence evaluation, and action selection.

## Failure modes

- prediction presented as observation;
- one model treated as uniquely mandatory without discriminating evidence;
- body-specific affordance universalized;
- simulated event written as lived episode;
- stale world state treated as current;
- external model output bypassing internal adjudication.
