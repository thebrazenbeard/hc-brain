# BASIRA Lab Deep Scour — Continuation Cut 3 — 2026-09-09

Status: research/provenance only. This cut records code-level findings from RegGNN, DGN, and GSR-Net. No source code is copied and no method below is promoted directly into canonical HC architecture.

## Source bindings

- `basiralab/RegGNN` `main@e1be911358f23a357c47c701981fd2dc83277bb0`
- `basiralab/DGN` `master@0f5aa1433c76a49a880df40535e0b02923e21959`
- `basiralab/GSR-Net` `master@bb54332a7d8fc94615860b61703e068ea1f40eb7`

Read depth for this cut extends beyond README claims into model/evaluator/preprocessing code where noted.

## 1. RegGNN — topology-aware regression and target-conditioned sample selection

### DOCUMENTED source framing

RegGNN predicts continuous cognitive scores from functional connectomes while preserving graph structure instead of flattening each connectome into an ordinary vector. The project also implements a learning-based sample-selection procedure and supports several graph/connectome representations, including Riemannian/geodesic, tangent, centrality, and concatenated topological features.

### OBSERVED code behavior

`proposed_method/RegGNN.py` is a compact graph-regression model built from two dense graph-convolution layers followed by a learned linear readout and MSE loss.

`proposed_method/sampleSelection.py` does something more important for HC research: within the supplied training indices it learns a linear relation between pairwise connectome distance and pairwise target-score error. For held-out members of the internal selection folds, it predicts which training samples should have the smallest target error and accumulates the most frequently selected samples for each requested `k`.

`evaluators.py` invokes that selection only from each outer fold's training indices before evaluating the selected model on the outer test indices. The inspected path therefore supports the claim that sample selection is nested inside the outer train split rather than directly selecting from the outer test fold.

### Transfer

The useful HC lesson is **not** that central subjects are inherently more important. It is that exemplar/evidence selection can be learned relative to a declared prediction objective and representation metric.

Required separations:

`SELECTED_FOR_TARGET_PREDICTION != GENERALLY_IMPORTANT_EVIDENCE`

`PREDICTED_HELPFULNESS != EPISTEMIC_TRUTH`

`FREQUENT_SELECTION != PROTECTED_RETENTION_PRIORITY`

`GRAPH_DISTANCE_METRIC != UNIVERSAL_SIMILARITY`

A future HC exemplar selector, rehearsal sampler, memory-retrieval ranker, or training-data curriculum should therefore bind at least:

- objective/task;
- source evidence class;
- distance/similarity representation;
- training/selection split;
- current data regime;
- uncertainty/coverage;
- protected-retention exclusions.

The selector must not delete rare contradictory evidence, revocation state, fault history, continuity-bearing material, or other protected content merely because those records are poor predictors for one target.

### Hostile controls

1. Create a rare sample that is low-ranked for the current prediction target but contains the only evidence of a critical fault or revoked authority. Selection may deprioritize it for one regression task but must not erase protected retention.
2. Change the target variable while holding graph data fixed. The selected sample set is allowed to change; if it does, the system must not claim the prior set was generally "representative".
3. Change the graph-distance representation. Selection sensitivity must remain visible rather than being laundered into one objective-free importance score.
4. Compare nested selection against a deliberately leaky selection baseline to ensure qualification can detect split contamination.

## 2. DGN — learned population template, multiview edge conditioning, and evaluation leakage hazard

### DOCUMENTED source framing

DGN estimates one connectional brain template from a population of multi-view brain networks. The README describes the target as representative/centered/discriminative and accepts tensors shaped approximately `subjects × nodes × nodes × views`.

### OBSERVED model construction

In `model.py`, DGN uses three `NNConv` layers with mean aggregation. `helper.cast_data()` turns each multiview matrix into a graph whose node features are all ones and whose edge attributes contain the values from the different views. In this implementation, multiview information is therefore carried as **edge features** into edge-conditioned message passing; it is not represented as HC-style higher-order temporal hyperedges.

The model's node outputs are expanded pairwise and converted to an adjacency-like template through absolute differences summed across the learned embedding dimension. A post-training helper runs the model across training subjects and takes an elementwise median of the resulting learned subject-biased templates to obtain the final population template.

This produces an important evidence distinction:

`LEARNED_POPULATION_TEMPLATE != OBSERVED_GRAPH`

`MEDIAN_OF_MODEL_OUTPUTS != MEASURED_POPULATION_STATE`

`MULTIVIEW_EDGE_FEATURES != HIGHER_ORDER_HYPEREDGE`

### OBSERVED evaluation concern

`train_model()` creates train/test folds through `helper.preprocess_data_array()`. During the epoch loop it periodically computes representativeness error on that nominal test fold, appends those values to `test_errors`, uses the trend to decide early stopping, saves candidate weights keyed by that test-fold score, and later restores the candidate associated with the minimum recorded test error.

For that inspected code path, the fold named `test` participates in model selection. It therefore behaves as validation evidence for early stopping/best-checkpoint selection rather than as a sealed untouched final holdout.

This is a code-level observation about the repository path, not a claim that every experiment in the publication used an invalid protocol.

HC qualification consequence:

`HELD_OUT_USED_FOR_MODEL_SELECTION != FINAL_BLIND_TEST`

`EARLY_STOPPING_SIGNAL != INDEPENDENT_FINAL_EVIDENCE`

A future HC learning/qualification harness should distinguish at least training, tuning/selection, and final untouched qualification cuts where the claim needs a blind holdout. If a split influences checkpoint selection, threshold choice, architecture choice, repair, prompt/policy tuning, or stopping, it must not later be reported as untouched final evidence.

### Additional reproducibility observation

DGN explicitly seeds NumPy/Torch and requests deterministic cuDNN behavior. This is useful engineering discipline, but deterministic execution under one stack is not identical to reproducibility across environments, library versions, hardware, or data pipelines.

`FIXED_SEED != FULL_REPRODUCIBILITY`

## 3. GSR-Net — graph super-resolution is generated topology, and preprocessing/model transforms are semantically material

### DOCUMENTED source framing

GSR-Net predicts high-resolution connectomes from low-resolution connectomes, including additional nodes/edges. Its published/demo framing uses a low-resolution graph, learned node features, a graph super-resolution operation, and high-resolution graph convolutions.

### OBSERVED transformation chain

The inspected implementation performs several materially semantic transformations:

- `preprocessing.py` takes the absolute value of loaded connectivity matrices;
- NaN locations are replaced by the literal value `1` even though a column mean is computed separately and not used for that replacement;
- padding functions force diagonal entries to `1`;
- `model.py` normalizes the low-resolution adjacency, applies the Graph U-Net/super-resolution path, symmetrizes the final prediction, forces its diagonal to `1`, and takes absolute values;
- `layers.py` also constructs an intermediate adjacency by taking absolute values, filling the diagonal, normalizing, multiplying the normalized matrix by its transpose, symmetrizing, and forcing a diagonal;
- the graph super-resolution layer contains a diagonal mask hard-coded to size `320` even though the surrounding model accepts a configurable `hr_dim`.

These transformations are implementation choices, not observations of the source graph.

HC transfer requirements:

`ABS_TRANSFORMED_RELATION != ORIGINAL_SIGNED_RELATION`

`SYMMETRIZED_RELATION != RAW_DIRECTIONAL_RELATION`

`FORCED_SELF_LOOP != OBSERVED_SELF_RELATION`

`IMPUTED_VALUE != MEASURED_VALUE`

`GENERATED_HIGH_RESOLUTION_GRAPH != OBSERVED_HIGH_RESOLUTION_GRAPH`

`DECLARED_TARGET_DIMENSION != HARDCODED_IMPLEMENTATION_DIMENSION`

The hard-coded `320` mask is an OBSERVED portability/parameterization defect in this code path. It should not be generalized into a criticism of graph-super-resolution theory, but it is an excellent HC adversarial test: a supposedly generic topology-transform component must be tested away from its development dimensions and must reject or expose incompatible shapes rather than silently carrying fixed-size assumptions.

### Cross-validation implementation observation

`demo.py` creates one `GSRNet` model and one optimizer before iterating over KFold splits, then repeatedly calls `train(model, optimizer, ...)` across folds without reinitializing model/optimizer inside the fold loop. On the literal demo path, later folds therefore begin from model/optimizer state already trained on earlier folds.

This means the demo is not a clean independent cross-validation implementation if interpreted as ordinary fold-isolated CV.

Again, this is a repository-code observation, not a blanket statement about all reported paper experiments.

HC qualification consequence:

`FOLD_BOUNDARY != STATE_RESET`

`CROSS_VALIDATION_LABEL != INDEPENDENT_FOLD_STATE`

A qualification harness should make reset scope explicit for model parameters, optimizer state, replay buffers, caches, learned topology, memory, calibration, and random-state lineage.

### Hostile controls

1. Run a resolution-transform component at dimensions unlike its development fixture; fixed-size assumptions must fail visibly or adapt correctly.
2. Supply signed relations where sign matters; an absolute-value transform must be explicit and reversible/traceable or rejected for that claim.
3. Supply asymmetric/directional relations; forced symmetrization must not masquerade as measured symmetry.
4. Supply missing entries; imputation method and imputed locations must remain provenance-bearing.
5. Run fold-isolation qualification with intentional state carryover; the harness must detect parameter/optimizer/cache contamination.
6. Compare multiple plausible high-resolution reconstructions from one coarse input; uncertainty/underdetermination must survive rather than collapsing to one pseudo-observation.

## 4. Licensing / source-use boundary

GitHub repository metadata for the three inspected BASIRA repositories did not expose a detected license at this cut, and direct checks did not find a root `LICENSE` file at the obvious paths tested. RegGNN's README states that its code is MIT-licensed, but the corresponding root license artifact was not found in the inspected tree path.

Therefore this HC research cut copies **no source code**. Concepts are paraphrased with exact source/ref/path provenance. Any future code reuse requires independent license resolution.

## 5. Cross-source synthesis

These three repositories jointly strengthen a set of HC implementation rules that are more important than adopting any particular GNN:

1. **Selection is objective-relative.** Learned relevance/representativeness must state what it is useful for.
2. **A template is a derived object.** Population summaries, learned CBTs, and medians of learned outputs remain derived representations, not observed state.
3. **Every topology transform has semantics.** Absolute value, symmetrization, diagonal forcing, imputation, normalization, pooling, contraction, and super-resolution must remain in provenance.
4. **Generated detail is not measured detail.** Super-resolution outputs are predictions/reconstructions unless independently observed.
5. **Qualification requires state isolation.** A nominal test fold used for early stopping is validation-like; a nominal cross-validation loop with carried model state is not independent-fold evidence.
6. **Configuration claims require adversarial dimension tests.** Parameterized interfaces must be tested away from the one hard-coded development shape.
7. **Multiview is not automatically higher-order.** Multiple views carried as edge attributes are a useful graph encoding but not an HC temporal hyperedge merely because several values share an edge.

## 6. Candidate HC promotion targets

Research findings should feed review of:

- `docs/architecture/CONFORMANCE_AND_QUALIFICATION.md` — split-role / sealed-final-holdout / state-reset requirements;
- topology-evidence provenance — transform lineage and generated-vs-observed distinction;
- `cognition/PERCEPTION_AND_MULTIMODAL_INFERENCE.md` — view-specific representation and transform provenance;
- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md` — learned selection/coarsening without protected-state erasure;
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — explicit graph projection vs true higher-order relation;
- future topology-transform machine schemas — dimension/configuration invariants and uncertainty.

No canonical change is proposed by this research note alone. Four should test implementation-readiness and Noah should decide promotion; Vera should hostile-review any proposed promotion for epistemic laundering or accidental topology assumptions.

## Disposition

**KEEP as research/provenance. HIGH VALUE for qualification and transform-lineage rules.**

The most important new negative controls are `SEALED_FINAL_HOLDOUT`, `FOLD_STATE_RESET`, `OBJECTIVE_BOUND_SELECTION`, `TRANSFORM_LINEAGE_PRESERVATION`, and `PARAMETERIZATION_VS_HARDCODED_DIMENSION`.