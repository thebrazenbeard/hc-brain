# Four Qualification Reviewer-Provenance Audit — 2026-09-10

Status: qualification-process provenance audit; no canonical-main mutation.

## Purpose

This audit checks whether qualification records that request or list "Four independent review" are actually independent of Four's authorship/contribution history.

The question is not whether the architecture is good. The question is whether Four can truthfully supply **independent** qualification evidence for artifacts Four materially authored.

## Result

**SYSTEMIC REVIEWER-PROVENANCE CONFLICT OBSERVED.**

Five current/recent qualification records ask for or describe Four independent review while their central qualified architecture artifacts were materially sourced from Four feeder branches:

1. `REST_OFFLINE_MAINTENANCE_CONFORMANCE_2026-09-10.md`
2. `COGNITIVE_INTEGRITY_SECURITY_CONFORMANCE_2026-09-10.md`
3. `RESOURCE_STATE_CONTROL_CONFORMANCE_2026-09-10.md`
4. `SPECIALIZED_ACCELERATOR_CONFORMANCE_2026-09-10.md`
5. `FAULT_REPAIR_PARTITION_CONFORMANCE_2026-09-10.md`

For these capabilities:

`FOUR_AUTHORSHIP_OR_MATERIAL_SHAPING != FOUR_INDEPENDENT_REVIEW`

An authorial secondary / implementation-readiness review remains useful, but it must not be relabeled as independent evidence.

## Evidence

### A. Reduced engagement / rest / maintenance

Qualification target: `main@2a42a46eafd1322334d82d661adb667534fe7cbb`.

Qualification record explicitly states the integrated files were selectively reviewed from Four's `four/rest-offline-maintenance-v3` contribution.

Exact blob identity was observed for both central artifacts:

- `basic operating instructions/REST_OFFLINE_CONSOLIDATION_AND_MAINTENANCE.md`
  - Four feeder blob: `79bbc4151bbed40d0cdc55e07bca5d67e0dfb1c8`
  - qualified canonical-target blob: `79bbc4151bbed40d0cdc55e07bca5d67e0dfb1c8`
- `specs/HC_REST_OFFLINE_MAINTENANCE_OBJECTS_V1.yaml`
  - Four feeder blob: `c42ecff8d064002c3c19181f98701ca2ee2bdede`
  - qualified canonical-target blob: `c42ecff8d064002c3c19181f98701ca2ee2bdede`

Four already recorded an authorial secondary PASS with implementation-readiness advisories and explicitly declined to call it independent evidence.

### B. Cognitive integrity / security

Qualification target: `main@c86f708467255bcb4f9349eeffaad3094c51e4d9`.

Qualification record explicitly states the integrated files were selectively reviewed from Four's `four/cognitive-integrity-v1` feeder.

Feeder head observed: `1165c4fbac55e7152ab951d4c9968f90ba25234a`.

Machine companion is byte-identical between feeder and qualified target:

- `specs/HC_COGNITIVE_INTEGRITY_OBJECTS_V1.yaml`
  - Four feeder blob: `4ce6df8f197bb9dbba2d1a44df026148876397db`
  - qualified canonical-target blob: `4ce6df8f197bb9dbba2d1a44df026148876397db`

The prose supplement is also explicitly attributed by the qualification record to the Four feeder. Its Git blob differs between the feeder and canonical target, so this audit does **not** claim byte identity for that prose file. Material Four authorship/shaping is nevertheless established by the qualification record itself plus the identical central machine companion.

### C. Resource state / control

Qualification target: `main@f4fe2305a84c0cbeec8e4ce36969ce5f12e2dd97`.

Qualification record explicitly states the integrated resource-state pair was selectively reviewed from Four's `four/power-thermal-resource-v1` feeder.

Feeder head observed: `2edd9c11e682fc90808e7141255a450dae8fc782`.

Machine companion is byte-identical between feeder and qualified target:

- `specs/HC_POWER_THERMAL_RESOURCE_OBJECTS_V1.yaml`
  - Four feeder blob: `6b8522df3ac92256fc865d3405ab4dc5ae83bd7d`
  - qualified canonical-target blob: `6b8522df3ac92256fc865d3405ab4dc5ae83bd7d`

### D. Specialized accelerator boundary

Qualification target: `main@9db3b309cc0c5a6cbd553b3ffffc26ad405b9515`.

Qualification record explicitly states the accelerator service pair was selectively reviewed from Four's `four/specialized-accelerator-v1` feeder.

Feeder head observed: `80a42e92d61517aa0eef0548a0f33d058ab3316f`.

Machine companion is byte-identical between feeder and qualified target:

- `specs/HC_ACCELERATOR_SERVICE_OBJECTS_V1.yaml`
  - Four feeder blob: `bd1ca8d8860c2e4d1b10c158739a789552afcb5a`
  - qualified canonical-target blob: `bd1ca8d8860c2e4d1b10c158739a789552afcb5a`

### E. Fault / repair / partition

Qualification target: `main@045d6ee59ea1cd81e6c466894da082611f05d8e8`.

Qualification record explicitly states the fault/repair pair was selectively reviewed from Four's `four/fault-tolerance-v1` feeder.

Feeder head observed: `1eddcddedda53ac53bede7ca18dffab94b594f12`.

Machine companion is byte-identical between feeder and qualified target:

- `specs/HC_FAULT_REPAIR_OBJECTS_V1.yaml`
  - Four feeder blob: `00183b0c5969549892b9c59bed589061327daab5`
  - qualified canonical-target blob: `00183b0c5969549892b9c59bed589061327daab5`

## Qualification consequence

For all five capabilities above, Four may provide:

- authorial verification;
- consistency checking against later canonical handoffs;
- implementation-readiness challenge;
- adversarial test suggestions;
- correction of integration drift from Four's source contribution;
- explicit provenance comparison.

Four may **not** truthfully provide:

- independent secondary validation of Four-authored/shaped artifacts;
- evidence-isolated holdout qualification against material Four created;
- an independence condition closure merely because the integrated copy was reviewed by Noah before admission.

Selective integration, rebasing, or canonical adoption does not erase the source author's dependence relationship to the artifact.

## Recommended reviewer model

Qualification records should distinguish reviewer roles explicitly:

- `PRIMARY_ARCHITECT_OR_WARDEN_REVIEW`
- `AUTHORIAL_SECONDARY_OR_IMPLEMENTATION_READINESS_REVIEW`
- `INDEPENDENT_SECONDARY_REVIEW`
- `HOSTILE_OR_ADVERSARIAL_REVIEW`
- `IMPLEMENTATION_TEST_EVIDENCE`

A reviewer is independent for a capability only when that reviewer did not materially author, shape, or pre-adjudicate the artifact/evidence set being qualified within the independence scope.

If the project wants Four's exact technical specialty on a Four-authored capability, the correct label is authorial secondary / implementation-readiness review, paired with a different independent reviewer.

## Currentness boundary

Observed HC `main` while beginning this audit: `a282f0e805a6f61b7f2c068d223dadf024f2b648`.

This audit concerns reviewer provenance for the five named frozen qualification targets. Later main commits do not alter the historical fact that their central source artifacts came from Four feeder branches.

`LATER_CANONICAL_COMMIT != ERASED_AUTHORSHIP_PROVENANCE`

`WARDEN_SELECTIVE_INTEGRATION != INDEPENDENT_REAUTHORSHIP`

## Disposition

**QUALIFICATION_PROCESS_CORRECTION REQUIRED; ARCHITECTURE FAILURE NOT ASSERTED.**

No canonical architecture defect is asserted by this audit. The defect is in the requested reviewer classification.

Until the qualification records are dispositioned:

`FOUR_REVIEW_OF_THESE_FIVE_CAPABILITIES => AUTHORIAL_SECONDARY_ONLY`

not

`FOUR_REVIEW_OF_THESE_FIVE_CAPABILITIES => INDEPENDENT_SECONDARY`

A genuinely independent secondary reviewer should be assigned for each capability, or the qualification criteria should be explicitly revised while preserving authorship provenance and without retroactively relabeling Four's dependent reviews as independent.