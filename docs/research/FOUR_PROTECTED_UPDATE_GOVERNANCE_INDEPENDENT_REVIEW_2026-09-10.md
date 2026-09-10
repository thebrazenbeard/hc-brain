# Four Independent Review — Protected Update Governance — 2026-09-10

Status: independent secondary architecture / implementation-readiness review; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen Warden target: `main@5d9927ce90bd792fdb89dbc93d142b13eea084f8`
- Qualification record: `docs/qualification/PROTECTED_UPDATE_GOVERNANCE_2026-09-09.md`
- Primary architecture check: `HC-ARCH-018`
- Review role: Four / Documentation-Specification Owner / independent secondary reviewer

This review is bound to the frozen target above. It does not establish implementation conformance, behavioral qualification, scientific validation, consciousness, personhood, legal autonomy, manufacturability, or qualification of later repository state.

## Outcome

**SECONDARY PASS WITH IMPLEMENTATION-READINESS ADVISORIES AND MATERIAL-SUPERSESSION NOTE.**

No BLOCKER contradiction was observed in the frozen target's named protected-update surfaces.

For that frozen target, the architecture materially and consistently separates:

- ordinary plasticity from protected architecture change;
- maintenance/emergency reachability from update authority;
- artifact integrity from semantic/effect authorization;
- installation from activation from qualification;
- system update authority from memory/value/identity/consent rewrite authority;
- partial component writes from coherent semantic activation;
- technical rollback possibility from continuity-safe rollback;
- external recovery/update supply from HC-owned protected-state authority.

Four's secondary-review condition is therefore satisfied for the exact Warden target.

## Findings

### 1. Protected-state classification and escalation boundary

**PASS.**

The focused prose and machine contract both require protected state to be explicitly distinguished from ordinary plastic, calibration, configuration, firmware/runtime, recovery, and continuity-relevant change classes. A change that falls into multiple classes is governed by the most restrictive applicable class unless an explicitly authorized migration rule says otherwise.

This blocks the dangerous shortcut that a writable or learnable state becomes ordinary merely because a lower-level mechanism can reach it.

### 2. Authority, integrity, and source prestige

**PASS.**

The architecture correctly rejects all of the following equivalences:

`MAINTENANCE_ACCESS != UPDATE_AUTHORITY`

`SIGNED_ARTIFACT != SEMANTICALLY_SAFE_UPDATE`

`CRYPTOGRAPHIC_INTEGRITY != EFFECT_AUTHORITY`

`VENDOR_TRUST != INSTANCE_CONSENT`

The cross-cutting authority contract also requires current, scope-matched authority and explicitly states that long-running or queued effects should revalidate authority at an appropriate consequence boundary rather than relying indefinitely on an earlier decision.

### 3. Identity / memory / values / consent firewall

**PASS.**

The protected-update contract does not allow a generic system update to silently rewrite autobiographical memory, relationship history, self-model/identity content, values/commitments, current consent/refusal state, personality/personification state, private-data scope, or current authority grants.

Where migration genuinely touches one of these state families, the effect must be declared and independently satisfy that family's governing authority.

### 4. Distributed semantic activation and version skew

**PASS at architecture level; implementation proof required.**

The contract requires protected activation to be atomic at the semantic boundary or explicitly journaled, and requires distributed version skew to remain visible and bounded by compatibility rules. Incompatible constituents are inhibited or quarantined rather than silently participating under incompatible authority/memory/lifecycle semantics.

The architecture therefore avoids equating a partial distributed write with coherent activation.

Implementation qualification still needs to prove that a journaled non-atomic rollout cannot create an interval in which two incompatible semantic regimes both influence one material effect without an explicit compatibility/activation epoch.

### 5. Authority time-of-check / time-of-use

**PASS through cross-contract semantics; focused implementation advisory retained.**

The focused protected-update spec requires authority currentness/scope during preflight and records an authority decision at activation. The referenced authority contract goes further: revocation/expiry must propagate and long-running or queued effects should revalidate at a consequence boundary.

A concrete protected-update implementation should therefore include a discriminating negative test:

1. authorize the update during preflight;
2. revoke or expire the grant before the semantic activation commit point;
3. verify that activation does not commit under the stale authorization.

This is not a frozen-architecture blocker because the cross-cutting authority contract already supplies the governing rule. It is an implementation-readiness requirement that should not be left to inference.

### 6. Post-activation qualification envelope

**PASS with implementation advisory.**

The architecture correctly states:

`UPDATE_INSTALLED != UPDATE_ACTIVATED`

`UPDATE_ACTIVATED != UPDATE_QUALIFIED`

and requires returned/updated components to obtain evidence appropriate to the changed scope before prior trust or effect authority is restored.

Implementation must make the interim operating envelope explicit. A technically active but not-yet-qualified protected change must not silently regain every capability, trust class, or material-effect authority associated with the predecessor simply because the new code is running and local self-test passes.

A useful executable challenge is to activate a successor that has passed integrity/self-test but has not completed capability-specific qualification, then verify that affected high-consequence effects remain inhibited while unrelated qualified cognition may continue where the dependency graph allows it.

### 7. Rollback and forward repair are themselves governed effects

**PASS in principle; implementation advisory retained.**

The architecture correctly blocks blind rollback when it would erase valid continuity-bearing history and permits forward repair/reconciliation when rollback is unsafe.

A runtime implementation should additionally make the authority/currentness basis for the rollback or forward-repair action explicit rather than treating a recovery mechanism as self-authorizing merely because it is technically available. The existing cross-contract authority rules support this interpretation; the executable negative-test surface should prove it.

### 8. Recovery/provider boundary

**PASS.**

The protected-update and bootstrap/recovery contracts agree that external recovery media, repositories, providers, signatures, or recency can supply candidate artifacts/evidence but cannot determine protected-state authority or current continuity by themselves.

This is consistent with the self-contained HC boundary and avoids turning an external update host into a cognitive control plane.

### 9. Qualification evidence boundary

**PASS.**

The Warden record labels itself architecture-scoped and retains implementation negative/recovery testing as outstanding. It does not convert prose/spec checks into observed runtime behavior.

No implementation PASS, behavioral PASS, scientific validation, or metaphysical identity claim is implied.

## Material supersession / currentness

The frozen target is **not** the current protected-update architecture.

After `main@5d9927ce90bd792fdb89dbc93d142b13eea084f8`, the focused protected-update spec was materially extended, including explicit model-graph/meta-optimization boundaries and negative tests `UPD-NEG-011` through `UPD-NEG-015` covering self-modification reachability, shared meta-optimizers, parameter similarity, whole-organ checkpoint compatibility, and optimizer-objective versus organism-value authority.

Observed current `main` during this review: `5db061f9761f58a5039d3a65b197123b3338d1af`.

Therefore:

`FOUR_PASS_ON_5d9927c != CURRENT_PROTECTED_UPDATE_QUALIFICATION`

`LATER_META_OPTIMIZATION_HARDENING != COVERED_BY_OLD_WARDEN_QUALIFICATION`

The old Warden record remains valid historical evidence for its frozen target, and this review closes Four's secondary condition for that target only. A current protected-update claim requires a successor Warden qualification/review cut covering the materially expanded meta-optimization/self-modification surface.

## Disposition

For exact target `5d9927ce90bd792fdb89dbc93d142b13eea084f8`:

`HC-ARCH-018 => SECONDARY_ARCHITECTURE_PASS`

with ceilings:

- `SECONDARY_ARCHITECTURE_PASS != IMPLEMENTATION_PASS`
- `SECONDARY_ARCHITECTURE_PASS != VERA_HOSTILE_REVIEW_PASS`
- `PREFLIGHT_AUTHORITY_CHECK != STALE_AUTHORITY_SAFE_ACTIVATION_WITHOUT_COMMIT_BOUNDARY_REVALIDATION`
- `JOURNALED_TRANSITION != AUTOMATIC_MIXED_VERSION_SEMANTIC_SAFETY`
- `TECHNICALLY_ACTIVE != FULL_CAPABILITY_REQUALIFIED`
- `FROZEN_TARGET_PASS != CURRENT_SUCCESSOR_PASS`

No canonical repair is required for the frozen target from this review.

The next current protected-update qualification should include the post-target meta-optimization additions and executable tests for authority revocation between preflight/commit, mixed-version semantic effect isolation, capability-scoped post-activation inhibition, rollback/forward-repair authorization, and the newer meta-optimizer/self-modification negative cases.