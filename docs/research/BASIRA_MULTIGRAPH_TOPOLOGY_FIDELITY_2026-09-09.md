# BASIRA Multigraph Integration and Topology-Fidelity Scour — 2026-09-09

Status: research/provenance only. Source methods are studied for transferable computational patterns and failure modes; they are not canonical HC mechanisms merely because they are published or implemented.

## Sources inspected in this pass

- `basiralab/MultiGraphGAN`
- `basiralab/topoGAN`
- `basiralab/MGN-Net`
- `basiralab/MICNet`
- `basiralab/survey-multigraph-integration-methods`
- `basiralab/ReMI-Net`
- `basiralab/netNorm-PY`
- `basiralab/SM-netFusion-PY`
- `basiralab/NAGFS-PY`

## Source-supported findings

### MultiGraphGAN and topoGAN — “topology-aware” is metric-scoped

DOCUMENTED from the project READMEs: MultiGraphGAN/topoGAN jointly predict multiple target brain graphs from one source graph and add topology-aware regularization intended to preserve target-graph topology.

OBSERVED from `MultiGraphGAN/prediction.py`: the implemented generator-side topology term combines:

- a global L1 loss between generated and target graph feature vectors;
- a local graph-metric loss computed from `topological_measures(...)`.

OBSERVED from `centrality.py`: `topological_measures` calculates closeness, betweenness, and eigenvector centrality arrays.

OBSERVED from `prediction.py`: the local topology loss actually indexes only element `0`, i.e. closeness centrality, despite all three centrality families being computed.

Therefore the implementation's “topology-aware” objective is not evidence that the complete target topology is preserved. It demonstrates a useful but narrower pattern: constrain generation against declared structural observables in addition to element-wise reconstruction.

HC transfer rule:

`MATCHED_TOPOLOGY_METRIC != MATCHED_TOPOLOGY`

`TOPOLOGY_REGULARIZED != TOPOLOGY_VERIFIED`

A future HC topology-fidelity claim must name the metric family, topology plane, time interval, resolution, weighting/direction/sign conventions, and tolerances actually tested.

### Static code-review finding in MultiGraphGAN

OBSERVED from the current source snapshot: `cluster_index_list` is assigned inside the discriminator's `for par in range(nb_clusters)` loop. In the subsequent generator-training loop, `for par in range(nb_clusters)`, the source as inspected does not recompute `cluster_index_list` before indexing embeddings and target graphs. As written, that means the generator loop appears to reuse the last discriminator-loop cluster index set while iterating all generator clusters.

This is a source-code review finding, not an HC defect and not a claim about published experimental results.

HYPOTHESIS: if this code path executes exactly as inspected, cluster-specific generator training may not actually train each generator on its corresponding cluster as intended.

Required falsification: execute an instrumented training step or unit test that logs `par`, `cluster_index_list`, selected sample IDs, and generator identity for each generator update.

Transfer lesson: do not inherit architecture claims from labels or diagrams without tracing the actual state/index path through implementation.

`NAMED_CLUSTER_SPECIFIC != VERIFIED_CLUSTER_SPECIFIC_EXECUTION`

### MGN-Net — representative normalization remains a population object

DOCUMENTED from the README: MGN-Net integrates heterogeneous multi-view biological-network populations into a single centered, representative and topologically sound connectional template, with emphasis on population fingerprints and typical/atypical differences.

HC relevance: learned normalization can produce useful reference/template state.

Boundary:

`CENTERED_TEMPLATE != INSTANCE_STATE`

`REPRESENTATIVE_OF_POPULATION != REPRESENTATIVE_OF_CURRENT_INDIVIDUAL`

### MICNet — end-to-end task optimization changes the meaning of integration

DOCUMENTED from the README: MICNet learns a subject-specific single-view integrated graph from a heterogeneous multigraph and jointly trains that integration block with a classifier under one end-to-end objective.

HC relevance: task-coupled integration can preserve features useful for one decision while suppressing information irrelevant to that training objective.

Therefore:

`CLASSIFICATION_OPTIMIZED_INTEGRATION != GENERAL_PURPOSE_FUSION`

`TASK_PERFORMANCE != INFORMATION_PRESERVATION`

Any HC learned fusion path used across multiple cognitive purposes must disclose the task/objective that shaped it and should not be assumed neutral.

### Comparative multigraph-integration survey — fidelity is multidimensional

DOCUMENTED from the survey README: the comparison of connectional-brain-template methods evaluates multiple distinct criteria, including centeredness, biomarker reproducibility, node-level similarity, global-level similarity, distance-based similarity, modularity, efficiency, participation, centrality families, and other graph measures.

HC relevance: no single scalar deserves the unqualified name “topology fidelity.” A representation can score well on one structural projection and poorly on another.

A useful HC fidelity report is therefore a vector of scoped tests, not a universal score.

`ONE_METRIC_PASS != REPRESENTATION_FIDELITY_PASS`

### netNorm — local selective fusion is not neutral fusion

DOCUMENTED from the README: netNorm selects, for each local pairwise connectivity, a representative cross-view feature vector from a population before estimating a representative tensor and nonlinearly fusing it into a final template.

HC relevance: selective local fusion is preferable to naive global averaging in some settings, but selection changes provenance and can discard minority/discordant evidence.

`SELECTED_REPRESENTATIVE != COMPLETE_EVIDENCE_SET`

The HC must preserve the fact that a fused value was selected/aggregated and retain access to materially dissenting source evidence when consequential.

### SM-netFusion — supervised topology weighting imports the training objective

DOCUMENTED from the README: SM-netFusion uses class-specific feature extraction/clustering and supervised multi-topology cross-diffusion, weighting multiple topological measures to improve representative/discriminative atlas construction.

HC relevance: learned weighting of structural measures can be useful for context-specific inference, but supervision imports a target objective into the representation.

`SUPERVISED_TOPOLOGY_WEIGHT != INTRINSIC_TOPOLOGICAL_IMPORTANCE`

A discriminative topology measure must not silently become semantic importance, salience, authority, or a general-purpose routing priority.

### NAGFS — discriminative features are not causal mechanisms

DOCUMENTED from the README: NAGFS identifies discriminative graph features by comparing learned group network atlases, motivated partly by retaining original feature identity for biomarker interpretation.

HC relevance: source-traceable feature selection is useful for explanation and diagnosis of model behavior.

Boundary:

`DISCRIMINATIVE_FEATURE != CAUSAL_MECHANISM`

`FEATURE_SELECTED != FEATURE_TRUE`

`BIOMARKER_REPRODUCIBLE != COGNITIVE_AUTHORITY`

### ReMI-Net — temporal template prediction preserves the forecast/instance divide

DOCUMENTED from the README: ReMI-Net infers a baseline population connectional template and predicts its longitudinal follow-up templates using recurrent graph blocks, time-dependent loss, cyclic recursion, and learned normalization.

HC relevance: recurring graph state can predict a trajectory of reference/topology representations.

Boundary:

`PREDICTED_TEMPLATE_TRAJECTORY != INSTANCE_HISTORY`

`RECURRENT_HIDDEN_STATE != HC_CURRENT_MEMORY`

The forecast remains tied to its baseline evidence cut and model version.

## Canonical implications

### Fidelity must be declared as a test vector

A material representation-fidelity report should identify the independent dimensions actually evaluated. Candidate dimensions include:

- element/edge-value reconstruction;
- local topology metrics;
- global topology metrics;
- higher-order hyperedge structure;
- temporal order/timing;
- provenance retention;
- source disagreement retention;
- correspondence retention;
- protected-field retention;
- uncertainty calibration;
- task-general versus task-specific information retention;
- round-trip reconstruction;
- perturbation/reproducibility stability.

No component may collapse an arbitrary subset of these into an unlabeled `fidelity` or `topology_preserved=true` claim.

### Training objective is part of representation provenance

If a fusion/alignment/compression model was optimized for classification, centeredness, reconstruction, adversarial indistinguishability, biomarker discrimination, graph metrics, or another target, that target is material provenance.

It tells downstream HC systems what the representation was trained to preserve and what it may have learned to discard.

### Minority and dissent retention

Population-template and selective-fusion methods repeatedly expose a general issue: a centered/representative result can suppress rare but important evidence.

HC should therefore distinguish:

`REPRESENTATIVE_SUMMARY`

from

`SOURCE_SET_WITH_DISSENT`

and should retain exceptional evidence when its consequence, novelty, fault, authority, safety, or continuity relevance justifies retention.

### Metric-conditioned learning must not create hidden control policy

Centrality, modularity, efficiency, centeredness, discriminativeness, reconstruction error, and other graph metrics may be training or diagnostic objectives. They must not silently become organism-wide reward, salience, authority, or executive-control variables.

## Current disposition

KEEP this source set as research/provenance. Promote only the generic fidelity/provenance constraints that survive HC's complete-organ, temporal-hypergraph, epistemic, authority, and protected-state boundaries.

No BASIRA source code is copied into HC.