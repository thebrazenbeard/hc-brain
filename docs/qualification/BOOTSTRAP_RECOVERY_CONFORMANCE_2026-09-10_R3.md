# Bootstrap / Recovery Conformance — 2026-09-10 R3

Status: QUALIFICATION EVIDENCE / CURRENT SUCCESSOR FOCUSED CUT

Target architecture snapshot: `main@f6ed8e0465627a1ec23e2df03c83e9b36a60df1e`

Predecessor qualification: `BOOTSTRAP_RECOVERY_CONFORMANCE_2026-09-09_R2.md`

Result: **CONDITIONAL PASS**

## Tested capability

Focused architecture-level consistency of bootstrap/recovery crash-state semantics after Four's R2 review identified a machine-spec completeness asymmetry, plus restart-epoch fencing for pre-restart queued/in-flight material work.

This is a successor cut, not a retroactive modification of the historical R2 result.

## Evidence inspected

- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `specs/HC_BOOTSTRAP_RECOVERY_V1.yaml`
- Four's frozen-target review: `docs/research/FOUR_BOOTSTRAP_RECOVERY_R2_INDEPENDENT_REVIEW_2026-09-10.md`
- interacting canonical recovery/authority/currentness/fault/provider boundaries referenced by those files.

Four's R2 review is independent evidence for the historical R2 target. Because its finding directly shaped this successor repair, it is diagnostic/shaping evidence for R3 and is **not** counted as fresh independent review of the affected R3 changes.

## Correction applied

The focused machine contract now explicitly enumerates:

- `EFFECT_REQUESTED`
- `EFFECT_CONFIRMED`

alongside write, projection, and external-replication crash states. It also adds explicit restart/recovery-epoch or equivalent causal-currentness fencing for pre-restart queued/in-flight material work and coalition/effect eligibility.

The prose contract was aligned to the same semantics and now states that missing effect confirmation after restart means unresolved effect state rather than proof of success, proof of failure, or permission to blindly retry a non-idempotent effect.

New negative tests cover effect-request-without-confirmation and serialized pre-restart work surviving an epoch change.

## Observed architecture result

**PASS within the inspected focused architecture scope.**

The machine/prose asymmetry identified by Four is corrected. The successor contracts now agree that:

`EFFECT_REQUESTED != EFFECT_CONFIRMED`

`COMMAND_RECORDED != EFFECT_CONFIRMED`

`PRE_RESTART_QUEUED_WORK != AUTOMATIC_POST_RESTART_ELIGIBLE_WORK`

and that non-idempotent retry requires receipt/outcome reconciliation when effect state is unresolved.

No contradiction was observed in the focused corrected surfaces.

## Why this is not PASS

The successor was directly shaped by Four's review finding, so that review cannot provide fresh independent evidence for the repaired scope. Vera hostile review has not yet been incorporated for this successor. No executable HC implementation has demonstrated recovery-epoch fencing, interrupted-effect reconciliation, distributed rejoin, provider-removal recovery, or post-restart authority/currentness revalidation.

The repository also contains materially newer interacting security, fault/repair, resource, accelerator, maintenance, provenance, and protected-update architecture than the historical R2 target. This focused successor cut does not claim an exhaustive whole-repository current-main qualification of every interaction.

Therefore the strongest justified result is **CONDITIONAL PASS**.

## Remaining uncertainty

UNKNOWN at this cut:

- runtime correctness of crash-state persistence and reconciliation;
- race behavior at restart/recovery epoch boundaries;
- treatment of in-flight distributed effects with partial receipts;
- rejoin behavior for stale distributed HC constituents;
- transitive provider-independence under actual recovery tooling;
- independent secondary reviewer findings for the R3 repair;
- Vera hostile-review findings;
- executable negative-test results.

## Evidence ceiling

`FOUR_R2_SECONDARY_PASS != FOUR_R3_INDEPENDENT_PASS`

`FOUR_FINDING_USED_FOR_R3_REPAIR -> SHAPING_ANCESTRY_FOR_R3_AFFECTED_SCOPE`

`FOCUSED_ARCHITECTURE_PASS != IMPLEMENTATION_PASS`

`RECORDED_REQUEST != CONFIRMED_EFFECT`

`R3_CONDITIONAL_PASS != WHOLE_CURRENT_REPOSITORY_PASS`

Later commits do not inherit this result automatically.
