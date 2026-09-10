# Fault / Repair / Partition Conformance — 2026-09-10

Status: QUALIFICATION EVIDENCE

Target architecture snapshot: `main@045d6ee59ea1cd81e6c466894da082611f05d8e8`

Result: **CONDITIONAL PASS**

## Tested capability

Architecture-level fault evidence, competing cause hypotheses, bounded degraded-capability description, scoped containment, repair proposal/application/verification, regression/requalification separation, and distributed HC partition/rejoin semantics without redefining canonical lifecycle, recovery, authority, protected-update, memory/currentness, or organ membership.

## Evidence inspected

- `basic operating instructions/FAULT_TOLERANCE_AND_SELF_REPAIR.md`
- `specs/HC_FAULT_REPAIR_OBJECTS_V1.yaml`
- `specs/HC_CONFORMANCE_EXTENSION_FAULT_REPAIR_PARTITION_V1.yaml`
- canonical bootstrap/recovery, lifecycle, authority/effect, protected-update, cognitive-integrity, physical-organ membership, resource-state, memory/currentness, and resolver contracts referenced by those files.

The fault/repair pair was selectively reviewed from Four's `four/fault-tolerance-v1` feeder rather than merging stale branch history wholesale.

## Observed architecture evidence

PASS at the inspected architecture-contract level:

- fault detection and root-cause knowledge are distinct;
- diagnostic measurements, derived state, and cause hypotheses remain epistemically separate;
- every material fault binds an exact subject/revision and preserves append-oriented history;
- degraded capability describes retained/unavailable function without redefining canonical health state;
- fallback service does not mark the original subject repaired;
- containment remains scoped and authority-bound rather than becoming a local executive;
- repair proposal, authorization, application receipt, verification, regression, and full requalification are separate states/evidence objects;
- verification modality is subject-appropriate rather than universally assuming direct readback;
- HC-internal partition does not convert remote constituents into external peripherals or independent successor minds;
- continuity-bearing protected state requires a declared partition policy compatible with canonical recovery/currentness semantics;
- rejoin/fork continuity remains governed by canonical memory/recovery rather than timestamp-only conflict resolution;
- alarm suppression or sensor loss does not establish health;
- diagnostic observability does not create write/identity/memory/value/consent authority.

## Adversarial checks applied

The architecture was checked against ambiguous root cause, muted alarms, fallback-as-repair, applied-but-unverified repair, local verification mistaken for requalification, unauthorized repair, repair/revision mismatch, distributed constituent disconnection, unsafe island writes, divergent rejoin, sensor loss, rerouting mistaken for repair, fault-priority authority leakage, and mismatched verification modality.

No contradiction was found in the inspected architecture cut.

## Why this is not PASS

No concrete HC implementation has yet demonstrated fault injection, partition/rejoin behavior, repair application, causal diagnosis, regression, continuity-safe reconciliation, or post-repair requalification. Four independent review and Vera hostile review for this exact cut have not yet been incorporated.

Therefore the strongest justified result is **CONDITIONAL PASS**.

## Remaining uncertainty

UNKNOWN at this cut:

- concrete partition protocol and protected-state policies for a physical HC implementation;
- detection latency, diagnostic accuracy, false-positive/false-negative behavior, and containment blast radius;
- repair authority envelopes for substrate-specific routine maintenance;
- physical destruction thresholds beyond which continuity cannot be preserved;
- regression and requalification coverage needed for each repair class;
- independent reviewer findings for this exact snapshot.

Later commits do not inherit this qualification result automatically.
