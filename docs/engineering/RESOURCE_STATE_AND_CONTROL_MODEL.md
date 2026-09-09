# Resource State and Control Model

Status: template machine-facing companion.

## Scope

Canonical `docs/engineering/POWER_THERMAL_AND_DISTRIBUTED_ORGAN.md` owns the HC's high-level engineering rules for distributed constituent ownership, power domains, thermal architecture, degradation, transplant handling, and body-support boundaries.

This document does not compete with that contract.

Its narrower purpose is to define the **typed resource-state semantics** needed by cognition, scheduling, fault handling, homeostasis, accelerators, memory, and maintenance.

The governing separations are:

`RESOURCE_OBSERVATION != RESOURCE_ESTIMATE`

`RESOURCE_ESTIMATE != RESOURCE_TARGET`

`RESOURCE_FORECAST != RESOURCE_MEASUREMENT`

`RESOURCE_PRESSURE != COGNITIVE_TRUTH`

`RESOURCE_PRIORITY != ACTION_AUTHORITY`

`PASSIVE_PHYSICAL_RESPONSE != AUTHORIZED_CONTROL_ACTION`

## Resource domains

A concrete HC may model any resource domain that materially constrains cognition or safe operation. Candidate domains include:

- power or energy;
- thermal load;
- heat/coolant/perfusion transport;
- HC-internal interconnect bandwidth and latency;
- compute and accelerator capacity;
- volatile working-state capacity;
- durable-memory capacity and write bandwidth;
- sensor/effector bandwidth;
- synchronization margin;
- plasticity/update budget;
- diagnostic/service capacity;
- fault/redundancy reserve.

Do not collapse these into one global `resource_health` scalar when different domains imply different actions or degradation.

## ResourceObservation

A `ResourceObservation` is evidence about a resource condition. It should bind the resource domain, constituent/path scope, observation time, evidence class, provenance, and where available value/range, units, calibration basis, source identity, uncertainty, and fault/saturation state.

Internal origin does not make a measurement infallible.

## ResourceEstimate

A `ResourceEstimate` combines or interprets observations into a current resource-state estimate or distribution.

It may carry trend, competing estimates, currentness/expiry, and forecast context. An estimate remains derived/inferred state even when it is highly confident.

## ResourceTarget

A `ResourceTarget` represents a governed operating range or envelope.

Targets may be fixed, context-sensitive, workload-sensitive, or implementation-specific. Target changes must preserve target source, authority/provenance, validity conditions, and protected limits where material.

`TARGET_CHANGE != OBSERVATION_CHANGE`

## ResourceForecast

A `ResourceForecast` predicts future resource effects over a declared horizon.

Examples include anticipated accelerator load, memory-consolidation cost, plasticity/update demand, body-action demand, cooling degradation, or interconnect congestion.

Forecast error should update calibration/model confidence where eligible; it must not rewrite prior observations.

## PassiveResourceMechanism

Some resource responses occur physically without an HC action decision. Passive conduction, heat spreading, radiation, thermal mass, or passive reserve behavior are examples.

Those mechanisms may still require engineering qualification, monitoring, and fault modeling, but their physical occurrence does not require an `authority_ref` merely to happen.

## ResourceControlAction

Active resource control is different. Examples include:

- flow/transport adjustment;
- workload migration;
- rate/duty throttling;
- capability degradation;
- nonessential subsystem inhibition;
- state-preservation/protective mode.

An active control action should bind its triggering resource state, control class, target scope, authority or standing policy, expected effect, provenance, and effect receipt where available.

A control response does not become epistemic truth merely because it was urgent or safety-related.

## Fault and degradation handoff

Resource state should feed the generic fault/degradation architecture rather than creating a parallel health ontology.

Examples:

- a local hotspot may create a resource estimate, then a fault hypothesis, then a bounded degraded-capability state;
- an accelerator thermal constraint may update accelerator availability/degradation while preserving its algorithmic suitability assessment;
- unstable power may restrict protected writes without implying memory corruption already occurred;
- loss of a body-support service may degrade the HC without transferring cognitive ownership to the body.

`RESOURCE_CONSTRAINT != ROOT_CAUSE_PROVEN`

`RESOURCE_DEGRADATION != IDENTITY_CHANGE`

## Evidence and currentness

Resource decisions may depend on fast-changing state. Objects should therefore preserve currentness/expiry where material and keep measured, derived, inferred, modeled, extrapolated, and speculative evidence classes distinguishable.

Exact wattage, thermal capacity, compute density, or energy efficiency is implementation evidence, not generic HC canon.

## Machine contract

The machine-readable companion is:

`specs/HC_POWER_THERMAL_RESOURCE_OBJECTS_V1.yaml`

That schema is subordinate to the canonical distributed-organ engineering contract for ownership/topology and supplies the typed resource objects used at runtime/design-contract level.
