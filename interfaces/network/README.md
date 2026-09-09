# Network Interface

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/network/` connects the HC to external communication networks, remote sensors/effectors, services, peers, databases, and distributed devices while preserving source identity, integrity, routing, privacy, and authority boundaries.

Networking is transport. It is not semantic understanding or authority.

## Core separation

```text
CONNECTED
!= AUTHENTICATED
!= AUTHORIZED
!= DELIVERED
!= INCORPORATED
!= TRUE
```

## Responsibilities

- endpoint discovery/configuration;
- transport/protocol handling;
- peer/service identity evidence;
- encryption/integrity state where available;
- message framing;
- timing/latency/reorder/drop state;
- retry/idempotency support;
- privacy/routing boundaries;
- remote actuator/sensor channel qualification;
- network health.

## Remote embodiment

A distributed body may place cameras, microphones, drones, or actuators across a network. The network interface transports their signals, while optics/kinesis/adaptable-I/O contracts still own sensor/effector interpretation and calibration.

## External knowledge/services

Network access to a database, search engine, or model produces retrieved/external evidence. It does not silently become internal current memory or authority.

## Failure modes

- network identity conflated with cognitive identity;
- stale cached response treated as current;
- duplicate delivery executed twice without idempotency;
- transport success treated as semantic incorporation;
- remote effect triggered without exact authority/readback;
- network partition silently filled with invented state.
