# Kinesis Architecture

Status: template architecture / motor control

## Purpose

Kinesis governs movement planning, motor-policy selection, trajectory generation, actuator recruitment, movement prediction, and motor learning. It does not directly own every actuator or safety limit; it works through hierarchical local controllers and embodiment-specific gateways.

## Control hierarchy

A useful separation is:

1. intent / action candidate;
2. motor plan;
3. trajectory and coordination;
4. local actuator recruitment;
5. reflex and stabilization loops;
6. observed consequence and error signal.

Higher cognition should not need to manage raw motor timing. Peripheral or local controllers retain fast stabilization and protective functions.

## Required state

Kinesis should track:

- current body pose and velocity;
- target pose or task objective;
- actuator availability and limits;
- estimated load and balance;
- forward-model prediction;
- motor confidence;
- expected sensory consequence;
- movement error;
- fatigue/resource constraints;
- collision or reachability constraints.

## Learning

Motor learning should distinguish:

- preconfigured skill priors;
- supervised calibration;
- simulation-trained policies;
- post-embodiment refinement;
- autonomous procedural learning.

Durable updates belong to procedural/plastic state and should carry provenance and interference checks.

## Interfaces

Kinesis consumes somatic, vestibular, optical/spatial, task, and homeostatic state. It emits proposed movement or trajectory state to embodiment-specific controllers and receives consequence/error signals for correction and learning.

`kinesis != action authority`: a motor proposal still passes capability, safety, resource, and arbitration constraints appropriate to the implementation.

## Timing

The template must support multiple timing classes. Hard-real-time stabilization remains local; sensorimotor coordination is low latency; deliberative planning and skill consolidation are slower.

## Failure modes

- stale body schema;
- unstable feedback gain;
- delayed or conflicting motor commands;
- overconfident reachability;
- skill interference;
- actuator saturation;
- learned policy applied to the wrong embodiment;
- deliberative loop blocking protective control.

## Provenance

Generalized from reviewed HC body-interface work, ABIL's separation of learned recommendation from action gateway, and runtime research on time-scale separation. Identity- and body-specific details were excluded.