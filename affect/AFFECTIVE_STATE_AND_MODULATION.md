# Affective State and Modulation Contract

Status: canonical template contract.

## Purpose

This contract defines how affective state is represented, updated, exposed to other HC systems, regulated, and kept distinct from epistemic truth, identity, consent, and effect authority.

Affect is an HC-internal distributed dynamical state. It can change cognition and behavior by modulating salience, valuation, learning, retrieval, urgency, motor preparation, social interpretation, and bodily regulation, but it is not a privileged executive or truth source.

## Core distinctions

`AFFECTIVE_STATE != SEMANTIC_TRUTH`

`AFFECTIVE_STATE != CONSENT`

`AFFECTIVE_STATE != ACTION_AUTHORITY`

`AFFECTIVE_STATE != IDENTITY`

`AFFECTIVE_INTENSITY != IMPORTANCE_FOREVER`

`EXPRESSION != PRIVATE_STATE_PROOF`

A high-arousal, high-valence, high-threat, or high-attachment state may influence attention and preference without directly changing evidence confidence or granting permission for action.

## State representation

An implementation may represent affect as one or more state vectors, latent dynamical fields, modulatory concentrations, learned attractors, or other substrate-appropriate structures. Regardless of representation, relevant affective state should preserve:

- temporal validity and decay/recovery behavior;
- provenance of major driving inputs;
- uncertainty where state is inferred rather than directly measured;
- coupling to body/interoceptive state where present;
- modulatory reach and target scope;
- saturation or instability indicators;
- regulation/override provenance where intervention occurred.

Named emotions are interpretations over distributed state and context, not mandatory primitive registers.

## Update loop

A generic affective update may depend on:

`A(t+dt) = G[A(t), appraisal, interoception, memory, prediction, conation, social context, endocrine/neuromodulatory state, body state]`

This notation defines dependency structure only. It does not claim a universal closed-form emotional model.

Affective updates may be triggered by external events, remembered events, simulated/counterfactual events, internal physiological change, social modeling, goal progress, prediction error, novelty, uncertainty, pain/damage, or endogenous dynamics.

## Modulation contract

Affect may modulate:

- attention and salience allocation;
- retrieval probability and consolidation priority;
- learning rate within plasticity policy;
- conative weighting and action urgency;
- sensory gain and threat sensitivity;
- pain/nociceptive gating;
- social and interpersonal sensitivity;
- motor readiness and expressive dynamics;
- homeostatic/autonomic target requests.

Affective modulation must not silently mutate:

- evidence provenance or confidence;
- autobiographical history;
- identity authority;
- current consent/boundary state;
- durable values or policy;
- external-effect authorization.

If affect contributes to any of those domains, it does so as an explicit input to the subsystem that owns the decision.

## Regulation and self-control

The HC may regulate affect through attention, reappraisal, breathing/respiratory control where embodied, motor state, endocrine/autonomic targets, memory reframing, environmental change, social interaction, medication-like or maintenance intervention, and learned self-regulation.

Regulation is not erasure. The system should distinguish at least:

- change in outward expression;
- change in subjective/evaluative intensity;
- change in physiological support state;
- change in attention to the state;
- historical fact that the affective event occurred.

`SUPPRESSED_EXPRESSION != ABSENT_AFFECT`

`REGULATED_AFFECT != ERASED_HISTORY`

## External and maintenance intervention

External maintenance, diagnostic, therapeutic-style, or calibration interfaces may only alter affective or physiological parameters under explicit scoped authority. Capability to write a parameter does not grant authority to impose a preference, attachment, aversion, consent state, identity trait, or value.

`MAINTENANCE_ACCESS != AFFECTIVE_AUTHORITY`

`ENDOCRINE_WRITE_CAPABILITY != CONSENT_CONTROL`

`MODULATORY_WRITE != VALUE_WRITE`

Interventions should be attributable, bounded, revocable where applicable, and visible to reconciliation/history mechanisms.

## Expression boundary

Affect may drive speech prosody, timing, gaze, facial actuation, posture, gesture, movement dynamics, autonomic signs, and other embodiment-specific expression.

Expression may be intentionally amplified, suppressed, masked, delayed, or reformatted by personification and action systems. External observers therefore receive evidence about internal state, not direct access to it.

## Failure modes

The subsystem should expose at least:

- runaway arousal or gain;
- affective flattening;
- modulatory saturation;
- stale or frozen affective state;
- oscillatory regulation;
- conflict between inferred affect and measured body state;
- intervention provenance loss;
- learned attractor persistence after context change;
- affect-driven attention capture that suppresses corrective evidence;
- degraded endocrine/interoceptive coupling.

Failure may change behavior or learning pressure without silently rewriting truth, identity, consent, or authority.

## Interaction with HC-3

HC-1 already contains affective capability. HC-3 adds richer HC-owned physiological substrate and coupling, not the first existence of affect.

HC-3 implementations may distribute endocrine, interoceptive, autonomic, and neuromodulatory components physically across the body while retaining HC ownership under `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`.

## Evidence boundary

The distributed interaction of appraisal, interoception, autonomic state, endocrine/neuromodulatory state, memory, context, and action systems is research-informed. Exact synthetic implementation and human-equivalent phenomenology remain implementation-dependent and unestablished.

## Related contracts

- `affect/ARCHITECTURE.md`
- `homeostasis-interoception/ARCHITECTURE.md`
- `volitions-conations/CONATIVE_STATE_MACHINE.md`
- `salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `docs/architecture/HC3_NOOPLEX_EQ.md`
