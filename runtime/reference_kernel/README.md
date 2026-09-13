# HC Minimal Reference Kernel

Status: executable prototype / not a cognition engine.

This directory is the first deliberately small executable vertical slice of the Hyperconnectome Brain architecture. It exists to force selected architectural distinctions to survive contact with running code rather than remaining prose-only constraints.

The prototype currently exercises:

- provenance-bearing observations and derived/predicted evidence;
- `ROUTED != INCORPORATED` and `PRIORITY != AUTHORITY`;
- append-oriented current-memory projection with fail-closed competing heads;
- current projections that retain epistemic class and source provenance;
- explicit supersession within a logical record scope;
- scoped authority checked at the material effect-request boundary;
- explicit authority-basis/provenance fields on registered grant fixtures;
- kernel-owned authorization time rather than caller-supplied effect-request time;
- revocation/expiry/current-epoch authority semantics;
- read-only public epoch/state views for authority-relevant kernel stores;
- immutable admitted payload snapshots, authority grants, and effect receipts;
- deterministic candidate-semantic binding for duplicate action IDs;
- `COMMAND_SENT/REQUESTED != EFFECT_CONFIRMED`;
- trusted action-bound observed confirmation evidence rather than arbitrary confirmation IDs;
- generic observations cannot bind effect outcomes without the explicit trusted-source gate, which durable replay rechecks;
- duplicate action-request suppression inside the current process model;
- restart fencing of stale plans and pre-restart authority;
- unresolved in-flight effects after restart, requiring reconciliation rather than blind replay;
- append-journal replay checks for those same narrow invariants.

It intentionally does **not** implement general cognition, semantics, consciousness, learning, distributed coalitions, full temporal-hypergraph execution, deep-memory consolidation, body control, or protected-update activation. Passing these tests therefore establishes only the behavior of this narrow reference slice.

Run the complete current regression surface from this directory with:

```bash
python3 -m unittest -v \
  test_hc_kernel.py \
  test_durable_kernel.py \
  test_four_adversarial_kernel.py \
  test_four_adversarial_kernel_r2.py
```

The prototype uses only the Python standard library.

Qualification history matters:

- the exact R2 implementation/test blobs recorded in `docs/qualification/MINIMAL_REFERENCE_KERNEL_VERTICAL_SLICE_2026-09-10_R2.md` were locally executed together and passed all 12 authored unit-test methods;
- Four independently demonstrated that those 12 green tests were nondiscriminating for caller-controlled authorization time, same-action-ID semantic aliasing, caller payload mutation, and current-projection provenance loss;
- therefore the old 12/12 result must not be cited as evidence that the effect gate was reliable;
- `test_four_adversarial_kernel.py` retains those failures as regression gates and extends them with repair-side attacks against durable replay, returned-state mutation, public state-map mutation, and epoch rewind;
- the current hardening branch remains a repair candidate until its exact executable snapshot is re-run independently. Hosted GitHub Actions attempts continue to fail before runner assignment or any reported step execution, so they remain infrastructure-unresolved rather than unit-test failures.

Architectural sources include `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md`, `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`, `current memory storage/CURRENT_STATE_SELECTION.md`, `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`, `kinesis/ACTION_GATEWAY.md`, and `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`.

The governing reality boundary is:

`REFERENCE_KERNEL_TEST_PASS != HC_IMPLEMENTATION_PASS`

`REFERENCE_KERNEL_TEST_PASS != GENERAL_COGNITION`

`REFERENCE_KERNEL_TEST_PASS != SCIENTIFIC_VALIDATION`

`MODELED_RESTART_EPOCH != DURABLE_CRASH_RECOVERY`

`BASIS_BEARING_GRANT_FIXTURE != QUALIFIED_AUTHORITY_ISSUANCE`
