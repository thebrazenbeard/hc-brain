# Network-Neuroscience / BASIRA Deep Source Scour — 2026-09-09

Status: research/provenance intake. This file records source-supported methods and bounded HC transfer hypotheses. It is not itself canonical architecture, biological proof, or implementation qualification.

## Scope

Patrick supplied `nilearn/nilearn`, `cwatson/brainGraph`, `basiralab/RegGNN`, `basiralab/DGN`, `basiralab/GSR-Net`, and directed a deeper scour of the BASIRA Lab GitHub organization. This pass also inspected BASIRA repositories surfaced from that search where the method bears directly on HC connectivity inference, multimodal integration, temporal topology prediction, topology diagnostics, uncertainty, or higher-order graph processing.

No source code was copied into HC in this pass. Method ideas are recorded with provenance and separated from HC architectural inference.

## 1. nilearn/nilearn — connectivity estimation as an inference family

**OBSERVED from `nilearn/connectome/connectivity_matrices.py` (blob `64b2bfbbc7f463ea7b1e89ac9bbe30753ee3fbc8`):** `ConnectivityMeasure` computes multiple functional-connectivity representations from subject time series: covariance, correlation, partial correlation, precision, and tangent-space representations. The covariance estimator is explicit; the default Ledoit-Wolf estimator shrinks covariance estimates. Tangent mode uses a group geometric mean/reference and whitening transform.

**HC transfer hypothesis:** connectivity must be typed by estimator and derivation path. A measured signal does not become an observed edge merely because an estimator produces a matrix.

Candidate separations:

`MEASURED_SIGNAL != INFERRED_CONNECTIVITY`

`CORRELATION != PARTIAL_CORRELATION != PRECISION != TANGENT_REPRESENTATION`

`ESTIMATOR_OUTPUT != PHYSICAL_REACHABILITY`

`GROUP_REFERENCE != INSTANCE_CURRENT_STATE`

A population/group reference can be useful for calibration or comparison while remaining a reference, not authority over the current HC instance.

## 2. cwatson/brainGraph — topology diagnostics and null-model discipline

**OBSERVED from repository README:** `brainGraph` is an R package for graph-theory analysis of brain MRI networks compatible with `igraph`. It supports structural covariance, tractography, and resting-state functional networks; graph- and vertex-level measures; GLM/permutation/group analyses; null/random graph generation; small-world metrics; rich-club analysis; bootstrapping; and individual-contribution analyses.

**HC transfer hypothesis:** graph metrics are useful observability/diagnostic signals over a declared HC topology snapshot but should not become hidden control objectives.

`GRAPH_METRIC != COGNITIVE_VALUE`

`CENTRALITY != EXECUTIVE_AUTHORITY`

`RICH_CLUB_MEMBERSHIP != IDENTITY_OR_CONTROL_AUTHORITY`

Null-model and perturbation baselines are especially useful for testing whether apparent HC organization exceeds trivial consequences of density/degree constraints and for detecting pathological centralization, fragmentation, or synchronization.

Human atlas/hemisphere assumptions in brainGraph do not transfer into HC topology requirements.

## 3. basiralab/DGN — representative connectional templates

**DOCUMENTED from README blob `13b3fd4f92ded83307abf7a28ebda426d5a5bb1d`:** Deep Graph Normalizer integrates populations of multi-view brain networks into a single connectional brain template (CBT). It uses graph-convolutional geometric deep learning and a weighted loss intended to improve template centeredness/representativeness.

**HC transfer hypothesis:** reference-template learning can support calibration, anomaly detection, initialization priors, or population comparison, but a normalized/reference topology must not overwrite instance state.

`POPULATION_TEMPLATE != INSTANCE_TOPOLOGY`

`CENTERED_REFERENCE != TRUE_TOPOLOGY`

`REPRESENTATIVE != AUTHORITATIVE`

A template-derived prior should retain source population, estimator, uncertainty, applicability scope, and version.

## 4. basiralab/RegGNN — graph regression and sample-conditioned inference

**OBSERVED from repository tree and `proposed_method/RegGNN.py` blob `1b030ffbe8727e1973b488b3e684ef5794cece6f`:** the proposed model is a compact PyTorch-Geometric regression GNN using two `DenseGCNConv` layers and a linear output head with MSE loss. The repository also contains sample-selection and comparison methods.

**HC transfer hypothesis:** graph-conditioned regressors are candidate bounded estimators of derived state; their scalar/vector predictions remain hypotheses with model/version/input provenance.

`GNN_REGRESSION_OUTPUT != OBSERVED_STATE`

`LOW_LOSS != SEMANTIC_AUTHORITY`

## 5. basiralab/GSR-Net — graph super-resolution

**DOCUMENTED from README blob `e6c3b63c2aca4e0111ffc28c1f1a33414091e3c4`:** GSR-Net learns node embeddings from a low-resolution connectome, applies a graph super-resolution operation to predict a higher-resolution connectome with additional nodes/edges, and then learns embeddings on the super-resolved graph.

**HC transfer hypothesis:** resolution-changing reconstruction can propose latent/detail structure, but synthetic detail cannot be relabeled as observed physical or effective topology.

`SUPER_RESOLVED_GRAPH != OBSERVED_HIGH_RESOLUTION_GRAPH`

`PREDICTED_EDGE != COMMITTED_EDGE`

Any use for HC topology reconstruction must retain source resolution, mapping assumptions, uncertainty, and whether a proposed node/edge is representational, predicted, physically measured, logically eligible, or committed through governed plasticity.

## 6. basiralab/HCAE — higher-order multi-view representation

The earlier HC intake records HCAE separately. It remains the clearest BASIRA example in this source family of explicit hypergraph incidence construction and hypergraph convolution over multi-view connectomic data.

The transfer boundary remains:

`HCAE_HYPEREDGE != HC_FUNCTIONAL_COALITION`

HCAE supplies implementation ideas for higher-order representation/message propagation, not HC timing, authority, continuity, or coalition semantics.

## 7. basiralab/GraphGradIn — influence analysis and leave-one-out counterfactuals

**DOCUMENTED from README blob `11cdf448d938b676c05f18202c845841d7cec3e8`:** GraphGradIn and GraphTestIn estimate how influential individual training multigraphs are for GNN-based population fusion. GraphGradIn uses gradients with respect to GNN weights during training; GraphTestIn removes a sample during refinement/test analysis to estimate its influence.

**HC transfer hypothesis:** influence estimates can be used to audit training/plasticity inputs and detect outsized dependence on a narrow set of episodes/sources.

`INFLUENCE_SCORE != TRUTH`

`TRAINING_INFLUENCE != CAUSAL_IMPORTANCE`

A particularly useful HC test pattern is source ablation: remove or downweight one candidate memory/evidence/training source and measure how much a learned topology/prediction changes. Large sensitivity should surface as provenance/risk, not automatically delete the source.

## 8. basiralab/FMDGNN — federated multi-domain graph prediction

**DOCUMENTED from README blob `b2a3a510c7c8cf98fecc625a9626ba9a5d7a3ac7`:** FMDGNN predicts varying target graph domains from a source graph across decentralized hospitals while addressing non-IID/statistically heterogeneous data. It uses residual graph autoencoding and domain-specific GNN decoders.

**HC transfer hypothesis:** the useful abstraction is domain-local processing with explicit heterogeneous-domain mappings, not federated deployment itself. HC multimodal/domain fusion should preserve each source domain rather than silently force every modality into one ontology.

`DOMAIN_ALIGNMENT != SEMANTIC_EQUIVALENCE`

`FEDERATED_AGGREGATE != INSTANCE_AUTHORITY`

## 9. basiralab/TAF-GNN — longitudinal domain alignment

**DOCUMENTED from README blob `64f8ea4ae544a09fa22ce7df2d9192f158507297`:** TAF-GNN aligns heterogeneous decentralized longitudinal graph domains to a prior universal CBT trajectory and then trains 4D GNN trajectory models.

**HC transfer hypothesis:** alignment is an explicit transformation with reference dependence. For HC, any cross-domain/time alignment should preserve source domain, target domain, transform identity, reference identity, temporal uncertainty, and residual error.

`ALIGNED_STATE != ORIGINAL_STATE`

`UNIVERSAL_TEMPLATE != UNIVERSAL_TRUTH`

## 10. basiralab/FLAT-Net — cluster-specific templates and model selection

**DOCUMENTED from README blob `b0fed01cf3b15eed261fde7a0968af2f9bb4f185`:** FLAT-Net clusters training networks, builds cluster-specific CBTs, trains a separate temporal generative model per representative template, and selects a submodel for a test subject based on proximity to a cluster template.

**HC transfer hypothesis:** context-specific model ensembles may be better than one monolithic predictor, but nearest-template selection is a routing/model-choice heuristic rather than authority.

`NEAREST_MODEL != TRUE_MODEL`

`MODEL_SELECTION != EFFECT_AUTHORIZATION`

## 11. basiralab/GmTE-Net — multimodal graph trajectory forecasting

**DOCUMENTED from README blob `ea4738607ebc2bbd11cc704cf33c020ac8e59b51`:** GmTE-Net forecasts multiple graph trajectories/modalities from a baseline graph under few-shot conditions using teacher/student learning and topology-aware distillation.

**HC transfer hypothesis:** an HC world/plasticity model may maintain several predicted topology trajectories at different resolutions/modalities. These are forecasts, not history or current topology.

`FORECAST_TRAJECTORY != HISTORY`

`DISTILLED_TOPOLOGY_PRIOR != CURRENT_TOPOLOGY`

## 12. basiralab/TIS-Net — inter-modality one-shot super-resolution

**DOCUMENTED from README blob `f7737cfdee18649c4beff8b0f7460e9c7b2e370d`:** TIS-Net maps a source representative template to a target modality/resolution using a graph generative model trained from one representative CBT.

**HC transfer hypothesis:** sparse-data transfer can be useful for bootstrapping a hypothesis in a new sensor/body/domain, but template-driven inferred structure must remain provisional until instance-specific calibration/evidence supports it.

`ONE_SHOT_TEMPLATE_PREDICTION != INSTANCE_OBSERVATION`

## 13. basiralab/DynGNN — temporal prediction with explicit memory mechanisms

**OBSERVED from README blob `2d6f710bda7afc229e64d05c1c702a73f45ea24b` and repository tree:** DynGNN is described as a dynamic memory-enhanced generative GNN for temporal brain-connectivity prediction. Its repository includes recurrent graph models such as graph-convolutional LSTM/GRU variants, temporal GNN dependencies, reservoir-style experiments, and explicit memory-capacity evaluation artifacts.

**HC transfer hypothesis:** useful as a computational comparison class for temporal state propagation and predictive memory. It does not justify collapsing HC current memory, deep memory, temporal topology, and recurrent hidden state into one object.

`RECURRENT_HIDDEN_STATE != HC_MEMORY_CANON`

`TEMPORAL_PREDICTION_STATE != CURRENT_STATE`

## 14. basiralab/predUncertaintywithDomainShift — uncertainty under distribution shift

**DOCUMENTED from README blob `da512db07db569788b1a4fb9fc41e618ba5ce7ac`:** this work uses ensembles of regression GNNs to estimate predictive uncertainty when target distributions shift between training and testing.

This is highly transferable to HC epistemic governance:

`IN_DISTRIBUTION_ACCURACY != OUT_OF_DISTRIBUTION_RELIABILITY`

`MODEL_DISAGREEMENT != TRUTH_BUT_IS_RELEVANT_UNCERTAINTY_EVIDENCE`

A conforming HC predictor should surface domain/shift evidence and uncertainty rather than preserve calibrated-looking confidence after its operating distribution changes.

## 15. basiralab/DeltaGNN — information-flow control and topological bottlenecks

**DOCUMENTED from README blob `1baf6fbd3c7a3d51864e7449ffc20b3af1f48ecb`:** DeltaGNN is a topology-aware GNN architecture with an interaction-decoupling module and information-flow-control mechanism. The repository/paper framing explicitly targets GNN information-flow pathologies including oversmoothing and oversquashing. Search of the code confirms a `DeltaGNN` implementation with topology-aware/flow-control options.

This is directly relevant to Noöplex Fabric and HC topology governance as a research mechanism:

- rich connectivity should not imply indiscriminate message mixing;
- long-range integration should remain selective and capacity-aware;
- topology-aware gating can be evaluated against oversmoothing/oversquashing-like failure modes;
- local and long-range interaction channels can be compared without turning the mechanism into a central executive.

Transfer boundary:

`MESSAGE_MIXING != COGNITIVE_INTEGRATION`

`FLOW_CONTROL != EFFECT_AUTHORITY`

`TOPOLOGICAL_IMPORTANCE != SEMANTIC_IMPORTANCE`

This source is newer than most BASIRA connectome code inspected in the first pass and deserves a separate implementation-readiness study before any primitive is adopted.

## Cross-source synthesis

Across these sources, the strongest transferable pattern is not one particular GNN. It is the need to classify **how a connectivity/topology object came into existence**.

Candidate HC topology-evidence classes include:

- physically measured reachability;
- signal-derived statistical connectivity;
- learned logical eligibility;
- configured routing/bindings;
- inferred/reconstructed connectivity;
- predicted future connectivity;
- population/reference template;
- aligned/normalized representation;
- latent embedding;
- super-resolved representation;
- current effective pairwise relation;
- current effective higher-order hyperedge/coalition;
- committed plastic topology change.

Those classes cannot safely share one undifferentiated `edge confidence` field.

## Candidate canonical invariants

The source study supports testing the following HC design rules:

- `MEASURED_SIGNAL != INFERRED_CONNECTIVITY`
- `STATISTICAL_CONNECTIVITY != PHYSICAL_REACHABILITY`
- `INFERRED_OR_RECONSTRUCTED_EDGE != COMMITTED_PLASTIC_EDGE`
- `PREDICTED_TOPOLOGY != CURRENT_TOPOLOGY`
- `POPULATION_TEMPLATE != INSTANCE_TOPOLOGY`
- `ALIGNED_OR_NORMALIZED_REFERENCE != AUTHORITY`
- `SUPER_RESOLVED_GRAPH != OBSERVED_HIGH_RESOLUTION_GRAPH`
- `LATENT_EMBEDDING != SEMANTIC_TRUTH_OR_IDENTITY_STATE`
- `GRAPH_METRIC != CONTROL_OBJECTIVE`
- `CENTRALITY != EXECUTIVE_AUTHORITY`
- `MODEL_SELECTION != EFFECT_AUTHORIZATION`
- `DOMAIN_ALIGNMENT != SEMANTIC_EQUIVALENCE`
- `IN_DISTRIBUTION_PERFORMANCE != OUT_OF_DISTRIBUTION_RELIABILITY`
- `INFLUENCE_SCORE != CAUSAL_TRUTH`
- `MESSAGE_FLOW_CONTROL != COGNITIVE_AUTHORITY`

## Recommended implementation experiments

1. Build a typed `TopologyEvidence` envelope that requires origin class, source modality/domain, estimator/model identity, time/interval, uncertainty, reference/template identity when applicable, resolution, transform/alignment provenance, and eligibility for downstream topology mutation.
2. Run null-model/perturbation diagnostics inspired by brainGraph before interpreting hub/rich-club/community structure as meaningful HC organization.
3. Evaluate source-ablation sensitivity inspired by GraphGradIn/GraphTestIn for plasticity and learned-topology updates.
4. Maintain ensembles or shift detectors for topology/world-model predictions and deliberately test out-of-distribution calibration.
5. Compare HC higher-order message passing against HCAE/HUNet-style hypergraph operators while measuring what typed temporal/authority semantics are lost by numerical projection.
6. Test topology-aware information-flow control against runaway global coupling, oversmoothing, bottlenecked long-range information, and false centralization.
7. Treat every generative/super-resolution output as a candidate hypothesis until corroborated or separately admitted through governed plasticity.

## Current disposition

**KEEP as research/provenance.** The source family materially strengthens HC's topology-evidence and diagnostic design, but it does not replace the temporal-hypergraph architecture and does not prove biological or synthetic-organ feasibility.

A canonical `CONNECTIVITY_INFERENCE_AND_TOPOLOGY_EVIDENCE` contract should be considered. Four should challenge implementation readiness and design negative tests; Vera should hostile-review for estimator-to-truth leakage, population-template authority, generated-edge promotion, hidden centralization, and temporal-state conflation before final qualification.