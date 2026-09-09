# Body Interface Boundary

Status: template architecture.

## Purpose

The adaptable I/O layer is the HC-owned boundary between the cognitive organ and whatever body or external sensor/actuator topology is attached to it.

The body supplies signals and effects. The HC interprets, learns, integrates, remembers, values, decides, and authorizes action.

## Interface principle

External devices are described by capabilities, not by assumptions about humanoid anatomy.

A body interface may expose:

- visual streams;
- acoustic streams;
- chemical, thermal, pressure, inertial, proprioceptive, nociceptive-like, or other sensor channels;
- manipulators, locomotion systems, speech apparatus, displays, lights, tools, remote actuators, or networked effectors;
- internal physiological/engineering telemetry such as temperature, power reserve, perfusion/cooling state, load, damage, and actuator health.

The HC must discover and validate what a channel can actually sense or do before assigning semantic meaning to it.

## Admission lifecycle

Recommended capability lifecycle:

`DISCOVERED -> DESCRIBED -> CALIBRATING -> VALIDATED -> AVAILABLE`

with exception states:

`DEGRADED`, `FAULTED`, `QUARANTINED`, `REMOVED`, `UNKNOWN`.

A new channel does not become trustworthy merely because it exists or reports metadata.

## Body-schema adaptation

The somatic/body-schema systems should learn mappings between:

- command and resulting movement/effect;
- sensory change and likely body/world cause;
- spatial/temporal relationships among channels;
- reliability, delay, saturation, dead zones, and drift;
- controllability versus passive observation;
- local-body versus remote/distributed effectors.

A body swap therefore creates a re-learning and revalidation problem, not a brain replacement problem.

## Remote embodiment

Distributed sensors and actuators can be treated as body extensions when they are admitted into the HC-owned interface model with explicit latency, trust, authority, failure, and disconnect semantics.

Remote embodiment must not silently convert an external controller or cloud service into the cognitive center.

## Evidence boundary

Outputs from external models, databases, operators, services, and diagnostic systems enter through typed evidence interfaces unless they are explicitly engineered as HC-internal services.

The interface must preserve source identity, observation time, confidence/reliability when available, transformation history, and failure state.

`CONNECTED != TRUSTED`

`AVAILABLE != UNDERSTOOD`

`OBSERVED != INTERPRETED`

`COMMAND_CAPABLE != AUTHORIZED_TO_ACT`
