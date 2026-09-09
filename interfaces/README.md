# HC Interface Systems

Status: GENERIC INTERFACE FAMILY / DESIGN

## Purpose

`interfaces/` contains HC-owned systems that connect the cognitive organ to external body hardware, environmental sensors, communication channels, actuators, and optional computational peripherals.

The interface systems are **inside the brain boundary** even when the hardware they connect to is outside it.

## Hard boundary

```text
EXTERNAL_HARDWARE
→ HC_INTERFACE
→ typed evidence/state
→ intrinsic cognition / Noöplex Fabric
```

and for effects:

```text
internal action candidate
→ authority/safety gate
→ HC_INTERFACE
→ EXTERNAL_EFFECTOR
→ effect observation/readback
```

No external device should directly own intrinsic cognition, memory, self-state, or authority.

## Interface classes

- `optics/` — visual sensor ingress and calibration;
- `audition-speech/` — auditory ingress and speech/audio output;
- `adaptable-io/` — generic discovery/calibration for novel sensor/effector classes;
- `kinesis/` — motor/action translation into body-specific effectors;
- `somatics-interoception/` — body/internal-state sensing and body-schema integration;
- `network/` — communication/network transport boundary;
- `external-compute/` — optional outside computational models/services as evidence-producing peripherals.

## Evidence discipline

Interface systems preserve the distinction between:

```text
MEASURED
DERIVED
INFERRED
```

A raw sensor reading is not automatically an object, event, intention, threat, identity, or semantic proposition.

## Calibration lifecycle

External interfaces should support:

```text
DISCOVERED
→ UNCALIBRATED
→ CALIBRATING
→ QUALIFIED
→ ACTIVE
```

with fault states:

```text
DEGRADED
FAULTED
DISCONNECTED
QUARANTINED
```

## Body portability

The HC owns mappings from external channel topology to internal representations. Changing body hardware should alter calibration/body schema/kinesis mappings, not the fundamental cognitive architecture.

## Failure modes

- direct body-to-cognition bypass;
- uncalibrated channels treated as trustworthy measurements;
- external compute treated as the organism's mind;
- actuator capability treated as permission to act;
- network delivery treated as semantic incorporation;
- body-specific assumptions baked into generic brain topology.
