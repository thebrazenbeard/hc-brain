# BASIRA Lab Hyperconnectome / Network-Neuroscience Research Intake — 2026-09-09

Status: research/provenance only; not canonical architecture and not documented biological proof of the HC design.

Sources supplied by Patrick:

- `https://github.com/basiralab/GNNs-in-Network-Neuroscience`
- `https://github.com/basiralab/HCAE`

## Source classification

### `basiralab/GNNs-in-Network-Neuroscience`

**DOCUMENTED from repository metadata and README:** this repository is a literature/repository survey of graph-neural-network methods applied to brain-connectivity data, primarily covering work published in 2017–2020. It organizes methods around graph prediction/synthesis, cross-resolution prediction, graph evolution over time, multi-network integration/fusion, disease classification, biomarker identification, and related machine-learning tasks.

**OBSERVED:** the repository tree contains only `README.md`; it is a curated source map rather than an implementation library.

**Transfer status:** useful as a bibliography/discovery index for network-neuroscience methods. It must not be treated as a primary scientific source for the claims of the papers it lists. Individual papers/codebases require claim-level verification before any result is labeled `DOCUMENTED` science inside HC.

### `basiralab/HCAE`

**DOCUMENTED from the project README:** HCAE is the "Multi-View Brain HyperConnectome AutoEncoder" for brain-state classification. The project represents many-to-many relationships through hypergraph structure, creates a hyperconnectome for each brain view, applies hypergraph convolutional autoencoding, and uses adversarial regularization to align learned embeddings/distributions for AD/MCI classification.

**OBSERVED from code:**

- `HCAE.py` accepts one or multiple brain-connectivity matrices per subject;
- multi-view mode concatenates four input views and separately constructs a hypergraph per view before concatenating those hypergraphs;
- `hypergraph_utils.py` builds incidence matrices from k-nearest-neighbor neighborhoods and computes a normalized hypergraph propagation operator of the form `D_v^-1/2 H W D_e^-1 H^T D_v^-1/2`;
- `layers.py` implements a hypergraph-convolution operation by multiplying input features by trainable weights and then by the hypergraph propagation matrix;
- the resulting subject embeddings are evaluated with an SVM in repeated random train/test splits.

**OBSERVED implementation age/portability constraint:** the README states Python 3.7 / TensorFlow 1.5-era dependencies. This should be treated as historical research code, not a ready HC runtime dependency.

**OBSERVED licensing inconsistency:** the README says the code is released under an MIT `LICENSE` file, but the inspected repository tree does not contain a `LICENSE` file and GitHub repository metadata reports no detected license. No HCAE code should be copied into HC unless licensing is independently resolved.

## What transfers conceptually

### 1. Higher-order relation machinery

HCAE is direct evidence that practical machine-learning pipelines can construct and operate on hypergraph incidence structure rather than reducing all relationships to pairwise edges.

This supports continued exploration of hypergraph-native implementation mechanisms for HC, especially for:

- learned logical eligibility;
- representation of higher-order relation candidates;
- multi-participant message aggregation;
- topology-aware representation learning;
- compression/embedding of high-dimensional network state.

It does **not** establish that HCAE's particular nearest-neighbor hyperedge construction is the correct HC cognitive topology.

`HCAE_HYPEREDGE != HC_FUNCTIONAL_COALITION`

HCAE hyperedges are generated from similarity/neighborhood structure in static subject data. HC functional coalitions are typed, provenance-bearing, task/context-scoped temporal hyperedges with authority, timing, uncertainty, lifecycle, and failure semantics.

### 2. Multi-view hypergraph fusion

HCAE's per-view hypergraph construction followed by multi-view fusion is relevant to HC multimodal integration.

A transferable HC pattern is:

`typed modality/view -> view-local higher-order structure -> provenance-preserving fusion -> learned representation`

However, HC should preserve source/view identity, calibration, timing, uncertainty, and disagreement through fusion. Blind concatenation of heterogeneous views is not sufficient as a canonical cognitive-integration rule.

Candidate HC targets:

- `cognition/PERCEPTION_AND_MULTIMODAL_INFERENCE.md`
- `integration-arbitration/NOOPLEX_FABRIC.md`
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md`
- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`

### 3. Hypergraph autoencoding as bounded representation learning

An HC-internal autoencoder or related representation learner could be useful for:

- latent compression of high-dimensional graph/hypergraph state;
- denoising;
- topology-aware feature learning;
- anomaly detection;
- learned embeddings for retrieval or downstream inference;
- comparing predicted and observed network configurations.

Any such embedding remains a derived representation rather than semantic truth, memory currentness, identity authority, consent, or effect authority.

`LATENT_EMBEDDING != BELIEF`

`RECONSTRUCTION_SUCCESS != TRUTH`

`CLASSIFICATION_CONFIDENCE != ACTION_AUTHORITY`

### 4. Network-neuroscience GNN methods as a research map

The GNN survey's categories map to several HC research questions:

- graph/network synthesis -> counterfactual or predicted topology candidates;
- graph evolution over time -> temporal topology prediction and plasticity evaluation;
- multi-network integration/fusion -> multimodal/heterogeneous evidence integration;
- graph super-resolution -> resolution-changing representations without pretending inferred detail was measured;
- graph embedding -> bounded latent representations;
- biomarker/classification work -> candidate feature-discovery methods, not organism self-definition.

Each method must retain HC's existing epistemic firewall:

`PREDICTED_GRAPH != OBSERVED_GRAPH`

`SUPER_RESOLVED_GRAPH != MEASURED_HIGH_RESOLUTION_GRAPH`

`CLASSIFIER_LABEL != IDENTITY_TRUTH`

`MODEL_IMPORTANCE != CAUSAL_MECHANISM`

## Important mismatch with HC architecture

HCAE's "hyperconnectome" is a data-analysis representation of brain-network measurements. HC's Hyperconnectome Brain is a complete cognitive-organ architecture whose runtime topology is a typed, attributed, multilayer temporal hypergraph.

The shared word **hyperconnectome** is useful but must not collapse the distinction.

HCAE does not model HC requirements such as:

- dynamic coalition lifetime and dissolution;
- authority/consent/effect governance;
- current/deep memory ownership and continuity;
- body-interface ownership;
- self-contained cognition;
- protected update governance;
- failure/degradation lineage;
- epistemic currentness/correction;
- affect/homeostasis/conation;
- distributed physical organ membership;
- organism identity continuity.

Therefore HCAE is **research input for mechanisms**, not a candidate replacement architecture.

## Research directions worth testing

1. Compare HC's current hyperedge/coalition model with incidence-matrix and message-passing representations to determine what information is lost when a rich typed temporal hyperedge is projected into a numerical propagation matrix.
2. Prototype a provenance-preserving multi-view hypergraph operator where each view remains typed and uncertainty-bearing rather than being flattened into anonymous concatenated incidence columns.
3. Test whether learned hypergraph embeddings can improve retrieval, anomaly detection, or coalition proposal while being prevented from directly mutating semantic truth, identity, authority, or durable memory.
4. Use network-evolution literature from the GNN survey to design falsifiable plasticity/topology-prediction tests, with explicit separation between predicted future topology and committed plastic change.
5. Examine newer hypergraph-neural-network and temporal-hypergraph literature before selecting implementation primitives; these repositories are historically useful but not current-state-of-the-art evidence by themselves.

## Current disposition

**KEEP as research/provenance source.**

No architecture replacement is adopted from either repository. No source code is copied. The immediate value is a concrete implementation family for hypergraph incidence/message propagation plus a curated network-neuroscience research map.

Any future canonical transfer requires a focused architecture proposal, evidence classification, implementation-readiness review by Four, hostile review by Vera for semantic/authority leakage, and Warden disposition.
