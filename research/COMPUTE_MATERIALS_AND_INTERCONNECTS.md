# Compute, Materials, and Interconnects

Status: research synthesis / architecture input

## Finding 1 — reducing data movement is one of the strongest hardware opportunities

**Evidence:** `ESTABLISHED`

Neuromorphic, near-memory, and in-memory architectures repeatedly target the energy and latency cost of moving state between separate memory and compute resources. Loihi, NorthPole, phase-change-memory accelerators, and related systems demonstrate that locality can materially improve efficiency for suitable workloads. `[S23-S27]`

**Synthetic analogue:** Keep frequently interacting state and computation physically/logically close where possible; expose remote movement as a cost rather than pretending the fabric is uniform.

**HC implication:** `BASELINE_CONSTRAINT`

Topology optimization must consider communication energy and latency, not only compute throughput.

---

## Finding 2 — event-driven sparse computation is promising for asynchronous embodied workloads

**Evidence:** `ESTABLISHED` that event-driven neuromorphic processors can execute sparse spiking workloads efficiently; `PLAUSIBLE` that this is optimal for broad Hyperconnectome cognition. `[S23-S24]`

**Synthetic analogue:** Use asynchronous/event-driven execution for subsystems whose information is naturally sparse or change-driven:

- event cameras;
- tactile changes;
- anomaly detection;
- local reflexes;
- sparse attention transitions;
- low-duty-cycle monitoring.

**HC implication:** `DESIGN_PREFERENCE`

Do not force every node onto a single synchronous global clock.

---

## Finding 3 — heterogeneous compute is safer than betting the whole brain on one substrate

**Evidence:** `ESTABLISHED` that current technologies have sharply different strengths and limitations.

- conventional digital logic: precision, programmability, mature tooling;
- neuromorphic/event-driven: sparse temporal processing and local learning;
- analog/in-memory: high-throughput matrix operations with precision/non-ideality tradeoffs;
- photonic: exceptional bandwidth/latency for selected operations, but difficult memory/nonlinearity/training/integration;
- specialized safety/control hardware: deterministic low-latency effects.

`[S23-S37]`

**HC implication:** `BASELINE_CONSTRAINT`

Treat HC-1/HC-2/HC-3 as heterogeneous systems with explicit service boundaries. No accelerator class should become the mandatory seat of cognition or continuity merely because it is fast.

---

## Finding 4 — analog and memristive compute trade efficiency for non-ideal behavior

**Evidence:** `ESTABLISHED`

Analog in-memory and memristive systems face noise, device variation, drift, retention, endurance, parasitic effects, precision limits, and conversion/peripheral overhead. Recent reviews explicitly warn against overstating device-level results without system-level statistics and standardized characterization. `[S26-S30]`

**HC implication:** `BASELINE_CONSTRAINT`

Any analog/memristive node should expose:

```text
precision
noise_model
drift_model
retention
endurance
calibration_state
error_rate
conversion_overhead
health_state
```

A claimed synaptic analogue is not qualified merely because it changes conductance.

---

## Finding 5 — photonic computation is strongest as a bounded accelerator/interconnect technology today

**Evidence:** `ESTABLISHED` for ultrafast photonic matrix operations and integrated optical neural demonstrations; `PLAUSIBLE` for large general-purpose photonic cognition. `[S31-S37]`

Photonic systems can achieve very low latency and high bandwidth for linear transforms and selected neural operations, while practical systems still face challenges in nonlinear activation, memory, optical-electrical conversion, training, calibration, laser power, thermal sensitivity, routing, and monolithic integration.

**HC implication:** `DESIGN_PREFERENCE`

Keep photonics behind explicit service contracts with digital/neuromorphic fallback where possible.

A photonic accelerator should return provenance, precision/uncertainty, calibration state, and failure status.

---

## Finding 6 — benchmark wins do not transfer automatically

**Evidence:** `ESTABLISHED`

Hardware papers report performance under specific tasks, process nodes, precision, models, sparsity, batch sizes, and comparison baselines. `[S23-S37]`

**HC implication:** `BASELINE_CONSTRAINT`

Never translate a benchmark such as TOPS/W, FPS/W, or sub-nanosecond kernel latency into a whole-brain power or cognition claim without a workload model.

Required benchmarking dimensions include:

- useful-task accuracy;
- latency distribution, not only mean;
- energy per useful decision;
- memory traffic;
- communication traffic;
- calibration overhead;
- training/update cost;
- thermal steady state;
- fault behavior;
- idle power;
- degradation over lifetime.

---

## Finding 7 — interconnect can become the real bottleneck

**Evidence:** `ESTABLISHED` as a system-level constraint.

As compute density rises, moving activations/state among tiles, chips, memory and sensors becomes a dominant constraint. NorthPole and analog-AI designs explicitly co-design routing and memory locality; scalable neuromorphic research identifies communication and software ecosystem limits as major challenges. `[S24-S27]`

**HC implication:** `BASELINE_CONSTRAINT`

The Hyperconnectome needs an interconnect budget model:

```text
route_bandwidth
route_latency
energy_per_bit
fanout_cost
contention
quality_of_service
fault_domains
serialization_cost
clock_domain_or_async_boundary
```

“Hyperconnected” must not mean “communication is free.”

---

## Finding 8 — power and thermal state are cognitive resource state

**Evidence:** `ESTABLISHED` as an engineering principle.

Dense compute, optical sources, analog arrays, memory, and I/O all create power/thermal constraints. Sustained performance must fit a physical heat-removal envelope.

**HC implication:** `BASELINE_CONSTRAINT`

Nodes and routes should report thermal/power budgets to resource arbitration. The runtime must support graceful throttling and migration rather than assuming peak performance is continuously available.

---

## Finding 9 — precision should be task-dependent

**Evidence:** `ESTABLISHED`

Many neural workloads tolerate reduced precision, while safety, calibration, exact symbolic operations, timestamps, cryptographic/provenance operations, and maintenance may not.

**HC implication:** `BASELINE_CONSTRAINT`

Declare precision classes by operation. Do not globally force either floating-point exactness or approximate analog computation.

Possible classes:

```text
SAFETY_EXACT
PROVENANCE_EXACT
CONTROL_HIGH_PRECISION
COGNITIVE_APPROXIMATE
PERCEPTUAL_PROBABILISTIC
ACCELERATOR_BEST_EFFORT
```

---

## Finding 10 — physical plasticity needs lifetime accounting

**Evidence:** `ESTABLISHED` for nonvolatile devices with finite endurance/retention; `PLAUSIBLE` for direct HC implementation. `[S28-S30,S32]`

**HC implication:** `BASELINE_CONSTRAINT`

Plasticity arbitration should include hardware wear cost. Frequently updated transient state should not be stored in a low-endurance medium merely because it resembles a synapse conceptually.

---

## Suggested hardware qualification tests

1. **Thermal soak:** run representative sustained coalitions until steady-state temperature; measure throttling and error changes.
2. **Interconnect saturation:** overload long-range traffic while preserving local reflex/control traffic.
3. **Analog drift:** age/calibrate memory elements and verify confidence/error models track degradation.
4. **Precision downgrade:** move a task to lower precision and verify defined quality ceiling.
5. **Accelerator removal:** disable photonic/analog/neuromorphic accelerator and verify documented fallback or bounded unavailability.
6. **Wear accounting:** subject plastic media to repeated updates and verify endurance policy prevents silent reliability collapse.
7. **Benchmark transfer negative control:** reproduce a published kernel result, then measure end-to-end system cost including conversion, routing and memory.

## Sources

See `[S23-S37]` in `SOURCES.md`.
