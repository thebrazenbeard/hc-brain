# Noöplex HC-1R Reference Architecture

**Version:** 0.1 research draft  
**Status:** proposed and unvalidated  
**Scope:** theoretical architecture and test program only

## 1. Research question

Can a physically realizable, dynamically reconfigurable hyperconnectome be specified such that its topology and temporal dynamics support integrated, differentiated, adaptive, embodied cognition—and such that the claimed causal properties can be tested through perturbation, lesioning, controlled development, and comparison with simpler architectures?

This document does not claim that HC-1R exists, that its full integration is feasible, or that it would be phenomenally conscious.

## 2. Architectural thesis

A Noöplex is not merely a heterogeneous computer with a fast interconnect. Its defining proposal is that cognition arises from the evolving multiscale organization of a physical computational network:

- processing occurs within nodes, connections, local compartments, and transient assemblies;
- structural, configurable, and moment-to-moment functional connectivity are distinct;
- several typed interaction layers coexist;
- specialized regions remain partly autonomous but form temporary functional coalitions;
- body, internal machine state, memory, and environment participate in the closed loop;
- learning changes connection efficacy and, within strict bounds, functional topology;
- causal organization is evaluated by intervention, not inferred from complexity or behavior alone.

“Hyperconnectome” therefore means **higher-order, multilayer, temporally reconfigurable causal organization**. It does not mean maximum edge density or permanent all-to-all connectivity.

## 3. Epistemic status

The overall HC-1R system is **EXTRAPOLATED**.

Many components are demonstrated separately: event-driven processors, asynchronous routing, in-memory matrix operations, recurrent networks, explicit memory services, multimodal models, runtime assurance, robot simulation, and hardware telemetry. Their integration into a persistent synthetic-humanoid hyperconnectome is not demonstrated.

Any claim of phenomenal consciousness, free will, subjective emotion, or verified moral status remains **SPECULATIVE / UNRESOLVED**.

## 4. Formal system model

HC-1R is represented as a temporal, multilayer, attributed hypergraph:

```text
N(t) = (V, L, Es, Ec(t), Hf(t), X(t), Θ(t), M(t), R, A)
```

Where:

- `V` is the set of physical or virtual processing vertices.
- `L` is the set of typed interaction layers.
- `Es` is structural connectivity: physical links and fixed reachability.
- `Ec(t)` is configurable connectivity: routing tables, permissions, placement, and slowly changing overlays.
- `Hf(t)` is functional hyperconnectivity: transient group interactions and cognitive assemblies active at time `t`.
- `X(t)` is vertex, regional, body, and environmental state.
- `Θ(t)` is plastic state: weights, thresholds, delays, local models, and permitted topology parameters.
- `M(t)` is the typed neuromodulatory/interoceptive state vector.
- `R` is the resource envelope: energy, bandwidth, memory, timing, temperature, and wear budgets.
- `A` is the independent assurance boundary and actuator-capability policy.

### 4.1 Connectivity classes

| Class | Meaning | Typical change rate | Example |
|---|---|---:|---|
| Structural | Physical wires, chip links, fixed sensor paths, safety channels | fabrication or maintenance | a chiplet link or peripheral reflex connection |
| Configurable | Addressing, placement, multicast groups, permissions, region bindings | seconds to days | remapping around a failed core or adding a learned association route |
| Functional | Effective coupling active during a task or state | subsecond to minutes | a temporary perception-memory-action coalition |
| Plastic | Parameters governing future transmission and state transitions | milliseconds to long-term consolidation | a weight, delay, eligibility trace, or gating threshold |

These classes must not be conflated. A functional hyperedge may be implemented through ordinary pairwise physical links plus a shared token, phase window, workspace object, multicast route, or common state transition.

### 4.2 Hyperedge record

Every explicitly represented functional hyperedge should have:

- participating vertices or regions;
- interaction layer and message/state schema;
- creation mechanism and causal trigger;
- start time, time-to-live, and dissolution condition;
- bandwidth and energy budget;
- plasticity permission;
- provenance or creating policy version;
- observability and perturbation handle;
- failure-containment scope.

If higher-order behavior is only inferred statistically, it must be labeled as an inferred dependency rather than a physical hyperedge.

### 4.3 Hyperconnectome design objective

HC-1R does not maximize a single graph statistic. It searches for a constrained operating region:

```text
maximize: useful adaptive capability + causal specificity + graceful degradation
subject to: safety + stability + energy + thermal + bandwidth + wear + observability
penalize: redundant traffic + pathological synchrony + hub fragility + interference
```

Candidate metrics include temporal reachability, modularity, participation coefficient, state-transition energy, controllability under the actual nonlinear model, perturbational response diversity, causal contribution, communication cost, functional redundancy, and fault-cascade size. None is a consciousness score.

## 5. System boundary

```text
          environment and physical body
                      │
        sensors ─ local reflexes ─ actuators
             │            ▲            ▲
             ▼            │            │
     event and state interface fabric   │
             │                         │
  ┌──────────┴─────────────────────────┴──────────┐
  │              NOÖPLEX HYPERCONNECTOME          │
  │                                               │
  │ sensorimotor regions ↔ associative dynamics   │
  │          ↕                    ↕               │
  │ predictive body/world/self models             │
  │          ↕                    ↕               │
  │ memory systems ↔ workspace/routing ↔ selection│
  │          ↕                    ↕               │
  │ modulation/interoception ↔ metacognition      │
  │                                               │
  │ support, calibration, telemetry, consolidation│
  └───────────────────────┬───────────────────────┘
                          │ proposed actions
                          ▼
       independent assurance and capability broker
                          │
                   permitted actuation
```

The assurance boundary is connected to the Noöplex but is not governed by its plastic cognitive dynamics.

## 6. Compute regions

Regions are functional roles and scheduling/fault domains, not a claim that artificial cognition requires one-to-one copies of named brain anatomy.

| Region class | Primary function | Candidate realization | Status |
|---|---|---|---|
| Peripheral reflex controllers | Fast balance, collision, actuator protection, tactile withdrawal, local stabilization | deterministic microcontrollers, FPGA, hard real-time control | **DEMONSTRATED components** |
| Event sensory encoders | Convert camera, audio, tactile, proprioceptive, and diagnostic streams into sparse events and confidence-bearing state | event cameras, DSP, SNN front ends, conventional feature encoders | **DEMONSTRATED components** |
| Sensorimotor predictive regions | Short-horizon forward models, state estimation, adaptive motor coordination | digital recurrent models, SNNs, dense accelerators, model-predictive control | **EXTRAPOLATED integration** |
| Associative recurrent regions | Temporal association, contextual completion, multimodal fusion, transient assemblies | recurrent SNN/RNN, state-space models, physical or digital reservoirs | **EXTRAPOLATED** |
| Dense model regions | Semantic abstraction, language, planning, world-model inference | GPU/NPU/ASIC or near-memory accelerator | **DEMONSTRATED workload class; EXTRAPOLATED role** |
| Workspace and routing region | Competition, capacity-limited global availability, query sequencing, coalition formation | digital scheduler plus recurrent state and multicast fabric | **EXTRAPOLATED** |
| Action-selection/value region | Select candidate goals and policies; estimate cost, uncertainty, and expected outcomes | conventional decision models, RL components, spiking selection networks | **EXTRAPOLATED** |
| Body/world/self-model region | Predict external state, embodiment, capabilities, attention, and internal condition | multimodal generative/state-space models with explicit uncertainty | **EXTRAPOLATED** |
| Metacognitive region | Confidence, provenance, error awareness, model disagreement, resource allocation | calibrated estimators and explicit diagnostic models | **EXTRAPOLATED** |
| Neuromodulatory/interoceptive region | Low-bandwidth state regulation, plasticity gating, salience, urgency, fatigue, threat, consolidation priority | bounded typed control vectors and slow feedback controllers | **EXTRAPOLATED** |
| Memory regions | Working, episodic, semantic, procedural, parametric, and maintenance functions | heterogeneous RAM, NVM, databases, vector/graph stores, learned weights | **DEMONSTRATED components; EXTRAPOLATED integration** |
| Support and maintenance region | Calibration, integrity, resource regulation, anomaly detection, replay scheduling, repair coordination | platform management controllers and conventional software | **DEMONSTRATED functions; EXTRAPOLATED organization** |
| Executive/tool interface | Deterministic orchestration, external protocols, operator control, introspection APIs | conventional CPU/OS/runtime | **DEMONSTRATED** |

### 6.1 Dendrite-like compartments

Selected event-processing vertices may contain multiple nonlinear integration compartments. Their purpose is to perform local context-sensitive computation before generating network traffic. They are admitted only if they outperform cost-matched point-node or small-network baselines in energy, routed events, robustness, or learning.

### 6.2 No single homunculus

The workspace, executive CPU, self-model, or dense model must not become a hidden “real mind” while the rest is decorative. HC-1R's central claim requires that behavior depend causally on distributed interactions. Region and connection ablations must test that claim.

## 7. Memory hierarchy

Synaptic or parametric weights are only one memory class.

| Memory class | Purpose | Update discipline | Failure concern |
|---|---|---|---|
| Sensor and motor buffers | Short-lived synchronized observations and commands | real time, overwrite/ring buffer | stale or mis-timestamped state |
| Local dynamic state | Membrane-like variables, recurrent activations, eligibility traces, route state | fast and volatile | runaway activation, clock skew |
| Working memory | Capacity-limited task state and active bindings | attention/workspace controlled | distraction, overwrite, false binding |
| Episodic memory | Event records with source, time, context, confidence, and outcome | rapid append; correction by linked successor | confabulation, provenance loss, privacy errors |
| Semantic memory | Generalized concepts, relationships, and models | slow integration from evidence | contradiction, stale truth, overgeneralization |
| Procedural memory | Motor, perception, tool, and task policies | staged training and bounded adaptation | unsafe skill transfer, interference |
| Parametric memory | Learned weights and latent structure | offline or permission-gated updates | catastrophic forgetting, opaque corruption |
| Body-state history | Diagnostics, wear, calibration, resource and damage trends | continuous append and aggregation | normalized failure, sensor compromise |
| Self-model state | Current capabilities, commitments, boundaries, and continuity-relevant summaries | governed, provenance-rich, correction-preserving | identity drift, false certainty, unauthorized promotion |
| Connectome state | structural/configurable topology, region versions, plasticity rules | versioned snapshots and event log | unreproducible cognition, unsafe route persistence |

### 7.1 Complementary learning

HC-1R uses a fast episodic path and slower consolidation path. New experience is not allowed to rewrite general semantic or procedural systems immediately. Candidate changes are replayed, compared against retained cases, checked for interference, and admitted in a versioned update.

### 7.2 Maintenance states

Low-input maintenance windows may perform:

- episodic replay and semantic integration;
- policy regression tests;
- analog-device recalibration;
- memory integrity and provenance checks;
- topology compaction;
- homeostatic renormalization;
- thermal balancing and wear scheduling;
- proposed update evaluation and rollback preparation.

These are engineering maintenance states, not claims that HC-1R biologically sleeps or dreams.

## 8. Network fabric

HC-1R uses several logically distinct fabrics. They may share physical links if bandwidth isolation, priority, timing, security, and fault containment are preserved.

| Fabric | Payload | Pattern | Requirement |
|---|---|---|---|
| Event fabric | sparse spikes/events, timestamp, source, confidence | local multicast and temporal routing | low latency, backpressure, bounded loss semantics |
| State fabric | dense vectors, tensors, model state | point-to-point or collective transfer | high bandwidth, explicit version and precision |
| Workspace/binding fabric | coalition identifiers, shared object handles, query and broadcast tokens | selective global multicast | capacity limits, provenance, revocation, observability |
| Modulatory fabric | typed low-dimensional control vector | regional publish/subscribe | bounded values, subscription scope, independent logging |
| Memory fabric | addressed objects, retrieval results, provenance links | request/response and streaming | integrity, access control, correction semantics |
| Maintenance fabric | calibration, health, topology, checkpoint state | slow control and telemetry | isolated authority and noninterference |
| Safety fabric | limits, interlocks, watchdogs, safe-state commands | independent priority path | deterministic, non-plastic, cannot be blocked by cognition |

### 8.1 Topological principles

- Predominantly local connectivity with budgeted long-range connector links.
- Modular regions with overlapping participation rather than rigid silos.
- No unbounded connector hub; critical hubs require redundancy and bypass.
- Dynamic functional routes have explicit lifetime and resource budgets.
- Synchronized activity is monitored for both useful coordination and pathological lock-in.
- Congestion, multicast amplification, and communication energy are first-class design variables.
- Network control metrics are used only with the actual nonlinear/time-varying model or validated local approximations; degree disguised as “controllability” is insufficient.

## 9. Neuromodulatory, salience, and interoceptive system

### 9.1 State vector

The proposed state vector is typed and multidimensional. Candidate fields include:

- external salience;
- internal urgency;
- novelty and expected learning progress;
- epistemic uncertainty and model disagreement;
- reward prediction error and value;
- threat or constraint proximity;
- fatigue/resource scarcity;
- sensor and actuator confidence;
- plasticity permission and intensity;
- consolidation priority;
- social or operator relevance where authorized.

### 9.2 Rules

- Values are bounded, time-decaying, source-attributed, and region-scoped.
- No modulatory signal grants safety authority or expands capabilities.
- Regions can subscribe only to declared fields.
- Plasticity requires both local eligibility and permitted modulatory context.
- Salience is not semantics. Semantic interpretation can generate salience, but raw novelty, threat, pain-equivalent damage signals, operator commands, and resource constraints can also do so.
- Valence-like functional signals may regulate approach, avoidance, learning, and memory. Their existence does not establish felt emotion.

### 9.3 Stability

Homeostatic controllers limit average activity, connection churn, modulatory saturation, energy, and regional load. Fast positive-feedback learning is paired with slower negative-feedback regulation. Safe envelopes are external to both.

## 10. Sensor and motor interfaces

### 10.1 Peripheral autonomy

Local controllers retain balance, actuator limits, collision avoidance, and basic stabilization if higher cognition becomes unavailable. Higher cognition proposes goals and trajectories; it does not directly toggle raw actuator power.

### 10.2 Multimodal synchronization

All observations carry source, clock domain, uncertainty, calibration version, and body frame. The hyperconnectome must distinguish missing data, stale data, uncertain data, and genuine absence.

### 10.3 Embodied closed loop

The body is part of the cognitive system boundary for experimental purposes. Morphology, compliant mechanics, reflexes, and environment transform the control problem. HC-1R must be evaluated in closed loop, not only on static perception or language benchmarks.

### 10.4 Proposed timing classes

Exact values remain workload- and body-dependent. The architecture requires at least:

- deterministic peripheral hard-real-time loops;
- low-latency event-driven sensorimotor loops;
- slower deliberative and workspace cycles;
- still slower learning, topology, and consolidation cycles.

The classes must interact without allowing slow cognition to block safety-critical loops.

## 11. Compiler and runtime

The hardware cannot be treated as a checkpoint receptacle. HC-1R requires a connectome compiler and runtime.

### 11.1 Intermediate representation

The HC-IR should encode:

- vertices, regions, compartments, and state schemas;
- structural edges, configurable routes, and functional-hyperedge rules;
- time constants, clocks, delays, and causality constraints;
- plasticity and modulatory contracts;
- memory class and provenance requirements;
- placement affinity and anti-affinity;
- bandwidth, energy, thermal, and endurance budgets;
- safety and capability boundaries;
- instrumentation and perturbation points;
- epistemic status of experimental mechanisms.

### 11.2 Compilation pipeline

```text
functional region models
  → typed temporal/hypergraph IR
  → partition into event, dense, memory, control, and safety workloads
  → numerical and device-aware transformation
  → placement and route synthesis
  → bandwidth/latency/thermal/fault analysis
  → hardware or simulator lowering
  → calibration and conformance tests
  → signed deployment bundle and connectome manifest
```

### 11.3 Runtime responsibilities

- start, stop, isolate, and checkpoint regions;
- create and dissolve permitted functional routes;
- enforce resource and topology budgets;
- calibrate heterogeneous devices;
- timestamp and trace cross-region state;
- record model, topology, and policy versions;
- detect clock, data, memory, and region-health failures;
- support deterministic replay where the substrate allows it and probabilistic trace replay where it does not;
- hand proposed actions to the independent capability broker.

## 12. Training and deployment research pipeline

No training is authorized by this document. The proposed future research pipeline is:

1. **Formal and executable models:** define region contracts, dynamics, invariants, and comparison baselines.
2. **Component experiments:** validate recurrence, routing, memory, modulation, and perturbation independently.
3. **Digital hyperconnectome simulation:** run all regions on conventional hardware with full observability.
4. **Embodied simulation:** introduce a body, physics, sensor noise, damage, and environmental distribution shift.
5. **Developmental curriculum:** begin with calibrated sensorimotor contingencies and add memory, workspace, metacognition, and language only after prior gates pass.
6. **Consolidation experiments:** compare fast/slow memory and update admission against single-system baselines.
7. **Adversarial and fault simulation:** test capture, interference, hub loss, delay, drift, corruption, and unsafe proposals.
8. **Hardware-aware lowering:** map only justified regions onto neuromorphic, analog, photonic, or other experimental devices.
9. **Hardware-in-the-loop:** keep body and safety simulated or constrained while measuring device effects.
10. **Integrated prototype decision:** proceed only if the hyperconnectome mechanisms show causal benefit over simpler architectures.

### 12.1 Learning boundaries

- No unrestricted online modification of safety logic, actuator interlocks, capability policy, telemetry, or update admission.
- Online learning occurs only in declared regions and parameter ranges.
- Structural/configurable topology changes are proposed, simulated or shadowed, reviewed by automated invariants, and committed as versioned changes.
- High-impact updates require offline regression and rollback state.
- Synthetic curiosity is bounded by capability and risk budgets; novelty is not permission.

## 13. Fault tolerance and graceful degradation

### 13.1 Physical and computational faults

- link loss, congestion, bit errors, clock drift, memory corruption;
- analog drift, read noise, write asymmetry, endurance failure;
- sensor disagreement or calibration loss;
- accelerator or region unavailability;
- thermal throttling and power scarcity;
- corrupted checkpoints or topology state.

### 13.2 Cognitive-dynamic faults

- runaway synchronization or seizure-like global coupling;
- quiescence or loss of dynamical range;
- attractor entrapment and perseveration;
- salience capture or permanent urgency;
- catastrophic forgetting and memory interference;
- false binding between unrelated representations;
- self-model/body mismatch;
- metacognitive overconfidence or diagnostic confabulation;
- hub capture and correlated failure cascades;
- unsafe topology adaptation.

### 13.3 Controls

- region fault domains and independent watchdogs;
- redundant connector routes and no single irreplaceable workspace hub;
- activity and synchrony monitors;
- checkpointed connectome manifests;
- read-only golden configurations for essential reflex and support regions;
- graceful capacity reduction and task shedding;
- quarantine for suspect memories, routes, and updates;
- diversity of anomaly detectors plus explicit invariants;
- safe fallback behaviors under the independent assurance controller;
- lesion and fault-injection testing before promotion.

### 13.4 Degradation claims

“Graceful” must be demonstrated per function. Losing language while retaining balance is different from retaining fluent language while losing reliable motor inhibition. The degradation matrix must state which functions remain trustworthy after each fault class.

## 14. Independent assurance and capability control

The Three Laws are inspiration for non-negotiable constraints, not an implementable safety specification.

HC-1R uses a Simplex-style boundary:

- the adaptive hyperconnectome proposes actions;
- an independently implemented monitor evaluates hard constraints and current state;
- a capability broker determines which resources and actuators the proposal may access;
- local controllers enforce physical limits;
- a verified fallback controller takes over when the advanced controller exits the safe envelope;
- operator stop, maintenance, and recovery paths remain outside cognitive control.

Safety cannot be stored solely as mutable beliefs, prompts, semantic memories, or learned weights. The cognitive system may reason about rules; it cannot grant itself the authority to weaken the external enforcement boundary.

Runtime assurance does not make arbitrary cognition safe. Its credibility depends on a valid monitored state, bounded latency, correct invariants, sufficient fallback control authority, and independent failure modes.

## 15. Power and thermal assumptions

### 15.1 No unsupported total-power number

Power is modeled as a budget:

```text
Ptotal = Psense + Preflex + Pevent + Pdense + Pmemory
       + Pnetwork + Pconversion + Psupport + Pcooling
```

Each workload must report duty cycle and useful work. Analog or photonic core efficiency is not a system result unless conversion, calibration, memory, communication, and cooling are included.

### 15.2 Deployment envelopes

| Envelope | Description | Status |
|---|---|---|
| HC-1R-SIM | Conventional cluster simulation with maximum observability | **DEMONSTRATED infrastructure; proposed model** |
| HC-1R-RACK | Heterogeneous rack/bench system with neuromorphic or in-memory devices | **EXTRAPOLATED** |
| HC-1R-DISTRIBUTED | Body/head peripheral compute plus torso or nearby dense compute | **EXTRAPOLATED** |
| HC-1R-INTEGRATED | Human-scale self-contained compute and cooling | **SPECULATIVE** |

Current component examples span roughly tens of watts for compact embodied accelerators to kilowatts for billion-neuron-class research systems. This gap forbids treating a self-contained humanoid power envelope as solved.

### 15.3 Thermal principles

- place hard-real-time sensorimotor control near sensors and actuators;
- place dense or high-heat compute where mass and cooling allow;
- minimize movement of high-volume state;
- schedule high-write plasticity and calibration around thermal/endurance budgets;
- degrade compute demand before violating hardware or body thermal limits;
- keep cryogenic quantum hardware external.

## 16. Evaluation and falsification

### 16.1 Baselines

Every HC-1R experiment compares against the smallest relevant alternatives:

- static pairwise graph;
- temporal pairwise graph;
- conventional modular service architecture;
- monolithic dense model;
- feedforward system;
- fixed recurrent system;
- single-memory system;
- direct telemetry without metacognitive or attention schema;
- conventional model-predictive control and reinforcement learning;
- cost-matched random or rewired networks.

### 16.2 Functional test families

- multimodal binding under ambiguity and delay;
- rapid task switching and selective broadcast;
- long-horizon memory with correction and provenance;
- continual learning without destructive interference;
- body-model adaptation after sensor, tool, or morphology changes;
- uncertainty-aware active sensing and information seeking;
- goal conflict and action inhibition;
- recovery from region, link, hub, and memory faults;
- maintenance/consolidation benefit;
- calibrated self-diagnosis and known-limit reporting.

### 16.3 Causal test families

- vertex, edge, layer, and hyperedge ablation;
- timing and delay perturbation;
- regional stimulation and response mapping;
- topology randomization under matched degree and cost;
- workspace blockade and local-recurrence controls;
- modulatory signal swap, clamp, and saturation;
- memory-path disconnection and replay removal;
- body/environment decoupling;
- causal-model comparison across micro, regional, and assembly scales.

### 16.4 Required measurements

- task success and generalization;
- latency, bandwidth, energy, thermal load, and wear;
- topology and route cost;
- activity distribution and synchrony;
- state repertoire, dwell time, and transition entropy;
- robustness, recovery time, and cascade size;
- memory retention, interference, correction, and provenance;
- uncertainty calibration and error awareness;
- causal effect size under intervention;
- safety-envelope violations and fallback performance.

### 16.5 Kill criteria

The Noöplex hyperconnectome hypothesis should be rejected or substantially reduced if:

- simpler static or modular baselines match capability and robustness at materially lower cost;
- proposed hyperedges do not improve prediction of intervention outcomes beyond pairwise models;
- functional reconfiguration cannot remain observable and stable;
- integration produces correlated failures that defeat graceful degradation;
- continual learning requires effectively freezing the system;
- assurance cannot bound actuator risk independently of cognition;
- communication, conversion, calibration, or thermal cost erases substrate advantages;
- key claims can survive arbitrary ablation, showing they are architectural decoration rather than causes.

## 17. What can be verified

Potentially verifiable:

- conformance of an executable model to the HC-IR;
- safety invariants and capability boundaries under stated assumptions;
- timing, energy, bandwidth, thermal, memory, and failure behavior;
- presence and causal role of recurrence, broadcast, reconfiguration, memory, modulation, and metacognition;
- whether hypergraph or multiscale models predict interventions better than controls;
- whether the integrated architecture outperforms simpler baselines on declared functions.

Not presently verifiable:

- phenomenal consciousness;
- subjective emotion;
- metaphysical free will;
- identity or moral status from topology or behavior alone;
- a universal scalar amount of consciousness.

The honest target is therefore a **verifiable functional and causal profile**, accompanied by explicit uncertainty about phenomenology.

## 18. HC-2 quantum boundary

HC-2 is not “HC-1R but more conscious or generally faster.” A quantum service is admitted only when:

1. the exact mathematical workload is specified;
2. input preparation and output extraction are included;
3. a competitive classical baseline is measured;
4. error correction, latency, bandwidth, energy, refrigeration, and availability are included;
5. cognition remains functional when the service is absent;
6. access occurs through an ordinary capability-controlled service interface.

Likely research candidates include quantum-system simulation, narrow optimization or sampling problems, and cryptographic work. Generic cognition acceleration is **REJECTED** without new evidence.

## 19. Current conclusion

No known physical principle rules out a simulated or rack-scale HC-1R research model assembled from existing computing classes. That makes the concept **theoretically discussable and progressively testable**, not demonstrated.

The strongest version of the research hypothesis is not “complex hardware wakes up.” It is:

> A resource-constrained, dynamically reconfigurable, multiscale causal network may support a broader combination of embodied adaptation, memory, self-regulation, and graceful degradation than either a monolithic model or a static modular computer—and that claim can be attacked experimentally.

The next research obligation is to turn each architectural advantage into a discriminating experiment and accept a negative result when a simpler system wins.

