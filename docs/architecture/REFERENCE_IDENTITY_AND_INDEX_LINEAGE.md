# Reference Identity and Index Lineage

Status: canonical architecture contract.

## Purpose

HC representations frequently move through filtering, sorting, batching, clustering, deduplication, pooling, subsetting, projection, alignment, compression, and resolution changes. Positional indices are convenient local addresses, but they are not durable entity identity.

A related representation can silently become bound to the wrong entity when one view changes positional order and another view is indexed as if nothing changed.

## Core separations

`POSITIONAL_INDEX != STABLE_ENTITY_ID`

`FILTERED_INDEX != ORIGINAL_INDEX`

`SORTED_INDEX != SOURCE_INDEX`

`BATCH_POSITION != ENTITY_IDENTITY`

`LOCAL_NODE_NUMBER != GLOBAL_ENTITY_ID`

`CORRESPONDING_POSITION != PROVEN_CORRESPONDENCE`

`SAME_SHAPE != SAME_INDEX_SPACE`

## Required lineage

Any consequential representation that uses positional addressing across transformations should retain enough information to reconstruct the binding between positions and stable referents.

A useful object is:

```text
INDEX_LINEAGE {
  index_space_id
  parent_index_space_id
  transform_id
  stable_entity_ids[]
  local_positions[]
  parent_positions[]
  dropped_entity_ids[]
  generated_entity_ids[]
  duplicate_or_merged_lineage[]
  ordering_rule
  snapshot_or_version
  provenance
}
```

Stable IDs need not be globally universal identifiers. They must be stable enough within the relevant scope to distinguish identity from current position.

## Multi-view rule

If two or more representations are supposed to describe the same entity set—such as low/high resolution views, modalities, memory projections, body maps, semantic views, or aligned graph layers—then filtering or reordering one view does not implicitly transform the others.

Cross-view lookup should use either:

1. stable IDs plus explicit correspondence; or
2. a verified shared index map tied to the exact transformation/version.

`SHARED_PRETRANSFORM_ORDER != SHARED_POSTTRANSFORM_ORDER`

## Generated and merged entities

Generated, split, merged, pooled, or super-resolved elements require explicit lineage.

A generated node may have one or more source ancestors without being identical to any one of them.

A pooled node may summarize multiple entities without becoming a new claim that those entities are one object.

`GENERATED_ENTITY != SOURCE_ENTITY`

`MERGED_REPRESENTATION != ENTITY_IDENTITY_MERGE`

`SOURCE_ANCESTOR != CURRENT_ENTITY_IDENTITY`

## Temporal-hypergraph relationship

Node/hyperedge identities in the HC temporal hypergraph must remain distinguishable from storage-array positions, tensor offsets, batch indices, database ordinals, file order, or transient routing slots.

Temporal changes in local layout do not by themselves create, destroy, merge, or split the represented cognitive entity.

Where identity itself changes, that change must be represented semantically and historically rather than inferred from position movement.

## Memory and chronology relationship

Memory records and chronology events should use stable record/event identity. Database insertion order, retrieval rank, chunk position, embedding-neighbor rank, or array offset must not become identity or supersession authority unless an explicit narrow contract defines it.

## Embodiment relationship

Body/interface remapping is especially sensitive to index drift. A new sensor ordering, actuator numbering scheme, bus enumeration, or body morphology must not silently reuse old positional mappings without calibration and identity reconciliation.

## Qualification tests

At minimum, consequential multi-view/indexed systems should be challengeable with:

- remove one interior entity and verify every surviving cross-view binding;
- permute source order while preserving stable IDs;
- duplicate one entity and verify ambiguity is surfaced rather than silently resolved;
- merge/pool entities and verify ancestry survives;
- insert generated entities and verify they do not inherit source identity automatically;
- reorder batches/chunks and verify semantic references are unchanged;
- swap embodiment enumeration order and verify stale motor/sensor mappings are rejected;
- replay historical records in a different storage order and verify event identity/currentness is preserved.

## Failure modes

- a filtered LR array selects an HR exemplar by unremapped local position;
- a sorted retrieval list is later interpreted using original database row order;
- a batched graph node index becomes a durable identity key;
- a generated high-resolution node receives the stable ID of the nearest source node without justified equivalence;
- body sensor channel 17 changes meaning after hardware replacement but retains the old learned mapping;
- deduplication collapses two semantically distinct records because their current positions or payloads look similar;
- a merged graph cluster silently becomes one entity in memory or semantics.

## Governing invariant

> **Identity follows explicit referential lineage, not incidental position. Any transformation that changes index space must preserve or explicitly reconstruct the mapping between local positions and stable referents.**

## Provenance

Promoted from existing HC representation/provenance requirements and reinforced by code-level study of BASIRA BGSR-PY, where filtered low-resolution positional indices and an unfiltered high-resolution feature array expose a concrete cross-view index-lineage hazard. See `docs/research/BASIRA_BGSR_EXEMPLAR_SYNTHESIS_AND_INDEX_LINEAGE_2026-09-09.md`.
