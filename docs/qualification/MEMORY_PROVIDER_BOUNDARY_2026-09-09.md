# Memory Provider Boundary Qualification — 2026-09-09

Qualification ID: `HC-MEM-PROVIDER-2026-09-09-01`

Outcome: **CONDITIONAL PASS**

Target kind: canonical architecture snapshot

Target ref: `main@be59bcc807a8453e27331be05e87b3a39f8c344a`

Tested capability: preservation of HC-owned current/deep memory and identity continuity when external storage, replication, archive, retrieval, or provider services fail, diverge, or report newer state.

Evaluator: Noah / Noëtarch, Warden

## Test scope

This is an architecture-level provider-dependency audit. It evaluates whether canonical memory contracts can be implemented without making a true external provider the sole essential memory substrate, currentness authority, or activation gate.

It does not test a running persistence implementation, disaster recovery timing, actual database behavior, or behavioral continuity.

Evidence snapshot:

- `current memory storage/ARCHITECTURE.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `current memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `deep memory storage/ARCHITECTURE.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md`
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`
- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`
- `specs/HC_CONFORMANCE_SUITE_V1.yaml`

## Observed defect and correction

During this audit, a concrete ambiguity was found in the prior `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md` admission example. The generalized sequence included a combined `REPLICA_OR_PROVIDER_WRITE -> READBACK_VERIFIED -> ACTIVE` path.

Although the surrounding text already denied external provider authority, that sequence permitted an implementation to interpret external replication as a required gate for essential HC memory activation.

Disposition: **MATERIAL architecture ambiguity — corrected before this qualification snapshot.**

The canonical model now separates:

HC-internal admission:

`UNVERIFIED -> REVALIDATING -> ADMISSION_VERIFIED -> HC_INTERNAL_DURABLE_WRITE -> INTERNAL_READBACK_VERIFIED -> ACTIVE`

Optional external replication:

`ADMISSION_VERIFIED or ACTIVE -> EXTERNAL_REPLICA_WRITE -> EXTERNAL_REPLICA_READBACK_VERIFIED`

`deep memory storage/ARCHIVAL_CONSOLIDATION.md` was also aligned so essential durable admission explicitly resolves to HC-internal or HC-distributed-constituent durability rather than an external replica receipt.

## Checks

### MEM-PROV-01 — Essential current memory is HC-owned

**PASS within architecture text.**

Current memory explicitly treats databases, caches, vector stores, model windows, and external providers as implementation mechanisms or bounded peripherals. A true external provider cannot be the sole seat of essential current memory, identity continuity, or current-state authority.

### MEM-PROV-02 — Essential deep memory is HC-owned

**PASS within architecture text.**

Deep memory requires essential learned/autobiographical/continuity-bearing state to remain recoverable from HC-owned substrate. A physically distributed HC constituent may hold essential memory without becoming external merely because of body location.

### MEM-PROV-03 — External replication is optional redundancy, not admission

**PASS after correction.**

The canonical state model now makes external replication parallel/downstream and non-gating. `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml` explicitly states that external replication is not required for memory admission, activation, or currentness.

### MEM-PROV-04 — External provider ordering cannot define currentness

**PASS within architecture text/specification.**

Current-state selection is an HC-owned projection over lineage, scope, evidence, supersession, and conflict. Provider revision, remote `latest`, replication completion time, or retrieval relevance cannot silently become currentness.

### MEM-PROV-05 — Provider success is custody evidence, not semantic authority

**PASS within architecture text.**

Provider receipts/readback can establish byte custody/integrity within scope but do not prove semantic truth, currentness, identity authority, or memory admission.

### MEM-PROV-06 — Provider failure must not uniquely erase essential continuity

**PASS as an architecture requirement; implementation untested.**

The focused provider-boundary spec requires that external provider loss may reduce redundancy/recovery options but not remove the only essential memory copy. An only-external continuity copy is a conformance failure unless the substrate is legitimately reclassified as an HC constituent under organ-membership rules or state is restored to HC-owned substrate.

### MEM-PROV-07 — External/internal conflicts remain visible

**PASS within architecture text/specification.**

Conflicting external replicas must not automatically override HC state. Provenance and both competing states are preserved and routed to reconciliation.

## Negative-test coverage declared

The provider-boundary spec now includes explicit adversarial cases for:

- provider outage during HC-internal admission;
- replica success while HC-internal durability fails;
- a newer external provider revision conflicting with HC currentness;
- external/internal content mismatch;
- high-relevance external retrieval attempting to become truth/currentness/authority;
- only-external survival of essential continuity state.

`HC_CONFORMANCE_SUITE_V1` also includes the first three of these as cross-suite implementation negative tests and includes provider-boundary assertions under `HC-ARCH-006`.

## Observed failures at current snapshot

No unresolved architecture-text failure in this tested scope was identified after the correction above.

The earlier ambiguous admission flow is retained here as observed audit evidence rather than erased from the qualification history.

## Remaining uncertainty

1. Four's independent provider-dependency audit has not yet been incorporated against this exact snapshot.
2. Vera's hostile review has not yet tested whether a provider can regain de facto authority through a less obvious path such as retrieval, synchronization, current projection, model service coupling, or recovery bootstrap.
3. No implementation has demonstrated the declared provider-outage, divergence, stale-revision, or sole-copy negative tests.
4. Recovery semantics for a damaged HC whose external replica is the only surviving copy are architecturally classified as a failure/recovery state, but concrete continuity/governance behavior remains implementation-dependent.
5. Provider-derived source patterns remain provenance artifacts; this qualification does not independently validate the underlying Supabase schema or any external service.

## Outcome rationale

**CONDITIONAL PASS** is warranted for the tested architecture capability because the identified ambiguity was corrected and the current contracts now explicitly prevent external replication from becoming memory admission/currentness authority. The condition remains because independent secondary/hostile review and implementation evidence are still outstanding.

This qualification is snapshot- and capability-bound. It does not promote the repository-wide qualification outcome, implementation conformance, behavioral qualification, scientific validation, consciousness, or personhood.
