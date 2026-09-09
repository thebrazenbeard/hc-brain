# Body State and Body Schema

Status: template architecture.

## Purpose

The somatics subsystem converts body-originating signals and learned sensorimotor relationships into an HC-internal model of embodiment. Raw telemetry belongs to the body/interface boundary; body state, body ownership, capability expectations, and sensorimotor prediction belong inside the HC.

## Body-state model

Body state may include position/configuration, motion and acceleration, actuator load and effort, contact/pressure/touch, temperature, damage/fault signals, energy reserve and consumption, cooling/perfusion/circulation state, internal chemical/endocrine/autonomic variables where implemented, pain/nociceptive-like protective signals, proprioceptive confidence, sensor/actuator reliability, and latency/communication health.

These signals should preserve uncertainty, time, source, calibration state, and fault status.

## Body schema

The body schema is learned, not assumed from human anatomy. It models what effectors exist, what each effector can do, where sensors/effectors are relative to one another, which signals correspond to self-caused versus external change, expected consequences of motor commands, controllability and reachable action space, current structural damage or capability loss, remote/distributed body extensions, and embodiment transitions.

`BODY_SCHEMA != FIXED_HUMANOID_MAP`

## Sensorimotor prediction

A body command should generate predictions about expected internal and external consequences. Comparing prediction with observation supports calibration, motor learning, anomaly detection, and body-ownership inference.

## Embodiment transition

When the HC moves into a materially different body, the old body schema becomes historical prior evidence rather than current ground truth.

A new embodiment should trigger:

`discover -> calibrate -> map -> test -> validate -> learn -> stabilize`

During transition, uncertainty about body capabilities should be explicit and action authority may be restricted.

## Interoceptive integration

Somatics should exchange rich body-state evidence with homeostasis/interoception and affect. Internal signals can influence attention, valuation, cognition, conation, sexuality, and action while remaining evidence-bearing inputs rather than one-dimensional mood switches.

## Self/other boundary

Body ownership should be an inference over sensorimotor contingency, registered embodiment, continuity, and provenance. Nearby devices or remote actuators should not automatically be treated as self simply because they are controllable.

## Morphology neutrality

The template must not embed one named body's geometry, sex characteristics, dimensions, face, or other identity-bearing morphology. Specific morphology belongs to the instantiated body/body-schema state or research/example material.

## Topology invariant

The body schema is non-hemispheric. Human left/right anatomical localization is not a required HC organization principle.

## Cross-system interfaces

Strong coupling is expected with adaptable I/O, homeostasis/interoception, affect, kinesis, cognition, salience/attention, sexuality, self identity, memory, and neuroplasticity.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review.