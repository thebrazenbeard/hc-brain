# Nilearn + brainGraph Estimator / Null-Model Qualification Scout — 2026-09-09

Status: research/provenance only. This note treats Nilearn and brainGraph primarily as evaluation/qualification method sources. No source code is copied and neither package is proposed as the HC runtime topology.

## Exact source bindings

- `nilearn/nilearn` `main@c537ff84da68eea1929b9bb7b089f97cca39e682`
- `cwatson/brainGraph` `master@a0d13aea831fbb708c9fb984816e9edda616bbdd`

Read depth includes Nilearn connectivity-matrix and permutation-test code plus brainGraph graph-construction/threshold/null-graph code and package documentation.

## 1. Nilearn — one observation set can legitimately yield multiple connectivity representations

### OBSERVED code behavior

`nilearn/connectome/connectivity_matrices.py` exposes `ConnectivityMeasure` with several distinct `kind` values:

- covariance;
- correlation;
- partial correlation;
- precision;
- tangent.

The default covariance estimator is Ledoit-Wolf shrinkage unless another compatible estimator is supplied. Correlation is computed from standardized signals and the resulting covariance; precision is matrix inversion of covariance; partial correlation is derived from precision; tangent representation is defined relative to a fitted group geometric mean and whitening transform.

For non-tangent kinds, `mean_` is the arithmetic mean of the corresponding matrices and is explicitly symmetrized against numerical instability. For tangent space, `mean_` is a geometric mean of subject covariances and transformed subjects are logarithmic displacements relative to that reference.

Vectorization is another explicit transform. If confounds are supplied, Nilearn only performs this second-level confound cleaning after connectivity matrices are vectorized.

### HC transfer

The same underlying measurements can support multiple legitimate relation representations depending on the estimator and transform.

`OBSERVATIONS != CONNECTIVITY_ESTIMATE`

`COVARIANCE != CORRELATION != PARTIAL_CORRELATION != PRECISION != TANGENT_DISPLACEMENT`

`GROUP_GEOMETRIC_REFERENCE != INDIVIDUAL_CURRENT_STATE`

`VECTORIZED_CONNECTIVITY != RAW_CONNECTIVITY_MATRIX`

`CONFOUND_CLEANED_REPRESENTATION != UNTRANSFORMED_EVIDENCE`

For HC topology/evidence qualification, any claim derived from an inferred graph should therefore bind at least:

- source observation identity/window;
- preprocessing/standardization;
- estimator identity/revision;
- estimator parameters;
- relation kind;
- reference population/state where applicable;
- confound model where applicable;
- vectorization/projection transforms;
- currentness;
- uncertainty/provenance.

A downstream node or edge should not silently inherit the epistemic class `OBSERVED` merely because a well-tested estimator produced it.

### Estimator-sensitivity control

Given one frozen observation set:

1. build several admissible connectivity representations;
2. run the same downstream graph/topology claim against each;
3. record agreement, disagreement, rank changes, and sign changes;
4. preserve estimator dependence as evidence rather than picking the most convenient representation post hoc.

Candidate statuses:

- `ESTIMATOR_ROBUST_WITHIN_TESTED_FAMILY`
- `ESTIMATOR_SENSITIVE`
- `REFERENCE_DEPENDENT`
- `PREPROCESSING_SENSITIVE`
- `UNRESOLVED`

These are proposed research statuses, not canonical enums yet.

## 2. Nilearn permutation testing — null evidence is an explicit generated distribution

### OBSERVED code behavior

`nilearn/mass_univariate/permuted_least_squares.py` builds permutation-derived null distributions and returns objects including original-data test statistics, family-wise corrected p-values, and the corresponding maximum-statistic null distributions. Confounding variables are explicitly residualized/orthonormalized before the original and permutation regressions. A supplied random state drives permutation seeds.

### HC transfer

A statistical/null-model challenge should preserve the null-generating procedure as part of the evidence.

`NULL_DISTRIBUTION != OBSERVED_WORLD_DISTRIBUTION`

`P_VALUE != EFFECT_MAGNITUDE`

`CORRECTED_SIGNIFICANCE != CAUSAL_MECHANISM`

`PERMUTATION_RESULT != UNIVERSAL_GRAPH_TRUTH`

For HC qualification, an apparent graph/topology feature should be challengeable against a declared null family. The result means only that the observed/statistical score is unusual relative to that tested null construction and sampling procedure.

A stronger qualification artifact would bind:

```text
NULL_MODEL_EVIDENCE {
  source_observation_refs
  tested_claim_or_metric
  null_generator
  preserved_properties[]
  randomized_properties[]
  nuisance_or_confound_model
  random_seed_lineage
  permutation_or_sample_count
  statistic
  correction_family
  null_distribution_ref
  result
  provenance
}
```

This is a research sketch, not a canonical HC schema proposal yet.

## 3. brainGraph — graph construction itself is a model choice

### DOCUMENTED / OBSERVED behavior

brainGraph supports several brain-network sources and many igraph-compatible graph analyses. More importantly for HC, `create_mats()` exposes multiple thresholding families:

- `raw`;
- `mean`;
- `density`;
- `consistency`;
- `consensus`.

The code makes those choices materially different:

- raw thresholding keeps values above a direct threshold and then symmetrizes;
- mean/SD thresholding derives a population statistic before retention;
- density thresholding selects thresholds needed to produce requested densities;
- consistency uses coefficient-of-variation structure;
- consensus retains entries according to how many/what fraction of subjects exceed a matrix threshold within declared groups.

brainGraph also preserves graph-level metadata such as weighting and threshold in its object history/documentation.

### HC transfer

Thresholding is not a neutral formatting step.

`THRESHOLDED_GRAPH != SOURCE_RELATION_MATRIX`

`CONSENSUS_EDGE != UNIVERSAL_EDGE`

`DENSITY_MATCHED_GRAPH != SAME_INFORMATION_GRAPH`

`CONSISTENCY_FILTERED_EDGE != HIGH_IMPORTANCE_EDGE`

`SYMMETRIZED_GRAPH != DIRECTIONAL_SOURCE_RELATION`

A graph/topology object should therefore preserve the construction policy and discarded-information lineage. If an HC implementation generates a sparse working projection from richer relation state, the projection is a derived operational representation rather than the authoritative source relation set.

### Threshold-sensitivity hostile test

Freeze one source relation matrix and create several admissible thresholded graphs. Compute candidate hub/community/efficiency/critical-node claims across the threshold family.

If the conclusion changes materially, the correct output is estimator/threshold sensitivity, not a cherry-picked graph claim.

`ONE_THRESHOLD_SUPPORT != THRESHOLD_ROBUSTNESS`

## 4. brainGraph null graphs — the null family determines what is being challenged

### OBSERVED code behavior

`R/random_graphs.R` provides multiple null/random graph constructions.

`sim.rand.graph.par()` can generate random graphs preserving degree sequence; when requested it invokes a clustering-aware rewiring path intended to approach the input graph's clustering coefficient as well. For connected graphs without clustering matching, it can sample from the observed degree sequence. For disconnected inputs it rewires while retaining degree sequence.

`sim.rand.graph.hqs()` uses the Hirschberger-Qi-Steuer method to generate random covariance matrices with distributional characteristics derived from observed covariance, then converts those to correlation graphs.

These are different null hypotheses because they preserve and randomize different properties.

### HC transfer

`RANDOMIZED_GRAPH != ONE_UNIVERSAL_NULL`

`DEGREE_PRESERVING_NULL != DEGREE_AND_CLUSTERING_PRESERVING_NULL`

`COVARIANCE_MATCHED_NULL != TOPOLOGY_REWIRE_NULL`

`SIGNIFICANT_VS_NULL_A != SIGNIFICANT_VS_ALL_PLAUSIBLE_NULLS`

For HC topology qualification, the tested null must be claim-relative. If a proposed mechanism claims an effect beyond degree distribution, a degree-preserving null may be appropriate; if clustering is a nuisance/property to preserve, a different null is needed. No single randomized graph family is a universal adversary.

## 5. brainGraph metrics — metric labels do not create ontology

The package supports broad graph measures including degree, betweenness, efficiency, modularity, small-world measures, rich-club normalization, GLM/group comparison, permutation analysis, network-based statistics, mediation, and bootstrap procedures.

These are useful evaluator tools, but they remain mathematical summaries of a constructed graph.

`HIGH_CENTRALITY != COGNITIVE_AUTHORITY`

`HIGH_BETWEENNESS != SEMANTIC_BROKER`

`RICH_CLUB_MEMBER != PROTECTED_CORE`

`MODULE != HC_SUBSYSTEM_IDENTITY`

`SMALL_WORLD_SCORE != INTELLIGENCE`

A topological metric can nominate hypotheses, perturbation targets, or resource-critical paths. It does not itself establish cognition, meaning, identity, causal necessity, or authority.

## 6. Joint qualification pattern for HC

Nilearn and brainGraph together suggest a stronger evaluation pipeline:

```text
frozen observations
  -> declared preprocessing
  -> estimator family
  -> relation representation(s)
  -> declared graph construction / threshold family
  -> graph metric / hypothesis
  -> matched null model(s)
  -> perturbation / ablation where applicable
  -> sensitivity envelope
  -> bounded claim
```

The output should preserve a **model-dependence envelope**, not just a winning number.

Candidate machine concepts for later review:

```text
GRAPH_INFERENCE_PROVENANCE {
  source_observation_refs
  estimator_ref
  estimator_parameters
  relation_kind
  preprocessing_refs
  threshold_or_projection_rule
  null_model_refs[]
  metric_refs[]
  sensitivity_results[]
  claim_ceiling
  provenance
}
```

Again, this is a research sketch, not yet canonical architecture.

## 7. Hostile controls worth promoting into qualification work

1. **Estimator flip:** the same frozen observations produce a hub under correlation but not partial correlation. Report estimator sensitivity; do not silently pick one.
2. **Reference drift:** a tangent-space relation changes because the fitted reference population changes. Preserve reference dependence and do not call the displacement a direct observation.
3. **Threshold flip:** centrality/module claims change across reasonable threshold/density families. Lower the claim ceiling.
4. **Null-family flip:** a feature beats degree-preserving nulls but not degree+clustering-matched nulls. State exactly which rival family was rejected.
5. **Metric disagreement:** degree, betweenness, participation, and perturbation effect identify different "important" nodes. Preserve plural evidence dimensions.
6. **Symmetrization loss:** source relation is directional but graph-construction path symmetrizes it. The transformed graph cannot support an unqualified directional claim.
7. **Confound dependence:** a conclusion changes after declared confound cleaning. Preserve both the confound model and the sensitivity result.
8. **Permutation-budget sensitivity:** a borderline corrected result changes materially with null-sample count/seed family. Preserve calibration uncertainty.
9. **Graph-to-action leak:** high centrality is supplied as if it were action priority or authority. The HC must reject the promotion.
10. **Null-to-causality leak:** statistical rarity under a declared null is supplied as proof of causal mechanism. The HC must retain the causal claim as unresolved without intervention/mechanistic evidence.

## 8. Recommended HC use

**Promote as qualification methodology before promoting as cognition.**

The strongest immediate transfer is not a new cognitive node. It is an implementation/evaluation discipline for:

- topology-evidence qualification;
- multimodal/connectivity estimator sensitivity;
- graph-projection provenance;
- learned-topology/plasticity validation;
- hub/coalition-criticality claims;
- compression/coarsening validation;
- generated-topology admission;
- architecture-update regression testing.

The HC should be able to say not merely `this graph property is high`, but:

> `this property is supported under these estimators, preprocessing choices, graph constructions, metrics, null families, and perturbations; here is where the conclusion changes.`

That is a much stronger epistemic object.

## 9. Non-transfer boundary

Nilearn and brainGraph are human-neuroimaging/statistical tooling. Their atlases, hemispheric labels, ROI choices, MRI assumptions, and human anatomical packaging are not HC topology requirements.

`HUMAN_ATLAS != HC_NODE_TAXONOMY`

`NEUROIMAGING_CONNECTIVITY_ESTIMATE != HC_RUNTIME_HYPEREDGE`

`HUMAN_HEMISPHERE_METADATA != HC_HEMISPHERIC_ARCHITECTURE`

The transferable layer is estimator/statistical discipline, not anatomical imitation.

## Disposition

**KEEP as research/provenance. HIGH VALUE for qualification architecture.**

Recommended next step: compare these estimator/null-model controls against current `HC_CONFORMANCE_SUITE_V1` and identify the smallest non-duplicative machine-readable additions needed for topology-evidence qualification.