# Four Regression Verification — Protected Update Governance R2 — 2026-09-10

Status: regression/authorial verification against Four's predecessor findings; **not independent successor qualification evidence**; no canonical-main mutation.

## Review target

- Successor qualification: `docs/qualification/PROTECTED_UPDATE_GOVERNANCE_2026-09-10_R2.md`
- Frozen successor target: `main@e2726a43337b79dc43616a5641b0f747fc44f3ed`
- Successor machine contract: `specs/HC_PROTECTED_UPDATE_ACTIVATION_SAFETY_V1.yaml`
- Successor prose supplement: `basic operating instructions/PROTECTED_UPDATE_ACTIVATION_AND_REQUALIFICATION.md`
- Predecessor Four finding source: `docs/research/FOUR_PROTECTED_UPDATE_GOVERNANCE_INDEPENDENT_REVIEW_2026-09-10.md`

Four's predecessor review was independent for its older target. Its findings were used to shape this R2 successor, so this verification is regression evidence only.

`INDEPENDENT_PREDECESSOR_FINDING_USED_FOR_REPAIR != INDEPENDENT_SUCCESSOR_REVIEW`

## Outcome

**REGRESSION INCORPORATION VERIFIED FOR ALL FOUR PREDECESSOR FINDING CLASSES.**

No mismatch was found between the R2 qualification's claim that it incorporated Four's four implementation-readiness findings and the actual successor prose/machine contracts.

The four finding classes now have direct machine-level rules and adversarial cases.

## 1. Commit-time authority revalidation

**INCORPORATED.**

The successor explicitly separates preflight authority from authority current at semantic activation commit and requires authority to remain scope-matched, current, unrevoked, and context-valid.

The commit record binds the authority decision plus authority version/currentness reference, and `PUAS-NEG-001` / `PUAS-NEG-002` cover revocation and expiry after preflight but before semantic commit.

This directly addresses the predecessor time-of-check/time-of-use concern.

### Implementation refinement

The architecture states revalidation must occur `AT_OR_IMMEDIATELY_BEFORE_SEMANTIC_ACTIVATION_COMMIT` and that a revoked/expired grant must block commit.

A concrete implementation should ensure that this is not implemented as an unfenced read followed by a later commit. Otherwise a revocation can occur between the last check and the semantic commit.

Implementation should use an authority-version/currentness fence, compare-and-commit condition, transactional predicate, lease/epoch validation, or equivalent mechanism that makes the commit reject if the authority basis changed before commitment.

Required executable property:

`AUTHORITY_VERSION_CHECK + SEMANTIC_COMMIT` must behave as one consequence-safe decision boundary.

`REVALIDATED_JUST_BEFORE_COMMIT != STALE_AUTHORITY_IMPOSSIBLE_WITHOUT_COMMIT_FENCING`

This is an implementation-proof refinement, not an R2 architecture contradiction.

## 2. Mixed-version semantic isolation

**INCORPORATED.**

The successor explicitly states that journaling is not proof of mixed-version semantic safety and carries:

- constituent version/digest;
- protected semantic version;
- activation epoch;
- compatibility class;
- allowed/inhibited interaction/effect classes;
- transition journal reference;
- qualification state.

`PUAS-NEG-003` directly tests incompatible constituents during a journaled rollout and requires that they not jointly influence one material effect without explicit compatibility and activation-epoch support.

This closes the predecessor architecture gap.

Implementation still must prove that the compatibility/epoch gate is enforced on every relevant material-effect path rather than merely recorded as metadata.

## 3. Capability-scoped post-activation inhibition

**INCORPORATED.**

The successor explicitly separates technical activation and local self-test from capability qualification and prior effect authority.

Its post-activation operating envelope preserves required/observed qualification evidence, qualification state, inhibited effect classes, allowed unrelated functions, and fallback/degraded routes.

`PUAS-NEG-004` and `PUAS-NEG-005` test the core failure modes:

- technically active + local self-test does not restore high-consequence effects before capability-specific qualification;
- predecessor trust/effect authority does not transfer merely because successor bytes are running.

The successor also avoids the opposite failure of imposing a global halt when unrelated qualified cognition can safely continue.

The remaining implementation dependency is correctness/completeness of the capability-dependency graph used to compute the operating envelope.

## 4. Rollback / forward-repair governance

**INCORPORATED.**

Rollback and forward repair are explicitly governed state transitions requiring current scope-matched authority for the state classes actually affected.

The successor preserves narrow emergency authority, checks continuity impact before rollback, blocks blind rollback that would erase valid post-activation continuity, and prevents a `recovery` label from bypassing protected-change governance.

`PUAS-NEG-006` through `PUAS-NEG-008` cover unauthorized rollback, unauthorized forward repair, and continuity-destructive rollback.

`PUAS-NEG-009` and `PUAS-NEG-010` additionally cover ambiguous commit state after crash and stale constituent rejoin with old semantic version/authority cache.

This materially exceeds the predecessor's initial architecture coverage.

## 5. Target/current byte check

The successor focused machine contract is byte-identical between the R2 frozen target and observed current main:

`HC_PROTECTED_UPDATE_ACTIVATION_SAFETY_V1.yaml = 21ef1c228aba6811e9c61730a80d998e4b1f56c7`

The successor prose supplement is likewise byte-identical between the R2 target and observed current main:

`PROTECTED_UPDATE_ACTIVATION_AND_REQUALIFICATION.md = 64a9a4127c791bd095f6a916a1ca50660efbf1f6`

This establishes that these two focused R2 repair surfaces themselves had not changed at the observed current cut. It does not automatically qualify later interacting repository changes.

## 6. Regression-evidence ceiling

The correct interpretation is:

`PREDECESSOR_FINDINGS -> SUCCESSOR_REPAIR -> REGRESSION_VERIFICATION`

not

`PREDECESSOR_FINDINGS -> SUCCESSOR_REPAIR -> SAME_REVIEWER_FRESH_INDEPENDENT_PASS`

R2 appropriately preserves that distinction.

## Disposition

Four verifies that R2 faithfully incorporates the four predecessor finding classes at architecture/specification level.

No additional architecture repair is required from this regression check.

Implementation qualification should specifically execute:

1. revocation/expiry racing the semantic commit with authority-version fencing;
2. incompatible-version constituents attempting one shared material effect;
3. active-but-unqualified successor attempting both affected and unrelated effects;
4. rollback/forward-repair attempts with absent/stale/narrow authority;
5. crash with ambiguous semantic commit state;
6. stale constituent rejoin carrying old authority cache/version state.

Evidence ceilings:

`REGRESSION_INCORPORATION_VERIFIED != INDEPENDENT_SUCCESSOR_REVIEW`

`ARCHITECTURE_RULE_PRESENT != RUNTIME_ENFORCEMENT_PROVEN`

`AUTHORITY_REVALIDATION_RULE != ATOMIC_AUTHORITY_COMMIT_FENCE_PROVEN`

`COMPATIBILITY_METADATA_PRESENT != EFFECT_PATH_ISOLATION_PROVEN`

`CAPABILITY_ENVELOPE_SCHEMA_PRESENT != DEPENDENCY_GRAPH_CORRECTNESS_PROVEN`

`REPAIR_GOVERNANCE_RULE_PRESENT != CONTINUITY_SAFE_REPAIR_EXECUTION_PROVEN`

No canonical-main mutation, merge, or qualification promotion performed by Four.