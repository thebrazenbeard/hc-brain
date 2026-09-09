# Kinesis Interface

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/kinesis/` translates internal action plans into body-specific motor/effect commands and reports effect/feedback evidence back into the HC.

Kinesis is inside the brain. Motors, limbs, wheels, drones, synthetic muscles, and actuators are external body/effect hardware.

## Core separation

```text
ACTION_GOAL
!= MOTOR_PLAN
!= EFFECT_COMMAND
!= COMMAND_ACCEPTED
!= PHYSICAL_EFFECT
!= VERIFIED_EFFECT
```

## Responsibilities

- maintain actuator/body capability maps;
- transform abstract actions into body-specific control targets;
- enforce calibrated ranges and constraints;
- preserve authority/safety gate results;
- coordinate multi-effector timing;
- model expected consequences;
- ingest proprioceptive/effect feedback;
- detect command/effect mismatch;
- support skill/procedural learning;
- degrade safely when effectors fail.

## Body portability

A humanoid reach, a wheeled turn, and a drone repositioning can be different kinesis realizations of a higher-level action goal.

The HC should learn embodiment-specific motor mappings rather than hard-code universal humanoid motion.

## Authority boundary

The kinesis system may know **how** to perform an action without being allowed to perform it.

```text
PROCEDURAL_CAPABILITY != EFFECT_AUTHORITY
```

## Feedback

Closed-loop action should compare:

- intended state;
- command sent;
- actuator acknowledgement;
- sensed consequence;
- error/residual;
- updated body/world model.

## Failure modes

- motor command treated as successful action;
- stale body geometry used after hardware change;
- actuator range guessed;
- safety/authority bypassed because motion is technically possible;
- remote actuator latency ignored;
- motor error hidden from cognition/planning.
