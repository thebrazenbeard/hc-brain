# Connectivity Planes

Status: REFERENCE CONTRACT / DESIGN / NOT IMPLEMENTED

The Hyperconnectome uses multiple connectivity planes because one overloaded notion of “connection” is too weak to describe cognition, routing, plasticity, timing, and governance without semantic collapse.

## Plane model

A plane describes what kind of relation is being asserted, not where the endpoints live physically.

| Plane | Core question | Typical relations |
| --- | --- | --- |
| `STRUCTURAL` | Could these endpoints exchange or influence anything under some allowed configuration? | `STRUCTURALLY_CONNECTS`, read/write eligibility |
| `FUNCTIONAL` | Are these endpoints currently co-active/coupled in a statistically or operationally meaningful way? | `FUNCTIONALLY_COUPLES`, `COOPERATES_WITH` |
| `EFFECTIVE` | Is one endpoint currently exerting directed influence on another? | `ACTIVATES`, `INHIBITS`, `ROUTES`, `GATES`, `ARBITRATES` |
| `MODULATORY` | Is one endpoint changing another endpoint’s gain, threshold, salience, plasticity, or routing behavior? | `MODULATES` |
| `PLASTIC` | Is a relation/state eligible for learning-driven modification, consolidation, decay, or reweighting? | `CONSOLIDATES`, `GENERALIZES_FROM`, plastic-update eligibility |
| `TEMPORAL` | What timing, synchronization, delay, cadence, recency, or ordering relation applies? | temporal alignment/order relations |
| `GOVERNANCE` | What policy/authority/constraint governs an operation? | `AUTHORIZES`, `RESTRICTS`, `VALIDATES`, `QUARANTINES` |

## Structural plane

Structural connectivity expresses reachability or interface availability. It may encode that an interface exists, a message type is accepted, a memory system may be queried, a sensor channel is physically/logically available, or a candidate write path exists.

Structural connectivity does **not** imply that the edge is currently active, the target is attending, the source is trusted, the source has write authority, the target will incorporate the signal, or a learned effective path currently prefers this route.

The runtime model distinguishes immutable/slow physical reachability from learned logical structural eligibility where necessary; both are structural propositions, but their change dynamics differ.

## Functional plane

Functional connectivity expresses present co-activity/coupling or task-related coordination. It may be inferred from correlated activation, shared task state, repeated co-participation in a coalition, synchronization measures, mutual information or another coupling metric, or explicit runtime coordination state.

Functional connectivity is descriptive and may be symmetric even when effective influence is directed.

`FUNCTIONALLY_COUPLED(A,B) != A_CAUSES_B`

## Effective plane

Effective connectivity expresses directed current influence.

Examples include one node activating an interpretation candidate, an inhibitory controller suppressing a motor program, a router directing a signal, a gate allowing a working-memory update, an arbiter selecting a candidate, or a correction invalidating an obsolete dependent route.

Effective relations are context-sensitive and may exist only for the duration of a coalition.

## Modulatory plane

Modulatory relations change how another process behaves without being ordinary semantic content transport.

Potential dimensions include gain, threshold, salience, plasticity rate, attention weighting, consolidation probability, exploration/exploitation bias, route preference, persistence duration, and inhibitory sensitivity.

A modulator should declare targets, dimensions, bounded effect/policy, onset/decay or validity, and provenance where relevant. If downstream processing must interpret semantic payload content, the transmission is also or instead a typed `SIGNAL`.

## Plastic plane

Plastic connectivity expresses how relations may change over time. A plastic relation may carry eligibility, current weight, allowed range, update rule, update budget, consolidation policy, decay/reversion policy, protected-invariant class, and provenance requirements.

Plastic eligibility is not a standing instruction to change.

`PLASTICITY_CANDIDATE != DURABLE_UPDATE`

## Temporal plane

Temporal relations express timing facts and uncertainty, including source event time, reference-time interval, clock domain, sequence, timestamp resolution, latency/jitter bound, drift/holdover state, cadence, synchronization state, definite/unresolved order, and recency/validity window.

Temporal metadata may alter effective routing or currentness evaluation, but time alone does not determine semantic authority.

## Governance plane

Governance relations constrain operations, including read/write permission, effect authority, privacy boundary, memory-admission policy, plasticity policy, source-admission policy, broadcast audience, escalation/quarantine rule, and recovery rule.

A governance relation can block an otherwise structurally and effectively available path.

Example:

```text
STRUCTURAL: motor_planner -> actuator_gateway exists
EFFECTIVE: motor_planner selects action A
GOVERNANCE: action A lacks required effect grant
RESULT: action candidate remains unexecuted
```

## Plane interaction

A complete route may require multiple planes simultaneously:

```text
structural reachability
AND target health
AND effective activation
AND governance eligibility
AND temporal validity
AND any required modulation/plasticity constraints
```

No one plane replaces the others.

Two nodes may simultaneously hold different relations on different planes. For example, they may be structurally reachable, functionally coupled, effectively directional, modulatory in one dimension, plasticity-eligible, temporally synchronized, and governance-restricted at the same time.

## Failure rules

A plane-aware implementation should fail closed on semantic mismatch:

- unknown plane → `INVALID`;
- relation incompatible with plane → `INVALID`;
- missing governance required for protected write/effect → `UNRESOLVED` or `DENIED` according to contract;
- missing timing evidence for a timing-sensitive claim → `UNRESOLVED`;
- functional correlation presented as causal influence → `INVALID_CLAIM` or equivalent;
- plastic candidate presented as durable update without consolidation → `INVALID_STATE_TRANSITION`.

## Design consequence

The Hyperconnectome is not “fully connected” in the naive sense that every node continuously exchanges everything with every other node.

It is hyperconnected because the architecture supports rich many-to-many, dynamically reconfigurable, multi-plane relationships and coalitions without imposing anatomical hemispheres or a fixed module hierarchy.

## Provenance

Selectively integrated from `research/hyperconnectome-foundations-20260909/docs/architecture/CONNECTIVITY_PLANES.md` after Warden review and aligned with the current orthogonal runtime-state model.