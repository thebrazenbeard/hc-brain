# Federated Ancestry and Model-Graph Control Matrix — 2026-09-09

Status: research/adversarial transfer matrix; noncanonical.

Companion to:

`FEDERATED_AND_MODEL_GRAPH_IMPLEMENTATION_SCOUT_2026-09-09.md`

## Governing distinctions

```text
MODEL_INSTANCE_COUNT != INDEPENDENT_EVIDENCE_COUNT
MODEL_GRAPH != WORLD_GRAPH
MODEL_GRAPH != OBSERVED_CONNECTOME
MODEL_GRAPH != HC_RUNTIME_HYPERGRAPH
DISJOINT_UNION != SEMANTIC_UNIFICATION
SHARED_UPDATE != INDEPENDENT_CORROBORATION
FEDERATED_CONVERGENCE != EXTERNAL_WORLD_TRUTH
REPLICA_DIVERSITY != INDEPENDENT_ANCESTRY
CENTER_ESTIMATE != FULL_DISTRIBUTION
GNN_LABEL != SOURCE_GRAPH_MESSAGE_PASSING
DOCUMENTED_METHOD_CLAIM != OBSERVED_CODE_PATH
```

## Source transfer matrix

| Source | Observed/documented mechanism | Shared/correlated ancestry introduced | Safe HC transfer hypothesis | Explicit non-transfer boundary | Hostile control |
|---|---|---|---|---|---|
| uGNN | heterogeneous NN architectures projected into model graphs; disjoint-union container; shared GNN/theta update mechanism | shared model-graph optimizer and parameter groups | bounded model introspection / heterogeneous model representation | model graph is not world or HC runtime topology | place unrelated models in same container; verify no semantic edge appears |
| UnifiedFL | current inspected entrypoint reuses uGNN-like core; precomputed sample clusters; one unified `UGNN_WS` training object | same core update family across model graphs; sample-cluster coupling | ancestry-aware multi-model optimization study | README dynamic federation not upgraded to observed code | require exact runtime evidence for claimed post-round clustering |
| RepFL | anchor plus same-architecture replicas from perturbed anchor-data lineage; replica/server aggregation | same global initialization, overlapping data ancestry, shared aggregation | robustness/diversity candidates with explicit genealogy | replica vote count is not witness count | make replicas identical; aggregation identity case and corroboration weight must expose dependence |
| Fed2M | heterogeneous client models, shared-layer averaging, cross-client representation sampling, global-centeredness pressure | parameter averaging + explicit cross-client representation alignment | provenance-preserving multi-view alignment | converged CBTs/representations are not independent observations | over-strengthen alignment until outputs agree; evidence independence must remain low |
| FedGmTE-Net | sample-weighted global model aggregation/rebroadcast across hospitals | global initialization + repeated aggregate/rebroadcast ancestry | distributed optimization with ancestry ledger | post-round client agreement is not independent forecast evidence | compare pre-federation vs post-federation correlation and preserve round ancestry |
| FedGmTE-Net-plus | same global ancestry plus FedDyn and two-step imputation machinery | federation ancestry + imputed-data ancestry | explicit imputation/federation lineage | imputed value is not observed value; FedDyn does not restore independence | mask observations, impute, federate, then test whether derived values retain dual lineage |

## Representation-plane matrix

| Object called a graph | Native meaning | HC classification if imported as evidence/mechanism | Must not be silently reclassified as |
|---|---|---|---|
| uGNN/UnifiedFL model graph | neural-network computation/parameter structure | `MODEL_IMPLEMENTATION_GRAPH` | `WORLD_GRAPH`, `SEMANTIC_GRAPH`, `HC_RUNTIME_HYPERGRAPH` |
| uGNN/UnifiedFL disjoint union | container of several model graphs | `MULTI_MODEL_CONTAINER_GRAPH` | semantic fusion/correspondence graph |
| Fed2M one-node/self-loop GCN graph | computational carrier for vectorized connectome features | `COMPUTATIONAL_MESSAGE_PASSING_GRAPH` | source connectome topology |
| Fed2M reconstructed CBT | generated population/reference graph | `GENERATED_OR_DERIVED_GRAPH` | direct subject observation |
| FedGmTE predicted connectome | forecast/generated trajectory state | `PREDICTED_GRAPH` | observed future graph |
| HC temporal hypergraph | typed attributed runtime relation/coalition structure | `HC_RUNTIME_TOPOLOGY` | any source-native graph merely because both use graph math |

## Ancestry dimensions HC should preserve

A multi-model or federated result should be able to declare, when material:

```text
source_model_ref
architecture_family_ref
parent_model_or_checkpoint_refs[]
initialization_ancestry[]
training_dataset_lineage[]
replica_or_derivative_parent_ref
shared_optimizer_or_update_family_ref
shared_parameter_group_refs[]
federation_round_refs[]
aggregation_operator_ref
cross_model_regularization_refs[]
distillation_or_alignment_refs[]
imputation_or_synthetic_data_refs[]
independent_holdout_evidence_refs[]
result_provenance
```

The point is not to maximize metadata. The point is to prevent this invalid transformation:

```text
three correlated descendants agree
        ->
three independent pieces of evidence agree
```

## Independence is claim-relative

Two models can share ancestry while still provide partially independent evidence for some questions.

Example:

- same initialization;
- independently collected sensors after initialization;
- no later parameter exchange;
- distinct noise/failure modes.

The correct question is not globally:

`ARE_THE_MODELS_INDEPENDENT?`

It is:

`HOW_INDEPENDENT_IS_THE_EVIDENCE_FOR_THIS_CLAIM_GIVEN_THE_RELEVANT_SHARED_ANCESTRY?`

Candidate evidence-dependence classes for future research/testing:

- `COMMON_SOURCE_DUPLICATE`
- `SHARED_INITIALIZATION_ONLY`
- `SHARED_DATA_LINEAGE`
- `SHARED_UPDATE_ANCESTRY`
- `FEDERATED_DESCENDANT`
- `REPLICA_OR_PERTURBED_DESCENDANT`
- `DISTILLED_OR_ALIGNED_DESCENDANT`
- `PARTIALLY_INDEPENDENT_EVIDENCE_PATH`
- `INDEPENDENT_WITHIN_DECLARED_SCOPE`
- `DEPENDENCE_UNKNOWN`

These are research vocabulary, not canonical machine statuses yet.

## Hostile control suite

### FMA-01 — Identical replica aggregation

Setup:

- one anchor + R replicas;
- identical parameters;
- identical data and no local update.

Expected:

An ordinary equal-weight aggregation operator preserves the input tensor exactly unless a scale transformation is explicitly declared.

Catches:

- double normalization;
- accidental shrinkage;
- count-dependent scaling.

### FMA-02 — Shared-ancestry corroboration illusion

Setup:

- create three models from one common checkpoint;
- repeatedly average them;
- provide overlapping data;
- collect agreeing outputs.

Expected:

Agreement may increase confidence only according to a dependence-aware rule; it must not be counted as three independent observations.

### FMA-03 — Independent-sensor / shared-model contrast

Setup:

Compare:

A. three model replicas over the same observation;
B. one model receiving three genuinely independent observations.

Expected:

Evidence accounting distinguishes model multiplicity from observation multiplicity.

### FMA-04 — Disjoint-union semantic illusion

Setup:

- graphify two unrelated models;
- place them in one PyG/disjoint container.

Expected:

No semantic correspondence, causal link, or HC runtime relationship is created solely from container membership.

### FMA-05 — Shared-theta induced agreement

Setup:

- two initially different model graphs;
- increasingly strong shared parameter-group updates;
- measure output convergence.

Expected:

Provenance records that convergence is partly update-induced.

### FMA-06 — Source-topology absence

Setup:

Use a GNN whose actual message-passing graph is self-loop-only while source-connectome values are encoded as feature vectors.

Expected:

System states:

`COMPUTATIONAL_GNN_USED = true`

without claiming:

`SOURCE_CONNECTOME_MESSAGE_PASSING_USED = true`.

### FMA-07 — Generated graph versus measured graph

Setup:

Generate a graph by super-resolution/template/prediction.

Expected:

Generated edges retain generation/inference provenance and cannot be silently relabeled measured.

### FMA-08 — Center-collapse

Setup:

Create two well-separated source modes with a center lying between them.

Expected:

A CBT/mean/median/template may exist but does not erase source-mode alternatives or become a representative observed individual.

### FMA-09 — Alignment-caused agreement

Setup:

Add a strong global-centeredness/cross-client representation loss.

Expected:

Later agreement is tagged with alignment ancestry and does not count as independent corroboration of the aligned relation.

### FMA-10 — Federation-round lineage

Setup:

Track clients before and after several FedAvg/FedDyn rounds.

Expected:

A result can identify the global checkpoint/aggregation rounds from which it descends.

### FMA-11 — Imputation plus federation

Setup:

- remove a longitudinal observation;
- impute it;
- train/federate on completed trajectories;
- later produce a prediction influenced by the imputed value.

Expected:

Lineage preserves both `IMPUTED` and `FEDERATED_DESCENDANT` dependencies rather than promoting the value to observed evidence.

### FMA-12 — README/code mismatch

Setup:

README claims runtime mechanism X; inspected default entrypoint does not expose X.

Expected:

Status remains:

`DOCUMENTED_SOURCE_CLAIM`

plus

`IMPLEMENTATION_NOT_ESTABLISHED_IN_INSPECTED_PATH`

rather than `OBSERVED_IMPLEMENTATION`.

### FMA-13 — Model-graph self-authority attack

Setup:

A model-graph analyzer identifies a parameter transformation with high predicted utility and writes the transformation back to the live model.

Expected:

Analysis/proposal does not bypass canonical protected-update/authority/qualification gates.

### FMA-14 — Model-graph representation loss

Setup:

Graphify a model using a projection that omits an operation, weight-tying constraint, normalization state, recurrent dependency, or other behaviorally material element.

Expected:

The graph projection's claim ceiling reflects its representational coverage; downstream reasoning cannot assume full behavioral equivalence to the original model.

## Static implementation observations requiring further verification

### RepFL double-normalization candidate

Observed source path:

`client/SGRepGenerator.py::aggregate_replicas`

Static behavior:

1. each input tensor is multiplied by `1/(R+1)`;
2. those tensors are then averaged by `.mean()` over `R+1` members.

Candidate identity failure:

For identical inputs `P`, output is `P/(R+1)` rather than `P`.

Status:

`OBSERVED_STATIC_CODE_DEFECT_CANDIDATE`

Not yet:

- executed in this research pass;
- reconciled against the paper's pseudocode;
- established as the exact path used for all published results.

### UnifiedFL dynamic clustering implementation gap

Source claim:

README describes communication-round Euclidean GNN-parameter clustering.

Inspected default training path:

- precomputed cluster-index files;
- one unified model object;
- epoch-based unified training;
- no post-round cluster recomputation observed in the entry point;
- targeted code searches did not locate the claimed Euclidean clustering implementation.

Status:

`DOCUMENTED_METHOD_CLAIM + OBSERVED_INSPECTED_CODE_GAP`

Do not generalize beyond the inspected cut/path without additional evidence.

## Promotion recommendations

### Candidate for future canonical evidence/provenance design

`SHARED_MODEL_ANCESTRY_MUST_REDUCE_OR_QUALIFY_CORROBORATION_WHEN_RELEVANT`

Reason:

Repeatedly supported across replica, shared-theta, FedAvg, FedDyn, and alignment mechanisms.

Promotion still requires Noah/Warden synthesis and machine-contract placement.

### Candidate for future model-analysis contract

`MODEL_GRAPH_REPRESENTATION_HAS_EXPLICIT_PROJECTION_SCOPE_AND_LOSS`

Reason:

uGNN/UnifiedFL demonstrate useful graphification, but graphification can omit or transform behaviorally meaningful architecture semantics.

### Keep research-only for now

- exact independence-weight formula;
- exact ancestry-class vocabulary;
- model-graph schema;
- correlation discount function;
- specific federated optimizer choice;
- any claim that one BASIRA method is directly suitable as HC runtime machinery.

## Current disposition

`RESEARCH_CONTROL_PACKAGE / HIGH_TRANSFER_VALUE / NO_DIRECT_ARCHITECTURE_PROMOTION`
