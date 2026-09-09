# HC-1 / HC-2 / HC-3 Research Implications Matrix

Status: architecture-facing research synthesis / not canon

Legend:

- `BASELINE_CONSTRAINT` — strong enough that new HC designs should satisfy it unless explicit contrary evidence is produced.
- `DESIGN_PREFERENCE` — preferred direction with room for alternative implementations.
- `EXPERIMENT` — promising but requires validation before promotion.
- `DO_NOT_ASSUME` — unsupported, over-broad, or dangerous as a default.

| Research finding | Evidence | HC-1 | HC-2 | HC-3 | Disposition |
|---|---|---|---|---|---|
| Hyperconnectivity should mean broad reachable integration, not permanent all-to-all edges | ESTABLISHED | Sparse typed structural fabric + dynamic coalitions | Same, including accelerator routes | Same | BASELINE_CONSTRAINT |
| Structural topology and runtime communication policy must be separate | ESTABLISHED | Explicit routing state | Explicit routing + Q/photonic service routes | Explicit routing across all heterogeneous services | BASELINE_CONSTRAINT |
| No hemispheric partition is required | Architecture invariant | Non-hemispheric | Non-hemispheric | Non-hemispheric | BASELINE_CONSTRAINT |
| High-degree integration hubs need redundancy and fault containment | ESTABLISHED/PLAUSIBLE | Redundant connector paths | Accelerator brokers cannot be sole path | Additional redundancy across advanced substrates | DESIGN_PREFERENCE |
| Communication latency/energy must be first-class resource state | ESTABLISHED | Route budgets | Stronger due heterogeneous fabric | Critical at greater substrate diversity | BASELINE_CONSTRAINT |
| Distributed arbitration is preferable to one omnipotent executive | ESTABLISHED/PLAUSIBLE | Bounded arbiters | Same | Same | BASELINE_CONSTRAINT |
| Arbiter selection must not create semantic truth | Systems constraint | Typed output + uncertainty | Same | Same | BASELINE_CONSTRAINT |
| Hard-real-time body protection must bypass slow deliberation | ESTABLISHED | Dedicated bounded control loops | Same | Same | BASELINE_CONSTRAINT |
| Attention/salience must not become epistemic confidence | ESTABLISHED/PLAUSIBLE | Separate allocation and belief state | Same | Same | BASELINE_CONSTRAINT |
| Metacognitive confidence should be scope-specific and calibrated | ESTABLISHED | Claim/decision-bound estimates | Same | Same | BASELINE_CONSTRAINT |
| Self-monitoring should not be a privileged truth oracle | ESTABLISHED/PLAUSIBLE | Fallible self-model + external receipts | Same | Same | BASELINE_CONSTRAINT |
| Agency attribution should be inferred from action/effect evidence | ESTABLISHED | Fallible agency hypotheses | Same | Same | BASELINE_CONSTRAINT |
| Active coalitions need both stability and release conditions | ESTABLISHED/PLAUSIBLE | Task-scoped activation lifecycle | Same | Same | BASELINE_CONSTRAINT |
| One recent coalition should remain globally dominant by recency alone | Unsupported | No | No | No | DO_NOT_ASSUME |
| Neuromodulation should change gain/eligibility/routing rather than encode truth | ESTABLISHED | Typed modulatory layer | Same | Same | BASELINE_CONSTRAINT |
| One global hormone/modulator scalar should not stand for an emotion or psychological state | ESTABLISHED transfer limit | Distributed affective state | Same | Same | DO_NOT_ASSUME |
| Homeostasis is an active stability process parallel to learning | ESTABLISHED | Stability controller/state | Same | Same | BASELINE_CONSTRAINT |
| Context-dependent internal targets may differ from one fixed set point | ESTABLISHED/PLAUSIBLE | Typed homeostasis/rheostasis/allostasis | Same | Same | DESIGN_PREFERENCE |
| Plasticity itself requires adaptive constraints/metaplastic state | ESTABLISHED | Learning thresholds/homeostasis | Same | Same | BASELINE_CONSTRAINT |
| Structural presence, activation and effective coupling are distinct | ESTABLISHED/PLAUSIBLE | Separate node/route lifecycle state | Same | Same | BASELINE_CONSTRAINT |
| A complete capability may be present while disabled or dormant | Owner design requirement + PLAUSIBLE analogy | Supported lifecycle | Same | Same | BASELINE_CONSTRAINT |
| Node activation proves developmental maturity or qualification | Unsupported | No | No | No | DO_NOT_ASSUME |
| Node activation silently widens effect authority | Unsupported | No | No | No | DO_NOT_ASSUME |
| Whole-brain capability map should equal the currently active cognitive set | Unsupported | No | No | No | DO_NOT_ASSUME |
| Rapid episodic capture and slow semantic integration should use different learning regimes | ESTABLISHED principle | Fast + slow memory paths | Same | Same | BASELINE_CONSTRAINT |
| Biological hippocampus/neocortex anatomy must be copied literally | Unsupported as requirement | No | No | No | DO_NOT_ASSUME |
| Replay/interleaving can reduce interference during slow learning | ESTABLISHED/PLAUSIBLE | Consolidation candidate | Same | Same | DESIGN_PREFERENCE |
| Retrieval should not silently mutate durable memory | ESTABLISHED boundary | Explicit reconsolidation path | Same | Same | BASELINE_CONSTRAINT |
| Corrections should preserve predecessor history/provenance | Engineering consequence | Successor links | Same | Same | BASELINE_CONSTRAINT |
| Imported knowledge should be distinguishable from lived/direct experience | Provenance requirement | Typed source classes | Same | Same | BASELINE_CONSTRAINT |
| Multimodal fusion must preserve source modality, time and uncertainty | ESTABLISHED | Typed sensory evidence | Same | Same | BASELINE_CONSTRAINT |
| Body schema should be learned/calibrated, not fixed solely from geometry | ESTABLISHED | Adaptive body model | Same | Same | BASELINE_CONSTRAINT |
| Interoceptive telemetry is uncertain evidence, not automatic truth | ESTABLISHED/PLAUSIBLE | Redundant estimates | Same | Same | BASELINE_CONSTRAINT |
| Predictive processing should be mandatory ontology for every node | Unsupported as universal mandate | No | No | No | DO_NOT_ASSUME |
| Language form, semantic content and pragmatic interpretation should remain distinguishable | ESTABLISHED/PLAUSIBLE | Typed language/semantic/pragmatic state | Same | Same | BASELINE_CONSTRAINT |
| Meaning should have multiple grounding channels rather than one mandatory grounding doctrine | ESTABLISHED/PLAUSIBLE | Multi-source grounding | Same | Same | DESIGN_PREFERENCE |
| Pragmatic inference should preserve speech act/context/uncertainty | ESTABLISHED | Pragmatic hypothesis state | Same | Same | BASELINE_CONSTRAINT |
| Material semantic ambiguity may remain unresolved | ESTABLISHED/PLAUSIBLE | Bounded interpretation set | Same | Same | BASELINE_CONSTRAINT |
| Referent identity should be explicit when a decision depends on it | Systems constraint | Stable subject bindings | Same | Same | BASELINE_CONSTRAINT |
| One universal token stream should be the only internal interchange format | Unsupported as requirement | No | No | No | DO_NOT_ASSUME |
| Social cognition should be one monolithic empathy function | Unsupported | No | No | No | DO_NOT_ASSUME |
| A model of another agent equals that agent's private ground truth | Unsupported | No | No | No | DO_NOT_ASSUME |
| Self-state and model-of-other should remain separate | ESTABLISHED/PLAUSIBLE | Scoped social state | Same | Same | BASELINE_CONSTRAINT |
| Relationship context should create operational authority | Unsupported | No | No | No | DO_NOT_ASSUME |
| Person-model state should carry privacy and currentness scope | Engineering constraint | Scoped person model | Same | Same | BASELINE_CONSTRAINT |
| One exact semantic wall clock is required for cognition | Unsupported | No | No | No | DO_NOT_ASSUME |
| Evaluator/physical time and brain-visible temporal cues should be separable | ESTABLISHED/PLAUSIBLE | Temporal planes | Same | Same | BASELINE_CONSTRAINT |
| Transport/file/message boundaries automatically define cognitive events | Unsupported | No | No | No | DO_NOT_ASSUME |
| Chronology establishes causality, currentness or authority | Unsupported | No | No | No | DO_NOT_ASSUME |
| Delayed learning credit should be assigned by nearest timestamp | Unsupported | No | No | No | DO_NOT_ASSUME |
| Temporal credit should preserve candidate causes and eligibility | ESTABLISHED/PLAUSIBLE | Typed credit state | Same | Same | BASELINE_CONSTRAINT |
| Event-driven neuromorphic compute is useful for sparse asynchronous workloads | ESTABLISHED capability | Candidate substrate | Candidate substrate | Candidate substrate | DESIGN_PREFERENCE |
| Keep compute near memory/state where workload supports it | ESTABLISHED | Near-memory/local state | Stronger heterogeneous locality | Stronger heterogeneous locality | DESIGN_PREFERENCE |
| Analog/memristive state requires explicit noise, drift, endurance and calibration models | ESTABLISHED | If used | If used | If used | BASELINE_CONSTRAINT |
| Photonics is ready to own all cognition | Unsupported | No | No | No | DO_NOT_ASSUME |
| Photonics is promising for selected matrix, communication and ultralow-latency workloads | ESTABLISHED capability | Optional | Central experiment for Q/photonic services | Candidate expanded role | EXPERIMENT / DESIGN_PREFERENCE |
| Quantum acceleration should be general-purpose cognitive magic | Unsupported | N/A | No | No | DO_NOT_ASSUME |
| Quantum acceleration should require an exact advantaged workload and classical baseline | Systems constraint | N/A | Required for Q service | Required | BASELINE_CONSTRAINT |
| Peak kernel TOPS/W or sub-ns latency predicts whole-brain efficiency | Unsupported | No | No | No | DO_NOT_ASSUME |
| Thermal and power state must participate in runtime resource arbitration | Engineering constraint | Required | Required | Required | BASELINE_CONSTRAINT |
| Precision should be task-dependent | ESTABLISHED | Mixed precision classes | Same | Same | BASELINE_CONSTRAINT |
| Physical plastic media need wear/endurance accounting | ESTABLISHED where applicable | Required if nonvolatile plastic devices used | Same | Same | BASELINE_CONSTRAINT |
| The HC should represent the complete synthetic cognitive organ | Owner design requirement | Whole cognitive boundary | Same | Same | BASELINE_CONSTRAINT |
| Essential reasoning may be outsourced to an unmodeled external mind while HC remains self-contained | Architecture contradiction | No | No | No | DO_NOT_ASSUME |
| External sensors/actuators/services may connect through HC-owned interfaces | Owner design requirement | Body/peripheral boundary | Same | Same | BASELINE_CONSTRAINT |
| External computational output should enter as evidence/service result unless the component is architecturally inside HC | Systems constraint | Explicit provider boundary | Same | Same | BASELINE_CONSTRAINT |
| The central Hyperconnectome fabric should be the sole thinker/homunculus | Unsupported/architecture contradiction | No | No | No | DO_NOT_ASSUME |
| The HC should adapt to different bodies through interface/body-schema remapping where possible | Design target | Body-independent template | Same | Same | DESIGN_PREFERENCE |
| Checkpoint persistence proves metaphysical continuity/consciousness | Unsupported | No | No | No | DO_NOT_ASSUME |
| Generic brain template should contain instantiated identity data | Architecture violation | No | No | No | DO_NOT_ASSUME |

## Highest-value architecture changes suggested by the research

### 1. Define the Hyperconnectome as a multilayer communication system

The architecture should explicitly distinguish:

```text
physical reachability
configured routing
functional coalition membership
modulatory influence
plasticity eligibility
memory provenance
resource state
```

A single “connection” concept is too weak.

### 2. Make selective activation a physical and computational principle

The system should maintain whole-network capability awareness and reachability while activating only the smallest useful coalition for the current task. This reduces energy, contention, interference and failure propagation without deleting dormant capability.

### 3. Give nodes an explicit multi-axis lifecycle

Separate presence, activation, development, qualification, authority, resource state, and health. A capability can be physically/logically present but disabled or dormant; activation is not permission.

### 4. Add fast/slow learning interfaces

Do not force episodic capture, semantic generalization, procedural learning and body calibration through one write mechanism.

### 5. Make attention, confidence and self-monitoring independent state

Attention allocates resources; confidence estimates correctness; self-monitoring models the system's own performance. None should automatically create truth or authority.

### 6. Make semantic/pragmatic state action-bearing

Preserve referents, ambiguity, provenance and pragmatic hypotheses in typed state that can affect tools/actions, not only generated language.

### 7. Scope social cognition as models of others

Person models should preserve self/other separation, privacy, proposition scope, confidence, correction history and currentness rather than becoming global social truth.

### 8. Make chronology semantically narrow

Maintain reliable clocks and elapsed-time services while separating physical time, visible cues, inferred event structure, causality, currentness and learning credit.

### 9. Make state transitions inspectable

Durable changes should carry predecessor/successor links, source, learning context, confidence, and scope. This is particularly important for memory correction, model updates, body calibration and long-term plasticity.

### 10. Treat heterogeneous acceleration as services

Neuromorphic, analog/in-memory, photonic and quantum components should expose explicit service contracts and failure/fallback behavior rather than being assigned identity or global executive status.

### 11. Preserve a self-contained cognitive-organ boundary

External bodies and services may extend sensing, action, communication and compute, but essential cognitive interpretation/reconciliation must remain represented inside HC. Every external dependency should identify whether it is a peripheral, an HC-internal substrate service, or an unacceptable unmodeled cognition dependency.

### 12. Design qualification around hostile perturbation

Every HC generation should be evaluated under:

- node lesions;
- hub/routing failures;
- stale state;
- sensor disagreement;
- actuator/safety urgency;
- memory interference;
- plasticity saturation;
- task-coalition stickiness;
- self-model miscalibration;
- agency spoofing;
- person-model correction/privacy failures;
- referent collisions and pragmatic ambiguity;
- clock skew and timestamp-currentness traps;
- dormant/disabled node activation;
- activation-authority leakage;
- thermal throttling;
- accelerator removal;
- analog drift;
- cross-domain conflict.

## Research-to-canon promotion rule

A matrix entry does not alter HC architecture canon automatically. Promotion requires a reviewed architecture change that cites the evidence or owner requirement, defines the engineering analogue, states transfer risk, and supplies an acceptance/qualification test.