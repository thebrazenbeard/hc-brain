# Conflict and Reconciliation

Status: template architecture.

## Purpose

The resolver handles bounded contradictions, ambiguous references, incompatible state heads, failed routes, dependency-invalidated conclusions, and other conflicts that require repair without becoming a universal executive.

## Conflict classes

The resolver should distinguish at least contradictory propositions, ambiguous semantic/pragmatic interpretations, competing current-state heads, stale dependency chains after correction, incompatible embodiment/calibration state, failed or expired routes, duplicate/idempotency conflict, action-policy conflict, evidence/provenance mismatch, unresolved social/person-model disagreement, and synchronization/version conflict.

Different conflict classes may require different repair mechanisms.

## Dependency-aware invalidation

When a source claim is corrected or invalidated, only dependent conclusions should become ineligible by default.

Useful repair metadata includes invalidated source, dependency edges, affected conclusions/actions, surviving independent state, newly unknown fields, and repair/recompute requirement.

`CORRECTION != GLOBAL_RESET`

`CONTRADICTION != AUTOMATIC_INVERSION`

## Reconciliation process

A generic bounded process is:

1. detect conflict;
2. classify conflict and scope;
3. freeze unsafe dependent effects if necessary;
4. preserve all material competing evidence/state;
5. identify a discriminating read, test, correction, or arbitration step;
6. resolve only when a valid discriminator exists;
7. record reconciliation event and provenance;
8. re-enable/recompute dependents explicitly.

## Dead-letter behavior

State or messages that cannot be safely interpreted, routed, incorporated, or acted upon should not disappear silently. A dead-letter/unresolved surface should preserve the original envelope/content reference, failure stage/code, attempted route or consumer, diagnostic details, applicability/scope, retry count, replay eligibility/state, timestamps, and provenance.

Dead-letter state is not necessarily permanent failure. It may be replayed after a capability, schema, route, or context change.

## Fail-closed scope

Fail closed only at the consequence boundary actually affected by the unresolved conflict. An unresolved motor authorization may block that effect while leaving unrelated perception, memory, or reasoning available.

`LOCAL_UNRESOLVED_STATE != WHOLE_BRAIN_HALT`

Global halt remains available for genuinely global integrity or safety failures.

## Reconciliation versus adjudication

Resolver output can establish that technical conflict has been repaired. It does not necessarily decide semantic truth, moral correctness, identity, consent, or value questions. Those remain with their appropriate systems and evidence contracts.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review.