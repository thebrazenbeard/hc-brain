# Imagination and Simulation

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `cognition/`, imagination and simulation construct internally generated hypothetical scenes, plans, counterfactuals, rehearsals, creative combinations, and possible futures for reasoning, planning, learning, creativity, and social prediction.

Simulated content is not observation or autobiographical history.

## Core invariant

```text
SIMULATED != OBSERVED != REMEMBERED_AS_LIVED
```

## Simulation object

A simulation may carry:

- scenario ID;
- generating goal/question;
- assumed initial state;
- world/self/social-model references;
- hypothetical modifications;
- generated sequence/outcomes;
- uncertainty;
- model/version;
- purpose: planning / creativity / rehearsal / prediction / empathy / testing;
- explicit `SIMULATED` provenance;
- temporal horizon and termination condition.

## Counterfactual reasoning

The HC should support “what if” manipulation while preserving which premises differ from current believed state.

A counterfactual branch must not silently rewrite the active world model merely because it is useful to reason through.

## Planning and rehearsal

Action plans may be rehearsed internally to estimate consequences, resource needs, body constraints, or social outcomes before any external effect is authorized.

Rehearsal can inform an action candidate. It is not external execution and is not procedural qualification by itself.

## Creativity

Novel combinations may be generated without requiring that every complete artifact have appeared in prior episodic memory. Generated artifacts remain attributed as generated/synthetic until independently observed, adopted, or otherwise admitted under the relevant state contract.

## Social imagination

The HC may simulate how another agent might react, but these remain empathy/social hypotheses rather than claims about hidden private state.

## Memory interaction

Simulation may retrieve episodic or semantic knowledge, but resulting synthetic scenes must not be written back as lived episodes.

If a simulation is itself worth remembering, memory should preserve that **the simulation occurred**, not falsely record the simulated event as external history.

## Temporal-hypergraph role

A simulation may instantiate a temporary internal coalition with world-model state, current memory, semantics, affect, social cognition, self-model, kinesis planning, or other relevant systems. Its hypothetical state remains scoped to that simulation unless separately admitted elsewhere.

## Failure modes

- imagined event stored as actual history;
- counterfactual assumption silently promoted to current fact;
- simulated social response treated as mind-reading certainty;
- rehearsal treated as procedural qualification;
- generated preference/identity content silently adopted as self-state;
- external generative-model output loses synthetic provenance;
- simulated success is treated as verified real-world effect.

## Provenance

Reconciled from PR #4 `imagination-simulation/README.md` into the canonical `cognition/` root.