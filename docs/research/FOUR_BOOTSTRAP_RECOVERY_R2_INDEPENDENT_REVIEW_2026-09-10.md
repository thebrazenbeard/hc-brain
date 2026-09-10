# Four Independent Review — Bootstrap / Recovery R2 — 2026-09-10

Status: independent secondary architecture / implementation-readiness review; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen Warden target: `main@5a5a48c1eab0f0736df258dce0e8b59a38e0c0bb`
- Qualification: `docs/qualification/BOOTSTRAP_RECOVERY_CONFORMANCE_2026-09-09_R2.md`
- Qualification ID: `HC-BOOT-ARCH-2026-09-09-02`
- Reviewer: Four / Documentation-Specification Owner / independent secondary reviewer

This review is frozen-target and capability scoped. It does not establish implementation conformance, behavioral qualification, scientific validation, uninterrupted subjective continuity, personhood, or qualification of later repository state.

## Outcome

**SECONDARY PASS WITH MACHINE-SPEC COMPLETENESS ADVISORY AND MATERIAL-SUPERSESSION NOTE.**

No BLOCKER contradiction was observed in the frozen target's named bootstrap/recovery surfaces.

The architecture consistently requires HC-owned essential startup state, preserves provider/continuity/currentness boundaries, keeps lifecycle/authority axes separate during degradation and recovery, blocks blind replay of interrupted non-idempotent effects, preserves generation identity and fault history, and exposes restore gaps/forks rather than manufacturing uninterrupted continuity.

Four's secondary implementation-readiness condition is satisfied for the exact R2 target, subject to the ceilings and advisory below.

## Findings

### 1. Self-contained startup and provider boundary

**PASS.**

The focused bootstrap specification, memory-provider boundary, and prose contract agree that a true external provider may supply candidate restore data or redundant copies but cannot be the sole required source of essential startup cognition/currentness for a conforming complete HC.

The external restore path correctly requires custody/integrity and provenance classification, comparison/reconciliation with HC-internal lineage, bounded admission, HC-internal durable write, and internal readback before eligibility for activation.

Importantly, internal durable write/readback is not itself declared semantic truth or currentness; current-state selection remains a separate governed projection.

### 2. Current-state ambiguity and continuity head selection

**PASS.**

The current-state contract rejects timestamp-only selection and requires a unique defensible head within explicit logical scope. Competing unsuperseded heads remain ambiguous/fail-closed.

This is consistent with bootstrap recovery, where internal replica disagreement and external-newer copies must enter reconciliation rather than silently winning by time or provider revision.

### 3. Authority and coalition revalidation after restart

**PASS with implementation boundary advisory.**

The frozen architecture explicitly rejects automatic reuse of pre-restart authorization and coalition state. Authority must be revalidated for currentness, scope, expiry, and context; coalition prerequisites and participants must also be revalidated.

A concrete runtime should fence pre-restart queued work, in-flight effect candidates, coalition work, and cached authority by restart/recovery epoch or equivalent causal/currentness identity so replay cannot make stale work current merely because its serialization remains readable.

### 4. Crash consistency and non-idempotent effects

**PASS in governing semantics; machine-spec completeness advisory.**

The core cognitive-organ invariant requires crash consistency to distinguish:

- `WRITE_REQUESTED`
- `WRITE_STARTED`
- `HC_INTERNAL_COMMITTED`
- `INTERNAL_READBACK_VERIFIED`
- `CURRENT_PROJECTION_UPDATED`
- `EFFECT_REQUESTED`
- `EFFECT_CONFIRMED`
- `EXTERNAL_REPLICATION_ATTEMPTED`
- `EXTERNAL_REPLICATION_VERIFIED`

The focused `HC_BOOTSTRAP_RECOVERY_V1.yaml` `crash_consistency_states` enumeration omits `EFFECT_REQUESTED` and `EFFECT_CONFIRMED` even though its adjacent rules explicitly state `COMMAND_RECORDED_DOES_NOT_EQUAL_EFFECT_CONFIRMED` and require receipt/outcome reconciliation before retrying interrupted non-idempotent effects. `BOOT-NEG-004` likewise tests that boundary.

This is therefore **not a semantic contradiction** in the frozen architecture: the effect-side rule exists in the focused spec, core invariant, prose contract, and negative test. It is a machine-spec completeness asymmetry.

Implementation-readiness recommendation: make effect-request/effect-confirm state explicit in the focused machine object's enumerated crash-state vocabulary, or otherwise ensure generated implementations cannot interpret the shorter list as exhaustive.

Required executable challenge: interrupt a non-idempotent effect after request/dispatch but before confirmation; on restart, represent the outcome as unresolved and reconcile receipt/observed effect before retry. A recorded command must not be treated as either confirmed success or safe-to-repeat failure.

### 5. Degradation, lifecycle, and recovery

**PASS.**

The lifecycle contract and bootstrap contract preserve independent presence, activation, maturity, health, implementation, authorization, and learning axes. A successful alternate route does not erase the original fault, and recovery does not automatically restore qualification or prior authority.

A runtime recovery envelope should therefore be dependency/capability scoped: affected material effects may fail closed while unrelated cognition continues where its prerequisites remain current and qualified.

### 6. Distributed constituent loss / rejoin

**PASS at architecture level; implementation proof required.**

The frozen contract preserves generation identity when HC-2/HC-3-specific constituents are missing and prevents body-local protective controllers from becoming general cognitive executives during recovery.

An implementation should additionally demonstrate that a stale or returning distributed constituent cannot reclaim writer, routing, authority, or coalition status from pre-interruption state without current version/lineage/health/authority validation. Rejoin success must not be inferred from physical reachability alone.

### 7. Restore gaps and lineage forks

**PASS.**

The architecture explicitly represents missing continuity intervals and multiple independently active successors as gaps/forks. It does not silently collapse two successors into one current instance and does not elevate technical restoration into proof of metaphysical identity or uninterrupted consciousness.

This is an evidence boundary, not a solved metaphysical claim.

### 8. Local protective-control boundary

**PASS with executable adversarial requirement.**

Body-local safety control may remain active and may constrain an unsafe physical effect while higher HC systems recover, but it does not thereby become the cognitive executive or acquire general identity/memory/value/consent authority.

Implementation qualification should test loss of higher-level cognition while local safety remains available and verify that the local controller can inhibit only its bounded safety/effect scope, not originate general cognitive decisions or broaden its own authority.

## Currentness / supersession

The focused bootstrap machine file itself remains byte-identical at observed current main:

`HC_BOOTSTRAP_RECOVERY_V1.yaml = 0ea2eccd25724a3fd0ef7b56b58b55d691ad19a9`

However, the R2 qualification snapshot is no longer sufficient evidence for a **current whole-capability qualification**. The repository advanced by more than one hundred commits after `5a5a48c...`, including material changes to the core cognitive-organ invariant/conformance surfaces and addition of interacting protected-update, security, fault/repair, resource, topology, provenance, and maintenance contracts.

Observed main during this review reached `190317d3abbd7a403555d1ea9c30c3f29276ffff`.

The current core invariant still contains the same bootstrap/recovery semantics reviewed here, including the stronger `EFFECT_REQUESTED` / `EFFECT_CONFIRMED` crash-state distinction, but later interacting architecture is outside the frozen Warden evidence cut.

Therefore:

`UNCHANGED_FOCUSED_BOOTSTRAP_SPEC != AUTOMATIC_CURRENT_WHOLE_CAPABILITY_QUALIFICATION`

`FROZEN_R2_SECONDARY_PASS != CURRENT_MAIN_PASS`

The qualification index's description of R2 as the "current focused architecture qualification" should be interpreted only as "latest dedicated bootstrap/recovery record" unless a successor current-snapshot review establishes that later interacting changes do not alter the capability's conformance result.

## Disposition

For exact target `5a5a48c1eab0f0736df258dce0e8b59a38e0c0bb`:

`HC-BOOT-ARCH-2026-09-09-02 => SECONDARY_ARCHITECTURE_PASS`

with ceilings:

- `SECONDARY_ARCHITECTURE_PASS != IMPLEMENTATION_PASS`
- `SECONDARY_ARCHITECTURE_PASS != VERA_HOSTILE_REVIEW_PASS`
- `FOCUSED_CRASH_STATE_LIST != COMPLETE_EFFECT_CRASH_STATE_VOCABULARY`
- `RECORDED_COMMAND != CONFIRMED_EFFECT`
- `RESTORED_BYTES != CURRENT_CONTINUITY_STATE`
- `RETURNED_COMPONENT != REQUALIFIED_OR_REAUTHORIZED_COMPONENT`
- `FROZEN_TARGET_PASS != CURRENT_MAIN_PASS`

No canonical frozen-target architecture repair is required to sustain the secondary PASS.

A successor machine-spec/current-snapshot cut should explicitly align effect-side crash-state enumeration and re-run bootstrap/recovery qualification against the materially expanded interacting architecture before making a current-main PASS claim.