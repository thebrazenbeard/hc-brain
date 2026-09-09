# BASIRA Federation, Heterogeneity, and Aggregation Scour — 2026-09-09

Status: research/provenance only. This note compares several BASIRA federation approaches as sources of aggregation, heterogeneity, lineage, and qualification constraints. It does not promote federated learning as HC distributed-organ topology and copies no source code.

## Exact source bindings and read depth

- `basiralab/reproducibleFedGNN main@c547b38358c000be2505fd438fa8782973c6ba38` — deep code read; detailed separately in `BASIRA_FEDERATED_REPRODUCIBILITY_CODE_SCOUT_2026-09-09.md`.
- `basiralab/Fed-CBT main@c85520ebd536153af1005454b48ca5fdb2cff3af` — README + config + main federated driver/aggregation code deep read.
- `basiralab/RepFL main@472723eb4519dd34b16ce78d2dd81ffa459e48a6` — README + constants + server + client + preprocessing + dataset + train-driver code deep read.
- `basiralab/UniFed main@f2a410d558350ef9c7567ea47877eb3ad6e19f00` — README/method framing + repository inventory; notebook implementation not treated as fully code-audited in this cut.

All four inspected repositories expose root license artifacts at the checked cuts. This note still copies no implementation code.

## 1. Federation is a policy family, not one operation

The source family spans materially different exchange mechanisms:

- `reproducibleFedGNN`: equal arithmetic averaging of homologous model parameters after local updates;
- `Fed-CBT`: configurable client participation plus optional temporal/freshness weighting of homologous DGN parameters;
- `RepFL`: selective aggregation of declared homologous layers across heterogeneous-resolution model architectures, plus replicas and other federation baselines;
- `UniFed`: source-described loss-guided dynamic and sequential server/client model exchange across highly heterogeneous classification tasks.

Therefore:

`FEDERATION != FEDAVG`

`MODEL_EXCHANGE != EVIDENCE_FUSION`

`PARAMETER_COMPATIBILITY != COGNITIVE_EQUIVALENCE`

`SHARED_LAYER != SHARED_SEMANTICS_BY_DEFAULT`

`SERVER_AGGREGATE != CONSENSUS_TRUTH`

Any future HC distributed-learning mechanism should type the exchange/aggregation policy explicitly rather than representing all multi-source learning as one generic merge.

## 2. Fed-CBT — temporal weighting is a useful mechanism with a dangerous interpretation boundary

### OBSERVED code behavior

`demo.py::get_averaged_weights()` can assign client weights using a recency function based on `current_epoch - last_updated_epoch`. Under `temporal_weighting`, more recently updated clients receive greater aggregation weight. Under ordinary averaging, participating clients receive equal weights.

This is a potentially useful HC mechanism for stale distributed model state: currentness can affect how strongly a model update participates in an aggregate.

But:

`RECENT_UPDATE != MORE_TRUE`

`FRESH_MODEL_STATE != HIGHER_EPISTEMIC_AUTHORITY`

`STALE_UPDATE != FALSE_UPDATE`

`TEMPORAL_WEIGHT != EFFECT_AUTHORITY`

Freshness is one aggregation dimension. Reliability, coverage, domain relevance, uncertainty, evidence quality, protected-state status, and adversarial/fault state remain separate.

### OBSERVED cardinality coupling

The temporal-weighting implementation computes its denominator from exactly `getWeight_i(0) + getWeight_i(1) + getWeight_i(2)`, and `last_updated_dict` is initialized with exactly `client0`, `client1`, and `client2`. `config.py` also defaults `number_of_samples = 3`.

Thus the inspected temporal-weighting path is structurally coupled to three clients even though surrounding helper functions accept `number_of_samples`.

`FUNCTION_PARAMETERIZED != IMPLEMENTATION_CARDINALITY_GENERIC`

This independently reinforces the cardinality-adversarial control found in `reproducibleFedGNN`.

### OBSERVED held-out evaluation use

Inside `train_kfold()`, the fold-level `all_test_data` is cast to `test_casted` before the epoch loop. Client validation calls repeatedly use that `test_casted` set during training, losses are logged from it, candidate model weights are saved using those values, and early-stop behavior is driven by those sequences.

For the literal inspected path, the nominal test fold participates in model selection/training control.

`TEST_NAMED_SPLIT != SEALED_FINAL_HOLDOUT`

This is consistent with the DGN code-level finding and strengthens the need for split-role machine metadata rather than relying on variable names such as `test`.

## 3. RepFL — heterogeneous models suggest homologous-state exchange rather than whole-model averaging

### OBSERVED architectural mechanism

RepFL uses clients at different target resolutions and therefore different generator classes. The server does not assume every model parameter is globally homologous. `constants.aggregating_layers` lists a bounded subset of parameter names eligible for server aggregation, while broader sets may participate in other exchange modes such as daisy-chain transfer.

This is more transferable to HC than naïve global state averaging:

`LOCAL_SPECIALIZATION != AGGREGATION_INELIGIBLE`

`PARTIAL_HOMOLOGY != WHOLE_MODEL_EQUIVALENCE`

`SHARED_PARAMETER_NAME != PROVEN_SHARED_FUNCTION`

A future HC update-exchange layer could declare **exchange-compatible state families** explicitly while preserving subsystem-specific local state.

Candidate research object:

```text
STATE_EXCHANGE_COMPATIBILITY {
  source_component_ref
  target_component_ref
  source_revision
  target_revision
  transferable_state_families[]
  nontransferable_state_families[]
  semantic_or_functional_compatibility_basis
  shape_or_schema_compatibility
  calibration_or_translation_ref
  qualification_refs[]
  provenance
}
```

Do not infer compatibility solely because tensors have matching dimensions/names.

## 4. RepFL replicas — diversity generation is not independent evidence

The source-described RepFL mechanism creates replicas of each client and perturbs local training datasets. `SGRepGenerator` recursively constructs replicas for anchor clients and `set_training_data()` removes different contiguous sample ranges from replica datasets according to the configured perturbation percentage/offset.

This can create useful training diversity, but the replicas share architecture, ancestry, original dataset, and parent initialization.

`REPLICA != INDEPENDENT_PARTICIPANT`

`PERTURBED_SUBSET != INDEPENDENT_EVIDENCE_SOURCE`

`MULTIPLE_REPLICAS != MULTIPLE_CAUSALLY_INDEPENDENT_CONFIRMATIONS`

For HC evaluation, synthetic/replica descendants must retain common-parent/common-data provenance so repeated agreement does not get counted as independent corroboration.

## 5. RepFL OBSERVED implementation defect — replica averaging appears double-scaled

`SGRepGenerator.aggregate_replicas()` sets:

`weight = 1 / (1 + NUMBER_REPLICAS)`

It then multiplies every replica tensor and the anchor tensor by `weight`, stacks those already-weighted tensors, and calls `torch.stack(...).mean(dim=0)`.

For `R` replicas plus one anchor, that computes conceptually:

`(1/(R+1)) * mean(x_0...x_R) = sum(x_i)/(R+1)^2`

rather than ordinary equal averaging `sum(x_i)/(R+1)`.

This is an OBSERVED arithmetic property of the inspected implementation. It may be accidental or may be compensated elsewhere, but no compensation is visible in the inspected aggregation function itself.

HC hostile control:

`DECLARED_AGGREGATION_WEIGHT != EFFECTIVE_NUMERICAL_WEIGHT`

Qualification should compare declared aggregation semantics against an analytically known toy case so a second hidden normalization/division cannot pass unnoticed.

## 6. RepFL OBSERVED implementation defect — target graphs are built from source arrays

`SGRepGenerator.set_training_data(X_train_source, X_train_target, ...)` deep-copies both arguments, but later builds:

- source graphs from `X_train_source` at resolution 35;
- target graphs from **`X_train_source` again** at the target resolution.

`SGRepGenerator.test(X_test_source, X_test_target)` does the same pattern: target graphs are constructed from `X_test_source`, not `X_test_target`.

`utils.utils.read_and_preprocess_files()` makes the mismatch concrete in the provided simulation:

- source vectors: length `595` (35-node lower triangle);
- target 160 vectors: length `12720`;
- target 268 vectors: length `35778`.

`utils.preprocess.convert_vector_to_graph()` assigns the supplied vector into the lower triangle for the **requested resolution**. Therefore a 595-element source vector cannot faithfully instantiate a 160/268 target lower triangle.

`dataset_brain_connectomes.MultiResolutionBrainConnectomeDataset` subsequently treats those generated target graph matrices as `target_x`.

This is a code-path defect at the inspected repository cut, not a criticism of the RepFL paper claim as a whole.

HC hostile controls:

- source/target lineage identity must be explicit;
- generated training targets must prove ancestry to the declared target evidence;
- a test harness should inject source and target tensors with deliberately incompatible sentinel patterns so accidental source reuse is detected immediately.

`TARGET_ARGUMENT_PRESENT != TARGET_ARGUMENT_USED`

`SOURCE_REUSED_AS_TARGET != SUPERVISED_TARGET_EVIDENCE`

## 7. RepFL OBSERVED driver/interface mismatches

The inspected `SGRepGenerator` defines `train(self)` with no external data arguments and `run_one_round()` returns one training-loss sequence.

The inspected `train/train_slim.py` contains paths that:

- call `train(X_train_source, X_train_target*)` in the FedDC routine;
- unpack `run_one_round()` into two values in the RepFL routine.

Those calls do not match the inspected class signatures.

This is strong evidence for a general HC qualification rule:

`ARCHITECTURE_OR_PAPER_COHERENCE != REPOSITORY_RUNTIME_COHERENCE`

Before promoting an external method as implementation-ready, perform interface-level executable or static compatibility checks across the actual called path, not only method/paper review.

## 8. UniFed — heterogeneous task federation should not be forced into one shared ontology

### DOCUMENTED source framing only for this cut

UniFed describes a loss-guided dynamic/sequential exchange process across clients performing highly heterogeneous medical-image classification tasks, including strongly and moderately non-IID splits. The README frames the method as agnostic to task complexity and intended to improve communication cost/convergence while accommodating heterogeneous tasks.

Because the notebook implementation was not fully code-audited in this cut, no stronger implementation claim is made here.

The useful HC hypothesis is:

`HETEROGENEOUS_TASKS != REQUIRE_SINGLE_IDENTICAL_LOCAL_OBJECTIVE`

A distributed HC or multi-subsystem learner may exchange transferable state while retaining subsystem-specific objectives, representations, maturity, and local constraints.

Any dynamic exchange rule based on loss or convergence must preserve:

`HIGH_LOSS != HIGH_AUTHORITY`

`SLOW_CONVERGENCE != GREATER_TRUTH`

`TASK_DIFFICULTY != GLOBAL_PRIORITY`

`MODEL_TRANSFER != STATE_OWNERSHIP_TRANSFER`

## 9. Cross-family synthesis — aggregation needs a declared semantics object

Across these sources, an aggregation/exchange event can vary along independent axes:

```text
DISTRIBUTED_UPDATE_EXCHANGE {
  parent_revision_or_state_refs[]
  contributor_refs[]
  contributor_roles[]
  local_objectives[]
  local_data_or_experience_scope[]
  local_model_or_state_revisions[]
  exchange_compatible_state_families[]
  aggregation_or_exchange_policy
  effective_numerical_weights[]
  freshness_or_last_update_state[]
  availability_or_participation_state[]
  heterogeneity_description
  replica_or_shared_ancestry_refs[]
  disagreement_or_uncertainty
  candidate_result_ref
  qualification_refs[]
  protected_update_required
  provenance
}
```

This is a research sketch, not canonical machine schema.

The important point is that **the policy itself is evidence-relevant state**.

`AGGREGATE_RESULT_WITHOUT_AGGREGATION_PROVENANCE != FULLY_INTERPRETABLE_UPDATE`

## 10. Proposed hostile controls

1. **Equal-vs-size weighting:** same client updates under equal and sample-count weighting; report policy dependence.
2. **Freshness-vs-quality conflict:** newer low-quality update versus older strongly supported update; freshness must not become truth.
3. **Client-count mutation:** run at 2, 4, 7 clients to expose hidden three-client assumptions.
4. **Partial homology:** two client architectures share one state family but differ elsewhere; only qualified shared state may transfer.
5. **Shape coincidence:** same tensor shape/name but intentionally different semantics; exchange must be rejected without compatibility basis.
6. **Replica independence illusion:** five replicas from one parent/data source agree; count shared ancestry rather than five independent confirmations.
7. **Double-normalization toy case:** aggregate identical scalar parameters and verify effective output equals declared aggregation policy exactly.
8. **Source-as-target sentinel:** source and target arrays carry incompatible marker values; training target lineage must point to the actual target.
9. **Interface compatibility:** statically/dynamically verify call signatures and return arity before declaring an external implementation runnable.
10. **Sequential exchange order:** change client order under a sequential exchange policy; expose order sensitivity rather than hiding it.
11. **Minority preservation:** aggregation improves mean performance while destroying one rare/high-consequence capability; global score must not erase minority failure.
12. **Protected update leak:** a distributed learned aggregate attempts to rewrite protected HC architecture/currentness/authority directly; it must remain a candidate until canonical update governance accepts it.

## 11. HC transfer disposition

**KEEP as high-value research/provenance.**

The strongest transfer is not any one federation algorithm. It is the requirement that HC distributed learning explicitly represent:

- what state was exchanged;
- why those states were considered compatible;
- what aggregation/exchange policy was used;
- effective numerical contribution, not just intended weight;
- recency/availability separately from evidence quality/authority;
- shared ancestry/replica dependence;
- heterogeneity and minority failure;
- sealed qualification evidence;
- protected-update handoff.

No canonical architecture change is made by this note alone.