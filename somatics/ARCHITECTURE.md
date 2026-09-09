# Somatics Architecture

Status: template architecture / embodiment interface

## Purpose

Somatics represents the HC's body-schema, proprioceptive, nociceptive, tactile, vestibular, motor-state, and embodiment-calibration functions. It is the bridge between distributed cognition and the continuously changing state of whatever body hosts the HC.

The base template does not assume one particular body morphology or physiology.

## Inputs

Candidate somatic inputs include:

- touch, pressure, vibration, and temperature;
- nociception or damage localization;
- joint position and velocity;
- tendon, load, and actuator-force state;
- vestibular acceleration and orientation;
- body pose;
- motor-command efference copy;
- local reflex state;
- embodiment calibration and geometry;
- peripersonal-space state.

## Body schema

The subsystem should maintain a probabilistic, updateable body model rather than a fixed anatomy table. It should distinguish:

- nominal morphology;
- current pose;
- reachable workspace;
- actuator capability;
- calibration confidence;
- current impairment or damage;
- predicted sensory consequence of movement;
- mismatch between expected and observed body state.

## Hierarchical control

Fast local stabilization and withdrawal loops should not wait for deliberative cognition. Higher layers issue goals, trajectories, or action candidates; local controllers enforce timing, load, and stabilization constraints.

This separation prevents slow cognition from becoming the only path for physical control.

## Calibration

Embodiment requires active calibration. Candidate learned mappings include:

- forward models: action -> predicted sensory consequence;
- inverse models: desired state -> motor recruitment;
- joint and collision envelopes;
- vestibulo-ocular or sensor-stabilization mappings;
- reach, grasp, locomotor, and posture primitives;
- nociceptive localization;
- body-ownership and peripersonal-space mappings.

Imported or preconfigured body models remain distinguishable from mappings established through actual calibration or lived interaction.

## Cross-system coupling

Somatics interfaces strongly with:

- `kinesis` for motor execution;
- `homeostasis-interoception` for internal-body state;
- `optics` and other sensory domains for spatial registration;
- `affect` for pain, arousal, posture, and action readiness;
- `self identity` for embodiment continuity in downstream identity implementations;
- `current memory storage` for live pose/task state;
- `routing instructions with neuroplasticity` for calibration updates;
- `integration-arbitration` for action selection under bodily constraints.

## Evidence boundary

DOCUMENTED: biological cognition depends strongly on sensorimotor, proprioceptive, vestibular, nociceptive, and interoceptive feedback.

INFERRED TEMPLATE RULE: a reusable HC architecture should treat body schema and somatic feedback as first-class state rather than as a peripheral device driver.

UNKNOWN / IMPLEMENTATION-DEPENDENT: exact host morphology, neural interface, actuator technology, and substrate realization.

## Provenance

Generalized from `research/nooplex-hc3-architecture-v1/docs/integration/SYNTHETIC_BODY_INTERFACE.md` and related HC embodiment research. Setting-specific body claims were excluded.