# BASIRA HADA Transductive Evaluation and Positional Trace — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/HADA@master/README.md`
- `basiralab/HADA@master/HADA.py`
- `basiralab/HADA@master/optimizer.py`

## DOCUMENTED source framing

HADA is presented as a hierarchical adversarial domain-alignment framework that predicts a target brain graph from a source graph and then uses source plus predicted target features for classification. The repository describes leave-one-out cross-validation on paired source/target graph data.

## OBSERVED implementation behavior

Inside each leave-one-out fold, `HADA.py` forms:

`test__train__SV = vstack(sourceGraph[train_index], sourceGraph[test_index])`

and then fits SIMLR on this combined training-plus-current-test source set before encoding the combined set and fitting a second SIMLR manifold.

Therefore the inspected inference procedure is transductive with respect to the unlabeled test source graph: the test source contributes to the representation/manifold used to predict that same test case.

This is not automatically data leakage. It is a different evaluation/deployment regime from an inductive model whose representation is fitted without access to the future test input distribution.

### Positional trace finding

For a leave-one-out fold over 150 samples, `sourceGraph[train_index]` contains 149 rows and the appended test source occupies local stacked position 149.

The code computes:

`tSubjectIndex = (sourceGraph[train_index].shape[0]-2) + testingSubject`

with `testingSubject` iterating over `range(1,2)`, which yields local index 148 rather than the appended test position 149.

That `tSubjectIndex` is subsequently used to choose the row of the learned similarity matrix and to index `rearrangedTargetView` for the target used in MAE calculation.

OBSERVED: the local index arithmetic visible in the inspected source does not point to the appended test row under ordinary zero-based NumPy indexing.

INFERRED/HYPOTHESIS: the procedure may reason from/evaluate a training-row position while attributing the result to `tSubjectOriginalIndex = test_index`. Exact runtime impact should be confirmed by instrumenting stable subject IDs rather than inferred solely from intended comments.

## HC lessons

`TRANSDUCTIVE_INFERENCE != INDUCTIVE_INFERENCE`

`TRANSDUCTIVE_TEST_ACCESS != AUTOMATICALLY_INVALID`

`TRANSDUCTIVE_RESULT != INDUCTIVE_GENERALIZATION_EVIDENCE`

`EVALUATION_REGIME != IMPLEMENTATION_LABEL`

`INTENDED_TEST_ROLE != VERIFIED_LOCAL_POSITION`

An HC qualification must state what information and adaptation are permitted at evaluation time. A system allowed to construct a representation from the current evaluation cohort or test-time input can be validly tested, but the resulting evidence supports that transductive/test-time-adaptive operating regime rather than a stronger claim that no evaluation input shaped inference state.

The positional finding independently reinforces the HC reference/index-lineage contract: stable referent tracing is needed to verify that the case being predicted, scored, or authorized is actually the intended case after concatenation/filtering/reindexing.

## Transfer candidates

1. Add an explicit evaluation-regime field such as `INDUCTIVE`, `TRANSDUCTIVE`, `TEST_TIME_ADAPTIVE`, `ONLINE_ADAPTIVE`, or `UNKNOWN` to qualification evidence/protocol records where material.
2. Qualification should report what test-time information is visible: current case only, unlabeled cohort, labels, targets, outcomes, prior evaluation cases, or post-decision feedback.
3. A transductive or test-time-adaptive PASS must not silently become evidence for an inductive/frozen deployment mode.
4. Positional case identity should be instrumented using stable IDs through evaluation pipelines rather than inferred from array arithmetic.

## Scope and caution

The transductive observation is directly supported by the inspected code. It is not inherently a defect if the intended operating regime is transductive and the claim is scoped accordingly.

The off-by-one consequence is a static code inference and should be execution-verified before claiming quantitative impact or invalidating reported experimental results.
