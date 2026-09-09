# Optics Architecture

Status: working HC template architecture.

## Purpose

`optics` is the HC-owned visual/optical perception subsystem. It converts admitted optical observations into uncertainty-bearing visual state that can participate in cognition without making external cameras, image sensors, renderers, or model services the owner of perception.

The physical camera or optical sensor may be outside the HC. Visual interpretation remains inside the cognitive-organ boundary.

`SENSOR_OUTPUT != VISUAL_INTERPRETATION`

`VISUAL_FEATURE != OBJECT_IDENTITY`

`GAZE_DIRECTION != ATTENTION`

`RECOGNITION_CANDIDATE != SEMANTIC_TRUTH`

## Responsibilities

The subsystem may own or coordinate:

- calibration and registration of visual channels;
- field-of-view and geometry models;
- frame/event timing and synchronization;
- low-level visual feature candidates;
- motion/flow and change candidates;
- depth/range/spatial hypotheses where evidence permits;
- object/region/scene candidates prior to semantic adjudication;
- visual salience candidates;
- gaze/retinal/optical state relevant to interpretation;
- uncertainty, occlusion, confidence, and sensor-quality state;
- cross-modal alignment with somatics, kinesis, speech/acoustics, temporal state, and other admitted channels;
- learned visual calibration/body-relative mappings;
- evidence/provenance needed by downstream cognition.

## Input boundary

Visual ingress comes through `adaptable I-O handler` capability admission and calibration.

External optical hardware can provide measurements such as pixels, events, spectra, range returns, or other optical observations. The external device does not decide what the observation means.

A compliant path is conceptually:

```text
external optical peripheral
-> adaptable I/O admission/calibration
-> optics observation state
-> visual hypotheses/features
-> downstream coalitions with semantics/cognition/memory/etc.
```

## Representation discipline

Optics should preserve distinctions among:

- raw or minimally transformed observation;
- calibrated observation;
- feature candidate;
- region/object/scene hypothesis;
- identity hypothesis;
- semantic interpretation;
- confidence/uncertainty;
- currentness and provenance.

An optical subsystem may propose `object_candidate = face-like-region`, for example, without owning the proposition `this is person X` unless a separate identity/semantic process supports that claim.

## Temporal-hypergraph role

Visual cognition is normally coalition-based rather than owned by one visual node.

Examples:

```text
optics + current memory + semantics + salience-attention
-> scene interpretation candidate
```

```text
optics + somatics + kinesis + chronology
-> body-relative motion / reachability estimate
```

```text
optics + empathy + sociological behaviors + pragmatics
-> social-cue hypothesis
```

Those are higher-order HC events. Optics supplies visual evidence/state; it does not inherit the authority of every participating subsystem.

## Gaze and attention

Optics may represent where visual sensors are pointed, what regions are available, and candidate visual salience. It does not own global attention.

`GAZE_TARGET != ATTENTIONAL_PRIORITY`

`VISUAL_SALIENCE != TRUTH`

`VISIBLE != RELEVANT`

`NOT_VISIBLE != NONEXISTENT`

Salience/attention arbitration remains cross-cutting and may select nonvisual evidence over a visually salient signal.

## Learning and plasticity

Optics may learn:

- sensor calibration;
- distortion correction;
- feature representations;
- body-relative geometry;
- sensor reliability models;
- visual invariances;
- cross-modal associations;
- efficient routing/coalition priors.

Plasticity must preserve the distinction between learned visual expectation and current observation. A strong prior may shape interpretation but may not overwrite contradictory measurement without explicit evidence handling.

## Embodiment portability

A body or sensor change may alter:

- camera count;
- position/orientation;
- spectral response;
- field of view;
- latency;
- resolution;
- event/frame modality;
- zoom/focus capability;
- depth/range support.

The optics subsystem remains part of the same HC and adapts by capability discovery, calibration, remapping, and learning rather than by changing brain identity.

A conforming HC can retain the optics capacity while no visual peripheral is connected. In that state the subsystem may be `DORMANT`, `INHIBITED`, `DEGRADED`, or otherwise unavailable according to the capability-state contract; it is not deleted from the organ.

## External visual computation

An external vision model or accelerator may provide bounded results such as segmentation, detection, reconstruction, tracking, or embedding services.

Its output enters as typed evidence/service result. It does not become the HC's sole visual cognition, scene memory, object identity authority, or semantic authority.

If a supposedly external service uniquely implements an essential visual cognitive capability, it must be reclassified as HC-internal substrate under the cognitive-organ boundary.

## Failure and deception resistance

The subsystem should represent or propagate failures such as:

- sensor unavailable or degraded;
- calibration invalid;
- time synchronization uncertain;
- conflicting sensors;
- occlusion;
- overexposure/underexposure;
- adversarial or spoofed input suspicion;
- stale imagery;
- unsupported depth/scale assumptions;
- unresolved identity/scene ambiguity.

Failure should reduce or qualify the affected visual claim rather than silently fabricating a clean percept.

## Cross-system interfaces

Strong coupling is expected with:

- `adaptable I-O handler` for sensor admission/calibration;
- `salience-attention` for visual selection and competition;
- `semantics` and `cognition` for interpretation;
- `current memory storage` and `deep memory storage` for recognition/history;
- `somatics` and `kinesis` for body-relative geometry and active vision;
- `chronology` for timing/currentness;
- `Empathy`, `sociological behaviors`, and `pragmatics` for social visual inference;
- `integration-arbitration` and the Noöplex Fabric for coalition formation and conflict handling.

## Provenance

This contract is a Warden synthesis from the current HC cognitive-organ boundary, adaptable-I/O admission model, temporal-hypergraph architecture, salience/attention separation, body-schema architecture, semantic claim discipline, and existing multimodal/non-equivalence rules. It intentionally defines cognitive visual responsibilities without prescribing a particular camera, visual model, biological cortical layout, or embodiment.
