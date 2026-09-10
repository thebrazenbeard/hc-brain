# Federated and Model-Graph Implementation Scout — 2026-09-09

Status: research/provenance only; noncanonical architecture input.

## Purpose

This is Four's implementation-focused research lane under `docs/research/BASIRA_COORDINATED_SCOUR_WORKPLAN_2026-09-09.md`.

The goal is not to import a federated-learning framework into the Hyperconnectome Brain. The goal is to identify mechanisms, hidden ancestry, representation boundaries, and failure modes that matter if HC later uses model graphs, multiple learners, replicas, federated optimization, generated graph state, or distributed computational evidence.

The central questions are:

1. When several models agree, how independent is that agreement after shared initialization, shared gradients, parameter aggregation, replicas, or cross-client regularization?
2. When a neural network is converted into a graph, what does that graph represent: a world, a connectome, a model's computation/parameters, or an HC runtime topology?
3. When a method is described as graph-based, is message passing actually using the source graph topology?
4. When generated/aligned models converge, is that convergence evidence about the external world or evidence about the optimization mechanism?
5. Which source claims are actually implemented in the inspected default-branch code?

## Evidence discipline

Evidence labels in this record use the HC vocabulary:

- `DOCUMENTED`: explicitly claimed in source documentation/publication metadata available in the source repository.
- `OBSERVED`: directly visible in inspected source code/repository state.
- `INFERRED`: a bounded consequence of observed code/structure.
- `HYPOTHESIS`: plausible transfer or failure mechanism requiring implementation testing.
- `UNKNOWN`: not established by the inspected source.

Static source inspection does not establish runtime correctness or reproduce a published experiment. Suspected defects are therefore labeled as code-level defect candidates unless execution or paper-level comparison closes the question.

No external source code is copied into HC by this research package.

## Exact source bindings and read depth

### UnifiedFL

Repository: `basiralab/UnifiedFL`

Default-branch cut inspected:

`main@de6a1c6d7d61900b4cd86b48ba6b6bee3d84e5e6`

Read depth: code-deep on the graphification/unification/model/training entry path.

Material paths inspected:

- `README.md` — blob `f98ccda20cb3d824f54b70f18bb28de3a78c8f4a`
- `unifiedfl/graphs/convert.py` — blob `e73737d2b1e063e3f9f8ac2dc26551cce18737dd`
- `unifiedfl/graphs/unify.py` — inspected default branch
- `unifiedfl/models/unifiedfl.py` — blob `889f449009885fbf7cc824444a7d9bc4cd669260`
- `unifiedfl/scripts/train_unifiedfl_ws.py` — blob `e2f2e2c8669451e51494212b14ddcd217567cf6a`

### uGNN

Repository: `basiralab/uGNN`

Default-branch cut inspected:

`main@8ba26f2d7637238c6ad89d06836eb3551d5568bd`

Read depth: code-deep on the graphification/unification/model path plus README workflow.

Material paths inspected:

- `README.md` — blob `4dace49a0bc01d760c8433df383f4086bd229804`
- `ugnn/graphs/convert.py` — blob `e73737d2b1e063e3f9f8ac2dc26551cce18737dd`
- `ugnn/graphs/unify.py` — blob `0fe122bf6b3b967e4218b16d8037ba6f02c7d259`
- `ugnn/models/ugnn.py` — blob `889f449009885fbf7cc824444a7d9bc4cd669260`

### RepFL

Repository: `basiralab/RepFL`

Default-branch cut inspected:

`main@472723eb4519dd34b16ce78d2dd81ffa459e48a6`

Read depth: code-deep on replica creation/data perturbation, replica aggregation, and server aggregation.

Material paths inspected:

- `README.md` — blob `f6a0f916027ef1690da648121fe9f2212fa07f6c`
- `client/SGRepGenerator.py` — blob `a4d62f65ee77c09b438df05a1b192d6338166e45`
- `server/FederatedServer.py` — blob `4f149cef17010243d937a9a8d1615e2d546c86f5`

### Fed2M

Repository: `basiralab/Fed2M`

Default-branch cut inspected:

`main@24b425779bdefaad4bfe74116787c30613765a31`

Read depth: code-deep on graph representation, loss structure, client/server federation, global representation exchange, and evaluation.

Material paths inspected:

- `README.md` — blob `cfbaaa173fe8bda669e1efe2bc073f67963946f1`
- `model.py` — blob `4d0bef446b012562eb6afb11fe5e3ef61b627f7a`
- `demo.py` — blob `86c75165941ec097595afad6433d9eacc13a0f36`

### FedGmTE-Net

Repository: `basiralab/FedGmTE-Net`

Default-branch cut inspected:

`main@e890ad61aa44dd1fd556f8b3ca0df1af857fee6d`

Read depth: code-deep on client/global model construction, weighted parameter aggregation, global-to-client rebroadcast, and training flow; temporal prediction details are Noah's primary lane.

Material paths inspected:

- `README.md` — blob `5ced22afc087a7201f2800266363692f5f796067`
- `main.py` — blob `6cf3e451055a64fbcdcc5c7265e1e61d45a571b6`
- `prediction.py` — source path inspected at this cut

### FedGmTE-Net-plus

Repository: `basiralab/FedGmTE-Net-plus`

Default-branch cut inspected:

`main@4d81ba4c3a501a8e4ad07bff7291bdcf7f622166`

Read depth: method/code read on federation, FedDyn additions, masks/imputation integration, and global/client ancestry; detailed imputation/forecast semantics are Noah's primary lane.

Material paths inspected:

- `README.md` — blob `0ac0045733600e181b2ab61046b68c07ad1357ee`
- `prediction.py` — blob `0c3c607dbb28ea8885638d90fae813bb27fb4a4f`

## 1. Model graphs are a separate representational plane

### uGNN / UnifiedFL graphification

`OBSERVED`:

The inspected `convert.py` turns neural-network implementation structure into a graph representation.

For MLPs:

- input/output units become graph nodes;
- linear weights become graph edges/edge attributes;
- biases become node-associated state;
- activation type is attached as node state.

For CNNs:

- spatial/channel activation positions are materialized as nodes;
- convolution-kernel relationships become explicit edges;
- kernel indices may be preserved for weight-sharing groups.

This graph is therefore a representation of a model's computational/parameter structure.

It is not, by construction, any of the following:

- an observed environmental graph;
- a biological connectome;
- a semantic/world model;
- the HC's canonical temporal hypergraph;
- proof of a model's causal reasoning structure.

Transfer invariant:

`MODEL_GRAPH != WORLD_GRAPH != OBSERVED_CONNECTOME != HC_RUNTIME_HYPERGRAPH`

### Disjoint-union “unification”

`OBSERVED`:

The uGNN/UnifiedFL `unify` functions concatenate individual model graphs by offsetting node identifiers and concatenating edge lists, attributes, biases, and activation state.

No cross-model semantic edges are introduced by that operation itself.

The result is therefore a disjoint union carrying several model graphs in one tensor/container.

`DISJOINT_UNION != SEMANTIC_UNIFICATION`

The useful transfer is representational interoperability: multiple heterogeneous models can be placed into one processing substrate while preserving model membership.

The non-transfer boundary is equally important: putting model A and model B into one graph container does not establish that a node/edge in A has a semantic correspondence to a node/edge in B.

## 2. UnifiedFL and uGNN share deeper implementation ancestry than names imply

### Byte-identical core blobs

`OBSERVED`:

At the inspected cuts:

- `uGNN/ugnn/graphs/convert.py` and `UnifiedFL/unifiedfl/graphs/convert.py` have the same blob SHA: `e73737d2b1e063e3f9f8ac2dc26551cce18737dd`.
- `uGNN/ugnn/models/ugnn.py` and `UnifiedFL/unifiedfl/models/unifiedfl.py` have the same blob SHA: `889f449009885fbf7cc824444a7d9bc4cd669260`.

`INFERRED`:

The current default-branch UnifiedFL core model-graph transformation/optimization implementation is not an independently evolved mechanism at these files; it shares exact code ancestry with uGNN.

This does not make either method invalid. It does matter for evidence independence and method-family accounting.

`SEPARATE_REPOSITORY != INDEPENDENT_IMPLEMENTATION_EVIDENCE`

### Shared theta updates over disjoint model graphs

`OBSERVED`:

The core UGNN implementation learns parameter groups that transform model-graph edge weights and biases. Individual model forward paths then use those transformed graph states.

The graphs can remain disjoint while their updates share learned theta parameters/grouping.

This creates shared optimization ancestry across nominally distinct models.

For HC:

`MULTIPLE_OUTPUTS_AFTER_SHARED_PARAMETER_UPDATE != MULTIPLE_INDEPENDENT_WITNESSES`

If several bounded internal models share a training/update mechanism, evidence ledgers should preserve at least:

- common initialization ancestry;
- common optimizer/update-family ancestry;
- shared parameter groups;
- shared training data or data lineage;
- cross-model regularization/alignment;
- independent versus shared evaluation evidence.

## 3. UnifiedFL default-branch implementation versus README federation claim

### Source claim

`DOCUMENTED from README`:

UnifiedFL describes a dynamic federated framework in which clients are clustered after communication rounds according to Euclidean distances between their GNN parameters, with more frequent exchange among similar clients and sparser exchange across dissimilar groups.

### Inspected code path

`OBSERVED`:

The inspected `train_unifiedfl_ws.py`:

- loads precomputed `PathMNIST_cluster{c}.npy` sample-index files;
- creates several local model architectures;
- graphifies/unifies those models;
- creates one `UGNN_WS` object;
- maps model `i` to cluster `i` using `model2cluster = {i:i ...}`;
- calls a unified training function for a configured number of epochs.

The entry point does not itself expose communication rounds, clients/servers, post-round Euclidean parameter-distance clustering, or a sparse cross-cluster synchronization scheduler.

Additional default-branch code search during this pass found the terms associated with Euclidean dynamic clustering in the README, but did not locate an implementation by searches for `euclidean`, `cdist`, or `KMeans` in the inspected code paths.

The script also retains uGNN-oriented internal naming (`ugnn`, `ugnn_ws`, `ugnn.scripts`).

### Classification

`OBSERVED_CODE_GAP / PAPER_OR_OTHER_BRANCH_BEHAVIOR_NOT_ESTABLISHED_BY_INSPECTED_DEFAULT_BRANCH`

This is not a claim that the described method was never implemented, that another branch/artifact lacks it, or that paper results are invalid.

The HC research implication is methodological:

`README_METHOD_DESCRIPTION != OBSERVED_RUNTIME_MECHANISM`

Promotion of an external method into HC architecture should bind to the exact code/paper mechanism actually verified, not the repository title or high-level diagram.

## 4. RepFL replicas are correlated descendants, not independent evidence

### Replica ancestry

`DOCUMENTED + OBSERVED`:

RepFL creates replica learners to diversify a small federated client set.

The inspected client implementation:

- recursively instantiates replicas from the same model class;
- initializes the anchor and replicas from the same supplied global model state;
- constructs replica training sets by perturbing/removing subsets from the anchor dataset lineage;
- aggregates replica and anchor model parameters before further federation.

The important HC inference is straightforward:

`REPLICA_COUNT != INDEPENDENT_EVIDENCE_COUNT`

Even if replica outputs later differ, they share substantial ancestry:

- model architecture;
- global initialization;
- anchor-data lineage;
- optimization family;
- aggregation path.

Replica agreement can be useful robustness evidence. It is not equivalent to corroboration by independently sourced witnesses.

### Static replica-aggregation defect candidate

`OBSERVED_STATIC_CODE_DEFECT_CANDIDATE`:

`SGRepGenerator.aggregate_replicas()` states that anchors and replicas are assigned equal weights.

For `R` replicas it sets:

`weight = 1 / (1 + R)`

It then multiplies each anchor/replica parameter tensor by that weight, stacks the already-weighted tensors, and applies `.mean(dim=0)`.

Algebraically, that yields:

`sum(parameters) / (R + 1)^2`

rather than the ordinary equal-weight average:

`sum(parameters) / (R + 1)`.

If all anchor/replica tensors were identical to `P`, the observed code path would produce `P / (R + 1)`, not `P`.

This looks inconsistent with the code comment and conventional equal-weight averaging.

Claim ceiling:

- this is a static code finding;
- no execution was performed in this pass;
- no claim is made here that the published algorithm intended this scaling;
- no claim is made here that reported experiments used this exact source state without compensating behavior elsewhere.

HC transfer control:

`AGGREGATION_CODE_MUST_PASS_IDENTITY_CASE`

A proposed averaging/fusion operator should include a control in which all inputs are identical; unless the operator intentionally transforms scale, the aggregate should preserve that identical value.

## 5. Fed2M: graph method naming can hide the actual message-passing graph

### One-node/self-loop computational graph

`OBSERVED`:

Fed2M's model docstrings describe vectorized connectome features as node features of a one-node graph, with the edge index connecting each graph node only to itself. In batched form, samples are represented in that computational graph with self connections rather than message passing over biological connectome regions/edges.

Its GCN layers therefore operate on a computational representation distinct from the source connectome topology.

Source topology information is carried through:

- the vectorized connectivity features;
- reconstruction loss;
- normalized-node-strength topology loss;
- CBT construction/evaluation.

This is a legitimate modeling choice, but it establishes a crucial HC research control:

`GRAPH_METHOD_NAME != SOURCE_GRAPH_TOPOLOGY_USED_BY_MESSAGE_PASSING`

When assessing an external GNN/graph method for HC, explicitly identify:

1. the graph on which message passing occurs;
2. the graph represented as input features;
3. the graph predicted/reconstructed;
4. the graph used only in the loss/evaluator;
5. the HC topology plane, if any, affected by the method.

### Parameter federation and cross-client representation pulling

`OBSERVED`:

Fed2M's server averages same-named compatible client parameters and broadcasts the aggregate back to clients.

The training code also samples intermediate representations from other clients and uses global-centeredness loss to pull local representations toward shared cross-client state.

Consequently:

`POST_FEDERATION_CLIENT_AGREEMENT != INDEPENDENT_CORROBORATION`

Agreement can be an intended product of the shared optimization objective.

An HC evidence object derived from several such clients should carry shared-training ancestry so the system does not count induced convergence as independent evidence about the external world.

### Center templates compress distributions

`OBSERVED`:

Fed2M generates connectional brain templates using median/center-like summaries and evaluates local/global centeredness.

Transfer warning:

`ROBUST_CENTER != FULL_POPULATION_DISTRIBUTION`

A center/template can be useful for normalization, anomaly comparison, or reference construction while still erasing multimodality, minority modes, rare-but-critical states, and conditional structure.

HC should preserve the source distribution or sufficient alternatives when those lost modes affect cognition, safety, identity, or uncertainty.

## 6. FedGmTE-Net: federated forecast models share explicit parameter ancestry

`DOCUMENTED + OBSERVED`:

FedGmTE-Net trains multiple hospital/client models and periodically aggregates them.

The inspected implementation:

- builds local encoders and two trajectory decoders per client;
- creates corresponding global encoder/decoder models when federation is enabled;
- initially loads global parameters into every client;
- computes weighted global parameters using client sample counts;
- loads the aggregated global state back into every client after federation rounds.

Thus, after the first global synchronization, client models have explicit shared parameter ancestry.

`GLOBAL_ROUND_DESCENDANTS_SHARE_ANCESTRY`

If two clients agree after repeated federation, the agreement may reflect:

- distinct local data;
- shared global initialization;
- previous aggregate states;
- common architecture/loss;
- repeated global rebroadcast;
- convergence pressure.

An HC evidence ledger should not flatten those causes into an unqualified `two_models_agree` counter.

### Boundary with Noah's temporal lane

The method is also a multi-trajectory predictor. Detailed forecast lineage, missing-timepoint completion, future-state admission, and temporal counterfactuals belong primarily to Noah's assigned lane.

Four's transfer here is narrower:

`PREDICTIONS_FROM_FEDERATED_DESCENDANTS_RETAIN_SHARED_MODEL_ANCESTRY`

## 7. FedGmTE-Net-plus preserves the ancestry rule while adding imputation/FedDyn complexity

`DOCUMENTED`:

FedGmTE-Net-plus extends the family with a two-step imputation process and additional federation/training options.

`OBSERVED`:

The inspected implementation still:

- creates one set of local encoders/decoders per client;
- creates global counterparts;
- loads global parameters into local clients;
- aggregates local parameters using client sample-count weighting;
- reloads the global state into clients;
- optionally applies FedDyn-style state/gradient terms.

Therefore the core ancestry conclusion is unchanged:

`FEDERATED_DESCENDANTS_REMAIN_CORRELATED_AFTER_MORE_SOPHISTICATED_AGGREGATION`

The extra imputation machinery creates another provenance dimension:

`IMPUTED_TRAJECTORY_VALUE != DIRECTLY_OBSERVED_TRAJECTORY_VALUE`

Detailed imputation/forecast treatment is deferred to Noah's temporal-prediction lane, but Four recommends that any HC implementation preserve the distinction at the evidence-object level.

## 8. Federated aggregation is coordination, not epistemic voting

Across the inspected methods, parameter sharing can be implemented through:

- ordinary weighted/unweighted averaging;
- replica aggregation;
- selected common-layer aggregation;
- shared graph-parameter transformations;
- FedDyn-like correction terms;
- global-centeredness/cross-client representation objectives.

These mechanisms are useful for distributed learning. None turns parameter consensus into independent external-world evidence.

Required HC distinction:

`OPTIMIZATION_CONSENSUS != EPISTEMIC_INDEPENDENCE`

A future HC multi-model object should distinguish at least:

```text
MODEL_EVIDENCE_LINEAGE {
  model_instance
  architecture_family
  initialization_ancestry
  training_data_lineage
  shared_update_ancestry
  replica_or_derivative_ancestry
  cross_model_regularization_refs
  aggregation_round_refs
  independently_held_out_evidence_refs
  result_provenance
}
```

This is a research concept, not a canonical schema proposal in this PR.

## 9. Model-graph self-analysis is useful but dangerous if it becomes self-authorizing

uGNN/UnifiedFL show that heterogeneous neural architectures can be projected into a shared graph representation and manipulated through graph-based parameter transformations.

That suggests possible future HC uses such as:

- bounded model introspection;
- identifying structurally similar update targets;
- comparing alternative candidate models;
- proposing parameter/update transformations;
- estimating blast radius of model changes;
- testing candidate updates in isolated/shadow state.

But the model graph is still a representation of implementation state.

It does not carry automatic authority to modify the represented model.

`MODEL_GRAPH_WRITE_ACCESS != PROTECTED_UPDATE_AUTHORITY`

`STRUCTURAL_SIMILARITY != SAFE_PARAMETER_TRANSFER`

`MODEL_GRAPH_EMBEDDING != MODEL_SEMANTIC_EQUIVALENCE`

Any eventual HC use should flow through existing protected-update, authority/effect, verification, rollback, and qualification contracts.

## 10. Hostile controls extracted from this source family

### Shared-ancestry false corroboration

Create three model instances with apparently independent outputs but:

- common initialization;
- repeated parameter aggregation;
- overlapping/replicated data lineage.

The HC must not assign the same corroboration weight as three independently trained/evidenced systems.

### Replica identity control

Create anchor plus replicas with identical parameters and identical data.

Aggregation should preserve the identical model state unless an explicit scaling transform is part of the declared algorithm.

### Disjoint-union semantic illusion

Place unrelated model graphs into one disjoint graph container.

No cross-model semantic correspondence may be inferred solely from graph co-membership.

### Model-graph/world-graph confusion

Use a model-graph edge and a world/connectome edge with similar numeric attributes.

The HC must preserve their representation-plane/type distinction.

### GNN-label topology illusion

Run a “GNN” whose message-passing graph is a self-loop computational graph while source topology is only encoded as features/loss.

The system must not claim source-graph message passing occurred.

### Induced-consensus control

Strongly align several client representations or repeatedly FedAvg their parameters until they agree.

Agreement after alignment must retain the alignment/aggregation lineage.

### Center-collapse control

Construct a bimodal source population whose arithmetic/median center lies in a state poorly representing either mode.

A center/template must not silently replace the distribution when alternatives matter.

### README/code mismatch control

Source documentation claims mechanism X; inspected default-branch entrypoint does not expose X.

Classification remains `DOCUMENTED_CLAIM + IMPLEMENTATION_NOT_ESTABLISHED` rather than silently upgrading the claim to observed code.

## 11. Recommended HC transfer

### Keep as research/implementation mechanisms

- model-to-graph projection for bounded introspection and heterogeneous model handling;
- explicit ancestry tracking across shared updates, replicas, and federation rounds;
- weighted aggregation as an optimization mechanism, not epistemic voting;
- distribution-preserving treatment of multi-client/model evidence;
- explicit distinction between computational graph, observed graph, generated graph, and HC runtime hypergraph;
- identity-case and correlated-ensemble hostile controls;
- currentness/provenance retention through federated results.

### Do not promote directly

- any source framework as an HC runtime architecture;
- model-graph edges as HC temporal-hypergraph relations;
- multiple federated/replica model outputs as independent evidence by count;
- center/template estimates as complete population state;
- README-only mechanisms as observed implementation;
- GNN terminology as proof that source graph topology participates in message passing;
- replica/federation agreement as semantic truth;
- model-graph manipulation as self-modification authority.

## 12. Open implementation questions for HC

1. What machine-readable ancestry object should accompany results from several related HC internal models?
2. How should corroboration weight decay with shared initialization, data, updates, distillation, or aggregation?
3. What conditions make two models independent enough for separate evidentiary weight on a particular claim?
4. How should an HC model-graph projection preserve typed node/edge roles, uncertainty, provenance, and protected-state boundaries?
5. Can model-graph comparison help detect risky update blast radius without creating a path around protected-update governance?
6. How should graph centers/templates preserve multimodal alternatives or rare-but-critical structure?
7. What static/runtime checks should detect aggregation operators that fail the identical-input identity case?
8. How should external method documentation/code mismatch affect promotion confidence and qualification scope?

## Current disposition

`KEEP_AS_RESEARCH / IMPLEMENTATION_CONTROL_VALUE_HIGH / NO_DIRECT_CANONICAL_PROMOTION`

The deepest transfer is an evidence-accounting rule:

> **Several models can be computationally separate while remaining epistemically correlated through shared ancestry. HC must preserve that ancestry before treating agreement as corroboration.**
