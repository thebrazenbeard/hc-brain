# BASIRA RepFL Replica Ancestry and Target-Dataflow Study — 2026-09-09

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/RepFL`, default branch `main`.

Inspected artifacts:

- `README.md` blob `f6a0f916027ef1690da648121fe9f2212fa07f6c`
- `train/train_slim.py` blob `21cc611bb7ba17f044fb556d19d2ec7d22e16c2a`
- `client/SGRepGenerator.py` blob `a4d62f65ee77c09b438df05a1b192d6338166e45`
- `server/FederatedServer.py` blob `4f149cef17010243d937a9a8d1615e2d546c86f5`
- `models/generators.py` blob `9d85f9d4919413185e43cca32c2adc7ea3263e2d`
- `dataset/dataset_brain_connectomes.py` blob `33098de35901801b1f104f8bbb42370817060739`
- `utils/preprocess.py` blob `0824780e7f78adf05eda47c676e22fc30d1aa5c8`
- `utils/utils.py` blob `8125b9f0ae28315a51ff0dea94e95e2eb2bc4490`
- `constants.py` blob `21fafc89e5c22f7e66ae56f6d8e70ebb17b15c09`

This note records implementation patterns useful to HC architecture. It does not establish publication validity, reproduce reported experiments, or make RepFL an HC implementation requirement.

## DOCUMENTED source framing

The repository README describes RepFL as a replica-based federated-learning approach for heterogeneous graph-super-resolution models. Each participating client is given replicas by copying the model architecture and perturbing its local training dataset. Anchor and replica models are later aggregated, and the method is intended to diversify client data distributions while learning from limited decentralized data.

The README exposes simulated samples with a 35-region source graph and target graphs at resolutions 160 and 268.

## OBSERVED replica ancestry

`SGRepGenerator.__init__` creates `NUMBER_REPLICAS` replica objects for a non-replica anchor when `fed_alg == "RepFL"`.

`set_training_data` begins replicas from copies of the same anchor-local source and target arrays, then removes a configured contiguous subset for each replica. Therefore the replica training sets are transformed descendants of one client-local source population rather than independent source populations.

This directly demonstrates:

`REPLICA_COUNT != INDEPENDENT_SOURCE_COUNT`

`PERTURBED_OR_SUBSET_COPY != NEW_OBSERVATION_SOURCE`

`REPLICA_MODEL != INDEPENDENT_MODEL_ANCESTRY`

The replicas can still provide useful diversity. The forbidden inference is that multiplying correlated descendants multiplies independent evidence.

## OBSERVED heterogeneous shared-layer aggregation

`models/generators.py` defines two heterogeneous generators. `Generator1` maps the common 35-node input through a 35-dimensional first graph-convolution stage and then to 160 dimensions. `Generator2` begins with an architecturally matching 35-dimensional first stage, continues through the same 160-dimensional intermediate stage, and adds a third stage to 268 dimensions.

`constants.py` limits ordinary `aggregating_layers` to selected `conv1` parameters. `FederatedServer.federated_average_intermodality` aggregates only those named parameters across clients.

This is a positive source pattern for heterogeneous model transfer: the implementation does not naively attempt to average every parameter across unequal architectures. It selects a shared prefix whose names and tensor structures correspond in the inspected source.

The general HC transfer is stricter than name/shape compatibility:

`SHAPE_COMPATIBLE_PARAMETER != SEMANTICALLY_HOMOLOGOUS_PARAMETER`

`SAME_PARAMETER_NAME != SAME_ARCHITECTURAL_ROLE_WITHOUT_CORRESPONDENCE`

`HETEROGENEOUS_TRANSFER_REQUIRES_EXPLICIT_PARAMETER_ROLE_MAPPING`

A heterogeneous HC update path should establish that transferred state has compatible semantic role, coordinate system, state family, version, and intended downstream meaning—not merely that an assignment operation succeeds.

## OBSERVED anchor/replica aggregation semantics

`run_one_round` trains the anchor and its replicas, then calls `aggregate_replicas`.

The inspected `aggregate_replicas` implementation declares that anchors and replicas receive equal weights. It computes:

```text
weight = 1. / (1 + NUMBER_REPLICAS)
```

multiplies every anchor/replica selected-layer tensor by that weight, stacks the already weighted tensors, and then applies `.mean(dim=0)`.

For `N = 1 + NUMBER_REPLICAS` contributors, this expression computes `sum(parameters) / N^2`, not the ordinary equal-weight mean `sum(parameters) / N`.

This is an OBSERVED static implementation expression and a useful execution-path fixture:

`NAMED_EQUAL_WEIGHT_AGGREGATION != VERIFIED_EFFECTIVE_WEIGHT_SEMANTICS`

It is not promoted here into a claim about the paper's empirical results. Whether another source revision, intended scaling convention, later normalization, or released experiment path changes the effect is UNKNOWN without execution-level reproduction.

By contrast, `FederatedServer.federated_average_intermodality` stacks selected client tensors and applies a single mean, providing a separate implementation path whose numerical operation differs from the anchor/replica aggregation expression.

## OBSERVED target-dataflow mismatch

`train/train_slim.py` passes distinct source and target arrays into `SGRepGenerator.set_training_data`, selecting the 160- or 268-resolution target according to client resolution.

Inside `set_training_data`, however, the inspected source constructs both transformed inputs from `X_train_source`:

```text
X_casted_train_source = convert_list_of_vectors_to_graphs(X_train_source, resolution=35)
X_casted_train_target = convert_list_of_vectors_to_graphs(X_train_source, resolution=self.resolution)
```

The provided `X_train_target` argument is copied and subsetted but is not used in the target conversion expression.

The `test` method has the analogous pattern: it accepts `X_test_source, X_test_target`, then constructs the target graph from `X_test_source` rather than `X_test_target`.

Therefore:

`TARGET_ARGUMENT_PRESENT != TARGET_DATA_EXECUTED`

`EVALUATION_TARGET_PROVIDED != EVALUATION_TARGET_USED`

`METHOD_SIGNATURE != DATAFLOW_PROOF`

`NOMINALLY_SUPERVISED != VERIFIED_TARGET_BINDING`

## OBSERVED source/target dimensional distinction

`utils/utils.py` creates distinct arrays with these simulated-data shapes:

- source: `(279, 595)`;
- resolution-160 target: `(279, 12720)`;
- resolution-268 target: `(279, 35778)`.

Those widths equal the lower-triangle element counts for 35, 160, and 268 nodes respectively.

`convert_vector_to_graph` allocates an `resolution x resolution` matrix and assigns the supplied vector into `np.tril_indices(resolution, -1)`.

A local deterministic NumPy probe reproducing that exact assignment pattern found:

- 595 values into a 35-node lower triangle: succeeds because the destination length is 595;
- 595 values into a 160-node lower triangle: raises `ValueError` because the destination length is 12720;
- 595 values into a 268-node lower triangle: raises `ValueError` because the destination length is 35778.

This local probe is OBSERVED execution evidence for NumPy assignment semantics, not execution of the full RepFL repository.

Combined with the source read, it supports the narrower conclusion that the inspected target-conversion expression is dimensionally incompatible with the simulated source-vector width for the documented 160/268 target resolutions if that path executes as shown.

UNKNOWN remains whether the published experiments used this exact source cut/path, whether unretrieved revisions differ, and what effect any corrected path has on reported results.

## HC transfer: executed dataflow is evidence

For consequential HC computation, an argument name, type annotation, schema field, configuration value, or function signature does not establish that the intended state actually reaches the material operation.

Qualification should trace the concrete path from source identity through transformation to loss, metric, memory admission, state update, action candidate, or protected effect.

General rules:

`DECLARED_INPUT != EXECUTED_INPUT_WITHOUT_PATH_VERIFICATION`

`TARGET_PARAMETER != VERIFIED_TARGET_BINDING`

`EXPECTED_TARGET_SOURCE != ACTUAL_TARGET_SOURCE_WITHOUT_TRACE`

`OUTPUT_SCORE != CORRECT_INPUT_BINDING`

A pipeline can produce syntactically valid outputs while using the wrong source, target, mask, authority record, memory record, body channel, timepoint, model branch, or provenance object.

## HC transfer: replica and synthetic-descendant independence

Replicas, bootstraps, perturbations, augmentations, generated variants, and resampled descendants may be useful for robustness and variance estimation. Their ancestry must remain explicit when independence matters.

`GENERATED_OR_PERTURBED_VARIANTS != INDEPENDENT_SOURCE_OBSERVATIONS`

`MODEL_DIVERSITY != EVIDENCE_INDEPENDENCE`

`MULTIPLE_REPLICA_VOTES != MULTIPLE_INDEPENDENT_OBSERVERS`

This aligns distributed-learning ancestry with qualification-evidence isolation: variants of one source or one learned ancestor cannot be silently counted as independent holdouts or independent corroborators.

## HC transfer: named aggregation versus effective influence

A configured coefficient or comment describing equal weighting does not by itself establish effective contribution weight after all transforms, averaging, normalization, clipping, sparsification, routing, or repeated aggregation.

`DECLARED_WEIGHT != EFFECTIVE_INFLUENCE_WITHOUT_EXECUTION_TRACE`

For consequential distributed updates, effective influence should be testable at the actual update boundary. This is especially important when protected state or authority-bearing decisions depend on contributor weighting.

## Adversarial tests suggested

1. Create five replicas from one source dataset and require independence accounting to retain their shared source ancestry.
2. Generate many perturbed descendants from one observation and verify independent support count does not increase automatically.
3. Give heterogeneous model branches parameters with matching shapes/names but deliberately different architectural semantics; require transfer rejection until a role/correspondence map is established.
4. Pass distinct `source` and `target` fixtures to a pipeline, intentionally wire `source` into the target transform, and require path-level qualification to fail even if signatures and shapes elsewhere look plausible.
5. Pass a sentinel target whose value cannot arise from source preprocessing; require the executed loss/metric path to prove that sentinel reaches the intended target position.
6. Provide two target arguments with different stable IDs while only one should be used; verify provenance reports the actually consumed target.
7. Configure equal aggregation weights and inject basis-vector contributor parameters; verify measured effective output coefficients match the declared weights.
8. Apply a weight and then an additional mean; require effective-influence instrumentation to detect the extra scaling.
9. Give several replica models identical ancestry but divergent stochastic perturbations; verify diversity is not promoted to observation independence.
10. Supply the correct evaluation target argument but deliberately consume a source-derived surrogate; require evaluation evidence to be invalidated for the claimed target task.
11. Correct a target-dataflow defect after seeing evaluation outcomes; reclassify the old evaluation cases as regression evidence rather than untouched final holdout evidence for the repaired successor.

## Transfer decision

PROMOTE GENERAL REPLICA-ANCESTRY, HETEROGENEOUS-PARAMETER CORRESPONDENCE, TARGET-DATAFLOW, AND EFFECTIVE-AGGREGATION VERIFICATION RULES; DO NOT PROMOTE REPFL ITSELF OR SOURCE-SPECIFIC DEFECT CLAIMS INTO HC ARCHITECTURE.

## Evidence boundary

DOCUMENTED: RepFL goals, replica framing, heterogeneous graph-super-resolution task, and source/target resolutions from the repository README.

OBSERVED: replica construction and dataset subsetting; heterogeneous generator structures and selected shared-layer aggregation; anchor/replica aggregation expression; client aggregation expression; distinct source/target array widths; target argument passed by caller; target conversion using source data in train and test methods; NumPy lower-triangle assignment semantics in a local deterministic probe.

INFERRED: the inspected target-conversion path is incompatible with the documented simulated source-vector width at 160/268 resolution if executed as shown; general HC rules for replica ancestry, heterogeneous parameter correspondence, executed target binding, and effective contributor influence.

UNKNOWN: publication-level impact, whether published results used exactly this code cut, whether unretrieved revisions repair the path, and quantitative effects of the aggregation expression.
