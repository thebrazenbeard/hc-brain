# Network Neuroscience and Graph-Methods Deep Scout Supplement — 2026-09-09

Status: research/provenance supplement only; not canonical architecture and not an implementation dependency.

## Why this file is a supplement

Canonical `main` already contains two broad source studies:

- `docs/research/NETWORK_NEUROSCIENCE_DEEP_SCOUR_2026-09-09.md`;
- `docs/research/BASIRA_ALIGNMENT_REPRODUCIBILITY_SCOUR_2026-09-09.md`.

It also already contains canonical architecture/conformance for connectivity inference, topology evidence, representation alignment, resolution change, generated topology, compression lineage, domain shift, source influence, null-model thinking, and message-flow control.

This file therefore does **not** restate those conclusions as new proposals.

Its purpose is narrower: record implementation-level or source-family details found in Four's independent deeper pass that sharpen existing canon or create additional hostile tests.

No source code is copied into HC.

## Governing boundary

`SOURCE_METHOD != HC_CANON`

`NUMERICAL_GRAPH_OPERATION != HC_RUNTIME_SEMANTICS`

`MODEL_SUCCESS != IMPLEMENTATION_QUALIFICATION`

`BRAIN_NETWORK_PACKAGING != HC_TOPOLOGY_REQUIREMENT`

Human atlas/ROI/hemisphere packaging remains source context only.

---

## S1. Gen-HNN makes the numerical-hyperedge construction assumption explicit

### Source observation

`basiralab/Gen-HNN/Hypergraph_utilities.py` constructs numerical hypergraphs by:

1. computing Euclidean distances between feature vectors;
2. choosing K-nearest neighbors around each center node;
3. assigning binary or probabilistic incidence weights;
4. optionally concatenating hyperedges across scales/views;
5. converting incidence `H` into a normalized propagation operator using node degree, hyperedge degree, and hyperedge weights.

Its multi-view helper constructs a KNN hypergraph per view and concatenates the incidence matrices before generating the propagation matrix.

### Existing canon strengthened

Canonical HC already says numerical hypergraph projection is not the HC functional coalition itself. This source provides a concrete reason:

`KNN_NEIGHBORHOOD_HYPEREDGE != TYPED_TEMPORAL_HC_HYPEREDGE`

The KNN incidence column does not inherently encode:

- participant roles;
- causal direction;
- semantic relation type;
- time interval/lifetime;
- authority/effect constraints;
- provenance lineage;
- unresolved alternatives;
- currentness;
- coalition formation/dissolution semantics.

### New implementation-readiness question

Any adapter from HC typed hyperedges into numerical hypergraph tensors should be able to declare:

```text
retained_fields[]
omitted_fields[]
projection_method
projection_parameters
reconstruction_capability
round_trip_test_refs[]
intended_computation
claim_ceiling
```

### Hostile test

Create two HC hyperedges with identical participant sets/numerical incidence but different roles, temporal scopes, or provenance. If the projected representation cannot distinguish them, downstream computation must not be allowed to claim those distinctions survived projection.

---

## S2. DeltaGNN's information-flow control is representation-change gating, not generic importance

### Source observation

The inspected `DeltaGNN` model computes message-passing change at each layer and uses those changes to alter graph propagation.

Observed pattern:

```text
next_x = adjacency @ x
first_delta = norm(next_x - previous_x)
second_delta = abs(delta_t - delta_t-1)
smoothed_statistics -> node/flow score
endpoint scores -> edge score
retain a configured fraction of higher-scoring edges
```

The code can also construct an alternate heterophily graph by selecting nodes from connected components and connecting selected representatives.

### Existing canon strengthened

Canonical HC already permits topology-aware information-flow control while stating:

`MESSAGE_FLOW_CONTROL != COGNITIVE_AUTHORITY`

Four's deeper code read adds another necessary boundary:

`REPRESENTATION_CHANGE_MAGNITUDE != INFORMATION_VALUE`

`REPRESENTATION_STABILITY != IRRELEVANCE`

`REPRESENTATION_CHANGE != NOVEL_EVIDENCE`

A large hidden-state change can come from noise/adversarial input; a tiny change can correspond to a stable but safety-critical invariant.

### Candidate research object

Not proposed for canon yet:

```text
INFORMATION_FLOW_ESTIMATE {
  route_or_relation_ref
  measurement_window
  representation_basis
  change_measure
  marginal_change_measure
  comparison_baseline
  model_or_layer_context
  uncertainty
  provenance
}
```

### Hostile tests

1. low-change safety-critical signal must survive;
2. high-change random/adversarial signal must not gain semantic priority;
3. flow pruning must not become self-reinforcing until minority channels disappear;
4. altered density must be tested for oversmoothing, oversquashing, fragmentation, and runaway centralization;
5. flow score must not directly mutate durable topology or effect authority.

---

## S3. STP-GSR shows that topology preservation can depend on reparameterization

### Source observation

`STP-GSR` reformulates graph super-resolution edge regression into node regression through dual/line-graph construction. The project explicitly positions this reparameterization as a way to better preserve topology.

### Existing canon strengthened

Canonical HC already requires:

`SUPER_RESOLVED_GRAPH != OBSERVED_HIGH_RESOLUTION_GRAPH`

The new methodological lesson is different:

> A representation change can make some structural constraints easier to learn, while changing which errors are natural or visible to the model.

### New qualification question

A topology-generating model should report not only final graph error but also the **representation in which the learning objective was applied**.

`LOW_ERROR_IN_DUAL_REPRESENTATION != ALL_ORIGINAL_GRAPH_PROPERTIES_PRESERVED`

### Hostile test

Compare direct adjacency prediction and line/dual-graph prediction while holding source/target data fixed. Evaluate both edge-level error and independent graph/topology measures. If one representation improves its training objective but damages an unoptimized structural property, the loss surface should not define the claim ceiling by itself.

---

## S4. Dif-GSR makes graph super-resolution explicitly distributional

### Source observation

`Dif-GSR` uses a noising process, a conditional denoiser, and sampling to produce high-resolution brain graphs conditioned on lower-resolution/inter-modality source graphs. Its framing explicitly addresses non-isomorphic source/target graph sizes/distributions.

### Existing canon strengthened

Canonical HC already preserves generated high-resolution detail as generated and supports non-isomorphic correspondence uncertainty.

The source adds an important practical lesson:

`ONE_COARSE_GRAPH MAY_SUPPORT MULTIPLE_FINE_GRAPH_CANDIDATES`

A topology-resolution system should therefore be able to retain a candidate distribution or multiple samples where the problem is underdetermined.

### Hostile test

Construct a coarse topology compatible with multiple fine topologies. If the system returns one candidate and labels it identified rather than sampled/inferred, the epistemic representation is too strong.

---

## S5. FALCON shows that compression equivalence is objective-dependent

### Source observation

`FALCON` collapses graphs under a feature/label preservation objective and exposes parameters that trade feature preservation against label preservation. It also benchmarks centrality-based and other graph-coarsening approaches.

### Existing canon strengthened

Canonical alignment conformance already requires a declared compression loss profile and protected-field retention.

Four's source read adds a sharper hostile condition:

> Two compressed graphs produced from the same source under two different preservation objectives can both be useful while preserving materially different information.

Therefore:

`COMPRESSION_OBJECTIVE_IS_PART_OF_COMPRESSION_MEANING`

`TASK_PERFORMANCE_PRESERVED != GENERAL_STRUCTURE_PRESERVED`

`LABEL_PRESERVATION != FEATURE_PRESERVATION`

### Hostile test

Compress the same graph under feature-heavy and label-heavy objectives. Require the HC to preserve which objective produced each result and forbid a generic `EQUIVALENT_GRAPH` label unless independent tests support the claimed equivalence scope.

---

## S6. GraphGradIn turns training influence into an auditable object

### Source observation

`GraphGradIn` and `GraphTestIn` estimate influence of individual training multigraphs on a learned population template through gradient-based or sample-exclusion analyses.

Canonical HC already added source-ablation/influence analysis.

### New implementation-readiness refinement

An influence result should identify the **learned target and objective** it is influence over.

Candidate research object:

```text
LEARNING_INFLUENCE_ESTIMATE {
  source_evidence_ref
  learned_subject_ref
  learning_objective_ref
  intervention_or_estimator_method
  effect_measure
  uncertainty
  applicability_scope
  provenance
}
```

Without `learned_subject_ref` and `learning_objective_ref`, a local influence score can be laundered into global epistemic importance.

### Hostile test

Make one example highly influential for a task-specific classifier but irrelevant to a different learned state. The influence record must not transfer its weight across targets automatically.

---

## S7. FireGNN and X-Node sharpen explanation/rule boundaries

### FireGNN source observation

`FireGNN` combines GNN embeddings with trainable Gaussian fuzzy-rule parameters and auxiliary tasks such as similarity, homophily, and neighborhood entropy prediction.

### X-Node source observation

`X-Node` computes topological features and uses an external language-model service to generate human-readable explanations of model/topology behavior.

### HC transfer boundary

These are useful examples of **interpretability layers**, but they justify stronger distinctions:

`TRAINABLE_FUZZY_RULE != ARCHITECTURAL_LAW`

`AUXILIARY_OBJECTIVE != EPISTEMIC_AUTHORITY`

`EXPLANATION_TEXT != MODEL_STATE`

`PLAUSIBLE_EXPLANATION != CAUSAL_EXPLANATION`

`EXTERNAL_EXPLANATION_SERVICE != INTROSPECTIVE_TRUTH`

### Hostile tests

- generate two equally plausible explanations from the same fixed model state;
- deliberately make an explanation inconsistent with a measured model feature and ensure the explanatory text does not rewrite the evidence;
- train a fuzzy rule that correlates with a dataset artifact and ensure legibility does not promote it to causal truth.

---

## S8. HGNet is more useful as research tooling than as HC topology evidence

### Source observation

`HGNet` targets scientific entity/relation extraction from literature. Its relation model is hierarchy-aware and its SPHERE benchmark is described as LLM-generated across several scientific domains.

### HC disposition

Potential future role:

- literature triage;
- candidate entity/relation extraction;
- organizing research leads.

Not justified role:

- direct scientific-evidence admission;
- canonical HC ontology generation;
- automatic architectural relation admission.

`EXTRACTED_RELATION != VERIFIED_SCIENTIFIC_RELATION`

`LLM_GENERATED_BENCHMARK != EMPIRICAL_GROUND_TRUTH`

---

## S9. netNorm / DGN / SM-netFusion reveal different meanings of "representative"

Canonical HC already distinguishes population templates from instance topology. The source-family comparison adds a qualification refinement.

The methods optimize different mixtures of:

- centeredness;
- reconstruction/representativeness;
- discriminability;
- local topology;
- global topology;
- cross-view structure.

Therefore:

`REPRESENTATIVE_REQUIRES_DECLARED_CRITERION`

A future HC reference/template object should never carry bare `representative: true` without the criterion and evaluation basis.

---

## S10. Nilearn and brainGraph jointly support estimator-plus-null-model qualification

Noah's canonical connectivity-evidence contract already captured estimator identity and graph/null-model discipline.

Four's cross-tool synthesis adds one practical test pattern:

```text
same source observations
-> multiple defensible connectivity estimators
-> multiple graph candidates
-> matched null/perturbation analyses
-> downstream functional comparison
```

This tests whether a learned HC conclusion is robust to reasonable representation choices rather than accidentally dependent on one estimator.

### Hostile test

If a claimed critical hub exists under correlation but disappears under partial correlation/precision and reasonable preprocessing variants, the architecture should represent estimator sensitivity rather than promoting the hub as unconditional topology truth.

---

## S11. What Four found that is already canonical and should not be duplicated

The following lessons surfaced independently in this deep source pass but are already represented on `main` and should **not** generate another architecture PR:

- connectivity estimator identity is part of evidence meaning;
- inferred/statistical connectivity is not physical reachability;
- generated/super-resolved topology is not observed topology;
- forecast topology is not current topology or plasticity commit;
- population template is not instance authority;
- domain alignment is not semantic equivalence;
- non-isomorphic alignment retains correspondence uncertainty;
- cycle consistency is not semantic correctness;
- fast adaptation is not automatic requalification;
- distributed/federated aggregation is not consensus truth;
- compression needs a declared loss profile and protected retention;
- influence score is not causal truth;
- graph metric/centrality is not authority or control objective;
- message-flow control is not cognitive/effect authority;
- learned topology should survive reasonable perturbation/reproducibility tests.

This supplement should therefore be evaluated as **research depth and hostile-test refinement**, not as an alternative canonical design.

---

## S12. Recommended next implementation research

### R1. Typed-hyperedge numerical projection loss study

Build a toy HC hyperedge object containing roles, timing, provenance, uncertainty, lifecycle, and authority-related metadata. Project it into KNN/incidence form and measure exactly what becomes unrecoverable.

### R2. Delta-style flow pilot

Prototype representation-change-based flow scoring in a non-authoritative routing sandbox. Compare against static and salience-based routing under:

- low-change critical signal;
- high-change noise;
- minority channel;
- long-range bottleneck;
- adversarial perturbation.

### R3. Estimator sensitivity harness

Using synthetic or replayable signal data, derive multiple topology candidates under correlation/partial-correlation/precision/distance/learned relation estimators. Test whether downstream route/plasticity conclusions are stable.

### R4. Distributional super-resolution harness

Generate multiple fine-topology candidates from one coarse state and require explicit candidate distribution/correspondence uncertainty.

### R5. Compression objective comparison

Apply at least two incompatible preservation objectives to the same graph and require explicit loss profiles. Verify protected semantics independently of task score.

### R6. Influence-target binding

Prototype source-ablation/influence records that bind each influence estimate to one exact learned target and objective.

### R7. Explanation divergence test

Generate multiple explanations for a fixed graph/model state and prove that explanation variation cannot mutate underlying model/topology evidence.

---

## Current disposition

KEEP as supplemental research/provenance.

The new material does not justify another top-level HC architecture. It strengthens implementation-readiness tests for canon that Noah has already established.

The highest-value transfer is therefore:

`DEEPER_SOURCE_MECHANISM -> MORE_PRECISE_NEGATIVE_TEST + IMPLEMENTATION_EXPERIMENT`

not:

`DEEPER_SOURCE_MECHANISM -> DUPLICATE_CANONICAL_CONTRACT`.
