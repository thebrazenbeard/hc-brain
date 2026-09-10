# BASIRA Federated Reproducibility Code Scout — 2026-09-09

Status: research/provenance only. No source code is copied and federated learning is not promoted as HC distributed-organ architecture.

## Exact source binding

`basiralab/reproducibleFedGNN main@c547b38358c000be2505fd438fa8782973c6ba38`

Read depth for this cut includes README, `fed_localmodel.py`, `learning_modes.py`, `fed_reproducibility.py`, `Analysis.py`, `cross_val.py`, `demo.py`, `options.py`, and repository tree/license metadata.

## 1. Source framing

The repository studies federated GNN learning over decentralized medical/connectomic datasets and emphasizes both predictive accuracy and reproducibility of discriminative features under distributed training.

It contains an explicit root `LICENSE` artifact at the inspected cut. No source code is copied into HC regardless.

The repository's federation model is a useful **distributed-learning comparison class**, not a model of one physically distributed HC organ.

`FEDERATED_CLIENTS != HC_CONSTITUENTS`

Separate hospitals are distinct data/model participants. HC constituents are parts of one cognitive organ under a different ownership, continuity, routing, authority, latency, and failure model.

## 2. OBSERVED aggregation — equal arithmetic parameter averaging

`fed_localmodel.py::average_weights()` deep-copies the first client state dictionary, adds each corresponding tensor from the other clients, and divides every parameter tensor by `len(weights)`.

`learning_modes.py::federatedLearning()` gives every hospital a deep copy of the same current global model for a communication round, collects each locally updated state dictionary, computes that equal arithmetic average, and loads the result into the global model.

On the inspected path, aggregation is therefore **equal-client parameter averaging**. It is not sample-count weighting, uncertainty weighting, evidence fusion, causal arbitration, or semantic consensus.

HC boundaries:

`PARAMETER_AVERAGE != EVIDENCE_FUSION`

`EQUAL_CLIENT_WEIGHT != EQUAL_EPISTEMIC_AUTHORITY`

`GLOBAL_MODEL != CONSENSUS_TRUTH`

`COMMON_PARAMETER_SHAPE != COMMON_SEMANTICS`

`FEDERATED_UPDATE != AUTHORIZED_PROTECTED_UPDATE`

A future HC distributed learner may borrow aggregation ideas, but every shared update must still preserve source/client/constituent provenance, objective, data regime, update semantics, qualification state, and protected-update boundaries.

### Minority/rare-state hostile control

Construct one participant whose local update contains a rare but real pattern that is attenuated by averaging. A high-performing aggregate must not justify the claim that the minority evidence was false or irrelevant. Where the HC is aggregating evidence rather than model parameters, evidence should remain recoverable rather than disappear into weight-space consensus.

## 3. Federation round semantics

Each communication round starts local learning from a deep copy of the current global model. The global model is then replaced by the average of local model parameters.

That gives a useful ancestry lesson:

`ROUND_N_GLOBAL -> CLIENT_LOCAL_DESCENDANTS -> ROUND_N_PLUS_1_AGGREGATE`

But the source code does not itself encode a durable causal/provenance ledger for every tensor contribution.

For HC research, any analogous distributed update should bind at least:

```text
AGGREGATED_UPDATE_CANDIDATE {
  parent_global_revision
  contributor_refs[]
  contributor_start_revision[]
  local_data_or_experience_scope[]
  local_update_refs[]
  aggregation_rule
  aggregation_weights[]
  excluded_or_missing_contributors[]
  uncertainty_or_disagreement
  candidate_result_ref
  qualification_refs[]
  provenance
}
```

This is a research sketch, not canonical schema.

## 4. OBSERVED reproducibility metric — top-feature-set overlap

`fed_reproducibility.py` obtains learned weight vectors, takes their absolute value, selects top biomarkers, and computes pairwise reproducibility matrices.

`Analysis.py::Top_biomarkers()` sorts feature weights and selects top-ranked indices. `Analysis.py::sim()` measures overlap between two equal-length top-feature sets as the fraction of one set found in the other. Federated reproducibility reporting uses these overlap scores across model/hospital combinations.

This is a useful, bounded stability measure. It is not a universal definition of reproducibility.

`TOP_WEIGHT_OVERLAP != CAUSAL_IMPORTANCE`

`TOP_WEIGHT_OVERLAP != REPRESENTATIONAL_EQUIVALENCE`

`FEATURE_REPRODUCIBILITY != PREDICTION_REPRODUCIBILITY`

`FEATURE_REPRODUCIBILITY != SEMANTIC_STABILITY`

`ABS_WEIGHT_MAGNITUDE != SIGNED_EFFECT_MEANING`

A feature may be consistently selected for reasons that are confounded, dataset-specific, architecture-specific, redundant, or noncausal. Conversely, two functionally equivalent models may distribute representation across different features.

### HC transfer

Use feature/explanation overlap as **one reproducibility dimension**, alongside behavior/output stability, calibration, causal perturbation, counterfactual response, protected-state preservation, and distributional robustness where the claim requires them.

## 5. OBSERVED configurability mismatches

The CLI exposes `hospital_num`, but several implementation paths retain literal three-hospital assumptions:

- `learning_modes.py` initializes `hospital_losses = [[], [], []]` in both federated and baseline paths;
- `Analysis.py::AvgRep_matrix()` accepts `hospital_num` and loops over it, but divides the aggregate by literal `3` rather than the supplied argument.

Therefore:

`CONFIGURABLE_INTERFACE != PARAMETERIZED_IMPLEMENTATION`

This is a code-level portability defect in the inspected implementation, not a criticism of federated learning as a method.

### HC hostile test

Every parameterized distributed-HC or evaluator component should be exercised at multiple constituent/client counts, including counts unlike its development fixture. A supposedly generic component that hides fixed cardinality assumptions must fail qualification until the assumption is exposed or removed.

## 6. OBSERVED label/split assumptions

`cross_val.py::stratify_splits()` explicitly creates `graphs_0` and `graphs_1` and only handles labels equal to `0` or `1`. It partitions each class list into `cv_number` folds, then combines corresponding class folds.

In `demo.py`, this helper is also used to form `hospital_data`; those hospital partitions are shuffled **after** assignment, not before the class lists are partitioned. Thus participant assignment can inherit source ordering within each class unless upstream loading has already randomized that order.

This matters because a generic CLI surface can mask a more specific binary-class/ordering assumption.

`BINARY_LABEL_IMPLEMENTATION != GENERIC_CLASSIFICATION_PIPELINE`

`SHUFFLED_WITHIN_CLIENT != RANDOMIZED_CLIENT_ASSIGNMENT`

`STRATIFIED_PARTITION != NATURAL_NON_IID_CLIENT_DISTRIBUTION`

For HC federation/distributed-learning experiments, client/constituent assignment, ordering, label distribution, domain distribution, and data heterogeneity should be explicit experimental variables.

## 7. Model selection versus assessment is explicitly separated

`cross_val.py` contains distinct `model_selection_split()` and `model_assessment_split()` functions.

For model selection, one local fold is used as validation while remaining folds train. For model assessment, the prior validation split is folded back into training and the held-out fold becomes test data. Threshold statistics are computed from the training set.

This separation is conceptually good and reinforces the qualification rule already found in the DGN scout:

`TUNING_EVIDENCE != FINAL_ASSESSMENT_EVIDENCE`

However, qualification must still verify how downstream train routines use the supplied validation/test loader before calling a result blind or final.

## 8. Accuracy and reproducibility are separate axes

The source project's motivation itself distinguishes predictive accuracy from reproducibility of selected features.

That is directly transferable to HC qualification:

`HIGH_TASK_ACCURACY != STABLE_INTERNAL_EVIDENCE_USE`

`STABLE_FEATURE_USE != HIGH_TASK_ACCURACY`

`HIGH_ACCURACY_AND_REPRODUCIBILITY != CAUSAL_CORRECTNESS`

An HC architecture/update may need multiple qualification dimensions instead of one aggregate score.

Candidate evaluation vector:

- task performance;
- calibration/uncertainty;
- feature/explanation stability;
- estimator/preprocessing sensitivity;
- causal perturbation robustness;
- domain/client shift robustness;
- protected-state preservation;
- authority/consent/effect integrity;
- resource/failure behavior.

## 9. Privacy claim boundary

Federated training avoids centralizing raw local datasets in the basic architecture, but parameter/model sharing is not identical to proven privacy.

`RAW_DATA_NOT_CENTRALIZED != PRIVACY_PROVEN`

`PARAMETER_SHARING != ZERO_INFORMATION_LEAKAGE`

Any HC use of distributed learning should independently model what leaves each trust/domain boundary, whether updates can leak sensitive state, and whether aggregation is compatible with the cognitive-organ ownership model.

## 10. Recommended HC promotion targets

High-value findings for later architecture/qualification review:

1. aggregation records need explicit parent revision, contributors, weights/rule, missing participants, and disagreement/provenance;
2. parameter aggregation and evidence integration must remain different operations;
3. feature reproducibility is one metric, not semantic/causal truth;
4. configurable distributed components require cardinality-adversarial tests;
5. client assignment/non-IID structure must be explicit rather than accidental source ordering;
6. tuning/selection data remain distinct from sealed final assessment;
7. distributed learning is not the same thing as distributed HC-organ membership.

No canonical promotion is made by this research note alone.

## 11. Candidate hostile controls

- one rare client carries a unique high-consequence signal that equal averaging suppresses;
- one client has ten times more valid evidence but receives equal model weight; the evaluator must distinguish aggregation policy from epistemic weighting;
- change hospital/client count from 3 to 2, 4, and 7 to expose hidden cardinality assumptions;
- reorder class members before participant assignment and measure whether learned/reported reproducibility changes;
- create non-IID client domains and compare aggregate accuracy versus per-domain performance and feature stability;
- preserve contributor lineage through multiple aggregation rounds and verify rollback does not erase which local revisions contributed;
- identical top-feature overlap with opposite signed/model effects must not be reported as semantic equivalence;
- high feature overlap under one architecture but low overlap under another must remain architecture-dependent evidence;
- federated update attempts to cross into protected HC architecture without protected-update qualification; it must remain a candidate only;
- demonstrate that raw data staying local does not by itself authorize a `PRIVACY_PRESERVED` claim without a defined threat/privacy analysis.

## Disposition

**KEEP as research/provenance. HIGH VALUE for distributed-learning and qualification boundaries.**

The strongest immediate HC transfer is not FedAvg itself. It is the requirement that any multi-source/model aggregation expose what was combined, under which rule, with what weighting and disagreement, and what claim the aggregate is allowed to support.