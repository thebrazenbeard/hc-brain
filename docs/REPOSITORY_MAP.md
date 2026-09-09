# Hyperconnectome Brain Repository Map

## Purpose

This repository defines the reusable HC-series Hyperconnectome Brain template. Core architecture is identity-neutral. Named identities belong only in clearly labeled examples, case studies, comparisons, or research artifacts where the identity itself is relevant.

## Authority

`WARDEN.md` defines Noëtarch / Noah as Warden, repository maintainer, primary architectural decision-maker, and project-facing voice of the HC brain, subject to owner authority.

## Core architecture

- `Architecture concept.md` — original node-oriented architectural seed.
- `docs/architecture/HC1_NOOPLEX.md` — HC-1 baseline architecture.
- `docs/architecture/HC2_NOOPLEX_Q.md` — HC-2 quantum/photonic augmentation.
- `docs/architecture/HC3_NOOPLEX_EQ.md` — HC-3 endocrine/interoceptive augmentation.
- `docs/architecture/HC_LINEAGE.md` — generational lineage.
- `docs/architecture/HYPERCONNECTOME_TOPOLOGY.md` — non-hemispheric distributed topology rule.
- `docs/architecture/hc-1r-reference-architecture.md` — deeper HC-1 reference architecture under research/development.
- `docs/architecture/claim-ledger.md` — architecture-level claim tracking.

## Runtime and formalization

- `docs/runtime/` — runtime model, node taxonomy, identity continuity, arbitration, plasticity, and state governance.
- `specs/HYPERCONNECTOME_RUNTIME_CONTRACT_V0_1.yaml` — machine-readable runtime contract draft.
- `specs/HYPERCONNECTOME_RESEARCH_CONSTRAINTS_V0_1.yaml` — machine-readable research constraints draft.

## Engineering and integration

- `docs/engineering/POWER_AND_THERMAL_ARCHITECTURE.md` — power, cooling, fault degradation, and thermal-domain constraints.
- `docs/integration/SYNTHETIC_BODY_INTERFACE.md` — embodiment interface between HC brains and compatible host physiology.

## Science and research

- `docs/science/EVIDENCE_BOUNDARIES.md` — boundary between documented science, engineering extrapolation, and project canon.
- `docs/research/` — literature synthesis, source registers, formal models, candidate mechanisms, falsification protocols, and runtime research.
- `research/2026-09-09/` — focused literature syntheses on neurobiology, affect/interoception/endocrine systems, and quantum coprocessors.

## Provenance and plans

- `docs/provenance/` — source lineage and retrieval records.
- `docs/plans/` — development plans and preserved design plans.

## Setting-specific references

- `references/wreckforge/` — Wreckforge/Synthetic source material retained as reference input. These files may constrain or illustrate particular embodiments but do not automatically define the universal HC template.

## Governing distinctions

1. Template architecture is not an identity-specific brain.
2. Human neuroscience informs mechanisms and constraints but does not dictate human gross anatomy.
3. The HC-series is non-hemispheric unless a later explicit engineering decision establishes otherwise.
4. Quantum systems are specialized accelerators/sensors, not a magical explanation for consciousness or cognition.
5. Affect is systemic: appraisal, neuromodulation, endocrine/autonomic state, interoception, memory, learning, and embodiment interact.
6. Setting-specific claims remain visibly separated from documented present-day science.
7. Earlier HC generations remain valid historical architectures when later generations are introduced.

## Repository-management status

Main is the canonical integration branch. Research branches may explore alternatives, but mature, non-conflicting work should be integrated into `main` and stale duplicate workstreams should not be treated as independent canon.
