# Fault / Repair / Partition Conformance — 2026-09-10 R2

Status: QUALIFICATION EVIDENCE / REVIEW-PROVENANCE CORRECTION

Architecture target retained from predecessor: `main@045d6ee59ea1cd81e6c466894da082611f05d8e8`

Predecessor: `FAULT_REPAIR_PARTITION_CONFORMANCE_2026-09-10.md`

Result: **CONDITIONAL PASS**

## Why R2 exists

The predecessor correctly bounded its architecture result but listed Four independent review as an outstanding condition. Four's reviewer-provenance audit establishes that Four materially authored/shaped the central fault/repair feeder artifacts, including a byte-identical machine companion admitted from `four/fault-tolerance-v1`.

Four may therefore provide authorial secondary verification and implementation-readiness challenge, but may not satisfy an independent-review condition for this artifact set.

`FOUR_AUTHORSHIP_OR_MATERIAL_SHAPING != FOUR_INDEPENDENT_REVIEW`

`SELECTIVE_CANONICAL_INTEGRATION != INDEPENDENT_REAUTHORSHIP`

## Architecture result retained

The provenance audit asserts no architecture failure. The predecessor's architecture-level `CONDITIONAL PASS` remains supported for its frozen target and stated scope.

## Corrected review conditions

- Warden architecture review: present in predecessor.
- Four authorial secondary / implementation-readiness review: useful if/when supplied, but not independent evidence for this target.
- Materially independent secondary review: **OUTSTANDING**.
- Vera hostile/adversarial review: **OUTSTANDING** unless separately returned and incorporated for this exact target.
- Fault injection, partition/rejoin, repair/verification, regression, and requalification implementation tests: **OUTSTANDING**.

## Result ceiling

`CONDITIONAL_PASS != SELF_REPAIR_IMPLEMENTATION_PASS`

`AUTHORIAL_REVIEW != INDEPENDENT_REVIEW`

`PARTITION_SAFETY_ARCHITECTURE != EXECUTED_PARTITION_RECOVERY_PROOF`

`FROZEN_TARGET_RESULT != CURRENT_MAIN_RESULT`

## Supersession rule

This R2 supersedes the predecessor only for reviewer-provenance interpretation and outstanding review conditions. It does not alter the frozen target or historical evidence record.
