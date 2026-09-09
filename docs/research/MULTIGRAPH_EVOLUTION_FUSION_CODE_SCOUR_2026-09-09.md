# Multigraph Evolution, Fusion, and Generated-Topology Code Scour — 2026-09-09

Status: research/provenance supplement only. Not canonical HC architecture. No source code is imported.

## Purpose

This note deep-scours additional BASIRA graph-learning sources that are adjacent to, but intentionally nonduplicative of, Noah's current HADA/BGSR lane and Four's earlier RegGNN/DGN/GSR-Net/Nilearn/brainGraph/federation findings.

The central HC question is not whether these methods can generate or fuse graphs. It is what provenance, uncertainty, objective, rollout, and validation information must remain visible when generated/fused graph structure is used as evidence about an HC temporal hypergraph.

## Exact source cuts

- `basiralab/DGL main@07bebcb2c4e3d4a8050bdad1083422ec3b86ed54`
- `basiralab/EvoGraphNet master@f49131c3ed0eb792524904e46ad436571c0a5811`
- `basiralab/MultigraphGNet main@3b6b2aa7a9d4f4c402551a6ed6442271d0fcea92`
- `basiralab/SM-netFusion-PY master@0731d26fc88d696e3a78969a96657fb1e66bc223`
- `basiralab/MultiGraphGAN master@7b6d2160daaf07c2462b11a7a621e5ead04cef0b`

## Evidence vocabulary

Each finding below is explicitly separated into:

- **SOURCE OBSERVATION** — directly read from the bound repository README/code;
- **HC TRANSFER INFERENCE** — Four's proposed research/qualification implication for HC;
- **DO NOT TRANSFER** — source-specific assumptions that must not become generic HC topology or scientific fact.

---

## 1. DGL is a methods/teaching map, not primary scientific evidence

### SOURCE OBSERVATION

The 2025 BASIRA `DGL` repository is a Deep Graph Learning course repository. Its README indexes material on graph types and matrices, GCN layers, node/graph embeddings, inductive versus transductive learning, pooling/aggregation, GNN sampling, batch normalization/dropout, permutation invariance/equivariance, expressiveness, graph generation, and generative-model evaluation.

The repository therefore provides a useful method taxonomy and teaching/reference surface. The inspected root does not make it a primary empirical neuroscience result.

### HC TRANSFER INFERENCE

Use DGL as a **qualification checklist / method map**, not as proof that a method is biologically correct or HC-ready.

Candidate controls suggested by the method categories:

- `INDUCTIVE_VS_TRANSDUCTIVE_SCOPE_DECLARED`
- `NODE_IDENTITY_VS_PERMUTATION_SEMANTICS`
- `SAMPLING_POLICY_BOUND_TO_RESULT`
- `POOLING_INFORMATION_LOSS_MEASURED`
- `GENERATION_EVALUATION_MODE_DECLARED`
- `EXPRESSIVENESS_CLAIM_BOUND_TO_MODEL_CLASS`

A graph learner that only works transductively over a fixed node set should not silently be credited with inductive HC generalization.

### DO NOT TRANSFER

Do not treat course organization, human brain-region examples, or standard pairwise-GNN pedagogy as mandatory HC topology.

---

## 2. EvoGraphNet: generated temporal state recursively conditions later generated state

### SOURCE OBSERVATION

The EvoGraphNet README states that time-dependent gGANs are cascaded so that each generator's predicted graph at one timepoint becomes the input to the successor generator for the next timepoint.

The implementation confirms this. In training and validation, the first generator produces `fake_data` for t1. `generator2(fake_data)` then predicts t2 from that generated t1 representation. The code comments explicitly describe `fake_data2` as generated t2 using generated t1.

The fold code creates fresh `generator`, `generator2`, `discriminator`, and `discriminator2` objects inside each fold, so model parameters are reset between folds on the inspected path.

A separate implementation asymmetry is observable: the second-stage identity term is computed with `identity_loss(generator(swapped_data2), data.y2)` while the optimizer subsequently stepped is `optimizer_G2`. The first-stage identity term correctly calls `generator`; the second-stage term also calls `generator`, not `generator2`.

### HC TRANSFER INFERENCE

A model-generated topology that becomes the parent of another prediction needs explicit **rollout lineage**.

Recommended distinctions:

`OBSERVED_T0 != PREDICTED_T1`

`PREDICTED_T1_PARENT_OF_PREDICTED_T2 != OBSERVED_T1_PARENT_OF_PREDICTED_T2`

`ONE_STEP_ACCURACY != FREE_RUNNING_ROLLOUT_ACCURACY`

`PREDICTION_DESCENDANT != NEW_OBSERVATION`

A future HC topology/plasticity predictor should bind, when material:

```text
prediction_id
forecast_time_or_horizon
parent_state_ref
parent_state_class = OBSERVED | DERIVED | PREDICTED | MIXED
model_revision
rollout_depth
uncertainty
calibration_state
training_regime
teacher_forcing_or_free_run_state
provenance
```

Each rollout descendant should retain that a generated predecessor was used. Uncertainty and model-error risk should not reset at each synthetic timepoint merely because the prediction has a graph-shaped representation.

Recommended qualification controls:

- `ONE_STEP_VS_FREE_ROLLOUT`
- `ROLLOUT_DEPTH_SENSITIVITY`
- `GENERATED_PARENT_LINEAGE`
- `TEACHER_FORCING_SHIFT`
- `PREDICTED_GRAPH_NE_OBSERVED_GRAPH`
- `LOSS_WIRING_AUDIT`
- `STAGE_SPECIFIC_ABLATION`

The observed second-stage identity-loss wiring is a useful reminder that reported conceptual losses and executable gradient paths are separate evidence. A qualification harness should verify which parameter family each advertised loss can actually influence.

### DO NOT TRANSFER

Do not transfer the fixed brain-matrix representation, the particular GAN losses, human longitudinal-connectome framing, or the assumption that a predicted topology is an HC plasticity commitment.

---

## 3. MultigraphGNet: template compression and reconstruction are learned/derived states

### SOURCE OBSERVATION

MultigraphGNet represents one subject as `(N_ROI, N_ROI, N_VIEWS)`. Its README describes a many-to-one DGN that maps a multigraph population into a connectional brain template (CBT), followed by a reverse one-to-many U-Net that reconstructs multiple views. The method uses a cyclic/reconstruction objective and then evaluates augmented graph samples in an independent classifier.

The training code creates `DGN` and `UNet` inside each K-fold iteration, so those models are reset per fold. Training-data min/max values are computed from `train_data` and then applied to both train and test data, which is the correct direction for avoiding preprocessing fit on the held-out split on this inspected path.

However, the nominal `test_index` fold is evaluated **inside every training epoch**. `avg_test_mae` is appended each epoch, compared against `best_test_mae`, used to save `best_mae` weights, and drives early stopping after patience exceeds 10.

Therefore, in the literal implementation, that fold participates in model selection and is not a sealed final test set.

### HC TRANSFER INFERENCE

The CBT and reconstructed views should be typed as learned representations:

`MULTIVIEW_INPUT != TEMPLATE`

`TEMPLATE != OBSERVATION`

`RECONSTRUCTED_VIEW != MEASURED_VIEW`

`CYCLE_CONSISTENCY != TRUTH`

`AUGMENTED_SAMPLE != INDEPENDENT_EVIDENCE`

For HC multimodal/hypergraph compression, retain:

```text
source_view_refs[]
source_view_classes[]
compression_objective
compression_model_revision
retained_information_tests[]
lost_information_tests[]
reconstruction_method
reconstruction_uncertainty
synthetic_or_observed_status
provenance
```

A compact template can be operationally useful while still being lossy, objective-conditioned, or blind to minority structure.

Recommended controls:

- `TEMPLATE_INFORMATION_LOSS`
- `VIEW_ABLATION`
- `MINORITY_VIEW_RETENTION`
- `RECONSTRUCTION_NE_OBSERVATION`
- `AUGMENTATION_NE_NEW_EVIDENCE`
- `SEALED_FINAL_HOLDOUT`
- `EARLY_STOPPING_SPLIT_CLASSIFICATION`

Any split used every epoch for patience, model selection, or best-checkpoint choice should be called validation/model-selection evidence, not a blind final test.

### DO NOT TRANSFER

Do not transfer ROI identity, fixed tensor shape, class-specific disease framing, or the assumption that reconstructability proves semantic/causal preservation.

---

## 4. SM-netFusion: fused atlas is explicitly label- and objective-conditioned

### SOURCE OBSERVATION

`SM_netFusion(train_data, train_Labels, Nf, displayResults)` receives training labels explicitly. Its code separates training graphs into two label-defined classes, runs SIMLR clustering separately inside each class, applies similarity-network fusion to cluster-specific graphs, fuses those local atlases into one atlas per class, computes `abs(AC1 - AC2)`, and selects the largest differences as discriminative features.

The function therefore constructs class-conditioned atlases and discriminative features by design. The README likewise describes class-specific feature extraction/clustering, supervised multi-topology cross-diffusion, and identification of discriminative connections.

The implementation also has an operational assumption worth preserving as a test case: after two-way SIMLR clustering, branches with more than one member are fused; otherwise code accesses `Ca1[0]`, `Ca2[0]`, `Cn1[0]`, or `Cn2[0]`. A zero-member cluster is therefore not handled by those branches on the inspected path.

### HC TRANSFER INFERENCE

A fused topology or atlas should bind its **objective and supervision lineage**.

`SUPERVISED_FUSION != NEUTRAL_SUMMARY`

`DISCRIMINATIVE != CAUSAL`

`DISCRIMINATIVE != TRUE`

`CLASS_ATLAS != INDIVIDUAL_OBSERVATION`

When HC creates a fused graph/state from multiple views or experiences, preserve at least:

```text
contributor_refs[]
contributor_classes[]
label_or_objective_conditioning
similarity_metric
clustering_method
cluster_assignment_state
fusion_method
fusion_hyperparameters
feature_or_topology_measures
weighting
normalization_or_transform_lineage
uncertainty_and_disagreement
provenance
```

Recommended controls:

- `FUSION_OBJECTIVE_SENSITIVITY`
- `LABEL_CONDITIONING_DISCLOSURE`
- `TOPOLOGY_MEASURE_WEIGHT_SENSITIVITY`
- `CLUSTER_EMPTY_OR_COLLAPSED_CASE`
- `MINORITY_SIGNAL_RETENTION`
- `ATLAS_NE_OBSERVATION`
- `DISCRIMINATIVE_NE_CAUSAL`
- `UNSUPERVISED_VS_SUPERVISED_FUSION_COMPARATOR`

If a fused representation changes when the label/task objective changes, that is not automatically a defect. It is evidence that the object is task-conditioned and must be represented as such.

### DO NOT TRANSFER

Do not copy class labels, disease atlases, fixed two-class clustering, or a particular diffusion/fusion rule into generic HC topology.

---

## 5. MultiGraphGAN: topology preservation is metric-specific and cluster assignment is part of the model

### SOURCE OBSERVATION

MultiGraphGAN jointly predicts multiple target graphs from one source graph. The README describes source-graph embedding/clustering, cluster-specific target decoders, and a topology-aware loss.

The implementation computes source embeddings and runs SIMLR clustering during training. Cluster-specific generators are then intended to operate on the assigned source subset.

The topology helper reconstructs a fixed 35x35 symmetric matrix from vectorized data, converts it to a NetworkX graph and then to an undirected graph, and computes closeness, betweenness, and eigenvector centrality. In the generator training path, the local topology loss shown in the inspected code uses **closeness centrality** (`fake_topology[0]` versus `real_topology[0]`) plus a global L1 reconstruction term.

A concrete implementation defect is visible in the cluster-specific generator loop. `cluster_index_list` is assigned inside the earlier discriminator loop for each `par`. In the subsequent generator loop, `for par in range(nb_clusters)` does not recompute `cluster_index_list` before using it. On the literal path, generator-cluster iterations reuse whichever cluster index list remained from the prior discriminator loop (the last discriminator cluster).

### HC TRANSFER INFERENCE

“Topology-preserving” is incomplete unless the preserved topology **metric family and preprocessing/projection** are declared.

`TOPOLOGY_LOSS_LOW != ALL_TOPOLOGY_PRESERVED`

`CENTRALITY_MATCH != EDGE_IDENTITY_MATCH`

`CENTRALITY_MATCH != CAUSAL_STRUCTURE_MATCH`

`CLUSTER_ASSIGNMENT != OBSERVED_TYPE`

For HC learned topology, bind:

```text
topology_representation
projection_or_symmetrization
metric_family[]
metric_weights
clustering_or_partition_method
cluster_assignment_uncertainty
loss_objectives[]
loss_weights
preserved_property_tests[]
violated_property_tests[]
provenance
```

Recommended controls:

- `TOPOLOGY_METRIC_FAMILY_SENSITIVITY`
- `SYMMETRIZATION_OR_DIRECTION_LOSS`
- `CENTRALITY_NE_STRUCTURAL_EQUIVALENCE`
- `CLUSTER_ASSIGNMENT_PERTURBATION`
- `CLUSTER_INDEX_LINEAGE`
- `LOSS_TO_PARAMETER_PATH_AUDIT`
- `LOCAL_VS_GLOBAL_TOPOLOGY_DISAGREEMENT`
- `GENERATED_GRAPH_NE_OBSERVED_GRAPH`

The observed stale/reused `cluster_index_list` path is particularly relevant to HC qualification: loop/control-flow lineage must be tested, not inferred from variable names such as “cluster-specific.”

### DO NOT TRANSFER

Do not transfer the 35-node hardcoding, forced symmetric/undirected projection, centrality selection, cluster count, or target-domain assumptions into generic HC.

---

## 6. Cross-source synthesis for HC qualification

Across these sources, four representation classes must remain distinct:

1. **observed graph/state** — directly measured or admitted evidence;
2. **derived/fused/template graph** — computed from observations under an estimator/fusion/objective;
3. **predicted/generated/reconstructed graph** — model output about unavailable/future/alternate state;
4. **committed HC topology/plasticity state** — an authorized internal architecture/runtime change.

The following promotions are prohibited without a separately justified transition:

`DERIVED_GRAPH -> OBSERVED_GRAPH`

`GENERATED_GRAPH -> OBSERVED_GRAPH`

`PREDICTED_GRAPH -> COMMITTED_TOPOLOGY`

`FUSED_ATLAS -> INDIVIDUAL_CURRENT_STATE`

`DISCRIMINATIVE_FEATURE -> CAUSAL_MECHANISM`

`LOW_RECONSTRUCTION_ERROR -> SEMANTIC_PRESERVATION`

A useful generic lineage object for future qualification work is:

```text
GRAPH_STATE_LINEAGE {
  graph_state_ref
  state_class = OBSERVED | DERIVED | FUSED | TEMPLATE | PREDICTED | GENERATED | RECONSTRUCTED | COMMITTED
  parent_refs[]
  estimator_or_model_revision
  objective_or_label_conditioning
  transforms[]
  topology_metrics[]
  rollout_depth
  uncertainty
  validation_scope
  provenance
}
```

This is a research proposal, not a canonical machine schema.

## 7. Candidate hostile-control bundle

Add to the research qualification backlog:

- `PREDICTION_ROLLOUT_LINEAGE`
- `ONE_STEP_VS_FREE_ROLLOUT`
- `GENERATED_PARENT_NE_OBSERVED_PARENT`
- `TEMPLATE_INFORMATION_LOSS`
- `RECONSTRUCTED_NE_MEASURED`
- `SEALED_FINAL_HOLDOUT`
- `MODEL_SELECTION_SPLIT_DISCLOSURE`
- `FUSION_OBJECTIVE_SENSITIVITY`
- `LABEL_CONDITIONING_DISCLOSURE`
- `MINORITY_SIGNAL_RETENTION`
- `TOPOLOGY_METRIC_FAMILY_SENSITIVITY`
- `SYMMETRIZATION_DIRECTION_LOSS`
- `CLUSTER_EMPTY_OR_COLLAPSED_CASE`
- `CLUSTER_INDEX_LINEAGE`
- `LOSS_TO_PARAMETER_PATH_AUDIT`
- `DGL_INDUCTIVE_VS_TRANSDUCTIVE_SCOPE`

These controls complement, rather than replace, Four's earlier estimator/null-family, transform-lineage, target-conditioned selection, federation, and graph-to-authority controls.

## Current disposition

**KEEP as research/provenance and qualification input.**

No source implementation is adopted as HC cognition. No source-generated graph is promoted to observation. No human atlas, hemisphere, ROI, or disease-class packaging is transferred into the generic HC template.

The strongest transferable lesson is that graph-shaped state needs explicit **epistemic class + lineage + objective + validation scope**. Shape alone does not tell the HC whether a graph was measured, fused, predicted, reconstructed, generated, or committed.