# Executed Dataflow and Binding Integrity

Status: canonical identity-neutral architecture contract.

## Purpose

The HC may declare the correct source, target, authority, memory record, timepoint, body channel, model branch, state family, or evaluation split at an interface while the executed implementation later consumes a different object or crossed an information boundary earlier. Type correctness, matching shapes, function signatures, configuration surfaces, split labels, and plausible output values do not establish semantic binding.

For consequential computation, qualification must therefore establish not only **what the system says an input is**, but **which concrete state actually reaches the material operation and which upstream information shaped that state before it arrived**.

The governing rule is:

> **Declared dataflow is not execution evidence. Consequential bindings must be traceable from stable source identity and information visibility through transformation to the operation that consumes or mutates state.**

## Core separations

`DECLARED_INPUT != EXECUTED_INPUT_WITHOUT_PATH_VERIFICATION`

`TARGET_ARGUMENT_PRESENT != TARGET_DATA_EXECUTED`

`TARGET_PARAMETER != VERIFIED_TARGET_BINDING`

`METHOD_SIGNATURE != DATAFLOW_PROOF`

`CONFIGURED_STRATEGY != EXECUTED_STRATEGY_WITHOUT_PATH_VERIFICATION`

`DECLARED_SPLIT_STAGE != ACTUAL_INFORMATION_FLOW_BOUNDARY`

`LATER_SPLIT != EARLIER_INFORMATION_ISOLATION`

`TRAIN_ONLY_FINAL_TENSOR != TRAIN_ONLY_DERIVATION_ANCESTRY`

`SAME_SHAPE != SAME_SEMANTIC_ROLE`

`TYPE_COMPATIBLE != REFERENTIALLY_CORRECT`

`SUCCESSFUL_EXECUTION != CORRECT_DATAFLOW`

`OUTPUT_SCORE != CORRECT_INPUT_BINDING`

`EVALUATION_TARGET_PROVIDED != EVALUATION_TARGET_USED`

`AUTHORITY_RECORD_AVAILABLE != AUTHORITY_RECORD_CHECKED`

`CURRENT_MEMORY_RECORD_LOADED != CURRENT_MEMORY_RECORD_CONSUMED`

## Material binding classes

Bindings deserve path-level verification when an error could change a consequential claim or effect. Examples include:

- observation ↔ represented entity;
- feature/source ↔ label/target;
- forecast ↔ target timepoint;
- body sensor channel ↔ body-state referent;
- action command ↔ actuator/effect target;
- actor/request ↔ authority or consent record;
- current-state selector ↔ memory record;
- semantic proposition ↔ supporting evidence;
- protected-update request ↔ state family being mutated;
- model/configuration selection ↔ executed strategy;
- contributor ↔ effective aggregation influence;
- qualification case ↔ expected result/ground truth;
- evaluation partition ↔ preprocessing visibility ancestry;
- correction ↔ dependency descendants.

Not every low-consequence local transform requires heavyweight tracing. The required fidelity is proportional to consequence and ambiguity.

## Binding lineage

A consequential executed path should permit recovery of a record such as:

```text
DATAFLOW_BINDING {
  operation_id
  execution_id
  semantic_role
  declared_input_id
  stable_referent_id
  source_artifact_or_state_id
  source_index_space_id
  source_partition_ids[]
  information_classes_visible[]
  transforms[]
  branch_or_strategy_id
  actually_consumed_object_id
  actually_consumed_referent_id
  output_or_mutation_target_id
  state_family
  authority_context
  chronology_context
  provenance
  instrumentation_or_test_ref
}
```

The implementation schema may differ. The semantic requirement is that the system can establish whether the object consumed at the material boundary is the intended referent under the intended role and whether its derivation respected the claimed information boundary.

## Referential integrity across transforms

Reference identity and dataflow are complementary concerns.

Stable IDs can be preserved correctly at one layer while a later function consumes the wrong variable. Conversely, the correct variable may be passed while its positional correspondence has already drifted.

Therefore a conforming path must account for both:

1. **referential lineage** — which entity/state the object represents; and
2. **execution lineage** — which object, information visibility, and transforms actually reached the operation.

`CORRECT_VARIABLE_NAME != CORRECT_REFERENT`

`CORRECT_REFERENT_METADATA != PROOF_OBJECT_WAS_CONSUMED`

If either lineage is unresolved where consequential, the binding is `UNKNOWN` rather than assumed correct.

## Source and target binding

Training, calibration, comparison, prediction evaluation, reconciliation, and error measurement depend on correct source/target separation.

A caller supplying a distinct target does not prove downstream code uses it. A transform that derives both source and target from the same upstream object may still produce syntactically valid objects in some dimensions while violating the intended task.

`NOMINALLY_SUPERVISED != VERIFIED_TARGET_BINDING`

`EXPECTED_TARGET_SOURCE != ACTUAL_TARGET_SOURCE_WITHOUT_TRACE`

Where the target is consequential, qualification should use discriminating fixtures that make source/target substitution observable.

## Evaluation split and preprocessing binding

A declared train/validation/test split is not necessarily the earliest information-flow boundary.

A topology, normalization statistic, template, manifold, embedding, calibration state, feature mask, nearest-neighbor index, generated representation, or routing policy may be derived from a broader cohort before the final records are split. If that derived artifact later influences training or inference, its source-partition ancestry remains part of the executed path.

`SPLIT_BEFORE_SCORING != SPLIT_BEFORE_ALL_INFLUENCE`

`TRAIN_GRAPH_OUTPUT != TRAIN_ONLY_PREPROCESSING_ANCESTRY`

`UNLABELED_EVALUATION_STRUCTURE_VISIBLE != NO_EVALUATION_EXPOSURE`

This does not mean unlabeled transductive preprocessing is inherently invalid. It means the executed information boundary must match the declared qualification/deployment regime.

For an `INDUCTIVE_FROZEN` claim, consequential fitted or constructed preprocessing state used by training should be derivable without the current evaluation cohort unless the scope explicitly says otherwise.

A robust test holds training-visible inputs fixed, perturbs only evaluation-cohort structure or values, recomputes preprocessing, and observes whether any training-time artifact changes. If it does, the path has evaluation-cohort ancestry even if the final training tensor contains only training rows.

## Authority and effect binding

The same problem applies to control, consent, and protected effects.

A request can contain a valid authority token while a downstream effect path checks a stale token, another actor's token, a cached authorization, or no token at all.

An action can be correctly authorized while the emitted actuator binding points to a different target.

`AUTHORIZED_REQUEST != CORRECTLY_BOUND_EFFECT`

`CORRECT_EFFECT_TARGET != AUTHORIZED_EFFECT`

Both authorization and target binding must hold.

## Memory and currentness binding

A memory query can retrieve the intended record while a later selector or renderer consumes a stale sibling, historical predecessor, top-ranked retrieval, or positional neighbor.

`RETRIEVED_CORRECT_RECORD != EXECUTED_CURRENT_STATE_BINDING`

Currentness, record identity, and execution path must remain jointly recoverable where the result influences belief, identity continuity, or action.

## Strategy and branch binding

Configuration values, feature flags, dependency injection, selected strategy objects, and parsed modes are declarations until the effect path demonstrates their use.

A later hard-coded call, fallback, shadow route, stale closure, cached handler, default branch, or direct function reference can bypass the selected strategy.

`SELECTED_POLICY_OBJECT != EFFECT_PATH_USES_SELECTED_POLICY`

`FEATURE_FLAG_SET != GUARANTEED_BEHAVIOR_CHANGE`

Qualification should trace branch/path coverage to the material state or effect boundary rather than stopping at configuration parsing.

## Verification techniques

Useful implementation-level techniques include:

- stable-ID tracing;
- sentinel values that cannot arise from competing inputs;
- basis-vector contributor probes;
- branch/path instrumentation;
- structured execution receipts;
- taint/provenance labels;
- controlled source/target swaps;
- deliberately incompatible fixtures;
- mutation watches;
- authority-token substitution tests;
- reorder/filter/shuffle perturbations;
- evaluation-cohort-only perturbations with training inputs held fixed;
- recomputation of preprocessing from train-only versus full-cohort visibility;
- negative controls where the wrong path must visibly fail.

No one technique is mandatory. The test must discriminate the intended path from plausible wrong paths.

## Sentinel discipline

A sentinel is useful only if it can distinguish competing bindings.

For example, if source and target can naturally contain the same values, merely observing a shared value downstream proves little. A stronger fixture assigns values, IDs, dimensions, or provenance markers that make substitution detectable.

`NONDISCRIMINATING_SENTINEL != PATH_PROOF`

A basis-vector test can similarly reveal effective contributor coefficients through an aggregation chain without relying on comments or configured weights.

## Failure modes

- caller passes `target`, callee transforms `source` twice and ignores target;
- validation features and labels have compatible shapes but refer to different entities;
- selected strategy variable is assigned but a downstream hard-coded function is invoked;
- graph topology is computed on a complete cohort, records are split afterward, and the training adjacency is mislabeled train-only;
- normalization/manifold/template state is fit before split and silently reused after split;
- correct consent record exists but the effect path checks another cached record;
- action authorization is correct but actuator channel mapping targets the wrong limb/device;
- current memory record is retrieved but a stale predecessor is rendered or used for planning;
- protected-state update classification occurs before a transform that changes which state family is actually written;
- aggregate weights are declared correctly but repeated averaging changes effective influence;
- metric executes successfully against a surrogate target rather than ground truth;
- output plausibility is used as evidence that inputs were correctly bound.

## Adversarial conformance tests

1. Supply source and target sentinels with mutually exclusive values; require the loss/metric/update path to expose the actual target consumed.
2. Give two same-shaped records distinct stable IDs and intentionally swap them; require binding failure despite type/shape compatibility.
3. Select strategy A while inserting a hard-coded path to strategy B; require execution-path verification to detect the bypass.
4. Configure contributor weights and use basis-vector contributor states; require measured output influence to match declared coefficients after all transforms.
5. Provide a valid authority record and a stale authority record; route the stale one to the effect path and require failure.
6. Reorder actuator enumeration while preserving stable actuator IDs; require stale positional binding rejection.
7. Retrieve current and superseded memory records together; intentionally consume the superseded object and require currentness/binding failure.
8. Pass a protected-state descriptor but mutate an ordinary-state fixture, then reverse the mismatch; require state-family binding checks in both directions.
9. Use an evaluation target that is deliberately dimensionally incompatible with the source-derived surrogate; require failure before reporting a qualification score.
10. Produce plausible output from a wrong input branch; require path evidence rather than output plausibility to determine conformance.
11. Compute a training-time topology or normalization artifact from train+evaluation inputs, split afterward, and require the derivation ancestry to expose evaluation-cohort visibility.
12. Hold training inputs fixed while perturbing only evaluation-cohort structure; if the training-time derived artifact changes, require an inductive-frozen claim to fail or be reclassified.

## Interfaces

Strong interfaces are expected with:

- reference identity/index lineage;
- representation fidelity/objective provenance;
- qualification evidence isolation;
- distributed learning/update ancestry;
- authority/consent/effect governance;
- action gateway and body-interface binding;
- current/deep memory;
- chronology;
- protected-update governance;
- resolver/correction;
- temporal forecast lineage;
- effective-topology transition governance.

## Evidence boundary

This architecture contract generalizes implementation-path risks already exposed across HC source studies. BASIRA 4D-FedGNN-Plus supplied a strategy-selection versus direct-call example. BASIRA DynGNN supplied a parallel-view referential mismatch example. BASIRA RepFL supplied a distinct source/target argument versus executed target-transform example and an aggregation-weight versus effective-influence example. BASIRA DuoGNN supplied a complete-cohort topology-construction versus later split example in which the derived conditional training topology is materially consumed by the dual-graph model path.

Those source fixtures motivate path-verification requirements. They do not establish that their source papers are invalid, nor do their implementation choices become HC mechanisms.

See:

- `docs/research/BASIRA_4D_FED_GNN_DISTRIBUTED_LEARNING_2026-09-09.md`
- `docs/research/BASIRA_DYNGNN_VALIDATION_IDENTITY_AND_STATE_SCOPE_2026-09-09.md`
- `docs/research/BASIRA_REPFL_REPLICA_ANCESTRY_AND_TARGET_DATAFLOW_2026-09-09.md`
- `docs/research/BASIRA_DUOGNN_PREPROCESSING_VISIBILITY_AND_DUAL_TOPOLOGY_2026-09-10.md`

## Governing invariant

> **For consequential cognition or effect, the HC must be able to establish that the intended referent actually reached the intended operation under the intended semantic role and information boundary. Declarations, signatures, compatible shapes, split labels, and plausible outputs are not substitutes for executed binding evidence.**
