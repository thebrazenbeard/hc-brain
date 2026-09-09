# Hyperconnectome Brain Research Layer

Status: independent research contribution / not architecture canon

This directory grounds the generic Hyperconnectome Brain template in current neuroscience and computing research while preserving a strict separation between observation, engineering analogy, architectural implication, and speculation.

## Non-hemispheric invariant

The Hyperconnectome Brain has **no hemispheres**.

Biological studies of lateralization may still be useful as evidence that specialization can coexist with global integration, but the architecture must not instantiate left/right halves, a corpus-callosum analogue, paired hemispheric executives, or any assumption that cognitive specialization requires anatomical bilateral partitioning.

The target is specialization through distributed nodes, dynamic coalitions, typed connectivity, multiple timescales, and plastic routing.

## Evidence labels

- `ESTABLISHED` — strong enough to use as a baseline design constraint.
- `PLAUSIBLE` — evidence-backed, but not stable or universal enough to hard-code.
- `SPECULATIVE` — a reasoned proposal that requires dedicated validation.
- `UNSUPPORTED_OR_CONTRADICTED` — should not be assumed in the baseline architecture.

## Translation rule

Each research finding should be read through five questions:

1. What does the source actually show?
2. Is the claim local to biology, or does it express a more general systems principle?
3. What synthetic analogue is proposed?
4. What can go wrong when transferring that principle?
5. What experiment would justify promotion into architecture canon?

## Research conclusions that already look robust

1. **Do not build an all-to-all brain.** Efficient biological networks combine local clustering/modularity with selective long-range integration; wiring, latency, energy, and vulnerability impose real costs. `[S01-S04]`
2. **Do not build one master executive.** Control and action selection are distributed across recurrent loops and specialized structures; coordination is not equivalent to a homunculus. `[S21-S22]`
3. **Treat communication policy as part of cognition.** Network function depends not only on what is connected but on how signals are routed, delayed, gated, prioritized, and transformed. `[S03]`
4. **Plasticity needs plasticity control.** Metaplasticity and neuromodulation show that learning rate and eligibility themselves need state-dependent regulation. `[S06-S09]`
5. **Separate fast acquisition from slow integration.** Complementary-learning-system research strongly supports avoiding one uniform learning rate for episodic capture and general semantic integration. `[S10-S14]`
6. **Memory retrieval may change memory.** Reconsolidation evidence argues against a model in which recall is always a read-only operation. `[S15]`
7. **Multimodal fusion must preserve modality, timing, and uncertainty.** Integration is context-sensitive and multi-timescale rather than a one-time conversion into a single undifferentiated stream. `[S16-S20]`
8. **Keep compute close to state where possible.** Neuromorphic and in-memory architectures show large potential benefits from reducing data movement, but precision, programmability, routing, device variability, and endurance remain hard constraints. `[S23-S30]`
9. **Photonic compute is promising but should remain heterogeneous.** Photonics can provide exceptional bandwidth and latency for selected operations; nonlinearities, memory, training, conversion, calibration, and integration remain practical bottlenecks. `[S31-S37]`
10. **No substrate result proves a mind.** Hardware capability, network topology, memory persistence, affective modulation, and complex behavior do not by themselves establish consciousness or personhood.

## Navigation

- `NEUROSCIENCE_AND_CONNECTOMICS.md` — topology, communication, hubs/modules, wiring cost, dynamic organization.
- `NEUROMODULATION_AND_ENDOCRINE_ANALOGUES.md` — gain control, salience, learning-context signals, endocrine transfer limits.
- `PLASTICITY_MEMORY_AND_CONTINUAL_LEARNING.md` — metaplasticity, complementary learning systems, consolidation, reconsolidation, interference.
- `MULTIMODAL_SENSORIMOTOR_INTEGRATION.md` — multisensory fusion, body schema, interoception, timing, action-perception loops.
- `DISTRIBUTED_CONTROL_AND_ARBITRATION.md` — distributed selection, control loops, arbitration, graceful degradation.
- `COMPUTE_MATERIALS_AND_INTERCONNECTS.md` — neuromorphic, in-memory, memristive, photonic, energy/thermal/interconnect constraints.
- `EVIDENCE_LIMITS_AND_OPEN_QUESTIONS.md` — claims that remain uncertain, unsupported, or experimentally bounded.
- `HC_IMPLICATIONS_MATRIX.md` — concise architecture-facing map.
- `SOURCES.md` — bibliography.

## Governance

Research documents may recommend changes to HC-1/HC-2/HC-3 but do not silently rewrite those architectures. Integration should happen through explicit review by repository governance.
