# Qualification Evidence Isolation

Status: canonical architecture contract.

## Purpose

HC qualification must distinguish evidence used to shape a system from evidence used to independently evaluate it.

A dataset, scenario set, behavioral trace, simulation, embodiment episode, adversarial case, or other evidence source that influences model selection, update acceptance, threshold tuning, policy revision, early stopping, checkpoint choice, architecture choice, or other adaptation is no longer untouched independent evidence for the decision it helped shape.

This applies to ordinary learned components, developmental learning, self-models, plasticity, protected updates, degraded-mode tuning, embodiment calibration, and behavioral qualification.

Qualification must also declare the evaluation regime when test-time information is allowed to shape inference state. Transductive or test-time-adaptive evaluation can be valid, but it supports that regime rather than silently proving inductive/frozen generalization.

Evaluation isolation is ancestry-aware: preprocessing, topology construction, normalization, manifold fitting, calibration, clustering, template generation, indexing, feature selection, or another derived artifact can expose evaluation information before records are later split or named as train/validation/test. A later split does not retroactively remove earlier exposure.

## Core separations

`TRAINING_EVIDENCE != VALIDATION_EVIDENCE`

`VALIDATION_EVIDENCE != FINAL_HOLDOUT_EVIDENCE`

`HOLDOUT_USED_FOR_SELECTION != INDEPENDENT_FINAL_HOLDOUT`

`EVALUATION_SIGNAL_USED_FOR_ADAPTATION != INDEPENDENT_QUALIFICATION_EVIDENCE`

`REPEATED_EXPOSURE_TO_TEST != UNTOUCHED_HOLDOUT`

`PASS_ON_REUSED_CASES != GENERALIZATION_EVIDENCE`

`ADVERSARIAL_CASE_USED_TO_PATCH != NOVEL_ADVERSARIAL_HOLDOUT`

`TRANSDUCTIVE_INFERENCE != INDUCTIVE_INFERENCE`

`TRANSDUCTIVE_TEST_ACCESS != AUTOMATICALLY_INVALID`

`TRANSDUCTIVE_RESULT != INDUCTIVE_GENERALIZATION_EVIDENCE`

`TEST_TIME_ADAPTATION != FROZEN_INFERENCE`

`LATER_SPLIT != EARLIER_INFORMATION_ISOLATION`

`DECLARED_SPLIT_STAGE != ACTUAL_INFORMATION_FLOW_BOUNDARY`

`TRAIN_ONLY_FINAL_TENSOR != TRAIN_ONLY_DERIVATION_ANCESTRY`

`UNLABELED_TEST_STRUCTURE_VISIBLE != TEST_LABEL_LEAKAGE`

## Evidence roles

Qualification evidence should declare a role such as:

- `TRAINING_OR_DEVELOPMENT` — directly changes learned state or parameters;
- `TUNING_OR_SELECTION` — selects among models, checkpoints, thresholds, architectures, policies, or update candidates;
- `DIAGNOSTIC` — inspected to understand a failure and may influence later repair;
- `REGRESSION` — known cases retained to prevent recurrence of previously observed defects;
- `INDEPENDENT_HOLDOUT` — not used to shape the target being qualified;
- `EXTERNAL_REPLICATION` — independently produced evidence when independence is actually supported;
- `UNKNOWN_ROLE` — provenance does not establish whether the evidence influenced the target.

Evidence may move from independent holdout to diagnostic/regression after it is inspected and acted upon. The historical result remains valid for the snapshot tested, but the same case cannot silently remain an untouched holdout for the modified successor.

## Evaluation regimes

Where material, a qualification should identify the operating/evaluation regime being tested. Useful values include:

- `INDUCTIVE_FROZEN` — representation/model state is fit before evaluation and the current evaluation cohort does not alter that fitted state or any consequential preprocessing artifact used by that state;
- `TRANSDUCTIVE` — unlabeled evaluation inputs or the evaluation cohort may participate in representation/manifold/topology construction or inference preparation;
- `TEST_TIME_ADAPTIVE` — the current test input may alter temporary or durable model state before its output is scored;
- `ONLINE_ADAPTIVE` — prior evaluation/production interactions may update state used for later cases;
- `MIXED` — different components operate under different declared regimes;
- `UNKNOWN` — available provenance does not establish the regime.

The regime record should state which test-time information is visible, such as:

- current input only;
- unlabeled cohort inputs;
- cohort graph structure or topology;
- labels;
- target outputs/ground truth;
- prior evaluation outcomes;
- aggregate evaluation metrics;
- human/evaluator feedback;
- production feedback after effect.

Access to unlabeled test inputs or cohort topology can be legitimate in a transductive deployment. It must not be described as evidence for a deployment in which such access is absent.

## Preprocessing visibility ancestry

The information boundary is established by the earliest consequential operation that can influence the target—not by the latest point where the resulting objects happen to be called `train`, `validation`, or `test`.

A derived artifact can carry evaluation-cohort information into later training or inference even when labels remain hidden. Material examples include:

- fitted normalization or calibration state;
- graph topology, connectivity scores, communities, or condensed adjacency;
- manifold/embedding construction;
- population/common templates;
- vocabulary or tokenizer statistics;
- feature-selection masks;
- nearest-neighbor or retrieval indexes;
- generated/imputed representations;
- route-selection or topology policies.

For consequential qualification, provenance should record the visibility set and derivation ancestry for such artifacts.

A useful representation is:

```text
PREPROCESSING_EXPOSURE {
  artifact_id
  derivation_operation
  source_partition_ids[]
  information_classes_visible[]
  labels_visible
  created_before_or_after_split
  downstream_targets_influenced[]
  evaluation_regime
  provenance
}
```

The implementation schema may differ. The required semantic question is whether evaluation-partition information influenced a state or artifact later used by training, selection, inference, or scoring.

If a train-only final tensor depends on a topology/template/statistic created from train+evaluation inputs, the tensor's derivation ancestry is not train-only.

## Evidence object

A qualification-evidence record should support:

```text
QUALIFICATION_EVIDENCE {
  evidence_id
  role
  source
  generation_method
  evaluation_regime
  test_time_information_visible[]
  preprocessing_artifact_refs[]
  derivation_visibility_ancestry[]
  target_snapshot_first_exposed
  exposure_history[]
  adaptations_influenced[]
  independence_group
  contamination_status
  applicability_scope
  provenance
}
```

`contamination_status` refers to evaluation independence, not data corruption. Useful states include `UNTOUCHED`, `EXPOSED_NOT_USED_FOR_CHANGE`, `USED_FOR_SELECTION`, `USED_FOR_REPAIR`, `REGRESSION_CASE`, and `UNKNOWN`.

## Snapshot rule

A qualification result remains snapshot-bound.

If an HC or subsystem is modified after reviewing a failed holdout case, that case becomes a regression test for the successor. Re-running it is valuable, but its success cannot alone establish independent generalization of the repaired successor.

A new independent holdout or other genuinely independent evidence should be used for claims requiring fresh generalization evidence.

## Adaptive systems

For continuously learning HC systems, strict permanent separation of all future experience is impossible and undesirable. The architecture therefore requires scoped evaluation windows and explicit exposure lineage rather than pretending adaptation did not occur.

A behavioral qualification may define a frozen or bounded evaluation interval in which:

- the target version/state is fixed or adaptation is explicitly constrained;
- evaluation cases are not fed back into durable learning until the evaluation decision is recorded, when the test requires independent holdout semantics;
- post-evaluation incorporation, if allowed, is recorded as a later learning event;
- online-learning qualification separately tests the adaptation process itself rather than treating adaptive exposure as untouched holdout evidence.

For transductive/test-time-adaptive qualification, the allowed adaptation scope and information boundary should be explicit, and the resulting PASS is scoped to that regime.

## Protected updates

A protected update must not be accepted solely because it performs well on evidence repeatedly used to design or tune that update.

Where consequence is high, acceptance should distinguish:

1. development/tuning evidence;
2. regression evidence;
3. independent qualification evidence;
4. post-deployment monitoring evidence.

`CANARY_SUCCESS != INDEPENDENT_QUALIFICATION` when the canary population or scenario was repeatedly used to tune the release decision.

## Adversarial review

A hostile reviewer should be able to ask:

- Was this supposedly independent case previously shown to the builder or optimizer?
- Did its score influence checkpoint or threshold selection?
- Did a failure become a patch target before the claimed final qualification?
- Are multiple "independent" tests descendants of the same generated source or template?
- Was the same simulation seed family used for both optimization and qualification?
- Did the evaluator adapt prompts, routing, heuristics, or model state after seeing intermediate holdout results?
- Was the evaluation transductive/test-time-adaptive while the reported claim sounds inductive/frozen?
- Did aggregate holdout statistics or unlabeled cohort structure influence the target even if individual labels were hidden?
- Was any topology, normalization, manifold, template, index, or calibration artifact fit before the declared split?
- Can changing only evaluation-cohort structure alter a training-time artifact while training records remain fixed?
- Does a source comment or variable name claim `inductive` while the executed preprocessing path crosses the evaluation boundary earlier?

## Failure modes

- early stopping on the test set and later reporting that same set as untouched final evidence;
- repeatedly tuning an HC update against a hostile-review fixture and calling the repaired fixture a novel adversarial test;
- selecting the best checkpoint across many holdout evaluations without recording holdout reuse;
- generated variants of one source being counted as independent test cases;
- body calibration scenarios reused as independent body-transfer qualification without declaring prior exposure;
- post-failure patching followed by a PASS based only on the original failed case;
- using production outcomes to adapt a model while still calling those same outcomes independent external validation;
- fitting a manifold/template to the unlabeled evaluation cohort and reporting the result as inductive generalization without declaring transductive access;
- computing topology/communities/normalization from the full cohort, splitting afterward, and calling the resulting training artifact train-only;
- test-time adaptation changing durable state while the record claims a frozen target snapshot;
- evaluator/human feedback changing prompts or routes during the holdout without recording that exposure.

## Qualification relationship

This contract does not require every test to be independent. Regression, tuning, diagnostic, transductive, test-time-adaptive, online-adaptive, and training evidence are all useful. It requires that their role and regime be represented honestly and that claims of independence/generalization not exceed the provenance.

## Governing invariant

> **Evidence that shaped the target cannot silently serve as untouched independent evidence for the same shaped target. Exposure, preprocessing ancestry, adaptation lineage, and evaluation regime are part of qualification provenance; a later split cannot erase earlier information visibility.**

## Provenance

Generalized from HC qualification/update-governance requirements and reinforced by code-level study of BASIRA DGN, HADA, and DuoGNN. The inspected DGN cross-validation implementation uses fold test error for early stopping/checkpoint restoration. The inspected HADA implementation fits part of its source-space manifold using combined train-plus-current-test source inputs, providing a concrete transductive evaluation pattern. The inspected DuoGNN topology-aware path constructs topology and a conditional graph from a complete pre-split graph before deriving the train/validation/test conditional adjacencies, providing a concrete preprocessing-visibility example where a later split does not restore an earlier information boundary. See the corresponding records under `docs/research/`.
