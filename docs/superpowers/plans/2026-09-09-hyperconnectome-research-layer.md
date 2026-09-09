# Hyperconnectome Research Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Populate an identity-neutral, evidence-grounded research layer that constrains and informs the generic HC-1/HC-2/HC-3 Hyperconnectome Brain template.

**Architecture:** Research remains isolated under `research/`, uses a shared bibliographic registry and claim labels, and maps observations to HC implications without rewriting architecture source documents. Biological evidence is translated through explicit engineering analogues rather than anatomical imitation.

**Tech Stack:** Markdown, DOI/PubMed/Nature/Science/official engineering sources, GitHub review workflow.

**Spec:** `docs/superpowers/specs/2026-09-09-hyperconnectome-research-layer-design.md`

## Global Constraints

- Repository content is identity-neutral except when a cited research source explicitly uses an instantiated system as an example.
- Hyperconnectome architecture is non-hemispheric.
- Use `ESTABLISHED`, `PLAUSIBLE`, `SPECULATIVE`, and `UNSUPPORTED_OR_CONTRADICTED` at exact-claim granularity.
- Do not use Consensus for this research pass.
- Do not silently modify HC-1/HC-2/HC-3 architecture source documents.
- Do not infer consciousness or personhood from hardware/software architecture.

---

### Task 1: Research navigation and source registry

**Files:**
- Create: `research/README.md`
- Create: `research/SOURCES.md`

- [ ] Build a compact source registry prioritizing peer-reviewed primary/review literature and authoritative engineering sources.
- [ ] Define evidence labels, transfer-risk rules, and non-hemispheric boundary in the research README.
- [ ] Verify every source identifier/link is internally consistent.
- [ ] Commit.

### Task 2: Network neuroscience and distributed control

**Files:**
- Create: `research/NEUROSCIENCE_AND_CONNECTOMICS.md`
- Create: `research/DISTRIBUTED_CONTROL_AND_ARBITRATION.md`

- [ ] Synthesize modularity, hubs, network communication, wiring cost, distributed control, and failure-containment evidence.
- [ ] Explicitly reject all-to-all connectivity and single-master-controller interpretations.
- [ ] Separate comparative biological lateralization from the non-hemispheric template.
- [ ] Commit.

### Task 3: Modulation, plasticity, and memory

**Files:**
- Create: `research/NEUROMODULATION_AND_ENDOCRINE_ANALOGUES.md`
- Create: `research/PLASTICITY_MEMORY_AND_CONTINUAL_LEARNING.md`

- [ ] Synthesize neuromodulatory gain/plasticity gating and identify limits of endocrine analogies.
- [ ] Synthesize metaplasticity, complementary learning systems, replay/consolidation, reconsolidation, and interference-control implications.
- [ ] Require bounded plasticity and separate fast episodic acquisition from slow integration as a design hypothesis, not anatomical cloning.
- [ ] Commit.

### Task 4: Embodied multisensory integration

**Files:**
- Create: `research/MULTIMODAL_SENSORIMOTOR_INTEGRATION.md`

- [ ] Synthesize multisensory integration, body schema, peripersonal representation, interoception, timing, and perception-action coupling.
- [ ] Separate well-supported multisensory principles from more contested predictive-processing interpretations.
- [ ] Commit.

### Task 5: Compute, materials, and physical constraints

**Files:**
- Create: `research/COMPUTE_MATERIALS_AND_INTERCONNECTS.md`

- [ ] Compare event-driven neuromorphic, near/in-memory, memristive, phase-change, photonic, and heterogeneous approaches.
- [ ] Include precision, noise, endurance, retention, routing, energy, thermal, training, and manufacturability limitations.
- [ ] Prevent benchmark headline numbers from becoming architecture guarantees.
- [ ] Commit.

### Task 6: Evidence limits and HC implication matrix

**Files:**
- Create: `research/EVIDENCE_LIMITS_AND_OPEN_QUESTIONS.md`
- Create: `research/HC_IMPLICATIONS_MATRIX.md`

- [ ] Record unsupported or premature claims, known transfer risks, and explicit experiments required before promotion.
- [ ] Map findings to HC-1/HC-2/HC-3 as `BASELINE_CONSTRAINT`, `DESIGN_PREFERENCE`, `EXPERIMENT`, or `DO_NOT_ASSUME`.
- [ ] Check the complete research surface for identity-specific leakage and hemispheric assumptions.
- [ ] Open a Draft PR for warden/repository review without merging.
