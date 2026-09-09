# Noöplex / Hyperconnectome Fabric

Status: CORE BRAIN INFRASTRUCTURE / DESIGN

## Purpose

`nooplex-fabric/` defines the internal integration substrate that makes the brain a hyperconnectome rather than a collection of disconnected subsystem folders.

The fabric is the conceptual center of the HC. It is infrastructure, not a homunculus.

## Fabric responsibilities

The fabric provides or coordinates:

- internal signal transport;
- typed routing;
- node/capability discovery;
- dynamic coalition formation and teardown;
- salience/attention allocation;
- synchronization and temporal coordination;
- bounded arbitration dispatch;
- conflict-state propagation;
- working-state propagation;
- broadcast to declared audiences;
- health/liveness/fault propagation;
- redundancy/failover routing;
- plasticity event coordination;
- topology/configuration updates under policy;
- internal trace/audit hooks where required.

## Explicit non-responsibilities

The fabric is not automatically the owner of:

- truth;
- semantics;
- autobiographical memory;
- self/identity;
- goals/desires;
- values;
- consent;
- social models;
- action authority;
- phenomenal consciousness.

Those functions remain distributed across specialist systems and cross-cutting contracts.

## Internal signal bus

A fabric signal should support at least:

```text
signal_id
signal_type
source
eligible_audience / target
payload_type
payload
provenance/evidence refs
priority/salience
causal parent / correlation refs
validity/expiry
privacy scope
authority ref when relevant
```

Transport metadata does not become semantic content unless a consumer explicitly interprets it.

## Capability discovery

Nodes/interface systems should advertise bounded capabilities and lifecycle state.

```text
capability
presence_state
activation_state
health_state
accepted_inputs
produced_outputs
resource profile
version
```

Capability discovery must not imply authority.

## Coalition engine

The fabric may assemble coalitions from eligible systems according to:

- task/context;
- signal domain;
- ambiguity/conflict;
- salience;
- capability need;
- privacy;
- current health;
- resource constraints;
- assurance requirements.

Coalitions remain temporary unless explicitly defined as persistent infrastructure.

## Salience and attention

The fabric may use salience to prioritize processing and working-state retention.

Salience can be influenced by:

- novelty;
- task relevance;
- affective/interoceptive modulation;
- threat/safety state;
- explicit goal state;
- uncertainty;
- social relevance;
- learned utility.

```text
HIGH_SALIENCE != HIGH_TRUTH != HIGH_AUTHORITY
```

## Synchronization

The fabric may coordinate timing-sensitive processing using temporal metadata, barriers, windows, or synchrony policies.

Literal biological oscillation bands are optional hypotheses, not architectural requirements.

## Arbitration

The fabric routes candidate sets to the appropriate scoped arbiter. It does not contain one global `decide_everything()` operation.

Examples:

- semantic ambiguity → semantic arbiter;
- motor candidates → action arbiter;
- memory candidates → admission arbiter;
- plasticity candidates → plasticity gate/arbiter;
- routing conflict → routing arbiter.

## Fault handling

The fabric should represent node/interface health and route around failures where safe alternatives exist.

Possible states:

```text
HEALTHY
DEGRADED
FAULTED
UNAVAILABLE
QUARANTINED
RECOVERING
```

A failed specialist need not halt the entire brain unless the missing capability is a hard prerequisite for the current operation.

## Plasticity coordination

The fabric may deliver learning/modulatory signals and coordinate candidate updates, but durable changes remain subject to target-specific plasticity/homeostasis policy.

## External boundary

No external body or compute device connects directly to arbitrary intrinsic systems. External channels terminate at HC-owned interface nodes which then participate in the fabric.

## Failure modes

- fabric treated as identity holder solely because all signals traverse it;
- broadcast treated as consciousness;
- routing treated as authority;
- attention priority treated as truth;
- permanent coalition growth until every subsystem is always active;
- unbounded plasticity applied as a fabric-wide side effect;
- external peripheral registered as internal authority without boundary transition.
