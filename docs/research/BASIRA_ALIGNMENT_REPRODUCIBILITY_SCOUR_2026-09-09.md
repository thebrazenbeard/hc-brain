# BASIRA Alignment, Resolution, and Reproducibility Deep Scour — 2026-09-09

Status: research/provenance only. This file records source-supported computational patterns and HC transfer limits; it is not proof of HC biology or implementation feasibility.

## Scope

This continuation studies BASIRA Lab repositories that were not exhausted in the earlier hyperconnectome/network-neuroscience intake, with emphasis on heterogeneous graph alignment, non-isomorphic resolution changes, hypergraph pooling, multiplex inference, federated aggregation, adaptation under domain shift, and reproducibility.

Sources inspected:

- `basiralab/HUNet`
- `basiralab/UMC`
- `basiralab/IMANGraphNet`
- `basiralab/HADA`
- `basiralab/AGSR-Net`
- `basiralab/L2S-KDnet`
- `basiralab/MultigraphGNet`
- `basiralab/ABMT`
- `basiralab/Fed-CBT`
- `basiralab/Meta-RegGNN`
- `basiralab/RG-Select`
- `basiralab/multimodalConnectomeGeneration` (provenance caveat below)

## Source-supported observations

### HUNet — higher-order pooling and restoration

DOCUMENTED from the repository README: HUNet is a hypergraph U-Net that constructs a normalized hypergraph over samples and stacks hypergraph convolution with hypergraph pooling/unpooling. Removed-node information from pooling is passed to corresponding unpooling stages so the representation can be restored for downstream embedding/classification.

HC relevance: higher-order structure can be compressed hierarchically rather than flattened to pairwise edges. The transfer lesson is not to adopt HUNet's population graph as HC topology, but to test hypergraph-native pooling/unpooling mechanisms for resource-bounded internal representations.

Critical boundary:

`POOLED_REPRESENTATION != ORIGINAL_HYPERGRAPH_STATE`

`UNPOOLED_RECONSTRUCTION != LOSSLESS_RESTORATION_UNLESS_VERIFIED`

### UMC — variable-size multimodal graph alignment

DOCUMENTED from the README: UMC aligns unpaired multimodal brain graphs of different sizes and distributions to a common fixed-size template graph, using node representations and correspondence matrices before classification.

HC relevance: modality- or embodiment-specific graphs may need comparison in a common reference frame without pretending their node sets or semantics are identical.

Critical boundary:

`COMMON_REFERENCE_FRAME != COMMON_ONTOLOGY`

`ALIGNED_GRAPH != ORIGINAL_GRAPH`

### IMANGraphNet / HADA — domain alignment is a learned transform

DOCUMENTED from the READMEs: IMANGraphNet predicts non-isomorphic target graphs across modalities while explicitly addressing changes in node count, topology, and distribution; HADA uses hierarchical adversarial domain alignment before target-graph prediction.

HC relevance: source and target representations can be mapped across materially different domains, but distributional alignment is evidence about transform usefulness, not evidence that the domains are semantically identical or that generated topology was observed.

`DISTRIBUTION_ALIGNMENT != SEMANTIC_EQUIVALENCE`

`NON_ISOMORPHIC_MAPPING != NODE_IDENTITY`

### AGSR-Net / L2S-KDnet — generated high-resolution detail

DOCUMENTED from the READMEs: AGSR-Net predicts a higher-resolution graph with additional nodes from a lower-resolution graph and uses adversarial regularization to align predicted and ground-truth high-resolution distributions. L2S-KDnet combines inter-domain alignment with teacher-student knowledge distillation to predict higher-resolution graphs.

HC relevance: inferred finer-resolution structure must preserve generation lineage and uncertainty. Teacher/student agreement or discriminator success cannot promote generated detail to measurement.

`DISTILLED_KNOWLEDGE != OBSERVATION`

`DISCRIMINATOR_CONFUSION != GROUND_TRUTH`

### MultigraphGNet — template compression plus one-to-many reconstruction

DOCUMENTED from the README: MultigraphGNet combines a many-to-one graph network that estimates a connectional brain template with a reverse one-to-many network that reconstructs multigraph populations, trained using a cyclic loss.

HC relevance: cycle-consistent compression/reconstruction is a useful candidate test for whether a compact representation retains information needed to reconstruct multiple views.

Critical boundary:

`CYCLE_CONSISTENCY != SEMANTIC_CORRECTNESS`

A transform can reconstruct its own training-domain conventions while still erasing provenance, authority, timing, or ontology distinctions important to HC.

### ABMT — inferred multiplex and inter-layer relations

DOCUMENTED from the README: ABMT predicts a target multiplex intra-layer and an inter-layer representing higher-order relationships between source and target layers from one source intra-layer.

HC relevance: inferred cross-layer/multiplex relations are a candidate mechanism for proposing higher-order relation structure across representations.

Critical boundary:

`INFERRED_INTER_LAYER != MEASURED_RELATION`

### Fed-CBT — decentralized aggregation

DOCUMENTED from the README: Fed-CBT trains local models on distributed datasets, sends learned model weights to an aggregation server, and estimates a global connectional brain template without centralizing the underlying datasets.

HC relevance: distributed constituents may exchange bounded learned summaries without moving all raw evidence. Aggregation, however, cannot erase source heterogeneity or become a truth vote.

`AGGREGATED_MODEL != CONSENSUS_TRUTH`

`MODEL_WEIGHT_SHARE != RAW_EVIDENCE`

### Meta-RegGNN — rapid adaptation under domain shift

DOCUMENTED from the README: Meta-RegGNN explicitly trains a regression GNN through meta-learning so a small number of gradient steps on little data can generalize to previously unseen connectomes, with domain-shift motivation.

HC relevance: rapid adaptation after embodiment/domain change is a plausible implementation strategy for calibration and bounded model adaptation.

Critical boundary:

`FAST_ADAPTATION != AUTOMATIC_REQUALIFICATION`

Any durable HC adaptation remains governed plasticity and must preserve protected invariants, evidence lineage, and consequence-appropriate validation.

### RG-Select — reproducibility as a first-class model property

DOCUMENTED from the README: RG-Select evaluates GNN reproducibility by comparing discriminative features/learned weights across different models, training strategies, data perturbations, views, and selected-feature counts.

HC relevance: reproducibility across seeds, perturbations, training paths, embodiments, or evidence cuts should become a qualification dimension for learned topology, route importance, explanations, biomarkers, and adaptation—not merely predictive accuracy.

`HIGH_ACCURACY != REPRODUCIBLE_MECHANISM`

`REPRODUCIBLE_FEATURE != CAUSAL_FEATURE`

### multimodalConnectomeGeneration provenance caveat

OBSERVED: the BASIRA-owned repository's documentation identifies itself as `micapipe` and attributes core development to MICA Lab / Montreal Neurological Institute. It describes a multimodal MRI processing pipeline producing microstructural, functional, structural, and spatial connectomes across multiple parcellations.

Disposition: useful as a pipeline/provenance example, but do not attribute micapipe's scientific or software authorship to BASIRA merely because a copy/fork is present under the BASIRA account. Any future transfer should cite the original MICA-LAB source lineage.

## Cross-source HC lessons

### 1. Alignment needs an explicit transform object

HC should never store only the aligned result. A material alignment should retain at least:

- source representation identity and resolution;
- target/reference identity and resolution;
- source and target ontology/correspondence assumptions;
- transform/model and version;
- parameters/configuration digest;
- source and target domains/modalities;
- learned correspondence or mapping;
- known non-isomorphic changes;
- generated/imputed nodes or relations;
- uncertainty and domain-applicability state;
- reconstruction/round-trip evidence when available;
- provenance and time validity.

### 2. Resolution change is epistemic change

Upsampling, super-resolution, template projection, pooling, contraction, or unpooling changes what is directly supported by evidence.

The architecture should distinguish:

`OBSERVED_AT_SOURCE_RESOLUTION`

`MAPPED_TO_REFERENCE_RESOLUTION`

`GENERATED_AT_FINER_RESOLUTION`

`COMPRESSED_TO_COARSER_RESOLUTION`

`RESTORED_FROM_COMPRESSED_STATE`

### 3. Non-isomorphic mapping requires correspondence uncertainty

When node sets differ, correspondence is not a free identity relation. HC should carry explicit mapping confidence and allow one-to-one, one-to-many, many-to-one, unmatched, and generated correspondences.

### 4. Reproducibility belongs in qualification

For learned topology or learned representation transforms, qualification should test whether material conclusions survive reasonable perturbations such as seed changes, evidence resampling, sensor/view dropout, modest domain changes, model initialization changes, and equivalent preprocessing choices.

A result that appears only in one brittle training run should remain lower-confidence or experimental even if its held-out score is high.

### 5. Compression may not discard protected semantics

Pooling, graph contraction, template compression, or low-dimensional embedding can be resource-efficient while still being unsafe if they drop the only representation of revocation, provenance, chronology, lineage, fault, or protected-state information.

Any HC compression scheme needs protected-retention rules and a declared loss profile.

### 6. Federated or ensemble aggregation is evidence fusion, not authority fusion

A distributed average of weights or predictions does not create semantic truth, consent, identity, or effect authority. Source-local disagreement, version, calibration, and applicability must remain recoverable when decision-relevant.

## Recommended canonical transfers

1. Add an explicit HC representation-alignment/resolution contract defining transform lineage, correspondence uncertainty, lossy/lossless claims, generated detail, and round-trip tests.
2. Add reproducibility/perturbation stability as a qualification dimension for learned topology and model-mediated architecture claims.
3. Add negative tests preventing aligned/generated/reconstructed topology from silently becoming physical/effective/committed topology.
4. Require protected-retention analysis before graph pooling/contraction can be used in degraded or resource-bounded modes.
5. Treat rapid meta-adaptation as governed plasticity that does not by itself restore qualification.

## Current disposition

KEEP as research/provenance source set. The computational mechanisms are useful; none of these repositories is a replacement architecture for HC, and no source code is copied into HC.