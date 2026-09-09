# Multigraph, Multilayer, and Hyperedge Semantics

Status: canonical architecture clarification.

## Purpose

The HC is a typed, attributed, multilayer temporal hypergraph. That statement contains several relation structures that must not be collapsed into one another.

Multiview/multimodal graph research repeatedly uses terms such as multigraph, multiplex, layer, inter-layer relation, graph fusion, and hyperconnectome. These terms are useful only if their semantics remain explicit inside HC.

The governing rule is:

> **Multiple pairwise relations are not automatically one higher-order relation, and a higher-order relation is not merely a stack of pairwise views.**

## Core separations

`MULTIPLE_EDGE_TYPES != HYPEREDGE`

`MULTIVIEW_GRAPH != HYPERGRAPH`

`MULTIPLEX_LAYER != COGNITIVE_PLANE`

`INTER_LAYER_MAPPING != NODE_IDENTITY`

`FUSED_EDGE != ORIGINAL_LAYER_SET`

`PAIRWISE_AGGREGATION != HIGHER_ORDER_CAUSAL_RELATION`

`HYPEREDGE != CLIQUE_EXPANSION`

## Pairwise multigraph semantics

HC may have multiple typed pairwise relations between the same participants.

For example, systems A and B may simultaneously have distinct pairwise relations for:

- physical substrate reachability;
- learned logical eligibility;
- configured message routing;
- modulatory influence;
- inhibition;
- provenance/dependency;
- authority scope;
- predicted interaction;
- measured statistical association.

These are not duplicate edges merely because the endpoint pair is the same.

A pairwise relation should retain enough attributes to identify its relation type, topology plane, provenance, temporal validity, directionality, weight/confidence, and governing semantics.

## Multiview and multiplex representations

A multiview or multiplex representation uses multiple relation layers or views over related participants.

Examples include different sensor modalities, feature families, relation types, resolutions, evidence origins, or processing contexts.

Layer identity must survive whenever it is decision-relevant.

`SAME_ENDPOINTS_ACROSS_LAYERS != SAME_RELATION`

A layer can be fused or projected for a particular purpose, but the fused result must preserve transformation lineage and must not retroactively replace the source layers.

## Cognitive planes are not ordinary data views

HC architectural planes such as physical, logical, configured, effective, modulatory, plastic, temporal, and governance state are semantically stronger than arbitrary data channels.

A model may encode them numerically as layers, but it must not treat them as interchangeable feature channels.

For example:

- high statistical association cannot substitute for physical reachability;
- configured routing cannot substitute for action authority;
- salience cannot substitute for epistemic support;
- a predicted relation cannot substitute for current effective topology.

`NUMERIC_LAYER_COMPATIBILITY != SEMANTIC_INTERCHANGEABILITY`

## Hyperedge semantics

A hyperedge represents one relation over a participant set where joint membership is itself material.

A hyperedge is appropriate when the function, constraint, event, or causal relation cannot be faithfully represented as independent pairwise relations without losing meaning.

Example:

```text
H = {A, B, C}
```

may encode that capability X exists only when A, B, and C jointly participate within a bounded temporal/contextual relation.

It is not equivalent to simply asserting:

```text
A-B
A-C
B-C
```

because clique expansion loses the identity and attributes of the joint relation.

## Two-member hyperedges

The formal hypergraph can support a two-member hyperedge when a uniform relation representation is useful, but implementations should prefer an ordinary typed edge when the semantics are genuinely pairwise.

The distinction is semantic, not just cardinality.

A two-member hyperedge may be justified when it belongs to a relation family whose lifecycle, role map, shared state, or governance is defined uniformly for higher-order relations.

## Inter-layer relations

Relations between layers may represent:

- correspondence;
- translation/alignment;
- dependency;
- modulation;
- coupling;
- shared source lineage;
- prediction from one layer into another;
- constraints between views.

An inter-layer relation does not prove the linked elements are the same entity.

When node sets are non-isomorphic, inter-layer correspondence must preserve the mapping semantics defined by `REPRESENTATION_ALIGNMENT_AND_RESOLUTION.md`.

## Fusion

Fusion creates a derived representation. It does not erase the semantics of the contributing relation set.

A fusion operator should declare whether it performs:

- selection;
- averaging;
- weighted aggregation;
- nonlinear projection;
- learned integration;
- template normalization;
- cross-diffusion;
- latent embedding;
- graph generation;
- relation collapse.

If several relation types are compressed to one edge weight, the result is a projection whose loss profile must be explicit.

`FUSED_EDGE_WEIGHT != COMPLETE_RELATION_HISTORY`

## Hypergraph projection

Numerical implementations may project hypergraphs into incidence matrices, clique expansions, star expansions, propagation matrices, embeddings, or ordinary graphs for bounded computation.

Those projections are implementation representations of the hypergraph, not permission to discard the original higher-order semantics.

A projection should preserve or separately retain:

- hyperedge identity;
- membership;
- member roles;
- temporal validity;
- relation type;
- topology plane;
- provenance;
- authority/policy references where material;
- uncertainty;
- projection lineage.

`PROJECTED_GRAPH != ORIGINAL_HYPERGRAPH`

## Temporal multilayer semantics

Layer membership, edge state, and hyperedge membership may all vary over time.

The effective HC state therefore cannot be reconstructed from an unlabeled stack of static adjacency matrices unless that stack also preserves the timing, layer semantics, higher-order relation identity, and transformation history required by the event.

`STATIC_MULTILAYER_SNAPSHOT != TEMPORAL_HYPERGRAPH_HISTORY`

## Failure modes

- treating four modality-specific pairwise edges as one higher-order cognitive relation;
- converting a hyperedge to a clique and later forgetting the shared relation existed;
- treating governance and statistical-association layers as interchangeable model channels;
- fusing multiple relation types to one scalar and losing source-layer dissent;
- treating cross-layer alignment as proof of node identity;
- using an inter-layer predicted edge as current physical/effective topology;
- calling a stack of ordinary adjacency matrices a complete HC hypergraph representation;
- losing temporal validity when projecting layered/higher-order state to a static graph.

## Conformance questions

1. Is the relation genuinely pairwise or jointly higher-order?
2. If multiple relations share endpoints, are their types and planes preserved?
3. Are layer identities semantically meaningful or merely implementation channels?
4. Does any inter-layer mapping imply identity that was never established?
5. Does fusion retain its source-layer lineage and loss profile?
6. If a hypergraph is projected to an ordinary graph/matrix, can the original hyperedge identity and material attributes still be recovered?
7. Are temporal changes in layer/edge/hyperedge state preserved?
8. Has a numerical representation silently weakened HC's epistemic, authority, or topology-plane boundaries?

## Evidence provenance

This clarification was informed by source study of multiview, multigraph, multiplex, hypergraph, alignment, and fusion methods in network-neuroscience codebases, including BASIRA Lab HCAE, HUNet, ABMT, MultiGraphGAN/topoGAN, MGN-Net, MICNet, netNorm, SM-netFusion, and related connectional-template work.

Those sources demonstrate computational uses of multilayer, multigraph, and hypergraph representations. HC's semantics are architecture-specific and must not be inferred wholesale from any one external method.