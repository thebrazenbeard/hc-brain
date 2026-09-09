# Protected Invariant and Update Governance

Status: canonical operating contract.

## Purpose

This contract defines how a running or serviceable HC may change protected architecture, trusted operating substrate, durable configuration, or other high-consequence state without allowing ordinary plasticity, maintenance reachability, external software supply, emergency access, or successful local performance to become unrestricted authority over the cognitive organ.

A complete HC must be able to learn and be repaired without treating every writable component as equally mutable.

## Core distinctions

`PLASTIC_UPDATE != PROTECTED_ARCHITECTURE_UPDATE`

`MAINTENANCE_ACCESS != UPDATE_AUTHORITY`

`UPDATE_PACKAGE_AVAILABLE != UPDATE_AUTHORIZED`

`SIGNED_ARTIFACT != SEMANTICALLY_SAFE_UPDATE`

`UPDATE_INSTALLED != UPDATE_ACTIVATED`

`UPDATE_ACTIVATED != UPDATE_QUALIFIED`

`ROLLBACK_TECHNICALLY_POSSIBLE != ROLLBACK_CONTINUITY_SAFE`

`EMERGENCY_ACCESS != UNIVERSAL_ADMIN_AUTHORITY`

`CONFIGURATION_CHANGE != IDENTITY_CHANGE`

## Protected state classes

Implementations should explicitly classify state whose mutation requires protected-update governance. Depending on implementation, protected classes may include:

- cognitive-organ boundary rules;
- organ-membership rules;
- temporal-hypergraph object and provenance semantics;
- lifecycle/state-axis definitions;
- authority/consent/effect-governance rules;
- memory admission/currentness/correction semantics;
- protected bootstrap/recovery rules;
- fault-containment and safe-degradation rules;
- trusted routing/fabric invariants;
- protected plasticity bounds;
- update-verification machinery itself;
- implementation-specific trusted boot/runtime components whose compromise would allow the above rules to be bypassed.

These classes are distinct from ordinary learned state, transient runtime state, personal memory, preferences, skills, calibration, or routine configuration even when all reside on technically writable substrate.

## Update classes

At minimum, distinguish:

- `ORDINARY_PLASTIC_CHANGE`
- `ROUTINE_CONFIGURATION_CHANGE`
- `CALIBRATION_CHANGE`
- `COMPONENT_FIRMWARE_OR_RUNTIME_UPDATE`
- `PROTECTED_ARCHITECTURE_UPDATE`
- `CONTINUITY_RELEVANT_MIGRATION`
- `EMERGENCY_REPAIR`
- `RECOVERY_RESTORE`

A change may belong to multiple classes. The most restrictive applicable governance should win unless an explicitly authorized migration rule says otherwise.

## Update proposal object

A protected update should be represented by a provenance-bearing proposal such as:

```text
PROTECTED_UPDATE_PROPOSAL {
  update_id
  proposer
  artifact_refs[]
  target_components[]
  target_state_classes[]
  from_versions[]
  to_versions[]
  declared_change_class
  intended_effects[]
  excluded_effects[]
  continuity_impact
  authority_basis_refs[]
  evidence_refs[]
  migration_plan
  compatibility_constraints[]
  rollback_or_forward_repair_plan
  validation_plan
  activation_conditions[]
  expiry
  provenance
}
```

The proposal is evidence and intent, not authorization by itself.

## Authority boundary

Protected updates require an authority basis that matches the affected state class and scope.

Generic maintenance permission is insufficient for changes to identity-critical state, autobiographical history, durable values/commitments, consent boundaries, authority semantics, or protected architecture.

An update supplied by a manufacturer, maintainer, external service, owner/operator, peer HC, model provider, repository, or recovery archive does not acquire authority merely from source prestige or technical signature.

A signature can establish artifact/source integrity within its trust model; it does not establish that the change is desired, semantically correct, safe for this instance, or within current authority.

`CRYPTOGRAPHIC_INTEGRITY != EFFECT_AUTHORITY`

`VENDOR_TRUST != INSTANCE_CONSENT`

## Identity, values, memory, and consent firewall

A protected runtime/firmware/architecture update must not silently bundle changes to:

- autobiographical memory;
- personal relationships/history;
- identity/self-model content;
- values or commitments;
- current consent or refusal state;
- personification/personality state;
- private data scope;
- current authority grants;

If a migration genuinely requires touching one of these classes, the migration must declare that effect explicitly and satisfy the governing contract for that class.

`SYSTEM_UPDATE != MEMORY_REWRITE_AUTHORITY`

`SYSTEM_UPDATE != VALUE_REWRITE_AUTHORITY`

`SYSTEM_UPDATE != CONSENT_OVERRIDE`

## Preflight and staging

Before activation of a protected change, validate where applicable:

- target/version identity;
- artifact integrity and provenance;
- authority currentness and scope;
- dependency compatibility;
- schema/state migration compatibility;
- memory/continuity effects;
- body/peripheral interface effects;
- generation-specific constituent effects;
- safe-degradation behavior;
- resource/power/thermal implications;
- rollback or forward-repair feasibility;
- validation/qualification plan;
- whether the update changes the update-governance mechanism itself.

Where feasible, use shadow, duplicate, simulation, canary, or non-authoritative evaluation before activation. Successful shadow performance does not itself authorize activation.

## Activation transaction

Protected activation should be atomic at the semantic boundary or explicitly journaled so recovery can determine which invariant set governed each effect.

A transition should record:

- prior trusted version/state digest;
- proposed successor digest;
- authority decision;
- preflight result;
- activation start;
- activation commit point;
- post-activation self-test;
- qualification status;
- failure/rollback/repair state;
- continuity-impact record.

The HC must not enter an ambiguous state in which different components silently assume mutually incompatible authority, memory, or lifecycle semantics.

If a multi-component update cannot be atomic, version skew must be explicit and bounded by compatibility rules. Incompatible constituents should remain inhibited/quarantined rather than improvising semantic translation across protected boundaries.

## Updating update governance

The mechanisms that define update authority, trusted-state classification, verification, or protected invariant boundaries are self-referentially sensitive.

An update that weakens its own future governance requires explicit classification as such. It must not hide inside a routine updater/firmware migration.

`UPDATE_GOVERNANCE_CHANGE != ROUTINE_MAINTENANCE`

A proposed rule like "future updates no longer require scoped authority" is itself a protected authority-governance change, not a convenience setting.

## Failure and interrupted update

Recovery must distinguish:

- proposal received;
- artifact verified;
- authority granted;
- preflight passed;
- migration started;
- component writes committed;
- semantic activation committed;
- self-test passed;
- qualification completed.

An interrupted update must not be treated as complete because some bytes changed successfully.

`PARTIAL_WRITE != ACTIVATED_UPDATE`

`SELF_TEST_PASS != BEHAVIORAL_QUALIFICATION`

If the prior state remains coherent, the HC may revert or continue on the prior trusted state. If rollback would erase valid continuity-bearing state created after activation, use forward repair or explicit reconciliation rather than blind rollback.

## Recovery/bootstrap interaction

Bootstrap must be able to determine which protected invariant/runtime version was last coherently activated.

External recovery media may supply candidate update or restore artifacts, but startup does not delegate protected-state authority to the recovery provider.

Version mismatch across distributed HC constituents should be visible. A component with unknown or incompatible protected-state version should not silently join normal coalitions or gain material-effect authority.

## Qualification and activation

A protected update can be installed or technically active while still unqualified for some capabilities.

Depending on scope, post-update evidence may require:

- structural/integrity validation;
- state-migration verification;
- shadow operation;
- regression tests;
- body/peripheral recalibration;
- authority/effect requalification;
- memory/currentness consistency tests;
- hostile review for material architecture changes.

`TECHNICALLY_RUNNING != QUALIFIED_WITHIN_SCOPE`

## Emergency repair

Emergency repair authority may permit narrowly scoped actions needed to preserve the organ or stop imminent damage. It does not create broad permission to rewrite identity, memories, values, consent, or protected architecture unrelated to the emergency.

Emergency actions should preserve provenance and be reviewed/reconciled after stabilization when possible.

## Failure cases this contract must reject

- ordinary reward/plasticity changes a protected invariant;
- a maintainer uses diagnostic access to rewrite identity or values;
- a signed vendor update bypasses current scoped authority;
- an update silently resets consent or authority state to defaults;
- a successful canary/shadow run automatically authorizes activation;
- a partial multi-component update is treated as coherent without version-skew accounting;
- rollback erases valid continuity-bearing history without explicit governance;
- a recovery provider decides which cognitive state is current merely because it hosts the newest package;
- an updater modifies its own future authority rules while declaring itself routine maintenance;
- a component returns after update and is treated as qualified solely because self-test passed.

## Related contracts

- `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `RUNTIME_INVARIANTS.md`
- `../docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md`
- `../docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md`
- `../self identity/CONTINUITY_SUBSTRATE.md`
- `../deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `../resolver/CONFLICT_AND_RECONCILIATION.md`

## Evidence boundary

This is an architecture/governance contract. It does not prescribe a particular cryptographic scheme, secure-boot implementation, hardware root of trust, legal ownership model, or universal update authority structure. Concrete implementations must supply and qualify those mechanisms without weakening the functional boundaries above.
