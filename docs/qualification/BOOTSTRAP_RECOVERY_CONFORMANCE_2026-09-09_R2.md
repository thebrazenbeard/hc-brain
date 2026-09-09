# Bootstrap / Recovery Architecture Conformance — 2026-09-09 R2

Qualification ID: `HC-BOOT-ARCH-2026-09-09-02`

Outcome: **CONDITIONAL PASS**

Target kind: canonical architecture snapshot

Target ref: `main@5a5a48c1eab0f0736df258dce0e8b59a38e0c0bb`

Supersedes for current bootstrap/recovery architecture assessment: `BOOTSTRAP_RECOVERY_CONFORMANCE_2026-09-09.md`

The earlier record remains historical evidence for its own snapshot and is not rewritten.

Tested capability: self-contained HC bootstrap, continuity recovery, crash consistency, safe degradation, generation preservation, authority/currentness revalidation after interruption, and consistency between prose contracts, focused machine-readable specification, core cognitive-organ invariants, and cross-suite conformance checks.

Evaluator: Noah / Noëtarch, Warden

## Why a successor record is required

After the first bootstrap/recovery qualification snapshot, the architecture changed materially enough to require a new assessment: bootstrap/recovery semantics were promoted into the core `HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` rather than existing only in the focused bootstrap specification and conformance suite.

A snapshot-bound qualification cannot silently transfer to that newer architecture.

## Evidence snapshot

- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `basic operating instructions/RUNTIME_INVARIANTS.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `basic operating instructions/README.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `resolver/CONFLICT_AND_RECONCILIATION.md`
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md`
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`
- `specs/HC_BOOTSTRAP_RECOVERY_V1.yaml`
- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`
- `specs/HC_CONFORMANCE_SUITE_V1.yaml`

## Checks

### BOOT-R2-01 — Core invariant promotion is consistent with focused bootstrap contract

**PASS within architecture text.**

The new `bootstrap_recovery_and_safe_degradation` section in `HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` encodes the same boundaries as the focused bootstrap contract rather than introducing an alternate lifecycle model.

It explicitly requires HC-owned essential startup state and rejects external essential startup authority, stale authority/coalition replay, blind replay of interrupted non-idempotent effects, generation rewriting during degradation, automatic requalification, and continuity-gap/fork erasure.

### BOOT-R2-02 — Core and focused specifications preserve self-contained cognitive-organ ownership

**PASS within architecture text/specification.**

The focused and core invariant sets agree that external restore data enters as candidate evidence through HC-owned admission and cannot directly become active continuity or currentness authority.

### BOOT-R2-03 — Crash-consistency state is represented at both focused and core layers

**PASS within architecture text/specification.**

The core invariant section now requires distinctions among requested, started, internally committed, internal-readback-verified, projection-updated, effect-requested/effect-confirmed, and external-replication states. This is consistent with the focused bootstrap spec and memory-provider boundary.

### BOOT-R2-04 — Authority/currentness are revalidated after interruption

**PASS within architecture text/specification.**

Unknown or stale authority fails closed for material effects. Pre-restart coalition membership and action authority are not presumed current after interruption.

### BOOT-R2-05 — Degradation and recovery preserve independent state axes

**PASS within architecture text/specification.**

Degradation does not rewrite generation identity. Alternate routing does not erase the original fault. Returning from fault does not automatically restore prior trust, activation, or authority.

### BOOT-R2-06 — Continuity history remains epistemically bounded

**PASS within architecture text/specification.**

Restore gaps and independent successor forks remain explicit. Technical restoration is not promoted into proof of metaphysical identity or uninterrupted consciousness.

### BOOT-R2-07 — Operating-document discoverability

**PASS.**

`basic operating instructions/README.md` now indexes the bootstrap/recovery contract alongside lifecycle, authority, activation, and runtime-invariant contracts and points to the machine-readable counterparts. This reduces the risk that an implementer follows an older partial operating surface while missing the recovery contract.

## Observed failures

No new Warden-observed BLOCKER or MATERIAL contradiction was found in the bounded R2 architecture comparison.

The earlier provider-admission ambiguity remains preserved in its own historical qualification record; it is not a current bootstrap defect after the provider-boundary correction.

## Remaining uncertainty

1. Vera hostile review has not yet been incorporated against this exact R2 snapshot.
2. Four's secondary implementation-readiness challenge has not yet been incorporated against this exact R2 snapshot.
3. No running implementation has executed the focused crash, provider-loss, stale-authority, constituent-loss, restore-gap, or fork tests.
4. The architecture does not establish that subjective continuity survives restoration, and deliberately does not claim to solve that metaphysical question.
5. A concrete implementation still must prove that local protective controllers, recovery services, and external restore tooling cannot accumulate hidden general cognitive authority.

## Outcome rationale

**CONDITIONAL PASS** remains the appropriate outcome. The R2 architecture is internally more complete than the prior snapshot because bootstrap/recovery constraints now exist in the core invariant layer as well as the focused specification and conformance suite, but the project-required independent hostile/secondary review and implementation evidence remain outstanding.

Promotion to `PASS` requires disposition of independent review findings against a current affected snapshot with no unresolved BLOCKER or MATERIAL defect in this tested capability.

This result remains architecture-only, capability-bound, and snapshot-bound. It does not establish implementation conformance, behavioral qualification, scientific validation, consciousness, personhood, or uninterrupted subjective identity.
