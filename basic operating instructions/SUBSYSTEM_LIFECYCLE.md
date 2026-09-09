# Subsystem Lifecycle

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: narrowed from PR #4 `contracts/SUBSYSTEM_LIFECYCLE.md` after deduplication against canonical `CAPABILITY_ACTIVATION_STATES.md` and `RUNTIME_INVARIANTS.md`.

## Purpose

This focused contract adds lifecycle behavior that is not captured by presence/activation labels alone.

Canonical axes remain independent:

```text
PRESENCE != ACTIVATION != DEVELOPMENT != HEALTH != AUTHORIZATION
```

A lifecycle projection may summarize those axes, but must not erase them.

## Typical lifecycle labels

```text
PRESENT_DISABLED
DORMANT
DEVELOPING
ACTIVE
INHIBITED
DEGRADED
FAULTED
RECOVERING
```

These are operational summaries, not evidence of architectural absence/presence by themselves.

## Inactive-learning policy

Whether an inactive capability learns is independent from whether it executes.

```text
NO_LEARNING
OBSERVE_ONLY
SHADOW_LEARNING
BOUNDED_DEVELOPMENT
FULL_LEARNING
```

Every first-class subsystem that can learn while non-active should declare this policy explicitly.

`DISABLED` must not silently mean either `FROZEN` or `FULL_BACKGROUND_LEARNING`.

## Fault/recovery semantics

A degraded/faulted capability should declare:

- affected capabilities;
- safe degradation mode;
- whether alternate routes exist;
- trust status of durable state produced before/after fault;
- whether active coalitions must reconfigure/terminate;
- recovery prerequisites;
- recalibration/requalification requirements where relevant.

Recovery should be a transition supported by health/evidence, not a label changed because the component became reachable again.

## Developmental transitions

A common path is:

```text
PRESENT_DISABLED
→ DORMANT
→ DEVELOPING
→ ACTIVE
```

but development, activation, and health may move independently. A mature capability can be dormant; an immature capability can be actively calibrating; an active capability can be degraded.

## Activation versus authorization

Some capabilities may activate autonomously under context; others may require developmental, privacy, safety, or configuration gates. The capability contract declares that policy.

```text
ACTIVE != AUTHORIZED_FOR_ANY_EFFECT
```

## Completeness rule

A capability should not be omitted from the generic HC template merely because initial hardware does not expose it, the first use case does not need it, it is intentionally disabled, or implementation is not yet mature. If it is a first-class synthetic-cognitive capacity, define its architectural home and mark realization state truthfully.
