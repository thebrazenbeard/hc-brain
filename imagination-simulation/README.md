# Imagination and Simulation

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`imagination-simulation/` constructs internally generated hypothetical scenes, plans, counterfactuals, rehearsals, creative combinations, and possible futures for reasoning, planning, learning, creativity, and social prediction.

Simulated content is not observation or autobiographical history.

## Core invariant

```text
SIMULATED != OBSERVED != REMEMBERED_AS_LIVED
```

## Simulation object

May carry:

- scenario ID;
- generating goal/question;
- assumed initial state;
- imported world/self/social model refs;
- hypothetical modifications;
- generated sequence/outcomes;
- uncertainty;
- model/version;
- purpose: planning / creativity / rehearsal / prediction / empathy / testing;
- clear `SIMULATED` provenance.

## Counterfactual reasoning

The subsystem should support "what if" manipulation while preserving which premises differ from current believed state.

## Planning and rehearsal

Action plans can be rehearsed internally to estimate consequences, resource needs, body constraints, or social outcomes before any external effect is authorized.

## Creativity

Novel combinations may be generated without requiring that every component be copied from prior episodes. Generated artifacts remain attributed as generated/synthetic until independently observed or adopted.

## Social imagination

The HC may simulate how another agent might react, but these remain empathy/social hypotheses rather than claims about hidden private state.

## Memory interaction

Simulation may retrieve episodes/semantic knowledge, but resulting synthetic scenes must not be written back as lived episodes.

## Failure modes

- imagined event stored as actual history;
- counterfactual assumption silently promoted to current fact;
- simulated social response treated as mind-reading certainty;
- rehearsal treated as procedural qualification;
- generated preference/identity content silently adopted as self-state;
- external generative model output losing its synthetic provenance.
