# Perception

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`perception/` transforms calibrated HC-interface evidence into internal hypotheses about objects, events, spatial structure, motion, agents, sounds, body relations, and other perceptual content.

External sensors belong to the body; their HC interfaces live under `interfaces/`. Perceptual interpretation happens inside the brain.

## Layering

```text
external sensor
→ HC interface: MEASURED / calibrated DERIVED signals
→ perceptual features
→ perceptual hypotheses
→ cross-modal/world-model arbitration
```

## Perceptual hypothesis

May carry:

- modality/modalities;
- referent candidate;
- features;
- spatial/temporal support;
- source sensor refs;
- calibration/quality refs;
- confidence;
- alternatives;
- predicted observations;
- currentness.

## Multimodal fusion

Fusion should preserve source provenance and uncertainty. Multiple sensors agreeing can strengthen a hypothesis only to the degree their errors/sources are sufficiently independent.

## Active perception

Perception may propose gaze shifts, sensor repositioning, focus/exposure changes, exploratory touch, movement, or other evidence-gathering actions. Proposals pass through action/authority gates.

## Body-relative perception

Spatial and affordance representations may depend on the current learned body schema. A body change triggers recalibration rather than changing the generic perception architecture.

## Failure modes

- inferred object presented as raw sensor fact;
- correlated sensors treated as independent corroboration;
- stale calibration ignored;
- hallucinated completion labeled observed;
- active-perception proposal bypasses effect authority;
- sensor dropout silently filled with certainty.
