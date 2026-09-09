# Coalitions, Gating, and Arbitration

Status: REFERENCE CONTRACT / DESIGN / NOT IMPLEMENTED

## 1. Purpose

The hyperconnectome avoids both extremes:

- a rigid collection of permanently isolated modules; and
- an undifferentiated network where every subsystem is equally active and equally authoritative all the time.

The runtime uses transient coalitions, explicit gates, bounded routers, modulators, and scoped arbiters.

## 2. Coalition principle

A coalition is a task/context-specific temporary configuration assembled from available nodes and edges.

```text
WHOLE_NETWORK_AVAILABLE
→ contextual eligibility
→ minimal sufficient coalition
→ expand only when evidence/stakes/failure require it
```

Coalitions are not anatomical lobes, hemispheres, personas, or permanent identity fragments.

## 3. Coalition contract

Every coalition declares:

```text
coalition_id
purpose
context_ref
entry_criteria
member_eligibility
active_members
effective_edges
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

A coalition without any termination semantics is invalid unless it is explicitly a persistent infrastructure structure rather than a cognitive coalition.

## 4. Formation

Coalition formation may be triggered by:

- task/domain classification;
- perceptual salience;
- ambiguity;
- memory retrieval;
- prediction error;
- explicit goal activation;
- social context;
- affective/interoceptive state;
- safety/assurance requirements;
- failure escalation.

Formation should prefer the smallest adequate set of capabilities.

Example:

```text
simple arithmetic
→ working memory + quantitative cognition + response renderer
```

rather than automatically activating autobiographical memory, sexuality, social inference, motor planning, and every other subsystem.

## 5. Expansion

A coalition may expand when:

- a required capability is absent;
- current confidence remains below threshold;
- competing hypotheses remain unresolved;
- evidence conflicts;
- stakes increase;
- the active route fails;
- an external effect requires assurance/authority review;
- social meaning requires relationship/context retrieval;
- a novel situation requires broader world-model search.

Expansion is a runtime operation and should be traceable where diagnostically important.

## 6. Gating

Gates answer bounded eligibility questions such as:

- may this signal enter working memory?
- may this candidate be broadcast?
- may this historical trace influence a current-state claim?
- may this episodic record be consolidated?
- may this action reach an actuator?
- may this plasticity update change a protected relation?
- may this private state cross a boundary?

A gate does not need to decide the final content or action. It decides whether the next operation is eligible.

## 7. Gate decision vocabulary

Recommended minimum:

```text
ALLOW
DENY
DEFER
UNRESOLVED
CONFLICT
QUARANTINE
```

`DEFER` means a decision is intentionally postponed pending another condition. `UNRESOLVED` means the required evidence/policy cannot currently produce a valid decision. `CONFLICT` means incompatible applicable requirements/evidence remain active.

## 8. Routing

Routers operate only over currently eligible targets.

Potential routing factors:

- capability match;
- domain/intent;
- current coalition membership;
- target health/liveness;
- privacy scope;
- timing requirements;
- cost/resource limits;
- salience/priority;
- learned utility;
- redundancy/failover;
- locality;
- policy constraints.

Routing must not silently convert:

```text
HIGH_PRIORITY -> HIGH_AUTHORITY
DELIVERED -> ACCEPTED
CAPABLE -> PERMITTED
```

## 9. Arbitration

An arbiter chooses among already-eligible candidates or decides that no single candidate should be selected.

Candidate arbiter scopes include:

- perceptual interpretations;
- semantic interpretations;
- goals/motives;
- actions;
- response forms;
- memory admission;
- resource allocation;
- plasticity updates;
- failure recovery strategies.

## 10. Arbitration outcomes

Recommended minimum:

```text
SELECT(candidate)
KEEP_MULTIPLE(candidates)
DEFER
NO_ACTION
CONFLICT
ESCALATE(scope)
```

A good arbiter can preserve ambiguity. It is not required to manufacture certainty for the convenience of a downstream renderer.

## 11. Distributed control

No arbiter owns the whole brain.

For example:

```text
semantic arbiter
  chooses among meaning hypotheses

conative arbiter
  chooses among active goal candidates

action arbiter
  chooses a motor/communicative action candidate

authority gate
  decides whether the chosen external effect is permitted
```

Even if one implementation combines these computations internally, their semantic outputs remain distinguishable.

## 12. Modulation and coalition state

Coalitions may carry temporary modulators such as:

- increased attention to a sensory channel;
- increased episodic encoding gain under novelty;
- reduced distractor routing;
- increased exploration under uncertainty;
- reduced plasticity during unstable/conflicted state;
- heightened assurance requirements for high-consequence action.

A temporary modulator expires with its declared validity/coalition unless separately consolidated by an allowed plasticity process.

## 13. Shared working state

Coalitions may expose a shared working-state surface.

This surface should preserve:

- object/proposition identity;
- candidate hypotheses;
- evidence refs;
- uncertainty/conflict;
- active goals;
- relevant retrieved traces;
- temporal validity;
- privacy scope;
- correction/supersession state.

It should not become an untyped dump of every participating subsystem's durable storage.

## 14. Social and affective example

A social utterance might form a coalition of:

```text
language parsing
+ semantic/pragmatic context
+ social inference
+ working memory
+ relevant relationship/context retrieval
+ affective appraisal
+ response/action arbitration
```

If ambiguity is low, the coalition may remain small. If the utterance conflicts with established context, a correction/history path may be added. If an external action with meaningful consequence is proposed, an authority/assurance path is added.

The social-inference node may suggest another person's likely state, but it does not gain direct epistemic access to that person's mind.

## 15. Failure isolation

A subsystem failure should not automatically collapse the whole coalition if alternate routes exist.

Examples:

- one renderer unavailable → choose another renderer;
- one retrieval provider unavailable → preserve `UNAVAILABLE` and use independently valid evidence if sufficient;
- one semantic hypothesis generator fails → retain other candidates;
- authority service unavailable for protected effect → withhold that effect even if cognition continues.

## 16. Reconciliation

Coalition-level conflict may be reconciled by:

1. retrieving missing evidence;
2. requesting/observing clarification;
3. activating an alternate specialist;
4. testing competing predictions;
5. checking currentness/provenance;
6. narrowing the proposition/referent;
7. preserving unresolved alternatives;
8. deferring action.

Reconciliation changes the live route only when evidence or policy actually supports the change.

## 17. Coalition lifecycle example

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

## 18. Design tests

A later validator/simulator should reject or flag:

- a cognitive coalition with no termination semantics;
- an arbiter declared as universal owner of truth/identity/authority;
- routing rules that infer authority from priority;
- gates whose missing evidence defaults to privileged access;
- temporary coalition state silently promoted to durable state;
- modulators that smuggle untyped semantic content;
- action arbitration that bypasses required authority/effect gates.
