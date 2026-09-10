# Four Independent Review — Memory Provider Boundary — 2026-09-10

Status: independent secondary architecture / implementation-readiness review; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen Warden target: `main@be59bcc807a8453e27331be05e87b3a39f8c344a`
- Qualification: `docs/qualification/MEMORY_PROVIDER_BOUNDARY_2026-09-09.md`
- Qualification ID: `HC-MEM-PROVIDER-2026-09-09-01`
- Reviewer: Four / Documentation-Specification Owner / independent secondary reviewer

## Outcome

**SECONDARY PASS WITH OPERATIONAL-RECOVERABILITY ADVISORIES AND CURRENTNESS CEILING.**

No unresolved BLOCKER or MATERIAL architecture contradiction was observed in the frozen target after the Warden-recorded provider-admission correction.

The corrected architecture consistently separates HC-internal memory admission/currentness from optional external replication, provider receipts from semantic authority, provider ordering from HC currentness, external retrieval relevance from truth, and physical location from cognitive-organ membership.

Four's independent provider-boundary review condition is satisfied for this exact frozen target.

## Findings

### 1. Warden-recorded admission ambiguity is actually corrected

**PASS.**

The corrected deep-memory provider architecture no longer places external replica/provider write-readback in the essential activation chain.

HC-internal admission is represented as:

`UNVERIFIED -> REVALIDATING -> ADMISSION_VERIFIED -> HC_INTERNAL_DURABLE_WRITE -> INTERNAL_READBACK_VERIFIED -> ACTIVE`

Optional external replication begins from `ADMISSION_VERIFIED` or `ACTIVE` and explicitly does not gate HC-internal active state.

The archival-consolidation contract independently requires essential durable admission to resolve to `HC_INTERNAL` or `HC_DISTRIBUTED_CONSTITUENT` durability rather than solely to an external receipt.

### 2. Provider success cannot rescue failed HC-internal durability

**PASS.**

`MEM-PROV-NEG-002` correctly rejects the dangerous case where an external replica write succeeds while the HC-internal write fails. Replica success alone cannot promote the memory to active essential HC memory.

This preserves custody versus cognitive ownership and avoids converting provider availability into an implicit commit protocol.

### 3. Provider revision / latest ordering cannot define currentness

**PASS.**

The current-state selector requires a unique defensible head within explicit logical scope and rejects timestamp-only winner selection. The provider-boundary contract separately states `PROVIDER_LATEST != HC_CURRENT` and requires external/internal conflicts to remain visible and enter reconciliation.

Provider revision numbers, remote timestamps, replica completion time, retrieval rank, or source prestige therefore cannot silently become currentness.

### 4. Retrieval is candidate generation, not authority

**PASS with implementation challenge.**

Current/deep memory contracts explicitly preserve `RETRIEVED != TRUE`; the external retrieval accelerator may improve access but may not be the only source of essential memory.

Implementation qualification should test more than returned content labels. Disable the external retrieval/index/search service entirely and prove that essential internally owned memory remains operationally retrievable enough to sustain the required cognitive/continuity envelope.

A design where the bytes are local but the only usable index, decoder, schema resolver, key service, embedding/search service, or equivalent access mechanism is external would violate the stated recoverability principle even though byte custody appears local.

`LOCAL_BYTES != OPERATIONALLY_PROVIDER_INDEPENDENT_MEMORY`

### 5. Hidden transitive provider dependencies

**PASS in architectural principle; implementation evidence required.**

The architecture says essential continuity must be recoverable without a true external provider. That requirement should be evaluated transitively, not merely at the database endpoint.

Implementation tests should remove external dependencies used for:

- indexing/search;
- decryption/key lookup where applicable;
- schema/type resolution;
- current-state projection;
- synchronization/current-head discovery;
- retrieval model inference;
- provider-hosted metadata needed to interpret local records;
- authentication required only to read HC-owned local state.

If loss of one of those services makes essential HC-owned memory unusable, the service is de facto essential substrate and must be moved inside the HC boundary, redundantly internalized, or explicitly reclassified under the physical-organ membership contract.

### 6. Reclassification is governed by organ-membership semantics

**PASS.**

`MEM-PROV-NEG-006` allows an only-surviving external substrate to become conforming only if state is restored to HC-owned substrate or the provider is reclassified as an HC constituent **under membership rules**.

That qualification matters. Necessity, availability, credentials, or possession of the only copy does not by itself create HC membership. Reclassification must satisfy cognitive ownership, lifecycle/fault governance, complete-organ transfer/repair semantics, and the other canonical membership conditions.

### 7. Provider readback is custody evidence only

**PASS.**

The architecture correctly separates write acknowledgement, readback/integrity verification, semantic truth, admission, activation, and currentness. A provider receipt can establish bounded custody evidence; it cannot prove that the represented proposition is true or that the provider's copy is the current continuity head.

### 8. Conflict and partition behavior

**PASS at architecture level; implementation concurrency advisory.**

External/internal mismatch is preserved with provenance and routed to reconciliation. The architecture does not authorize last-writer-wins or newest-provider-wins as a general currentness rule.

A distributed implementation should prove that asynchronous replica completion, retry, duplicate delivery, delayed provider acknowledgement, and provider-side revision races cannot overwrite or reclassify the HC-internal current projection. External replication state should remain its own custody/health plane.

### 9. Privacy/scope preservation

**PASS.**

The archival contract requires external replication to preserve or further restrict privacy/scope. Transport to a provider does not authorize broader disclosure or use.

This is consistent with treating provider operations as bounded storage/transport effects rather than cognitive authority.

## Currentness note

The two most directly relevant corrected provider surfaces remain byte-identical on observed current main:

- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml` = `137978a111ee638a50875120409a3da2e1ba0cff`
- `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md` = `eefbdc3bb0e896d3fd1345166811ff9fc651691c`

Observed main during this review: `222a6e03bcb008dad2b54c7072bc64c60bbbfe4a`.

However, the frozen qualification predates later bootstrap/recovery, protected-update, security, fault/repair, source-lineage, and other interacting architecture. Unchanged focused provider files do not automatically qualify those newer integration paths.

Therefore:

`FOCUSED_PROVIDER_BOUNDARY_UNCHANGED != CURRENT_WHOLE_SYSTEM_PROVIDER_INDEPENDENCE_PROVEN`

`FROZEN_SECONDARY_PASS != IMPLEMENTATION_PROVIDER_INDEPENDENCE_PASS`

A current implementation still must prove that newer recovery, maintenance, accelerator, security, synchronization, and currentness paths do not reintroduce an external provider as a hidden essential dependency.

## Disposition

For exact target `be59bcc807a8453e27331be05e87b3a39f8c344a`:

`HC-MEM-PROVIDER-2026-09-09-01 => SECONDARY_ARCHITECTURE_PASS`

with ceilings:

- `SECONDARY_ARCHITECTURE_PASS != IMPLEMENTATION_PASS`
- `SECONDARY_ARCHITECTURE_PASS != VERA_HOSTILE_REVIEW_PASS`
- `HC_OWNED_BYTES != OPERATIONALLY_RECOVERABLE_WITHOUT_EXTERNAL_DEPENDENCY`
- `PROVIDER_READBACK_VERIFIED != MEMORY_CURRENT_OR_TRUE`
- `PROVIDER_NEWER != HC_CURRENT`
- `EXTERNAL_SERVICE_BECOMES_NECESSARY != AUTOMATIC_HC_MEMBERSHIP`
- `FROZEN_TARGET_PASS != CURRENT_WHOLE_SYSTEM_PASS`

No canonical repair is required for the frozen provider-boundary architecture from this review.

Implementation qualification should emphasize provider-removal tests that sever transitive access dependencies, not merely disconnect the database while leaving provider-hosted interpretation/index/key/currentness services available.