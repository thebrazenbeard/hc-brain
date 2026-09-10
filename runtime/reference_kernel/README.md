# HC Minimal Reference Kernel

Status: executable prototype / not a cognition engine.

This directory is the first deliberately small executable vertical slice of the Hyperconnectome Brain architecture. It exists to force selected architectural distinctions to survive contact with running code rather than remaining prose-only constraints.

The prototype currently exercises:

- provenance-bearing observations and derived/predicted evidence;
- `ROUTED != INCORPORATED` and `PRIORITY != AUTHORITY`;
- append-oriented current-memory projection with fail-closed competing heads;
- explicit supersession within a logical record scope;
- scoped authority checked at the material effect-request boundary;
- explicit authority-basis/provenance fields on registered grant fixtures;
- revocation/expiry/current-epoch authority semantics;
- `COMMAND_SENT/REQUESTED != EFFECT_CONFIRMED`;
- action-bound observed confirmation evidence rather than arbitrary confirmation IDs;
- duplicate action-request suppression inside the current process model;
- restart fencing of stale plans and pre-restart authority;
- unresolved in-flight effects after restart, requiring reconciliation rather than blind replay.

It intentionally does **not** implement general cognition, semantics, consciousness, learning, distributed coalitions, full temporal-hypergraph execution, deep-memory consolidation, body control, or protected-update activation. Passing these tests therefore establishes only the behavior of this narrow reference slice.

Run from this directory with:

```bash
python -m unittest -v test_hc_kernel.py
```

The prototype uses only the Python standard library.

The exact R2 implementation/test blobs recorded in `docs/qualification/MINIMAL_REFERENCE_KERNEL_VERTICAL_SLICE_2026-09-10_R2.md` were executed together locally and passed all 12 unit-test methods. Hosted GitHub Actions attempts currently fail before the jobs API reports any executed step, so hosted CI is classified as infrastructure-unresolved rather than a unit-test result.

Architectural sources include `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md`, `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`, `current memory storage/CURRENT_STATE_SELECTION.md`, `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`, `kinesis/ACTION_GATEWAY.md`, and `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`.

The governing reality boundary is:

`REFERENCE_KERNEL_TEST_PASS != HC_IMPLEMENTATION_PASS`

`REFERENCE_KERNEL_TEST_PASS != GENERAL_COGNITION`

`REFERENCE_KERNEL_TEST_PASS != SCIENTIFIC_VALIDATION`

`MODELED_RESTART_EPOCH != DURABLE_CRASH_RECOVERY`

`BASIS_BEARING_GRANT_FIXTURE != QUALIFIED_AUTHORITY_ISSUANCE`
