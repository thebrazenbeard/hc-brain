# BASIRA FALCON Label-Constrained Collapse and Regime Variation — 2026-09-10

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/FALCON`

Source branch: `main@b9152c294580c271b14b58cbb4bba1293e974a44`

Inspected artifacts:

- `README.md` blob `5f2a6b13b78dc0502970961800c33e74a1b7344b`
- `contraction.py` blob `2ff815690298a21bcc4838c35ae146e8d5d38ac8`
- `main_Cora.py` blob `a88dbfe533b9bcac646708fcaa9d1f602f667f31`
- `main_PPI.py` blob `0cfe912bcdea3215b598d7a75ab9f2484aa8dd7e`

This record studies information visibility and preprocessing ancestry. It does not reproduce FALCON experiments or establish publication-level validity or invalidity.

## DOCUMENTED source framing

The repository describes FALCON as feature-label constrained graph collapse for memory-efficient GNNs. Its exposed `constraint='FL'` mode clusters nodes using both features and labels, while `gamma` controls the relative feature-versus-label contribution. The README describes `gamma=1` as feature-only, `gamma=0` as label-only, and intermediate values as mixed prioritization.

The Cora entrypoint defaults to:

```text
constraint = FL
N_cluster = 150
gamma = 0.5
```

so its default collapse configuration is explicitly feature-label constrained.

## OBSERVED contraction semantics

In `contraction.py`, `contract_graph` builds matrices `X` and `Y` by iterating over every node in the supplied graph and reading both `node['x']` and `node['y']`.

For `constraint == 'FL'`, it scales features and labels, concatenates them as `XY`, and fits KMeans to `XY`. The resulting cluster labels `parts` are then used when deciding the partition quota and eligibility of training-node contractions.

The removal operation itself is restricted to nodes whose `train` attribute is true. That restriction does not erase how the cluster assignment was produced.

Therefore:

`TRAINING_NODE_ONLY_MUTATION != TRAINING_ONLY_PREPROCESSING`

`LABEL_NOT_USED_IN_FINAL_LOSS != LABEL_NOT_USED_TO_SHAPE_TRAINING_STATE`

`FILTERED_EFFECT_SCOPE != INPUT_VISIBILITY_SCOPE`

A preprocessing transform can consume information from one partition while mutating only another partition.

## OBSERVED Cora visibility path

`main_Cora.py` loads one Planetoid graph containing features, labels, edges, and train/validation/test masks. It constructs a single graph `G` from those arrays.

It first copies `G` to produce uncontracted validation/test tensors. It then passes the original full `G` directly into `contract_graph` using the configured feature-label constraint.

Only after contraction does it call `split_graph(G)` to derive the contracted training graph used for training.

Because `contract_graph` reads `x` and `y` from every node in its supplied full graph, the inspected Cora `FL` path makes validation/test node labels and features visible to the clustering stage that influences which training nodes are collapsed.

This is an OBSERVED source-level dataflow property:

`EVALUATION_LABEL_NOT_PASSED_TO_MODEL_FORWARD != EVALUATION_LABEL_NOT_USED_TO_SHAPE_TRAINING_ARTIFACT`

`LATER_TRAIN_SPLIT != PREPROCESSING_LABEL_ISOLATION`

The claim does not depend on whether the label-derived influence is large; the information path exists in the inspected implementation.

## OBSERVED PPI contrast

The same repository contains a materially different data-visibility path for PPI.

`main_PPI.py` loads train, validation, and test datasets separately, constructs separate `G_train`, `G_val`, and `G_test` graphs, and calls `contract_graph` only on `G_train`.

Under that entrypoint, feature-label clustering inside `contract_graph` sees the labels of the supplied training graph rather than labels from the separate validation/test graphs.

Therefore the repository itself provides a useful counterexample to method-level overgeneralization:

`SAME_METHOD_NAME != SAME_EVALUATION_INFORMATION_BOUNDARY`

`SAME_PREPROCESSOR != SAME_EXPOSURE_ANCESTRY_ACROSS_ENTRYPOINTS`

Evaluation provenance must be path-, configuration-, dataset-, and entrypoint-specific when those distinctions change information visibility.

## INFERRED qualification implication

For the inspected Cora default `FL` path, training-graph construction is evaluation-label-exposed because validation/test labels participate in KMeans clustering that influences training-node contraction. A qualification that describes this as train-only or `INDUCTIVE_FROZEN` preprocessing without declaring that exposure would overstate isolation.

This is stronger than the preceding DuoGNN structural-exposure fixture because labels themselves are read by the preprocessing stage.

However:

- it does not prove that every FALCON entrypoint has the same exposure;
- it does not prove label exposure occurs when `constraint` is not `FL` or when `gamma=1` makes the label contribution zero in the constructed `XY` values;
- it does not establish publication-level quantitative impact;
- it does not make feature-label constrained preprocessing inherently invalid when labels are legitimately available under the intended task/deployment.

`LABEL_VISIBILITY != AUTOMATIC_METHOD_INVALIDITY`

The supported requirement is honest scope and isolation provenance.

## HC transfer: information influence rather than API location

HC qualification must trace any information class that can shape consequential derived state, not merely what is passed into the final learner, reasoner, or action function.

Labels, authority state, identity state, protected values, private evidence, future observations, evaluator feedback, or other privileged information can affect downstream behavior indirectly through preprocessing such as:

- clustering;
- node/edge selection;
- topology collapse;
- normalization;
- feature selection;
- template generation;
- retrieval-index construction;
- threshold fitting;
- route or topology selection;
- compression/quantization calibration;
- curriculum/sample selection.

Accordingly:

`NOT_IN_FINAL_CALL_SIGNATURE != NOT_IN_CAUSAL_ANCESTRY`

`PRIVILEGED_INPUT_USED_ONLY_FOR_PREPROCESSING != PRIVILEGED_INPUT_UNUSED`

For qualification and protected-state boundaries, causal derivation ancestry matters more than where the information entered the code.

## HC transfer: output-side restriction does not prove input-side isolation

A system can mutate only training-visible state while using evaluation or protected information to decide *which* training state to mutate.

Similarly, an HC update gate could write only ordinary plastic state while consulting unauthorized continuity-bearing identity state, private person-model evidence, or future/held-out evidence to choose the update. Restricting the destination does not establish lawful or independent source information use.

`AUTHORIZED_DESTINATION != AUTHORIZED_SOURCE_INFORMATION`

`TRAINING_ONLY_WRITE_TARGET != TRAINING_ONLY_DECISION_ANCESTRY`

This is useful beyond ML evaluation: protected-information flow, privacy, authority, memory admission, and action governance all need source-information lineage as well as destination checks.

## Adversarial tests suggested

1. Hold all training nodes/features/labels fixed; permute only evaluation labels before preprocessing. If the training artifact changes, require evaluation-label ancestry to be recorded.
2. Hold evaluation labels fixed; alter evaluation features or graph structure and observe whether training topology/collapse changes; classify each visible information class separately.
3. Compare `constraint=FL` with a truly feature-only path and verify provenance changes with the executed configuration rather than the method name.
4. Compare two dataset entrypoints using the same preprocessor where one receives a train-only graph and the other receives a full graph; require separate evaluation-regime classifications.
5. Restrict the final write to training state but feed held-out labels into clustering/selection; require independence failure despite output-side restriction.
6. Feed a privileged HC state into a route selector while keeping the privileged field out of the final action payload; require causal ancestry to reveal the influence.
7. Set a nominal label-weight parameter to zero and verify by execution trace that labels truly have zero material influence rather than assuming configuration intent.
8. Remove evaluation labels entirely from an allegedly inductive preprocessing path; require equivalent training artifact/behavior within declared nondeterministic tolerance if labels are truly irrelevant.

## Evidence boundary

DOCUMENTED: FALCON feature-label constrained collapse framing and the documented meaning of `gamma`; Cora's source-level default configuration.

OBSERVED: `contract_graph` reads features and labels from all nodes supplied to it; feature-label KMeans cluster membership influences training-node contraction; Cora supplies a full graph before post-contraction split; PPI constructs separate train/validation/test graphs and contracts only the training graph.

INFERRED: Cora's inspected default feature-label preprocessing is evaluation-label-exposed for training-artifact construction; the correct HC transfer is path-specific source-information ancestry rather than a source-wide judgment about FALCON.

UNKNOWN: quantitative effect on published metrics; exact configuration of every reported experiment; whether other branches/revisions alter the path; publication-level interpretation; whether all non-Cora full-graph entrypoints share identical behavior without individual inspection.

## Transfer decision

PROMOTE CAUSAL SOURCE-INFORMATION ANCESTRY, LABEL/PREPROCESSING ISOLATION, AND ENTRYPOINT-SPECIFIC EVALUATION-REGIME RULES; DO NOT PROMOTE FALCON'S COLLAPSE MECHANISM AS AN HC PRIMITIVE OR GENERALIZE THE Cora PATH TO ALL FALCON EXPERIMENTS.
