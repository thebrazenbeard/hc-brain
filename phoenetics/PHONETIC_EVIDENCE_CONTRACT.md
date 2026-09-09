# Phonetic Evidence Contract

Status: canonical focused subsystem contract.

## Purpose

This contract defines the typed evidence objects and boundaries used by `phoenetics` when representing speech-like acoustic form, prosody, timing, and phonetic/phonological candidates.

The folder name `phoenetics` is retained as the canonical repository spelling.

## Core distinctions

`ACOUSTIC_EVENT != PHONETIC_UNIT`

`PHONETIC_UNIT != LEXICAL_TOKEN`

`LEXICAL_TOKEN != SEMANTIC_INTERPRETATION`

`PROSODY != INTENT`

`SPEAKER_CHARACTERISTIC != SPEAKER_IDENTITY_CERTAINTY`

`PHONETIC_PLAN != AUTHORIZED_SPEECH_EFFECT`

## Input boundary

Physical microphones, vibration sensors, bone-conduction sensors, contact sensors, or other acoustic transducers are body/peripheral hardware unless a specific implementation classifies them otherwise.

`adaptable I-O handler` owns admission, capability registration, calibration, units, timing quality, and channel health.

`phoenetics` consumes calibrated acoustic/signal evidence and produces HC-internal form hypotheses.

It must not silently invent sensor certainty that the interface layer did not provide.

## Phonetic evidence object

A generic representation should be able to carry:

```text
PHONETIC_EVIDENCE {
  evidence_id
  source_channel_refs[]
  observation_interval
  raw_or_feature_refs[]
  segmentation_hypothesis
  phonetic_candidates[]
  phonological_candidates[]
  prosodic_features
  timing_rhythm_pause_features
  speaker_channel_features
  language_or_code_hypotheses[]
  confidence
  alternatives[]
  calibration_state
  source_quality
  provenance
  currentness
}
```

No field implies final lexical, semantic, pragmatic, social, or identity adjudication.

## Segmentation

Continuous acoustic input may admit multiple valid segmentation hypotheses.

The subsystem should support:

- uncertain onset/offset boundaries;
- overlapping speakers or sources;
- coarticulation;
- reduced/merged forms;
- non-speech vocalizations;
- silence as potentially meaningful timing evidence;
- interruptions and truncation;
- rhythmically or temporally encoded structure;
- code-switching or unknown linguistic system.

A convenient word-like boundary must not be promoted into observation fact merely because downstream recognition prefers discrete tokens.

## Phonetic and phonological hypotheses

The subsystem may generate candidate phones, phonemes, syllable-like structures, stress patterns, tone categories, or other form units where a language/code model supports them.

It must preserve which layer produced which claim:

```text
measured acoustic evidence
-> derived acoustic features
-> phonetic hypothesis
-> phonological hypothesis
-> lexical hypothesis (speech recognition)
```

Each transformation may add uncertainty and model dependence.

## Prosody

Prosodic representation may include:

- pitch contour;
- intensity contour;
- duration;
- speech rate;
- stress/accent candidates;
- rhythm;
- pause placement;
- turn-taking timing;
- voice quality features;
- hesitation/disfluency markers.

Prosody may inform pragmatic, affective, social, or speaker-model hypotheses, but does not itself establish them.

For example, a falling pitch contour may support a candidate interpretation in context; it does not prove certainty, dominance, anger, sarcasm, or finality by itself.

## Speaker/channel representation

The subsystem may represent acoustic characteristics useful for adaptation or source separation, including channel response, habitual articulation, pitch range, timing tendencies, or other voice features.

Those features are evidence for downstream speaker hypotheses, not an identity credential.

Voice similarity must not become identity certainty without appropriate corroboration.

## Language and accent adaptation

Phonetic interpretation may adapt to:

- accent/dialect;
- articulation differences;
- speech impairment or unusual motor realization;
- developmental stage;
- synthetic/nonhuman vocal apparatus;
- channel distortion;
- learned vocabulary/phonotactics;
- code-switching;
- newly learned communication systems.

Adaptation changes the model used to interpret signal form; it does not rewrite what was physically observed.

Historical evidence should preserve enough provenance to distinguish later reinterpretation from original measurement.

## Outgoing form boundary

For speech production, `phoenetics` may help represent a selected utterance's phonetic/phonological realization target and prosodic constraints.

Conceptually:

```text
selected linguistic content
-> phonological/phonetic realization candidate
-> speech synthesis/articulation plan
-> action/effect authorization
-> emitted acoustic effect
```

`phoenetics` does not independently choose social content, consent state, communicative intent, or whether an utterance is authorized to be emitted.

## Prediction and self-monitoring

The subsystem may participate in speech self-monitoring by comparing:

- intended phonetic/prosodic realization;
- predicted acoustic consequence;
- observed or estimated emitted signal;
- mismatch/error.

Predicted output and observed output must remain distinguishable.

`PREDICTED_ACOUSTIC_FORM != OBSERVED_ACOUSTIC_FORM`

Mismatch may create calibration, motor-learning, synthesis, or interface-repair candidates rather than automatic correction of semantic content.

## Multimodal boundary

`phoenetics` is not a universal communication parser.

Gesture, sign, text, image, direct machine protocol, chemical signaling, or other modalities may bypass this subsystem entirely while still participating in shared semantics/pragmatics.

Cross-modal coalitions may use phonetic timing/prosody alongside visual gesture, gaze, body state, or context without forcing all evidence into spoken-language units.

## Failure states

The subsystem should expose, rather than hide:

- insufficient signal quality;
- stale or unknown calibration;
- segmentation ambiguity;
- speech/non-speech ambiguity;
- overlapping sources;
- unknown phone/phoneme inventory;
- language/code uncertainty;
- competing phonetic parses;
- prosodic ambiguity;
- speaker-model mismatch;
- timing/synchronization uncertainty;
- output prediction mismatch.

Downstream speech recognition should be able to consume uncertainty rather than receiving a fabricated clean phonetic stream.

## External compute

External acoustic, phonetic, speaker, or prosody models may be used only under the HC external-compute boundary.

Their outputs are typed service results with model/version/provenance and cannot become the sole implementation of essential HC phonetic cognition in a conforming complete HC unless the service is reclassified as HC-internal substrate.

## Cross-system interfaces

Strong coupling is expected with:

- `adaptable I-O handler` for channel admission/calibration;
- `speech recognition & synthesis` for lexical recognition and production realization;
- `chronology` for temporal alignment and turn structure;
- `semantics` and `pragmatics` for meaning/function hypotheses;
- `affect`, `Empathy`, `sociological behaviors`, and `personification` for downstream interpretation/expression shaping;
- `somatics` and `kinesis` for embodied articulation/self-monitoring;
- `cognition` for competing hypotheses and model selection;
- `integration-arbitration` for multimodal coalition handling.

## Evidence boundary

This contract specifies HC information architecture. It does not assume one universal phonological theory, one language family, human vocal anatomy, or a perfect mapping from acoustic signal to linguistic structure.

## Provenance

Expanded from `phoenetics/ARCHITECTURE.md`, `speech recognition & synthesis/ARCHITECTURE.md`, the adaptable-I/O boundary, temporal-hypergraph model, semantics/pragmatics contracts, and the project principle that measurement, derivation, interpretation, and action authority remain distinct.
