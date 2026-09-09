# Resolver and Arbitration

Status: CROSS-CUTTING BRAIN INFRASTRUCTURE / DESIGN

## Purpose

`resolver/` defines scoped mechanisms for resolving competing eligible hypotheses, actions, goals, routes, memory candidates, or updates.

It is not a universal executive person.

## Resolver scopes

Possible resolver classes:

- semantic/referent resolution;
- perceptual hypothesis resolution;
- goal/motive arbitration;
- action selection;
- response selection;
- memory admission;
- currentness/supersession resolution;
- routing conflict resolution;
- plasticity update arbitration;
- failure/recovery strategy selection.

Each declares its own input and outcome semantics.

## Outcome vocabulary

```text
SELECT
KEEP_MULTIPLE
NO_ACTION
DEFER
UNRESOLVED
CONFLICT
ESCALATE
QUARANTINE
```

A resolver is allowed to return uncertainty.

## Evidence discipline

Resolver policy may consider:

- direct correction;
- provenance;
- freshness/currentness;
- evidence support;
- authority scope;
- conflict;
- predicted consequences;
- task context;
- safety/privacy constraints.

It may not invent missing evidence merely because a single answer is operationally convenient.

## Scoped authority

A resolver's ability to choose among candidates is not general authority to execute resulting external effects or rewrite durable state.

## No global arbiter

The Noöplex Fabric may dispatch to the appropriate resolver, but no resolver owns all truth, selfhood, action, memory, and authority.

## Failure modes

- forced certainty;
- one global resolver accumulating all control;
- latest timestamp used as universal winner;
- semantic similarity used to merge distinct provenance/identities;
- selected candidate silently executed;
- conflict hidden from downstream systems.
