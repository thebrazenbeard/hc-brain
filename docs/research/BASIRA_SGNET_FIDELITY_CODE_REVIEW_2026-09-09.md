# BASIRA SG-Net Fidelity Code Review — 2026-09-09

Status: RESEARCH / SOURCE PROVENANCE / NON-CANONICAL FINDINGS

## Source

- `basiralab/SG-Net`
- repository tree: `ba5e9ed162317e7875cbc827cde645aa88502b15`
- `README.md` blob `445792f3c2f5207c1373c042ced5e5bb1ecd2376`
- `losses.py` blob `13f2212b9d36b545b98d44bd9694c2c334595cf8`

## DOCUMENTED source claim

SG-Net is presented as a multi-resolution graph alignment and synthesis framework spanning inter- and intra-modality graph generation. The README describes a Ground Truth-Preserving loss intended to improve preservation of target brain-graph topology.

## OBSERVED code behavior

`losses.py::GT_loss(target, predicted)` combines three terms:

1. L1 reconstruction loss over the target and predicted tensors;
2. a Pearson-correlation term expressed as `1 - pc_loss`;
3. L1 distance between eigenvector-centrality outputs computed for target and prediction.

The function returns:

```text
G_loss = L1(target, predicted)
       + (1 - Pearson(target, predicted))
       + L1(EigenCentrality(predicted), EigenCentrality(target))
```

The separate `Alignment_loss` computes a scaled KL-divergence expression over softmax-transformed target/predicted values.

## INFERRED HC lesson

This is a concrete example of why an implementation or paper label such as `topology-preserving` must be scoped to the actual objective and metrics.

Matching element values, global correlation, and eigenvector centrality can constrain important aspects of a graph while leaving other structure untested, including:

- exact edge-set identity;
- local motifs;
- shortest-path structure;
- modularity/community structure;
- directed or signed semantics if absent from the representation;
- higher-order hyperedge membership;
- temporal ordering/dynamics;
- multilayer/view identity;
- provenance and source disagreement.

Useful HC separations:

`EIGENVECTOR_CENTRALITY_MATCH != TOPOLOGY_EQUIVALENCE`

`COMBINED_FIDELITY_OBJECTIVE != COMPLETE_REPRESENTATION_PRESERVATION`

`TOPOLOGY_PRESERVING_LABEL != UNBOUNDED_TOPOLOGY_PROOF`

`DISTRIBUTION_ALIGNMENT_LOSS != SEMANTIC_EQUIVALENCE`

## Transfer disposition

No SG-Net model/code is promoted as HC machinery in this review.

The source strengthens existing canonical requirements in:

- `docs/architecture/REPRESENTATION_FIDELITY_AND_OBJECTIVE_PROVENANCE.md`
- `docs/architecture/REPRESENTATION_ALIGNMENT_AND_RESOLUTION.md`
- `specs/HC_REPRESENTATION_ALIGNMENT_V1.yaml`

The main transfer is an adversarial qualification fixture: whenever an HC component claims to preserve topology, qualification should enumerate the exact structural dimensions and metrics actually tested rather than accept the label.

## Qualification fixture

Given a transform that passes L1 reconstruction, correlation, and eigenvector-centrality thresholds, construct counterexamples that materially change one or more untested dimensions while retaining similar scores.

Expected result: the component may pass its declared metric-scoped fidelity claim but must not receive an unqualified `TOPOLOGY_PRESERVED` label.

## Evidence boundary

This static code review establishes what the inspected `GT_loss` function computes. It does not establish the complete training dynamics, paper-result validity, biological meaning of the generated graphs, or suitability of SG-Net as an HC implementation.
