# BASIRA uGNN Model-Graph Sharing and Execution-Path Study — 2026-09-10

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/uGNN`, default branch `main`.

Inspected artifacts:

- `README.md` blob `4dace49a0bc01d760c8433df383f4086bd229804`
- `ugnn/graphs/convert.py` blob `e73737d2b1e063e3f9f8ac2dc26551cce18737dd`
- `ugnn/graphs/unify.py` blob `0fe122bf6b3b967e4218b16d8037ba6f02c7d259`
- `ugnn/models/ugnn.py` blob `889f449009885fbf7cc824444a7d9bc4cd669260`
- `ugnn/scripts/train_ugnn_ws.py` blob `5a0746c8736eb6f1cdb603f5b903a86f600addb2`
- root `ugnn_new.py` blob `6d5940857ab383620f96aab4e51d97f6a0c6db05` was identified as a Colab-generated historical/monolithic artifact but was not used as evidence for the packaged-script path below.

This note records implementation patterns useful to HC architecture. It does not establish publication validity, reproduce reported experiments, or make uGNN an HC implementation requirement.

## DOCUMENTED source framing

The repository README describes uGNN as converting heterogeneous neural models into graph representations: model weights become edges, biases become nodes, and a unified GNN operates over a disjoint union of model-graphs. The documented weight-sharing variant uses shared learned controls over graphified model parameters so heterogeneous architectures can participate in one learning scheme.

The packaged quick-start training path is `ugnn/scripts/train_ugnn_ws.py`, despite the README's shorter displayed `scripts/...` path. The actual repository tree places the scripts under `ugnn/scripts/`.

## OBSERVED graphification and disjoint-union identity

`convert.py` graphifies MLPs and CNNs while retaining explicit positional metadata for weight-sharing correspondence.

For MLP linear edges, the weight-sharing key records `layer_num`, `target_idx`, and `source_idx`. For convolutional edges, the key records `layer_num`, output channel, input channel, and kernel coordinates.

`unify_ws` concatenates the graphified models into one disjoint union by applying node offsets while retaining per-model node/layer/input/output maps and a combined edge-to-kernel index.

This supports the distinctions:

`SHARED_CONTAINER != SHARED_REFERENT_IDENTITY`

`DISJOINT_UNION_MEMBERSHIP != SEMANTIC_PARAMETER_HOMOLOGY`

`POSITIONAL_PARAMETER_KEY != VERIFIED_SEMANTIC_ROLE`

A common graph container can preserve component boundaries while still permitting cross-model learned coupling through a higher-level grouping mechanism.

## OBSERVED weight-sharing correspondence mechanism

`UGNN_WS.__init__` constructs global grouping keys from positional metadata. Convolutional keys are effectively `('conv', layer_num, out_channel, in_channel, kernel_i, kernel_j)` and linear keys are `('linear', layer_num, target_idx, source_idx)`.

Equal keys across model-graphs are assigned one common kernel identity before possible compression into fewer theta groups.

This is an OBSERVED implementation mechanism, not proof that every equal positional key across heterogeneous architectures denotes the same semantic parameter role.

The existing HC rules therefore apply directly:

`SHAPE_COMPATIBLE_PARAMETER != SEMANTICALLY_HOMOLOGOUS_PARAMETER`

`SAME_POSITIONAL_ROLE_KEY != VERIFIED_SEMANTIC_HOMOLOGY`

`WEIGHT_SHARING_GROUP != AUTHORITY_OR_IDENTITY_FUSION`

For HC, heterogeneous state sharing that matters to cognition, continuity, values, authority, or protected state must preserve explicit state-family and semantic-role correspondence rather than treating positional coincidence as sufficient.

## OBSERVED packaged training path

The packaged `ugnn/scripts/train_ugnn_ws.py` imports and instantiates `UGNN_WS`, calls `unify_ws`, and passes that model to `train_unified_gnn`.

No use of `UGNNModelSpecific` occurs in that packaged training script.

Therefore the `UGNNModelSpecific` observation below is source-level evidence about an exposed implementation variant, not evidence that the documented packaged `UGNN_WS` quick-start path executes that variant.

## OBSERVED model-specific execution-path anomaly

The packaged `UGNNModelSpecific` class constructs per-model trainable theta groups and its `_update_edge_bias` method calculates updated edge and bias tensors.

However its inspected `forward` method:

1. calls `_update_edge_bias()` and assigns the results to `upd_e, upd_b`;
2. initializes an all-zero hidden-state tensor;
3. writes only model inputs into input-node positions;
4. never calls `propagate`, `message`, `aggregate`, or another operation that uses `upd_e` or `upd_b`;
5. reads each model's output-node slice directly from the hidden-state tensor and returns it.

For graphified feed-forward models whose output nodes are distinct from their input nodes, the inspected method therefore provides no path by which its computed parameter updates or input activations reach output nodes.

The narrow source observation is:

`COMPUTED_UPDATE != CONSUMED_UPDATE`

`TRAINABLE_PARAMETER_PRESENT != OUTPUT_DEPENDS_ON_PARAMETER`

`MESSAGE_PASSING_METHOD_DEFINED != MESSAGE_PASSING_EXECUTED`

`DECLARED_VARIANT_CAPABILITY != VERIFIED_VARIANT_EXECUTION_PATH`

This is a static code-path observation. We did not execute the repository. It is UNKNOWN whether another historical source path, unretrieved revision, local experimental script, or downstream user invokes a repaired/alternate implementation.

The packaged quick-start script's use of `UGNN_WS` prevents promotion of this finding into a claim about the documented packaged uGNN training path or publication results.

## HC transfer: causal output dependence

A component can expose the right parameters, helper methods, interfaces, names, and update calculations while its material output does not depend on them.

Consequential HC qualification must establish causal dependence between the mechanism claimed to operate and the output/state/effect used downstream.

General rules:

`COMPUTED_STATE != EFFECTIVE_STATE_WITHOUT_CONSUMPTION`

`LEARNABLE_PARAMETER != BEHAVIORALLY_EFFECTIVE_PARAMETER`

`REGISTERED_COMPONENT != CAUSALLY_ACTIVE_COMPONENT`

`METHOD_AVAILABLE != METHOD_EXECUTED`

`INTERMEDIATE_UPDATE_CREATED != UPDATE_REACHES_OUTPUT_OR_MUTATION_BOUNDARY`

This extends executed-dataflow verification beyond choosing the correct input or strategy: a claimed transformation itself must reach the material output or state mutation.

## HC transfer: heterogeneous model-state sharing

Graphifying unlike mechanisms into one common representation can be useful without implying that all graph coordinates are semantically interchangeable.

A safe HC transfer should distinguish common representation/container identity, component/model identity, parameter/state family, semantic role, coordinate or positional key, sharing-group membership, learned influence ancestry, and protected-state eligibility/authority.

A sharing mechanism may propose correspondence. It does not establish it merely by assigning a common group ID.

## Adversarial tests suggested

1. **Dead-update sentinel** — force a large, unique change in a claimed learned parameter/update and verify the material output changes through the declared causal path.
2. **Helper-not-called trap** — define a correct transformation helper but bypass it in `forward`; require execution-path qualification to fail despite the helper's existence.
3. **Zero-path output** — initialize intermediate state to zero, write only inputs, skip propagation, then read distinct output nodes; require output-dependence instrumentation to detect the missing path.
4. **Same-key/different-role** — create heterogeneous model parameters with identical positional sharing keys but intentionally different semantic roles; require correspondence validation before shared durable update.
5. **Common-container fusion** — place several components into one unified graph/container and verify their referent identities, provenance, authority, and protected state remain distinct unless an explicit relation says otherwise.
6. **Group-ID laundering** — assign two unrelated state items to the same learned sharing group and verify the group ID alone cannot establish semantic equivalence or protected-update eligibility.
7. **Variant reachability** — expose several implementation variants and verify qualification reports only the variant actually instantiated on the tested path.
8. **Parameter perturbation dependency** — perturb one claimed effective parameter while holding inputs fixed and verify a detectable output/state dependency within the claimed scope; zero dependency where nonzero influence is claimed is a failure.

## Transfer decision

PROMOTE GENERAL EXECUTED-TRANSFORMATION / OUTPUT-DEPENDENCE VERIFICATION AND REINFORCE HETEROGENEOUS PARAMETER-ROLE CORRESPONDENCE. DO NOT PROMOTE uGNN ITSELF OR THE SOURCE-SPECIFIC `UGNNModelSpecific` ANOMALY INTO HC ARCHITECTURE.

## Evidence boundary

DOCUMENTED: uGNN's repository framing, model-to-graph representation, unified-learning purpose, and packaged weight-sharing quick-start description.

OBSERVED: graphification metadata, disjoint-union offset construction, positional weight-sharing keys, `UGNN_WS` packaged-script instantiation, and the inspected `UGNNModelSpecific.forward` dataflow described above.

INFERRED: equal positional keys across heterogeneous models are insufficient by themselves to prove semantic state homology; causal output-dependence verification is a useful general HC conformance requirement.

UNKNOWN: runtime behavior of unexecuted paths, use of the model-specific variant in unpublished/historical experiments, publication-level impact, and whether alternate revisions repair or replace the inspected model-specific path.
