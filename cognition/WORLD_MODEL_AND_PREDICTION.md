# World Model and Prediction

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `cognition/`, world modeling maintains revisable models of external and internal environments, entities, causal relations, affordances, dynamics, and expected consequences.

Prediction is a supported cognitive capability, not a requirement that every HC process conform to one predictive-coding theory.

## Model contents

A world-model representation may include:

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
- alternate competing models.

## Predictions

A prediction should be able to declare:

- model/hypothesis source;
- target variable/event;
- expected range/distribution;
- time horizon;
- conditions/assumptions;
- confidence/uncertainty;
- discriminating observations or interventions.

## Revision

```text
prior model
+ observation/evidence
+ prediction error / incompatibility
→ compare alternatives
→ revise | split | retain | reject | keep unresolved
```

Prediction error is evidence that a model or assumption needs review. It is not automatic proof of one replacement model.

## Temporal-hypergraph role

World-model state may be distributed across several HC systems and temporarily assembled into a task-specific coalition. The architecture does not require one monolithic world-model node.

Models and predictions must carry temporal scope so stale state is not silently treated as the current world.

## Counterfactuals and simulation

World-model components may participate in hypothetical simulation for planning and reasoning without converting simulated state into historical memory or asserted observation.

```text
SIMULATED != OBSERVED
PREDICTED != OCCURRED
```

## Affordances and embodiment

Affordances are body-relative and context-relative. A different embodiment can therefore change available actions and calibration without requiring a different generic HC cognitive architecture.

## External models

An external simulator, LLM, specialist model, or other computational peripheral may propose predictions through an HC-owned interface. Internal HC cognition remains responsible for evidence classification, integration, currentness, arbitration, memory admission, and action selection.

## Failure modes

- prediction presented as observation;
- one model treated as mandatory without discriminating evidence;
- body-specific affordance is universalized;
- simulated event is written as lived episode;
- stale world state is treated as current;
- external model output bypasses HC-internal adjudication;
- prediction error is treated as proof of a preferred alternate explanation.

## Provenance

Reconciled from PR #4 `world-model/README.md` into the canonical `cognition/` root.