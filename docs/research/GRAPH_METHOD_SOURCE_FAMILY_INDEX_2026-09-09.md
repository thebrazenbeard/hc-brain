# Graph-Method Source Family Index — 2026-09-09

Status: research provenance / source-disposition index.

## Purpose

This file records the source depth of the 2026-09-09 network-neuroscience and graph-methods deep scout. It prevents three different activities from being conflated:

- **deep read** — README plus implementation/detail files were inspected;
- **method read** — project framing/method/evaluation were inspected from repository material;
- **organization inventory** — repository metadata/name/family were reviewed, but the repository was not treated as a claim-level source.

`ORG_INVENTORIED != REPOSITORY_DEEPLY_READ`

`README_READ != PAPER_INDEPENDENTLY_VERIFIED`

`REPOSITORY_EXISTS != METHOD_VALIDATED`

No source code is copied by this index.

---

## A. Deep-read sources

### `nilearn/nilearn`

Depth: `DEEP_READ`

Inspected:

- `README.rst`, blob `5d7d942a8b536eb546798fb769591d006130ee64`;
- `nilearn/connectome/connectivity_matrices.py`, inspected blob `64b2bfbbc7f463ea7b1e89ac9bbe30753ee3fbc8`.

Useful mechanisms:

- explicit connectivity-estimator kinds;
- covariance-estimator provenance;
- standardization and confound handling;
- tangent-space/group-reference representation;
- dimension/input validation.

HC disposition: `MECHANISM_AND_EVIDENCE_DISCIPLINE_SOURCE`.

Do not transfer: neuroimaging atlas/anatomical packaging as HC topology.

### `cwatson/brainGraph`

Depth: `METHOD_READ`

Inspected:

- `README.md`, inspected blob `30dee10608b27466c6b66c8739c2373e250989e1`.

Useful mechanisms:

- graph statistical testing;
- permutation/bootstrap;
- network-based statistic;
- null/random graph families;
- local/global graph metrics;
- targeted/random failure robustness.

HC disposition: `QUALIFICATION_AND_NULL_MODEL_SOURCE`.

Do not transfer: atlas, lobe, hemisphere or MRI-specific graph packaging as HC topology.

### `basiralab/RegGNN`

Depth: `DEEP_READ`

Inspected:

- `README.md`, blob `0a872b8290f8b9fcc446f5ead8583d56dd976dcc`;
- `proposed_method/RegGNN.py` via code search at repository commit `e1be911358f23a357c47c701981fd2dc83277bb0`.

Useful mechanisms:

- graph-preserving regression rather than flattening;
- topology-derived feature alternatives;
- learned training-sample selection;
- SPD/manifold-aware comparison as source-specific technique.

HC disposition: `TOPOLOGY_AWARE_LEARNING_AND_SAMPLE_SELECTION_SOURCE`.

### `basiralab/DGN`

Depth: `DEEP_READ`

Inspected:

- `README.md`, blob `13b3fd4f92ded83307abf7a28ebda426d5a5bb1d`;
- `model.py` implementation surface via code search at commit `0f5aa1433c76a49a880df40535e0b02923e21959`.

Useful mechanisms:

- nonlinear multi-view graph integration;
- representative/centered template learning;
- end-to-end feedback rather than purely sequential fusion;
- topology-aware population summary.

HC disposition: `MULTIVIEW_FUSION_AND_TEMPLATE_SOURCE`.

### `basiralab/GSR-Net`

Depth: `DEEP_READ`

Inspected:

- `README.md`, blob `e6c3b63c2aca4e0111ffc28c1f1a33414091e3c4`;
- demo/model references to Graph U-Net structure via repository code search at commit `bb54332a7d8fc94615860b61703e068ea1f40eb7`.

Useful mechanisms:

- graph super-resolution;
- explicit source/target resolution;
- predicted nodes/edges as generated structure;
- cross-validation of graph prediction.

HC disposition: `TOPOLOGY_SUPER_RESOLUTION_SOURCE`.

### `basiralab/Gen-HNN`

Depth: `DEEP_READ`

Inspected:

- `README.md`, blob `1ea2743c73b7c380f75255593172e533ffe58d13`;
- `Hypergraph_utilities.py`, blob `a73b7f42ec86df874eb61378ec35cc5e6a52a8f6`.

Observed implementation detail:

- Euclidean feature-space distances;
- K-nearest-neighbor hyperedge construction;
- optional probabilistic incidence weights;
- view-local incidence matrices;
- concatenated multi-view incidence;
- normalized hypergraph propagation operator.

HC disposition: `NUMERICAL_HYPERGRAPH_PROJECTION_SOURCE`.

Explicit non-equivalence:

`KNN_HYPEREDGE != HC_TYPED_TEMPORAL_HYPEREDGE`

### `basiralab/DeltaGNN`

Depth: `DEEP_READ`

Inspected:

- `README.md`, blob `1baf6fbd3c7a3d51864e7449ffc20b3af1f48ecb`;
- repository model inventory;
- `models/delta_gnn_model.py`, blob `e8722f171e96a43605bd3fff35a0efbf4483d346`.

Observed implementation detail:

- layerwise representation-change deltas;
- second differences;
- exponential smoothing/variance-derived scores;
- edge filtering based on flow scores;
- optional heterophily graph construction.

HC disposition: `INFORMATION_FLOW_CONTROL_RESEARCH_SOURCE`.

Explicit boundary:

`REPRESENTATION_CHANGE_SCORE != SEMANTIC_IMPORTANCE_OR_ROUTING_AUTHORITY`

---

## B. Method-read sources

### `basiralab/netNorm-PY`

Depth: `METHOD_READ`

Inspected `README.md`, blob `d8ef457abef523d2f23bc67508ef6f2bbfe0e038`.

Contribution:

- local selective multi-view fusion;
- representative tensor/template estimation;
- heterogeneous-distribution integration under same-size graph assumption.

HC disposition: `LOCAL_RELATION_SPECIFIC_FUSION_SOURCE`.

### `basiralab/SM-netFusion-PY`

Depth: `METHOD_READ`

Inspected `README.md`, blob `4c90188798f6dd7c7074f532004dd60d68e50faa`.

Contribution:

- supervised multi-topology cross-diffusion;
- topology-feature mixtures;
- discriminative population-template objectives.

HC disposition: `SUPERVISED_FUSION_AND_OBJECTIVE_BIAS_SOURCE`.

### `basiralab/survey-multigraph-integration-methods`

Depth: `METHOD_READ`

Inspected `README.md`.

Contribution:

- explicit multigraph integration comparison;
- centeredness;
- biomarker reproducibility;
- local/global topology;
- graph-distance measures;
- multi-metric evaluation rather than one loss.

HC disposition: `MULTI_METRIC_TEMPLATE_QUALIFICATION_SOURCE`.

### `basiralab/EvoGraphNet`

Depth: `METHOD_READ`

Inspected `README.md`, blob `142490dc023c601c927355085a26b6efbe936cb0`.

Contribution:

- cascaded time-dependent graph generation;
- prediction-to-next-prediction ancestry;
- trajectory distribution alignment.

HC disposition: `TOPOLOGY_FORECAST_AND_SYNTHETIC_ANCESTRY_SOURCE`.

### `basiralab/GmTE-Net`

Depth: `METHOD_READ`

Inspected `README.md`, blob `ea4738607ebc2bbd11cc704cf33c020ac8e59b51`.

Contribution:

- multi-trajectory graph evolution;
- teacher/student few-shot learning;
- topology-aware distillation;
- multiple modalities/resolutions.

HC disposition: `MULTITRAJECTORY_FORECAST_AND_DISTILLATION_SOURCE`.

### `basiralab/MultigraphGNet`

Depth: `METHOD_READ`

Inspected `README.md`, blob `a335d7d04f03170adb60917747838aff3f160175`.

Contribution:

- many-to-one graph-template compression;
- one-to-many reconstruction;
- cyclic reconstruction objective;
- synthetic data augmentation.

HC disposition: `COMPRESSION_RECONSTRUCTION_AND_SYNTHETIC_DATA_SOURCE`.

### `basiralab/predUncertaintywithDomainShift`

Depth: `METHOD_READ`

Inspected `README.md`, blob `da512db07db569788b1a4fb9fc41e618ba5ce7ac`.

Contribution:

- ensembles for regression-GNN predictive uncertainty;
- explicit target-domain shift;
- calibration concern beyond IID evaluation.

HC disposition: `DOMAIN_SHIFT_UNCERTAINTY_SOURCE`.

### `basiralab/Meta-RegGNN`

Depth: `METHOD_READ`

Inspected `README.md`, blob `ccbebfe11b1566c3698586352b706c77df522799`.

Contribution:

- meta-learning for fast graph-domain adaptation;
- few-gradient-step adaptation to unseen graph distributions.

HC disposition: `FAST_ADAPTATION_AND_SUPPLIED_PRIOR_SOURCE`.

### `basiralab/TAF-GNN`

Depth: `METHOD_READ`

Inspected `README.md`, blob `64f8ea4ae544a09fa22ce7df2d9192f158507297`.

Contribution:

- federated multiview domain alignment;
- decentralized non-IID graph learning;
- template-based alignment prior.

HC disposition: `DISTRIBUTED_DOMAIN_ALIGNMENT_SOURCE`.

### `basiralab/STP-GSR`

Depth: `METHOD_READ`

Inspected `README.md`, blob `4d4f98a38b21cfa487c2733ca0089c82a2697288`.

Contribution:

- topology-preserving graph super-resolution;
- dual/line-graph reparameterization;
- edge-regression-to-node-regression transformation.

HC disposition: `TOPOLOGY_PRESERVING_REPARAMETERIZATION_SOURCE`.

### `basiralab/Dif-GSR`

Depth: `METHOD_READ`

Inspected `README.md`, blob `25c9f3b12707722e84df76525bb19aecd9229039`.

Contribution:

- diffusion-based graph super-resolution;
- distributional generation;
- non-isomorphic/inter-modality source/target graphs.

HC disposition: `DISTRIBUTIONAL_SUPER_RESOLUTION_SOURCE`.

### `basiralab/GraphGradIn`

Depth: `METHOD_READ`

Inspected `README.md`, blob `11cdf448d938b676c05f18202c845841d7cec3e8`.

Contribution:

- gradient-based training-sample influence;
- exclusion/test-phase influence estimation;
- training-set selection based on influence.

HC disposition: `LEARNING_INFLUENCE_AUDIT_SOURCE`.

### `basiralab/FALCON`

Depth: `METHOD_READ`

Inspected `README.md`, blob `5f2a6b13b78dc0502970961800c33e74a1b7344b`.

Contribution:

- graph collapse/coarsening for memory efficiency;
- explicit feature/label preservation objectives;
- centrality-conditioned contraction variants;
- comparison to other scalable GNN techniques.

HC disposition: `GRAPH_COMPRESSION_PRESERVATION_CONTRACT_SOURCE`.

### `basiralab/FireGNN`

Depth: `METHOD_READ`

Inspected `README.md`, blob `64cdb78fb68b08a0e4ebabe18abda7d7900be9d7`.

Contribution:

- trainable fuzzy rules;
- auxiliary topology objectives;
- neuro-symbolic graph-learning interface.

HC disposition: `INTERPRETABLE_SOFT_RULE_RESEARCH_SOURCE`.

### `basiralab/X-Node`

Depth: `METHOD_READ`

Inspected `README.md`, blob `ea2e32c91c67a12dd65a6bde515426b5e7c47a31`.

Contribution:

- topology-aware explanation inputs;
- external language-model explanation generation.

HC disposition: `EXPLANATION_VS_EVIDENCE_BOUNDARY_SOURCE`.

### `basiralab/HGNet`

Depth: `METHOD_READ`

Inspected `README.md`, blob `f67c3778d7d14d091c7382fe6190e207630a8d42`.

Contribution:

- scientific entity/relation extraction;
- hierarchy-aware graph relation extraction;
- LLM-generated multidomain benchmark.

HC disposition: `RESEARCH_TOOLING_CANDIDATE`, not HC cognitive topology source.

Explicit boundary:

`EXTRACTED_SCIENTIFIC_RELATION != DOCUMENTED_SCIENTIFIC_FACT`

---

## C. Organization-level family inventory

The BASIRA organization inventory exposed a much larger research family. The following repositories were classified by apparent/source-described family but were **not all deeply inspected** in this pass.

### Graph/multigraph normalization, templates, and integration

- `DGN`
- `netNorm`
- `netNorm-PY`
- `SM-netFusion`
- `SM-netFusion-PY`
- `MGN-Net`
- `MultigraphGNet`
- `survey-multigraph-integration-methods`
- `HCAE`
- `Gen-HNN`
- `UMC`
- `M2GI-Net`

Disposition: `FAMILY_RELEVANT`; use specific repository only after claim-level read.

### Graph evolution / longitudinal prediction

- `EvoGraphNet`
- `GmTE-Net`
- `FedGmTE-Net`
- `FedGmTE-Net-plus`
- `4D-FED-GNN`
- `4D-FedGNN-Plus`
- `TAF-GNN`

Disposition: `FAMILY_RELEVANT` for forecast, trajectory, domain/federation research.

### Graph super-resolution

- `GSR-Net`
- `AGSR-Net`
- `BGSR`
- `BGSR-PY`
- `Dif-GSR`
- `STP-GSR`

Disposition: `FAMILY_RELEVANT` for predicted topology/resolution research.

### GNN regression / domain shift / uncertainty

- `RegGNN`
- `Meta-RegGNN`
- `predUncertaintywithDomainShift`
- `DuoGNN`
- `uGNN`

Disposition: `FAMILY_RELEVANT`; individual method claims require direct reading.

### Federated graph learning / decentralized learning

- `reproducibleFedGNN`
- `Fed-CBT`
- `Fed2M`
- `RepFL`
- `RepTreeFL`
- `UnifiedFL`
- `UniFed`
- `4D-FED-GNN`
- `FedGmTE-Net`

Disposition: `POTENTIALLY_RELEVANT` for distributed learning/privacy/domain handling, not automatically HC distributed-organ architecture.

### Information-flow, topology, compression, and influence

- `DeltaGNN`
- `FALCON`
- `GraphGradIn`
- `RG-Select`
- `FS-Select`
- `NAGFS`
- `CQSIGN`

Disposition: `FAMILY_RELEVANT` for flow control, sample/feature influence and scalable graph computation.

### Generative graph learning

- `gGAN`
- `CGTS-GAN`
- `topoGAN`
- `Reproducible-Generative-Learning`
- `RBGM`
- `Gen-HNN`

Disposition: `POTENTIALLY_RELEVANT` for candidate generation; generated topology remains predicted/synthetic.

### Explainability / neuro-symbolic / graph reasoning

- `X-Node`
- `FireGNN`
- `HGNet`
- `GraphGradIn`

Disposition: `POTENTIALLY_RELEVANT`, especially as evidence/presentation-boundary research.

### Surveys / bibliographies / tutorials

- `GNNs-in-Network-Neuroscience`
- `graph-based-deep-learning-literature`
- `Awesome-Federated-Learning-on-Graph-and-GNN-papers`
- `MICCAI-OpenSourcePapers`
- `GiNN-MICCAI24-Tutorial`
- `basic-ML-DL-concepts`
- `mathematics-for-DL-book`

Disposition: `DISCOVERY_INDEX_ONLY` unless individual referenced works are independently read.

---

## D. Repositories not treated as BASIRA-origin HC research merely because they appear in the organization

The organization also contains forks or general-purpose/tool repositories such as:

- `langchain`;
- `transformers`;
- `pytorch_geometric`;
- `MONAI`;
- `AutoGPT`;
- `chemprop`;
- `machine_learning_refined`;
- `udlbook`;
- `ManimML`;
- `drawio-desktop`;
- `ipyvizzu`.

These may be useful software/tools in other contexts, but their presence under the BASIRA account is **not evidence that their design should populate HC**.

`ORGANIZATION_FORK_OR_TOOL != BASIRA_RESEARCH_CONTRIBUTION`

---

## E. Source-use rules for future HC work

1. Bind exact source repository and file/commit for any transferred method claim.
2. Distinguish source-description claims from independently verified paper/science claims.
3. Preserve method assumptions such as graph size, isomorphism, atlas, view count, labels, population structure, and training objective.
4. Do not transfer human hemispheres, atlas regions, disease labels, IQ targets, or other task packaging into generic HC topology.
5. Do not import source code merely because its mechanism is useful; licensing and dependency review are separate gates.
6. Generated graphs remain generated/predicted evidence.
7. Learned templates remain summaries/models.
8. Hypergraph incidence structures remain numerical projections unless independently bound to richer HC semantics.
9. External explanation systems remain presentation/derived inference.
10. A source may motivate a hostile test even when no architecture mechanism is adopted.

## Current disposition

The source universe is sufficiently rich to justify continued HC experiments in graph representation, topology learning, higher-order projection, flow control, domain-shift uncertainty, compression, forecasting, super-resolution, and qualification.

It does **not** justify selecting one external graph-learning architecture as the Hyperconnectome Brain runtime.
