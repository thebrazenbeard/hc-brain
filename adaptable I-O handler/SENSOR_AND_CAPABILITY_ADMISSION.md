# Sensor and Capability Admission

Status: template architecture.

## Purpose

The adaptable I/O layer admits new sensors, effectors, channels, and external computational peripherals through bounded evidence rather than assuming that discoverable hardware is trustworthy, understood, or safe to use.

## Evidence classes

For interface-derived information, preserve at least:

- `MEASURED` — lossless values/bytes as returned across the declared acquisition boundary;
- `DERIVED` — calibrated, scaled, filtered, transformed, localized, segmented, or feature-extracted values with lineage;
- `INFERRED` — interpretations about object, state, cause, fault, meaning, or capability.

`MEASURED != DERIVED != INFERRED`

A driver or adapter may supply necessary transport decoding without being credited as learned semantics.

## Admission lifecycle

Recommended lifecycle:

`DISCOVERED -> DESCRIBED -> TESTING -> CALIBRATING -> VALIDATED_WITHIN_SCOPE -> AVAILABLE`

Exception/negative states:

`UNSUPPORTED`, `DEGRADED`, `FAULTED`, `QUARANTINED`, `REJECTED`, `REMOVED`, `UNKNOWN`.

## Capability manifest

An admitted interface should expose, where applicable, channel/interface identity, modality/effect class, read/write direction, units/encoding/transport, sampling/update behavior, latency/jitter, dynamic range/saturation, spatial/body attachment scope, calibration basis/version, confidence/reliability, write/action capabilities, safety/consequence class, failure/disconnect semantics, embodiment binding, provenance, and test evidence.

## Bounded validation

Validation claims must be scoped to the operating conditions actually tested. Useful admission tests include known positive and negative/sham conditions, remount/reconnection repeatability, confounder perturbation, barrier/occlusion tests, saturation/range checks, timing/latency verification, independent corroboration where available, and the cheapest decisive kill test for the claimed capability.

A passed test establishes only the bounded claim tested.

## Independence of evidence

Multiple derived features from one raw measurement belong to one evidence family; they are not automatically independent corroboration.

Likewise, multiple software interpretations of the same sensor stream should not be counted as multiple physical observations.

## Semantic admission

Hardware metadata and adapter labels are hypotheses/annotations about what a channel represents. Learned body/world semantics should retain separate provenance so a manufacturer label does not masquerade as HC discovery.

## Effectors

Write-capable channels must declare effect capability separately from observation capability. Merely connecting a bidirectional protocol must not silently grant actuation authority.

`WRITE_CAPABLE != AUTHORIZED_TO_WRITE`

## Embodiment transfer

Calibration and learned mapping are bound to embodiment/interface identity. Transfer to a new body or replacement device requires explicit compatibility evaluation and recalibration when material.

## External computation

An external model/service can be admitted as a computational peripheral with declared input/output contract, provenance, latency, failure mode, and evidence ceiling. Its output enters as evidence/result, not direct internal belief or authority.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review.