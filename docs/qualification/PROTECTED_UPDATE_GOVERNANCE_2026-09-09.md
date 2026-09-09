# Protected Invariant / Update Governance Architecture Conformance — 2026-09-09

Qualification ID: `HC-UPD-ARCH-2026-09-09-01`

Outcome: **CONDITIONAL PASS**

Target kind: canonical architecture snapshot

Target ref: `main@5d9927ce90bd792fdb89dbc93d142b13eea084f8`

Tested capability: protected architectural/state update classification, scoped update authority, separation from ordinary plasticity and maintenance reachability, identity/value/memory/consent firewalling, coherent distributed activation, interrupted-update recovery, continuity-safe rollback/forward repair, and post-update requalification.

Evaluator: Noah / Noëtarch, Warden

## Evidence snapshot

- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `basic operating instructions/README.md`
- `docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md`
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `resolver/CONFLICT_AND_RECONCILIATION.md`
- `specs/HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`
- `specs/HC_CONFORMANCE_SUITE_V1.yaml`

## Checks

### UPD-ARCH-01 — Protected state is distinct from ordinary plastic state

**PASS within architecture text/specification.**

The architecture explicitly separates ordinary plasticity, routine configuration, calibration, component runtime/firmware update, protected architecture update, continuity-relevant migration, emergency repair, and recovery restore. Ordinary reward, repetition, salience, learning pressure, or local performance cannot silently commit a protected architecture change.

### UPD-ARCH-02 — Maintenance reachability and artifact integrity do not create authority

**PASS within architecture text/specification.**

The architecture preserves the distinctions:

`MAINTENANCE_ACCESS != UPDATE_AUTHORITY`

`SIGNED_ARTIFACT != SEMANTICALLY_SAFE_UPDATE`

`CRYPTOGRAPHIC_INTEGRITY != EFFECT_AUTHORITY`

A manufacturer/vendor/provider/repository/source signature may establish artifact integrity inside its trust model, but does not establish current instance authorization, semantic safety, identity authority, value authority, consent override, or unrestricted protected-state write authority.

### UPD-ARCH-03 — Identity, memory, values, consent, and authority are firewalled from generic system update

**PASS within architecture text/specification.**

The protected-update contract and focused spec explicitly reject silent bundled rewrites of autobiographical memory, relationship history, self-model/identity content, values/commitments, current consent/refusal state, personification/personality state, private-data scope, and current authority grants. A migration that truly must touch one of those classes must declare the effect and satisfy that class's own governing authority.

### UPD-ARCH-04 — Protected activation is semantically coherent across distributed constituents

**PASS within architecture text/specification.**

Protected activation must be atomic at the semantic boundary or explicitly journaled. Version skew across physically distributed HC constituents must remain visible and bounded by declared compatibility rules. An incompatible constituent remains inhibited or quarantined rather than silently joining normal coalitions under mismatched authority, lifecycle, memory, or provenance semantics.

### UPD-ARCH-05 — Installed, active, self-tested, and qualified remain distinct

**PASS within architecture text/specification.**

The architecture preserves:

`UPDATE_INSTALLED != UPDATE_ACTIVATED`

`UPDATE_ACTIVATED != UPDATE_QUALIFIED`

`SELF_TEST_PASS != BEHAVIORAL_QUALIFICATION`

Returning or updated components require evidence appropriate to the changed scope before prior trust or effect authority is restored.

### UPD-ARCH-06 — Interrupted update and rollback preserve continuity

**PASS within architecture text/specification.**

The architecture distinguishes proposal receipt, artifact verification, authority grant, preflight, migration start, component writes, semantic activation, self-test, and qualification. Partial writes do not imply coherent activation. Blind rollback is blocked when it would erase valid continuity-bearing state created after activation; forward repair or explicit continuity governance is required instead.

### UPD-ARCH-07 — Update governance cannot silently remove its own protections

**PASS within architecture text/specification.**

A change to update authority, trusted-state classification, protected invariant boundaries, or future verification requirements is itself classified as protected governance change. It cannot hide inside routine firmware or maintenance semantics.

### UPD-ARCH-08 — External update/recovery providers remain evidence sources, not cognitive authority

**PASS within architecture text/specification.**

Provider recency, artifact hosting, update availability, or external recovery-media possession do not determine current protected state. Protected-state authority remains HC-owned and must resolve through the HC's internal governance and admission mechanisms.

### UPD-ARCH-09 — Core invariant and conformance surfaces carry the protection

**PASS within architecture text/specification.**

Protected-update rules are no longer confined to the focused contract/spec. `HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` now carries a dedicated `protected_invariant_and_update_governance` section and corresponding forbidden shortcuts. `HC_CONFORMANCE_SUITE_V1.yaml` now includes blocker gate `HC-ARCH-018` and implementation-negative-test requirements for the protected-update failure modes.

### UPD-ARCH-10 — Discoverability

**PASS.**

`basic operating instructions/README.md` indexes the protected-update contract and focused spec alongside lifecycle, authority, recovery, and core conformance material.

## Observed failures

No Warden-observed BLOCKER or MATERIAL contradiction was found in the bounded architecture comparison for this cut.

No claim is made that the design has been exercised on a running HC implementation. The PASS statements above are architecture-text/specification checks only.

## Remaining uncertainty

1. Vera hostile review has not yet been incorporated against this exact protected-update snapshot.
2. Four's secondary implementation-readiness challenge has not yet been incorporated against this exact protected-update snapshot.
3. No implementation has executed the `UPD-NEG-*` negative tests, distributed version-skew recovery, continuity-safe rollback/forward-repair tests, or update-governance self-modification tests.
4. A concrete implementation still must define and qualify roots of trust, artifact verification, protected-state storage, atomic/journaled activation, component attestation/versioning, and authority representation without collapsing those engineering mechanisms into cognitive authority.
5. The architecture intentionally does not define a universal legal/ownership model or assert that any one cryptographic scheme is sufficient for instance autonomy, consent, or semantic safety.

## Outcome rationale

**CONDITIONAL PASS** is appropriate for the tested architecture scope. The protected-update boundary is explicit, internally consistent with current authority, lifecycle, recovery, continuity, plasticity, and cognitive-organ constraints, and is represented at focused-contract, focused-spec, core-invariant, and conformance-suite layers.

Promotion to `PASS` requires disposition of independent hostile/secondary review findings against a current affected snapshot with no unresolved BLOCKER or MATERIAL architecture defect in this capability. Implementation qualification remains separate and requires actual negative/recovery/update tests.

This record is target-, capability-, evidence-, and snapshot-bound. It does not establish implementation conformance, behavioral qualification, scientific validation, consciousness, personhood, legal autonomy, or manufacturability.
