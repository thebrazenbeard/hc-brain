# BASIRA Federated Replica, Hierarchical Integration, and Relational Reasoning Scour — 2026-09-09

Status: research/provenance only. This file records source-supported computational patterns, static code-review findings, and HC transfer limits. It is not canonical architecture by itself.

## Sources inspected

- `basiralab/RepFL`
- `basiralab/Fed2M`
- `basiralab/Dual-HINet`
- `basiralab/MSRGNN`
- `basiralab/DGL` as an educational/source-discovery resource
- related context from earlier EvoGraphNet, SG-Net, and connectional-template work

## RepFL — replicas are dependent evidence, not new independent sources

DOCUMENTED from the README: RepFL creates replicas of participating clients by copying model architecture and perturbing local training datasets, then aggregates multiple local models for graph super-resolution in a federated setting.

OBSERVED from `client/SGRepGenerator.py`:

- each anchor can recursively instantiate a configured number of replica generators;
- replicas are initialized from the same global model;
- replica training data are produced by removing subsets from the anchor's copied source/target training data;
- anchor and replicas are later aggregated.

This creates deliberately correlated learners. That may improve optimization/diversity, but it must not be counted as independent epistemic corroboration.

`REPLICA != INDEPENDENT_SOURCE`

`PERTURBED_COPY != INDEPENDENT_CORROBORATION`

`MORE_REPLICAS != MORE_INDEPENDENT_EVIDENCE`

### RepFL static code-review findings

OBSERVED from the current default-branch snapshot:

1. In `SGRepGenerator.aggregate_replicas`, each anchor/replica parameter tensor is first multiplied by `1/(1 + NUMBER_REPLICAS)`, then the stacked tensors are passed through `mean(dim=0)`. As written, this appears to apply an additional division by the number of stacked models instead of a conventional equal-weight mean. HYPOTHESIS: the aggregate is scaled by an extra factor of `1/(1 + NUMBER_REPLICAS)` relative to an ordinary arithmetic mean.

2. In both `set_training_data` and `test`, target graphs are constructed by passing `X_train_source` / `X_test_source` into `convert_list_of_vectors_to_graphs(..., resolution=self.resolution)` rather than the corresponding target arrays.

3. `utils/preprocess.py::convert_vector_to_graph` constructs an adjacency matrix at the requested `resolution`, but then hard-codes `edge_attr = ...view(1225, 1)`, i.e. `35 * 35`, independent of requested resolution. For a 160x160 or 268x268 matrix this static shape is incompatible.

The README describes 35 -> 160/268 graph super-resolution. The source-data vector in `read_and_preprocess_files` has 595 features (35 choose 2), while the 160 and 268 target vectors have 12,720 and 35,778 features respectively. Passing the 595-feature source vector into target-resolution lower-triangle assignment also appears dimensionally incompatible with the target-resolution matrix.

These are static code-review findings on the inspected snapshot. They do not invalidate the paper's reported experiments, which may have used different code/revisions. They do establish that repository/paper claims cannot substitute for execution qualification of the specific artifact under consideration.

`PUBLISHED_METHOD != VERIFIED_CURRENT_REPOSITORY_EXECUTION`

Recommended falsification: run a minimal fixture for resolutions 35, 160, and 268 and record shape behavior; separately compare equal-weight aggregate output with a direct arithmetic mean.

## Fed2M — convergence to a global center is not epistemic consensus

DOCUMENTED from the README: Fed2M learns hospital-specific local connectional brain templates from different modalities and resolutions, aggregates shared learned mappings across hospital-specific GNNs, and uses a loss that encourages global centeredness/consistency among local templates.

HC relevance: distributed components can coordinate toward a shared representational reference while retaining local computation.

Boundary:

`CONVERGENCE_TO_SHARED_CENTER != CORRECTNESS`

`CONSISTENCY_LOSS != TRUTH`

`GLOBAL_TEMPLATE != LOCAL_CURRENT_STATE`

A consensus/center objective can be useful for normalization while still suppressing rare or locally valid evidence.

## Dual-HINet — learned hierarchy is not ontology

DOCUMENTED from the README: Dual-HINet jointly learns node-level and cluster-level integration of multigraphs and a clustering assignment across edge types while estimating a connectional brain template.

HC relevance: hierarchical integration at multiple structural scales may be useful, especially where local relations and larger functional groupings interact.

However:

`LEARNED_CLUSTER != FUNCTIONAL_ONTOLOGY_TRUTH`

`HIERARCHICAL_POOL != BIOLOGICAL_OR_COGNITIVE_MODULE_PROOF`

`CLUSTER_ASSIGNMENT != AUTHORITY_DOMAIN`

A learned hierarchy is a representation/hypothesis whose training objective and evidence must remain explicit.

## MSRGNN — relational reasoning is conditioned on a chosen graph prior

DOCUMENTED from the root README: MSRGNN is a multi-scale relational GNN for several abstract visual reasoning tasks.

OBSERVED from `I_RAVEN/msrgnn.py`:

- visual inputs are encoded at three adaptive-pooling scales (`4x4`, `2x2`, `1x1`);
- each scale is projected and processed by a shared gated pairwise-relation GNN stage;
- scale-local results are concatenated, then passed through a second unified GNN relation stage;
- relation messages are generated from pairs of integrated node features and position embeddings;
- attention weights gate those pairwise messages;
- a candidate-specific graph is built from context panels plus one candidate answer;
- the graph topology is not discovered from the task evidence by default: it is supplied as a fixed `row_col` template, a fully connected template, or a caller-provided edge template;
- the final graph state is pooled by mean, max, and sum before candidate scoring.

This is a useful demonstration of candidate-scoped relational reasoning and late fusion across feature scales.

It also exposes a key HC boundary:

`REASONING_GRAPH_PRIOR != WORLD_RELATION_TRUTH`

`FIXED_MESSAGE_PATH != DISCOVERED_CAUSAL_STRUCTURE`

`ATTENTION_WEIGHT != EPISTEMIC_AUTHORITY`

`CANDIDATE_SCORE != FACT`

A relational reasoning workspace may intentionally impose a topology that defines which comparisons are computed. That topology is a computational prior/hypothesis unless separately supported as a world or HC-topology claim.

### Multi-scale lesson

MSRGNN processes each visual scale separately through a shared reasoning stage before concatenating scale outputs for a second relation stage.

HC transfer candidate:

`scale-local evidence -> scale-local relational hypotheses -> provenance-preserving cross-scale fusion -> candidate evaluation`

This supports the existing HC preference to preserve source/view identity before fusion rather than flatten heterogeneous evidence immediately.

## DGL course repository — useful teaching map, not claim authority

DOCUMENTED from the README: the BASIRA DGL course covers graph types/matrices, embeddings, GCNs, pooling, sampling, permutation invariance/equivariance, GNN expressiveness, graph generation, Graph U-Net, and evaluation of generative GNNs.

Disposition: useful as a structured study/discovery map and for identifying implementation topics to test. Lecture material is not a substitute for primary papers or claim-level scientific verification.

## Cross-source HC lessons

### 1. Dependency lineage is required for corroboration counts

If several models, replicas, derived views, or summaries descend from the same source evidence or initialization, HC must retain that dependency lineage.

Independent-looking outputs may be correlated by shared data, shared initialization, shared preprocessing, shared model, shared template, or copied state.

`NUM_OUTPUTS != NUM_INDEPENDENT_SOURCES`

### 2. Consensus objectives can hide exceptions

Global centeredness, consistency loss, averaging, template normalization, and federation can improve coordination while simultaneously suppressing minority evidence.

Any HC consensus-like transform should retain material source dissent and should not turn numerical agreement into semantic truth.

### 3. Hierarchies and modules are hypotheses unless protected architecture says otherwise

Learned communities, clusters, pooling assignments, and hierarchical representations can guide computation without becoming permanent cognitive ontology.

A learned module boundary should remain revisable through governed plasticity unless it corresponds to separately established physical/protected architecture.

### 4. Reasoning topology and world topology are separate

A reasoning workspace may choose a fully connected graph, sparse comparison graph, row/column graph, task template, or learned candidate topology because it is computationally useful.

That graph describes **which relations the reasoning process evaluates**, not automatically **which relations are true in the world** or **which routes physically/effectively exist in HC**.

## Current disposition

KEEP as research/provenance. Promote generic dependency-lineage, relational-prior, and meta-evidence boundaries selectively. No source code is copied into HC.