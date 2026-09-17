# Causal Authority, Recovery, and Partition Hardening V2

Status: DESIGN CANDIDATE / NOT CANONICAL / NOT QUALIFIED

Subject branch base: `3d9df59b2ad8b10f2d46b4dfe67a309e2b02f207` (`noah/reference-kernel-authority-hardening-v1`).

## Purpose

The current HC architecture already separates routing, authority, epistemic support, resource state, temporal-hypergraph state, recovery, reviewer provenance, and effect confirmation. The next hardening step is not another broad conceptual layer. It is to make four existing architectural promises mechanically harder to counterfeit:

1. a grant must not become valid merely because a caller can construct a syntactically valid grant object;
2. restart fencing must become one semantically atomic recovery transition rather than a sequence that can be observed half-applied;
3. partition behavior must be declared per protected state family rather than left as a generic choice among leases, epochs, quorum, consensus, or mergeable island operation;
4. qualification must bind exact source, exact evidence ancestry, reviewer provenance, and architecture/spec conformance through executable checks rather than prose conventions alone.

This design deliberately does not introduce a central executive, one universal consistency algorithm, or a global truth scalar.

## Evidence and architecture basis

The existing architecture already supports this direction:

- `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md` requires explicit, scoped, current, provenance-bearing authority and states that routing, capability, desire, role, and technical access do not create effect permission.
- `BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md` requires recovery epochs or equivalent causal-currentness identities and treats interrupted non-idempotent effects as unresolved until reconciled.
- `FAULT_TOLERANCE_AND_SELF_REPAIR.md` explicitly allows different partition mechanisms but requires each continuity-bearing protected state family to have a declared policy.
- `TEMPORAL_EVENT_CONTRACT.md` rejects insertion order and wall-clock recency as automatic semantic precedence.
- `RUNTIME_COMPONENT_REGISTRATION_AND_STATE_CUSTODY.md` requires all material causal state to have explicit lifetime, referent, durability, recovery, and governance semantics.
- `QUALIFICATION_REVIEWER_PROVENANCE.md` defines independence as scope-relative shaping ancestry, not reviewer label inequality.

External research reinforces but does not dictate the design. Recent network-neuroscience work continues to support dynamic, nonstationary, higher-order interactions rather than one static pairwise graph, while distributed-systems literature emphasizes state-machine replication/consensus as tools whose guarantees depend on the failure and consistency model. Filesystem journaling literature likewise distinguishes a durable transaction commit from a sequence of individually durable writes. These are transfer principles, not claims that HC should copy one biological or distributed-systems implementation.

## Design principle 1 — authority mutation is itself an effect

The current reference kernel checks whether a stored grant allows an effect, but `register_grant()` and `revoke_grant()` accept caller-supplied semantic identities. That means the narrow slice protects consumption of authority more strongly than creation/mutation of authority.

The replacement rule is:

`VALID_GRANT_SHAPE != AUTHORIZED_GRANT_ISSUANCE`

`KNOWN_GRANT_ID != AUTHORIZED_REVOCATION`

### Issuer capability boundary

The reference slice will use the same narrow pattern already proven useful for effect-outcome sources: host-registered opaque in-process capabilities.

Conceptually:

```text
AUTHORITY_ISSUER_REGISTRATION {
  opaque_capability
  principal_id
}
```

A grant-creation request supplies possession of the opaque capability; the kernel derives the grantor principal from the registered capability rather than trusting a caller-supplied grantor label.

A revocation request must likewise carry an issuer/revoker capability. The kernel may permit revocation when the capability principal equals the original grantor in the minimal slice. More complex delegation/revocation ancestry remains an architectural extension and must not be faked by broad string matching.

This mechanism is explicitly an in-process reference boundary, not cryptographic identity proof or process isolation.

## Design principle 2 — recovery fencing is one semantic transaction

The current durable recovery path advances the epoch and then emits one receipt transition per unresolved requested action. A crash or journal failure between those records can leave a durable prefix in which the recovery epoch advanced while only some in-flight effects have been fenced.

The replacement invariant is:

`RECOVERY_EPOCH_ADVANCE <=> ALL_PREVIOUS_EPOCH_REQUESTED_EFFECTS_FENCED`

For the reference journal, recovery will be encoded as one append event whose payload contains:

```text
RECOVERY_FENCE {
  from_epoch
  to_epoch
  requested_action_ids[]
}
```

Replay validates that:

- `to_epoch == from_epoch + 1`;
- `from_epoch` equals the currently reconstructed epoch;
- `requested_action_ids` exactly equals the set of currently `REQUESTED` receipts;
- every listed receipt originates in `from_epoch`;
- applying the event changes the epoch and all those receipts to `UNRESOLVED_AFTER_RESTART` as one in-memory semantic transition.

A missing action, extra action, duplicate, stale epoch, or reordered/replayed fence is journal corruption, not a partially acceptable recovery.

This does not claim a single filesystem append is universally power-loss atomic. The journal's existing integrity model remains a reference-slice limitation. Future torn-tail handling may add explicit transaction framing or a repair/quarantine mode, but this design removes the current *semantic* multi-record recovery split.

## Design principle 3 — partition policy belongs to the state family

The architecture correctly refuses to mandate one distributed-systems algorithm. That freedom is unsafe if an implementation can omit the policy entirely.

Every protected or continuity-bearing distributed state family therefore needs a machine-readable profile:

```text
STATE_FAMILY_CONSISTENCY_PROFILE {
  family_id
  semantic_owner
  consistency_class
  write_authority_model
  causal_metadata
  partition_write_policy
  partition_read_policy
  merge_or_reconciliation_rule
  stale_state_policy
  recovery_fence_policy
  effect_dependency_policy
  qualification_refs[]
  provenance
}
```

Candidate `consistency_class` values describe semantics, not vendor algorithms:

- `SINGLE_WRITER_EPOCH`;
- `QUORUM_COMMITTED`;
- `LINEARIZABLE_REQUIRED`;
- `CAUSALLY_ORDERED`;
- `MERGEABLE_CONCURRENT`;
- `LOCAL_EPHEMERAL`;
- `READ_ONLY_REPLICA`.

Candidate partition write policies include `BLOCK`, `BOUNDED_ISLAND`, and `MERGE_CANDIDATES_ONLY`.

Important default: a protected family without a declared profile is **not** silently treated as eventually consistent. For material writes its distributed conformance state is `UNKNOWN` and the write path fails closed where the policy is required.

The point is not maximum consistency everywhere. Telemetry, ephemeral coalition scratch state, evidence append logs, authority state, identity/continuity state, and effect receipts have different semantics and should be permitted to choose different policies explicitly.

## Design principle 4 — causal frontier is distinct from wall clock

Temporal metadata remains important, but clocks do not by themselves establish semantic precedence under partition or replay.

Where ordering materially affects authority, continuity, reconciliation, or durable state, records should be able to carry a causal frontier or equivalent predecessor set:

```text
CAUSAL_FRONTIER {
  epoch
  predecessor_ids[]
  local_sequence_or_generation
  observed_clock_metadata
}
```

This does not force vector clocks universally. A single-writer epoch may need only `(epoch, generation)`. A mergeable concurrent family may need richer predecessor information. The common invariant is that semantic currentness can be reconstructed without pretending wall-clock recency implies causality.

`LATER_TIMESTAMP != CAUSAL_SUCCESSOR`

## Qualification and review plane

Qualification must not merely say that a reviewer was different from the author. The existing provenance contract already defines shaping ancestry. V2 therefore treats a review receipt as an exact-subject evidence object with at least:

```text
REVIEW_RECEIPT {
  receipt_id
  subject_repo
  subject_head
  reviewed_scope[]
  reviewer_execution_subject
  reviewer_role
  independence_state
  authored_artifact_refs[]
  shaping_or_diagnostic_refs[]
  prior_adjudication_refs[]
  admitted_context_refs[]
  verdict
  evidence_refs[]
  issued_at
  supersedes[]
}
```

A promotion/qualification gate may consume such a receipt. The receipt never grants merge authority.

The repository also needs a separate architecture/spec conformance workflow. It should validate machine-readable files, referenced canonical paths, duplicate IDs, status vocabulary, exact-subject fields where required, and known architecture-to-kernel contract bindings. Kernel unit tests should remain narrow and not become a repository linter.

## Hostile design challenges

### H1 — capability possession becomes universal authority

Counterexample: one issuer handle can mint every action/target scope.

Response: the minimal slice proves issuer authenticity only, not unrestricted semantic jurisdiction. A host policy or later delegation contract must constrain which registered principal may issue which grant class/scope. Qualification must not generalize the narrow slice into complete delegation governance.

### H2 — revocation by original grantor is too weak

Counterexample: emergency or hierarchical revocation may need a different principal.

Response: the reference slice's same-principal rule is intentionally narrow. The architecture record reserves explicit revocation ancestry/policy rather than pretending string equality solves delegation.

### H3 — one recovery record can become huge

Counterexample: millions of in-flight effects make a single fence record impractical.

Response: the reference slice is small. A production design may use transaction framing or a committed recovery manifest plus chunked members. What may not change is the semantic atomicity rule: no externally usable state may claim the new recovery epoch while a subset of prior requested effects remain unfenced.

### H4 — strong consistency everywhere destroys availability

Counterexample: global linearizability would make benign local cognition brittle under partition.

Response: V2 explicitly rejects one global consistency class. The state-family profile exists to permit weaker semantics where safe and stronger semantics where required.

### H5 — causal metadata becomes another truth scalar

Counterexample: a causally later record is assumed more correct.

Response: causal succession establishes dependency/order only. It does not establish epistemic truth, authority, or identity relevance.

### H6 — qualification receipts become self-certifying

Counterexample: a branch adds its own PASS receipt and passes CI.

Response: repository-local structure can verify shape, subject binding, and declared provenance, but cannot independently prove the human/agent/process identity behind a receipt. Acceptance policy must classify the trust root explicitly; exact-head receipt presence is eligibility evidence, not autonomous promotion authority.

## Proposed implementation cut

This branch will implement only the smallest executable vertical slices needed to falsify the three most immediate runtime gaps and the current qualification-process gaps:

1. opaque capability-bound authority issuance/revocation in `ReferenceKernel` and durable replay;
2. single-event atomic recovery fencing in `DurableReferenceKernel`;
3. machine-readable state-family consistency policy schema plus hostile conformance fixtures;
4. machine-readable review receipt schema/validator and a separate repo-wide architecture/spec conformance command/workflow.

It will not implement complete cognition, distributed consensus, cryptographic identities, full delegation law, autonomous merge, or production deployment.

## Claim ceiling

A successful V2 test run would establish only that the named reference mechanisms enforce their declared invariants under the tested fixtures.

`V2_TEST_PASS != COMPLETE_HC_IMPLEMENTATION`

`V2_TEST_PASS != DISTRIBUTED_CONSENSUS_PROOF`

`V2_TEST_PASS != CRYPTOGRAPHIC_IDENTITY_PROOF`

`V2_TEST_PASS != MERGE_AUTHORITY`

`V2_TEST_PASS != CONSCIOUSNESS_OR_PERSONHOOD_PROOF`
