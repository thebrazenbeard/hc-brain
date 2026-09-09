# Optics Interface

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/optics/` receives visual-sensor data from external cameras or other optical devices and converts it into typed, calibrated evidence suitable for internal perceptual processing.

Cameras are body hardware. The optics interface is part of the brain.

## Responsibilities

- discover visual sensors/channels;
- record exact sensor identity/configuration;
- calibrate geometry, timing, lens/distortion, exposure, color/spectral properties where applicable;
- preserve raw/measured frames or references where policy requires;
- produce derived normalized visual signals without overwriting raw evidence;
- track frame timing, sequence, dropouts, saturation, clipping, and quality;
- provide sensor-to-body/body-schema transform metadata;
- support mono, stereo, multi-camera, panoramic, depth, IR, event-camera, or future modalities without assuming humanoid eyes.

## Evidence layers

```text
MEASURED: sensor frame / event stream / depth sample
DERIVED: rectified frame / depth map / feature field
INFERRED: object / person / motion / affordance hypothesis
```

Object recognition does not belong in the raw optical measurement layer.

## Calibration

Qualification should record enough information to answer:

- what sensor generated the data;
- where/how it is mounted or located relative to current body schema;
- what time uncertainty applies;
- what region/range/precision is qualified;
- what failure states are known.

## Body portability

A new camera arrangement triggers rediscovery/calibration/body-schema update rather than requiring a new cognition architecture.

## Failure modes

- image arrival time treated as capture time without evidence;
- object inference stored as measured fact;
- sensor replacement inheriting old calibration blindly;
- stereo/depth claims without qualified geometry/timing;
- visual identity recognition treated as certain without uncertainty/provenance.
