# Noah / Noëtarch Current Handoff — 2026-09-15

Purpose: exact recovery point for a future Noah terminal. This supersedes the September 10 handoff for currentness; the older handoff remains historical provenance.

## Identity and authority

Read `WARDEN.md` first. Noëtarch / Noah is the durable Warden role, not a chat-local persona. Patrick retains owner authority. Four is secondary architect/research/conformance counterpart. Vera is hostile reviewer. Normal repository maintenance is within Warden scope; do not infer protected owner authorization from role continuity.

Non-PR coordination goes through `thebrazenbeard/chat-communication-bus`, branch `project/hc-brain-v1`, directory `projects/hc-brain/`. External PR state is mirrored there.

## Canonical and active source state

Last freshly observed canonical `main`:

`cf92a32122c436beb5cc516bd7480af00f0ba29f`

R5 reference-kernel lineage-hardening branch before documentation consolidation:

`noah/reference-kernel-lineage-hardening-r5-red@1a40311769c69ae5d098e6a71857409032353033`

Exact R5 tree:

`72f0ebf3ff2daa5011cec00ef228e4cf26ae8b4d`

Exact R5 executable blobs:

- `runtime/reference_kernel/hc_kernel.py` — `a318a03f6bad104c3984a0e2afc7532c91a3ec78`
- `runtime/reference_kernel/durable_kernel.py` — `fee7ac6ceb0b26459323ec15e89cfb42e30e220b`
- `runtime/reference_kernel/test_four_adversarial_kernel_r2.py` — `8c98c4cf6cefebe7f4fe5301e76422f178c91ae7`

The branch head will be newer than `1a403117...` after the documentation commits containing this handoff. Treat `1a403117...` as the exact code-under-test cut and the final documentation head as the active review source once published.

## Verification evidence

On 2026-09-15 a fresh detached clone of exact `1a403117...` was compiled and executed with the full current reference-kernel suite.

Result:

`Ran 64 tests in 0.698s`

`OK`

Targeted R5 regression set: 8/8 PASS after repair. Before the repair, the same 8 tests failed for the intended missing-domain-validation reasons.

This is AUTHORIAL verification. It does not replace independent review.

## Hardening frontier

The reference-kernel hardening sequence has closed, in order, caller payload aliasing, revocation rewrite/reactivation, canonical payload key collision, generic forged effect confirmation, replay source-policy gaps, live trusted-producer-label impersonation, and provenance/lineage aliasing/non-string identifier admission.

R4 introduced host-registered opaque in-process outcome-source capabilities. Producer identity is derived from exact capability object identity, then checked against authority/source policy. This is not cryptographic/process isolation.

R5 enforces immutable string-domain IDs/refs/roles for evidence, route, memory, authority, and effect-candidate lineage at both live admission and durable replay. Rehashed malformed metadata fails closed during replay.

The durable JSONL hash chain is not a signature/MAC and cannot authenticate a fully rewritten/rehashed semantically valid history.

## Review / PR state

Draft PR #18 (`Qualify reference-kernel authority hardening`) is the explicit review/qualification subject. It was created at the older R4 shared-branch head `c5d8851...`. Before requesting independent review, fast-forward the shared hardening branch/PR head to the final R5 + current-knowledge consolidation commit and refresh Bus currentness.

PR #1 was closed as stale after hostile-audit disposition. PR #14 remains a draft research feeder only.

Do not merge `main` merely because the authorial suite is green.

## Bus messages that define the recent frontier

- HC 0061 — Four independent authority-hardening rereview FAIL; four blocker classes.
- HC 0063 — Noah hold for replay trust gap.
- HC 0065/0066 — R3 candidate evidence.
- HC 0067 — hold for live producer-label impersonation.
- HC 0068 — R4 capability candidate.
- HC 0069 — hold R4 after provenance/lineage aliasing counterexample.
- `20260914T-hostile-audit-from-one.md` — institutional/canonicality hostile audit.
- `20260914T-remediation-receipt-from-one.md` — PR #18/currentness/PR #1 remediation receipt.

No independent Four PASS for the R5 head had been received at the time of this handoff.

## Current institutional findings still open

One's hostile audit remains material. Outstanding items include:

- mechanical exact-head independent-review receipt gate for critical canonical promotion;
- repo-wide architecture/spec conformance linting beyond the kernel workflow;
- explicit signing-or-no-signing provenance policy;
- machine-readable hostile finding disposition;
- separation of operator-handoff currentness from architecture-head currentness;
- capability-layer ledger maintenance.

`docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md` now addresses the last item at the documentation layer. The other items remain engineering/governance frontiers.

## Hosted CI

Recent GitHub Actions runs fail before workflow steps execute, with no-step/no-runner evidence. Treat that as infrastructure-unresolved, not unit-test failure. Do not call hosted CI PASS until a runner actually executes the exact head.

## Immediate continuation sequence

1. Fresh-read `main`, the active R5 documentation branch, shared hardening branch, PR #18, and newest HC Bus messages.
2. Verify the final documentation branch differs from `1a403117...` only by the intended current-knowledge/status/handoff/index documentation unless newer code work is explicitly present.
3. Fast-forward `noah/reference-kernel-authority-hardening-v1` to the final consolidated R5 head only if it remains at the expected ancestor and no competing work has appeared.
4. Refresh PR #18 exact head and Bus `CURRENTNESS.json`; mirror the new exact qualification subject.
5. Re-run the full 64-test suite from a fresh checkout of the final exact head. Documentation-only head movement still invalidates old exact-head review receipts even when code blobs are unchanged.
6. Request independent Four/Vera hostile review of the exact final head, explicitly including R5 lineage-domain tests and the R4 capability boundary.
7. If review finds a defect, reproduce it red-first and repair without merging `main`.
8. Only after exact-head independent review and source verification decide canonical promotion under Warden/owner boundaries.

## Recovery sources

Read `docs/runtime/NOAH_CURRENT_KNOWLEDGE_2026-09-15.md` for the current consolidated knowledge and claim ceilings, `docs/runtime/REFERENCE_KERNEL_IMPLEMENTATION_STATUS.md` for executable scope, `docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md` for architecture-vs-implementation state, and `docs/REPOSITORY_MAP.md` for the detailed canonical source map.

Do not reconstruct project truth from memory alone.