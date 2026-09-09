# Coalition Lifecycle and Gating

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: narrowed from PR #4 `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` after deduplication against canonical distributed arbitration and cross-system integration.

## Purpose

Define task-local coalition formation, expansion, gating, working-state scope, failure reconfiguration, and termination without creating a global executive.

A coalition is an operational temporal hyperedge/configuration, not an anatomical module, hemisphere, persona, identity fragment, or consciousness locus.

## Formation

```text
WHOLE_HC_AVAILABLE
→ contextual eligibility
→ minimal sufficient coalition
→ expand only when evidence/stakes/failure require it
```

Triggers may include task/domain classification, salience, ambiguity, memory retrieval, prediction error, goals, social context, affect/interoception, assurance needs, or failure escalation.

## Coalition state

A coalition should be able to declare:

```text
coalition_id
purpose/context_ref
entry_criteria
member_eligibility
active_members
effective_edges_or_hyperedges
temporary_modulators
shared_working_state
routing_policy
arbitration_refs
persistence_ceiling
exit_criteria
timeout_or_failure_boundary
trace_policy
```

Required invariant:

```text
exit_criteria OR bounded_timeout MUST EXIST
```

An indefinitely persistent structure is infrastructure, not an ordinary cognitive coalition.

## Expansion

Expand only when a required capability is absent, evidence remains materially unresolved, conflict cannot be handled locally, stakes change, active routes fail, protected effects need review, or a broader model/search is justified.

Expansion should be traceable when it changes decision-relevant context.

## Gating

Gates answer bounded eligibility questions such as:

- may this signal enter working memory?
- may this historical trace influence a current claim?
- may a candidate be broadcast?
- may a memory/plasticity candidate proceed?
- may private state cross this boundary?
- may an action candidate proceed to the canonical gateway?

Recommended outcomes:

```text
ALLOW
DENY
DEFER
UNRESOLVED
CONFLICT
QUARANTINE
```

A gate grants eligibility only within its scope. It does not create truth, identity, or generic authority.

## Shared working state

Task-local shared state may contain proposition/object identity, hypotheses, evidence refs, uncertainty/conflict, active goals, retrieved trace refs, temporal validity, privacy scope, and correction/supersession state.

It must not become an untyped copy of participating durable stores.

## Failure isolation

A member failure may cause route substitution, coalition contraction/expansion, degraded mode, or task deferral without forcing whole-brain shutdown when independent valid paths remain.

Protected effects remain withheld if their required gate is unavailable even while unrelated cognition continues.

## Lifecycle

```text
CREATE
→ MEMBERS_SELECTED
→ ACTIVE
→ EXPANDED? / CONTRACTED? (zero or more)
→ RESOLVED | DEFERRED | FAILED | CANCELLED
→ TERMINATED
→ durable candidates independently evaluated for admission
```

Coalition termination is not memory deletion.

## Failure tests

Reject or flag:

- no termination semantics;
- coalition membership automatically granting write/effect authority;
- missing gate evidence defaulting to privileged access;
- temporary coalition state silently becoming durable;
- one member becoming global truth owner;
- unresolved member failure disappearing rather than propagating typed degradation.
