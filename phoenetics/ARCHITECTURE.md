# Phoenetics / Phonetic-Signal Architecture

Status: working HC template architecture.

## Purpose

This subsystem handles acoustic/phonetic signal structure as one communication modality among many. It should extract and represent signal form without assuming that speech-like segmentation, tokenization, or linguistic interpretation is always valid.

## Processing responsibilities

The subsystem may represent:

- acoustic events and boundaries;
- phonetic/phonological candidates;
- prosody, timing, rhythm, emphasis, hesitation, and silence;
- speaker/channel characteristics relevant to interpretation;
- uncertainty over segmentation and unit identity;
- links to speech recognition and pragmatics without collapsing into either.

## Architectural boundaries

Physical-channel detection, signal segmentation, communicative-function inference, semantic grounding, convention negotiation, and rendering are distinct layers. A phonetic parse is not semantic truth.

The system must admit non-token and nonlinguistic channels, so this subsystem is a specialized path, not a universal ingress requirement.

## Provenance and uncertainty

Raw observation, parsed event, inferred signal unit, semantic hypothesis, and rendered output should remain distinguishable. Ambiguity and provenance must survive downstream processing.

## Failure modes

- forcing continuous or multimodal signals into sentence-like tokens;
- treating prosodic correlation as semantic identity;
- discarding silence, timing, or rhythm as non-information;
- promoting a segmentation hypothesis into fact;
- conflating recognized words with speaker intent.

## Provenance

Generalized primarily from `thebrazenbeard/unvtrslr`, especially its design principle that communication may be discrete, continuous, temporal, spatial, multimodal, or nonlinguistic and that channel discovery, segmentation, semantics, and rendering must remain separate.
