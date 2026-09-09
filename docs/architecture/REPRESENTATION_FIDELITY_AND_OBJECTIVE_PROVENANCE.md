# Representation Fidelity and Objective Provenance

Status: canonical architecture contract.

## Purpose

HC representations may be fused, normalized, compressed, generated, aligned, forecast, or learned under objectives that reward only selected properties of the source state.

A component may accurately preserve one structural statistic while distorting another, or preserve task-discriminative information while discarding information needed by another cognitive process.

Therefore:

> **Representation fidelity is a scoped vector of tested properties, not an unqualified scalar claim.**

## Core separations

`MATCHED_TOPOLOGY_METRIC != MATCHED_TOPOLOGY`

`TOPOLOGY_REGULARIZED != TOPOLOGY_VERIFIED`

`ONE_METRIC_PASS != REPRESENTATION_FIDELITY_PASS`

`CENTERED_TEMPLATE != INSTANCE_STATE`

`REPRESENTATIVE != COMPLETE`

`DISCRIMINATIVE != REPRESENTATIVE`

`TASK_PERFORMANCE != INFORMATION_PRESERVATION`

`CLASSIFICATION_OPTIMIZED_INTEGRATION != GENERAL_PURPOSE_FUSION`

`SUPERVISED_TOPOLOGY_WEIGHT != INTRINSIC_TOPOLOGICAL_IMPORTANCE`

`DISCRIMINATIVE_FEATURE != CAUSAL_MECHANISM`

## Fidelity vector

A consequential transformation should declare which fidelity dimensions were actually tested. Candidate dimensions include:

- element/edge-value reconstruction;
- local graph metrics;
- global graph metrics;
- higher-order hyperedge membership and attributes;
- temporal order, duration, latency, and synchronization;
- node/entity correspondence;
- modality/view identity;
- provenance lineage;
- source disagreement/dissent;
- uncertainty/calibration;
- protected-state retention;
- reversibility or round-trip reconstruction;
- task-general information retention;
- perturbation/reproducibility stability.

A component does not need to test every dimension for every use. It must not claim a broader fidelity scope than the dimensions and operating envelope actually tested.

A useful representation is:

```text
FIDELITY_REPORT {
  representation_id
  source_representation_ids[]
  transform_id
  tested_dimensions[]
  metric_or_test_per_dimension
  topology_plane_or_state_family
  time_or_snapshot_scope
  resolution
  weighting_direction_sign_conventions
  tolerance_or_acceptance_rule
  observed_result
  known_untested_dimensions[]
  perturbation_scope
  qualification_ref
  provenance
}
```

## Training-objective provenance

The objective that shaped a learned representation is part of its provenance.

Material objectives include, for example:

- reconstruction error;
- centeredness;
- classification or regression performance;
- discriminativeness;
- adversarial distribution matching;
- graph metric preservation;
- sparsity or compression;
- temporal smoothness;
- contrastive agreement;
- task-specific reward.

Downstream systems should be able to determine what a transform was optimized to preserve and what it had no incentive to preserve.

`OPTIMIZED_FOR_X != NEUTRAL_WITH_RESPECT_TO_Y`

A representation trained for one task may still be useful elsewhere, but transfer requires evidence rather than an assumption of neutrality.

## Metric semantics

A topology metric is a projection of structure under declared conventions. Closeness, betweenness, eigenvector centrality, modularity, efficiency, participation, density, centeredness, distance measures, and related quantities do not describe the same property.

Accordingly, labels such as `topology-aware`, `topology-preserving`, or `topologically sound` are insufficient implementation evidence by themselves.

A fidelity claim should identify:

- the metric family;
- topology plane;
- graph/hypergraph projection used;
- directed/undirected convention;
- weighted/unweighted convention;
- sign handling;
- time interval/snapshot;
- node/edge inclusion rules;
- null/reference model where relevant;
- threshold/tolerance.

## Representative summaries and dissent

Population templates, averaged states, selected representative features, and fused views may be efficient references. They are lossy whenever source variation is not fully recoverable.

HC should preserve a distinction between:

- `REPRESENTATIVE_SUMMARY`;
- `SOURCE_SET_WITH_DISSENT`;
- `EXCEPTION_OR_OUTLIER_EVIDENCE`.

Rare evidence must not be discarded solely because it reduces centeredness, reproducibility, or majority agreement. Novel, safety-critical, authority-bearing, continuity-bearing, fault-related, or otherwise high-consequence evidence may justify retention even when statistically unrepresentative.

`MINORITY_EVIDENCE != ERROR`

`OUTLIER != DISCARDABLE`

## Task-coupled fusion

If integration and downstream prediction are trained end-to-end under one objective, the resulting integrated representation is task-coupled unless separately qualified as task-general.

Task coupling should be explicit in representation metadata and transfer decisions.

A task-coupled fusion output cannot automatically replace source-native evidence for semantic adjudication, memory admission, identity continuity, action authorization, or unrelated reasoning.

## Feature importance and biomarkers

Feature-selection, attribution, reproducibility, and group-discrimination methods may identify useful predictive structure.

They do not by themselves establish:

- causality;
- mechanism;
- semantic truth;
- authority;
- identity;
- durable preference;
- protected architecture importance.

Reproducibility strengthens the claim that a signal is stable under the tested perturbations. It does not transform association into causation.

## Implementation verification

Architecture names and comments do not establish runtime behavior.

If a component claims properties such as cluster-specific learning, source-specific routing, protected retention, or modality-specific processing, qualification should trace the actual data/state path and verify that the intended partition or routing occurs at runtime.

`NAMED_BEHAVIOR != VERIFIED_EXECUTION`

Instrumentation, controlled fixtures, negative controls, and state/index tracing are preferred over assuming that loop labels, class names, or diagrams match executed behavior.

## Failure modes

- one centrality metric is reported as preservation of topology generally;
- reconstruction accuracy hides loss of provenance or higher-order relations;
- classifier-optimized fusion is reused as a neutral world representation;
- centered template suppresses rare but critical evidence;
- supervised structural weighting becomes a hidden salience/reward policy;
- stable discriminative feature becomes a claimed causal mechanism;
- high fidelity on a static graph masks timing-order failure;
- a named cluster/modality route processes the wrong partition at runtime;
- implementation test verifies output score without verifying intended state flow.

## Conformance questions

1. What exact properties were tested for fidelity?
2. Which properties remain untested?
3. What objective trained or selected the representation?
4. What source variation or dissent can no longer be recovered?
5. Is this representation task-general or task-coupled?
6. Which metric conventions define any structural-preservation claim?
7. Does any metric accidentally become salience, authority, or reward?
8. Can rare but consequential evidence survive summary/fusion?
9. Has claimed partition-specific or route-specific behavior been traced at runtime?
10. Are causal or semantic claims being inferred from discrimination, attribution, or reproducibility alone?

## Evidence provenance

This contract was motivated by source study of BASIRA Lab multigraph integration/generation methods and their evaluation implementations, including MultiGraphGAN, topoGAN, MGN-Net, MICNet, netNorm, SM-netFusion, NAGFS, ReMI-Net, and the comparative multigraph-integration survey.

The computational methods provide examples of scoped optimization and validation patterns. They do not prove HC's complete synthetic-organ design or elevate any graph metric into a cognitive primitive.

See `docs/research/BASIRA_MULTIGRAPH_TOPOLOGY_FIDELITY_2026-09-09.md` for source-specific observations and transfer limits.