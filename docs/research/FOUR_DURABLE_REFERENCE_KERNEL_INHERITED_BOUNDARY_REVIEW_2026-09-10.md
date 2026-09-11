# Four Static Implementation Review — Durable Reference Kernel Inherited Boundaries — 2026-09-10

Status: independent static implementation review of current durable-kernel artifacts; no canonical-main mutation; no independent runtime execution claim for this durable pair in this record.

## Target

Observed canonical cut during review:

`main@cf92a32122c436beb5cc516bd7480af00f0ba29f`

Reviewed current blobs:

- `runtime/reference_kernel/durable_kernel.py` = `3564c5bc2fc2050ca57db0834f883350acf874a5`
- `runtime/reference_kernel/test_durable_kernel.py` = `0f2f8940ab002a8bc9397f3c6eeeabcb704cd327`
- inherited base `runtime/reference_kernel/hc_kernel.py` = `e48355da01482cc6ca709928214ad61c9998249e`

This follows Four's independent implementation review of the base kernel, which found two BLOCKERs in effect-gate semantics and two material evidence/currentness issues.

## Disposition

**DURABLE IMPLEMENTATION REMAINS BLOCKED ON INHERITED EFFECT-GATE SEMANTICS.**

The durable journal substantially improves replay integrity and crash/reopen evidence, but its effect-request path explicitly delegates to the unchanged base implementation:

```text
def request_effect(self, candidate, **kwargs):
    existed = candidate.action_id in self.effect_receipts
    receipt = super().request_effect(candidate, **kwargs)
    if existed:
        return receipt
    ... journal new receipt ...
```

Therefore durability does not independently repair the two base-kernel authorization/idempotency BLOCKERs.

## Inherited BLOCKER A — caller-controlled authorization time

`DurableReferenceKernel.request_effect()` forwards arbitrary `**kwargs` to `ReferenceKernel.request_effect()`, including the public `now=` value used for authority currentness.

The base counterexamples therefore remain reachable through the durable API:

- expired authority can be evaluated at a caller-selected historical time inside the grant window;
- revoked authority can be evaluated at a caller-selected pre-revocation time.

The journal will then durably record the resulting `REQUESTED / AUTHORIZED` receipt.

This is worse than merely failing to detect a stale grant after restart: the durable system can faithfully preserve an authorization decision whose currentness was selected by the requester.

`DURABLE_RECORD_OF_AUTHORIZATION != TRUSTWORTHY_AUTHORIZATION_DECISION`

Cheapest repair remains a trusted/kernel-owned clock dependency, with any fake clock injected at kernel construction/test environment rather than at the effect-request call boundary.

## Inherited BLOCKER B — same action ID can alias different candidate semantics

The durable method checks whether `candidate.action_id` already exists, delegates to the base method, then returns immediately for an existing receipt.

The base method also returns the existing receipt before comparing candidate semantics.

Therefore a same-ID/different-content candidate can inherit a prior authorized receipt in the durable API just as in the in-memory API.

The journal cannot detect the mismatch because effect receipts do not currently preserve a canonical candidate fingerprint containing origin/action/target/payload/authority/epoch identity.

On replay, the receipt is internally consistent with itself while the candidate whose semantics originally justified it is absent from the journaled receipt state.

`JOURNAL_INTEGRITY != CANDIDATE_RECEIPT_BINDING_INTEGRITY`

Cheapest repair:

- journal/register canonical effect-candidate identity or digest before/with the first effect request;
- bind receipt to that candidate identity;
- on duplicate action ID require exact semantic match;
- fail closed on any same-ID mismatch.

## Material inherited issue — mutable live payload can diverge from durable replay payload

Durable admission calls `_ensure_jsonable(payload)`, then stores the original caller payload through the inherited base record, then serializes it into the journal.

Because the inherited record retains the original mutable object by reference, a caller can mutate that object after the journal write.

Result:

- live in-memory record may change under the same ID;
- durable journal retains the original serialized value;
- reopening the journal reconstructs the original value, not the mutated live value;
- the runtime can therefore have two values for the same record identity depending on whether state is live or replayed.

This is a stronger manifestation of the base mutable-payload finding:

`LIVE_STATE_AFTER_ALIAS_MUTATION != JOURNALED_STATE_FOR_SAME_RECORD_ID`

without any journal event documenting the change.

Cheapest repair: canonicalize/deep-copy to an immutable representation before both in-memory admission and journal serialization, ideally binding content digest to record identity/provenance.

Recommended hostile test:

1. admit mutable dict payload;
2. capture record/journal;
3. mutate original caller dict;
4. assert live record remains unchanged;
5. reopen in inspect mode;
6. assert live-before-reopen and replayed state are identical.

## Current-projection typing issue also remains inherited

`JournaledCurrentMemory` subclasses `CurrentMemory` and does not override `current()`.

Therefore the public projection still returns payload/head IDs without selected-head epistemic class/source metadata.

The journal preserves the backing record's class/source information; the projection API still makes consumers dereference separately to avoid class laundering.

This is not a journal corruption defect but remains a read-boundary precision issue.

## Durable test-suite assessment

The current durable suite meaningfully exercises:

- memory ambiguity across reopen;
- derived evidence lineage replay;
- in-flight requested effect -> unresolved on reopen;
- stale old-epoch authority after reopen;
- confirmed effect persistence;
- entry hash corruption;
- sequence discontinuity despite attacker rehash;
- event epoch mismatch despite rehash;
- grant-without-basis replay corruption;
- missing derived parent replay corruption;
- confirmation receipt rebound to wrong evidence;
- rejection of unserializable payload before mutation;
- read-only/nonmutating inspection;
- durable reconciliation;
- separate-process reopen semantics.

Those tests provide useful durability/replay evidence. They do not discriminate:

- caller-backdated authority;
- same action ID with altered candidate semantics;
- mutation of a JSON-serializable payload after admission;
- live-versus-replayed content equality after such mutation;
- epistemic classification retention at the current-projection return boundary.

## Evidence ceiling

This static review does not claim the durable test suite itself fails when executed. It establishes that the current source path inherits counterexamples already executable against the unchanged base implementation and that the authored durable tests do not currently cover them.

`DURABLE_JOURNAL_HARDENING != EFFECT_GATE_REPAIR`

`HASH_CHAIN_VALID != AUTHORIZATION_DECISION_VALID`

`REPLAY_CONSISTENT != LIVE_STATE_IMMUTABLE`

`DURABLE_REFERENCE_KERNEL_REVIEW != HC_IMPLEMENTATION_PASS_OR_FAIL`

Recommended sequencing: repair the base effect-gate/time/idempotency semantics first, add regression tests to both base and durable suites, then perform exact-blob durable execution/qualification on the repaired cut.
