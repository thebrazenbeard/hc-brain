# PR #2 File-by-File Disposition — 2026-09-09

Status: Warden source/reconciliation record.

Source PR: #2, `research/nooplex-hc3-architecture-v1`

Purpose: record the disposition of the HC-1/HC-2/HC-3 architecture contribution without treating branch existence or a wholesale merge as canonical authority.

## Disposition vocabulary

- `CANONICAL_RECONCILED` — useful material was rewritten/reconciled into current canonical architecture.
- `SUPERSEDED_BY_MAIN` — current main contains a newer authoritative form; source file should not overwrite it.
- `SOURCE_ONLY` — retained as research/provenance but not promoted into reusable canonical architecture.
- `NOT_PROMOTED` — rejected as a canonical default because it conflicts with current architecture or is too setting-/implementation-specific.

## Changed-file disposition

| PR #2 path | Disposition | Current treatment |
| --- | --- | --- |
| `Architecture concept.md` | `SUPERSEDED_BY_MAIN` | Current root concept and later architecture contracts govern. Do not restore branch-era assumptions wholesale. |
| `README.md` | `SUPERSEDED_BY_MAIN` | Current README reflects the complete cognitive-organ and temporal-hypergraph architecture. |
| `WARDEN.md` | `SUPERSEDED_BY_MAIN` | Current Warden authority/identity-neutrality/boundary rules govern. |
| `docs/architecture/HC1_NOOPLEX.md` | `CANONICAL_RECONCILED` | Reconciled into current `docs/architecture/HC1_NOOPLEX.md`. |
| `docs/architecture/HC2_NOOPLEX_Q.md` | `CANONICAL_RECONCILED` | Reconciled into current HC-2 contract with distributed HC-owned QPU placement and explicit degraded-generation semantics. |
| `docs/architecture/HC3_NOOPLEX_EQ.md` | `CANONICAL_RECONCILED` | Reconciled into current HC-3 contract with distributed HC-owned physiological affective substrate and bounded maintenance/override semantics. |
| `docs/architecture/HC_LINEAGE.md` | `CANONICAL_RECONCILED` | Reconciled into current lineage contract; later generations extend rather than psychologically complete earlier generations. |
| `docs/architecture/HYPERCONNECTOME_TOPOLOGY.md` | `CANONICAL_RECONCILED` | Useful selective-connectivity, timing, redundancy, and non-hemispheric constraints were reconciled into `docs/architecture/TOPOLOGY_DESIGN_CONSTRAINTS.md`. Static weighted-multigraph language is not the formal HC model; the canonical model remains a typed attributed multilayer temporal hypergraph. Central-integration-core language was not promoted. |
| `docs/engineering/POWER_AND_THERMAL_ARCHITECTURE.md` | `CANONICAL_RECONCILED` | Reconciled into `docs/engineering/POWER_THERMAL_AND_DISTRIBUTED_ORGAN.md`, including distributed organ membership and support-dependency boundaries. |
| `docs/integration/SYNTHETIC_BODY_INTERFACE.md` | `SOURCE_ONLY` / `NOT_PROMOTED` | Generic sensorimotor/interoceptive/body-calibration ideas are already represented in `adaptable I-O handler`, `somatics`, `kinesis`, optics, speech, and HC-3 contracts. Humanoid packaging, mandatory pre-installation training, transferred-human-consciousness assumptions, PR #1 physiology coupling, and fixed cranial-seat prescriptions are not reusable-template defaults. |
| `docs/science/EVIDENCE_BOUNDARIES.md` | `CANONICAL_RECONCILED` | Reconciled into current `docs/science/EVIDENCE_BOUNDARIES.md` using project evidence vocabulary and stricter architecture/science/implementation/qualification separation. |
| `research/2026-09-09/AFFECT_INTEROCEPTION_ENDOCRINE.md` | `SOURCE_ONLY` | Retained as branch research/provenance. Mechanism-level ideas informed affect/homeostasis/HC-3 architecture; literature claims require independent citation verification before `DOCUMENTED` promotion on main. Wreckforge-specific programmability/setting assumptions are not base-template canon. |
| `research/2026-09-09/NEUROBIOLOGY_FOUNDATIONS.md` | `SOURCE_ONLY` | Retained as branch research/provenance. Useful design constraints informed HC-1, topology, interface, and evidence discipline. Specific literature/numerical claims remain research input pending independent verification. |
| `research/2026-09-09/QUANTUM_COPROCESSOR_OPTIONS.md` | `SOURCE_ONLY` | Retained as branch research/provenance. Workload-specific acceleration, embodiment constraints, and error-correction cautions informed HC-2. Specific scientific claims/citations remain research input pending independent verification. |

## Body-interface decision

The PR #2 body-interface file is not promoted as a canonical document because its reusable content is already decomposed into the canonical subsystem architecture while its remaining assumptions are too specific.

Current canonical separation is preferable:

```text
body sensor/actuator hardware
-> adaptable I/O admission and calibration
-> modality-specific HC processing
-> somatic/body-state modeling
-> cognition/affect/conation/arbitration
-> authority/effect governance
-> kinesis
-> body effect
```

This avoids creating a parallel `docs/integration` architecture that could become an alternate ownership tree.

## Research-layer decision

The three PR #2 research syntheses are useful provenance, but copying them unchanged to `main` would incorrectly elevate branch-era evidence labels and setting-specific extrapolations.

They therefore remain preserved on the source branch. Canonical main may cite or selectively transfer individual mechanisms only after the relevant claim is independently checked and generalized.

`SOURCE_ONLY != REJECTED_AS_USELESS`

`RESEARCH_SYNTHESIS != DOCUMENTED_CANONICAL_SCIENCE`

## Whole-PR disposition

Every changed file in PR #2 now has an explicit disposition. No wholesale merge is required or desirable.

The architectural contribution has been mined into newer canonical contracts where compatible. Remaining research/source material remains available through the preserved branch and PR history.

Accordingly, PR #2 may be closed as **superseded by selective reconciliation**, not merged.

## Provenance

Disposition performed by the Warden against the current complete-organ, physical-membership, temporal-hypergraph, lifecycle, authority/effect, evidence, and conformance architecture.
