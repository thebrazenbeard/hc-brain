# Affective State and Modulation Contract

Status: template architecture.

## Purpose

This contract defines affect as a distributed, multidimensional evaluative state that can shape salience, learning, memory access, action weighting, social interpretation, body regulation, and expression without becoming a truth source, identity store, consent mechanism, or unrestricted executive controller.

Affect is not one scalar mood, one named emotion, one hormone, or one dedicated node.

## Core separations

`AFFECTIVE_STATE != SEMANTIC_TRUTH`

`AFFECTIVE_STATE != IDENTITY`

`AFFECTIVE_STATE != CONSENT`

`AFFECTIVE_STATE != ACTION_AUTHORIZATION`

`MODULATORY_STATE != EMOTION_LABEL`

`EMOTION_LABEL != RAW_INTEROCEPTION`

`WANTING != LIKING`

`DESIRE != COMMITMENT`

`AROUSAL != INTENT`

## Affective state vector

The HC should support simultaneous, potentially conflicting dimensions rather than force one global mood.

Candidate dimensions include:

- valence;
- arousal/activation;
- threat estimate;
- safety estimate;
- novelty;
- uncertainty;
- pain burden;
- fatigue/energy pressure;
- attachment/social salience;
- reward expectation;
- hedonic response;
- incentive salience/wanting;
- action readiness;
- approach/avoidance pressure;
- motivational conflict;
- domain-specific salience such as sexual relevance where applicable.

Not every implementation must use these exact dimensions, but the architecture must permit mixed state.

Examples that must remain representable include:

- positive valence with low activation;
- negative valence with strong approach motivation;
- strong desire with explicit inhibition;
- high sexual relevance with low action intention;
- high uncertainty with high curiosity;
- pain with low threat;
- fear-like appraisal with preserved epistemic uncertainty.

## AffectiveAppraisal

An affective appraisal is an interpretation of what a situation means for the organism's goals, safety, body state, social state, expectations, or learned values.

Conceptual fields may include:

- triggering evidence/state references;
- affected concern/goal/value references;
- appraisal dimensions;
- context;
- confidence;
- competing appraisals;
- chronology/currentness;
- provenance.

Appraisal remains revisable. A later interpretation may supersede an earlier appraisal without rewriting the historical event that triggered it.

## Named emotion hypotheses

Named emotions are higher-order interpretations over affective dimensions plus context, memory, self-model, social state, and embodiment.

The HC may represent candidates such as anger, fear, affection, shame, excitement, grief, or other learned categories, but those labels are not privileged primitive truths.

`NAMED_EMOTION = INTERPRETATION_OVER_STATE`

Different cultures, learned concepts, languages, or individual development may partition similar underlying state differently.

## ModulationField

Neuromodulatory/endocrine-like state should act as a typed target-specific control field rather than a semantic payload.

Conceptual fields may include:

- signal/modulator class;
- source;
- target scope;
- effect class;
- parameter/gain change;
- onset;
- decay/clearance;
- saturation;
- eligibility context;
- feedback state;
- provenance.

Candidate effect classes include:

- processing gain;
- signal-to-noise bias;
- salience bias;
- attention bias;
- learning rate;
- plasticity eligibility;
- routing bias;
- action urgency;
- consolidation priority;
- pain/homeostatic gain;
- social sensitivity.

The same modulator may have different effects in different target scopes.

## Modulation is not evidence

Affective or modulatory state may alter which evidence receives attention, how quickly learning occurs, or how strongly a candidate action is weighted.

It must not directly raise the truth confidence of a proposition because the proposition is desirable, threatening, comforting, or emotionally congruent.

`AFFECT/CONATION -> INFORMATION_SEEKING_OR_WEIGHTING`

`AFFECT/CONATION -X-> DIRECT_EPISTEMIC_CONFIDENCE`

## Interaction with interoception/homeostasis

The relationship is recurrent:

`interoceptive evidence -> physiological estimate -> appraisal -> affective update -> modulation/regulatory change -> altered body state -> new interoceptive evidence`

This loop is intentionally circular but provenance-bearing. Each stage remains distinguishable.

Affect can propose or bias regulatory changes within allowed ranges but does not silently rewrite protected physiological targets.

## Interaction with conation

Affect can supply urgency, valence, incentive salience, effort willingness, and avoidance/approach pressure to conative systems.

Conation owns directional concern/intention state. Affect does not automatically create commitment.

Strong affect remains compatible with:

- no intention;
- delayed action;
- redirection;
- inhibition;
- explicit decline;
- authorization `UNKNOWN`.

## Expression boundary

Where embodiment supports expression, affective state may influence prosody, timing, gaze, posture, gesture, facial actuation, movement energy, and other presentation channels.

Personification and social/pragmatic systems may regulate how much of an affective state is outwardly expressed.

`DISPLAY_REGULATION != STATE_ERASURE`

Suppressing or altering expression does not retroactively delete the triggering evidence, appraisal, body state, or memory.

## Persistent affective state

A themed response, route, prompt, or one-time output style is not enough to establish durable affect.

Where persistent affective state is claimed, the implementation should expose at least:

- exact state identity;
- triggering/update evidence;
- substrate-appropriate state verification or estimation evidence;
- currentness and supersession;
- decay/reset/reversibility semantics;
- causal effect on eligible processing;
- negative-transfer containment;
- provenance.

Direct state readback is one valid verification method where the substrate exposes meaningful addressable state. It is not universally available or sufficient for a distributed, biohybrid, reconstructed, or estimator-based affective state. Other methods may include declared state estimation, intervention/causal probes, reconstruction from distributed state, or bounded behavioral/control signatures with an explicit claim ceiling.

`STATE_VERIFICATION_EVIDENCE != DIRECT_READBACK_ONLY`

## Metaplasticity and saturation

Affective/modulatory state may temporarily change how easy the system is to modify without altering learned content itself.

Plasticity-related fields may include:

- current learning rate;
- plasticity threshold;
- recent update load;
- eligibility trace;
- stability margin;
- cooldown/refractory state.

No affective intensity should grant unbounded durable-write authority.

## Failure controls

The subsystem should detect or constrain:

- one-scalar mood collapse;
- hormone/emotion lookup tables presented as ground truth;
- affective preference leaking into epistemic confidence;
- strong desire leaking into consent/authority;
- modulation saturating without bounded recovery;
- stale affective state treated as current;
- display suppression being mistaken for absence of affect;
- social or sexual salience transferring to the wrong referent;
- external affect classifier becoming authoritative over internal state;
- persistent affect claims based only on themed output.

## Evidence boundary

This contract generalizes current HC affect, conation, sexuality, homeostasis/interoception, and neuromodulation research. It specifies a reusable state/control architecture and does not claim human-equivalent phenomenology, a particular endocrine chemistry, or implementation proof.