# BASIRA BGSR Exemplar Synthesis and Index Lineage — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/BGSR-PY@master/README.md`
- `basiralab/BGSR-PY@master/BGSR.py`
- `basiralab/BGSR-PY@master/atlas.py`
- `basiralab/BGSR-PY@master/BGSR-demo.py`

## DOCUMENTED source behavior

BGSR is described as brain-graph super-resolution. The repository describes a pipeline that estimates a connectional brain template (CBT), computes residual/topological descriptors for low-resolution graphs, fuses similarity information, selects similar training subjects, and predicts high-resolution features from high-resolution training examples.

## OBSERVED implementation behavior

`atlas.py` vectorizes low-resolution training graphs, clusters them with SIMLR, builds cluster-specific fused networks with similarity-network fusion (SNF), and fuses those cluster networks into a global CBT.

`BGSR.py` computes residual graphs relative to the CBT, derives degree/closeness/betweenness descriptors, learns/fuses similarity matrices, selects `kn` similar entries, copies their rows from `HR_features`, and returns the arithmetic mean of those selected HR rows as `pHR`.

Therefore the predicted high-resolution output is exemplar-derived synthesis. It is not a direct high-resolution measurement of the test subject.

### Positional-index concern

In `BGSR-demo.py`, leave-one-out cross-validation removes the test subject from the low-resolution `train_data`/`train_labels`, but the call to `BGSR` passes the full `HR_data_Featurematrix` rather than an equivalently filtered/remapped HR matrix.

Inside `BGSR`, neighbor positions are derived from similarity matrices whose rows index the filtered low-resolution training array, and those positions are then used directly against `HR_features`.

OBSERVED: the inspected code does not pass an explicit stable subject identifier or positional remapping from filtered LR index space to original HR index space.

INFERRED/HYPOTHESIS: unless the positional spaces happen to remain aligned for a particular test index, the selected HR exemplar may correspond to a different subject than the selected LR training entry; for some leave-one-out positions this could also make the held-out subject addressable through the unfiltered HR array. Execution with traceable subject IDs is required to establish exact runtime consequences.

## HC lessons

`SUPER_RESOLVED_DETAIL != OBSERVED_DETAIL`

`EXEMPLAR_SYNTHESIS != INDEPENDENT_MEASUREMENT`

`SOURCE_COHORT != INSTANCE_STATE`

`FILTERED_POSITIONAL_INDEX != STABLE_ENTITY_ID`

`REORDERED_INDEX != ORIGINAL_INDEX`

`POSITIONAL_ALIGNMENT != IDENTITY_ALIGNMENT`

When one representation is filtered, sorted, clustered, deduplicated, batched, or reordered while a related representation is not transformed identically, downstream positional lookup can silently bind evidence to the wrong entity.

## Transfer candidates

1. Generated/super-resolved outputs should retain the exact exemplar/source set, source weights, source cohort/version, and transformation lineage.
2. Stable entity IDs should be preferred across multi-view transforms; positional indices require an explicit index-map/version whenever filtering or reordering occurs.
3. Qualification should include permutation/filtering tests that prove cross-view identity remains correct after subset operations.
4. A high-resolution-looking representation produced by averaging exemplars remains generated evidence even if it has the same shape as measured high-resolution data.

## Scope and caution

The positional-index issue is a static implementation finding and inferred failure mode. This record does not claim that every published BGSR experiment suffered leakage/misbinding or quantify any impact. That requires reproducing the exact experimental data path and instrumenting subject identity through execution.
