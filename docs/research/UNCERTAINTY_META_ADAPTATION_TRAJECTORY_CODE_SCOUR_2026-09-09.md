# Predictive Uncertainty, Meta-Adaptation, and Teacher–Student Trajectory Code Scour — 2026-09-09

Status: research/provenance supplement only. Not canonical HC architecture. No source code is imported.

## Purpose

This note deep-scours three BASIRA sources whose useful transfer to the Hyperconnectome Brain is not their human-connectome task framing, but their handling of:

1. predictive uncertainty under deliberately constructed domain shift;
2. fast adaptation from a meta-trained parameter state;
3. teacher–student / few-shot trajectory forecasting across time and resolution.

The HC qualification question is:

> **What capability or uncertainty was acquired from current evidence, what was supplied by a prior/teacher/evaluator, and what executable path actually produced the claimed training signal?**

## Exact source cuts

- `basiralab/predUncertaintywithDomainShift main@bf30c331736820f714603999f47561afcb2b4376`
- `basiralab/Meta-RegGNN main@e7e54c5bb968cac8b85849f7000b179aee60ea69`
- `basiralab/GmTE-Net main@629852bbccfecbce1db9f7f3e20835fde8627dd5`

## Evidence vocabulary

- **SOURCE OBSERVATION** — directly observed in the bound README/code.
- **HC TRANSFER INFERENCE** — Four's proposed qualification/design implication.
- **DO NOT TRANSFER** — source-specific assumptions that must not become generic HC architecture.

---

## 1. predUncertaintywithDomainShift: ensemble disagreement is a specific uncertainty estimator

### SOURCE OBSERVATION

The repository describes a deep ensemble of regression GNNs for predictive uncertainty under target-domain shift.

In the inspected `EnsembleModel.train_test_ensemble()` implementation:

- each ensemble member is trained and evaluated independently;
- the ensemble prediction is the mean of member predictions;
- `ensemble_test_uncs` is computed as `np.std(self.models_test_preds, axis=0)`.

Therefore the code's per-sample uncertainty quantity is directly the standard deviation across ensemble predictions.

The `domain_shift(...)` function constructs shift cases from **ground-truth target `y` values**. It collects every sample's `item.y`, clusters those target values using a chosen clustering algorithm, and then creates three train/test cases by holding out one target-value cluster at a time.

Supported clustering options in the inspected code include KMeans, MeanShift, AgglomerativeClustering, AffinityPropagation, BIRCH, and SpectralClustering.

### HC TRANSFER INFERENCE

The uncertainty object must name the estimator and what uncertainty source it can actually expose.

`ENSEMBLE_DISAGREEMENT != TOTAL_EPISTEMIC_UNCERTAINTY`

`LOW_ENSEMBLE_VARIANCE != KNOWN_CORRECT`

`HIGH_ENSEMBLE_VARIANCE != PROVEN_DOMAIN_SHIFT`

`EVALUATOR_CONSTRUCTED_SHIFT != ONLINE_SHIFT_DETECTION`

A useful research object would preserve:

```text
uncertainty_ref
prediction_ref
uncertainty_estimator
ensemble_member_refs[]
ensemble_member_training_provenance[]
spread_statistic
calibration_reference
known_shift_condition
shift_construction_method
shift_visibility_to_model
in_distribution_reference
outcome_or_error_ref
provenance
```

For HC, an uncertainty estimate should state whether it reflects:

- ensemble disagreement;
- posterior approximation;
- measurement uncertainty;
- model calibration error;
- distribution-shift detector output;
- unresolved competing hypotheses;
- data sparsity;
- unknown/other.

These are not interchangeable.

Recommended controls:

- `UNCERTAINTY_ESTIMATOR_IDENTITY`
- `ENSEMBLE_DIVERSITY_ABLATION`
- `DISAGREEMENT_VS_ERROR_CALIBRATION`
- `KNOWN_WRONG_LOW_DISAGREEMENT`
- `KNOWN_SHIFT_LOW_DISAGREEMENT`
- `EVALUATOR_DEFINED_VS_ONLINE_DETECTED_SHIFT`
- `SHIFT_CONSTRUCTION_SENSITIVITY`
- `UNCERTAINTY_NE_AUTHORITY`

The target-score clustering is a valid controlled evaluation device for the paper's question, but it must remain tagged as evaluator-constructed shift. A deployed HC cannot assume access to an unknown ground-truth target simply to decide whether it is out of distribution.

### DO NOT TRANSFER

Do not transfer IQ targets, ABIDE cohort ontology, target-score clustering as a production shift detector, or standard deviation as the HC's universal uncertainty representation.

---

## 2. Meta-RegGNN: nominal K-fold test data participates in meta-training

### SOURCE OBSERVATION

The README describes Meta-RegGNN as explicitly training a regression GNN parameter state so that a small number of gradient steps on a small data amount generalizes to unseen connectomes.

The inspected `evaluate_MetaRegGNN(...)` implementation creates a K-fold split into `train_idx` and `test_idx`, then constructs:

- `selected_train_data` from `train_idx`;
- `test_data` from `test_idx`;
- `train_loader` and `test_loader` from those sets.

Inside **every training epoch**, the code creates `tgt_data = iter(test_loader)`.

For each training batch it:

1. computes an inner loss on the training/source batch;
2. computes parameter gradients and constructs `updated_params`;
3. loads `updated_params` into `candidate_model`;
4. takes a batch from `test_loader`;
5. computes `outer_loss` against `batch_tgt.y` from that nominal test fold;
6. periodically calls `outer_loss.backward()` and `optimizer.step()`.

Therefore the nominal K-fold test split is an optimization input to the meta-learning procedure on the literal code path. It is not a sealed final holdout.

The model's `forward(..., params=None)` signature accepts a `params` argument, but the inspected implementation does not use that argument when invoking its layers. The evaluator passes `params` in the target call after already applying `candidate_model.load_state_dict(updated_params)`. Thus the apparent `params` argument should not itself be treated as evidence of a separate stateless MAML parameter path.

The evaluator also loops over `k_list`, but the visible shot/update condition is hard-coded as `if i % 5 == 0`; the inspected function does not show `k` controlling that condition. No stronger claim about intended experiment semantics is made here.

### HC TRANSFER INFERENCE

Fast adaptation must be decomposed into at least:

`PRIOR_CAPABILITY + CURRENT_EXPOSURE + UPDATE_RULE -> ADAPTED_CAPABILITY`

not simply:

`FEW_EXAMPLES -> LEARNED_FROM_SCRATCH`

And evaluation evidence must be classified by actual use:

`CALLED_TEST != HELD_OUT`

`OUTER_LOOP_TARGET_DATA != INDEPENDENT_TEST`

`META_TRAINED_INITIALIZATION != UNTRAINED_INITIALIZATION`

`FAST_ADAPTATION != LOW_PRIOR_INFORMATION`

A future HC developmental/learning certificate should bind:

```text
initial_parameter_or_policy_state
pretraining_or_meta_training_sources[]
prior_capabilities[]
current_exposure_refs[]
inner_update_rule
outer_update_rule
outer_objective_data_scope
number_of_effective_updates
frozen_components[]
adapted_components[]
sealed_holdout_refs[]
from_scratch_baseline_ref
ablation_refs[]
provenance
```

Recommended controls:

- `META_PRIOR_ABLATION`
- `RANDOM_INIT_COMPARATOR`
- `TARGET_EXPOSURE_DISCLOSURE`
- `OUTER_LOOP_DATA_CLASSIFICATION`
- `SEALED_POST_META_HOLDOUT`
- `UPDATE_COUNT_SENSITIVITY`
- `ADAPTATION_NE_ACQUISITION_FROM_SCRATCH`
- `SUPPLIED_PRIOR_CAPABILITY_ACCOUNTING`
- `FORWARD_PARAMETER_PATH_AUDIT`

For HC developmental claims, prior structure is not a flaw. The flaw is crediting prior-supplied capability to current learning without declaring it.

### DO NOT TRANSFER

Do not transfer intelligence-score regression, human ROI topology, the literal test-as-outer-loop protocol, or the specific meta-gradient implementation as generic HC learning architecture.

---

## 3. GmTE-Net: teacher-derived targets and gradient-path integrity

### SOURCE OBSERVATION

GmTE-Net is described as a few-shot teacher–student framework for predicting multiple graph evolution trajectories from a baseline graph. The README states that the teacher learns from a small set of real complete subjects while the student learns from a larger simulated/augmented set; a local topology-aware distillation loss is intended to make student predicted graph topology consistent with teacher predictions.

The inspected training implementation makes the teacher provenance explicit.

After teacher training, teacher outputs over the student baseline data are stored in `predicted_Trajectory_LR` and `predicted_Trajectory_SR`. A code comment describes these lists as “the ground truth to the student.” Student local-topology losses then compare student predictions against those teacher-predicted trajectories rather than against direct observations in that loss term.

The student loss also includes a term comparing the student encoder embedding against the teacher embedding.

Therefore student competence is explicitly teacher-distilled and should retain that ancestry.

### Executable gradient-path finding

The `local_topology` loss path calls `topological_measures(...)` and then computes `sklearn.metrics.mean_absolute_error(...)` between topology arrays. The inspected topology helper reconstructs NumPy arrays, builds NetworkX graphs, and returns NumPy centrality arrays. The loss then wraps the sklearn scalar in a fresh `torch.tensor(..., requires_grad=True)`.

That fresh tensor is not computationally connected to the student prediction tensor that produced the topology arrays. On the literal code path, the numeric local-topology loss value therefore does not provide a gradient path back through the NetworkX/NumPy computation to the student output.

This is a code-path observation, not a claim about the paper's intended mathematics.

### Public-cut packaging finding

`prediction.py` imports `from model1b import *`. The bound repository root exposes `model.py`, and repository search for `model1b` returned only the import statement. At this public cut, `model1b.py` is therefore not available in the inspected repository surface.

This is classified as `PACKAGING/RUNTIME_MISMATCH_AT_BOUND_CUT`, not proof that such a file never existed in another environment.

### HC TRANSFER INFERENCE

Teacher/student capability needs generative provenance:

`TEACHER_OUTPUT != DIRECT_OBSERVATION`

`DISTILLED_CAPABILITY != INDEPENDENTLY_DISCOVERED_CAPABILITY`

`FEW_REAL_EXAMPLES + TEACHER_PRIOR != FEW_SHOT_FROM_SCRATCH`

And an advertised training objective must be verified at the executable path:

`LOSS_VALUE_PRESENT != LOSS_GRADIENT_REACHES_TARGET_PARAMETERS`

`OBJECTIVE_NAMED_IN_PROSE != OBJECTIVE_EFFECTIVELY_OPTIMIZES_MODEL`

A future HC training/qualification record should preserve:

```text
teacher_or_source_model_ref
teacher_training_sources[]
student_training_sources[]
simulated_or_augmented_status
teacher_generated_target_refs[]
distillation_objectives[]
loss_component_refs[]
loss_to_parameter_paths[]
freezing_state
independent_ground_truth_refs[]
sealed_holdout_refs[]
provenance
```

Recommended controls:

- `TEACHER_ABLATION`
- `TEACHER_OUTPUT_NE_GROUND_TRUTH`
- `DISTILLATION_PROVENANCE`
- `REAL_VS_SIMULATED_TRAINING_CONTRIBUTION`
- `LOSS_TO_PARAMETER_PATH_AUDIT`
- `ZERO_GRADIENT_OBJECTIVE_DETECTION`
- `TEACHER_STUDENT_LEAKAGE`
- `INDEPENDENT_POST_DISTILLATION_HOLDOUT`
- `PACKAGING_REPRODUCIBILITY`
- `MULTI_TRAJECTORY_RESOLUTION_SEPARATION`

A student can legitimately inherit useful structure from a teacher. HC must simply avoid reporting that as independently grounded acquisition.

### DO NOT TRANSFER

Do not transfer neonatal-development framing, human morphological/functional graph resolutions, specific centrality functions, or teacher-generated predictions as generic HC truth.

---

## 4. Cross-source synthesis: learning credit requires ancestry

These sources converge on a qualification principle that is broader than graph learning:

> **A capability claim is incomplete without the ancestry of the capability-producing information.**

At minimum distinguish:

- fixed architecture prior;
- pretrained/meta-trained prior;
- teacher/distillation input;
- simulator/augmentation input;
- current direct observations;
- evaluator-only labels or constructed shift conditions;
- optimization/model-selection evidence;
- sealed independent holdout evidence.

Proposed research object:

```text
LEARNING_PROVENANCE_PROFILE {
  capability_ref
  architecture_prior_ref
  initialization_or_pretraining_ref
  meta_training_refs[]
  teacher_or_distillation_refs[]
  simulated_or_augmented_refs[]
  direct_exposure_refs[]
  evaluator_only_refs[]
  optimization_refs[]
  model_selection_refs[]
  sealed_holdout_refs[]
  update_rule_refs[]
  effective_gradient_paths[]
  provenance
}
```

This remains a research proposal, not canonical schema.

## 5. Candidate hostile-control bundle

- `UNCERTAINTY_ESTIMATOR_IDENTITY`
- `KNOWN_WRONG_LOW_DISAGREEMENT`
- `DISAGREEMENT_VS_ERROR_CALIBRATION`
- `EVALUATOR_DEFINED_VS_ONLINE_SHIFT`
- `SHIFT_CONSTRUCTION_SENSITIVITY`
- `META_PRIOR_ABLATION`
- `RANDOM_INIT_COMPARATOR`
- `TARGET_EXPOSURE_DISCLOSURE`
- `OUTER_LOOP_DATA_CLASSIFICATION`
- `SEALED_POST_META_HOLDOUT`
- `SUPPLIED_PRIOR_CAPABILITY_ACCOUNTING`
- `TEACHER_ABLATION`
- `DISTILLATION_PROVENANCE`
- `TEACHER_OUTPUT_NE_GROUND_TRUTH`
- `LOSS_TO_PARAMETER_PATH_AUDIT`
- `ZERO_GRADIENT_OBJECTIVE_DETECTION`
- `PACKAGING_REPRODUCIBILITY`

## Current disposition

**KEEP as research/provenance and qualification input.**

No human brain-region topology, IQ target, neonatal developmental schedule, or source training loop is adopted as HC cognition.

The strongest transferable rule is:

`ADAPTATION / UNCERTAINTY / DISTILLATION CLAIM -> DECLARED INFORMATION ANCESTRY + EXECUTABLE TRAINING PATH + INDEPENDENT EVIDENCE SCOPE`
