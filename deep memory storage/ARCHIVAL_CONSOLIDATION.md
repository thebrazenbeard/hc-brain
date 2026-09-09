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

A candidate durable memory should normally pass through:

`capture -> classify -> provenance-bind -> relevance/scope check -> consolidation eligibility -> durable admission -> readback/verification`

Not every salient event deserves durable storage. Salience creates a candidate opportunity, not automatic memory truth.

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
- source revision;
- content/envelope digest;
- byte length or equivalent integrity measure;
- write observation;
- readback observation;
- verifier route;
- result and limitations.

`WRITE_REQUESTED != DURABLY_STORED`

`STORED != CURRENT`

`RETRIEVED != ADMITTED_AS_TRUE`

## Historical revision

Later evidence can revise the interpretation or current relevance of an old memory without deleting the original historical record.

A contradiction should create new lineage/evidence, not silently overwrite the past.

## Replay and learning

Replay may support consolidation and transfer, but replay priority should be resource-bounded and should not allow a small set of emotionally or operationally salient memories to monopolize learning indefinitely.

## Privacy and scope

Memory storage and retrieval should preserve privacy/access scope as structural metadata. A memory may be valid for one context and ineligible for another.

## Provenance basis

Generalized from `deepmemorystorage`, Semantic Atlas provenance/currentness rules, and observed Supabase memory-epoch/provider-receipt patterns. Person-specific memory payloads are excluded.
