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
| Neuromodulation should change gain/eligibility/routing rather than encode truth | ESTABLISHED | Typed modulatory layer | Same | Same | BASELINE_CONSTRAINT |
| One global hormone/modulator scalar should not stand for an emotion or psychological state | ESTABLISHED transfer limit | Distributed affective state | Same | Same | DO_NOT_ASSUME |
| Plasticity itself requires adaptive constraints/metaplastic state | ESTABLISHED | Learning thresholds/homeostasis | Same | Same | BASELINE_CONSTRAINT |
| Rapid episodic capture and slow semantic integration should use different learning regimes | ESTABLISHED principle | Fast + slow memory paths | Same | Same | BASELINE_CONSTRAINT |
| Biological hippocampus/neocortex anatomy must be copied literally | Unsupported as requirement | No | No | No | DO_NOT_ASSUME |
| Replay/interleaving can reduce interference during slow learning | ESTABLISHED/PLAUSIBLE | Consolidation candidate | Same | Same | DESIGN_PREFERENCE |
| Retrieval should not silently mutate durable memory | ESTABLISHED boundary | Explicit reconsolidation path | Same | Same | BASELINE_CONSTRAINT |
| Corrections should preserve predecessor history/provenance | Engineering consequence | Successor links | Same | Same | BASELINE_CONSTRAINT |
| Multimodal fusion must preserve source modality, time and uncertainty | ESTABLISHED | Typed sensory evidence | Same | Same | BASELINE_CONSTRAINT |
| Body schema should be learned/calibrated, not fixed solely from geometry | ESTABLISHED | Adaptive body model | Same | Same | BASELINE_CONSTRAINT |
| Interoceptive telemetry is uncertain evidence, not automatic truth | ESTABLISHED/PLAUSIBLE | Redundant estimates | Same | Same | BASELINE_CONSTRAINT |
| Predictive processing should be mandatory ontology for every node | Unsupported as universal mandate | No | No | No | DO_NOT_ASSUME |
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

The system should maintain whole-network reachability while activating only the smallest useful coalition for the current task. This reduces energy, contention, interference and failure propagation.

### 3. Add fast/slow learning interfaces

Do not force episodic capture, semantic generalization, procedural learning and body calibration through one write mechanism.

### 4. Make state transitions inspectable

Durable changes should carry predecessor/successor links, source, learning context, confidence, and scope. This is particularly important for memory correction, model updates, body calibration and long-term plasticity.

### 5. Treat heterogeneous acceleration as services

Neuromorphic, analog/in-memory, photonic and quantum components should expose explicit service contracts and failure/fallback behavior rather than being assigned identity or global executive status.

### 6. Design qualification around hostile perturbation

Every HC generation should be evaluated under:

- node lesions;
- hub/routing failures;
- stale state;
- sensor disagreement;
- actuator/safety urgency;
- memory interference;
- plasticity saturation;
- thermal throttling;
- accelerator removal;
- analog drift;
- cross-domain conflict.

## Research-to-canon promotion rule

A matrix entry does not alter HC architecture canon automatically. Promotion requires a reviewed architecture change that cites the evidence, defines the engineering analogue, states transfer risk, and supplies an acceptance/qualification test.
