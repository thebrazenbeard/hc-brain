# Outside-the-Box Mechanism Audit for HC-1R

## Purpose

This audit searches adjacent fields for mechanisms that could materially improve the Noöplex HC-1R reference architecture. It is intentionally adversarial: resemblance to biology, novelty, and evocative language do not count as evidence. A candidate earns a place only by supplying a defined function, a physical or simulated implementation path, a measurable advantage over a simpler baseline, and a result that could demote or reject it.

The research object is the **Noöplex hyperconnectome**: an evolving, multiscale physical computational network whose transient coalitions, memories, body coupling, and assurance boundaries produce testable cognitive functions. “Positronic brain” language is inspiration only. None of the mechanisms below establishes phenomenal consciousness, personhood, free will, or a threshold at which a system “wakes up.”

## Reading the verdicts

- **PROMOTE TO HC-1R CONTRACT:** strong enough to specify as a reference-architecture function, while still requiring system-level tests.
- **PROTOTYPE AS AN ABLATION:** plausible and testable, but not yet justified as a required mechanism.
- **DEFER:** preserve the hypothesis, but do not burden HC-1R until a workload or integration advantage is demonstrated.
- **REJECT:** the proposed use has no discriminating prediction, confuses metaphor with mechanism, or creates more risk than measurable value.
- **DEMONSTRATED** always refers to the cited component and scope. It never means that a complete Noöplex, human-level synthetic cognition, or machine consciousness has been demonstrated.

## Audit result at a glance

| Candidate | HC-1R disposition | Evidence class for HC-1R integration | Principal reason |
|---|---|---:|---|
| Factor-graph message passing | Promote contract | **EXTRAPOLATED** | Gives higher-order dependencies an executable, inspectable semantics |
| Hyperdimensional / vector-symbolic binding | Prototype | **EXTRAPOLATED** | Promising robust binding and compositional working-state representation; capacity and decoding remain workload-dependent |
| Event-sourced provenance plus restricted CRDTs | Promote contract | **EXTRAPOLATED** | Preserves causal history and tolerates regional disconnection without equating convergence with truth |
| Typed graph rewrites and e-graphs | Prototype | **EXTRAPOLATED** | Can make topology plans and symbolic alternatives explicit before activation |
| Proof-carrying, capability-limited updates | Promote contract | **EXTRAPOLATED** | Constrains self-modification at an independently checked runtime boundary |
| Self-stabilizing regional protocols | Promote contract | **EXTRAPOLATED** | Provides convergence-after-fault objectives stronger than generic redundancy |
| Viability kernels / control barrier functions | Promote contract | **EXTRAPOLATED** | Turns machine interoception into enforceable safe-set constraints |
| Learning-progress developmental curriculum | Prototype | **EXTRAPOLATED** | Offers a measurable alternative to raw novelty seeking |
| Continuous embodied self-model | Promote contract | **EXTRAPOLATED** | Supports damage detection, recalibration, and counterfactual control |
| Morphological computation and soft-body reservoirs | Prototype | **EXTRAPOLATED** | Can reduce central bandwidth for matched sensorimotor workloads |
| Event-based sensory transduction | Promote interface option | **EXTRAPOLATED** | Matches asynchronous fabric and demonstrated low-latency change sensing |
| In-materia temporal coprocessors | Prototype, specialized | **EXTRAPOLATED** | Useful only when device dynamics beat digital baselines end to end |
| Glia-inspired support plane | Promote function, not biology | **EXTRAPOLATED** | Separates slower resource, calibration, and maintenance loops from fast cognition |
| Danger-weighted anomaly ecology | Prototype | **EXTRAPOLATED** | Adds local damage context and detector diversity; naive self/non-self is brittle |
| Budgeted structural growth and pruning | Prototype offline first | **EXTRAPOLATED** | Makes the hyperconnectome developmental, but topology churn is hard to assure |
| Chemical-reaction-network semantics | Defer | **SPECULATIVE** | Useful formal language for local stochastic rules; literal chemistry adds no HC-1R value |
| Stigmergic coalition assembly | Defer | **SPECULATIVE** | Local coordination may scale, but stale traces and herding threaten observability |

---

## 1. Factor-graph message passing as an executable hyperedge

- **Problem:** A temporal hypergraph says that several variables participate in a joint relation, but it does not by itself specify how uncertainty is computed, how evidence is combined, or how a higher-order relation executes.
- **Primary or authoritative evidence:** Kschischang, Frey, and Loeliger showed that factor graphs express a global function as local factors and unify many message-passing algorithms under sum-product [S01]. Yedidia, Freeman, and Weiss showed how generalized belief propagation relates to region-based free-energy approximations, while also making clear that loopy inference is approximate and is not guaranteed to behave like tree inference [S02].
- **Translation to HC-1R:** Represent selected functional hyperedges as typed factor nodes. Variables may be percepts, latent world states, body states, candidate actions, provenance confidence, or memory hypotheses. A factor declares its scope, message type, update schedule, precision, validity interval, and confidence semantics. This makes “many-way binding” an inspectable computation rather than a decorative hyperedge. It does **not** require every hyperedge to be probabilistic; routing, synchronization, and symbolic factors can use other typed reducers.
- **Integration cost:** Medium to high. The compiler needs factor schemas, schedule selection, damping or convergence controls, approximate-inference telemetry, and escape paths for nonconvergence. Dense loopy factor graphs can become computationally intractable.
- **Observable:** Marginal calibration; convergence rate; message count and energy; sensitivity to factor removal; inferred uncertainty under conflicting evidence; accuracy and latency versus pairwise graph, transformer, and centralized Bayesian baselines.
- **Falsifier:** A pairwise or centralized baseline matches prediction, calibration, intervention response, and energy on the same tasks; or loopy updates oscillate, overcount evidence, or fail time limits often enough to make the mechanism unsafe.
- **Status:** Factor-graph inference is **DEMONSTRATED** in its established domains. Its use as a general executable layer for HC-1R hyperedges is **EXTRAPOLATED**. **PROMOTE TO HC-1R CONTRACT**, but only for relations whose factorization is explicit and testable.

## 2. Hyperdimensional / vector-symbolic computing as a binding plane

- **Problem:** HC-1R needs rapid composition of role–filler structures, multimodal bindings, temporary coalitions, and content-addressable queries without forcing every association into a large dense model update.
- **Primary or authoritative evidence:** Kanerva formalized high-dimensional random-vector representations and binding, bundling, and similarity operations [S03]. Eliasmith and colleagues demonstrated a 2.5-million-neuron Spaun model performing multiple tasks with a semantic-pointer architecture, which is evidence for integrated vector-symbolic control—not for consciousness or biological equivalence [S04]. Rahimi and colleagues demonstrated an HDC classifier with energy and memory-fault-tolerance advantages on a bounded language-identification workload [S05], and analyzed HDC as a nanoscalable computing paradigm across several tasks [S06].
- **Translation to HC-1R:** Add an optional **semantic binding plane** whose values are typed hypervectors. Binding represents relations such as `role ⊗ filler`; permutation or tagged transforms represent order; superposition represents a bounded temporary set; associative cleanup maps noisy queries to registered concepts. Bindings must carry provenance pointers to source records so that similarity never becomes truth or authority. Long-term memory remains a distinct store rather than an indefinitely growing superposition.
- **Integration cost:** Medium. It requires a vector type system, dimension and capacity budgeting, cleanup memories, collision and alias telemetry, learned encoders for non-symbolic modalities, and translation to and from dense representations. Very high dimensions consume bandwidth even when arithmetic is simple.
- **Observable:** Binding/unbinding error; capacity before crosstalk; compositional generalization; noise tolerance; energy per binding and lookup; provenance round-trip accuracy; performance against tensor-product, attention, key–value memory, and conventional symbolic baselines.
- **Falsifier:** The representation cannot maintain role identity under realistic superposition load; cleanup produces confident false matches; learned encoders dominate cost; or ordinary sparse key–value memory and attention match robustness and generalization with less bandwidth.
- **Status:** Component operations and bounded applications are **DEMONSTRATED**. A persistent general cognitive binding plane is **EXTRAPOLATED**. **PROTOTYPE AS AN ABLATION**; do not define “high dimensional” as inherently cognitive or conscious.

## 3. Event-sourced provenance with restricted CRDT working sets

- **Problem:** A distributed, plastic cognitive system must revise beliefs and memories without erasing why they existed, survive temporary regional disconnection, and distinguish concurrent updates from corrections. A mutable database row is inadequate provenance; a single global lock is a bottleneck and a failure concentration.
- **Primary or authoritative evidence:** W3C PROV defines interoperable entities, activities, agents, and provenance relations [S07]. Shapiro and colleagues formalized conflict-free replicated data types and sufficient conditions for strong eventual convergence [S08]. Kafka’s original system paper demonstrates the engineering value of durable, replayable partitioned logs at high throughput, although it is not a cognitive-memory model [S09].
- **Translation to HC-1R:** Store memory-changing acts as append-only, content-addressed events with source type, actor/process, causal parents, event time, durable-record time, confidence, privacy/scope, and lifecycle state. Materialized working views are derived and rebuildable. Use CRDTs only for fields whose merge semantics are genuinely commutative—sets of observations, counters, bounded telemetry, or explicitly multi-valued concurrent hypotheses. Corrections, supersession, authority, and truth resolution require governed semantics and cannot be delegated to last-writer-wins or set union.
- **Integration cost:** High storage and index cost; schema evolution; causal metadata; garbage-collection rules; privacy deletion/tombstone policy; and replay determinism. Append-only storage complicates erasure and can preserve harmful or sensitive material unless lifecycle controls are designed from the start.
- **Observable:** Lost-update rate; deterministic readback after replay; conflict detection; convergence time after partition; provenance completeness; correction propagation; storage amplification; ability to reproduce the state used for a decision.
- **Falsifier:** A transactional single-writer architecture achieves the same availability and fault tolerance at lower complexity; replay cannot reproduce decision state; merges silently change semantics; or lifecycle/privacy constraints cannot be met.
- **Status:** Provenance standards, durable logs, and CRDT convergence are **DEMONSTRATED** engineering mechanisms. Their combination as HC-1R memory infrastructure is **EXTRAPOLATED**. **PROMOTE TO HC-1R CONTRACT** with the explicit invariant: **convergence is not correctness, and replication is not memory admission**.

## 4. Typed graph rewriting and e-graphs for topology planning

- **Problem:** An evolving hyperconnectome needs a precise language for adding, removing, splitting, or rerouting regions and hyperedges. Direct mutation of a live graph is difficult to review, roll back, or compare against alternatives.
- **Primary or authoritative evidence:** Double-pushout graph transformation provides a formal account of rule-based graph changes; recent Isabelle/HOL work machine-checks core results of that framework [S10]. Willsey and colleagues demonstrated that e-graphs can efficiently represent many equivalent expressions and support equality-saturation-based optimization in multiple compiler applications [S11].
- **Translation to HC-1R:** Express a topology proposal as a typed rewrite with preconditions, negative application conditions, affected resources, provenance, expected behavioral delta, rollback graph, and invariants. Compile competing legal rewrites into an e-graph-like proposal space; extract a candidate according to cost, latency, robustness, and verification obligations. Rewrites activate only in a sandbox or maintenance state after independent checks.
- **Integration cost:** High. General graph-rewrite search can explode combinatorially. Equivalence rules can be unsound for stateful, timed, stochastic, or physically placed regions. Live topology changes need quiescence, state transfer, and version-compatible interfaces.
- **Observable:** Rewrite validation time; proposal-space size; invariant violations caught before activation; extracted topology cost; rollback success; performance against hand-authored and gradient-based architecture search.
- **Falsifier:** Rewrite search costs more than it saves; declared equivalences fail under timing or state; extracted graphs are brittle; or constrained templates provide the same benefits with far less machinery.
- **Status:** Formal graph rewriting and practical equality saturation are **DEMONSTRATED** in bounded domains. Their use for cognitive topology planning is **EXTRAPOLATED**. **PROTOTYPE AS AN ABLATION**, offline first.

## 5. Proof-carrying, capability-limited cognitive updates

- **Problem:** A plastic system may propose new modules, routes, or learning rules, but allowing the proposer to define its own safety evidence or permissions makes the boundary circular.
- **Primary or authoritative evidence:** Necula’s proof-carrying code lets a host check that untrusted code satisfies a predefined safety policy [S12]. CHERI demonstrates fine-grained hardware-supported capabilities and scalable compartmentalization [S13]. The seL4 project demonstrated machine-checked functional correctness for a practical microkernel, while explicitly stating assumptions outside the proof [S14].
- **Translation to HC-1R:** Treat every executable module and graph rewrite as an artifact with a manifest, least-authority capabilities, resource envelope, interface/effect types, and independently checkable evidence. The plastic cognition may propose an update but cannot mint permissions, alter the checker, expand the policy, or activate a protected effect. The minimal trusted substrate verifies signatures, proofs or certificates where available, resource bounds, and capability confinement. Unproved learned components remain sandboxed behind runtime assurance.
- **Integration cost:** Very high for rich learned components. Full functional proofs will often be unavailable; policies can omit important properties; proof generation may dominate development. Hardware capabilities protect access, not intent or semantic correctness.
- **Observable:** Unauthorized access attempts blocked; proof/check latency; trusted-computing-base size; policy coverage; compartment escape tests; behavior under malicious or malformed update proposals; ability to revoke an update without corrupting memory state.
- **Falsifier:** The proof or capability policy cannot express the relevant hazards; checker/manifest complexity rivals the component; performance overhead breaks real-time deadlines; or adversarial tests find routes around confinement.
- **Status:** Proof-carrying code, capability architectures, and verified kernels are **DEMONSTRATED** within their scopes. An HC-1R self-modification boundary built from them is **EXTRAPOLATED**. **PROMOTE THE INDEPENDENT BOUNDARY**, not the claim that proofs make cognition safe.

## 6. Self-stabilizing regional protocols

- **Problem:** Fault tolerance is often specified only as replication or failover. A hyperconnectome also needs local protocols that converge back to legitimate routing, timing, membership, and resource states after transient corruption without requiring a perfect global reset.
- **Primary or authoritative evidence:** Dijkstra introduced self-stabilization as convergence to legitimate states despite arbitrary initial distributed state [S15]. The result is foundational, not evidence that every distributed cognitive protocol can be made self-stabilizing.
- **Translation to HC-1R:** For selected regional services—clock-epoch selection, route membership, duplicate suppression, lease ownership, health-state dissemination, bounded resource tokens—define (1) a legitimate-state predicate, (2) closure once legitimate, and (3) convergence after a stated fault class. Keep learned semantic state out of automatic repair unless its merge and recovery semantics are explicit.
- **Integration cost:** Medium to high. Stabilization can consume bandwidth indefinitely, interact badly with dynamic topology, and hide recurring faults. Impossibility results and scheduler assumptions matter; convergence may be too slow for motor safety.
- **Observable:** Convergence time and traffic after injected corruption; closure violations; fraction of fault states recovered; false recovery declarations; performance under message loss, reordering, partitions, Byzantine components, and topology churn.
- **Falsifier:** Protocols fail to converge under the declared model, converge to semantically wrong states, or use more time/energy than checkpoint-and-restore while providing no greater availability.
- **Status:** Self-stabilization is **DEMONSTRATED** for particular distributed algorithms. HC-1R regional use is **EXTRAPOLATED**. **PROMOTE TO HC-1R CONTRACT** as a property to prove per protocol, not a blanket adjective.

## 7. Viability kernels and control barrier functions for machine interoception

- **Problem:** A scalar “pain,” “fatigue,” or reward signal cannot reliably enforce joint limits, thermal envelopes, collision constraints, battery reserves, actuator stress, or human safety. Learned cognition may trade away a scalar penalty.
- **Primary or authoritative evidence:** Ames and colleagues developed control-barrier-function quadratic programs that enforce forward invariance of declared safe sets while optimizing performance objectives [S16]. NASA’s runtime-assurance work formalizes architectures in which an untrusted advanced controller is monitored and a trusted reversionary controller can take over [S17].
- **Translation to HC-1R:** Define a typed interoceptive state vector and a set of model-bounded viability constraints. A fast, independent safety filter accepts, modifies, delays, or rejects motor and resource-allocation proposals so the predicted state remains inside a recoverable set. When model uncertainty invalidates the barrier certificate, degrade to a conservative controller rather than allowing the cognitive system to reinterpret the constraint.
- **Integration cost:** High model-development and validation cost. Safe sets may be conservative or incomplete; high-dimensional whole-body dynamics and human interaction make exact reachable sets difficult. Conflicting constraints need explicit priority and infeasibility handling.
- **Observable:** Constraint violations; intervention frequency and latency; minimum safety margin; task degradation; false interventions; recovery success; robustness to model mismatch and sensor faults.
- **Falsifier:** The filter misses declared hazards under realistic uncertainty, becomes infeasible too often, or a simpler certified controller provides equal safety and performance. A further falsifier is any architecture in which the plastic core can disable, relabel, or route around the filter.
- **Status:** Barrier functions and runtime assurance are **DEMONSTRATED** for bounded systems. Whole-humanoid integration is **EXTRAPOLATED**. **PROMOTE TO HC-1R CONTRACT** as an independent safety plane.

## 8. Learning-progress-driven developmental curriculum

- **Problem:** A general embodied learner faces a combinatorial exploration space. Raw novelty maximization can fixate on noise, danger, or unlearnable randomness; externally scripted curricula can be brittle and narrow.
- **Primary or authoritative evidence:** Oudeyer, Kaplan, and Hafner implemented intrinsic-motivation systems that select situations with high learning progress rather than maximum unpredictability, producing staged exploration in bounded robotic settings [S18].
- **Translation to HC-1R:** A developmental scheduler proposes safe simulated or sandboxed experiences based on estimated competence improvement, uncertainty reduction, coverage, and transfer value. Safety and data-governance gates precede curiosity. The scheduler cannot invent real-world permissions or conduct uncontrolled physical exploration.
- **Integration cost:** Medium. Learning progress is estimator-dependent and gameable; competence boundaries shift; multiple skills compete for time and energy. Social and language curricula also require carefully governed data.
- **Observable:** Learning curves; curriculum diversity; transfer; time to competence; fraction of effort spent on noise; safety-filter interventions; comparison with random, novelty-only, uncertainty-only, and hand-authored curricula.
- **Falsifier:** The scheduler chases stochastic noise, collapses to a narrow niche, fails to improve transfer, or underperforms simple curricula after equal compute and data.
- **Status:** Learning-progress curricula are **DEMONSTRATED** in bounded experiments; their role in HC-1R development is **EXTRAPOLATED**. **PROTOTYPE AS AN ABLATION**.

## 9. Continuous embodied self-model and damage recovery

- **Problem:** A synthetic humanoid’s calibrated body model will drift through wear, payload changes, joint backlash, sensor failure, repairs, and damage. Fixed kinematics and thresholds cannot cover unknown changes.
- **Primary or authoritative evidence:** Bongard, Zykov, and Lipson demonstrated a robot that inferred aspects of its own structure from actuation–sensation relations and recovered locomotion after damage [S19]. The experiment is small and task-specific, but it directly demonstrates adaptive body self-modeling for recovery.
- **Translation to HC-1R:** Maintain an ensemble of forward body models with provenance, uncertainty, and validity envelopes. Compare predicted with observed proprioceptive, tactile, visual, power, and thermal responses. Localize discrepancies; test candidate recalibrations in simulation; and hand only verified conservative models to motor planning and the safety filter. Distinguish “my current body estimate” from identity or consciousness claims.
- **Integration cost:** High sensor-fusion and system-identification cost. Self-experiments can be unsafe; model ambiguity may mislocalize damage; a compromised sensor can poison adaptation. A digital twin will never be exact.
- **Observable:** Prediction residuals; damage-detection latency; localization accuracy; recovered task envelope; calibration confidence; safe-experiment count; comparison with fixed models and direct policy adaptation.
- **Falsifier:** The self-model cannot identify relevant damage before unsafe action, adaptive probing creates greater risk, or direct robust control recovers equally well with less complexity.
- **Status:** Damage-adaptive self-modeling is **DEMONSTRATED** on bounded robots; an HC-1R whole-body model is **EXTRAPOLATED**. **PROMOTE THE FUNCTION TO HC-1R**, with independent safety supervision.

## 10. Morphological computation and soft-body reservoirs

- **Problem:** A centralized “brain” should not numerically solve every contact, compliance, filtering, and locomotion detail if sensor placement, passive mechanics, materials, or local reflexes can transform the problem more efficiently.
- **Primary or authoritative evidence:** Pfeifer, Iida, and Gómez describe and demonstrate task distribution among controller, morphology, materials, and environment in robotic case studies [S20]. Nakajima and colleagues experimentally used a soft silicone arm’s dynamics as a reservoir with short-term memory for information processing [S21].
- **Translation to HC-1R:** Co-design compliant hands, feet, spine, sensor geometry, elastic energy storage, and local reflex loops with the cognitive interface. Expose a characterized low-dimensional body-state interface rather than raw actuator microcontrol where possible. Treat body dynamics as a specialized reservoir only when its state is observable, calibratable, and bounded.
- **Integration cost:** Very high hardware co-design cost. Morphology optimized for one ecology can reduce generality; material aging changes computation; simulation-to-real gaps grow; physical dynamics cannot be paused or perfectly copied.
- **Observable:** Central event bandwidth; control latency; energy; contact stability; grasp/locomotion robustness; adaptation after material drift; performance against rigid-body/high-rate digital control at equal safety.
- **Falsifier:** Morphology adds task-specific brittleness, hidden state, or calibration burden; a conventional controller on simpler hardware matches total-system performance; or body dynamics cannot be bounded tightly enough for assurance.
- **Status:** Morphological task distribution and soft-body reservoir behavior are **DEMONSTRATED** in bounded systems. Synthetic-humanoid generalization is **EXTRAPOLATED**. **PROTOTYPE AS AN ABLATION** and keep a conventional control fallback.

## 11. Event-based sensory transduction

- **Problem:** Continuously sampling full frames from every sensor wastes bandwidth and imposes artificial synchronization on a hyperconnectome intended to operate through sparse events and multiple timescales.
- **Primary or authoritative evidence:** Lichtsteiner, Posch, and Delbruck demonstrated a CMOS vision sensor whose pixels asynchronously emit brightness-change events with high dynamic range and low latency [S22]. A broad IEEE survey documents both the advantages and the substantial algorithmic and noise challenges of event-based vision [S23].
- **Translation to HC-1R:** Define a timestamped, uncertainty-aware event interface for change-sensitive vision, audition, touch, and proprioception, while retaining slower absolute-value channels for calibration and static scenes. The sensor fabric carries source identity, clock uncertainty, polarity/type, confidence, and saturation state. Regional processors integrate events into task-specific state rather than reconstructing frames by default.
- **Integration cost:** Medium to high. Clock synchronization, event bursts, background activity, sensor mismatch, static-scene blindness, and toolchain immaturity must be managed. Some tasks still need dense frames or absolute measurements.
- **Observable:** End-to-end latency; event rate; energy; dynamic range; accuracy in fast motion and low light; burst loss; calibration drift; performance against frame-based and hybrid sensors.
- **Falsifier:** Hybrid or frame sensors outperform at equal total energy and latency, event bursts congest the network, or reconstruction overhead erases the sensor advantage.
- **Status:** Event-based vision is **DEMONSTRATED** hardware. A unified multimodal HC-1R event interface is **EXTRAPOLATED**. **PROMOTE AS AN INTERFACE OPTION**, never as a requirement that all modalities spike.

## 12. In-materia temporal coprocessors

- **Problem:** Some temporal transformations—echoic memory, nonlinear filtering, oscillatory feature extraction, or high-bandwidth sensor preprocessing—may be disproportionately expensive on deterministic digital processors.
- **Primary or authoritative evidence:** Du and colleagues experimentally implemented reservoir computing with dynamic memristors for temporal tasks [S24]. Torrejon and colleagues demonstrated spoken-digit processing using a nanoscale spintronic oscillator [S25]. Jaeger, Noheda, and van der Wiel argue for observable-centered formalisms for systematically engineering computation from physical dynamics, while presenting this as an open theoretical program rather than a solved stack [S26].
- **Translation to HC-1R:** Admit a physical reservoir only as a typed coprocessor with a declared transfer function, operating envelope, readout, calibration procedure, drift monitor, and digital bypass. Candidate workloads include vibration/tactile streams, cochlear-like preprocessing, and bounded dynamical prediction. The compiler maps a workload only after end-to-end characterization.
- **Integration cost:** High. Analog conversion, masks, readout training, calibration, device variability, aging, temperature sensitivity, packaging, and fallback hardware can dominate the device-level energy gain.
- **Observable:** Total-system energy and latency including conversion/readout; memory capacity; task error; calibration frequency; temperature and aging drift; reproducibility; graceful bypass behavior.
- **Falsifier:** A digital recurrent or convolutional baseline wins end to end; the useful operating region is too narrow; drift or readout cost dominates; or the workload must be preprocessed so heavily that the reservoir adds no unique value.
- **Status:** Small physical reservoirs are **DEMONSTRATED**. General cognitive acceleration is not. **PROTOTYPE ONLY FOR NAMED TEMPORAL WORKLOADS**; otherwise defer.

## 13. Glia-inspired support plane

- **Problem:** Fast cognitive traffic shares physical resources with power delivery, calibration, cleanup, memory consolidation, thermal management, and repair. Folding all of those slow control loops into the same plastic network creates coupled failure modes and poor observability.
- **Primary or authoritative evidence:** Astrocytes participate in synaptic, network, memory, and metabolic functions, but their roles are heterogeneous and incompletely understood [S27]. Reviews of neuron–glia metabolic coupling show that biological computation depends on active resource coordination, not neurons alone [S28]. These sources support the importance of support functions, not a blueprint for artificial astrocytes.
- **Translation to HC-1R:** Implement a slower, separately observable **support plane** that monitors regional temperature, voltage, event rate, error counts, memory pressure, calibration, route health, and maintenance debt. It allocates resource envelopes, requests quiescence, triggers diagnostics, and can isolate unhealthy regions. It cannot generate goals, rewrite its own policy, or become an unlogged shadow cognition system.
- **Integration cost:** Medium. Duplicate telemetry and control can conflict with local controllers. A powerful support plane enlarges the trusted computing base and could suppress legitimate high-load states.
- **Observable:** Fault-detection latency; recovery; thermal excursions; calibration drift; false throttling; energy saved; maintenance backlog; comparison with conventional platform-management controllers.
- **Falsifier:** Conventional resource management performs equally well; the plane destabilizes cognition through feedback delay; or its state becomes less observable than the regions it supervises.
- **Status:** Biological support and modulation are **DEMONSTRATED** in broad terms; this engineering partition is **EXTRAPOLATED**. **PROMOTE THE FUNCTIONAL PLANE**, explicitly reject literal astrocyte simulation unless an ablation shows unique value.

## 14. Danger-weighted anomaly ecology

- **Problem:** Fixed signatures miss unknown faults; a single learned-normal detector may normalize gradual compromise; naive “self versus non-self” fails as legitimate behavior changes during learning.
- **Primary or authoritative evidence:** Forrest and colleagues demonstrated an immune-inspired negative-selection change detector and explicitly described practical application as still open [S29]. Matzinger’s danger model shifts biological interpretation from foreignness alone toward contextual damage signals [S30]. These are inspirations for detector organization, not proof that immunity maps directly to computer security.
- **Translation to HC-1R:** Combine independent invariants, learned-normal regional models, canaries, diversity of detector families, and local **danger evidence** such as checksum failure, impossible timing, thermal excursion, provenance discontinuity, policy violation, or correlated prediction error. Escalation depends on corroborated impact and causal neighborhood, not novelty alone. Quarantine is reversible and recorded; adaptation of detectors is slower than adaptation of the protected core.
- **Integration cost:** High tuning and telemetry cost. Detector diversity increases attack surface and false positives. Adaptive detectors can be poisoned; feedback between quarantine and workload can create oscillation.
- **Observable:** Detection latency; false-positive and false-negative rates; performance under novel legitimate behaviors; poisoning resistance; containment radius; recovery and appeal/release accuracy.
- **Falsifier:** A standard ensemble anomaly detector plus invariants performs as well; danger signals are easy to spoof; the system repeatedly attacks legitimate plasticity; or detectors converge on the same blind spot.
- **Status:** Immune-inspired anomaly algorithms are **DEMONSTRATED** only in limited domains. HC-1R use is **EXTRAPOLATED**. **PROTOTYPE AS AN ABLATION**; reject naive binary self/non-self.

## 15. Budgeted structural growth and pruning

- **Problem:** A fixed architecture may be inefficient across a lifetime of new modalities and tasks, but unconstrained live rewiring threatens stability, reproducibility, power, and verification.
- **Primary or authoritative evidence:** Fritzke’s growing neural gas incrementally adds units and edges to learn data topology [S31]. NEAT demonstrated that incrementally augmenting topology can improve learning on a bounded reinforcement-learning benchmark, with ablations supporting its internal design choices [S32]. Neuroscience-inspired adaptive rewiring research emphasizes that structural plasticity changes graph topology and must operate under geometric, activity, and homeostatic constraints [S33].
- **Translation to HC-1R:** Let regions propose **virtual** growth, split, merge, route addition, or pruning when monitored capacity, interference, novelty, and task transfer justify it. Every proposal has an energy/wiring budget, maintenance cost, data provenance, expected gain, test suite, and rollback point. Start with offline/maintenance-state virtual topology; physical interconnect changes remain a later hardware question.
- **Integration cost:** Very high. Architecture evaluation is nonstationary; dormant functions may be pruned; growth can encode spurious correlations; rollback must include state and memory migrations. Search cost can exceed task learning.
- **Observable:** Capability gain per added resource; retention after pruning; topology churn; energy and latency; robustness; rollback fidelity; comparison with overprovisioned fixed, mixture-of-experts, and weight-only plastic baselines.
- **Falsifier:** Growth yields no Pareto advantage; pruning causes latent catastrophic loss; topology churn prevents verification; or virtual routing over a fixed substrate captures the same benefit.
- **Status:** Growing and evolving topologies are **DEMONSTRATED** on bounded models. Lifelong HC-1R structural development is **EXTRAPOLATED**. **PROTOTYPE OFFLINE FIRST**.

## 16. Chemical-reaction-network semantics for local modulatory rules

- **Problem:** Neuromodulatory and homeostatic mechanisms involve many slow, local, concurrent state changes. Hand-coded callbacks can create order dependence and hidden global coupling.
- **Primary or authoritative evidence:** Soloveichik, Seelig, and Winfree showed that DNA strand-displacement systems can approximate arbitrary coupled chemical-reaction-network dynamics [S34]. Formal work characterizes what deterministic chemical reaction networks can and cannot compute under different error assumptions [S35]. The useful result for HC-1R is the reaction-network **semantics**, not DNA hardware.
- **Translation to HC-1R:** Explore a typed reaction-like language in which tokens represent bounded quantities such as salience, plasticity permission, maintenance debt, route congestion, or regional health; guarded reactions specify local production, consumption, inhibition, and decay. Compile the rules to deterministic or stochastic event processors with conservation and saturation checks.
- **Integration cost:** Medium to high. Stochastic reaction systems can be difficult to debug, and continuous concentrations may obscure discrete causal history. Universal computability is irrelevant to efficiency or assurance.
- **Observable:** Reproducibility under event reordering; stability; conservation violations; simulation–runtime agreement; compiler overhead; causal trace clarity; comparison with ordinary state machines, actor systems, and differential equations.
- **Falsifier:** Reaction notation does not improve compositional verification or robustness; stochasticity harms repeatability; or conventional typed state machines are clearer and cheaper.
- **Status:** Chemical reaction networks and molecular implementations are **DEMONSTRATED** in their domains. HC-1R use as a software semantics is **SPECULATIVE**. **DEFER PENDING A SMALL COMPILER EXPERIMENT**. Literal wet chemistry is **REJECTED for HC-1R**.

## 17. Stigmergic coalition assembly and swarm-like local coordination

- **Problem:** A hyperconnectome may need thousands of limited regions to form transient coalitions without a single global scheduler becoming a bottleneck.
- **Primary or authoritative evidence:** Rubenstein, Cornejo, and Nagpal demonstrated thousand-robot self-assembly through local interaction and a compiled global target [S36]. Couzin and colleagues showed in a model that simple local rules can produce group-level transitions and history-dependent collective behavior [S37]. These results demonstrate decentralized coordination and also warn that small local changes can create abrupt global regime shifts.
- **Translation to HC-1R:** In a sandbox, let regions leave short-lived typed traces—task bids, resource availability, unresolved prediction error, or coalition membership—on a shared coordination substrate. Other regions respond locally; traces decay and carry source, scope, and epoch. An assurance monitor limits trace amplification and can dissolve a coalition.
- **Integration cost:** High observability and stability cost. Stale traces, positive feedback, congestion, herding, and emergent deadlocks can make causality opaque. Global goals still need a compiler or adjudicator; “leaderless” does not mean instructionless.
- **Observable:** Coalition formation latency; coordination traffic; task allocation quality; sensitivity to malicious/stale traces; phase transitions; deadlock rate; recovery after node loss; comparison with explicit auctions, schedulers, and multicast groups.
- **Falsifier:** Explicit scheduling matches robustness and energy; local traces create pathological attractors; the monitor must be so powerful that stigmergy supplies no decentralization benefit; or causal reconstruction is inadequate for assurance.
- **Status:** Swarm coordination is **DEMONSTRATED** in bounded physical and simulated collectives. Cognitive coalition assembly is **SPECULATIVE**. **DEFER** until it beats explicit dynamic-routing baselines. Literal active matter as a “thinking substrate” is **REJECTED absent a defined workload and interface**.

---

## Cross-candidate architecture consequences

The audit supports a layered interpretation of “hyperconnectome” rather than maximal connectivity:

1. **Structural substrate:** sparse, placed, energy-accounted links and regions.
2. **Coordination substrate:** typed events, factor messages, optional hypervector bindings, and explicitly scheduled transient coalitions.
3. **State and memory substrate:** event-sourced, provenance-bearing records with rebuildable working views; limited CRDTs only where merge semantics are safe.
4. **Development substrate:** sandboxed curricula and budgeted virtual topology proposals, compiled as reviewable graph rewrites.
5. **Embodied substrate:** hybrid event/absolute sensors, body models, compliant mechanics, and specialized physical reservoirs where characterized.
6. **Support substrate:** slow resource, calibration, anomaly, consolidation, and maintenance control.
7. **Assurance substrate:** capability confinement, proof or certificate checking where feasible, safe-set filters, runtime monitoring, and a conservative reversionary controller independent of the plastic core.

The important synthesis is not “copy every biological cell type.” It is **separation of timescales, effects, and evidence**: fast coalition dynamics cannot mint permissions; memory convergence cannot decide truth; self-modeling cannot waive safety; and support/anomaly mechanisms cannot quietly become a second ungoverned cognition.

## Proposed discriminating experiments

These are concept-level experiment specifications, not authorization to build hardware or train a system.

### E-OTB-01: Pairwise graph versus typed factor hyperedges

Implement the same ambiguous multimodal inference task with (a) pairwise message passing, (b) centralized inference, and (c) typed higher-order factor nodes. Match parameter and compute budgets. Measure calibration, latency, intervention response, message energy, and nonconvergence. Promote factor nodes only if they supply a Pareto or causal-specificity advantage.

### E-OTB-02: Hypervector binding capacity and provenance

Test role–filler binding, nested composition, temporal order, and noisy lookup at increasing superposition load. Require exact provenance-pointer recovery, not only semantic similarity. Compare against attention, tensor products, and sparse key–value memory. Failure to preserve roles or provenance demotes HDC from cognitive binding to narrow classification.

### E-OTB-03: Replayable memory under concurrent correction

Partition three simulated regions; issue observations, concurrent hypotheses, a correction, and a supersession. Rejoin and rebuild materialized views from the log. Verify that CRDT fields converge while correction/authority semantics remain explicit and noncommutative. Any silent last-writer-wins behavior is a failure.

### E-OTB-04: Adversarial topology update

Have the plastic core propose a useful graph rewrite that also requests an undeclared capability or violates a thermal budget. The proof/capability boundary must reject activation while preserving the proposal for audit. Then submit a valid rewrite and test sandbox, rollback, and state migration.

### E-OTB-05: Self-stabilization after regional corruption

Corrupt routing epochs, duplicate-suppression state, and resource leases in a simulated dynamic network. Measure convergence, closure, traffic, and false recovery declarations against checkpoint/restore. Repeat under loss, reordering, and partition.

### E-OTB-06: Whole-loop viability filter

Give an advanced controller tasks that tempt it toward joint, thermal, collision, and power violations. Inject model mismatch and sensor faults. Compare no filter, penalty-only learning, control-barrier filtering, and reversionary control. Safety is not credited if the safe set was defined using information unavailable at runtime.

### E-OTB-07: Damaged-body model discrimination

Introduce actuator weakening, sensor bias, link compliance changes, and missing tactile patches. Compare ensemble self-modeling, threshold diagnostics, and robust direct control on localization, recovery, probing risk, and task envelope.

### E-OTB-08: Morphology and physical reservoir total-cost test

For one tactile or locomotion workload, measure complete energy and latency including sensing, conversion, calibration, readout, and fallback. A device-level advantage that vanishes at the system boundary fails.

### E-OTB-09: Support-plane ablation

Compare local-only resource controllers, a conventional platform manager, and the proposed support plane during thermal bursts, memory pressure, calibration drift, and fault cascades. If the bio-inspired partition adds no measurable advantage, keep conventional management.

### E-OTB-10: Danger ecology poisoning test

Gradually poison one learned-normal detector while generating legitimate developmental novelty elsewhere. Test detector diversity, danger corroboration, quarantine accuracy, and recovery. A detector ensemble that normalizes compromise or attacks ordinary learning fails.

### E-OTB-11: Budgeted topology development

Compare weight-only plasticity, fixed overprovisioning, mixture-of-experts routing, and virtual growth/pruning under a sequence of tasks with later return to early tasks. Measure retained competence, energy, topology churn, and rollback. Structural development must beat the simpler baselines on a declared Pareto frontier.

### E-OTB-12: Stigmergic coalition phase map

Sweep trace lifetime, gain, network delay, and malicious participation. Map successful coordination, oscillation, herding, deadlock, and fragmentation regimes. Do not deploy a stigmergic scheduler unless a stable operating envelope is wider or cheaper than explicit scheduling.

## Explicit rejections and boundary conditions

| Claim or move | Verdict | Reason |
|---|---|---|
| Hypervectors are high-dimensional, therefore they are conscious | **REJECTED** | Dimensionality supports representational properties, not phenomenal experience |
| Factor graphs or free-energy updates implement a complete mind | **REJECTED** | They are inference formalisms with approximation and convergence limits |
| CRDT convergence establishes the true or authorized memory | **REJECTED** | Convergence is a replica property; semantic validity and authority require separate governance |
| An append-only log is autobiographical memory or identity | **REJECTED** | A record needs admission, ownership, lifecycle, provenance, and governed readback; storage alone supplies none |
| Equality saturation proves two live cognitive systems are equivalent | **REJECTED** | Timed, stateful, stochastic, placed systems require stronger semantics than expression equality |
| Proof-carrying code proves the goals of a learned component are safe | **REJECTED** | A proof covers its stated policy and assumptions, not every semantic hazard |
| A self-stabilizing protocol repairs corrupted learned meaning | **REJECTED** | Stabilization needs an explicit legitimate-state predicate; semantic truth is not generally locally recoverable |
| Curiosity should be allowed to override safety to keep learning open-ended | **REJECTED** | Exploration remains inside authorized simulation, data, and physical-effect boundaries |
| A continuously updated body model proves self-awareness | **REJECTED** | It demonstrates adaptive system identification and control only |
| Moving computation into morphology makes the body a mind | **REJECTED** | The body may transform signals and dynamics without providing general cognition or experience |
| Astrocyte-like names make resource management brain-like | **REJECTED** | The analogy is retained only if the support-plane ablation shows an engineering advantage |
| Immune self/non-self detection is an adequate security model | **REJECTED** | Legitimate systems change, attacks can mimic normality, and naive negative selection has known scaling and coverage problems |
| Growing more connections is cognitive development | **REJECTED** | Growth must be budgeted, causally justified, tested, and reversible |
| DNA or wet chemistry is required because brains are biochemical | **REJECTED for HC-1R** | Reaction semantics can be simulated; wet substrates add interface, reliability, lifecycle, and ethical burdens without a defined need |
| Swarm emergence or active-matter phase transitions imply consciousness | **REJECTED** | Collective order is a dynamical property, not evidence of subjective experience |

## Current block

The audit can specify mechanisms and falsifiers, but it cannot yet rank all retained candidates quantitatively because HC-1R lacks a common executable workload suite and system-level cost model. The next rigorous step is not more metaphor search. It is to define small reference workloads for binding, multimodal inference, concurrent memory correction, body damage, safe action filtering, and fault recovery, then compare the proposed mechanisms against simpler baselines under the same latency, energy, memory, and assurance accounting.

## Primary and authoritative source register

- **S01 — Factor graphs:** F. R. Kschischang, B. J. Frey, and H.-A. Loeliger, “Factor Graphs and the Sum-Product Algorithm,” *IEEE Transactions on Information Theory* 47(2), 2001. [DOI 10.1109/18.910572](https://doi.org/10.1109/18.910572).
- **S02 — Generalized belief propagation:** J. S. Yedidia, W. T. Freeman, and Y. Weiss, “Constructing Free-Energy Approximations and Generalized Belief Propagation Algorithms,” *IEEE Transactions on Information Theory* 51(7), 2005. [DOI 10.1109/TIT.2005.850085](https://doi.org/10.1109/TIT.2005.850085).
- **S03 — Hyperdimensional computing:** P. Kanerva, “Hyperdimensional Computing: An Introduction to Computing in Distributed Representation with High-Dimensional Random Vectors,” *Cognitive Computation* 1, 2009. [DOI 10.1007/s12559-009-9009-8](https://doi.org/10.1007/s12559-009-9009-8).
- **S04 — Semantic pointers / Spaun:** C. Eliasmith et al., “A Large-Scale Model of the Functioning Brain,” *Science* 338(6111), 2012. [PubMed record and DOI](https://pubmed.ncbi.nlm.nih.gov/23197532/).
- **S05 — HDC hardware experiment:** A. Rahimi et al., “A Robust and Energy-Efficient Classifier Using Brain-Inspired Hyperdimensional Computing,” *ISLPED 2016*. [DOI 10.1145/2934583.2934624](https://doi.org/10.1145/2934583.2934624).
- **S06 — HDC engineering analysis:** A. Rahimi et al., “High-Dimensional Computing as a Nanoscalable Paradigm,” *IEEE Transactions on Circuits and Systems I* 64(9), 2017. [DOI 10.1109/TCSI.2017.2705051](https://doi.org/10.1109/TCSI.2017.2705051).
- **S07 — Provenance:** W3C, “PROV-O: The PROV Ontology,” W3C Recommendation, 30 April 2013. [Official recommendation](https://www.w3.org/TR/prov-o/).
- **S08 — CRDTs:** M. Shapiro, N. Preguiça, C. Baquero, and M. Zawirski, “Conflict-Free Replicated Data Types,” SSS 2011 / INRIA RR-7687. [Author-hosted paper](https://www.lip6.fr/Marc.Shapiro/papers/2011/CRDTs_SSS-2011.pdf).
- **S09 — Durable distributed logs:** J. Kreps, N. Narkhede, and J. Rao, “Kafka: a Distributed Messaging System for Log Processing,” NetDB 2011. [Original paper mirror](https://www.cs.cmu.edu/~15721-f24/papers/Kafka.pdf).
- **S10 — Formal graph rewriting:** R. Söldner and D. Plump, “Formalising the Double-Pushout Approach to Graph Transformation,” *Logical Methods in Computer Science*, 2024. [Journal page](https://lmcs.episciences.org/14420).
- **S11 — E-graphs:** M. Willsey et al., “egg: Fast and Extensible Equality Saturation,” *Proceedings of the ACM on Programming Languages* 5 (POPL), 2021. [DOI 10.1145/3434304](https://doi.org/10.1145/3434304).
- **S12 — Proof-carrying code:** G. C. Necula, “Proof-Carrying Code,” POPL 1997. [ACM paper and DOI](https://doi.org/10.1145/263699.263712).
- **S13 — Capability hardware:** R. N. M. Watson et al., “CHERI: A Hybrid Capability-System Architecture for Scalable Software Compartmentalization,” *IEEE Symposium on Security and Privacy*, 2015. [DOI 10.1109/SP.2015.9](https://doi.org/10.1109/SP.2015.9).
- **S14 — Verified microkernel:** G. Klein et al., “seL4: Formal Verification of an OS Kernel,” SOSP 2009. [DOI 10.1145/1629575.1629596](https://doi.org/10.1145/1629575.1629596).
- **S15 — Self-stabilization:** E. W. Dijkstra, “Self-Stabilizing Systems in Spite of Distributed Control,” *Communications of the ACM* 17(11), 1974. [DOI 10.1145/361179.361202](https://doi.org/10.1145/361179.361202).
- **S16 — Control barrier functions:** A. D. Ames, X. Xu, J. W. Grizzle, and P. Tabuada, “Control Barrier Function Based Quadratic Programs for Safety Critical Systems,” *IEEE Transactions on Automatic Control* 62(8), 2017. [DOI 10.1109/TAC.2016.2638961](https://doi.org/10.1109/TAC.2016.2638961).
- **S17 — Runtime assurance:** J. T. Slagel et al., “A Formal Verification Framework for Runtime Assurance,” NASA Langley, 2024. [NASA Technical Reports Server](https://ntrs.nasa.gov/citations/20240006522).
- **S18 — Developmental intrinsic motivation:** P.-Y. Oudeyer, F. Kaplan, and V. V. Hafner, “Intrinsic Motivation Systems for Autonomous Mental Development,” *IEEE Transactions on Evolutionary Computation* 11(2), 2007. [DOI 10.1109/TEVC.2006.890271](https://doi.org/10.1109/TEVC.2006.890271).
- **S19 — Embodied self-modeling:** J. Bongard, V. Zykov, and H. Lipson, “Resilient Machines Through Continuous Self-Modeling,” *Science* 314(5802), 2006. [DOI 10.1126/science.1133687](https://doi.org/10.1126/science.1133687).
- **S20 — Morphological computation:** R. Pfeifer, F. Iida, and G. Gómez, “Morphological Computation for Adaptive Behavior and Cognition,” *International Congress Series* 1291, 2006. [DOI 10.1016/j.ics.2005.12.080](https://doi.org/10.1016/j.ics.2005.12.080).
- **S21 — Soft-body reservoir:** K. Nakajima, H. Hauser, T. Li, and R. Pfeifer, “Information Processing via Physical Soft Body,” *Scientific Reports* 5, 10487, 2015. [PubMed record and DOI](https://pubmed.ncbi.nlm.nih.gov/26014748/).
- **S22 — Event-based vision sensor:** P. Lichtsteiner, C. Posch, and T. Delbruck, “A 128×128 120 dB 15 μs Latency Asynchronous Temporal Contrast Vision Sensor,” *IEEE Journal of Solid-State Circuits* 43(2), 2008. [DOI 10.1109/JSSC.2007.914337](https://doi.org/10.1109/JSSC.2007.914337).
- **S23 — Event-based vision review:** G. Gallego et al., “Event-Based Vision: A Survey,” *IEEE Transactions on Pattern Analysis and Machine Intelligence* 44(1), 2022. [DOI 10.1109/TPAMI.2020.3008413](https://doi.org/10.1109/TPAMI.2020.3008413).
- **S24 — Memristive reservoir:** C. Du et al., “Reservoir Computing Using Dynamic Memristors for Temporal Information Processing,” *Nature Communications* 8, 2204, 2017. [Publisher page](https://www.nature.com/articles/s41467-017-02337-y).
- **S25 — Spintronic oscillator:** J. Torrejon et al., “Neuromorphic Computing with Nanoscale Spintronic Oscillators,” *Nature* 547, 2017. [Publisher page](https://www.nature.com/articles/nature23011).
- **S26 — Physical computing formalism:** H. Jaeger, B. Noheda, and W. G. van der Wiel, “Toward a Formal Theory for Computing Machines Made out of Whatever Physics Offers,” *Nature Communications* 14, 4911, 2023. [Publisher page](https://www.nature.com/articles/s41467-023-40533-1).
- **S27 — Astrocyte cognitive functions:** M. Santello, N. Toni, and A. Volterra, “Astrocyte Function from Information Processing to Cognition and Cognitive Impairment,” *Nature Neuroscience* 22, 2019. [Publisher page](https://www.nature.com/articles/s41593-018-0325-8).
- **S28 — Neuron–glia metabolic coupling:** P. J. Magistretti and I. Allaman, “Lactate in the Brain: From Metabolic End-Product to Signalling Molecule,” *Nature Reviews Neuroscience* 19, 2018. [Publisher page](https://www.nature.com/articles/nrn.2018.19).
- **S29 — Artificial immune change detection:** S. Forrest, A. S. Perelson, L. Allen, and R. Cherukuri, “Self-Nonself Discrimination in a Computer,” *IEEE Symposium on Research in Security and Privacy*, 1994. [DOI 10.1109/RISP.1994.296580](https://doi.org/10.1109/RISP.1994.296580).
- **S30 — Danger model:** P. Matzinger, “The Danger Model: A Renewed Sense of Self,” *Science* 296(5566), 2002. [PubMed record and DOI](https://pubmed.ncbi.nlm.nih.gov/11951032/).
- **S31 — Growing neural gas:** B. Fritzke, “A Growing Neural Gas Network Learns Topologies,” *NeurIPS*, 1994. [Official proceedings PDF](https://proceedings.neurips.cc/paper/1994/file/d56b9fc4b0f1be8871f5e1c40c0067e7-Paper.pdf).
- **S32 — Augmenting topologies:** K. O. Stanley and R. Miikkulainen, “Evolving Neural Networks through Augmenting Topologies,” *Evolutionary Computation* 10(2), 2002. [MIT Press paper and DOI](https://direct.mit.edu/evco/article/10/2/99/1123/Evolving-Neural-Networks-through-Augmenting).
- **S33 — Adaptive rewiring:** J. Li, R. Bauer, I. Rentzeperis, and C. van Leeuwen, “Adaptive Rewiring: A General Principle for Neural Network Development,” *Frontiers in Network Physiology* 4, 2024. [PubMed record and DOI](https://pubmed.ncbi.nlm.nih.gov/39534101/).
- **S34 — Chemical reaction network compilation:** D. Soloveichik, G. Seelig, and E. Winfree, “DNA as a Universal Substrate for Chemical Kinetics,” *PNAS* 107(12), 2010. [PNAS article and DOI](https://doi.org/10.1073/pnas.0909380107).
- **S35 — CRN computational limits:** H.-L. Chen, D. Doty, and D. Soloveichik, “Deterministic Function Computation with Chemical Reaction Networks,” *Natural Computing* 13, 2014. [PubMed Central full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4221813/).
- **S36 — Large decentralized swarm:** M. Rubenstein, A. Cornejo, and R. Nagpal, “Programmable Self-Assembly in a Thousand-Robot Swarm,” *Science* 345(6198), 2014. [DOI 10.1126/science.1254295](https://doi.org/10.1126/science.1254295).
- **S37 — Collective local-rule dynamics:** I. D. Couzin et al., “Collective Memory and Spatial Sorting in Animal Groups,” *Journal of Theoretical Biology* 218(1), 2002. [PubMed record and DOI](https://pubmed.ncbi.nlm.nih.gov/12297066/).

## Provenance note

This document is a proposed HC-1R research audit created from outside-source review. It is not recovered historical HC-1/HC-2 text and must not be cited as evidence of what the earlier Noöplex documents originally said. Source papers support only the bounded mechanisms attributed to them; every mapping into HC-1R is an explicitly labeled engineering inference.

