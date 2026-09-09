# BASIRA CGTS-GAN Cycle and Topology-Objective Scope — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/CGTS-GAN@master/README.md`
- `basiralab/CGTS-GAN@master/model.py`

## DOCUMENTED source framing

CGTS-GAN is described as a bidirectional cyclic graph-translation system with a topology-strength constraint intended to improve brain-connectome synthesis while preserving ROI topological strength.

## OBSERVED implementation objective

The inspected `graph2graph.build_model` constructs forward and reverse generators plus cycle paths. The generator objectives combine:

- adversarial discriminator loss;
- L1 reconstruction against the paired target/source graph;
- terms comparing `degre_tf(...)` between real and generated graphs, including cycle outputs.

The topology-guidance visible in the inspected objective is therefore scoped to the degree/strength-like statistic produced by `degre_tf`, not to every possible graph/topology property.

The cycle paths explicitly generate `A -> fake_B -> fake_A_` and `B -> fake_A -> fake_B_`.

## HC transfer interpretation

`DEGREE_OR_STRENGTH_MATCH != TOPOLOGY_EQUIVALENCE`

`CYCLE_CONSISTENCY != SEMANTIC_EQUIVALENCE`

`A_TO_B_TO_A_RECONSTRUCTION != INVERTIBLE_CAUSAL_MAPPING`

`BIDIRECTIONAL_GENERATION != TWO_INDEPENDENT_EVIDENCE_SOURCES`

`TOPOLOGY_GUIDED_OBJECTIVE != COMPLETE_TOPOLOGY_PRESERVATION`

Cycle consistency can constrain information loss and improve reversible-looking translation while still permitting mappings that preserve the optimization objective without preserving all source semantics, provenance, higher-order relations, or causal structure.

## HC disposition

No new canonical subsystem is required. Existing HC contracts already cover the transfer boundary:

- `docs/architecture/REPRESENTATION_FIDELITY_AND_OBJECTIVE_PROVENANCE.md`
- `docs/architecture/REPRESENTATION_ALIGNMENT_AND_RESOLUTION.md`
- `specs/HC_REPRESENTATION_ALIGNMENT_V1.yaml`

This source strengthens the requirement that any claim such as `topology-preserving`, `cycle-consistent`, or `bidirectional` identify the actual metric/objective and not exceed its tested semantic scope.

## Scope and caution

This record describes the objective visible in the inspected source revision. It does not claim the associated method is defective; degree/strength constraints and cycle losses are useful optimization tools when their scope is reported accurately.
