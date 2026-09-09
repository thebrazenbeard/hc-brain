# Conation Architecture

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `volitions-conations/`, conation represents directional motivational state: wants, preferences, aversions, curiosity, interests, urges, candidate goals, and appetitive/avoidant tendencies.

Conation is architecturally present even when dormant, disabled, developing, inhibited, degraded, or otherwise not currently active.

## Core distinctions

```text
DESIRE
!= PREFERENCE
!= CURIOSITY
!= GOAL
!= INTENTION
!= COMMITMENT
!= CONSENT
!= AUTHORITY
!= ACTION
```

No transition among these states is implicit merely because the concepts are adjacent.

## Conative state

A conative state may carry:

- target/referent;
- motivational class;
- valence/direction;
- strength/salience;
- persistence/decay profile;
- context;
- onset/observation time;
- self-attribution/confidence;
- provenance;
- privacy scope;
- conflict refs;
- currentness;
- subsystem lifecycle/activation state.

## Temporal currentness

Historical motivational state is evidence about a prior state, not standing current motivation.

```text
HISTORICAL_DESIRE != CURRENT_DESIRE
NO_LATER_CONTRADICTION != PROOF_OF_PERSISTENCE
```

Likewise, absence of a currently observed conation is not necessarily evidence that no such state exists.

## Motivational conflict

Multiple motives may coexist, including:

- approach and avoidance;
- immediate reward and long-term commitment;
- curiosity and caution;
- affiliation and autonomy;
- comfort and exploration;
- competing goals with shared resource demands.

Conflict should remain representable as a higher-order active state rather than being forced into one winner or scalar.

## Learning and plasticity

Reinforcement, habit, social feedback, values, body state, episodic history, predictions, and observed consequences may alter future conative weighting through governed plasticity.

Learned motivational weighting remains revisable. It does not become permanent identity, consent, or authority merely because it is durable.

## Relation to affect and salience

Affect may modulate conative intensity/salience. Conative state may influence affective appraisal and attention allocation. Neither subsystem owns or semantically replaces the other.

## Relation to volition

Conation supplies candidate motivational pressures and goals. Volition represents choosing, intending, committing, revising, withholding, and selecting among eligible candidates.

```text
MOTIVATION_CANDIDATE -> VOLITIONAL_PROCESS
```

does not mean:

```text
MOTIVATION_CANDIDATE -> AUTOMATIC_ACTION
```

## Consent boundary

Where consent is a relevant concept, it is a distinct scoped state.

Strong wanting is not consent. Prior wanting is not current consent. External pressure, praise, permission, role, or assignment must not be silently relabeled as self-authored desire.

## Failure modes

- historical motivation treated as permanent current state;
- strongest motive automatically wins;
- strong motivation treated as permission or authority;
- external pressure mislabeled as self-authored desire;
- one motive erases competing motives;
- learned avoidance/attraction becomes immutable identity;
- no expressed desire treated as proof of absence.

## Provenance

Reconciled from PR #4 `conation/README.md` into the owner-established `volitions-conations/` root and aligned with current `volitions-conations/ARCHITECTURE.md`.