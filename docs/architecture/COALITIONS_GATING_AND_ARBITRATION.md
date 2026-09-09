# Coalitions, Gating, and Arbitration

Status: REFERENCE CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

The Hyperconnectome avoids both a rigid collection of permanently isolated modules and an undifferentiated network where every subsystem is equally active and equally authoritative all the time.

Runtime cognition uses transient coalitions, explicit gates, bounded routers, modulators, and scoped arbiters inside the HC.

## Coalition principle

A coalition is a task/context-specific temporary higher-order configuration assembled from available HC nodes, edges, modulators, and shared working state.

```text
WHOLE_NETWORK_AVAILABLE
→ contextual eligibility
→ minimal sufficient coalition
→ expand only when evidence/stakes/failure require it
```

Coalitions are not anatomical lobes, hemispheres, personas, or permanent identity fragments. Under the canonical temporal-hypergraph model, an operational coalition is a dynamically instantiated temporal hyperedge.

## Coalition contract

Every cognitive coalition should declare:

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

A coalition without termination semantics is invalid unless it is explicitly persistent infrastructure rather than a cognitive coalition.

## Formation

Coalition formation may be triggered by task/domain classification, perceptual salience, ambiguity, memory retrieval, prediction error, goal activation, social context, affective/interoceptive state, assurance requirements, or failure escalation.

Formation should prefer the smallest adequate set of capabilities rather than activating the whole brain indiscriminately.

## Expansion

A coalition may expand when a required capability is absent from the active set, confidence remains insufficient, competing hypotheses remain unresolved, evidence conflicts, stakes increase, an active route fails, an external effect requires stronger assurance/authority review, social meaning requires broader context retrieval, or novelty requires broader model search.

Expansion is a runtime event and should remain traceable where diagnostically important.

## Gating

Gates answer bounded eligibility questions such as:

- may this signal enter working memory?
- may this candidate be broadcast?
- may this historical trace influence a current-state claim?
- may this episodic record be consolidated?
- may this action reach an actuator?
- may this plasticity update change a protected relation?
- may this private state cross a boundary?

A gate does not need to decide final content or action; it decides whether the next operation is eligible.

Recommended gate outcomes:

```text
ALLOW
DENY
DEFER
UNRESOLVED
CONFLICT
QUARANTINE
```

`DEFER` means a decision is intentionally postponed pending another condition. `UNRESOLVED` means required evidence/policy cannot currently produce a valid decision. `CONFLICT` means incompatible applicable requirements/evidence remain active.

## Routing

Routers operate only over currently eligible targets. Routing factors may include capability match, domain/intent, coalition membership, health/liveness, privacy scope, timing requirements, resource cost, salience/priority, learned utility, redundancy/failover, locality, and policy constraints.

Routing must not silently convert:

```text
HIGH_PRIORITY -> HIGH_AUTHORITY
DELIVERED -> ACCEPTED
CAPABLE -> PERMITTED
```

## Arbitration

An arbiter chooses among already-eligible candidates or decides that no single candidate should be selected.

Separate arbitration scopes may govern perceptual interpretations, semantic interpretations, goals/motives, actions, response forms, memory admission, resource allocation, plasticity updates, and failure recovery strategies.

Recommended outcomes:

```text
SELECT(candidate)
KEEP_MULTIPLE(candidates)
DEFER
NO_ACTION
CONFLICT
ESCALATE(scope)
```

A valid arbiter may preserve ambiguity; it is not required to manufacture certainty for downstream convenience.

## Distributed control

No arbiter owns the whole brain.

For example:

```text
semantic arbiter
  chooses among meaning hypotheses

conative arbiter
  chooses among active concern/action preferences

action arbiter
  selects an action candidate

authority gate
  decides whether the chosen external effect is permitted
```

Even when a concrete implementation co-locates these computations, their semantic outputs remain separate.

## Modulation and coalition state

Coalitions may carry temporary modulators such as increased attention to a sensory channel, increased episodic encoding under novelty, reduced distractor routing, increased exploration under uncertainty, reduced plasticity during unstable/conflicted state, or heightened assurance requirements for high-consequence action.

A temporary modulator expires with its declared validity/coalition unless separately admitted by an allowed plasticity process.

## Shared working state

Coalition working state should preserve object/proposition identity, candidate hypotheses, evidence references, uncertainty/conflict, active concerns/goals, relevant retrieved traces, temporal validity, privacy scope, and correction/supersession state.

It must not become an untyped dump of every participating subsystem's durable storage.

## Failure isolation

A subsystem failure should not automatically collapse the whole coalition if valid alternate routes exist. Conversely, inability to establish required authority for a protected effect should withhold that effect even while unrelated cognition continues.

Local unresolved state is not a whole-brain halt unless the integrity failure is genuinely global.

## Reconciliation

Coalition-level conflict may be reconciled by retrieving missing evidence, requesting/observing clarification, activating an alternate specialist, testing competing predictions, checking currentness/provenance, narrowing the proposition/referent, preserving unresolved alternatives, or deferring action.

Reconciliation changes the live route only when evidence or policy supports the change.

## Coalition lifecycle

```text
CREATE
→ MEMBERS_SELECTED
→ ACTIVE
→ EXPANDED? (zero or more times)
→ RESOLVED | DEFERRED | FAILED | CANCELLED
→ TERMINATED
→ durable candidates independently evaluated for consolidation
```

Termination is not memory deletion. It means the task-local organization is no longer the active effective configuration.

## Design tests

A later validator/simulator should reject or flag:

- a cognitive coalition with no termination semantics;
- an arbiter declared as universal owner of truth, identity, or authority;
- routing rules that infer authority from priority;
- gates whose missing evidence defaults to privileged access;
- temporary coalition state silently promoted to durable state;
- modulators that smuggle untyped semantic content;
- action arbitration that bypasses required authority/effect gates.

## Provenance

Selectively integrated from `research/hyperconnectome-foundations-20260909/docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` after Warden review and aligned with current Noöplex, action-gateway, resolver, and distributed-arbitration contracts.