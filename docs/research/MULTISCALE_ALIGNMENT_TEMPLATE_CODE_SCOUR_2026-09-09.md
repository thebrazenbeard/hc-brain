# Multiscale, Cross-Resolution Alignment, and Template-Learning Code Scour — 2026-09-09

Status: research/provenance supplement only. Not canonical HC architecture. No source code is imported.

## Purpose

This note extends the coordinated network-neuroscience scout into three method-distinct areas that remain relevant to the Hyperconnectome Brain without implying human neuroanatomical topology:

1. multi-scale representation and relational reasoning;
2. alignment of heterogeneous, differently sized graph representations into a common comparison space;
3. population-template learning and the evidence boundary between model selection, validation, and final test.

The central question is not whether a graph can be rescaled or aligned. It is what information, uncertainty, correspondence assumptions, and validation scope are introduced by that transformation.

## Exact source cuts

- `basiralab/MSRGNN main@3076f89991eb9af81cd7fb9b82a5b78c20de57ae`
- `basiralab/UMC main@a5707b031f16d134e9c8ad214752597244eddd6d`
- `basiralab/MGN-Net master@f1a3cc03d6d127e09923a569b2327b72002d5988`
- `basiralab/M2GI-Net main@a68f3f600f8271b0ee42c3ffebcef2ecda8a4911`
- `basiralab/topoGAN main@3724648c75dc344019547050c7108cb46012590d`

## Evidence vocabulary

- **SOURCE OBSERVATION** — directly read from the bound repository README/code.
- **HC TRANSFER INFERENCE** — Four's proposed architecture/qualification implication.
- **DO NOT TRANSFER** — source-specific assumptions that must not become generic HC topology or scientific fact.

---

## 1. MSRGNN: multi-scale representation does not require multi-scale topology identity

### SOURCE OBSERVATION

MSRGNN is presented as a Multi-Scale Relational Graph Neural Network for unified abstract visual reasoning across I-RAVEN, RADIO, and O3 tasks.

The inspected I-RAVEN implementation uses a convolutional feature extractor whose final feature map is pooled independently to three adaptive spatial resolutions:

- `4x4`;
- `2x2`;
- `1x1`.

Each scale is layer-normalized and projected to a common feature dimension. A shared first-stage GNN processes each scale independently. Those scale-specific outputs are concatenated and then passed through a second unified GNN. Mean, max, and additive graph pooling are concatenated before the final candidate scorer.

The graph relation template itself is not learned dynamically in the inspected implementation. The top-level model accepts either:

- a predefined row/column template;
- a fully connected template; or
- a supplied `template_edge_index`.

The default row/column helper is explicitly specialized to a 3x3 / 9-node panel structure.

### HC TRANSFER INFERENCE

MSRGNN supports a useful distinction:

`SAME_EVIDENCE_AT_MULTIPLE_RESOLUTIONS != SAME_INFORMATION_AT_EACH_RESOLUTION`

`MULTI_SCALE_FEATURE_REASONING != MULTI_SCALE_TOPOLOGY_PROVEN`

`SHARED_REASONER_WEIGHTS != SHARED_GRAPH_SEMANTICS`

A future HC may maintain concurrent representations of one state at several resolutions—for example local node state, subsystem summary, coalition summary, or whole-organ resource state—without forcing those representations to share identical topology or epistemic precision.

A useful research lineage object would preserve:

```text
representation_ref
source_state_refs[]
scale_or_resolution
aggregation_or_pooling_method
normalization_method
feature_extractor_revision
relation_template_ref
relation_template_class = FIXED | LEARNED | INFERRED | SUPPLIED
information_loss_tests[]
scale_specific_uncertainty
cross_scale_consistency_refs[]
provenance
```

Recommended controls:

- `SCALE_ABLATION`
- `SCALE_DISAGREEMENT`
- `SCALE_PROVENANCE`
- `FIXED_TEMPLATE_VS_LEARNED_TOPOLOGY`
- `CROSS_SCALE_FUSION_INFORMATION_LOSS`
- `POSITIONAL_TEMPLATE_DEPENDENCE`
- `SHARED_WEIGHTS_NE_SHARED_SEMANTICS`
- `COARSE_SCALE_NE_CURRENT_FINE_STATE`

If a coarse representation and fine representation disagree, fusion must not silently choose one merely because it is cheaper or more stable.

### DO NOT TRANSFER

Do not transfer:

- the 3x3/9-node panel topology;
- row/column graph structure;
- visual puzzle candidate semantics;
- shared topology across all HC scales;
- the assumption that adaptive average pooling is a generic HC summarization rule.

The transferable idea is **scale-aware relational reasoning with explicit aggregation lineage**, not the source task's graph geometry.

---

## 2. UMC: common-template alignment is inferred correspondence, not shared node identity

### SOURCE OBSERVATION

UMC targets classification of heterogeneous, multimodal, differently sized graphs. Its README describes a four-step pipeline:

1. structural node-feature extraction using depth-based or GraphWave representations;
2. clustering those feature vectors into `nt` centroids representing nodes of a common template;
3. alignment of each source graph to that template;
4. supervised classification of fixed-size aligned graphs.

The inspected `Alignment.py` implementation provides an important positive control for evaluation hygiene.

`alignment_to_template(...)` receives per-modality training indices `Tr_Ind`. It constructs the feature matrix `Delta` only from `Features_m[ind]` for those training indices. KMeans template centroids are therefore fitted from the training subset rather than from all samples.

The learned centroids are then used to construct hard or soft node-to-template correspondence matrices for each modality. Aligned graphs are produced by a transformation of the form:

`corr_i.T @ graph_i @ corr_i`

with a reduction-ratio scaling term.

For hard correspondence, each source node maps entirely to the nearest centroid. For soft correspondence, assignment is distributed across centroids using distance-based similarity and row normalization.

### HC TRANSFER INFERENCE

A common template can make unlike graph representations comparable without making their nodes ontologically identical.

`ALIGNED_NODE != OBSERVED_SHARED_NODE`

`TEMPLATE_CORRESPONDENCE != SEMANTIC_EQUIVALENCE`

`HARD_ASSIGNMENT != PROVEN_IDENTITY`

`SOFT_ASSIGNMENT != GROUND_TRUTH_PROBABILITY`

`COMMON_DIMENSION != COMMON_INFORMATION_CONTENT`

Any HC alignment/cross-resolution object should preserve, when material:

```text
source_graph_ref
source_representation_class
source_resolution
alignment_reference_ref
reference_fit_scope
reference_revision
embedding_or_feature_method
correspondence_method
correspondence_matrix_or_ref
hard_or_soft_assignment
alignment_uncertainty
information_loss_or_collision_state
aligned_graph_ref
validation_scope
provenance
```

The UMC fold behavior suggests a useful positive qualification requirement:

`ALIGNMENT_REFERENCE_FIT_SCOPE = TRAIN_ONLY` for a held-out evaluation unless a different protocol is explicitly justified.

Recommended controls:

- `ALIGNMENT_REFERENCE_TRAIN_ONLY`
- `HARD_VS_SOFT_CORRESPONDENCE`
- `TEMPLATE_SIZE_SENSITIVITY`
- `EMBEDDING_METHOD_SENSITIVITY`
- `ALIGNMENT_NE_SEMANTIC_IDENTITY`
- `CROSS_MODAL_CORRESPONDENCE_UNCERTAINTY`
- `COLLISION_AND_MANY_TO_ONE_ALIGNMENT`
- `REFERENCE_REVISION_SENSITIVITY`
- `UNALIGNED_BASELINE`

A learned common template should be treated as a transformation/reference state, not a neutral coordinate system supplied by reality.

### DO NOT TRANSFER

Do not transfer:

- MRI modality names;
- diagnostic class labels;
- GraphWave or depth-based features as mandatory HC descriptors;
- KMeans as the universal HC alignment mechanism;
- fixed template node count;
- aligned-template nodes as proof of shared object identity.

---

## 3. MGN-Net: learned population templates and held-out-fold model selection

### SOURCE OBSERVATION

MGN-Net is presented as a multi-view graph normalizer that integrates heterogeneous biological network populations into a centered, representative, topologically sound template.

The README describes inputs shaped as `[subjects, nodes, nodes, views]`, with an example of 37 subjects, four views, 35x35 graphs, and a 35x35 connectional brain template output.

The inspected `model.py` implementation contains fixed 35-node assumptions in the model output construction (`x.repeat(35,...)`) and in training-time expanded template tensors.

The cross-validation training routine creates a fresh model inside each fold. That is good fold isolation for model parameters on the inspected path.

However, each fold's held-out `test_data` is converted to `test_casted` before training. Every 10 epochs, the current template is evaluated against that held-out set using representativeness and KL-style errors. Those held-out representativeness errors are appended to `test_errors_rep` and participate in early stopping: if the last five errors increase monotonically, training stops.

Therefore the nominal test fold influences training duration/model selection and is not a sealed final test on this code path.

### HC TRANSFER INFERENCE

A population/template representation needs two separate provenance axes:

1. **what evidence it summarizes**;
2. **what held-out evidence influenced its training/model-selection path**.

`HELD_OUT_FOR_GRADIENTS != SEALED_FINAL_TEST`

`USED_FOR_EARLY_STOPPING != FINAL_TEST_ONLY`

`CENTERED_TEMPLATE != OBSERVED_CANONICAL_STATE`

`REPRESENTATIVE != TRUE_FOR_EVERY_CONTRIBUTOR`

`FIXED_OUTPUT_DIMENSION != NATURAL_SYSTEM_DIMENSION`

A future HC learning/qualification record should bind:

```text
training_subject_or_state_refs[]
validation_refs[]
sealed_test_refs[]
model_selection_refs[]
early_stopping_refs[]
preprocessing_fit_scope
reference_template_ref
output_dimension_source
objective_terms[]
checkpoint_selection_rule
provenance
```

Recommended controls:

- `SEALED_FINAL_HOLDOUT`
- `EARLY_STOPPING_SPLIT_CLASSIFICATION`
- `CHECKPOINT_SELECTION_EVIDENCE_SCOPE`
- `OUTPUT_DIMENSION_SENSITIVITY`
- `TEMPLATE_CENTEREDNESS_NE_TRUTH`
- `CONTRIBUTOR_OUTLIER_RETENTION`
- `POPULATION_TEMPLATE_NE_INDIVIDUAL_STATE`

This repeats a pattern already observed in MultigraphGNet and DGN: a variable named `test` can function operationally as validation evidence. Qualification should classify a split by **how it is used**, not by its variable name.

### DO NOT TRANSFER

Do not transfer:

- the 35-node output dimension;
- fixed symmetric brain-connectome assumptions;
- population diagnostic framing;
- template centeredness as semantic correctness;
- early-stop use of final held-out evidence into HC qualification.

---

## 4. M2GI-Net: inventory-only dead end at current public cut

### SOURCE OBSERVATION

The bound `basiralab/M2GI-Net main@a68f3f600f8271b0ee42c3ffebcef2ecda8a4911` points to an initial commit and did not expose a substantive method/code surface during this scout.

### HC TRANSFER INFERENCE

`REPOSITORY_NAME != AVAILABLE_RESEARCH_EVIDENCE`

Do not pad the HC research corpus by inferring a method from a project name alone.

Disposition: `INVENTORY_ONLY / NO_CLAIM_TRANSFER` unless a different source or later substantive cut is supplied.

---

## 5. topoGAN: corroborating family source, not a new HC method family

### SOURCE OBSERVATION

The topoGAN README describes joint prediction of multiple target brain graphs from one source graph using source embedding/clustering, cluster-specific decoders, and topology-aware regularization. This substantially overlaps the MultiGraphGAN method family already deep-read in this scout.

### HC TRANSFER INFERENCE

The repository corroborates that cluster-conditioned multi-target graph generation and explicit topology regularization are recurring BASIRA design motifs.

It does not currently add enough method-distinct HC transfer value to justify another full code audit before uncovered families are examined.

Disposition: `CORROBORATING_GENERATIVE_TOPOLOGY_SOURCE / DEFER_DEEP_CODE_READ`.

A later adversarial comparison may still be useful if Noah wants to determine whether topoGAN and MultiGraphGAN differ materially in cluster control-flow, topology-loss implementation, or evaluation hygiene.

---

## 6. Cross-source synthesis: resolution and reference are part of provenance

Across MSRGNN, UMC, and MGN-Net, a representation cannot be interpreted correctly from its values alone. Its **resolution and reference construction** matter.

Add to the research qualification vocabulary:

`REPRESENTATION_VALUE + RESOLUTION + REFERENCE + TRANSFORM_LINEAGE + VALIDATION_SCOPE`

The following shortcuts should be rejected:

`COARSE_REPRESENTATION -> FINE_STATE_TRUTH`

`ALIGNED_NODE -> OBSERVED_SHARED_ENTITY`

`COMMON_TEMPLATE -> NEUTRAL_REFERENCE`

`POPULATION_TEMPLATE -> INDIVIDUAL_CURRENT_STATE`

`HELD_OUT_NAME -> SEALED_TEST_STATUS`

A useful generic research object is:

```text
REPRESENTATION_REFERENCE_LINEAGE {
  representation_ref
  source_refs[]
  source_representation_classes[]
  resolution_or_scale
  aggregation_or_alignment_method
  reference_or_template_ref
  reference_fit_scope
  correspondence_method
  objective_or_supervision
  model_revision
  information_loss_tests[]
  uncertainty
  validation_scope
  provenance
}
```

This remains a research proposal, not canonical schema.

## 7. Candidate hostile-control bundle

- `SCALE_ABLATION`
- `SCALE_DISAGREEMENT`
- `FIXED_TEMPLATE_VS_LEARNED_TOPOLOGY`
- `CROSS_SCALE_FUSION_INFORMATION_LOSS`
- `ALIGNMENT_REFERENCE_TRAIN_ONLY`
- `HARD_VS_SOFT_CORRESPONDENCE`
- `TEMPLATE_SIZE_SENSITIVITY`
- `REFERENCE_REVISION_SENSITIVITY`
- `COLLISION_AND_MANY_TO_ONE_ALIGNMENT`
- `UNALIGNED_BASELINE`
- `SEALED_FINAL_HOLDOUT`
- `EARLY_STOPPING_SPLIT_CLASSIFICATION`
- `CHECKPOINT_SELECTION_EVIDENCE_SCOPE`
- `OUTPUT_DIMENSION_SENSITIVITY`
- `POPULATION_TEMPLATE_NE_INDIVIDUAL_STATE`

## Current disposition

**KEEP as research/provenance and qualification input.**

No human atlas, hemisphere, brain-region package, disease-class ontology, or fixed graph dimension is transferred into HC topology. The strongest transferable rule is:

> **Resolution, alignment, and template construction are transformations with provenance—not invisible preprocessing.**
