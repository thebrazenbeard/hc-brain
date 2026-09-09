# Coalitions, Gating, and Arbitration

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: selectively remapped from Draft PR #4 `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` into the canonical `integration-arbitration/` subsystem.

## 1. Purpose

The Hyperconnectome avoids both a rigid collection of permanently isolated modules and an undifferentiated network where every subsystem is equally active and equally authoritative all the time.

Runtime coordination uses transient coalitions, explicit gates, bounded routers, modulators, and scoped arbiters.

## 2. Coalition principle

A coalition is a task/context-specific temporary configuration assembled from available nodes and relations.

```text
WHOLE_NETWORK_AVAILABLE
→ contextual eligibility
→ minimal sufficient coalition
→ expand only when evidence, stakes, or failure require it
```

Coalitions are operational temporal hyperedges/configurations. They are not anatomical lobes, hemispheres, personas, permanent identity fragments, or a seat of consciousness.

## 3. Coalition contract

A coalition should be able to declare:

```text
coalition_id
purpose
context_ref
entry_criteria
member_eligibility
active_members
effective_relations
temporary_modulators
shared_working_state
routing_policy
arbitration_policy
persistence_ceiling
exit_criteria
timeout_or_failure_boundary
trace_policy
```

Required invariant:

```text
exit_criteria OR bounded_timeout MUST EXIST
```

A structure intended to persist indefinitely is infrastructure, not an ordinary task-local coalition.

## 4. Formation and expansion

Coalition formation may be triggered by task/domain classification, perceptual salience, ambiguity, memory retrieval, prediction error, goals, social context, affect/interoception, safety/assurance requirements, or failure escalation.

Formation should prefer the smallest adequate capability set.

Expansion is justified when a required capability is absent, confidence remains insufficient, evidence conflicts, stakes rise, a route fails, protected effects require review, contextual meaning requires more retrieval, or a novel situation demands broader model search.

Expansion should be traceable when diagnostically important.

## 5. Gating

Gates answer bounded eligibility questions such as whether a signal may enter working memory, a candidate may broadcast, a historical trace may influence a current claim, an episodic record may consolidate, an action may reach an actuator, a plastic update may touch a protected relation, or private state may cross a boundary.

Recommended minimum decisions:

```text
ALLOW
DENY
DEFER
UNRESOLVED
CONFLICT
QUARANTINE
```

A gate decides eligibility for the next operation; it does not thereby decide truth, identity, or final action.

## 6. Routing

Routers operate over currently eligible targets using factors such as capability match, domain/intent, coalition membership, health, privacy, timing, resource cost, salience/priority, learned utility, redundancy/failover, locality, and policy constraints.

Routing must not silently convert:

```text
HIGH_PRIORITY -> HIGH_AUTHORITY
DELIVERED -> ACCEPTED
CAPABLE -> PERMITTED
```

## 7. Arbitration

An arbiter chooses among already-eligible candidates or preserves non-resolution. Candidate scopes include perceptual/semantic interpretations, goals/motives, actions, response forms, memory admission, resource allocation, plasticity updates, and recovery strategies.

Recommended outcomes:

```text
SELECT(candidate)
KEEP_MULTIPLE(candidates)
DEFER
NO_ACTION
CONFLICT
ESCALATE(scope)
```

Selection means a candidate is chosen under a declared policy. It does not create epistemic truth, semantic authority, or generic effect authority.

## 8. Distributed control

No arbiter owns the whole brain.

Different scopes may use different arbiters. A semantic arbiter can choose among meaning hypotheses while a conative arbiter weighs active goals, an action arbiter selects an action candidate, and an authority gate decides whether a protected effect is permitted.

Even if one implementation co-locates these computations physically, their semantic outputs remain distinguishable.

## 9. Modulation and working state

Coalitions may carry temporary modulators that alter attention, encoding gain, distractor routing, exploration, plasticity, or assurance requirements. Temporary modulators expire with declared validity unless separately consolidated through an allowed plasticity process.

Shared working state should preserve proposition/object identity, hypotheses, evidence refs, uncertainty/conflict, goals, retrieved traces, temporal validity, privacy scope, and correction/supersession state.

It must not become an untyped dump of every participating subsystem's durable storage.

## 10. Failure isolation and reconciliation

A subsystem failure should not automatically collapse the whole coalition when alternate valid routes exist.

Reconciliation can include retrieving missing evidence, observing clarification, activating an alternate specialist, testing competing predictions, checking currentness/provenance, narrowing the proposition/referent, preserving unresolved alternatives, or deferring action.

Reconciliation changes the live route only when evidence or policy supports the change.

## 11. Coalition lifecycle

```text
CREATE
→ MEMBERS_SELECTED
→ ACTIVE
→ EXPANDED? (zero or more times)
→ RESOLVED | DEFERRED | FAILED | CANCELLED
→ TERMINATED
→ durable candidates independently evaluated for consolidation
```

Termination is not memory deletion. It means the task-local effective configuration is no longer active.

## 12. Design tests

A later validator/simulator should reject or flag:

- cognitive coalitions with no termination semantics;
- arbiters declared universal owners of truth, identity, or authority;
- routing rules that infer authority from priority;
- gates whose missing evidence defaults to privileged access;
- temporary coalition state silently promoted to durable state;
- modulators that smuggle untyped semantic content;
- action arbitration that bypasses required authority/effect gates.
