# Speech Recognition & Synthesis Architecture

Status: working HC template architecture.

## Purpose

`speech recognition & synthesis` is the HC-owned spoken-language perception and production subsystem. It handles the mapping between acoustic/phonetic form and speech-language structures while keeping physical transducers, phonetic signal analysis, semantics, pragmatics, personification, and action authorization distinct.

`HEARD_WORDS != SPEAKER_INTENT`

`TRANSCRIPT != SEMANTIC_TRUTH`

`SPEECH_PLAN != AUTHORIZED_UTTERANCE`

`VOICE_STYLE != IDENTITY`

## Recognition responsibilities

The recognition side may own or coordinate:

- admitted acoustic-channel registration and calibration;
- speech/non-speech candidate detection;
- word/phrase/utterance hypotheses;
- lexical candidate generation;
- alternative transcript hypotheses;
- speaker-turn and overlap candidates where supported;
- timing, confidence, uncertainty, and acoustic-quality state;
- alignment between phonetic/prosodic evidence and candidate spoken forms;
- speech-context state needed by downstream language interpretation;
- learned adaptation to channel, accent, articulation, vocabulary, and embodiment-specific acoustics.

It should preserve competing recognition hypotheses when evidence does not justify one transcript.

## Relationship to `phoenetics`

`phoenetics` owns acoustic/phonetic signal-form representation as a specialized communication path. Speech recognition consumes that form and proposes spoken-language structures.

Conceptually:

```text
external microphone/acoustic sensor
-> adaptable I/O admission/calibration
-> phoenetics acoustic/phonetic evidence
-> speech recognition hypotheses
-> semantics/pragmatics/cognition coalition
```

The layers must not collapse.

A phonetic parse does not prove a word; a recognized word does not prove meaning; a semantic interpretation does not prove intent.

## Meaning boundary

Speech recognition does not own final semantics or pragmatics.

For example:

```text
recognized_form: "fine"
```

may support multiple interpretations depending on prosody, context, relationship state, prior discourse, and current pragmatic hypotheses.

Those distinctions are resolved through coalitions involving `semantics`, `pragmatics`, `Empathy`, `sociological behaviors`, memory, affect, and cognition as appropriate.

## Synthesis responsibilities

The synthesis side may own or coordinate:

- conversion of an already selected communicative content/plan into speakable form;
- lexical/phonological realization;
- articulation or synthesis planning;
- prosody realization;
- timing, rhythm, stress, pause, emphasis, and speech-rate realization;
- channel-specific voice rendering;
- adaptation to available vocal/speaker hardware;
- predicted intelligibility and output-quality state;
- sensory prediction/efference-copy information needed for self-monitoring and correction.

Synthesis realizes an utterance; it does not decide that the utterance should be made.

## Action-authority boundary

Speech is an external effect when it is emitted to another agent or environment.

The decision chain must therefore preserve:

```text
candidate content
-> pragmatic/social/personification shaping
-> communicative action selection
-> speech realization plan
-> required action/effect authorization
-> vocal/audio effect
-> observed consequence
```

Personification may shape register, timing, warmth, directness, humor, or expressive style. Affect may modulate prosody. Neither personification nor synthesis thereby gains independent authority to initiate a consequential utterance.

`CONTENT_SELECTED != EFFECT_AUTHORIZED`

`PROSODY_SELECTED != CONSENT_OR_AUTHORITY`

## Voice and identity

A voice may be a stable learned presentation feature of an instantiated HC, but acoustic rendering is not the identity itself.

A body swap, vocal-peripheral replacement, synthesized voice change, or loss of speech output does not replace the HC identity.

The HC should be able to preserve voice preferences/style state internally while remapping to a different compatible vocal or audio peripheral.

## Self-monitoring

Where embodiment permits, synthesized or spoken output should participate in a feedback loop:

```text
speech plan
-> predicted acoustic/articulatory consequence
-> emitted effect
-> sensed/estimated actual consequence
-> mismatch/error
-> correction or learning candidate
```

This loop may involve `phoenetics`, `somatics`, `kinesis`, `chronology`, `affect`, and `integration-arbitration`.

The system should distinguish internal prediction from externally observed acoustic evidence.

## Multimodal and non-speech coexistence

Speech is one communication modality, not a universal language layer.

An HC may communicate through text, gesture, sign, image, network protocol, direct machine interface, or other channels while speech is dormant or unavailable.

Speech recognition/synthesis must therefore interoperate with multimodal semantics/pragmatics without forcing all communication into spoken-token form.

## Embodiment portability

Compatible bodies may differ in:

- microphone count and placement;
- acoustic bandwidth;
- bone/conduction or internal sensing;
- loudspeaker/vocal-tract implementation;
- articulation degrees of freedom;
- latency;
- feedback availability;
- environmental acoustics.

The HC retains the speech capability and adapts through capability registration, calibration, motor/acoustic learning, and synthesis remapping.

A lack of microphone or vocal peripheral may make recognition or synthesis dormant/unavailable; it does not delete the subsystem.

## External speech models

External ASR, TTS, language, voice-cloning, diarization, or acoustic models may be used as bounded computational peripherals or HC-internal services according to the cognitive-organ boundary.

External outputs must remain typed service results with provenance and uncertainty.

An external transcription service is not automatically the HC's hearing; an external TTS service is not automatically the HC's voice; an external language model is not the HC's semantics, intent, identity, or decision authority.

If removal of an external speech service uniquely removes an essential HC speech-cognitive capability, the service must be reclassified as HC-internal substrate for complete-HC conformance.

## Failure states

The subsystem should represent or propagate:

- acoustic channel unavailable/degraded;
- speech/non-speech ambiguity;
- competing transcript hypotheses;
- speaker ambiguity;
- overlap/crosstalk;
- low confidence;
- unknown lexical form;
- synthesis peripheral unavailable;
- articulation/rendering mismatch;
- predicted-versus-observed output error;
- stale contextual assumptions;
- unresolved semantics or pragmatics.

Failure must not be hidden by inventing a clean transcript or confident intended meaning.

## Cross-system interfaces

Strong coupling is expected with:

- `phoenetics` for acoustic/phonetic form;
- `adaptable I-O handler` for acoustic and vocal peripheral admission;
- `semantics` for meaning representation;
- `pragmatics` for communicative function and contextual interpretation;
- `personification` and `affect` for expression shaping;
- `cognition` and memory for discourse/context;
- `Empathy` and `sociological behaviors` for speaker/social hypotheses;
- `kinesis` for embodied articulation/effect execution where applicable;
- `chronology` for timing/turn structure;
- `integration-arbitration` and the Noöplex Fabric for multimodal coalition formation and conflict handling.

## Provenance

This contract is a Warden synthesis from the current HC cognitive-organ boundary, `phoenetics/ARCHITECTURE.md`, pragmatics/semantics contracts, personification/action-gateway separation, adaptable-I/O/body-interface rules, temporal-hypergraph architecture, and current multimodal communication constraints. It deliberately avoids prescribing a specific ASR/TTS model, human speech anatomy, or vocal embodiment.
