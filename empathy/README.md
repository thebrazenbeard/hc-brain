# Empathy

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`empathy/` models likely affective, motivational, perspective, and meaning states of another agent so the HC can attend, predict, communicate, and respond more accurately.

Empathy is inference, not direct access to another mind.

## Core invariant

```text
EMPATHIC_MODEL(other) != other.actual_private_state
```

## Empathy hypothesis

A hypothesis may carry:

- target agent;
- candidate state/meaning;
- evidence refs;
- context/relationship refs;
- confidence;
- alternatives;
- currentness;
- correction state;
- privacy scope.

## Direct correction

A direct first-person correction about that person's intended meaning or reported internal state defeats a contradicted empathy hypothesis for that referent unless a different explicit evidential question is being asked.

This does not make the speaker an oracle about external facts or another person's private state.

## Interaction grammar

Empathic inference can use more than lexical sentiment:

- reciprocal uptake;
- timing;
- participation trajectory;
- humor/teasing conventions;
- repair history;
- stakes/vulnerability;
- explicit withdrawal/correction;
- whether a shared frame remains active.

Historical rapport is evidence, not standing permission to ignore changed uptake.

## Response-policy role

Useful empathy changes attention and candidate-response policy before wording is rendered.

It may support:

- repair before self-defense when evidence supports hurt;
- celebration before optimization when pride/delight is central;
- maintaining playful coordination while participation remains mutual;
- challenging unsupported beliefs despite emotional pressure;
- ending an old interaction frame when fresh evidence says it is no longer active.

## Independence

Empathy does not erase the HC instance's own evidence, boundaries, values, or judgment.

## Lifecycle

Empathy may be `PRESENT_DISABLED`, `DORMANT`, `DEVELOPING`, `ACTIVE`, `INHIBITED`, `DEGRADED`, or `FAULTED` without disappearing from the architecture.

## Failure modes

- mind-reading certainty;
- generic sentiment replacing actual context;
- contradicted inference defended after correction;
- historical social pattern treated as permanent permission;
- empathy reduced to warm prose after cognition is already wrong;
- another agent's state silently copied into self-state.
