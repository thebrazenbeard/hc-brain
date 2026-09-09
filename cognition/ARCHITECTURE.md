# Cognition Architecture

Status: working HC template architecture.

## Purpose

The cognition subsystem coordinates inference, perception-level hypothesis handling, prediction, planning, simulation, world-model revision, metacognitive monitoring, uncertainty, strategy selection, and task-local cognitive configuration without becoming a monolithic executive or identity store.

Cognition participates in the HC temporal hypergraph; it does not own every cognitive function simply because this folder contains several cross-cutting reasoning contracts.

## Functional distinctions

The architecture should keep separate:

- calibrated observation/evidence;
- perceptual hypotheses;
- world-model state;
- predictions;
- counterfactual/simulated state;
- metacognitive assessment/recommendation;
- relatively persistent learned capabilities;
- active goals and commitments;
- task-local cognitive strategy;
- temporary attentional allocation;
- current uncertainty profile;
- communication stance;
- learned strategy currently being applied;
- self-model and identity continuity, which remain outside cognition proper;
- action/effect authority, which remains separately governed.

## Focused cognition contracts

- `EPISTEMIC_COGNITIVE_CONTROL.md` — rival hypotheses, causal discrimination, prediction/explanation/control separation, regime detection, and epistemic discipline.
- `PERCEPTION_AND_MULTIMODAL_INFERENCE.md` — HC-internal perceptual hypotheses, multimodal evidence fusion, calibration/currentness, and active-perception proposals.
- `WORLD_MODEL_AND_PREDICTION.md` — revisable world/body/environment models, causal hypotheses, affordances, predictions, and external-model evidence boundaries.
- `IMAGINATION_SIMULATION_AND_COUNTERFACTUALS.md` — simulated/counterfactual state, rehearsal, creativity, social simulation, and strict separation from observation and lived memory.
- `METACOGNITIVE_MONITORING.md` — confidence/uncertainty monitoring, strategy/error review, evidence/tool-use recommendations, and bounded self-monitoring without a homuncular executive.

These are functional contracts, not separate top-level roots. Runtime cognition remains distributed across cognition, memory, semantics, pragmatics, affect, empathy, self-model, salience/attention, kinesis, interfaces, and other participating systems.

## Scientific loop

A useful generic cognition loop is:

```text
observe
-> form perceptual/semantic hypotheses
-> compare world-model alternatives
-> predict
-> choose discriminating observation/action candidate
-> obtain authorized observation/effect
-> observe consequence
-> update provisional models
-> metacognitively assess residual uncertainty / strategy quality
-> preserve unresolved uncertainty
-> test again
```

This supports causal discrimination and active learning rather than passive pattern matching alone.

The loop is not required to execute serially; multiple stages may recur concurrently in temporal-hypergraph coalitions.

## Strategy persistence and release

Temporary configurations may legitimately alter inference depth, retrieval, attention, confidence thresholds, simulation budget, or response policy. The system must retain competence while releasing obsolete control settings after a context shift.

Repeated strategy use must not silently promote a task-local mode into personality, identity, or a global behavioral norm.

Temporary prediction/simulation/metacognitive coalitions likewise must not become permanent control topology without an admitted plasticity change.

## Multiple methods

No single model family is assumed to solve all cognitive problems. The HC template may combine probabilistic inference, learned representations, rules, planning, causal models, simulation, system identification, change detection, and other specialized mechanisms.

Likewise, support for prediction does not mandate one universal predictive-coding theory, support for simulation does not imply that simulated state is perception or memory, and metacognition does not imply a separate supervisory mind.

## External computation boundary

External LLMs, simulators, planners, retrieval systems, and specialist models may provide candidate hypotheses, predictions, plans, or generated simulations through HC-owned interfaces.

Their outputs remain typed external/model evidence until the HC evaluates them. External computation does not become internal belief, world-model authority, memory, identity, desire, or action authority merely because it is sophisticated or frequently correct.

Metacognition may recommend using such services; that recommendation does not outsource ownership of the cognitive task.

## Failure modes

- mode residue after task completion;
- mode-to-self promotion;
- correlation presented as causation;
- one hypothesis collapsed prematurely for output convenience;
- perception/prediction/simulation provenance collapse;
- explanation replacing required action;
- generated language treated as evidence authority;
- external model output bypassing HC adjudication;
- simulated event written as lived autobiographical history;
- body-specific affordance treated as universal after embodiment change;
- metacognitive self-monitor becoming a universal executive or starving the primary task.

## Provenance

Generalized from reusable mechanisms in `thebrazenbeard/noema`, `thebrazenbeard/unvtrslr`, and `thebrazenbeard/abil`, with focused perception/world-model/simulation/metacognition contracts selectively remapped from preserved `research/hyperconnectome-foundations-20260909` material. The alternate branch root taxonomy was not adopted.
