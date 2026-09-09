# Perception and Multimodal Inference

Status: canonical focused cognition contract.

## Purpose

Perception is HC-internal inference over calibrated interface evidence. External sensors belong to the body/peripheral side unless separately classified as HC constituents; interpretation of their signals belongs inside the HC.

A useful layering is:

```text
external sensor / HC-owned transducer
-> calibrated HC interface evidence
-> perceptual features
-> perceptual hypotheses
-> cross-modal / world-model arbitration
```

`MEASURED_SIGNAL != PERCEPTUAL_INTERPRETATION`

## Perceptual hypotheses

A perceptual hypothesis should be able to carry:

- modality or modalities;
- referent/object/event candidate;
- supporting features;
- spatial and temporal support;
- source sensor/interface references;
- calibration and quality references;
- confidence/uncertainty;
- alternatives;
- predicted discriminating observations;
- currentness/validity.

The architecture should preserve the distinction between raw observation, calibrated/derived signal, feature extraction, perceptual hypothesis, semantic interpretation, and belief/state admission.

## Multimodal fusion

Multiple modalities may strengthen, weaken, or split hypotheses, but fusion must preserve source dependence.

Two agreeing signals are not automatically independent corroboration. Shared calibration faults, shared upstream preprocessing, copied data, or common environmental artifacts can create false agreement.

Where source independence is unknown, confidence should reflect that uncertainty rather than count duplicated evidence as separate support.

## Active perception

Perception may propose evidence-gathering actions such as:

- gaze or camera reorientation;
- focus/exposure changes;
- microphone beam or gain changes;
- exploratory touch;
- body/head movement;
- sensor repositioning;
- requesting another measurement modality.

These are action candidates. They remain subject to kinesis, interface, resource, privacy, and effect-authorization gates.

`PERCEPTUAL_VALUE_OF_ACTION != AUTHORITY_TO_EXECUTE_ACTION`

## Body-relative perception

Spatial interpretation and affordances may depend on the current learned body schema and sensor placement.

A body change therefore may require:

- calibration refresh;
- sensor-frame remapping;
- uncertainty expansion;
- body-schema update;
- relearning body-relative affordances.

It does not require a new generic perception architecture or identity reset.

## Missing and degraded evidence

Sensor dropout, stale calibration, low signal quality, occlusion, clipping, aliasing, and contradictory modalities must remain representable.

The HC may predict or interpolate missing content for continued operation, but predicted completion must retain its inferred/simulated provenance.

`PREDICTED_COMPLETION != OBSERVED_SIGNAL`

## Coalition participation

Perception may form or join temporary coalitions with optics, speech/phonetic processing, somatics, chronology, memory, semantics, affect, salience/attention, world-model reasoning, and action planning.

No coalition gains global truth authority merely because several participating systems converge.

## Failure modes

- inferred object presented as raw sensor fact;
- correlated sensors treated as independent evidence;
- stale calibration ignored;
- sensor dropout filled with unjustified certainty;
- hallucinated/predicted completion labeled observed;
- perceptual salience treated as epistemic authority;
- active-perception proposal bypassing effect authorization;
- external model output being inserted directly as perception without source classification.

## Provenance

Selectively generalized from preserved foundation material on `research/hyperconnectome-foundations-20260909/perception/README.md`, then remapped into the owner-established `cognition/` root and reconciled against current HC interface, authority, temporal-hypergraph, and evidence-state contracts. The alternate branch root taxonomy was not adopted.
