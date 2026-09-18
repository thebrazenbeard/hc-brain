# Causal Authority, Recovery, and Partition Hardening V2

Status: DESIGN CANDIDATE / NOT CANONICAL / NOT QUALIFIED

Subject branch base: `3d9df59b2ad8b10f2d46b4dfe67a309e2b02f207` (`noah/reference-kernel-authority-hardening-v1`).

## Purpose

The current HC architecture already separates routing, authority, epistemic support, resource state, temporal-hypergraph state, recovery, reviewer provenance, and effect confirmation. V2 makes four existing promises mechanically harder to counterfeit:

1. a grant must not become valid merely because a caller can construct a valid object or possess an authenticated issuer handle;
2. restart fencing must become one semantically atomic recovery transition rather than a sequence that can be observed half-applied;
3. partition behavior must be declared per protected state family rather than left as a generic choice among leases, epochs, quorum, consensus, or mergeable island operation;
4. qualification must bind exact source, exact evidence ancestry, reviewer provenance, and architecture/spec conformance through executable checks rather than prose conventions alone.

This design deliberately does not introduce a central executive, one universal consistency algorithm, or a global truth scalar.

## Design principle 1 — authority mutation is itself an effect

The predecessor kernel protects consumption of stored authority more strongly than creation/mutation of authority. V2 separates two questions that must both pass:

`WHO_IS_REQUESTING_ISSUANCE?`

`IS_THAT_PRINCIPAL_ALLOWED_TO_ISSUE_THIS EXACT GRANT IN THIS CURRENT TEMPORAL/EPOCH CONTEXT?`

Therefore:

`VALID_GRANT_SHAPE != AUTHORIZED_GRANT_ISSUANCE`

`AUTHENTICATED_ISSUER != UNLIMITED_ISSUANCE_JURISDICTION`

`KNOWN_GRANT_ID != AUTHORIZED_REVOCATION`

### Issuer capability boundary

The reference slice uses host-registered opaque in-process capabilities. A grant request supplies the opaque capability; the kernel derives the grantor principal by object identity rather than trusting a caller-supplied label.

This authenticates only the in-process principal identity used by the narrow reference slice.

### Issuance-jurisdiction policy

The kernel separately consults a host-owned policy over one immutable `AuthorityIssuanceRequest` containing:

- issuer principal;
- grantee;
- action scope;
- target scope;
- basis refs;
- `valid_from`;
- `expires_at`;
- kernel-observed current time;
- current recovery epoch.

Missing policy fails closed. Policy denial prevents grant creation. This lets one policy enforce semantic jurisdiction and temporal/currentness bounds together rather than authenticating a principal and then silently accepting any validity interval.

The kernel binds the configured policy ID into reserved grant provenance. Caller-supplied provenance cannot occupy the reserved `authority-issuance-policy:` namespace. The policy ID is an audit identity, not cryptographic proof that arbitrary callback bytes implement the advertised policy; stronger policy-artifact digest/trust-root binding remains a separate production concern.

A future implementation may replace the callback with a typed delegation graph, jurisdiction lattice, grant-class registry, or equivalent governed mechanism, but must preserve the separation between issuer identity and issuance jurisdiction/currentness.

### Revocation

Revocation also requires an opaque capability. The current V2 slice permits revocation only when the capability principal equals the original grantor. Emergency or hierarchical revocation remains an explicit future policy extension rather than being inferred from technical access or labels.

These are in-process reference boundaries, not cryptographic identity proof or process isolation.

## Design principle 2 — recovery fencing is one semantic transaction

The predecessor durable recovery path writes an epoch advance and then one receipt transition per unresolved action. A durable prefix can therefore expose a new epoch while only some prior in-flight effects have been fenced.

V2 requires:

`RECOVERY_EPOCH_ADVANCE <=> ALL_PREVIOUS_EPOCH_REQUESTED_EFFECTS_FENCED`

The reference journal uses one `RECOVERY_FENCE` event containing `from_epoch`, `to_epoch`, and the exact canonical set of `requested_action_ids`.

Replay rejects missing IDs, extra IDs, duplicates, noncanonical order, epoch mismatch, noncontiguous epoch advance, or a requested receipt originating in another epoch. Applying the event advances the epoch and converts the exact set to `UNRESOLVED_AFTER_RESTART` as one in-memory semantic transition.

Durability precedes live semantic promotion: if the fence append fails, the in-memory epoch and receipts remain in their old state.

This does not prove power-loss atomicity of one filesystem append. Torn-tail handling and production-scale transaction framing remain separate implementation work.

## Design principle 3 — partition policy belongs to the state family

The architecture correctly refuses to mandate one global distributed-systems algorithm. That freedom is unsafe if an implementation can omit the policy entirely.

Every concrete reference-family profile therefore includes both semantic policy and the evidence binding used to exercise that policy:

```text
STATE_FAMILY_CONSISTENCY_PROFILE {
  family_id
  semantic_owner
  consistency_class
  protected
  continuity_bearing
  partition_write_policy
  partition_read_policy
  merge_or_reconciliation_rule
  stale_state_policy
  recovery_fence_policy
  effect_dependency_policy
  safety_invariants[]
  coordination_basis
  mechanical_evidence_refs[]
  qualification_refs[]
  provenance
}
```

Consistency classes describe required semantics, not vendor algorithms. V2 allows `SINGLE_WRITER_EPOCH`, `QUORUM_COMMITTED`, `LINEARIZABLE_REQUIRED`, `CAUSALLY_ORDERED`, `MERGEABLE_CONCURRENT`, `LOCAL_EPHEMERAL`, and `READ_ONLY_REPLICA`.

The profile must state the safety invariant that motivates coordination or coordination avoidance. Concrete reference profiles must also identify existing source/test files that mechanically exercise related invariants. Those references are evidence bindings, not formal proofs of the declared distributed consistency class.

An undeclared protected/material family is `UNKNOWN`, not eventually consistent by default. Material writes fail closed where the family policy is required.

## Design principle 4 — causal frontier is distinct from wall clock

Where ordering materially affects authority, continuity, reconciliation, or durable state, records should carry enough causal metadata to reconstruct predecessor relationships. A generic form is:

```text
CAUSAL_FRONTIER {
  epoch
  predecessor_ids[]
  local_sequence_or_generation
  observed_clock_metadata
}
```

A single-writer family may need only `(epoch, generation)`; a concurrent mergeable family may need richer predecessor metadata.

`LATER_TIMESTAMP != CAUSAL_SUCCESSOR`

`CAUSAL_SUCCESSOR != MORE_TRUE`

`CAUSAL_SUCCESSOR != MORE_AUTHORIZED`

## Qualification and review plane

Qualification must not merely compare reviewer and author labels. Independence remains scope-relative material authorship/shaping ancestry.

A V2 review receipt includes exact subject, reviewed scope, reviewer execution subject/role, independence state, provenance refs, whether material shaping overlaps the reviewed scope, verdict, evidence refs, and an attestation-location declaration.

### Scope-relative reviewer dependence

Unrelated historical work must not automatically destroy independence for every future scope:

`UNRELATED_AUTHORSHIP != AUTOMATIC_DEPENDENCE_FOR_ALL_SCOPES`

`MATERIAL_SHAPING_WITHIN_REVIEWED_SCOPE != INDEPENDENT_WITHIN_THAT_SCOPE`

### Exact-head attestation placement

An exact-head receipt cannot be committed into the same Git subject tree that it attests without changing that head:

`REVIEW HEAD A -> COMMIT RECEIPT FOR A -> HEAD B`

The committed receipt is then historical evidence about A, not an exact-head receipt for B. Therefore current exact-head receipts must live out of the subject tree—for example as an exact-head-bound pull-request review, external check/attestation, or governed Bus receipt. The repository contains the receipt schema and validator, not a self-invalidating current receipt.

The receipt cannot prove this placement by self-report. Validation requires an externally observed attestation-location context; the receipt declaration must agree with that observation.

`IN_SUBJECT_RECEIPT_FOR_CURRENT_HEAD = SELF_INVALIDATING`

`SELF_DECLARED_OUT_OF_TREE != OBSERVED_OUT_OF_TREE`

A review receipt can feed qualification eligibility within policy; it never grants merge authority.

## Hostile design challenges and dispositions

### H1 — capability possession becomes universal authority

Counterexample: one issuer handle can mint every action/target scope or arbitrary validity interval.

Disposition: **REPAIRED IN V2 REFERENCE SLICE.** Issuer authentication and issuance jurisdiction are separate; one immutable policy request includes semantic scope plus validity interval, observed time, and current epoch. Missing or denying policy fails closed.

Residual ceiling: the callback and host-supplied policy identity are a narrow host-policy seam, not complete delegation/jurisdiction architecture or cryptographic policy attestation.

### H2 — revocation by original grantor is too weak

Disposition: **OPEN BY DESIGN / NARROW SLICE.** Broader revocation requires explicit typed policy rather than implicit power inheritance.

### H3 — one recovery record can become huge

Disposition: **OPEN PRODUCTION-SCALE DESIGN.** Production may use transaction framing or a committed manifest with chunks, but no externally usable state may claim the new epoch while only a subset of prior requested effects is fenced.

### H4 — strong consistency everywhere destroys availability

Disposition: **REJECTED DESIGN.** V2 requires state-family semantics rather than one global consistency mode. Coordination choices must name the invariant they protect.

### H5 — causal metadata becomes another truth scalar

Disposition: **REJECTED DESIGN.** Causal order remains separate from epistemic support, authority, consent, and identity relevance.

### H6 — qualification receipts become self-certifying

Disposition: **PARTIALLY MECHANICALLY HARDENED.** Repository-local validation can check structure and declared provenance consistency, and attestation placement is checked from external validation context. It still cannot independently prove reviewer identity, shaping ancestry, or the trust root behind that external observation.

### H7 — exact-head receipt invalidates itself

Disposition: **REPAIRED IN V2 CONTRACT.** Current exact-head receipts are out-of-subject attestations, and location is not accepted from receipt self-report alone.

### H8 — unrelated work destroys all reviewer independence

Disposition: **REPAIRED IN V2 VALIDATOR.** Material dependence is evaluated within the declared review scope.

### H9 — consistency profile is only decorative prose

Disposition: **PARTIALLY HARDENED.** Concrete profiles require explicit safety invariants, coordination rationale, and resolvable mechanical evidence refs. This creates auditable architecture-to-code/test bindings but does not prove the full distributed consistency model.

## Implemented V2 cut

This branch implements:

1. opaque capability-bound authority issuer identity plus separate fail-closed issuance-jurisdiction/currentness policy over an immutable request object;
2. single-event semantic recovery fencing in `GovernedDurableReferenceKernelV2`;
3. machine-readable state-family consistency profiles with explicit invariant/coordination rationale and mechanical evidence bindings;
4. machine-readable exact-head review receipt schema/validator with externally observed attestation placement;
5. separate exact-PR-head reference-kernel and architecture/spec workflows;
6. external research synthesis and hostile self-review surface.

It does not implement complete cognition, distributed consensus, cryptographic identities, complete delegation law, cryptographic policy attestation, production-scale torn-write recovery, autonomous merge, or deployment.

## Claim ceiling

`V2_TEST_PASS != COMPLETE_HC_IMPLEMENTATION`

`V2_TEST_PASS != DISTRIBUTED_CONSENSUS_PROOF`

`V2_TEST_PASS != CRYPTOGRAPHIC_IDENTITY_OR_POLICY_PROOF`

`V2_TEST_PASS != COMPLETE_DELEGATION_GOVERNANCE`

`V2_TEST_PASS != POWER_LOSS_ATOMICITY_PROOF`

`V2_TEST_PASS != INDEPENDENT_REVIEW`

`V2_TEST_PASS != MERGE_AUTHORITY`

`V2_TEST_PASS != CONSCIOUSNESS_OR_PERSONHOOD_PROOF`
