# HC-1R Physical Substrate Feasibility

**Status:** research memo; no fabrication, procurement, deployment, model training, or protected effect is authorized  
**Evidence reviewed through:** 2026-08-19  
**System question:** Can a dynamically reconfigurable Noöplex "hyperconnectome" be realized as a physically credible cognition substrate, including body-scale sensorimotor I/O, without treating component demonstrations as evidence of cognition or consciousness?

## Executive finding

**A research-scale HC-1R is physically plausible as a heterogeneous, mostly digital system whose logical connectivity is dynamically remapped over fixed physical interconnects. It is not presently credible as a densely all-to-all, physically rewiring, body-integrated brain.**

The defensible near-term substrate is:

1. digital event-driven or spatial compute tiles with local SRAM;
2. a sparse multicast network-on-chip and chip-to-chip fabric;
3. a versioned control plane that implements structural plasticity by changing routing and synapse tables, not wires;
4. conventional memory for durable state, checkpoints, provenance, and recovery;
5. optional analog in-memory, physical-reservoir, photonic, or spintronic islands only for workloads on which their complete systems beat digital baselines;
6. event-driven sensors and local safety/reflex controllers at the body edge; and
7. quantum processors, if ever useful, as asynchronous external services with no real-time or continuity-critical responsibility.

The largest directly relevant digital demonstration is Intel's six-rack-unit Hala Point research system: 1,152 Loihi 2 processors, capacity for 1.15 billion modeled neurons and 128 billion synapses, and a maximum power of 2.6 kW. This proves that large sparse event fabrics can be assembled; it does not prove brain equivalence, general cognition, or body-portable power. [Intel Hala Point](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai)

The principal feasibility boundary is therefore not a transistor count. It is whether useful computation remains sparse and local enough that routing, memory traffic, topology churn, calibration, cooling, observability, and failure recovery fit inside explicit budgets.

## Classification and claim boundary

This memo uses the project classes:

- **DEMONSTRATED:** a cited device or system directly performed the stated component function at the stated scale.
- **EXTRAPOLATED:** the ingredients exist, but their HC-1R combination, scale, reliability, or cognitive role has not been demonstrated.
- **SPECULATIVE:** a key mechanism, scale, or advantage is presently unsupported.
- **REJECTED:** the candidate depends on a false physical premise, lacks a defined workload, or loses its proposed benefit when complete-system costs are counted.

All neuron, synapse, node, TOPS, and bandwidth figures are engineering capacities under particular abstractions. None is a measure of intelligence, personal identity, phenomenal consciousness, or moral status.

### Provenance and proposal legend

Sources and recommendations are deliberately kept distinct:

| Label | Meaning in this memo |
|---|---|
| **CURRENT SOURCE — peer reviewed** | A result reported in a linked peer-reviewed paper and checked during the 2026-08-19 web review. It remains bounded to that paper's device, workload, measurement boundary, and date. |
| **CURRENT SOURCE — official technical/vendor** | A specification or product/research-system claim from the responsible organization. It is useful primary evidence for configuration and interface facts, but is not independent validation of performance. |
| **SYNTHESIS / INFERENCE** | An engineering conclusion drawn from multiple sources. It is not itself a reported experimental result. |
| **HC-1R PROPOSAL** | A candidate architecture, control rule, safety boundary, or integration choice introduced by this memo. It has not been demonstrated as an HC-1R system. |
| **PROPOSED TEST / FALSIFIER** | A validation or rejection criterion for future simulation or hardware-in-loop work; it is not a completed experiment. |

In the candidate matrix, **Demonstrated scale and evidence** contains current-source claims and direct URLs; **Plausible HC-1R role** and **Main integration gap** are synthesis/proposal; **Observable test** and **Falsifier** are proposed tests. In the detailed sections, reported numbers and named demonstrations are current-source claims when linked, paragraphs headed **Integration decision** are HC-1R proposals, and all stages in the validation ladder are HC-1R proposals. Unqualified design language such as “should” or “use” is therefore a recommendation, never a claim that the integrated system exists.

## The minimum physically coherent interpretation of “hyperconnectome”

A literal implementation of every possible pairwise or higher-order connection is not scalable. HC-1R should instead represent a time-varying sparse multilayer hypergraph in software and compile it onto fixed hardware:

- ordinary directed edges become entries in local synapse or routing tables;
- a one-to-many edge becomes a multicast route;
- a higher-order interaction becomes a factor node, shared stateful process, or topic with an explicit aggregation rule;
- temporary binding becomes a leased route or short-lived shared workspace;
- structural plasticity becomes an atomic change to an address, route, allocation, or factor-node membership;
- slow consolidation changes the durable graph only after validation;
- failed or overheated tiles are removed from the logical graph and their state is restored elsewhere.

This interpretation preserves a testable form of dynamic effective connectivity without claiming impossible dynamic metal wiring. The control plane should apply topology changes in numbered epochs: prepare, validate resource and safety constraints, instantiate shadow routes, quiesce affected edges, atomically commit, verify, and retain a rollback point. A half-applied graph must never be treated as a valid cognitive state.

The [Neuromorphic Intermediate Representation](https://www.nature.com/articles/s41467-024-52259-9) (NIR) demonstrates that three spiking graphs can be represented and reproduced across seven simulators and four digital neuromorphic platforms. That is strong evidence for a substrate-neutral graph layer. It also exposes a limit: platform discretization and semantics still differ, so HC-1R needs conformance tests for state trajectories and timing, not just successful compilation.

## Candidate substrate matrix

| Mechanism | Demonstrated scale and evidence | Plausible HC-1R role | Main integration gap | Observable test | Falsifier | Epistemic class |
|---|---|---|---|---|---|---|
| Digital event-driven neuromorphic tiles | Loihi 2: up to 1 million modeled neurons, 120 million synapses, 128 neural cores, 192 KB/core; Hala Point: 1,152 chips, 1.15 billion neurons, 128 billion synapses, 2.6 kW. [Loihi 2 brief](https://download.intel.com/newsroom/2021/new-technologies/neuromorphic-computing-loihi-2-brief.pdf), [Hala Point](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai) | Primary sparse temporal/event substrate; online local rules; sensor-stream processing | Useful general algorithms, mapping, traffic hotspots, tooling, deterministic recovery, and fair full-system comparison | Matched-task quality, p50/p99 latency, joules per completed task, event sparsity, route occupancy, topology-update cost | No repeatable end-to-end energy-delay gain over a tuned digital baseline at matched quality, or traffic becomes dense enough to saturate the fabric | DEMONSTRATED as hardware; EXTRAPOLATED as HC-1R core |
| Digital spatial compute with local SRAM | IBM NorthPole eliminated off-chip model-memory access and reported 25x FPS/W and 22x lower latency than a comparable-node GPU on ResNet-50; Cerebras WSE-3 exposes 900,000 active cores and 44 GB on-chip SRAM. [NorthPole paper](https://research.ibm.com/publications/neural-inference-at-the-frontier-of-energy-space-and-time), [WSE-3](https://www.cerebras.ai/chip) | Dense kernels, graph compilation, global workspace, checkpoints, and control-plane compute near memory | Model capacity, programming restrictions, external-memory spill, power/cooling, vendor-specific toolchains | Working-set residency, local/remote byte ratio, stall time, full-card energy, remap time after a disabled tile | Benefit disappears when real state, I/O, checkpointing, and model spill are included | DEMONSTRATED for specialized compute; EXTRAPOLATED for cognition |
| Mixed-signal analog neuromorphic dynamics | BrainScaleS-2: 512 analog neuron compartments, 131,072 synapses, 256 synapses/neuron, two embedded plasticity processors, about 1,000x biological time. [BrainScaleS-2](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full) | Fast dynamical microcircuits, accelerated learning experiments, dendritic or attractor kernels | Per-device calibration, mismatch, limited fan-in, small scale, difficult cross-system timing, jitter-sensitive interconnect | Parameter-identification residual, device-to-device trajectory error, recalibration time, cross-temperature task quality | Hardware-in-loop training and calibration cannot hold a preregistered trajectory/task tolerance over devices, days, and temperatures | DEMONSTRATED at single-chip scale; EXTRAPOLATED as a tiled subsystem |
| RRAM/PCM analog in-memory compute | NeuRRAM: 48 cores, each with 256 x 256 RRAM cells, about 3 million devices. IBM analog-AI: 35 million PCM devices in 34 tiles, up to 12.4 TOPS/W sustained; a 45-million-weight speech model used five chips and more than 140 million PCM devices. [NeuRRAM](https://www.nature.com/articles/s41586-022-04992-8), [IBM analog-AI](https://research.ibm.com/publications/an-analog-ai-chip-for-energy-efficient-speech-recognition-and-transcription) | Bounded matrix-vector kernels, read-mostly associative transforms, fixed experts | ADC/DAC and communication overhead, finite precision, programming cost, endurance, temperature, drift, training and update asymmetry | Wall-plug energy including converters and host, accuracy over time, program pulses/update, calibration duty cycle, thermal sensitivity | Less than a meaningful end-to-end advantage after peripherals, or required plasticity exceeds endurance/calibration budgets | DEMONSTRATED for inference kernels; EXTRAPOLATED as bounded accelerator; SPECULATIVE as primary plastic memory |
| Virtual structural plasticity | BrainScaleS-2 changes synapse-local source addresses and demonstrated an on-chip structural-plasticity algorithm with fixed fan-in on a simple supervised task. [Structural plasticity experiment](https://doi.org/10.1016/j.neunet.2020.09.024) | Sparse edge birth/death, module reassignment, temporary assemblies, resource reclamation | Atomic multi-tile updates, stability, credit assignment, route-table pressure, state migration, audit and rollback | Improvement over weight-only learning under equal compute/memory; churn rate; route-table occupancy; commit latency; rollbacks; instability events | Topology change adds no quality/robustness benefit, or churn causes congestion, forgetting, oscillation, or unbounded metadata | DEMONSTRATED in a small fixed-fan-in system; EXTRAPOLATED at HC-1R scale |
| Memristive/nanowire physical reservoirs | Self-organizing nanowire networks demonstrate nonlinear dynamics and fading memory; MEMSORN used measured CMOS/RRAM device statistics to improve a sequence task by more than 15% over its random-network baseline. [Nanowire reservoir](https://www.nature.com/articles/s41563-021-01099-9), [MEMSORN](https://www.nature.com/articles/s41467-022-33476-6) | Low-power temporal feature extraction near sensors; stochastic or novelty kernels | Small tasks, external readout/training, device variability, poor observability, transfer between specimens, unclear scaling | Same-device and cross-device accuracy over weeks/temperature; transducer-inclusive energy; linear-probe capacity; perturbation response | A tuned digital reservoir with the same observable state count matches or beats it once readout, reset, calibration, and training are included | DEMONSTRATED for small reservoirs; EXTRAPOLATED as peripheral island |
| Photonic compute/reservoir | A 2024 silicon photonic reservoir used a 2 mm2 passive core, experimentally operated above 60 GHz, and obtained NARMA10 NMSE 0.107 with 45 output nodes. A 2025 hybrid accelerator implemented a 64 x 64 optical MAC with more than 16,000 photonic components and four external lasers. [Photonic reservoir](https://www.nature.com/articles/s41467-024-55172-3), [PACE](https://www.nature.com/articles/s41586-025-08786-6) | Ultra-low-latency linear transform, optical-domain signal processing, specialized reservoir | Laser wall-plug power, modulators, detectors, ADC/DAC/TIA, thermal phase drift, calibration, 4-8 bit practical precision, memory and nonlinearity | Full-system joules/inference, accuracy versus temperature/time, reprogram latency, calibration duty, converter and laser share | Core-only advantage vanishes at the wall plug, or useful precision/size requires more control energy and area than digital | DEMONSTRATED at small/specialized scale; EXTRAPOLATED for bounded kernels |
| Photonic interconnect | A 2025 3D electronic-photonic link demonstrated 80 channels, 800 Gb/s aggregate, 5.3 Tb/s/mm2, and front-end energies of 50 fJ/bit TX plus 70 fJ/bit RX at 10 Gb/s/channel. [3D photonic interconnect](https://www.nature.com/articles/s41566-025-01633-0) | Chiplet, board, or rack links where electrical reach and bandwidth dominate | Lasers, packaging, fibre attach, control, link reliability, traffic burst handling, protocol overhead | End-to-end pJ/bit, bandwidth density, BER, latency, thermal drift, serviceability | No energy/bandwidth-density benefit at the actual reach after laser and protocol overhead, or recovery cannot meet system requirements | DEMONSTRATED component link; EXTRAPOLATED HC-1R fabric |
| Spintronic oscillators, skyrmions, and nanomagnets | Spoken digits were demonstrated with one time-multiplexed spin-torque oscillator; vowels with four coupled oscillators. A skyrmion reservoir used one 150 x 900 micrometre Hall bar and 50 time-multiplexed virtual nodes with 0.1 s input intervals. [Single oscillator](https://www.nature.com/articles/nature23011), [four oscillators](https://arxiv.org/abs/1711.02704), [skyrmion reservoir](https://www.nature.com/articles/s41467-023-39207-9) | Compact nonlinear dynamics, samplers, oscillator-based binding experiments, niche reservoirs | Arrays, reproducible coupling, readout, bias power, fabrication variation, temperature, peripheral electronics, fair baseline | Performance and energy of a physically coupled 64-plus-device array across chips/temperatures, including readout | Time multiplexing or electronics perform most of the computation, or array variability prevents reproducible task transfer | DEMONSTRATED for single/few-device experiments; SPECULATIVE at useful HC-1R scale |
| Chiplets, 2.5D/3D integration, and multicast NoC | UCIe 3.0 specifies 48/64 GT/s links, runtime recalibration, priority sideband events, fast throttle, and emergency shutdown; Hala Point reports 3.5 PB/s inter-core and 5 TB/s inter-chip bandwidth. [UCIe specifications](https://www.uciexpress.org/specifications), [Hala Point](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai) | Heterogeneous assembly, fault domains, local-memory tiles, management and safety sideband, sparse event multicast | Bisection bandwidth, hotspot traffic, link/protocol energy, package yield, thermal coupling, power delivery, cross-vendor semantics | Traffic sweeps with real fan-out distributions; p99 latency; drops; route-table use; per-link energy; hotspot and throttling maps | Claimed connectivity only works at low average load, bursts violate deadlines, or 3D thermal throttling removes density benefit | DEMONSTRATED standards/components; EXTRAPOLATED as integrated HC-1R package |
| Body-scale event sensorimotor interface | Sony IMX636 event vision: 1,280 x 720, up to 1.06 Gevents/s and less than 100 microseconds ROI latency at 1 klux. DAVIS346: 346 x 260, up to 12 Mevents/s, under 180 mA at 5 V. A 2024 tactile system demonstrated first-spike timing for rapid object classification. [Sony EVS](https://www.sony-semicon.com/en/products/is/industry/evs.html), [DAVIS346](https://docs.inivation.com/_static/hardware_guides/davis346.pdf), [neuromorphic tactile system](https://pubmed.ncbi.nlm.nih.gov/38723082/) | Sparse vision, tactile, auditory, proprioceptive, and internal-state events; local reflex loops | Coverage, cabling, synchronization, burst rates, calibration, durability, privacy, sensor failure, actuator safety, ground truth | Sensor-to-actuator p99 latency/jitter, event burst envelope, clock error, packet loss, local-reflex availability, safe-stop time | Saturating scenes or damage defeat rate control; single faults create unsafe commands; cognition path is required for emergency stop | DEMONSTRATED per sensor/prototype; EXTRAPOLATED body-wide |
| External quantum service | Rigorous work shows that training data can make classical learners competitive even on quantum-generated problems; D-Wave scaling beat simulated annealing on one family but did not establish quantum speedup. [Power of data in QML](https://www.nature.com/articles/s41467-021-22539-9), [quantum annealer benchmark](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.031016) | Optional offline quantum simulation or sharply defined optimization, never the continuous cognitive loop | Encoding and readout, queue/network latency, noise/error mitigation, weak classical baselines, cost, reproducibility | End-to-end wall clock, energy/cost, solution quality, scaling, and confidence interval against the best known tuned classical methods | Advantage disappears when loading, queueing, readout, mitigation, embedding, and equally tuned classical baselines are counted | REJECTED as a required substrate; SPECULATIVE as an optional service |

## Detailed feasibility assessment

### 1. Digital neuromorphic and local-memory systems should carry the architectural burden

Digital substrates currently provide the best combination of scale, programmability, observability, deterministic state transfer, and fault isolation.

Loihi 2 directly supports graded event payloads, programmable neuron models, third-factor learning traces, on-the-fly state monitoring, sparse connection formats, external AER/SPI/Ethernet interfaces, and 3D tile arrangements. Those features are unusually well aligned with a versioned dynamic graph. They still do not remove physical fan-in, memory, or network limits. [Loihi 2 brief](https://download.intel.com/newsroom/2021/new-technologies/neuromorphic-computing-loihi-2-brief.pdf)

Hala Point's scale is encouraging, but its 2.6 kW maximum power places it in the lab/rack class. Its headline 1.15-billion-neuron capacity is not a portable-body envelope. Its high aggregate bandwidth also does not guarantee adequate bisection bandwidth or tail latency for arbitrary graph traffic.

IBM NorthPole and Cerebras show a complementary lesson: putting compute near local SRAM and using explicit spatial dataflow can reduce data movement dramatically. NorthPole's published results are for low-precision neural inference, not a continually learning recurrent system. Cerebras's WSE-3 is vendor-reported at 900,000 active cores, 44 GB SRAM, and 21 PB/s memory bandwidth; its redundant cores and routes demonstrate a useful fail-in-place pattern, but the system is specialized, datacenter-class, and not neuromorphic. [NorthPole](https://research.ibm.com/publications/neural-inference-at-the-frontier-of-energy-space-and-time), [Cerebras architecture](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem)

**Integration decision:** use digital tiles as the authoritative state holder. Analog or physical devices may provide observations or accelerations, but a digital shadow records configuration, topology epoch, calibration state, and recoverable weights where required.

**Promotion test:** across at least three preregistered streaming workloads, a candidate digital neuromorphic mapping must preserve task quality and beat a tuned CPU/GPU/MCU/FPGA comparison on complete-system energy-delay product, with all host preprocessing and I/O included. [NeuroBench](https://www.nature.com/articles/s41467-025-56739-4) supplies a useful measurement discipline, but HC-1R must add graph-churn, persistence, fault, and sensorimotor tests.

### 2. Analog in-memory compute is an accelerator, not trustworthy canonical memory

Analog crossbars are compelling because Kirchhoff summation performs many multiply-accumulates where weights reside. NeuRRAM and IBM's PCM systems demonstrate that useful multi-core chips are real, not merely device simulations. The evidence is strongest for read-mostly inference and bounded models.

The same literature provides a direct warning. In one PCM ResNet-32 experiment, accuracy was 93.75% 25 seconds after programming, but without drift compensation it fell to chance-level 10% after roughly 1,000 seconds. Global compensation retained more than 92.6% for one day. This is model- and device-specific, but it demonstrates why an unmonitored analog state cannot be treated as durable truth. [PCM drift experiment](https://www.nature.com/articles/s41467-020-16108-9)

A 2025 ALBERT demonstration mapped 7.1 million unique weights onto 28.3 million PCM devices. Uncompensated accuracy degraded by roughly 5% over 30 days; recalibration reduced the loss to under 1%. That is meaningful progress, and it still requires calibration data, digital arithmetic, and access to ground truth. [ALBERT on analog PCM](https://www.nature.com/articles/s41467-025-63794-4)

**Integration decision:** restrict PCM/RRAM arrays to explicitly typed numerical state. Keep semantic records, authority, safety rules, topology commits, and rollback metadata in error-checked digital memory. Use program-and-verify, reference cells, periodic calibration, hardware-aware training, and a per-array validity interval.

**Accelerated-life falsifier:** subject a candidate array/model to target-equivalent write counts, temperature cycles, power interruptions, idle aging, and read disturb. If quality or calibration cost crosses its preregistered bound before the planned service interval, or if the energy consumed by conversion and calibration removes the system advantage, it is not an HC-1R production candidate.

### 3. Structural plasticity should be virtual, sparse, rate-limited, and reversible

BrainScaleS-2 shows the important mechanism: each synapse has a local source address, so changing an address changes the effective connectome while the physical array stays fixed. Its published structural-plasticity experiment continuously rewired partners while keeping fan-in constant. That is a real mechanism, but only a small supervised example.

HC-1R should separate at least three time scales:

- **fast gating:** activate/deactivate an existing edge or change gain without moving state;
- **medium remapping:** reassign sparse routes, factor-node memberships, or tile placement at an epoch boundary;
- **slow consolidation:** create a durable successor graph only after replay, stability checks, and capacity review.

Each proposed change needs a resource lease, provenance, expected benefit, expiration or consolidation condition, and rollback target. Per-module homeostasis should constrain total event rate, degree, weight norm, and excitation. A global controller should not directly write every synapse in real time.

**Observable:** compare weight-only, gating-only, and structural-plasticity conditions under equal compute, memory, and training data. Report task transfer, forgetting, recovery after lesion, edge churn, route-table pressure, energy, and topology commit failures.

**Falsifier:** if rewiring does not outperform simpler gating or sparse-mixture baselines, or if it produces persistent congestion, catastrophic forgetting, oscillatory topology churn, or unverifiable partial commits, remove it.

### 4. Physical reservoir computing is promising at the periphery, not as a general brain

Physical reservoirs exploit nonlinear dynamics and fading memory while training mainly a readout. The physical medium may be photonic, memristive, magnetic, mechanical, or even the compliant body of a robot. This is attractive for local temporal transforms where a rich but partly unknown response is useful.

The strongest outside-the-box role is **morphological preprocessing**: compliant limbs, skins, tendons, or soft structures can turn forces and contact histories into a high-dimensional sensor trace before digital inference. Soft-body reservoir experiments have demonstrated payload, terrain, wind, and locomotion-related functions. [Soft-body physical computing review](https://www.nature.com/articles/s41467-026-70866-6), [soft-body reservoir experiment](https://www.nature.com/articles/srep10487)

The limitation is equally important: a fixed reservoir is not an open-ended cognitive architecture. Performance may reside in offline preprocessing, time multiplexing, or a conventional linear readout. Device-to-device transfer and long-term calibration are unresolved for many materials.

**Integration decision:** use reservoirs as replaceable, typed sensor transforms with bypass paths. Never let an opaque reservoir own canonical memory, safety logic, or topology authority.

**Falsifier:** compare against a carefully tuned digital echo-state network, delay embedding, polynomial features, and small recurrent network with the same number of observable states. If the physical system loses after transducer, reset, readout, calibration, and training costs are counted, the material novelty is not a system advantage.

### 5. Photonics is most credible first as interconnect

Optics provides high bandwidth, wavelength multiplexing, and low propagation latency. Integrated photonic computing has demonstrated very fast small matrix and reservoir operations. The missing costs are often at the boundary: lasers, drivers, modulators, photodetectors, transimpedance amplifiers, ADC/DACs, thermal tuning, memory, and nonlinear activation.

The 64 x 64 PACE system is informative because it is a packaged hybrid, not just an optical core: it required more than 16,000 photonic components, a 28 nm electronic IC, a 65 nm photonic IC, four external continuous-wave lasers, DACs, receivers, SRAM, and 2.5D assembly. This is a useful systems demonstration and a warning against quoting light-propagation energy alone. [PACE](https://www.nature.com/articles/s41586-025-08786-6)

A 2025 large-scale photonics assessment reports that electronics currently exceed photonic integration density by four to five orders of magnitude, practical optical precision is commonly 4-8 bits, and memory movement can dominate power. It identifies optical interconnect and narrow analog-input niches as more credible near-term applications than general digital replacement. [Large-scale photonic processors](https://www.nature.com/articles/s44310-025-00075-4)

By contrast, the 80-channel 3D photonic transceiver is directly relevant to chiplet/rack communication: its 800 Gb/s aggregate and 120 fJ/bit combined front-end result are measured component evidence. The complete link still needs laser and protocol accounting.

**Integration decision:** evaluate photonics first for longer, hotter, bandwidth-limited links and native optical/RF inputs. Promote optical compute only for a stable matrix or reservoir kernel that wins at the wall plug.

**Falsifier:** no promotion if a claimed TOPS/W advantage excludes laser, conversion, memory, calibration, or cooling, or if precision and reconfiguration requirements erase the advantage.

### 6. Spintronics is a research island, not a scale assumption

Spin-torque oscillators and skyrmions supply compact nonlinear dynamics, stochasticity, memory, and synchronization. The experimentally demonstrated networks remain tiny or time-multiplexed. The single-oscillator spoken-digit demonstration used conventional preprocessing and linear readout; the four-oscillator vowel system demonstrates physical coupling but not scalable cognition. The skyrmion reservoir's 50 nodes were virtual time slots on one comparatively large device, and each input interval was 0.1 seconds.

Passive frustrated nanomagnets are an interesting alternative because coupled relaxation can form a reservoir with little internal drive energy. The cited work fabricated a frustrated array but evaluated task expressivity mainly in micromagnetic simulation and projected system resource savings; it is not a complete large hardware reservoir. [Passive nanomagnet reservoir](https://www.nature.com/articles/s42005-023-01324-8)

**Integration decision:** reserve spintronics for small oscillator-binding, stochastic-sampling, or reservoir experiments. Require a digital bypass and external ground truth.

**Falsifier:** a minimum credible scaling experiment is a physically coupled, independently addressable array of at least tens of devices whose task transfer, synchronization, energy, and readout remain stable across specimens and temperature. If time multiplexing and conventional electronics supply the useful dimension, report that rather than a device-array advantage.

### 7. Chiplets and 3D integration solve some wire problems and create heat problems

UCIe establishes a plausible commercial path for heterogeneous chiplets. Version 3.0 adds 48/64 GT/s operation, continuous raw-mode mappings, priority sideband events, runtime recalibration, and emergency throttling/shutdown. Those management features are especially relevant to a zoned HC-1R.

The standard does not make arbitrary chiplets interoperable at the semantic or learning-rule level. It also cannot remove traffic and heat. A peer-reviewed UCIe/3D analysis notes that additional stacked chiplets exacerbate hotspot power density and introduce cooling, power-delivery, reliability, and repair challenges. [UCIe 3D analysis](https://www.nature.com/articles/s41928-024-01126-y)

Neuromorphic traffic favors multicast. SpiNNaker demonstrates hardware multicast and fault-aware routing at million-core design scale, while routing work shows that full connectivity produces worse delay and firing rate than sparse connectivity. [SpiNNaker project](https://doi.org/10.1109/JPROC.2014.2304638), [multicast routing](https://doi.org/10.1016/j.parco.2015.01.002), [configurable neural NoC analysis](https://doi.org/10.1016/j.micpro.2010.08.005)

**Integration decision:** use hierarchical multicast, locality-aware placement, explicit traffic classes, and separate control/safety sidebands. Never infer usable capacity from aggregate bandwidth alone. Size against bisection bandwidth and adversarial bursts.

**Falsifier:** if real graph traces exhibit a phase transition into congestion, timing-dependent computation changes under harmless traffic rearrangements, or required cooling/throttling removes the density benefit, reduce fan-out, add hierarchy, or abandon 3D stacking for that zone.

### 8. Body-scale I/O requires a peripheral nervous system, not raw sensor fan-in

Event cameras demonstrate that sparse asynchronous sensing is mature enough for real hardware-in-loop work. Sony's IMX636 provides 1,280 x 720 event pixels and can emit up to 1.06 billion events/s; that maximum rate is also a denial-of-service envelope, not merely a capability. Tactile systems increasingly encode touch as spike timing, and neuromorphic skins have demonstrated local pain/injury-like protection and modular replacement. [Neuromorphic robotic skin](https://pubmed.ncbi.nlm.nih.gov/41428887/)

HC-1R should use body regions as independent timing and failure domains:

- sensor tiles timestamp, calibrate, filter, compress, and rate-limit locally;
- a low-power local controller implements reflexes and safe-state behavior;
- synchronized event gateways translate each modality into typed messages;
- the main cognitive substrate receives sparse summaries plus requested detail;
- actuator requests pass through an independent safety arbiter with hard bounds;
- failure, saturation, stale timestamps, or broken synchronization changes the sensor's validity state rather than silently generating normal events.

Raw camera, tactile, audio, and proprioceptive streams should not all converge on one global bus. The design should exploit local loops for grip slip, collision withdrawal, joint limits, battery/thermal protection, and emergency stop. These loops must continue when the cognition substrate is overloaded, reconfiguring, or offline.

**Observable:** measure acquisition-to-actuation p99/p99.9 latency, jitter, clock skew, burst drop rate, stale-data detection, local-reflex availability, safe-stop time, and the fraction of events discarded or summarized at each edge tier.

**Falsifier:** any single sensor, cable, gateway, or cognitive tile can generate an unbounded actuator command, defeat safe stop, or saturate unrelated body regions.

### 9. Quantum resources do not belong in the baseline architecture

No source reviewed establishes a practical quantum advantage for the continuous classical sensorimotor, memory, routing, or learning workloads HC-1R requires. Quantum machine-learning advantages are highly sensitive to data-access assumptions and classical baselines. A quantum annealer may show favorable scaling against a chosen classical algorithm without beating the best classical method or achieving end-to-end speedup.

If a future workload emerges, treat the QPU as a remote batch accelerator behind a typed request/response interface. The rest of HC-1R must remain correct when the service is absent, delayed, noisy, or returns no useful answer.

Before any claim of advantage:

1. freeze a practical workload and solution-quality threshold;
2. include encoding, embedding, queueing, networking, calibration, error mitigation, repeated sampling, readout, and post-processing;
3. tune classical exact, heuristic, tensor-network, GPU, and problem-specialized solvers with equal effort;
4. report scaling, not one problem size;
5. repeat across seeds and, when possible, independent hardware;
6. publish failures and confidence intervals.

The default result is **no dependency and no claimed advantage**. A useful quantum result would change only the relevant service implementation, not the HC-1R identity, memory, or control architecture.

## Calibration, drift, observability, and fault containment

### Calibration architecture

Every non-digital island needs a calibration contract:

- device and array identifier;
- measured transfer function and uncertainty;
- temperature, voltage, age, and time since programming;
- calibration dataset provenance and validity interval;
- correction parameters and residual error;
- last successful self-test;
- bypass and invalidation conditions.

Calibration should be layered:

1. manufacturing or laboratory characterization;
2. boot-time parameter identification;
3. continuous reference channels and lightweight health probes;
4. scheduled deeper calibration while redundant capacity carries the workload;
5. task-level sentinel tests that can detect a correct-looking electrical response with wrong functional behavior.

IBM's open-source [Analog Hardware Acceleration Kit](https://github.com/IBM/aihwkit) includes PCM models calibrated to a one-million-device chip, ADC/DAC quantization, programming noise, device variation, drift, and hardware-aware training. It is suitable for pre-hardware falsification, not proof that an unseen device will behave identically.

### Required observability

At minimum, log by tile, link, sensor, and topology epoch:

- energy and instantaneous power;
- temperature and thermal-throttle state;
- event input/output rates and sparsity;
- queue depth, drops, retries, CRC errors, route changes, and p99 latency;
- active graph/topology version and partially prepared changes;
- local-memory occupancy and remote bytes transferred;
- analog calibration residual, drift estimate, saturation, and clipped outputs;
- device faults, disabled resources, remaps, restore source, and recovery time;
- sensor validity, clock offset, event-rate limiting, and actuator-arbiter decisions.

Instrumentation must be budgeted because indiscriminate probing can change timing and power. Use sampled telemetry plus triggerable high-resolution traces.

### Fault-containment rules

- Each tile and accelerator is a replaceable failure domain.
- Event packets carry source, type, topology epoch, age/TTL, and integrity protection appropriate to the link.
- Routers enforce per-source rate limits and bounded queues; no event storm gets unlimited replication.
- Safety and management traffic has a separate priority path and cannot be starved by cognitive traffic.
- Analog output is range-checked and plausibility-checked before it affects durable state or actuators.
- Durable checkpoints are digital, versioned, and verified before restore.
- A route-around operation cannot silently change the computational model; remapped execution must pass a conformance probe.
- Recovery is tested by fault injection, not inferred from neural “graceful degradation.”

SpiNNaker's use of spare processors, emergency routing, and post-boot discovery of working resources is a useful precedent, while fault-injection work shows that bad weight memory or neuron behavior can materially degrade SNNs. [SpiNNaker fault tolerance](https://eprints.gla.ac.uk/180253/), [RescueSNN](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1159440/full)

## Power and thermal zoning

The design should be thermally hierarchical rather than treating the entire substrate as one power domain.

| Zone | Contents | Normal posture | Failure posture |
|---|---|---|---|
| S0: safety and vital telemetry | independent safety MCU/FPGA, emergency stop, joint/battery/temperature limits, heartbeat | always on, low and predictable power, no dependence on learned state | command safe state and isolate all higher zones |
| S1: sensor/reflex edge | event encoders, tactile/vision/audio/proprioceptive preprocessing, local reflexes | event-driven, aggressive idle, local buffering and rate limits | declare invalid/stale, retain bounded reflex or safe stop |
| S2: digital cognitive tiles | local SRAM, event/spatial compute, graph routes, working state | dynamic voltage/frequency and workload migration | checkpoint, quiesce, remap, or shed noncritical work |
| S3: experimental accelerators | PCM/RRAM, analog neurons, reservoirs, spintronics | normally power-gated; enabled only for a typed workload | bypass, invalidate calibration, remove from graph |
| S4: optical/chiplet links | co-packaged optics, die-to-die links, high-radix gateways | traffic-aware lane and laser management | reroute, throttle, lower data fidelity, preserve safety traffic |
| S5: external services | rack-scale compute or quantum service | asynchronous, nonessential to immediate control | timeout with a defined classical/local fallback |

Hala Point provides a concrete reminder that billion-neuron-class digital neuromorphic capacity currently means kilowatts and rack cooling. Conversely, sensor-level microwatt claims do not include lenses, interfaces, compute, and networking. Every power claim should be reported at the narrow component boundary and the complete system boundary.

Thermal simulation must include spatial hotspots, inter-tier coupling, leakage-temperature feedback, link/laser heat, power delivery, cooling power, and performance under throttling. 3D stacking is not promoted on room-temperature peak bandwidth alone.

## Promising mechanisms outside the conventional path

1. **Factor-node hyperedges instead of literal hyperwires — EXTRAPOLATED.** Encode a many-party relation once and multicast membership updates, avoiding quadratic physical connectivity.
2. **Structural-plasticity virtualization — DEMONSTRATED small-scale / EXTRAPOLATED system-scale.** Change addresses, routing tables, placement, and sparse allocation; keep metal fixed.
3. **Dual-plane event fabric — EXTRAPOLATED.** A fast sparse data plane carries events, while a slower transactional plane commits topology, calibration, provenance, and recovery state.
4. **Morphological and sensor-native reservoirs — DEMONSTRATED small-scale / EXTRAPOLATED.** Let compliant bodies, photonic front ends, or tactile materials perform narrow preprocessing before digitization.
5. **Stochastic devices as samplers, not memories — EXTRAPOLATED.** Device noise may be useful for exploration or probabilistic inference if output statistics are calibrated; it is harmful for canonical state.
6. **Photonic interconnect before photonic cognition — DEMONSTRATED component / EXTRAPOLATED fabric.** Spend optical complexity where distance and bandwidth make the electrical alternative expensive.
7. **Fault-aware spatial compilation — DEMONSTRATED in adjacent systems / EXTRAPOLATED.** Treat temperature, link load, calibration quality, and failed resources as compiler inputs, not after-the-fact exceptions.
8. **Event-sourced topology epochs — EXTRAPOLATED.** Record graph changes as replayable transactions so a restored system can distinguish state, wiring, calibration, and time.
9. **Time-multiplexed dynamics only when latency permits — DEMONSTRATED.** One physical device can expose many virtual states, but virtual-node count must never be reported as physical scale and serial latency must be counted.

## Seductive dead ends and rejected interpretations

- **Literal rapidly rewiring physical all-to-all hyperconnectivity — REJECTED.** Wire, router, memory, and power costs grow too quickly. Sparse virtual graphs are the viable analogue.
- **Neuron or synapse count as evidence of brain equivalence — REJECTED.** Counts omit dynamics, algorithms, embodiment, learning, memory, and causal organization.
- **“Memristor equals synapse, therefore cognition” — REJECTED.** Device resemblance does not supply an architecture, task, stability rule, or semantics.
- **Analog has infinite precision or free MACs — REJECTED.** Noise, IR drop, ADC/DAC, programming, calibration, and drift are measured system costs.
- **Photon propagation energy as total photonic energy — REJECTED.** Lasers, modulation, detection, conversion, memory, control, and cooling must be included.
- **A fixed reservoir as a general learning system — REJECTED.** Reservoirs are useful transforms; readout, transfer, continual learning, and system control remain external.
- **Spintronic virtual nodes as a large physical network — REJECTED.** Time multiplexing is serial reuse, not simultaneous device scale.
- **3D integration as unlimited bandwidth — REJECTED.** It trades wire length for thermal, power-delivery, repair, and packaging constraints.
- **“Edge of chaos” or self-organization as a sufficient objective — REJECTED.** These are measurable dynamical regimes, not certificates of useful cognition or safety.
- **Quantum consciousness, generic quantum cognition, or an assumed QML speedup — REJECTED.** No defined HC-1R workload or end-to-end advantage supports them.
- **A head-mounted Hala Point equivalent — REJECTED at present.** The demonstrated system is a 2.6 kW six-rack-unit research machine.
- **Opaque analog state as canonical memory — REJECTED.** Drift, calibration dependence, and recovery requirements demand a governed digital record.

## Staged simulation and hardware-in-loop validation ladder

No stage below authorizes custom fabrication or deployment. Each stage may stop the candidate permanently.

### Stage 0 — Requirement and falsifier freeze

**Build:** a versioned workload manifest, candidate mechanism registry, baseline list, metric definitions, safety invariants, and per-candidate falsifiers.

**Required workloads:**

- sparse event vision with controllable burst density;
- tactile slip/contact and local reflex;
- streaming audio or other long temporal sequence;
- multimodal binding through explicit factor-node hyperedges;
- continual/context learning with interference measurement;
- topology churn and module migration;
- fault, clock, packet-loss, and thermal stress.

**Exit gate:** each result can be reproduced from a workload version, input trace, topology epoch, calibration state, hardware/software version, and measurement boundary. If a candidate has no workload-specific hypothesis, reject it before implementation.

### Stage 1 — Substrate-neutral functional model

**Build:** an executable sparse temporal graph with local state, multicast, factor nodes, topology epochs, checkpoint/restore, and safety-plane mocks. Use NIR-compatible primitives where possible and a conventional reference implementation.

**Tests:**

- identical graph execution under multiple scheduling orders;
- atomic edge/factor membership change;
- restore from every commit boundary;
- no half-visible topology epoch;
- weight-only versus gating versus structural-plasticity ablations;
- dense-traffic adversarial case.

**Exit gate:** task and state invariants survive permitted execution-order differences. **Stop** if correctness requires global instantaneous state or dense all-to-all messaging.

### Stage 2 — Communication, memory, power, and thermal co-simulation

**Build:** feed recorded Stage 1 event traces into a cycle-level network model such as [BookSim 2](https://github.com/booksim/booksim2); add local/remote memory accounting; use [HotSpot](https://lava.cs.virginia.edu/hotspot/) or a validated 2.5D/3D thermal model; model analog candidates with [AIHWKit](https://github.com/IBM/aihwkit).

**Sweeps:** topology, placement, fan-out, event density, burst correlation, packet size, link faults, DVFS, ambient temperature, cooling, calibration, drift, quantization, and ADC/DAC precision.

**Exit gate:** p99/p99.9 deadlines, no-loss or explicitly lossy semantics, thermal limits, and energy budgets hold at the target load plus a preregistered margin. **Stop** if the result depends on average traffic while realistic bursts saturate the network.

### Stage 3 — Fault and drift campaign

**Inject:** stuck weights, conductance drift, read/write noise, dead cores, dead links, corrupted routes, clock skew, stale sensor time, queue overflow, packet duplication/drop/reorder, power interruption, thermal throttling, and calibration failure.

**Tests:** containment radius, alarm latency, safe-stop latency, graph rollback, checkpoint integrity, state remap, degraded-mode task quality, and repeat fault during recovery.

**Exit gate:** every injected fault either remains in its declared domain or triggers a bounded safe state. **Stop** if a candidate produces silent, plausible, unsafe output or if recovery cannot identify the topology/calibration version restored.

### Stage 4 — Conventional heterogeneous emulator

**Build:** map the graph across CPUs/GPUs and FPGA event routers with local SRAM/DRAM partitions; connect recorded sensor streams and simulated actuators. This stage supplies a full digital baseline and exposes compiler/runtime overhead before scarce hardware is used.

**Measure:** end-to-end wall power, host work, event serialization, tail latency, topology-update stalls, checkpoint cost, and observability overhead.

**Exit gate:** the architecture functions without any exotic substrate. A specialized substrate is eligible only if it has a measured bottleneck to attack.

### Stage 5 — Digital neuromorphic hardware-in-loop

**Build:** execute bounded partitions on available research hardware such as Loihi 2, SpiNNaker2, or BrainScaleS-2 while the rest remains in the emulator. Replay identical sensor traces and compare with the reference state/task outputs.

**Tests:** cross-backend NIR conformance; multicast hot spots; on-chip learning; graph remapping; fault isolation; timestamp translation; host dependency; and energy from the wall or board rails.

**Exit gate:** repeatable advantage or uniquely useful dynamics on a defined workload, with no hidden host path. **Stop or demote** if mapping/tooling or dense traffic dominates.

### Stage 6 — Analog, reservoir, photonic, and spintronic coupons through existing hardware

**Build:** no new fabrication. Use existing laboratory, remote-access, or partner devices as replaceable accelerators behind the same interface.

**Protocol:** characterize multiple devices; blind the task evaluator to device identity; repeat after idle time and temperature changes; include all converters, lasers, readout, reset, calibration, and host processing; run tuned digital alternatives.

**Exit gate:** a statistically repeatable complete-system advantage or a functional capability not reproduced by the digital baseline. A core-only TOPS/W or one-device demo is insufficient.

### Stage 7 — Bounded body hardware-in-loop rig

**Build:** event camera, tactile patch, audio/proprioceptive sources, synchronized gateways, simulated plant first, then a mechanically constrained benchtop actuator or hand. An independent safety controller owns limits and emergency stop.

**Tests:** glare/flicker and event storms; contact bursts; cable removal; sensor damage; clock loss; compute overload; stale commands; topology update during motion; thermal throttling; and emergency stop at every software state.

**Exit gate:** local reflex and safe stop remain available with the cognitive substrate absent or maliciously overloaded. This is a laboratory HIL result, not deployment authorization.

### Stage 8 — Integrated evidence review

**Deliver:** a source-linked evidence matrix, raw traces, calibration records, measurement-boundary diagrams, baseline tuning logs, failure results, reproducibility package, and explicit no-go list.

**Promotion rule:** keep the simplest substrate that meets the workload. Heterogeneity is justified only by measured end-to-end benefit or necessary function. No result at this stage proves consciousness, authorizes fabrication, or authorizes a deployed system.

## Recommended benchmark and reporting contract

For every candidate, report:

- task quality and uncertainty;
- p50, p95, p99, and p99.9 end-to-end latency and jitter;
- throughput under average and burst traces;
- joules per completed task and energy-delay product;
- wall power plus a component breakdown including host, I/O, conversion, laser, memory, calibration, and cooling when relevant;
- active versus provisioned neurons/synapses/nodes/devices;
- physical devices versus time-multiplexed virtual nodes;
- local and remote bytes, event sparsity, fan-out, queue occupancy, drops, and retries;
- topology changes per second, commit time, migration bytes, rollbacks, and route-table use;
- task quality versus time since calibration, temperature, voltage, device age, and faults;
- recovery time, containment radius, restored topology/state version, and safe-stop result;
- baseline hardware, software, precision, batch size, tuning budget, and measurement method.

A reasonable research promotion threshold is a preregistered, statistically supported complete-system improvement over a strong baseline, not a fixed universal multiplier. For optional exotic accelerators, a marginal result should be treated as a failure because integration cost and uncertainty are high.

## Bottom line

HC-1R does not need a new physical law. It needs disciplined virtualization of connectivity, local memory, sparse event communication, transactional topology changes, calibration-aware heterogeneous acceleration, thermal zoning, and independent body safety.

The strongest buildable research direction is a **digital, local-memory, multicast substrate with virtual structural plasticity**, augmented only by accelerators that survive complete-system tests. Analog in-memory and physical reservoirs are promising narrow islands. Photonics is most credible first for interconnect. Spintronics remains small-scale experimental work. Body-scale event sensing is ready for HIL research but not yet a validated unified nervous system. Quantum hardware should remain absent from the baseline and optional at the service boundary.

That architecture is **EXTRAPOLATED but falsifiable**. A literal dynamically rewiring, dense physical hyperconnectome is **REJECTED** under current evidence.

