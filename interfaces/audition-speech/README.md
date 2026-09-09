# Audition and Speech Interface

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/audition-speech/` connects external microphones, acoustic sensors, speakers, synthetic vocal hardware, and audio channels to internal language, perception, affect, social-cognition, and action systems.

## Auditory ingress

Responsibilities include:

- microphone/channel discovery;
- timing and gain calibration;
- localization geometry where multiple sensors exist;
- raw waveform/event preservation policy;
- noise/quality state;
- derived feature/audio segmentation;
- source-separation candidates;
- speech/non-speech classification candidates.

## Speech recognition boundary

```text
MEASURED_AUDIO
→ DERIVED_AUDIO_FEATURES
→ CANDIDATE_PHONETIC/LINGUISTIC_PARSE
→ semantic/pragmatic interpretation
```

A transcript is derived/inferred content, not raw measurement.

## Speech/audio output

The interface converts an internally selected communication/action representation into external audio/speech hardware commands.

It may handle:

- voice synthesis parameters;
- prosody;
- volume;
- spatial channel selection;
- device capability limits;
- output confirmation/readback where available.

The interface does not independently decide what the organism means to say.

## Nonverbal audio

The architecture should support alarms, tones, music, environmental sonification, nonverbal vocalization, and other acoustic outputs independently of linguistic speech.

## Failure modes

- transcript treated as perfect source evidence;
- background speaker attribution promoted to certainty;
- microphone clipping/noise hidden from downstream systems;
- synthesis style treated as identity definition;
- output command treated as confirmed emitted sound without readback.
