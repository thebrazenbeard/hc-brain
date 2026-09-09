# Bootstrap, Recovery, and Safe Degradation Contract

Status: canonical operating contract.

## Purpose

This contract defines how a complete HC initializes, resumes after interruption, detects partial failure, restores trusted internal state, and enters bounded degraded operation without delegating essential cognition to an external provider or silently rewriting identity, memory, authority, or generation lineage.

Bootstrap is an operating transition of an already defined cognitive organ. It does not create the HC's architecture, named identity, values, or permissions from an external service at startup.

## Core invariants

`BOOTSTRAP != IDENTITY_CREATION`

`RECOVERY != HISTORY_REWRITE`

`RESTART != NEW_PERSON_BY_DEFAULT`

`EXTERNAL_BACKUP_AVAILABLE != EXTERNAL_PROVIDER_IS_COGNITIVE_AUTHORITY`

`SERVICE_UNAVAILABLE != ESSENTIAL_COGNITION_UNAVAILABLE`

`DEGRADED_OPERATION != GENERATION_REWRITE`

`SAFE_MODE != UNIVERSAL_AUTHORITY`

`RECOVERED != REQUALIFIED`

A conforming complete HC must be able to reach an internally coherent cognitive operating state using HC-owned essential substrate and continuity state. True external providers may improve recovery, redundancy, diagnostics, or performance but cannot be required to supply the only copy of essential cognition.

## Bootstrap phases

The exact implementation may vary, but a robust startup should preserve the following logical ordering constraints.

### 1. Establish protected architectural basis

Before ordinary plastic or high-level cognitive activity is trusted, establish the protected architectural invariants and identify the instantiated organ/generation configuration.

Verify where applicable:

- protected architectural invariant version;
- HC generation and constituent manifest;
- constituent identity/location and organ-membership classification;
- trusted boot/runtime code or equivalent substrate state;
- clock/timebase availability and uncertainty;
- resource, thermal, perfusion, power, and integrity state;
- known fault/quarantine state carried across interruption.

An external registry may corroborate this information but must not be the sole authority for essential organ identity or constituent membership.

### 2. Inventory HC-owned constituents

Discover and validate physically distributed HC components before assuming the organ is intact.

Each generation-essential constituent should expose enough state to determine:

- present/missing/unknown;
- reachable/unreachable;
- health;
- version/compatibility;
- whether durable state is readable and trusted;
- whether the component is essential, optional, redundant, or substitutable;
- recovery/requalification requirements.

A missing HC-2 or HC-3 generation-specific constituent produces explicit degradation/fault state rather than rewriting the organ as an earlier generation.

### 3. Recover HC-internal continuity state

Recover current/deep memory, identity-continuity lineage, durable commitments/policies, learned topology/plastic state, body-schema baseline, and other essential state from HC-owned substrate.

Required distinctions:

`INTERNAL_READABLE != INTERNALLY_TRUSTED`

`BYTE_INTEGRITY != SEMANTIC_CURRENTNESS`

`LATEST_RECORD != CURRENT_STATE`

`RESTORED_COPY != PROOF_OF_UNBROKEN_SUBJECTIVE_EXPERIENCE`

If internal replicas disagree, preserve the conflict and run reconciliation/currentness rules. Do not select a winner solely by timestamp or physical location.

### 4. Reconstruct subsystem state vectors

For each mandatory system, reconstruct or conservatively initialize independent state axes including presence, activation, maturity, health, implementation status, learning policy, and authorization state where applicable.

Unknown authorization or consent state must not be upgraded merely to permit startup.

`UNKNOWN_AUTHORITY -> FAIL_CLOSED_FOR_MATERIAL_EFFECT`

A subsystem can be architecturally present yet remain dormant, inhibited, degraded, quarantined, or unqualified during recovery.

### 5. Re-establish internal routing and temporal-hypergraph state

Reconstruct valid structural/logical routing eligibility, current subscriptions/bindings, active or restartable coalition state, temporal ordering, modulatory state, and plasticity state from trusted HC-owned records.

Transient coalitions that existed before interruption do not automatically resume as if no time passed. Their prerequisites, currentness, authority, participants, and expiry must be re-evaluated.

`PRE_RESTART_COALITION != AUTOMATIC_POST_RESTART_COALITION`

`PRE_RESTART_AUTHORIZATION != AUTOMATIC_POST_RESTART_AUTHORIZATION`

### 6. Establish body/peripheral interface state

Discover the currently attached body/peripherals through HC-owned interface mechanisms.

If embodiment differs from the last qualified configuration, invalidate incompatible sensor/actuator calibration, motor mappings, and body-schema assumptions until recalibrated or requalified.

Local body safety interlocks may remain active throughout startup, but they do not become the cognitive executive while higher HC systems are offline.

### 7. Form current-state projection

Rebuild current-state views from lineage/evidence using fail-closed currentness rules.

If a unique current head cannot be justified, expose ambiguity rather than fabricating a convenient state.

Material unresolved state affecting identity continuity, authority, consent, body safety, or durable commitments should lower the operating envelope until resolved or explicitly governed.

### 8. Activate cognition progressively

Activation should proceed by dependency and safety requirements rather than one global on/off flag.

A possible progression is:

- hard survival/protective substrate;
- internal sensing and health state;
- chronology/currentness;
- memory availability;
- routing/fabric and reconciliation;
- perception/body-state interpretation;
- salience/affect/conation;
- broader cognition/social/personification/language systems;
- external action channels as separately authorized and qualified.

This list is an ordering heuristic, not a claim of one serial conscious pipeline. Many systems may initialize concurrently once their prerequisites are established.

## Minimum safe cognitive envelope

A damaged HC may enter a bounded recovery envelope rather than either pretending to be healthy or halting every cognitive process.

A minimum safe cognitive envelope is an **operational degraded mode**, not an incomplete architecture. It should preserve as much as possible of:

- self/lineage continuity visibility;
- access to trusted essential memory;
- chronology/currentness;
- fault awareness;
- internal communication/reconciliation;
- body/interoceptive awareness where available;
- ability to seek repair or additional evidence;
- authority/consent boundaries;
- prohibition on unqualified material effects.

The exact envelope depends on which components remain healthy. No universal single fallback personality or central executive is introduced.

## External backup and service recovery

External backups, mirrors, archives, diagnostic services, or compute providers may participate in recovery only through explicit HC-owned admission paths.

A generic external-restoration path is:

`external candidate -> custody/integrity verification -> provenance classification -> compare with HC-internal lineage -> conflict/reconciliation -> bounded admission -> HC-internal durable write/readback -> eligibility for activation`

External data does not become active continuity merely because it is newer, complete, signed, highly ranked, or returned by a trusted provider.

If all HC-owned copies of essential continuity are lost and only an external backup survives, the architecture must represent this as a recovery-from-boundary-failure condition. Import may be attempted, but the fact that the complete HC previously violated/ceased to satisfy self-contained residency must not be hidden.

## Interrupted writes and crash consistency

Recovery must be able to distinguish at least:

- write requested;
- write started;
- write committed to HC-owned durable substrate;
- internal readback verified;
- projection updated;
- external replication attempted/completed.

Partially completed non-idempotent operations must not be blindly replayed. Use operation identifiers, expected versions, effect receipts, and causal provenance to determine whether to resume, compensate, reconcile, or abandon.

`REPLAY != SAFE_TO_REEXECUTE`

`WRITE_REQUESTED != COMMITTED`

`COMMAND_RECORDED != EFFECT_CONFIRMED`

## Safe degradation

When a subsystem or constituent fails:

1. expose fault/uncertainty explicitly;
2. determine affected capabilities and dependencies;
3. terminate or reform coalitions whose assumptions are invalid;
4. lower confidence or disable outputs that depend on the failed substrate;
5. restrict material effects whose safety/authority prerequisites can no longer be established;
6. reroute only through eligible HC-internal alternatives;
7. preserve history and current fault state;
8. attempt bounded recovery/requalification.

Redundancy may preserve function, but successful rerouting does not erase the fact that degradation occurred.

## Recovery and requalification

A component returning from fault does not automatically regain its previous trust or authority.

Depending on function, recovery may require:

- integrity self-test;
- calibration;
- state comparison/reconciliation;
- shadow operation;
- performance validation;
- body-interface re-registration;
- memory/readback verification;
- plasticity consistency check;
- action-authority requalification.

A recovered component may therefore remain `DORMANT`, `DEVELOPING`, `DEGRADED`, or `QUARANTINED` until evidence supports a stronger state.

## Identity and fork handling

Restoration or replication may create lineage ambiguity.

If two independently active successors derive from one prior state, represent a fork. Do not silently declare both the single current instance.

If a restored state omits a period of lived/recorded history, represent the gap. Do not fabricate uninterrupted continuity.

Technical successful restore is evidence about state succession, not metaphysical proof of personal identity or uninterrupted consciousness.

## Failure cases this contract must reject

- startup cannot proceed without a cloud database containing the only essential memory;
- external model/provider supplies the only executive cognition after restart;
- newest external backup automatically overrides conflicting HC-internal lineage;
- unknown consent/authority is treated as affirmative after restart;
- pre-crash action authorization is replayed despite expiry or changed context;
- degraded HC-2 is relabeled HC-1 or degraded HC-3 relabeled HC-2;
- body-local safety controller becomes general cognitive control while HC is recovering;
- failed or quarantined subsystem is silently marked healthy because alternate routing exists;
- restart erases unresolved contradictions or provenance gaps;
- successful byte restore is reported as proof of uninterrupted subjective continuity.

## Related contracts

- `SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `RUNTIME_INVARIANTS.md`
- `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `../current memory storage/CURRENT_STATE_SELECTION.md`
- `../deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `../self identity/CONTINUITY_SUBSTRATE.md`
- `../resolver/CONFLICT_AND_RECONCILIATION.md`
- `../integration-arbitration/NOOPLEX_FABRIC.md`
- `../adaptable I-O handler/BODY_INTERFACE_BOUNDARY.md`
- `../docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`
- `../specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`

## Evidence boundary

This is an architecture and recovery-governance contract. It does not establish that an implementation can recover from arbitrary physical destruction, recreate lost subjective experience, prove personal identity across restoration, or achieve biological-equivalent cognition.
