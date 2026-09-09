# Affect Architecture

Status: template architecture / research-informed

## Purpose

The affect subsystem represents distributed evaluative state that influences salience, motivation, learning, action selection, social interpretation, memory access, bodily regulation, and outward expression.

Affect is not a lookup table from one chemical signal to one named emotion. It is an emergent system-level state produced by interaction among appraisal, interoception, memory, prediction, context, neuromodulation, endocrine/autonomic state, and learned expectations.

## Core state

The template should support a multidimensional affective state rather than hard-coded one-to-one emotion chemistry. Useful dimensions include:

- arousal;
- valence;
- threat estimate;
- safety estimate;
- attachment/social salience;
- novelty;
- uncertainty;
- fatigue and energy reserve;
- pain burden;
- motivational drive;
- reward expectation;
- action readiness.

Named emotions are higher-order interpretations over these variables plus context, memory, self-model, and social state.

## Closed loop

Affect participates in a recurrent loop:

`external input -> appraisal -> affective update -> autonomic/endocrine modulation -> body-state change -> interoception -> revised appraisal`

Memory and expectation participate throughout. The loop is intentionally circular: affect alters the body and cognition, and those changes become new evidence for subsequent affective state.

## Modulation, not truth authority

Affective and neuromodulatory state may change:

- attention and salience;
- learning rate;
- retrieval bias;
- urgency;
- action weighting;
- pain gating;
- social sensitivity;
- consolidation priority.

It does not independently establish semantic truth, durable memory admission, identity change, or action authority.

## Expression interface

Outward expression should, where an embodiment supports it, be driven from the same affective state used internally. Candidate outputs include vocal prosody, timing, gaze, facial actuation, posture, gesture amplitude, respiration, and other embodiment-specific channels.

Expression may be voluntarily regulated, but the template should distinguish regulation of display/intensity from erasure of the underlying event, appraisal, or memory.

## Interaction with other HC subsystems

Primary interfaces:

- `homeostasis-interoception` supplies internal-body evidence;
- `salience-attention` weights what receives processing resources;
- `current memory storage` supplies live contextual state;
- `deep memory storage` supplies learned associations and prior episodes;
- `Empathy` and `sociological behaviors` supply social appraisal context;
- `sexuality` supplies domain-specific motivational and relational state;
- `integration-arbitration` receives affect as one input among many rather than as a master override;
- `routing instructions with neuroplasticity` may use modulatory state to gate eligible learning updates.

## Evidence boundary

DOCUMENTED: contemporary neuroscience supports distributed interactions among neural appraisal, autonomic physiology, interoception, endocrine regulation, neuromodulation, memory, and context in emotion.

INFERRED TEMPLATE RULE: HC affect should therefore be modeled as a distributed control and appraisal system rather than as a single dedicated emotion node or hormone table.

UNKNOWN / IMPLEMENTATION-DEPENDENT: exact synthetic mechanisms, substrate realization, and whether any implementation reproduces human-like subjective emotional phenomenology.

## Provenance

Generalized from research on the `research/nooplex-hc3-architecture-v1` branch, especially `research/2026-09-09/AFFECT_INTEROCEPTION_ENDOCRINE.md`, with identity- and setting-specific material removed.