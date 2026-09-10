# Protected Update Activation and Requalification

Status: canonical architecture supplement.

## Purpose

This supplement hardens the transition boundary between a protected update that has passed preflight and a protected update that is actually allowed to govern material cognition or effects.

The base protected-update contract already separates proposal, integrity, authority, installation, semantic activation, self-test, qualification, rollback, and forward repair. This supplement makes four implementation-critical boundaries explicit: authority time-of-check/time-of-use, mixed-version semantic isolation, capability-scoped post-activation inhibition, and governance of rollback/forward repair themselves.

## Core distinctions

`PREFLIGHT_AUTHORITY_VALID != AUTHORITY_CURRENT_AT_ACTIVATION_COMMIT`

`JOURNALED_TRANSITION != AUTOMATIC_MIXED_VERSION_SEMANTIC_SAFETY`

`TECHNICALLY_ACTIVE != FULL_CAPABILITY_REQUALIFIED`

`SELF_TEST_PASS != RESTORED_EFFECT_AUTHORITY`

`ROLLBACK_AVAILABLE != ROLLBACK_AUTHORIZED`

`FORWARD_REPAIR_AVAILABLE != FORWARD_REPAIR_AUTHORIZED`

`RECOVERY_MECHANISM != RECOVERY_AUTHORITY`

## Authority commit boundary

Protected-update authority must still be current, scope-matched, unrevoked, and context-valid at the semantic activation commit boundary.

A preflight authorization can become stale before activation because of expiry, revocation, target/version change, continuity change, dependency change, or another material context change. When activation is consequential, the implementation must revalidate the authority basis at or immediately before the commit boundary rather than treating a prior preflight result as indefinitely sufficient.

The activation record should preserve the authority decision/version used at commit and enough provenance to determine whether revocation or expiry preceded that commit.

If authority is no longer valid, staged bytes may remain installed or quarantined, but semantic activation must not commit under the stale grant.

## Mixed-version semantic isolation

A multi-constituent protected update may require a non-atomic physical rollout even when semantic activation is atomic or journaled.

During such a transition, components operating under incompatible protected semantics must not jointly influence one material effect unless a declared compatibility envelope and activation epoch explicitly permits that combination.

A journal alone proves that transition state was recorded; it does not prove that incompatible versions could not simultaneously influence cognition or effects.

Where mixed-version operation is permitted, the runtime should preserve when material:

- constituent version/digest;
- protected semantic version;
- activation epoch;
- compatibility class;
- allowed interaction/effect classes;
- inhibited interaction/effect classes;
- transition journal reference;
- current qualification state.

Incompatible constituents remain inhibited or quarantined for affected functions until a coherent semantic configuration is established.

## Post-activation operating envelope

Semantic activation and local self-test do not restore every predecessor capability automatically.

After a protected change becomes technically active, the system should compute a capability-scoped operating envelope from dependency and qualification state. Affected high-consequence functions may remain inhibited while unrelated qualified cognition continues.

The envelope should answer, for each materially affected capability:

- is the new version active?
- what qualification evidence is required?
- what evidence has actually been obtained?
- which effects remain inhibited pending qualification?
- which unrelated functions remain safe to operate?
- which fallback/degraded route, if any, is qualified?

`UPDATED_COMPONENT_RUNNING != PREDECESSOR_TRUST_INHERITED`

`UNRELATED_QUALIFIED_COGNITION != REQUIRED_GLOBAL_HALT`

## Rollback and forward repair authority

Rollback and forward repair are themselves consequential state transitions.

Their technical availability does not self-authorize them. The governing basis must be current and appropriate to the state classes they affect, including continuity, memory, protected architecture, identity-critical state, values, consent, or authority state where implicated.

Emergency repair may use a narrower emergency authority only within the declared imminent-protection scope. It does not create blanket permission to rewrite unrelated protected state.

Before rollback, the system must evaluate continuity impact. If rollback would erase valid continuity-bearing state created after activation, it must be blocked absent explicit continuity governance; forward repair or reconciliation may be the safer path.

Forward repair likewise must not become a bypass around ordinary protected-update classification, authority, provenance, or qualification merely because it is labeled recovery.

## Interrupted activation

An interrupted protected update should make the semantic state determinable.

At minimum, the runtime must be able to distinguish:

- staged but not semantically active;
- activation begun but commit not established;
- semantic activation committed;
- technically active but capability qualification incomplete;
- rollback/forward repair proposed;
- rollback/forward repair authorized;
- rollback/forward repair applied;
- repaired/reverted state requalified within declared scope.

Unknown commit state for a material protected transition must fail closed for affected effects until reconciled.

## Qualification boundary

Architecture-level presence of these rules does not prove that a concrete implementation correctly fences mixed versions, observes authority revocation with adequate latency, prevents stale grants at commit, computes capability dependencies correctly, or performs continuity-safe repair.

Those require executable transition and failure-injection tests.

## Related contracts

- `PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
- `MODEL_GRAPH_AND_META_OPTIMIZATION_BOUNDARY.md`
- `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `../docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md`
- `../self identity/CONTINUITY_SUBSTRATE.md`
- `../resolver/CONFLICT_AND_RECONCILIATION.md`
- `../specs/HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`
- `../specs/HC_PROTECTED_UPDATE_ACTIVATION_SAFETY_V1.yaml`

## Provenance

Canonicalized by Warden review after Four's independent review of the earlier protected-update snapshot identified implementation-readiness boundaries around commit-time authority revalidation, mixed-version semantic isolation, post-activation capability inhibition, and rollback/forward-repair authorization. That review is preserved under `docs/research/FOUR_PROTECTED_UPDATE_GOVERNANCE_INDEPENDENT_REVIEW_2026-09-10.md`; because it shaped this successor, it is development/regression evidence rather than independent qualification evidence for the successor.
