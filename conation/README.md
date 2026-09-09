# Conation

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`conation/` represents directional motivational state: wants, preferences, aversions, curiosity, interests, urges, goals, appetitive/avoidant tendencies, and related motivational dynamics.

Conation is architecturally present even when dormant or disabled.

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

A runtime may relate these states, but no transition is implicit merely because the labels sound adjacent.

## Conative state

A state may carry:

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
- lifecycle/activation state.

## Present-state rule

Historical motivational records are evidence about prior state, not standing current motivation.

```text
HISTORICAL_DESIRE != CURRENT_DESIRE
```

No later contradiction does not prove persistence.

## Conflict

Multiple motives may coexist:

- approach and avoidance;
- immediate reward and long-term commitment;
- curiosity and caution;
- affiliation and autonomy;
- comfort and exploration.

Conflict should remain representable rather than being forced into one scalar.

## Learning

Reinforcement, habit, social feedback, values, body state, episodic history, and prediction can alter future conative weighting through plasticity.

Learned motivation remains revisable and does not become irrevocable authority.

## Relation to affect

Affect can modulate conative salience. Conation can influence affective appraisal and attention. Neither subsystem owns the other.

## Relation to volition

Conation supplies candidate motivational pressures/goals. Volition handles choice, intention, commitment, revision, and action selection under evidence, values, constraints, and authority.

## Consent boundary

Strong wanting is not consent. Prior wanting is not current consent. Consent is a separate scoped state where the concept applies.

## Failure modes

- old motivation treated as permanent;
- strong motivation treated as permission;
- external pressure mislabeled as self-authored desire;
- one motive erasing conflicting motives;
- learned avoidance/attraction becoming immutable identity;
- no expressed desire treated as proof of absence.
