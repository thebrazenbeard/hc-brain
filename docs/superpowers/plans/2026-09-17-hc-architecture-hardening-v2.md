# HC Architecture Hardening V2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make authority mutation, restart fencing, distributed-state consistency semantics, and qualification provenance mechanically enforceable in the HC reference and conformance surfaces.

**Architecture:** Preserve the current narrow reference-kernel boundary. Add opaque issuer capabilities for authority mutation, collapse recovery epoch advancement plus in-flight effect fencing into one semantic journal event, define state-family-specific consistency profiles without mandating one consensus algorithm, and add a separate architecture/spec conformance validator for exact-subject review receipts and machine contracts.

**Tech Stack:** Python 3 standard library, `unittest`, YAML-as-data contracts already used by the repository, GitHub Actions.

**Spec:** `docs/architecture/CAUSAL_AUTHORITY_RECOVERY_HARDENING_V2.md`

## Global Constraints

- No merge, deployment, protected runtime activation, or branch deletion is authorized by this plan.
- `REFERENCE_KERNEL_TEST_PASS != HC_IMPLEMENTATION_PASS`.
- `ROUTING != AUTHORITY` and `VALID_GRANT_SHAPE != AUTHORIZED_GRANT_ISSUANCE`.
- Recovery must not expose a new epoch while only a subset of prior `REQUESTED` effects are fenced.
- No state family may silently inherit a global consistency model.
- Reviewer independence is shaping-ancestry scoped, not reviewer-name inequality.
- Use only Python standard library for executable repository tooling in this cut.

---

### Task 1: Authority issuance/revocation capability boundary

**Files:**
- Modify: `runtime/reference_kernel/hc_kernel.py`
- Modify: `runtime/reference_kernel/durable_kernel.py`
- Create: `runtime/reference_kernel/test_vera_adversarial_kernel_v2.py`

**Interfaces:**
- Consumes: `ReferenceKernel(..., authority_issuer_capabilities=...)`
- Produces: capability-authenticated `register_grant(source_capability=..., ...)` and `revoke_grant(..., source_capability=...)` semantics.

- [ ] **Step 1: Write failing issuer-authenticity tests**

Add tests that construct two opaque objects, register only one as principal `operator-A`, and assert:

```python
with self.assertRaisesRegex(ValueError, "authority issuer capability is not registered"):
    kernel.register_grant(
        source_capability=unknown_handle,
        grantee="planner",
        action_scope="MOVE",
        target_scope="arm",
        basis_refs=("basis:1",),
        valid_from=now,
        expires_at=now + timedelta(minutes=5),
    )
```

Then assert the registered handle produces a grant whose `grantor == "operator-A"`; there is no caller-supplied `grantor` argument.

- [ ] **Step 2: Write failing revocation-authenticity tests**

Create a grant with `operator-A`; attempt revocation using a registered `operator-B` capability and require rejection. Revoke with A and require immutable revocation state.

- [ ] **Step 3: Run the new test module and verify RED**

Run:

```bash
python3 -m unittest -v test_vera_adversarial_kernel_v2.py
```

Expected: failures because `authority_issuer_capabilities` / `source_capability` do not yet exist.

- [ ] **Step 4: Implement minimal opaque capability registration**

Add a normalizer analogous to `_normalize_outcome_source_capabilities`, rejecting scalar/copyable labels as handles and requiring non-empty principal IDs. Add `_principal_for_authority_capability()` using object identity.

Change `register_grant()` so the grantor is derived from the capability. Change `revoke_grant()` so the current minimal policy requires the revoker principal to equal `grant.grantor`.

- [ ] **Step 5: Durable replay remains semantic, not caller-authenticated**

Do not require the historical opaque capability during replay. The durable journal replays already-admitted `AuthorityGrant` state while checking immutable grant semantics, just as outcome-source capabilities are not reconstructed as external live authority. Ensure live mutation still requires the capability.

- [ ] **Step 6: Run targeted and full kernel suites GREEN**

```bash
python3 -m unittest -v test_vera_adversarial_kernel_v2.py
python3 -m unittest -v test_hc_kernel.py test_durable_kernel.py test_four_adversarial_kernel.py test_four_adversarial_kernel_r2.py test_vera_adversarial_kernel_v2.py
```

### Task 2: Atomic recovery fence journal event

**Files:**
- Modify: `runtime/reference_kernel/durable_kernel.py`
- Extend: `runtime/reference_kernel/test_vera_adversarial_kernel_v2.py`

**Interfaces:**
- Produces journal event `RECOVERY_FENCE` with `from_epoch`, `to_epoch`, `requested_action_ids`.

- [ ] **Step 1: Write failing exact-set replay tests**

Construct two `REQUESTED` actions, persist them, then directly create malformed recovery fixtures that omit one action, duplicate an action, add an unknown action, or claim the wrong epoch. Each must raise `JournalIntegrityError` on replay.

- [ ] **Step 2: Write failing one-event recovery test**

After reopening a non-empty journal in recover mode, parse appended journal lines and require exactly one new recovery event for the restart transition, not `EPOCH_SET` plus N receipt transitions.

- [ ] **Step 3: Verify RED**

The current implementation must fail because it emits multiple records and has no exact-set `RECOVERY_FENCE` replay rule.

- [ ] **Step 4: Implement `RECOVERY_FENCE`**

At durable recovery, compute sorted IDs of all current `REQUESTED` receipts. Record one event while still at `from_epoch`; event data includes `from_epoch`, `to_epoch = from_epoch + 1`, and the exact ID list. After durable append succeeds, apply the semantic transition in memory. During replay, validate the exact set and transition epoch plus all receipts together.

- [ ] **Step 5: Preserve ordinary in-memory `ReferenceKernel.restart()` behavior**

Do not claim the non-durable kernel models filesystem crash atomicity. The durable subclass owns journal transaction semantics.

- [ ] **Step 6: Run targeted and full suites GREEN**

Use the same full command from Task 1.

### Task 3: State-family consistency policy contract

**Files:**
- Create: `specs/HC_STATE_FAMILY_CONSISTENCY_POLICY_V1.yaml`
- Create: `docs/architecture/STATE_FAMILY_CONSISTENCY_AND_CAUSAL_FRONTIER.md`
- Create: `tools/validate_hc_architecture.py`
- Create: `tests/test_validate_hc_architecture.py`

**Interfaces:**
- Produces validator function `validate_state_family_profiles(document: dict) -> list[str]` returning deterministic error strings.

- [ ] **Step 1: Write validator tests first**

Fixtures must reject: missing family ID, duplicate IDs, unknown consistency class, protected family with missing partition write policy, `MERGE_CANDIDATES_ONLY` without a reconciliation rule, and material family with no recovery fence policy.

A valid fixture must contain at least distinct profiles demonstrating stronger authority/continuity semantics and weaker telemetry/ephemeral semantics.

- [ ] **Step 2: Verify RED**

Run:

```bash
python3 -m unittest -v tests.test_validate_hc_architecture
```

Expected: import/function missing.

- [ ] **Step 3: Add machine contract and minimal validator**

Use explicit allowed values only. Do not import a YAML dependency: the validator's first executable cut reads JSON-compatible fixture dictionaries in unit tests and performs repository text/static checks for the YAML contract. YAML parsing remains outside this zero-dependency cut.

- [ ] **Step 4: Document causal-frontier semantics**

Specify that causal succession is an ordering/dependency claim only and never promotes truth, authority, or identity relevance. Permit `(epoch, generation)` for single-writer state and richer predecessor sets for mergeable concurrency.

- [ ] **Step 5: Run validator tests GREEN**

### Task 4: Review receipt and architecture/spec conformance gate

**Files:**
- Create: `specs/HC_REVIEW_RECEIPT_V1.yaml`
- Extend: `tools/validate_hc_architecture.py`
- Extend: `tests/test_validate_hc_architecture.py`
- Create: `.github/workflows/architecture-conformance.yml`

**Interfaces:**
- Produces `validate_review_receipt(receipt: dict, *, expected_repo: str, expected_head: str) -> list[str]`.

- [ ] **Step 1: Write failing receipt tests**

Reject receipts with head mismatch, empty reviewed scope, unknown verdict, `INDEPENDENT_WITHIN_DECLARED_SCOPE` plus non-empty material shaping refs for the same scope, missing execution subject, and a receipt that attempts to encode merge authority.

Accept a scoped `OPEN_REVIEW`/technical review receipt even when it is not independent, as long as it does not satisfy an independent-review requirement.

- [ ] **Step 2: Verify RED**

- [ ] **Step 3: Implement minimal deterministic validator**

The validator checks shape, vocabulary, exact subject equality, and internal provenance contradictions. It must explicitly state that repository-local validation cannot cryptographically prove reviewer identity.

- [ ] **Step 4: Add separate architecture workflow**

The workflow runs `python3 -m unittest -v tests.test_validate_hc_architecture` and a repository validator command. It must remain separate from `.github/workflows/reference-kernel.yml`.

- [ ] **Step 5: Run all repository-local tests GREEN**

### Task 5: Hostile self-review and repair pass

**Files:**
- Create: `docs/qualification/VERA_HOSTILE_SELF_REVIEW_HC_HARDENING_V2_2026-09-17.md`
- Modify earlier V2 files only if findings require repair.

**Interfaces:**
- Produces a finding ledger with severity, exact subject head, counterexample, disposition, repair commit, and residual uncertainty.

- [ ] **Step 1: Attack capability security**

Try handle aliasing, scalar handles, duplicate registration, caller-supplied principal spoofing, foreign revocation, post-registration object mutation, and durable replay without live issuer handles.

- [ ] **Step 2: Attack recovery semantics**

Try omitted IDs, duplicate IDs, unknown IDs, wrong from/to epoch, replayed fence, already-unresolved receipts, zero-request recovery, and journal write exception before the semantic transition.

- [ ] **Step 3: Attack consistency profiles**

Try global-one-size-fits-all policy, undefined protected family, causal-later-as-truth, merge-without-conflict preservation, and availability claims that silently permit protected writes during partition.

- [ ] **Step 4: Attack qualification mechanics**

Try stale head, self-PASS, reviewer-label laundering, missing shaping ancestry, scope laundering, and a receipt that implies merge authority.

- [ ] **Step 5: Repair every material finding with a new RED→GREEN cycle**

Do not edit the test to accommodate a defect unless the design itself is revised and the review ledger records why.

### Task 6: PR and exact-head evidence

**Files:**
- Update: `docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md` only to the evidence level actually earned.
- Update: `docs/qualification/HOSTILE_AUDIT_DISPOSITION_2026-09-15.md` with successor status, preserving history.

- [ ] **Step 1: Run complete relevant tests from a clean checkout**

Record exact branch head, Python version, command, pass/fail counts, and any unavailable CI evidence.

- [ ] **Step 2: Open a draft stacked PR against `noah/reference-kernel-authority-hardening-v1`**

The PR body must distinguish base dependency, exact head, source evidence, authorial test evidence, hostile self-review, unresolved independent review, and claim ceiling.

- [ ] **Step 3: Review the PR as an adversary**

Do not approve it. Add concrete findings or a bounded `COMMENT` review tied to the exact head. Any repair moves the head and invalidates the previous exact-head self-review as current qualification evidence.

- [ ] **Step 4: Leave final status as candidate**

No merge or canonical promotion without separate exact authority and the required independent review provenance.
