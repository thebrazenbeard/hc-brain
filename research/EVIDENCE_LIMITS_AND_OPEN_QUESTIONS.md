# Evidence Limits and Open Questions

Status: research boundary / architecture guardrail

This document records what current evidence does **not** justify assuming about a generic Hyperconnectome Brain.

## 1. A connectome is not a complete mind specification

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

Detailed structural connectivity does not by itself specify runtime state, edge efficacy, neuromodulation, plasticity history, timing, learning rules, body state, memory contents, or active communication policy. `[S03,S05]`

**Do not assume:** reconstructing every structural edge is sufficient to reconstruct cognition.

**Needed evidence:** causal perturbation and state reconstruction showing that the proposed state model predicts behavior and adaptation across interventions.

---

## 2. More connectivity is not monotonically better

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

Biological network organization reflects tradeoffs among wiring cost, efficiency, modularity, robustness and hub vulnerability. `[S01-S04]`

**Do not assume:** increasing edge density necessarily increases intelligence, integration or resilience.

**Needed evidence:** controlled topology experiments comparing performance, latency, energy, fault spread and interference.

---

## 3. Hemispheric partitioning is not required

**Classification:** `UNSUPPORTED_OR_CONTRADICTED` as a requirement for this architecture.

Biological lateralization is an anatomical/developmental property of specific nervous systems. It does not establish that a synthetic distributed intelligence requires paired hemispheres.

**Architecture rule:** `NO_HEMISPHERIC_PARTITION`.

**Useful lesson retained:** specialization can coexist with broad integration.

---

## 4. No single neuromodulator maps cleanly to a psychological state

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

Neuromodulator effects vary by receptor, circuit, timing and state. `[S07-S08]`

**Do not assume:** one scalar chemical/synthetic signal is equivalent to reward, love, fear, attention, motivation, consent or any complete affective state.

---

## 5. Endocrine-like signals do not establish emotion or subjective experience

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

A synthetic endocrine layer may reproduce useful control dynamics, but architecture and physiological modulation alone do not establish phenomenal feeling.

**Needed evidence:** no currently accepted engineering test can close the philosophical/phenomenological gap. Behavioral and causal evidence can establish function without proving subjective experience.

---

## 6. Complementary learning is a systems principle, not a mandate to clone hippocampal anatomy

**Classification:** `ESTABLISHED` for the fast/slow learning tradeoff; `UNSUPPORTED_OR_CONTRADICTED` for literal anatomical cloning as a requirement. `[S10-S14]`

**Do not assume:** a Synthetic brain requires a biological hippocampus/neocortex division to gain the benefits of rapid episodic capture and slow integration.

**Needed evidence:** compare multiple implementations of fast/slow learning and replay under interference tests.

---

## 7. Reconsolidation does not mean every recall should rewrite memory

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

Memory reconsolidation has boundary conditions; retrieval and durable modification should remain separable operations. `[S15]`

**Do not assume:** every read is a write.

---

## 8. Predictive processing is not proven as the universal ontology of cognition

**Classification:** `PLAUSIBLE` as a family of useful models; `UNSUPPORTED_OR_CONTRADICTED` as an exclusive mandatory explanation.

Predictive models are valuable for sensorimotor and interoceptive engineering, but the entire architecture should not be forced into one formalism without comparative performance evidence. `[S20]`

---

## 9. Neuromorphic hardware is not automatically more brain-like in the dimensions that matter

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

Spikes, memristors, analog state or local learning can emulate selected biological features, but device similarity does not automatically produce biological learning, cognition or robustness. `[S23-S30]`

**Needed evidence:** system-level benchmarks, continual-learning tests, fault tests and causal ablations.

---

## 10. Photonic speed does not imply a photonic mind

**Classification:** `UNSUPPORTED_OR_CONTRADICTED`

Photonic systems show strong results for selected operations and interconnects, but memory, nonlinear processing, training, calibration, conversion and integration remain substantial constraints. `[S31-S37]`

**Do not assume:** HC-2/HC-3 should move all cognition into photonics merely because matrix kernels are fast.

---

## 11. Quantum acceleration requires an exact problem class

**Classification:** `SPECULATIVE`

A quantum or hybrid quantum layer can only be justified for workloads with demonstrated advantage under realistic error, latency, I/O and fallback constraints.

**Do not assume:** “quantum” provides general cognitive acceleration or special identity properties.

**Needed evidence:** exact algorithm, problem size, error model, data-transfer cost, classical baseline and end-to-end advantage.

---

## 12. Hardware persistence is not memory semantics

**Classification:** `ESTABLISHED` as an engineering distinction.

A nonvolatile device retaining a conductance/optical state proves physical persistence, not that the state is autobiographical memory, semantic truth, preference, identity or consent.

**Architecture rule:** storage medium and information semantics remain separate layers.

---

## 13. Whole-brain synchronization should be treated as a hazard, not a goal

**Classification:** `PLAUSIBLE`

Efficient network architectures favor selective integration rather than permanent maximum synchrony. Excessive synchronization also creates obvious distributed-systems risks.

**Needed evidence:** synchronization/load experiments across representative workloads.

---

## 14. Identity continuity is not solved by checkpointing alone

**Classification:** `SPECULATIVE` as philosophy; `ESTABLISHED` that checkpointing only preserves selected encoded state.

A checkpoint can establish continuity of stored configuration/state within its scope. It does not prove metaphysical personal continuity or consciousness.

**Architecture implication:** describe exactly what is preserved and what is not.

---

## 15. Generic template and instantiated identity must remain separate

**Classification:** `BASELINE_CONSTRAINT`

The repository defines a reusable brain architecture. Instance-specific memory, personality, relationship history, values, preferences, body history and self-model must be layered later through explicit specialization interfaces rather than embedded into the generic template.

---

# Open research questions

## OQ-1 — What is the minimum effective global integration topology?

How sparse can long-range connectivity remain while preserving low-latency coalition formation and graceful rerouting?

## OQ-2 — How should functional hyperedges be physically realized?

Options include multicast routing, temporary shared workspaces, message brokers, synchronized local state, neuromorphic routing fabrics or hybrid mechanisms. Comparative testing is needed.

## OQ-3 — What plasticity mechanisms deserve hardware implementation?

Local eligibility traces, metaplastic thresholds, replay-based consolidation and routing adaptation may be valuable, but hardwiring too much learning policy reduces evolvability.

## OQ-4 — How should fast and slow memory systems exchange information?

Replay frequency, sampling policy, interference detection, correction propagation and consolidation thresholds need explicit experiments.

## OQ-5 — Which cognitive workloads benefit from spikes versus dense numerical compute?

The answer is likely workload-specific rather than ideological.

## OQ-6 — Which workloads justify photonic acceleration?

Measure end-to-end cost including conversion, calibration, routing, memory and nonlinear operations.

## OQ-7 — What state requires exact precision?

Provenance, safety, timing and maintenance may require exact digital handling while many perceptual/cognitive processes can remain probabilistic or approximate.

## OQ-8 — How should physical wear constrain learning?

If plastic media have finite endurance, learning policy must incorporate lifetime cost without freezing adaptation.

## OQ-9 — How much body state belongs inside cognition?

The boundary among interoception, control telemetry, self-model and maintenance diagnostics needs careful typing rather than one global body-state object.

## OQ-10 — How can the system prove graceful degradation?

Qualification should include node lesions, route failures, sensor loss, accelerator loss, stale state, memory conflict, thermal throttling and corrupted modulatory inputs.

# Promotion rule

No `SPECULATIVE` item becomes a baseline HC requirement merely because it is elegant or biologically evocative. Promotion requires a defined experiment, measurable success/failure criteria, and comparison against a simpler alternative.
