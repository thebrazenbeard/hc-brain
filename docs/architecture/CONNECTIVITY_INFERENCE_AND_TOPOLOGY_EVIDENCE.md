# Connectivity Inference and Topology Evidence

Status: canonical architecture contract.

## Purpose

The HC temporal hypergraph contains several different topology planes. This contract prevents measured signals, statistical connectivity, model-generated edges, population templates, embeddings, predictions, and committed HC topology from being collapsed into one undifferentiated graph.

The governing principle is:

> **A topology claim carries the semantics of how it was obtained. Derivation does not silently become observation, physical reachability, current effective topology, or committed plastic structure.**

This contract refines `TOPOLOGY_DESIGN_CONSTRAINTS.md`, `TEMPORAL_HYPERGRAPH_MODEL.md`, and the runtime separation among `E_p`, `E_l(t)`, `E_c(t)`, and `H_f(t)`.

## Core separations

`MEASURED_SIGNAL != INFERRED_CONNECTIVITY`

`STATISTICAL_CONNECTIVITY != PHYSICAL_REACHABILITY`

`INFERRED_CONNECTIVITY != LEARNED_LOGICAL_ELIGIBILITY`

`PREDICTED_TOPOLOGY != CURRENT_TOPOLOGY`

`RECONSTRUCTED_EDGE != OBSERVED_EDGE`

`SUPER_RESOLVED_GRAPH != OBSERVED_HIGH_RESOLUTION_GRAPH`

`POPULATION_TEMPLATE != INSTANCE_TOPOLOGY`

`ALIGNED_REFERENCE != ORIGINAL_STATE`

`LATENT_EMBEDDING != TOPOLOGY_AUTHORITY`

`GRAPH_METRIC != CONTROL_OBJECTIVE`

`CENTRALITY != EXECUTIVE_AUTHORITY`

`MODEL_SELECTION != EFFECT_AUTHORIZATION`

`INFLUENCE_SCORE != CAUSAL_TRUTH`

## Topology planes remain authoritative

The canonical runtime planes retain their meanings:

- `E_p` — physically available substrate reachability;
- `E_l(t)` — durable learned/logical structural eligibility;
- `E_c(t)` — configured routes, subscriptions, and bindings;
- `H_f(t)` — current transient functional hyperedges/coalitions.

A derived connectivity object does not become one of these planes merely because its values can be represented as an adjacency/incidence matrix.

For example:

- correlation from sensor time series is evidence about statistical dependence, not proof of a physical link;
- a learned reconstruction is a topology hypothesis, not an installed route;
- a forecast is a possible future state, not history;
- a population template is a reference/prior, not the individual's current HC state;
- a latent embedding is a derived representation, not the underlying topology itself.

## Topology evidence classes

A conforming implementation should classify topology-related evidence at least as finely as necessary to distinguish:

- `PHYSICAL_MEASUREMENT` — direct or instrument-mediated evidence about substrate reachability or constituent state;
- `SIGNAL_DERIVED_STATISTICAL_CONNECTIVITY` — covariance, correlation, partial correlation, precision, coherence, or another declared estimator over signals;
- `MODEL_INFERRED_CONNECTIVITY` — inferred relation produced by a model from available evidence;
- `RECONSTRUCTED_CONNECTIVITY` — denoised, completed, imputed, or reconstructed topology;
- `SUPER_RESOLVED_CONNECTIVITY` — predicted detail at a finer node/edge resolution than directly supplied;
- `PREDICTED_FUTURE_TOPOLOGY` — forecast topology for a future interval or event;
- `POPULATION_OR_REFERENCE_TEMPLATE` — representative/reference topology learned from a population or corpus;
- `ALIGNED_OR_NORMALIZED_REPRESENTATION` — topology transformed into another domain/reference frame;
- `LATENT_TOPOLOGY_EMBEDDING` — compressed learned representation of graph/hypergraph state;
- `CURRENT_EFFECTIVE_RELATION_EVIDENCE` — evidence that a pairwise relation or higher-order coalition is actually operative now;
- `PLASTICITY_COMMIT_EVIDENCE` — durable evidence that a governed topology modification was admitted and committed.

These are evidence-origin classes, not interchangeable truth levels.

## TopologyEvidence envelope

A material topology claim should be representable with an envelope such as:

```text
TOPOLOGY_EVIDENCE {
  evidence_id
  subject_or_instance
  origin_class
  claimed_target_plane
  relation_or_structure
  source_modality_or_domain
  source_ids[]
  source_resolution
  target_resolution_if_transformed
  estimator_or_model
  estimator_or_model_version
  parameters_or_configuration_digest
  reference_or_template_id
  transform_or_alignment_lineage[]
  event_time_or_interval
  observation_time
  record_time
  temporal_uncertainty
  epistemic_support
  domain_shift_or_applicability_state
  known_limitations[]
  provenance
  mutation_eligibility
  expiry_or_revalidation_rule
}
```

Not every field is mandatory for every claim, but the implementation must preserve enough information to prevent a derived representation from being mistaken for a stronger evidence class later.

## Estimator identity is part of meaning

Different connectivity estimators answer different questions. Covariance, correlation, partial correlation, precision, tangent/reference-space representation, model inference, and physical measurement must not share an unlabeled `connectivity` type.

Changing estimator, hyperparameters, preprocessing, reference population, node resolution, or alignment transform may materially change the result.

Therefore:

`SAME_INPUT + DIFFERENT_ESTIMATOR MAY PRODUCE DIFFERENT_TOPOLOGY_EVIDENCE`

Estimator disagreement should remain visible when decision-relevant rather than being silently averaged into apparent certainty.

## Population/reference templates

Population or corpus-derived templates may support:

- initialization priors;
- calibration references;
- anomaly detection;
- model selection;
- comparison across instances;
- sparse-data bootstrapping;
- domain alignment.

They must not directly overwrite:

- current instance topology;
- identity continuity;
- current memory;
- current body schema;
- current values/commitments;
- authority/consent;
- current functional coalition state.

`REPRESENTATIVE != AUTHORITATIVE`

A reference must retain its source population/corpus, version, estimator, scope, and applicability assumptions.

## Generative reconstruction and super-resolution

A generative or super-resolution model may propose nodes, edges, weights, hyperedges, or trajectories not directly present in its input.

Such outputs enter HC as hypotheses/derived evidence.

They may be used for:

- prediction;
- simulation;
- anomaly investigation;
- planning experiments;
- candidate route/plasticity proposals;
- representation at another resolution.

They may not by themselves mutate `E_p`, `E_l(t)`, `E_c(t)`, or durable memory.

A durable topology change requires the ordinary governing path for the target state class, including current evidence, plasticity eligibility, authority where applicable, and commit/verification semantics.

`GENERATED_EDGE != ADMITTED_EDGE`

## Temporal prediction

Predicted topology trajectories should retain:

- prediction origin;
- forecast horizon;
- baseline/evidence cut;
- model/version;
- uncertainty;
- alternate trajectories when material;
- observed outcomes once available.

The system must preserve:

`FORECAST != HISTORY`

`PREDICTED_FUTURE_TOPOLOGY != PLASTICITY_COMMIT`

Forecast error may update a model or its calibration through governed learning but does not rewrite the historical forecast into what later occurred.

## Multimodal and multidomain fusion

Multi-view/domain integration must preserve source identity and disagreement.

A useful path is:

`source-local evidence -> source-local relation hypothesis -> provenance-preserving alignment/fusion -> integrated hypothesis`

Fusion may improve inference without proving that all domains are semantically equivalent.

`DOMAIN_ALIGNMENT != SEMANTIC_EQUIVALENCE`

`FUSED_REPRESENTATION != UNANIMOUS_SOURCE_AGREEMENT`

If one modality is stale, degraded, out of distribution, or poorly calibrated, that state should remain available to downstream arbitration.

## Domain shift and predictive uncertainty

A predictor qualified under one operating distribution must not silently retain the same confidence when source modality, embodiment, population, environment, task, node resolution, or other material domain characteristics shift.

A conforming implementation should expose domain/applicability state and uncertainty appropriate to consequence.

`IN_DISTRIBUTION_PERFORMANCE != OUT_OF_DISTRIBUTION_RELIABILITY`

Ensemble disagreement, residuals, shift detectors, or other uncertainty signals may contribute evidence. They do not themselves establish truth.

## Influence and source-ablation analysis

A training episode, memory item, source, modality, or graph can have outsized influence on a learned topology or predictor.

HC evaluation should support source-ablation/perturbation tests where practical:

1. establish a baseline result;
2. remove, mask, perturb, or downweight a source;
3. recompute the relevant derived topology/prediction;
4. measure the change;
5. record sensitivity and affected outputs.

Large sensitivity is diagnostic evidence about dependence. It is not automatic evidence that the source was correct, incorrect, causal, or should be deleted.

## Graph metrics and null models

Degree, centrality, efficiency, modularity, rich-club structure, small-worldness, community structure, and related metrics may be valuable HC diagnostics.

They must be bound to:

- the topology plane measured;
- the snapshot/time interval;
- weighting/direction/sign conventions;
- node/edge inclusion rules;
- comparison/null model where relevant.

A graph metric must not silently become a cognitive reward or governance signal merely because it is easy to optimize.

Examples of dangerous shortcuts:

- maximizing centrality of one subsystem and thereby creating a de facto homunculus;
- maximizing global efficiency until fault containment disappears;
- maximizing density until selective routing loses meaning;
- treating modularity as proof of functional ontology;
- treating rich-club membership as evidence of authority.

Null/randomized topology comparisons and perturbation tests are preferred when interpreting whether an observed metric is structurally meaningful.

## Information-flow control

Rich HC integration does not require unconstrained mixing.

Topology-aware flow control, gating, capacity allocation, and interaction decoupling are legitimate implementation research directions for preventing bottlenecks, runaway global coupling, oversmoothing-like homogenization, and oversquashing-like loss of long-range information.

However:

`MESSAGE_FLOW_CONTROL != COGNITIVE_AUTHORITY`

`TOPOLOGICAL_IMPORTANCE != SEMANTIC_IMPORTANCE`

`HIGH_FLOW_CAPACITY != EFFECT_PERMISSION`

Flow-control machinery remains subordinate to typed routing, epistemic support, authority, lifecycle, and Noöplex anti-homunculus constraints.

## Failure modes

Relevant failures include:

- inferred edge relabeled as measured;
- statistical connectivity relabeled as physical reachability;
- forecast relabeled as history/currentness;
- generated/super-resolved edge committed without admission;
- population template overwriting instance state;
- alignment transform erasing source disagreement;
- latent embedding treated as semantic truth;
- graph metric becoming an implicit reward/authority function;
- centrality creating permanent executive control;
- domain shift with unchanged confidence;
- influential training source silently dominating topology learning;
- numerical hypergraph projection erasing typed temporal/authority semantics;
- information-flow optimizer bypassing routing or effect governance.

## Conformance questions

A topology-producing component should be able to answer:

1. Was the structure measured, statistically derived, inferred, reconstructed, generated, aligned, embedded, forecast, or committed?
2. Which topology plane is being claimed, and does the evidence class actually support that plane?
3. What estimator/model/reference produced it?
4. What source modalities/domains and time intervals support it?
5. What uncertainty, domain-shift state, and limitations apply?
6. What transformation/alignment/resolution changes occurred?
7. Can the original source evidence be distinguished from the derived topology?
8. Can the result mutate HC topology directly? If so, what separate governance authorizes and verifies the commit?
9. Would a population template or graph metric accidentally become instance authority?
10. What happens under source ablation, null-model comparison, or material domain shift?

## Evidence provenance

This contract was motivated by a source study of network-neuroscience/connectome tooling and graph-learning methods including `nilearn/nilearn`, `cwatson/brainGraph`, and BASIRA Lab projects such as DGN, RegGNN, GSR-Net, HCAE, GraphGradIn, FMDGNN, TAF-GNN, FLAT-Net, GmTE-Net, TIS-Net, DynGNN, predictive-uncertainty-under-domain-shift work, and DeltaGNN.

The source methods are research evidence for computational patterns, not proof that HC's complete synthetic cognitive organ is biologically established or presently implementable. See `docs/research/NETWORK_NEUROSCIENCE_DEEP_SCOUR_2026-09-09.md` for bounded source-by-source observations and transfer limits.