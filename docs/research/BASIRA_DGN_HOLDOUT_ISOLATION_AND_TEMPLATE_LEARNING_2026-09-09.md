# BASIRA DGN Holdout Isolation and Template Learning — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/DGN@master/README.md`
- `basiralab/DGN@master/model.py`

## DOCUMENTED source claims

The DGN repository describes a Deep Graph Normalizer that integrates a population of multi-view brain networks into a single connectional brain template (CBT). The README frames the CBT as a normalized or average-like graph intended to be representative of a population and describes the method as optimizing representativeness/centeredness and discriminability.

## OBSERVED implementation behavior

`DGN.forward` applies three `NNConv` layers to a subject graph, then constructs a subject-biased CBT from pairwise absolute differences among learned node embeddings.

`generate_cbt_median` evaluates the trained model over the training subjects and returns the element-wise median of the resulting subject-biased CBTs.

Inside `train_model`, each cross-validation fold obtains `train_data` and `test_data`. Every ten epochs the code computes a CBT from the training data, evaluates `mean_frobenious_distance(cbt, test_casted)`, appends that value to `test_errors`, and—when early stopping is enabled—uses the trajectory of those test errors to stop training. It also attempts to restore the temporary checkpoint associated with `min(test_errors)` before saving the final fold model.

Therefore the fold named `test_data` in the inspected implementation is not purely untouched final-evaluation evidence when early stopping/model restoration uses its score.

## INFERRED HC lessons

1. A population template is a learned summary of a source population, not an instance state or independent observation.
2. Median/centeredness operations can improve representativeness while suppressing minority or exceptional structure; source dissent therefore needs recoverable provenance when consequential.
3. A held-out set used to select epochs, checkpoints, architecture, hyperparameters, thresholds, or adaptation policy is no longer independent final qualification evidence for that same selection process.
4. HC self-adaptation and protected-update qualification therefore need explicit evidence-set roles rather than a generic `test` label.

## Proposed separations

`POPULATION_TEMPLATE != INSTANCE_STATE`

`CENTERED_TEMPLATE != COMPLETE_SOURCE_SET`

`HOLDOUT_USED_FOR_SELECTION != INDEPENDENT_FINAL_HOLDOUT`

`EVALUATION_SIGNAL_USED_FOR_ADAPTATION != INDEPENDENT_QUALIFICATION_EVIDENCE`

`BEST_ON_REUSED_HOLDOUT != UNBIASED_GENERALIZATION_ESTIMATE`

## Scope and caution

The implementation observation above is a static code reading of the repository version inspected. It does not by itself establish the behavior of every experiment reported in the associated paper, invalidate the scientific work, or quantify any resulting bias. Those stronger claims would require experiment-level reconstruction and execution.

## HC transfer candidate

Promote a generic qualification-evidence isolation rule: evidence that influences model selection, update acceptance, threshold tuning, early stopping, or other adaptive decisions must record that use and must not subsequently be presented as untouched independent qualification evidence for the decision it helped select.
