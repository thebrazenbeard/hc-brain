# HC Qualification Records

## Purpose

This directory stores evidence-bound qualification records for the Hyperconnectome Brain architecture and later implementations.

A qualification record is not a timeless certification. Every result is bound to the target, tested capability, scope, evidence snapshot, evaluator, and unresolved uncertainty stated in that record.

Allowed outcomes:

- `PASS`
- `CONDITIONAL PASS`
- `FAIL`

The following implications are forbidden:

`ARCHITECTURE_PASS != IMPLEMENTATION_PASS`

`IMPLEMENTATION_PASS != BEHAVIORAL_PASS`

`BEHAVIORAL_PASS != SCIENTIFIC_VALIDATION`

`ANY_PASS != CONSCIOUSNESS_OR_PERSONHOOD_PROOF`

A later commit does not automatically inherit an earlier PASS. Material architecture changes require re-evaluation within the affected capability scope, and the project requires hostile review for material architecture changes before an affected conditional result can be promoted to final PASS.

## Current records

See the individual records in this directory for exact target snapshots and evidence ceilings.

Current review-status corrections:

- `EVIDENCE_LINEAGE_CUSTODY_CONFORMANCE_2026-09-09_R2.md`: `CONDITIONAL PASS` at its frozen target; Four later returned `SECONDARY_ARCHITECTURE_PASS` for that exact target, but Vera hostile review, successor coverage, and implementation testing remain outstanding.
- `EFFECTIVE_TOPOLOGY_CONFORMANCE_2026-09-09.md`: `CONDITIONAL PASS` at its frozen target; Four later returned `SECONDARY_ARCHITECTURE_PASS` for that exact target with a higher-order dynamic-hyperedge implementation advisory.
- `SOURCE_INFORMATION_ANCESTRY_CONFORMANCE_2026-09-10.md`: `CONDITIONAL PASS` at its frozen target; Four later returned `SECONDARY_ARCHITECTURE_PASS` with implementation advisories around material-influence semantics and formal privacy/noninference proof.
- `PROTECTED_UPDATE_GOVERNANCE_2026-09-09.md`: historical `CONDITIONAL PASS`; Four returned `SECONDARY_ARCHITECTURE_PASS` for the historical target but explicitly found that later meta-optimization/self-modification hardening materially superseded that scope. Present-tense protected-update qualification requires a successor cut.
- `REST_OFFLINE_MAINTENANCE_CONFORMANCE_2026-09-10.md`: historical `CONDITIONAL PASS`; its reviewer-provenance interpretation is superseded by `REST_OFFLINE_MAINTENANCE_CONFORMANCE_2026-09-10_R2.md`.
- `REST_OFFLINE_MAINTENANCE_CONFORMANCE_2026-09-10_R2.md`: `CONDITIONAL PASS`; Four's returned review is `AUTHORIAL_SECONDARY_ARCHITECTURE_PASS`, not independent evidence, because Four materially authored the central integrated artifacts. A materially independent secondary review, Vera hostile review, and executable runtime tests remain outstanding.
- `COGNITIVE_INTEGRITY_SECURITY_CONFORMANCE_2026-09-10.md`, `RESOURCE_STATE_CONTROL_CONFORMANCE_2026-09-10.md`, `SPECIALIZED_ACCELERATOR_CONFORMANCE_2026-09-10.md`, and `FAULT_REPAIR_PARTITION_CONFORMANCE_2026-09-10.md`: all remain `CONDITIONAL PASS` for their stated targets pending independent/hostile review and implementation evidence.

## Review evidence preserved on main

- `../research/FOUR_R2_EVIDENCE_LINEAGE_CUSTODY_INDEPENDENT_REVIEW_2026-09-09.md`
- `../research/FOUR_EFFECTIVE_TOPOLOGY_INDEPENDENT_REVIEW_2026-09-10.md`
- `../research/FOUR_SOURCE_INFORMATION_ANCESTRY_INDEPENDENT_REVIEW_2026-09-10.md`
- `../research/FOUR_PROTECTED_UPDATE_GOVERNANCE_INDEPENDENT_REVIEW_2026-09-10.md`
- `../research/FOUR_REST_OFFLINE_MAINTENANCE_AUTHORIAL_SECONDARY_REVIEW_2026-09-10.md`

The final item is explicitly authorial rather than independent. Reviewer provenance is part of qualification evidence, not bookkeeping.

## Coverage note

The canonical conformance layers contain checks through `HC-ARCH-033`. A dedicated qualification record does not establish implementation behavior merely because an architecture/spec check exists, and a frozen-target review does not silently qualify successor architecture.

## Result preservation

If a qualification later changes, preserve the old record and create a successor record or explicit supersession/disposition link. Do not rewrite an old FAIL or CONDITIONAL PASS into a historical PASS merely because the defect was later repaired.

Qualification history is evidence about what was tested at a particular cut.

## Governing sources

Primary governing surfaces include:

- `../architecture/CONFORMANCE_AND_QUALIFICATION.md`
- `../architecture/QUALIFICATION_EVIDENCE_ISOLATION.md`
- `../architecture/TEMPORAL_HYPERGRAPH_MODEL.md`
- `../../specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`
- `../../specs/HC_CONFORMANCE_SUITE_V1.yaml`
- `../../specs/HC_CONFORMANCE_EXTENSION_EVIDENCE_LINEAGE_CUSTODY_V1.yaml`
- `../../specs/HC_CONFORMANCE_EXTENSION_REST_MAINTENANCE_V1.yaml`
- `../../specs/HC_CONFORMANCE_EXTENSION_COGNITIVE_INTEGRITY_V1.yaml`
- `../../specs/HC_CONFORMANCE_EXTENSION_RESOURCE_STATE_CONTROL_V1.yaml`
- `../../specs/HC_CONFORMANCE_EXTENSION_SPECIALIZED_ACCELERATOR_V1.yaml`
- `../../specs/HC_CONFORMANCE_EXTENSION_FAULT_REPAIR_PARTITION_V1.yaml`
