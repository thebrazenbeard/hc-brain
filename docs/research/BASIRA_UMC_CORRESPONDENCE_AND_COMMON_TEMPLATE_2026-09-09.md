# BASIRA UMC Correspondence and Common-Template Study — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/UMC@main/README.md`
- `basiralab/UMC@main/Alignment.py`

## DOCUMENTED source framing

UMC is a unified classifier for heterogeneous, multi-modal and differently sized graphs. It extracts structural node features, clusters training-node features into a fixed number of template centroids, aligns graphs from different modalities to that common template, and performs downstream classification on the fixed-size aligned graphs.

## OBSERVED implementation behavior

`alignment_to_template` constructs the centroid-training matrix `Delta` from feature rows selected by the supplied training indices (`Tr_Ind`). The resulting centroids are then used to build correspondence matrices for all graphs in each modality.

For hard correspondence, each source node receives a value of 1 for its closest centroid and 0 elsewhere.

For soft correspondence, the code computes Euclidean node-to-centroid distance, transforms it with `exp(-distance / p)`, and normalizes across centroids so each row sums to 1.

The aligned graph is then computed as:

`corr_i.T @ graph_i @ corr_i`

followed by a resolution-dependent scaling factor.

## HC interpretation

The soft correspondence values are normalized similarity weights produced by a specific distance/kernel construction. Row normalization does not by itself make them calibrated probabilities that a source node and template node are the same entity.

`NORMALIZED_CORRESPONDENCE_WEIGHT != CALIBRATED_IDENTITY_PROBABILITY`

`CLOSEST_CENTROID != PROVEN_ENTITY_IDENTITY`

`COMMON_TEMPLATE_POSITION != SHARED_REAL_WORLD_ENTITY`

`C^T G C != ORIGINAL_GRAPH`

`ALIGNED_TO_SAME_TEMPLATE != SEMANTICALLY_EQUIVALENT`

The transform is valuable as a common representational coordinate system. Its common coordinates are learned structural bins/centroids, not automatically ontological identity claims.

## Positive design lesson

The implementation explicitly fits the template centroids from training indices and then applies those centroids to all graphs. This is a useful pattern for avoiding direct target-fold participation in fitting the alignment reference, provided the surrounding cross-validation path preserves that intended separation.

That does not turn the aligned test output into independent evidence: it remains a transformation of test input under a training-derived template.

## HC transfer disposition

No new canonical subsystem was needed. Existing HC architecture already covers the important transfer boundaries:

- `docs/architecture/REPRESENTATION_ALIGNMENT_AND_RESOLUTION.md`
- `specs/HC_REPRESENTATION_ALIGNMENT_V1.yaml`
- `docs/architecture/REFERENCE_IDENTITY_AND_INDEX_LINEAGE.md`

This source strengthens the existing assertion that soft correspondence weights are transformation parameters unless separately calibrated/qualified as probabilities, and that common-template coordinates must not silently become entity identity.

## Scope and caution

These observations concern the inspected implementation and documented algorithm. They do not claim UMC is defective; the alignment semantics are useful when kept within their stated representational purpose.
