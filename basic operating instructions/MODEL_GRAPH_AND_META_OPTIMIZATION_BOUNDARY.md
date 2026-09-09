# Model-Graph and Meta-Optimization Boundary

Status: canonical operating contract.

## Purpose

HC implementations may contain heterogeneous learned models, adapters, predictors, routing functions, perception modules, control policies, and other computational components whose internal parameters can themselves be represented as graph-structured state.

HC may also use learned optimizers or cross-component coordination mechanisms to propose changes to those components.

This contract allows those mechanisms without creating a hidden central executive, universal self-modification authority, or semantic confusion between implementation topology and cognitive topology.

The governing rule is:

> **The ability to represent, compare, predict, or optimize a component does not grant authority to redefine the cognitive organ.**

## Core separations

`MODEL_GRAPH != COGNITIVE_TEMPORAL_HYPERGRAPH`

`MODEL_PARAMETER_EDGE != COGNITIVE_RELATION_EDGE`

`META_OPTIMIZER_REACHABILITY != UPDATE_AUTHORITY`

`PROPOSED_PARAMETER_UPDATE != AUTHORIZED_UPDATE`

`LOW_LOSS_UPDATE != SEMANTICALLY_SAFE_UPDATE`

`PARAMETER_SIMILARITY != SEMANTIC_SIMILARITY`

`PARAMETER_SIMILARITY != FUNCTIONAL_EQUIVALENCE`

`SAME_CLUSTER != SAME_AUTHORITY_SCOPE`

`SYNCHRONIZATION_FREQUENCY != AUTHORITY`

`META_LEARNING != PROTECTED_SELF_MODIFICATION_AUTHORITY`

## Model-graph representation

A model graph is an implementation-level representation of a bounded computational component.

Depending on implementation, it may encode:

- parameterized connections;
- weights;
- biases;
- layer/module structure;
- kernel/group identity;
- parameter-sharing relationships;
- input/output interfaces;
- dependency relationships;
- resource and latency metadata;
- version and qualification state.

A model graph can be useful for introspection, migration planning, compatibility analysis, optimization, fault localization, and controlled knowledge transfer.

It must remain namespaced from HC cognitive topology.

A cognitive node, edge, hyperedge, coalition, topology plane, authority relation, memory relation, or semantic relation cannot be inferred solely from similarity to implementation graph structure.

## Meta-optimization proposal path

A learned optimizer may generate candidate updates.

The ordinary path is:

```text
MODEL_OR_COMPONENT_STATE
-> MODEL_GRAPH_OR_OTHER_IMPLEMENTATION_REPRESENTATION
-> ANALYSIS_OR_META_OPTIMIZER
-> UPDATE_CANDIDATE
-> CHANGE_CLASSIFICATION
-> AUTHORITY_AND_GOVERNANCE_CHECK
-> STAGING_OR_SHADOW_TEST
-> ACTIVATION_TRANSACTION_IF_AUTHORIZED
-> POST_ACTIVATION_QUALIFICATION
```

The optimizer does not skip change classification or update governance.

If the proposal affects protected state, `PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md` controls.

If the proposal is ordinary plasticity, `PLASTICITY_AND_STATE_GOVERNANCE.md` controls.

A component may be granted bounded autonomous update authority for a declared low-consequence state class, but that grant must be explicit, scoped, current, revocable where applicable, and unable to silently widen itself.

## Anti-homunculus requirement

A shared meta-optimizer may coordinate many components without becoming the organism's executive person.

A conforming design must avoid a permanent architecture in which one learned optimizer becomes the sole source of:

- semantic truth;
- attention priority;
- values;
- consent;
- memory currentness;
- identity continuity;
- effect authority;
- protected-update authority;
- all cognitive routing decisions.

The optimizer may participate in bounded temporal coalitions and produce proposals/evidence like other HC systems.

`GLOBAL_PARAMETER_ACCESS != GLOBAL_COGNITIVE_AUTHORITY`

## Similarity and clustering

Models or components may be clustered by parameter distance, behavior, topology, task, latency, failure signature, or other declared features.

Cluster membership is a derived coordination aid.

It may inform:

- evaluation scheduling;
- candidate parameter sharing;
- communication frequency;
- migration planning;
- redundancy analysis;
- fault comparison;
- transfer-learning proposals.

It does not establish semantic equivalence, identity, authority scope, interchangeable qualification, or independent corroboration.

The similarity metric and feature space are part of provenance.

## Parameter sharing and synchronization

Cross-component parameter sharing must preserve component identity, version lineage, qualification scope, and protected-state boundaries.

A frequently synchronized cluster cannot silently become one indivisible authority domain.

A component receiving shared state must still satisfy its own compatibility and qualification requirements where material.

`SHARED_PARAMETER != SHARED_AUTHORITY`

`SHARED_OPTIMIZER != SHARED_IDENTITY`

`TRANSFERRED_WEIGHT != TRANSFERRED_QUALIFICATION`

## Objective provenance

A meta-optimizer's objective is part of update provenance.

Examples include:

- predictive loss;
- resource reduction;
- latency;
- robustness;
- reconstruction;
- cross-component average performance;
- fairness metric;
- topology metric;
- communication cost.

Optimizing such an objective cannot silently redefine the HC's values, authority, semantic truth, or protected invariants.

`OPTIMIZER_OBJECTIVE != ORGANISM_VALUE_FUNCTION`

A proposal that improves one metric while degrading another protected or high-consequence property must remain visible to arbitration and qualification.

## Coherent versioning

Per-component optimization can create version skew.

HC should preserve:

- component version/digest;
- optimizer/model version;
- source state/evidence cut;
- proposal lineage;
- target state class;
- compatibility envelope;
- qualification state;
- activation relation to other constituent versions.

Selecting the individually best checkpoint for each component does not prove that the combined set is a coherent whole-organ configuration.

`BEST_COMPONENT_CHECKPOINTS != QUALIFIED_SYSTEM_CONFIGURATION`

## Self-referential updates

An optimizer that can modify itself, its objective, its update permissions, its protected-state classifier, or its validation rules creates a self-referential governance boundary.

Such modifications must be classified by the state actually affected.

An optimizer cannot convert a protected change into ordinary plasticity merely by producing the change itself.

`SELF_PROPOSED_GOVERNANCE_CHANGE != ORDINARY_LEARNING`

## Failure modes

- implementation graph is mistaken for the HC cognitive hypergraph;
- model-parameter similarity is treated as semantic equivalence;
- one shared optimizer becomes an executive homunculus;
- low training loss is treated as protected-update authorization;
- parameter sharing transfers obsolete or incompatible authority state;
- per-component best checkpoints produce an incoherent whole-organ cut;
- optimizer objective becomes hidden organism-wide reward/value policy;
- dynamic synchronization frequency becomes de facto authority weight;
- self-modifying optimizer weakens its own governance as ordinary learning;
- learned update skips requalification because it was produced internally.

## Conformance questions

1. Is this graph a representation of implementation state or cognitive topology?
2. What exact state class can the optimizer modify autonomously?
3. What authority governs the proposed change?
4. Can the optimizer widen its own scope or modify update governance?
5. What objective shaped the update proposal?
6. Does parameter similarity imply anything beyond the declared feature space?
7. Are component versions and qualification states preserved through sharing/synchronization?
8. Could one shared optimizer become the permanent source of executive or semantic authority?
9. Is the combined post-update system coherent, not merely each component locally successful?
10. What requalification is required after the proposed change?

## Evidence provenance

This boundary was informed by model-graph and meta-learning research patterns studied in `basiralab/uGNN`, `basiralab/UnifiedFL`, and `basiralab/Meta-RegGNN`.

The external methods motivate implementation patterns only. HC update authority, protected-state semantics, identity continuity, and anti-homunculus requirements remain defined by HC's own architecture.

See `docs/research/BASIRA_MODEL_GRAPH_META_OPTIMIZATION_2026-09-09.md` for source-level observations and limits.