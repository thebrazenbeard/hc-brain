# Synthetic Body Interface Specification

## Purpose

This document defines how HC-series Noöplex brains interface with a humanoid Synthetic body without assuming that every in-universe body-physiology claim is already scientifically demonstrated. It is an engineering bridge between the brain architecture and the Synthetic physiology material under consideration in PR #1.

## Interface principle

The brain should not be modeled as a sealed computer inserted into a body. Human cognition depends on continuous sensorimotor, autonomic, endocrine, vestibular, proprioceptive, nociceptive, and interoceptive feedback. Accordingly, every HC-series host requires a bidirectional body interface with four classes of signal:

1. Exteroceptive: vision, audition, touch, temperature, chemical sensing.
2. Proprioceptive/vestibular: joint position, muscle tension, body acceleration and head orientation.
3. Autonomic/interoceptive: internal pressure, flow, temperature, oxygenation, substrate availability, damage state, fluid balance and endocrine concentrations.
4. Motor/autonomic output: skeletal actuation, facial expression, voice, visceral pumps, vasomotor equivalents, pupil response and endocrine release.

## Cranial seat

The Noöplex occupies a compliant cranial cradle rather than being rigidly fixed to the skull. The seat should provide:

- mechanical decoupling from impact and high-frequency vibration;
- fluid and thermal coupling to the body-wide circulation/coolant system;
- redundant power and data trunks through the foramen-magnum analogue;
- optical/electrical isolation between high-speed compute hardware and excitable neural tissue;
- service access that does not require disturbing long-term memory-bearing tissue.

A scientifically conservative design favors a bioelectronic boundary layer composed of flexible electrode arrays, optical waveguides where optogenetic tissue is intentionally engineered, microfluidic channels, and conventional digital conversion electronics outside the neural tissue itself.

## Peripheral nervous-system analogue

The body interface is organized hierarchically rather than as one flat bus.

### Somatic afferent network

Carries touch, pressure, vibration, temperature, pain, limb position, tendon load and joint state toward the Noöplex. Peripheral preprocessing should mirror biology: local receptors and ganglion-like nodes compress information before central transmission.

### Somatic efferent network

Carries voluntary motor commands to distributed actuator controllers. Local spinal-like reflex nodes handle time-critical stabilization, withdrawal and load sharing without waiting for conscious deliberation.

### Autonomic network

Controls pumps, regional flow, thermal shunts, pupil equivalents, respiratory motion, endocrine release and other involuntary or semi-voluntary state regulation.

HC-3 permits conscious modulation of this system while preserving an autonomous response mode the Synthetic may voluntarily engage.

## Sensorimotor calibration

Physical Interaction Training is mandatory before normal embodiment because raw actuator geometry is not equivalent to a learned body schema. Training should establish:

- actuator recruitment maps;
- joint limits and collision envelopes;
- inverse and forward kinematic models;
- vestibulo-ocular stabilization;
- reach, grasp and locomotor primitives;
- facial-expression calibration;
- vocal-tract control;
- nociceptive localization;
- interoceptive baseline ranges;
- body ownership and peripersonal-space maps.

A transferred human consciousness may provide pre-existing priors for a human body, but those priors still require recalibration to the Synthetic body's actual mass, strength, compliance, sensory gain and latency.

## HC-series differences

### HC-1

HC-1 uses the full body interface but without specialized quantum coprocessor services or synthetic endocrine integration as intrinsic architectural requirements. It is therefore the simplest model to calibrate and diagnose.

### HC-2

HC-2 retains the HC-1 interface and adds high-speed coprocessor traffic. Quantum/photonic hardware does not replace the body interface; it operates as an accelerator for selected computational tasks. Failure of the accelerator should degrade performance rather than sever sensorimotor function.

### HC-3

HC-3 adds endocrine, autonomic and affective coupling as first-class body signals. The body is therefore part of the emotional computation rather than merely a vehicle for expression. Facial, vocal, postural and autonomic outputs should be driven by the same affective state that modulates cognition, with conscious suppression or amplification possible by volitional control.

## Compatibility with PR #1 physiology

PR #1 proposes a fully organic Synthetic body with vitreofluid circulation, distributed synthetic endocrine microclusters, enhanced musculature, hydration-dependent maintenance and a cortical Limbic Governor. This interface specification is compatible with those concepts at the architectural level, but does not independently establish the claimed material properties, strength multipliers, non-aging mechanism, hydration interval or metabolic chemistry as current real-world science.

## Design rule

No HC-series brain should be considered correctly embodied until sensorimotor control, autonomic regulation, interoception and self-model calibration have converged together. A brain that can move the body but cannot accurately feel the body's internal state is incomplete.