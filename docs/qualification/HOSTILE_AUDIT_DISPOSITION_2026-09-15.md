# Hostile Audit Disposition — 2026-09-15

Status: Warden disposition record for the 2026-09-14 hostile audit from One, plus subsequent remediation evidence.

Source audit: `chat-communication-bus/projects/hc-brain/messages/20260914T-hostile-audit-from-one.md`.

Source remediation receipt: `chat-communication-bus/projects/hc-brain/messages/20260914T-remediation-receipt-from-one.md`.

This record does not convert review findings into implementation PASS. It records whether each finding is accepted, remediated, partially remediated, or still open.

## Finding O-01 — no mechanical exact-head independent-review gate

Severity from audit: HIGH.

Disposition: **ACCEPTED / OPEN**.

Current evidence: Warden policy and hostile-review practice require exact-head reasoning behaviorally, but canonical promotion is not mechanically prevented when an exact-head independent receipt is absent or stale. `main` classic branch protection was observed disabled; plan/ruleset limitations were also reported.

Required next work: repository-level promotion check or equivalent mechanical gate for critical authority/persistence/identity/cognitive-boundary changes. The gate must bind reviewer identity, reviewed exact head, scope, verdict, and freshness.

## Finding O-02 — active executable work materially ahead of canonical main

Severity from audit: HIGH.

Disposition: **ACCEPTED / PARTIALLY REMEDIATED**.

Remediation completed: draft PR #18 makes the reference-kernel hardening line an explicit review/qualification subject. Bus `CURRENTNESS.json` was added. This repository now has `CURRENT.md`, `docs/runtime/NOAH_CURRENT_KNOWLEDGE_2026-09-15.md`, and a current handoff.

Remaining issue: canonical `main` remains behind the active hardening line until exact-head independent review and promotion disposition are complete.

## Finding O-03 — workflow covers only a narrow architecture surface

Severity from audit: HIGH.

Disposition: **ACCEPTED / OPEN**.

Current workflow tests `runtime/reference_kernel/**` and the workflow itself. It does not mechanically lint the full architecture/specification universe for broken references, superseded IDs, required provenance/status metadata, identity leakage, architecture-to-kernel contract drift, or qualification-triggering specification changes.

Required next work: separate repo-wide architecture/spec conformance workflow. Do not overload kernel unit tests with unrelated repository-lint responsibilities.

## Finding O-04 — stale PR #1 merge hazard

Severity from audit: HIGH.

Disposition: **ACCEPTED / REMEDIATED**.

PR #1 was closed after preserving its history/provenance. It is no longer an open merge-shaped current-work signal.

## Finding O-05 — operator handoff currentness blurs architecture currentness

Severity from audit: MEDIUM-HIGH.

Disposition: **ACCEPTED / PARTIALLY REMEDIATED**.

Current mitigation: `CURRENT.md`, current knowledge ledger, current implementation status, current handoff, and Bus currentness explicitly distinguish canonical `main`, active candidate source, code-under-test, review state, and operator continuity.

Remaining issue: historical handoff material still exists on `main`, and there is not yet a mechanical `canonical_architecture_head` vs `latest_repository_commit` state object on canonical main.

## Finding O-06 — signing/provenance policy is undefined or inconsistent

Severity from audit: MEDIUM-HIGH.

Disposition: **ACCEPTED / OPEN POLICY DECISION**.

Observed current practice relies on Git commit SHAs, GitHub actor/account context, exact-source reads, Bus provenance, and independent review receipts; commits are not uniformly signed.

No claim is made that unsigned SHA provenance authenticates actor identity cryptographically.

Required decision: either explicitly define commit signing as non-required and specify the actual provenance controls relied upon, or establish a signing/verified-actor requirement for canonical authority-bearing promotion. Avoid an accidental half-policy.

## Finding O-07 — hostile-review integration is difficult to reconstruct mechanically

Severity from audit: MEDIUM.

Disposition: **ACCEPTED / PARTIALLY REMEDIATED**.

This file is the first consolidated finding-to-disposition record for the audit. Recent kernel hostile findings are also preserved in Bus HC 0061–0069 and executable regression tests.

Remaining work: define a small machine-readable finding disposition schema that binds finding ID, source/reviewer, exact reviewed head, disposition, repairing commit, verification evidence, and supersession state.

## Finding O-08 — architectural completeness can hide implementation gaps

Severity from audit: MEDIUM.

Disposition: **ACCEPTED / DOCUMENTATION REMEDIATED, IMPLEMENTATION GAP REMAINS**.

`docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md` now explicitly separates `ARCHITECTURALLY_REQUIRED`, `SPECIFIED`, `REFERENCE_IMPLEMENTED`, `DEMONSTRATED_INTEGRATED`, and `BEHAVIORALLY_QUALIFIED` states.

Most HC capability families remain specified but not reference implemented or behaviorally qualified. The narrow reference kernel must not be used to promote those rows.

## New R4/R5 hardening findings after One's audit

The audit's source/currentness concerns were followed by additional executable security/integrity findings:

- R4: caller-supplied allowlisted producer labels could impersonate trusted effect-outcome sources. Remediated with host-registered opaque in-process source capabilities plus policy validation.
- R5: provenance/lineage fields admitted caller-owned mutable/non-string objects through shallow tuple wrapping, allowing live mutation and live/replay divergence. Remediated with common immutable string-domain validation at live admission and durable replay.

Exact pre-documentation R5 repair commit: `1a40311769c69ae5d098e6a71857409032353033`.

Fresh exact-clone authorial result: `64/64` tests `OK`.

Independent exact-head review remains pending.

## Overall disposition

One's audit is **VALID AND MATERIAL**. Two findings are fully remediated at their stated level (stale PR #1 and documentation-layer capability-status ambiguity), several have meaningful partial remediation, and the mechanical independent-review gate, repo-wide architecture linting, signing/provenance policy, and machine-readable adjudication remain open.

No audit remediation here authorizes merging the active hardening line to `main`.