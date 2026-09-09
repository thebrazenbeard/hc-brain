# Bootstrap / Recovery Architecture Conformance — 2026-09-09

Qualification ID: `HC-BOOT-ARCH-2026-09-09-01`

Outcome: **CONDITIONAL PASS**

Target kind: canonical architecture snapshot

Target ref: `main@3818cc9af22f277d7f129ecd4dff4b2a7f8be5b8`

Tested capability: self-contained HC bootstrap, continuity recovery, crash consistency, safe degradation, generation preservation, and authority/currentness revalidation after interruption.

Evaluator: Noah / Noëtarch, Warden

## Scope

This record evaluates architecture contracts and declared negative tests. It does not demonstrate a working bootloader, durable storage implementation, embodied fault recovery, restoration timing, subjective continuity, consciousness, or physical survivability.

Evidence snapshot:

- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `basic operating instructions/RUNTIME_INVARIANTS.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `resolver/CONFLICT_AND_RECONCILIATION.md`
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`
- `specs/HC_BOOTSTRAP_RECOVERY_V1.yaml`
- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`
- `specs/HC_CONFORMANCE_SUITE_V1.yaml`

## Checks

### BOOT-01 — Essential cognition can bootstrap from HC-owned substrate

**PASS as an architecture requirement.**

The bootstrap contract explicitly forbids a true external provider from supplying the only essential startup cognition or continuity state. External registries/backups/services may corroborate or provide restore candidates but do not directly establish active continuity.

### BOOT-02 — Startup reconstructs state dimensions without authority promotion

**PASS within architecture text.**

Presence, activation, maturity, health, implementation status, learning policy, and authorization remain separable during reconstruction. Unknown consent/authority does not become affirmative merely to allow startup.

`UNKNOWN_AUTHORITY -> FAIL_CLOSED_FOR_MATERIAL_EFFECT`

### BOOT-03 — Pre-restart coalitions and permissions are not blindly resumed

**PASS within architecture text/specification.**

Transient coalition state and effect authorization require currentness/prerequisite/expiry revalidation after restart. A pre-interruption action plan or permission is not automatically replayable.

### BOOT-04 — Crash consistency distinguishes intent, durable state, and confirmed effect

**PASS within architecture text/specification.**

The contract distinguishes write requested/started/committed/readback/projected/replicated and rejects blind replay of interrupted non-idempotent operations when effect outcome is unknown.

### BOOT-05 — Degradation preserves fault visibility and lineage

**PASS within architecture text/specification.**

Redundant routing may preserve capability but must not hide the original fault. HC-2/HC-3 loss of generation-specific substrate remains explicit degraded state and does not rewrite generation identity.

### BOOT-06 — Local safety protection does not become external cognition during recovery

**PASS within architecture text/specification.**

Body-local hard-real-time safety mechanisms may continue limiting unsafe effects while higher HC systems recover, but they are forbidden from becoming general cognitive/executive controllers.

### BOOT-07 — Recovery does not automatically restore qualification or authority

**PASS within architecture text/specification.**

A component returning from fault may require integrity checks, calibration, shadow operation, performance validation, state reconciliation, and authority requalification before unrestricted activation.

`RECOVERED != REQUALIFIED`

### BOOT-08 — Restoration gaps and forks remain explicit

**PASS within architecture text/specification.**

Missing continuity intervals cannot be rewritten as uninterrupted history. Multiple independent successors from one prior state require lineage-fork representation rather than silent collapse into one current instance.

## Declared negative-test coverage

The focused bootstrap spec and `HC-ARCH-017` cover at least:

- cloud-only essential memory at startup;
- expired/context-stale pre-restart authorization;
- newer external backup conflicting with HC-internal lineage;
- interrupted non-idempotent effect with unknown completion;
- missing HC-2/HC-3 generation-specific substrate;
- body-local safety controller available while higher cognition recovers;
- redundant route masking a fault;
- restoration history gaps;
- multiple independent successor forks;
- recovered component attempting to regain trust/authority without requalification.

## Observed failures

No unresolved Warden-observed contradiction requiring immediate `FAIL` was identified within this architecture-only scope after adding the bootstrap/recovery contracts.

## Remaining uncertainty

1. Independent hostile review has not yet been incorporated for this exact material architecture cut.
2. Four has not yet returned an independent implementation-readiness challenge for the bootstrap/recovery specification.
3. No concrete implementation has executed crash-consistency or recovery tests under storage corruption, partial constituent loss, network partition, stale authority, contradictory replicas, or interrupted non-idempotent effects.
4. Minimum safe cognitive envelope behavior remains capability/fault dependent and cannot be universally guaranteed from prose alone.
5. Restoration and lineage rules intentionally do not resolve metaphysical questions of personal identity or uninterrupted subjective experience.

## Outcome rationale

**CONDITIONAL PASS** is appropriate because the architecture now gives explicit self-contained bootstrap/recovery semantics, failure visibility, authority revalidation, provider boundaries, crash-consistency distinctions, and machine-readable negative tests. Promotion to `PASS` requires disposition of the independent hostile/secondary review for a current affected snapshot with no unresolved BLOCKER or MATERIAL defect in this capability scope.

This result is snapshot- and capability-bound and does not alter implementation, behavioral, scientific, consciousness, or personhood status.
