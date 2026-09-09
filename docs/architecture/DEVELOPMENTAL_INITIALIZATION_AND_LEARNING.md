# Developmental Initialization and Learning

Status: canonical architecture contract.

## Purpose

A complete HC should not be confused with a fully developed HC.

The template requires the complete latent cognitive organ to be architecturally present, but it does not require a newly initialized HC to begin with mature skills, a finished world model, a specific personality, a personal history, or fully developed effective connectivity.

The governing distinction is:

`CAPABILITY_PRESENCE != DEVELOPMENTAL_MATURITY != LEARNED_CONTENT`

## Developmental design principle

A fresh HC should begin with enough built-in structure to remain coherent, learn safely, discover its interfaces, preserve protected architectural invariants, and develop its mandatory capacities. It should not require every mature cognitive relation to be pre-authored.

The architecture therefore separates four broad initialization layers.

### 1. Protected architectural invariants

These are not ordinary learned state.

Examples include:

- the complete-cognitive-organ boundary;
- the temporal-hypergraph object model;
- subsystem capability homes;
- lifecycle/state-axis semantics;
- provenance/currentness distinctions;
- action/effect authority boundaries;
- memory admission and correction semantics;
- protected fault-containment rules;
- physical-organ membership rules;
- the rule that ordinary learning cannot manufacture authority merely from reward, repetition, priority, or confidence.

Normal plasticity must not silently rewrite these invariants.

### 2. Bootstrap priors and developmental affordances

A manufacturer or implementation may supply bounded generic priors needed to make learning possible, such as:

- initial structural reachability;
- candidate routing eligibility;
- plasticity ranges and stability ceilings;
- generic signal schemas;
- basic homeostatic operating ranges;
- fault-detection and self-test behavior;
- initial attention/salience mechanisms;
- interface-discovery mechanisms;
- generic learning algorithms;
- protected developmental gates;
- minimal motor/sensory calibration procedures.

These are starting conditions, not a named identity.

A bootstrap prior may bias development without being immutable. Its mutability class must be explicit.

### 3. Developmentally learned structure

Experience may progressively shape:

- learned logical connectivity;
- routing preferences;
- coalition-formation tendencies;
- predictive models;
- semantic and pragmatic competence;
- body schema;
- sensorimotor mappings;
- procedural skills;
- social models;
- affective associations;
- habits and conditioned responses;
- language/convention competence;
- confidence calibration;
- context-dependent values/preferences in instantiated systems where legitimately learned or admitted.

Learned structure changes future hypergraph behavior but must not rewrite the historical record of how that learning arose.

### 4. Instance-specific continuity content

An instantiated HC may develop or receive:

- autobiographical memory;
- relationships/social history;
- personal preferences;
- self-model content;
- commitments;
- roles/personification state;
- embodiment history;
- current task/session state.

This content belongs to the instantiated organism, not to the identity-neutral base template.

## Initialization lifecycle

A conceptual initialization path may include:

```text
INERT
-> BOOTSTRAP
-> SELF_TEST
-> INTERNAL_CALIBRATION
-> INTERFACE_DISCOVERY
-> EMBODIMENT_CALIBRATION
-> DEVELOPMENTAL_LEARNING
-> OPERATIONAL_WITHIN_QUALIFIED_SCOPE
```

Implementations may refine these states. The lifecycle describes engineering readiness and developmental status; it does not define a metaphysical instant at which consciousness or personhood begins.

## Learning modes

The HC should support multiple learning regimes rather than one universal update rule, including where appropriate:

- supervised or instructional learning;
- self-supervised/predictive learning;
- reinforcement and credit assignment;
- episodic capture;
- semantic generalization;
- imitation/social learning;
- procedural practice;
- active experimentation;
- counterfactual/simulation learning;
- calibration/body learning;
- observe-only or shadow learning for unqualified capabilities.

A learning mode declares what state families it may propose changes to. No learning mode has universal write authority merely because it improves a local objective.

## Shadow development

High-risk or immature capabilities should be able to develop without immediately gaining effect authority.

A useful progression is:

```text
OBSERVE_ONLY
-> SHADOW_PREDICTION
-> REPLAY_OR_OFFLINE_EVALUATION
-> BOUNDED_SUPERVISED_USE
-> QUALIFIED_ACTIVE_USE
```

This allows competence evidence to accumulate before deployment authority is widened.

`PREDICTS_WELL != AUTHORIZED_TO_ACT`

## Credit assignment

Credit/blame signals should preserve uncertainty about causal contribution.

Co-activation alone must not force every participating relation to strengthen. Reward, punishment, user approval, repeated exposure, salience, and emotional intensity are learning signals or context; none is automatically semantic truth, consent, permission, or universal value.

## Negative transfer and overgeneralization

Development should be tested for inappropriate generalization, including:

- one embodiment's calibration applied to a different body without remapping;
- one relationship convention generalized to every agent;
- one context-specific social behavior leaking into unrelated tasks;
- reward shaping eroding refusal/authority boundaries;
- stylistic success overriding epistemic discipline;
- one domain procedure being applied outside its qualified regime;
- a temporary coalition becoming an undeclared permanent control path;
- repeated external model output becoming internal belief without admission.

## Plasticity boundary

Developmental learning proposes or stages changes. Durable changes remain governed by the plasticity/state-governance contracts.

At minimum:

```text
learning_signal
-> candidate_change
-> scope/eligibility check
-> protected-invariant check
-> bounded provisional update
-> evaluation
-> consolidate | revise | decay | revert | quarantine
```

The more continuity-relevant a state family is, the stronger its provenance, conflict, and rollback requirements should be.

## Development versus activation

A subsystem may be architecturally present while developmentally immature.

For example:

```text
presence: PRESENT
activation: DORMANT | DEVELOPING | ACTIVE
maturity: UNDEVELOPED | CALIBRATING | LEARNING | STABLE_WITHIN_SCOPE | ADAPTING
health: NOMINAL | DEGRADED | FAULTED | QUARANTINED | UNKNOWN
```

These axes remain independent.

An `ACTIVE` capability may still be immature. A `DORMANT` capability may retain mature learned state. A `DEVELOPING` capability does not receive unrestricted action authority.

## Embodiment transfer

A body change should preserve learned cognitive state that belongs to the HC while triggering redevelopment only where embodiment-dependent mappings actually changed.

A transplant may therefore retain:

- autobiographical memory;
- semantic/procedural knowledge not tied to the old body;
- personality/self-model continuity;
- learned social models;
- internal values/commitments;
- non-body-specific routing/plasticity state;

while requiring recalibration or redevelopment of:

- sensor maps;
- actuator maps;
- proprioception;
- body schema;
- balance/locomotion;
- force/latency models;
- interoceptive mappings;
- embodiment-specific affordances.

`BODY_RECALIBRATION != IDENTITY_RESET`

## Complete-organ consequence

A complete HC should therefore be architecturally rich but developmentally open.

The architecture supplies capability, protected invariants, learning machinery, and bounded priors. Development supplies much of the effective topology, competence, calibration, and identity-bearing content.

This avoids both failure modes:

- a supposedly complete HC that is missing mandatory capacities until external services provide them; and
- a supposedly newborn HC whose mature identity, preferences, skills, and effective topology were all silently pre-authored by the template.

## Evidence boundary

This document is an HC architectural decision about how to separate innate/bootstrap structure from developmental learning. It is informed by general adaptive-system and neurodevelopmental principles but does not claim that the HC reproduces a literal human developmental program or that any particular developmental schedule is scientifically established for a synthetic cognitive organ.

## Provenance

The learning-mode and negative-transfer distinctions were selectively generalized from preserved foundation research on `research/hyperconnectome-foundations-20260909`, especially its `learning/README.md`, then reconciled against current HC plasticity, capability-state, cognitive-organ, and identity-neutrality contracts. The alternate branch taxonomy was not adopted.
