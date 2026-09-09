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

`PARALLEL_ARRAY_POSITION != PROVEN_SAME_ENTITY`

`SAME_LOCAL_POSITION != SAME_SOURCE_REFERENT`

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

If two or more representations are supposed to describe the same entity set—such as low/high resolution views, modalities, memory projections, body maps, semantic views, labels/features, predictions/targets, masks/data, or aligned graph layers—then filtering or reordering one view does not implicitly transform the others.

Cross-view lookup should use either:

1. stable IDs plus explicit correspondence; or
2. a verified shared index map tied to the exact transformation/version.

`SHARED_PRETRANSFORM_ORDER != SHARED_POSTTRANSFORM_ORDER`

## Parallel arrays and split datasets

Arrays or tensors are not referentially aligned merely because they have compatible length, shape, or local index ranges.

When features, labels, metadata, masks, memory-capacity targets, authority records, chronology records, or other related views are split or transformed separately, their shared entity binding must survive explicitly.

`SAME_LENGTH != SAME_ENTITY_ORDER`

`SAME_SHAPE_OR_INDEX_RANGE != VERIFIED_CORRESPONDENCE`

`PARALLEL_VIEW_BINDING_REQUIRES_SHARED_REFERENTIAL_LINEAGE`

A train/validation/test split, shuffle, crop, subset, deduplication, or batch operation applied to one view does not authorize reuse of the corresponding local positions from another independently transformed view.

If binding cannot be established, the correspondence is `UNKNOWN`; matching local positions are not a safe fallback.

This rule applies equally to machine-learning datasets and live HC state. A metric, correction, memory admission, actuation decision, or authority check bound to the wrong referent is a semantic failure even if tensor shapes and execution remain valid.

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
- split two parallel views with deliberately different source ranges but matching local lengths and require rejection;
- shuffle only one of a feature/target pair and require referential mismatch detection before scoring;
- swap embodiment enumeration order and verify stale motor/sensor mappings are rejected;
- replay historical records in a different storage order and verify event identity/currentness is preserved.

## Failure modes

- a filtered LR array selects an HR exemplar by unremapped local position;
- a validation feature slice is paired with labels from a different source slice because both start at local index zero;
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

A second independent implementation fixture comes from BASIRA DynGNN `demo.py`, where validation subjects are sliced from the tail of one parent array while validation memory-capacity targets are sliced from the head of the related parent array and later paired by local position. The quantitative effect is not established here; the transferable lesson is that parallel local positions do not prove shared referent identity. See `docs/research/BASIRA_DYNGNN_VALIDATION_IDENTITY_AND_STATE_SCOPE_2026-09-09.md`.
