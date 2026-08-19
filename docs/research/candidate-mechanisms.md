# Candidate Mechanisms and Negative Findings

This document preserves cross-disciplinary ideas considered for HC-1R. “Outside the box” is a discovery strategy, not an exemption from evidence.

## Selection rule

A candidate enters the reference architecture only if it supplies a defined function, maps to an observable mechanism, admits a comparison against a simpler baseline, and has a plausible physical or simulated realization.

## Retained candidates

### 1. Temporal multilayer hyperconnectome

- **Problem:** Pairwise static graphs cannot represent changing coalitions, multiple signal types, or higher-order binding.
- **Mechanism:** Model HC-1R as a temporal multilayer attributed hypergraph. Layers distinguish event traffic, dense state, modulatory control, memory association, sensorimotor coupling, and assurance. Hyperedges represent transient functional assemblies.
- **Physical interpretation:** A hyperedge need not be a literal multi-terminal wire. It may be realized by a shared workspace token, coincidence window, multicast group, synchronized attractor, common memory object, or routing rule over pairwise links.
- **Observable:** layer-specific degree and cost; participation coefficient; hyperedge lifetime; temporal reachability; integration/segregation; controllability; state-transition energy; failure propagation.
- **Falsifier:** If a pairwise, single-layer baseline predicts behavior and intervention outcomes equally well with lower cost, the hypergraph layer is unnecessary.
- **Class:** **EXTRAPOLATED**.

### 2. Dynamic routing and gain control rather than all-to-all wiring

- **Problem:** Permanent dense connectivity is expensive, noisy, failure-correlating, and difficult to route.
- **Mechanism:** Sparse structural connectivity plus rapidly reconfigurable functional connectivity. A routing/gain-control system constructs task-relevant temporary networks.
- **Inspiration:** Thalamic control of cortical interactions and communication-through-coherence, abstracted as engineering functions rather than copied anatomy.
- **Observable:** routing reconfiguration latency; task-conditioned effective connectivity; congestion; energy; functional isolation; recovery after route loss.
- **Falsifier:** Static routing matches adaptive performance and robustness at lower complexity.
- **Class:** **EXTRAPOLATED**; dynamic routing itself is **DEMONSTRATED** in engineered networks, but its proposed cognitive role is not.

### 3. Dendrite-like local nonlinear subunits

- **Problem:** Treating every processing node as a point neuron may move too much feature interaction into network-level wiring.
- **Mechanism:** Nodes contain several independently addressable nonlinear integration compartments before an output event is generated.
- **Value:** May reduce communication, provide context-sensitive coincidence detection, and support local credit assignment.
- **Observable:** task accuracy per routed event; fan-in; energy; robustness; representational capacity relative to point-neuron and small multilayer baselines.
- **Falsifier:** Equivalent point-neuron or conventional accelerator designs match performance and energy after fair tuning.
- **Class:** Biological dendritic computation is **DEMONSTRATED**; HC-1R use is **EXTRAPOLATED**.

### 4. Metastable cognitive assemblies

- **Problem:** Cognition requires states persistent enough for integration but flexible enough to switch.
- **Mechanism:** Recurrent regions form transiently stable assemblies with controlled dwell times and transition probabilities.
- **Observable:** state repertoire; dwell-time distribution; transition entropy; responsiveness to input; hysteresis; escape from spurious states.
- **Falsifier:** Assemblies either collapse immediately, become rigid attractors, or add no capability over ordinary recurrent-state baselines.
- **Class:** Neuroscientific association is **DEMONSTRATED**; engineered cognitive necessity is **EXTRAPOLATED**.

### 5. Complementary fast and slow learning systems

- **Problem:** Rapid incorporation of episodes conflicts with stable general knowledge and causes catastrophic interference.
- **Mechanism:** A provenance-rich episodic store learns quickly; a slower parametric/semantic system integrates selected information through gated replay and consolidation.
- **Observable:** retention/plasticity curves; interference; provenance fidelity; generalization; correction propagation; rollback success.
- **Falsifier:** A single memory system matches adaptation, retention, and energy without destructive interference.
- **Class:** Principle **DEMONSTRATED** in neuroscience and machine-learning studies; complete HC-1R integration **EXTRAPOLATED**.

### 6. Offline consolidation and maintenance states

- **Problem:** Continuous online plasticity makes verification, calibration, and stable memory difficult.
- **Mechanism:** Scheduled low-input states perform replay, compaction, calibration, integrity checking, thermal balancing, and candidate update evaluation. Call these maintenance states, not biological sleep.
- **Observable:** retention; calibration drift; fragmentation; thermal load; error rate; performance before and after maintenance.
- **Falsifier:** Maintenance yields no benefit or produces unacceptable memory distortion compared with continuous methods.
- **Class:** Component functions **DEMONSTRATED** separately; unified maintenance cycle **EXTRAPOLATED**.

### 7. Homeostatic plasticity guardrails

- **Problem:** Hebbian or reward-gated plasticity can drive runaway activation, silence, or brittle specialization.
- **Mechanism:** Slow negative-feedback controllers regulate firing/event rates, excitation-inhibition analogues, connection churn, learning rate, and resource consumption.
- **Observable:** stability margins; activity distribution; recovery after perturbation; plasticity without collapse.
- **Falsifier:** Homeostatic loops produce oscillation, erase useful learning, or fail to contain runaway dynamics.
- **Class:** Biological principle **DEMONSTRATED**; engineering translation **EXTRAPOLATED**.

### 8. Typed neuromodulatory state vectors

- **Problem:** Local learning and attention need global or regional context, but a single scalar “reward chemical” cannot carry all relevant control state.
- **Mechanism:** A low-bandwidth typed vector distributes bounded signals such as salience, uncertainty, urgency, novelty, reward prediction error, threat, fatigue, plasticity permission, and consolidation priority. Regions subscribe selectively.
- **Observable:** sensitivity, ablation effects, saturation, cross-talk, temporal credit assignment, stability.
- **Falsifier:** Signals are redundant, cannot be disentangled, or destabilize learning and routing.
- **Class:** Three-factor and neuromodulatory principles **DEMONSTRATED**; the exact bus **EXTRAPOLATED**.

### 9. Interoceptive machine-state model

- **Problem:** An embodied system cannot regulate behavior without modeling its physical condition and resource limits.
- **Mechanism:** Treat battery state, temperatures, actuator stress, damage, sensor confidence, network congestion, memory integrity, and compute headroom as primary internal sensory data.
- **Observable:** prediction error, resource violations, graceful task adaptation, calibration, damage response.
- **Falsifier:** The model cannot improve regulation over direct threshold controllers or becomes a route for self-justifying unsafe behavior.
- **Class:** Instrumentation and model-predictive control are **DEMONSTRATED**; unified cognitive interoception is **EXTRAPOLATED**.

### 10. Attention schema as a control instrument

- **Problem:** The system needs a compressed model of what currently receives processing priority and why.
- **Mechanism:** Maintain an explicitly queryable attention/routing schema used for control, confidence calibration, and audit.
- **Observable:** prediction of attention allocation; correction of attentional capture; counterfactual routing; calibration.
- **Falsifier:** Schema does not improve attention control over direct telemetry or produces persuasive but inaccurate self-reports.
- **Class:** **SPECULATIVE** as a consciousness theory; **EXTRAPOLATED** as a control mechanism.

### 11. Morphological computation boundary

- **Problem:** Central cognition should not solve mechanical problems that body compliance and local control can solve more cheaply.
- **Mechanism:** Co-design sensors, compliant structures, actuators, reflex controllers, and higher cognition. Treat body dynamics as part of the closed-loop computation.
- **Observable:** central bandwidth, latency, energy, stability, damage tolerance, sim-to-real sensitivity.
- **Falsifier:** Morphological design reduces generality or provides no benefit over conventional control at equivalent safety.
- **Class:** Principle **DEMONSTRATED**; synthetic-humanoid integration **EXTRAPOLATED**.

### 12. Physical reservoirs as specialized temporal front ends

- **Problem:** High-bandwidth temporal signals can be expensive to digitize and process centrally.
- **Mechanism:** Use memristive, spintronic, photonic, or other nonlinear physical reservoirs only where their dynamics match the signal timescale; train simple readouts or interface layers.
- **Observable:** task performance, memory capacity, bandwidth, calibration burden, total-system energy, drift.
- **Falsifier:** Digital recurrent baselines win on total energy, reproducibility, or maintainability.
- **Class:** Small reservoirs **DEMONSTRATED**; HC-1R deployment **EXTRAPOLATED**.

### 13. Glia-inspired support plane

- **Problem:** Computation depends on resource allocation, cleanup, calibration, repair, and local environmental stability.
- **Mechanism:** A slower support plane monitors regional health, schedules calibration and memory maintenance, regulates resource budgets, and contains anomalies. This is a functional analogy, not an astrocyte simulation.
- **Observable:** fault detection, recovery time, false positives, drift containment, interference with useful plasticity.
- **Falsifier:** Conventional platform management performs equally well or the support plane becomes an unobservable second cognition system.
- **Class:** **EXTRAPOLATED**.

### 14. Immune-inspired danger and anomaly detection

- **Problem:** A self-modifying distributed system needs to recognize corrupt, adversarial, or physiologically impossible internal patterns.
- **Mechanism:** Combine invariant monitors, learned-normal models, diversity of detectors, and local “danger” signals. Do not rely on naive binary self/non-self classification.
- **Observable:** detection latency, false-positive/negative rate, adaptation to legitimate change, containment success.
- **Falsifier:** Learned detectors normalize compromise, attack plasticity, or perform worse than conventional anomaly detection.
- **Class:** Artificial immune algorithms are **DEMONSTRATED** in limited domains; HC-1R use **EXTRAPOLATED**.

### 15. Perturbational and lesion-based evaluation

- **Problem:** Behavioral success alone does not establish that the proposed hyperconnectome mechanisms cause the behavior.
- **Mechanism:** Apply controlled perturbations, region/edge silencing, delay injection, signal scrambling, and topology lesions; measure response complexity, functional specificity, recovery, and graceful degradation.
- **Observable:** causal effect size; response diversity; integration without global collapse; redundancy; compensation.
- **Falsifier:** Claimed regions or hyperedges can be removed without predicted consequences, or metrics fail to distinguish meaningful organization from random complexity.
- **Class:** Intervention methods **DEMONSTRATED** generally; HC-1R metric suite **EXTRAPOLATED**.

## Deferred candidates

### Photonic inter-region fabric

Potentially valuable for high-bandwidth, low-latency communication, but optical/electrical conversion, buffering, switching, memory, and total thermal cost need an end-to-end comparison. **SPECULATIVE for HC-1R**.

### Spintronic oscillatory regions

Potentially useful as compact stochastic oscillators or reservoirs, but current systems are small and often depend on conventional readout. **SPECULATIVE for HC-1R**.

### Structural plasticity in physical hardware

Virtual route and graph changes are testable now. Physically growing or destroying interconnect during operation adds endurance, verification, and rollback problems. **SPECULATIVE physically; EXTRAPOLATED virtually**.

### Wetware or organoid regions

Current experiments demonstrate limited adaptive or reservoir computation but raise reliability, interface, reproducibility, lifecycle, and moral-status problems. Not required for the Noöplex concept. **DEFERRED / SPECULATIVE**.

## Rejected assumptions

| Assumption | Verdict | Reason |
|---|---|---|
| More connections automatically yield more intelligence or consciousness | **REJECTED** | Ignores topology, dynamics, differentiation, wiring cost, congestion, instability, and failure correlation |
| A connectivity threshold causes the system to “wake up” | **REJECTED** | No validated threshold exists; IIT does not reduce to connection count |
| Optimize exact Φ as an engineering objective | **REJECTED for HC-1R** | Exact evaluation is intractable at relevant scale, theory remains contested, and proxy optimization may reward irrelevant structure |
| Operate permanently at the “edge of chaos” | **REJECTED as requirement** | Criticality evidence and definitions remain contested; target measured task/stability outcomes instead |
| Global broadcast proves consciousness | **REJECTED** | It may explain access, flexible coordination, and reportability without settling phenomenology |
| Biological fidelity is intrinsically better | **REJECTED** | Added biological detail must earn its cost through task, energy, robustness, or learning benefits |
| Literal synthetic hormones are required for emotion | **REJECTED** | Functional regulation can be implemented by typed machine-state signals; phenomenology remains unresolved |
| A single reward scalar is an adequate neuromodulatory system | **REJECTED** | Conflates value, uncertainty, salience, threat, fatigue, and plasticity permission |
| Safety can be learned as beliefs inside the plastic core | **REJECTED** | The same cognition could reinterpret, forget, route around, or corrupt them |
| Logical contradiction should damage the cognitive substrate | **REJECTED** | Contradictions require paraconsistent handling, uncertainty, quarantine, and safe degradation—not “brain death” |
| Quantum parallelism is generic cognition acceleration | **REJECTED** | Advantages are workload- and assumption-specific; data movement, error correction, and cryogenics dominate integration |
| A cold QPU belongs inside a warm humanoid head | **REJECTED for foreseeable HC-1R** | Thermal stages, shielding, control electronics, and refrigeration make an external service more credible |
| Organoid task learning establishes sentience | **REJECTED** | Adaptive behavior and reservoir performance do not demonstrate phenomenal experience |
| Electromagnetic-field or quantum-consciousness claims may fill mechanism gaps | **REJECTED pending discriminating evidence** | Renaming integration as a field or quantum effect supplies no unique prediction or engineering interface |

## Promotion rule

A deferred or rejected candidate may be reconsidered only with a new source, a defined workload, a discriminating experiment, and an explicit update to the claim ledger.


