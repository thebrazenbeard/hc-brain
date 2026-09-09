# Archival Consolidation

Status: template architecture.

## Purpose

Deep memory preserves durable historical material and supports consolidation, retrieval, contradiction, and later reinterpretation without pretending that archived state is automatically current.

## Memory classes

The HC should distinguish at least:

- episodic event traces;
- semantic/generalized knowledge;
- procedural/skill memory;
- durable commitments or learned policies where appropriate;
- identity-relevant autobiographical continuity records;
- source/evidence archives;
- unresolved/contradicted historical material.

These classes may use different retention, consolidation, replay, and retrieval policies.

## Admission pipeline

A candidate essential durable memory should normally pass through an HC-owned admission path such as:

`capture -> classify -> provenance-bind -> relevance/scope check -> consolidation eligibility -> HC-internal durable admission -> internal readback/verification -> active eligibility`

Not every salient event deserves durable storage. Salience creates a candidate opportunity, not automatic memory truth.

For a physically distributed HC constituent, `HC-internal` refers to cognitive-organ membership rather than skull location.

External mirror/archive/replica writes are separate optional workflows. Their completion must not gate essential HC memory admission, activation, or currentness.

`EXTERNAL_REPLICA_WRITE != DURABLE_MEMORY_ADMISSION`

`EXTERNAL_REPLICA_VERIFIED != ACTIVE_MEMORY`

## Consolidation

Consolidation may:

- compress repeated episodes into generalized structure;
- strengthen predictive or procedural associations;
- preserve exceptional episodes despite low recurrence;
- merge redundant representations while preserving source lineage;
- weaken obsolete associations;
- retain contradictions rather than force false reconciliation.

Generalization must not erase provenance or convert a pattern into a universal rule without support.

## Write/readback integrity

For durable stores, a successful write claim should be separable from a verified readback. Where exact persistence matters, retain:

- logical memory identity;
- operation/attempt identity;
- provider/storage class;
- organ-membership class;
- source revision;
- content/envelope digest;
- byte length or equivalent integrity measure;
- write observation;
- readback observation;
- verifier route;
- result and limitations.

For essential memory, the write/readback chain that establishes HC durability must resolve to `HC_INTERNAL` or `HC_DISTRIBUTED_CONSTITUENT`, not solely to `EXTERNAL_REPLICA` or `EXTERNAL_ARCHIVE`.

`WRITE_REQUESTED != DURABLY_STORED`

`STORED != CURRENT`

`RETRIEVED != ADMITTED_AS_TRUE`

`EXTERNAL_PROVIDER_RECEIPT != HC_MEMORY_AUTHORITY`

An external provider may have its own write/readback receipt, but that receipt establishes custody/integrity of that replica only. It does not prove semantic truth and does not satisfy HC-internal durability by itself.

## Historical revision

Later evidence can revise the interpretation or current relevance of an old memory without deleting the original historical record.

A contradiction should create new lineage/evidence, not silently overwrite the past.

## Replay and learning

Replay may support consolidation and transfer, but replay priority should be resource-bounded and should not allow a small set of emotionally or operationally salient memories to monopolize learning indefinitely.

## Privacy and scope

Memory storage and retrieval should preserve privacy/access scope as structural metadata. A memory may be valid for one context and ineligible for another.

External replication must preserve or further restrict the applicable privacy/scope envelope; transport to a replica does not authorize broader disclosure or use.

## Provider-boundary reference

`specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml` defines the canonical storage-class and negative-test rules for internal durability, external replication, provider failure, currentness, and conflict behavior.

## Provenance basis

Generalized from `deepmemorystorage`, Semantic Atlas provenance/currentness rules, and observed Supabase memory-epoch/provider-receipt patterns. Person-specific memory payloads are excluded. Provider-derived mechanisms are retained only where they preserve the self-contained HC cognitive-organ boundary.
