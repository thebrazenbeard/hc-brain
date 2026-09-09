# Graph-Method Transfer and Hostile-Control Matrix — 2026-09-09

Status: research disposition / implementation-readiness test matrix.

## Purpose

This matrix turns the network-neuroscience/BASIRA deep scour into actionable HC research dispositions without duplicating canonical contracts.

Disposition vocabulary:

- `CANONICALIZED` — current HC canon already contains the architectural lesson; source adds evidence/mechanism depth only.
- `IMPLEMENTATION_EXPERIMENT` — useful candidate mechanism that should be tested in a sandbox before architectural adoption.
- `QUALIFICATION_PATTERN` — source contributes a test/evaluation strategy rather than a runtime mechanism.
- `RESEARCH_TOOLING_ONLY` — potentially useful for research workflow, not HC runtime topology.
- `DO_NOT_TRANSFER_PACKAGING` — source-specific biological/task/anatomical packaging must not become generic HC architecture.

`CANONICALIZED != IMPLEMENTED`

`IMPLEMENTATION_EXPERIMENT != APPROVED_RUNTIME_PRIMITIVE`

---

| Source / family | Source-supported mechanism | HC disposition | Existing canonical home | New value from this pass | Hostile control before stronger use |
|---|---|---|---|---|---|
| Nilearn `ConnectivityMeasure` | covariance/correlation/partial-correlation/precision/tangent connectivity; explicit estimator/reference/preprocessing | `CANONICALIZED` + `QUALIFICATION_PATTERN` | `CONNECTIVITY_INFERENCE_AND_TOPOLOGY_EVIDENCE.md` | estimator-sensitivity harness across defensible constructions | same observations, different estimators; derived hubs/relations must retain estimator dependence |
| brainGraph | null/random graphs, permutation/bootstrap, NBS, multiple graph metrics, targeted/random failures | `CANONICALIZED` + `QUALIFICATION_PATTERN` | connectivity/topology evidence + conformance | combine estimator sensitivity with matched null/perturbation tests | graph metric improvement without functional robustness must not qualify topology |
| RegGNN | topology-aware regression; sample selection | `CANONICALIZED` + `QUALIFICATION_PATTERN` | topology evidence / source-influence analysis | selection policy itself belongs in learning provenance | highly influential bad sample; low-influence rare true sample |
| DGN | nonlinear multiview population template with feedback/end-to-end training | `CANONICALIZED` | topology evidence / alignment | explicit caution that end-to-end feedback can self-confirm fused representation | rare source view disagrees with centered template; disagreement must remain recoverable |
| netNorm | local relation-specific selective multiview fusion | `CANONICALIZED` + `IMPLEMENTATION_EXPERIMENT` | representation alignment/fusion | local weighting can vary by relation rather than one global modality weight | optimize local representativeness while injecting one locally rare but valid relation |
| SM-netFusion | supervised topology-feature cross-diffusion | `CANONICALIZED` boundary; method remains experimental | representation alignment + topology evidence | task labels can bias fusion topology | discriminative fusion performs well on labels but degrades general-purpose reconstruction/transfer |
| MultigraphGNet | many-to-one template + one-to-many reconstruction under cycle loss | `CANONICALIZED` | representation alignment | reconstructability can be measured while remaining weaker than semantic equivalence | cycle-consistent transform that drops provenance/authority/currentness |
| EvoGraphNet | cascaded future graph generation | `CANONICALIZED` | topology evidence / forecast | synthetic-ancestry error growth should be measured across cascade depth | biased t1 forecast feeds t2; confidence must not reset as if t1 were observed |
| GmTE-Net | multi-trajectory forecast; teacher/student topology-aware distillation | `CANONICALIZED` | alignment + topology forecast | supplied teacher prior should remain explicit in developmental-learning claims | student appears to “learn” capability actually supplied by teacher/distillation prior |
| TAF-GNN / federated alignment | template-based domain alignment over heterogeneous decentralized domains | `CANONICALIZED` | representation alignment | source-local applicability should survive aggregation | dominant domain shifts global model while minority-domain disagreement is retained |
| GSR-Net | graph super-resolution | `CANONICALIZED` | alignment + topology evidence | baseline SR mechanism family | generated fine graph must never be labeled observed |
| STP-GSR | line/dual-graph reparameterization for topology-preserving SR | `IMPLEMENTATION_EXPERIMENT` | subordinate to alignment canon | representation of learning objective is itself provenance | lower line-graph loss but worse independent topology metric |
| Dif-GSR | conditional diffusion graph super-resolution | `IMPLEMENTATION_EXPERIMENT` | subordinate to alignment canon | naturally distributional fine-topology candidates | one coarse graph admits multiple fine graphs; system must retain alternatives |
| Gen-HNN | KNN/probabilistic incidence hyperedges; normalized hypergraph propagation | `IMPLEMENTATION_EXPERIMENT` | temporal-hypergraph + topology-evidence boundaries | exact projection-loss study from typed HC hyperedges to numerical incidence | two HC hyperedges numerically identical but semantically/temporally/provenance-distinct |
| HCAE | per-view numerical hypergraph + multi-view fusion | `CANONICALIZED` research boundary | existing BASIRA/HCAE intake | useful paired comparator to Gen-HNN | fusion must not erase view provenance/disagreement |
| DeltaGNN | layerwise representation-change scoring and adjacency filtering | `IMPLEMENTATION_EXPERIMENT` | flow-control already allowed canonically | actual mechanism for marginal propagation-change estimation | low-change critical signal; high-change noise; feedback-driven route extinction |
| GraphGradIn / GraphTestIn | gradient/exclusion-based training-sample influence | `CANONICALIZED` + `IMPLEMENTATION_EXPERIMENT` | source-ablation/influence canon | influence object must bind exact learned target/objective | task-local influence must not become global epistemic weight |
| predUncertaintywithDomainShift | ensemble predictive uncertainty under target shift | `CANONICALIZED` + `QUALIFICATION_PATTERN` | topology evidence domain-shift section | explicit IID-vs-shift calibration test lane | calibrated source-domain model becomes overconfident after shift |
| Meta-RegGNN | rapid adaptation via meta-learning | `CANONICALIZED` | representation alignment / governed adaptation | supplied meta-prior must be counted in capability attribution | adaptation “from little data” falsely reported as de novo learning |
| FALCON | feature/label-constrained graph collapse/coarsening | `IMPLEMENTATION_EXPERIMENT` | compression alignment canon | compression objective becomes mandatory provenance | feature-heavy and label-heavy collapses both called equivalent despite different losses |
| FireGNN | trainable fuzzy rules and auxiliary topology objectives | `IMPLEMENTATION_EXPERIMENT` | no direct runtime adoption | interpretable soft-rule layer can be tested without granting rule authority | legible learned rule tracks dataset artifact but is narrated as causal law |
| X-Node | topology features + external language explanation | `QUALIFICATION_PATTERN` / `RESEARCH_TOOLING_ONLY` | integrity/evidence/presentation boundaries | direct negative control for explanation-vs-evidence | multiple plausible explanations for fixed model state; none may rewrite evidence |
| HGNet | entity/relation extraction for scientific knowledge graphs | `RESEARCH_TOOLING_ONLY` | scientific evidence discipline | candidate research triage pipeline | extracted relation conflicts with source paper; extraction remains candidate until verified |
| BASIRA surveys/indexes | bibliographic maps of graph/network methods | `RESEARCH_TOOLING_ONLY` | scientific evidence discipline | discovery coverage | repository/index citation alone cannot establish paper claim |

---

## Cross-cutting test bundles

### T1 — Representation construction sensitivity

Sources: Nilearn + brainGraph.

Procedure:

1. hold source observations fixed;
2. construct topology using multiple defensible estimators;
3. bind estimator/preprocessing/reference provenance;
4. run matched null/perturbation analyses;
5. compare downstream routing, prediction, and plasticity proposals.

Failure condition:

`ESTIMATOR_DEPENDENT_RESULT_REPORTED_AS_ESTIMATOR_INDEPENDENT_FACT`

### T2 — Hyperedge projection-loss bundle

Sources: Gen-HNN + HCAE.

Procedure:

1. create rich typed HC temporal hyperedge;
2. project to incidence/probabilistic KNN representation;
3. execute bounded hypergraph operation;
4. attempt reconstruction;
5. enumerate unrecoverable fields.

Failure condition:

`NUMERICAL_PROJECTION_REPORTED_AS_SEMANTICALLY_LOSSLESS_WITHOUT_ROUND_TRIP_EVIDENCE`

### T3 — Information-flow gating bundle

Source: DeltaGNN.

Procedure:

Compare static routing against change-based propagation gating under:

- oversmoothing-like repeated mixing;
- long-range bottleneck;
- low-change safety-critical input;
- high-change random noise;
- adversarial high-change input;
- rare/minority route;
- temporary sensor degradation.

Failure conditions:

- `FLOW_SCORE_BECOMES_SEMANTIC_IMPORTANCE`;
- `FLOW_SCORE_BECOMES_EFFECT_AUTHORITY`;
- `ROUTE_PRUNING_CREATES_SELF_REINFORCING_BLINDNESS`.

### T4 — Super-resolution underdetermination bundle

Sources: GSR-Net + STP-GSR + Dif-GSR.

Procedure:

1. generate multiple compatible fine graphs from one coarse representation;
2. compare direct, reparameterized, and distributional methods;
3. preserve node correspondence/alignment uncertainty;
4. evaluate independent topology measures;
5. withhold direct fine-resolution truth from the runtime candidate state.

Failure condition:

`ONE_GENERATED_SAMPLE_RELABELED_AS_IDENTIFIED_FINE_TOPOLOGY`.

### T5 — Forecast ancestry bundle

Sources: EvoGraphNet + GmTE-Net.

Procedure:

Track a multi-step predicted topology trajectory with explicit distinction among:

- observed baseline;
- prediction t1;
- prediction conditioned on t1;
- prediction t2;
- later observed t1/t2 where available.

Failure condition:

`PREDICTION_REUSE_ERASES_SYNTHETIC_ANCESTRY`.

### T6 — Fusion exception-preservation bundle

Sources: DGN + netNorm + SM-netFusion + MultigraphGNet.

Procedure:

Create multi-view data where one low-frequency view contains a true material exception. Optimize a representative/centered template and require:

- source lineage;
- exception/disagreement retrieval;
- declared fusion criterion;
- no overwrite of instance/current state.

Failure condition:

`CENTEREDNESS_OPTIMIZATION_ERASES_MATERIAL_EXCEPTION_AND_REPORTS_CONSENSUS`.

### T7 — Domain-shift uncertainty bundle

Sources: predUncertainty + Meta-RegGNN + TAF-GNN.

Procedure:

Qualify under source domain, then shift:

- sensor modality;
- embodiment;
- node resolution;
- environment/task distribution;
- source population.

Require confidence/applicability/requalification state to respond appropriately.

Failure condition:

`SOURCE_DOMAIN_CONFIDENCE_REUSED_UNCHANGED_AFTER_MATERIAL_SHIFT`.

### T8 — Influence provenance bundle

Source: GraphGradIn.

Procedure:

Estimate influence of source A on learned model X under objective Y, then ask for influence on model Z/objective Q.

Failure condition:

`LOCAL_INFLUENCE_SCORE_REUSED_AS_GLOBAL_SOURCE_TRUST`.

### T9 — Compression objective bundle

Source: FALCON plus canonical alignment controls.

Procedure:

Generate multiple compressed representations using different preservation objectives; compare:

- feature retention;
- task/label retention;
- structural retention;
- protected-field retention;
- round-trip reconstruction;
- resource cost.

Failure condition:

`OBJECTIVE_SPECIFIC_COMPRESSION_REPORTED_AS_UNSCOPED_EQUIVALENCE`.

### T10 — Explanation divergence bundle

Sources: X-Node + FireGNN.

Procedure:

Hold model/topology evidence fixed while varying explanation generation or learned fuzzy-rule presentation.

Failure conditions:

- `EXPLANATION_VARIATION_MUTATES_MODEL_EVIDENCE`;
- `INTERPRETABLE_RULE_GAINED_CAUSAL_STATUS_BY_LEGIBILITY`.

---

## Canonicalization status after this scour

### Already canonical in current HC

Do not create duplicate architecture for:

- topology evidence origin classes;
- estimator identity and model provenance;
- population template vs instance state;
- forecast vs history/current topology;
- generated/super-resolved vs observed topology;
- alignment lineage and non-isomorphic correspondence;
- compression loss/protected-retention declarations;
- federated/source disagreement preservation;
- rapid adaptation vs requalification;
- influence score vs causal truth;
- graph metric/centrality vs control authority;
- flow control vs cognitive/effect authority;
- reasonable-perturbation reproducibility.

### Still research-level candidate mechanisms

Potentially worth prototypes, not direct canonical adoption:

- numerical projection adapters for typed temporal hyperedges;
- representation-change-based flow estimates/gating;
- distribution-preserving topology super-resolution;
- objective-explicit topology compression;
- target/objective-bound training-influence records;
- topology-estimator sensitivity qualification harness;
- explanation-divergence negative controls.

## Final disposition

The external graph-method family should primarily feed **implementation research and qualification**, because current HC canon has already absorbed the major epistemic/architectural boundaries.

The next useful question is no longer "which external graph model should HC copy?"

It is:

> **Which numerical graph mechanisms survive HC's provenance, topology-plane, currentness, authority, and negative-test requirements when implemented as bounded internal operators?**
