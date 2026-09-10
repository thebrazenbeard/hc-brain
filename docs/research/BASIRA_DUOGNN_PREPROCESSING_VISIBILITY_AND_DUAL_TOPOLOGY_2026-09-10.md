# BASIRA DuoGNN Preprocessing Visibility and Dual-Topology Study — 2026-09-10

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/DuoGNN`

Source branch: `main@624cf21548465ea1c9e281788e8eaad5a8be82c1`

Inspected artifacts:

- `README.md` blob `ab7dc577d787edaf23f84fa196124dab23d9b2a2`
- `main_multilabel_classification.py` blob `c9e7ea1bd008599b9c031aa9aec371977bd5abaf`
- `models/dual_gnn_model.py` blob `382d168d67e196dcb0333cc73f629300558427fd`
- `train/train_multi_class_classification.py` blob `e000ca4d80b0d3a8fee53184e0a4f2fc7ef717a7`
- `train/utils.py` blob `802cd05295511095533df4798d64159cbb25470e`

This note records source-specific implementation observations and reusable HC transfer lessons. It does not reproduce the paper's experiments, establish publication-level validity or invalidity, or make DuoGNN an HC implementation requirement.

## DOCUMENTED source framing

The repository README describes DuoGNN as a topology-aware graph neural network with homophily/heterophily interaction decoupling and identifies the repository as accompanying a MICCAI GRAIL 2024 workshop paper. The implementation exposes a `DualGCN` path in which two graph views are processed separately and their learned representations are concatenated before the final output layer.

## OBSERVED dual-topology computation

`models/dual_gnn_model.py` maintains distinct parameter stacks for two branches. `forward(x, adj_a, adj_b)` clones the same feature tensor into two branches, processes `adj_a` through the ordinary branch and `adj_b` through the heterophily branch, then concatenates the branch outputs before the final linear layer.

This provides a concrete example of one feature state participating in multiple computational topology views without those views becoming independent observations.

`MULTIPLE_TOPOLOGY_VIEWS != MULTIPLE_INDEPENDENT_OBSERVATIONS`

`PARALLEL_COMPUTATIONAL_RELATIONS != MULTIPLE_WORLD_FACT_SOURCES`

That lesson is already compatible with HC relational-provenance rules; DuoGNN is a new source fixture rather than a new HC primitive.

## OBSERVED full-graph topology preprocessing before split

`main_multilabel_classification.py` constructs a single NetworkX graph `G` from all supplied nodes, features, labels, train/validation/test masks, and edges. It then copies that complete graph into `G_topo`.

The code next calls `split_graph(G)` under a comment describing inductive training. `split_graph` first emits the complete graph as its test representation, then removes test nodes to produce the train-plus-validation graph, then removes validation nodes to produce the training graph.

However, the topology-aware preprocessing path does not operate on those already separated graph objects. Instead, when `topological_measure != "none"`, it continues from the earlier `G_topo` copy of the complete graph.

The inspected implementation computes topology values on `G_topo` using one of Forman curvature, degree centrality, betweenness centrality, eigenvector centrality, or random values. It can then remove edges according to those scores.

For `DualGCN`, it further:

1. computes connected components on the transformed complete `G_topo`;
2. selects the maximum-topology node from each selected component;
3. removes all edges;
4. fully connects the selected nodes into the condensed/heterophilic graph; and only then
5. calls `split_graph(G_topo)` to derive the training, validation, and test conditional adjacency views.

Therefore, on the topology-aware `DualGCN` path, the graph transformation that determines the conditional training topology is computed before train/validation/test structural separation.

`LATER_SPLIT != EARLIER_INFORMATION_ISOLATION`

`INDUCTIVE_LABEL_OR_COMMENT != VERIFIED_INDUCTIVE_PREPROCESSING`

`TRAIN_GRAPH_OUTPUT != TRAIN_ONLY_PREPROCESSING_ANCESTRY`

## OBSERVED executed use of the conditional topology

`train/train_multi_class_classification.py` accepts `adj_train_cond`, `adj_val_cond`, and `adj_test_cond`.

During training, if `adj_train_cond` is present, `full_batch_step` executes the model as:

```text
model(x_train, adj_train, adj_train_cond)
```

During validation and testing, the corresponding conditional adjacency is likewise passed to the model.

The conditional topology is therefore not merely diagnostic or visual metadata in the inspected path. It reaches the model's material forward computation.

`PREPROCESSING_ARTIFACT_CREATED != UNUSED_ARTIFACT`

`DECLARED_SPLIT_STAGE != ACTUAL_INFORMATION_FLOW_BOUNDARY`

## INFERRED evaluation-regime implication

For topology-aware `DualGCN` runs, the training-time conditional graph can depend on graph structure from nodes/edges belonging to validation or test partitions because the topology scores, component decomposition, representative-node selection, edge removal, and condensed topology are produced from the complete pre-split graph.

This supports classifying that preprocessing/dataflow as structurally transductive or evaluation-cohort-exposed with respect to graph topology, rather than as strictly `INDUCTIVE_FROZEN` preprocessing.

The narrower supported statement is:

> The inspected topology-aware path allows evaluation-partition graph structure to influence the conditional topology later supplied during training.

The source read does **not** establish that test labels are used by the topology metrics. The graph objects contain labels as node attributes, but the inspected topology-score and condensation operations do not consume those label attributes.

Accordingly:

`UNLABELED_TEST_STRUCTURE_VISIBLE != TEST_LABEL_LEAKAGE`

`STRUCTURAL_TRANSDUCTIVE_EXPOSURE != AUTOMATIC_EVALUATION_INVALIDITY`

A transductive regime can be valid when declared and matched to the intended deployment. The defect class for HC is silent mismatch between the actual information boundary and the claimed qualification regime.

## Split timing is provenance

The important reusable lesson is that evaluation visibility is determined by the earliest operation that can influence the target computation, not by the point at which objects are later named `train`, `validation`, or `test`.

A pipeline may split the final tensors correctly and still carry evaluation-cohort information into training through an earlier fitted or constructed artifact such as:

- topology or adjacency;
- normalization statistics;
- manifold or embedding;
- vocabulary or tokenizer statistics;
- graph communities or clusters;
- calibration map;
- feature-selection mask;
- learned transform;
- nearest-neighbor index;
- generated template;
- routing or topology policy.

Therefore HC qualification should record preprocessing visibility ancestry and the information set available when each consequential derived artifact was created.

`SPLIT_BEFORE_SCORING != SPLIT_BEFORE_ALL_INFLUENCE`

`TRAIN_ONLY_FINAL_TENSOR != TRAIN_ONLY_DERIVATION_ANCESTRY`

## Source-specific implementation note: layer-count hazard

`DualGCN.__init__` defines local variable `hidden_dim` only inside the loop `for _ in range(num_layers - 2)` and later uses `hidden_dim` when constructing `merge_layer_b`.

The main script defaults `--layers` to `3`, so the default path initializes the variable. If the model is instantiated with `num_layers == 2`, the inspected constructor appears to reach `merge_layer_b` without assigning `hidden_dim` first.

This is OBSERVED static source structure. Whether supported experiment configurations ever use two layers is UNKNOWN from the inspected cut. It is retained as a source-specific implementation hazard and is not promoted to HC architecture.

## HC transfer

PROMOTE the general information-boundary rule:

> **Evaluation isolation is ancestry-aware. Any preprocessing, topology construction, fitting, normalization, calibration, or representation step that can influence the trained/evaluated target must declare which evaluation-partition information was visible at the time it was constructed. A later train/test split cannot retroactively erase earlier exposure.**

This strengthens two existing HC contracts:

1. qualification evidence isolation — evaluation regime and exposure lineage include preprocessing artifacts, not only direct model fitting or label access;
2. executed dataflow/binding integrity — the declared split stage must correspond to the actual earliest information-flow boundary.

Do not promote DuoGNN's particular two-branch architecture, topological measures, representative-node condensation, or source-specific layer-count hazard as HC requirements.

## Adversarial tests suggested

1. Compute a preprocessing topology from a complete cohort, split afterward, and require `INDUCTIVE_FROZEN` qualification to fail unless the topology is recomputed from training-visible information only.
2. Add one test-only node/edge that changes a full-graph centrality/component result; verify that any resulting training-topology change is recorded as test-cohort exposure.
3. Hold training tensors fixed while perturbing only evaluation-cohort structure; if a training-time derived artifact changes, require regime/provenance to expose that dependency.
4. Build normalization/manifold/template state from train+test inputs without labels; verify it is not mislabeled train-only merely because labels were hidden.
5. Split source records first but reuse a derived artifact fit before the split; require ancestry-aware isolation to detect the earlier exposure.
6. Construct parallel topology views from one observation graph and verify independent evidence count remains one unless genuinely independent source ancestry exists.
7. Use a source-level comment or variable name claiming `inductive`; require executable provenance rather than the label to establish the regime.
8. Recompute the topology using only the permitted training graph and compare it with the full-cohort-derived version; any difference demonstrates material preprocessing dependence.

## Evidence boundary

DOCUMENTED: repository framing, model purpose, workshop-paper context, and exposed DualGCN usage from README/source descriptions.

OBSERVED: complete graph construction before split; `G_topo` copy before split; full-graph topology scoring/filtering/condensation; later split of the transformed conditional graph; use of `adj_train_cond` in training forward computation; separate dual model branches; nested node-removal behavior in `split_graph`; default layer count of 3; static two-layer constructor hazard.

INFERRED: the topology-aware DualGCN preprocessing is structurally transductive/evaluation-cohort-exposed under the inspected source cut because validation/test graph structure may affect the conditional topology later consumed in training; general HC ancestry-aware preprocessing-visibility requirements.

UNKNOWN: quantitative effect on reported results, which exact experiment runs used which topology settings, whether the paper labels those runs inductive or transductive, whether other unretrieved source revisions differ, whether two-layer DualGCN is an intended supported configuration, and publication-level impact.

## Transfer decision

PROMOTE PREPROCESSING-VISIBILITY AND ACTUAL-INFORMATION-BOUNDARY RULES; RETAIN DUOGNN-SPECIFIC DETAILS AS RESEARCH EVIDENCE ONLY.
