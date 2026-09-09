# Connectivity Planes

Status: REFERENCE CONTRACT / DESIGN / NOT IMPLEMENTED

The hyperconnectome uses multiple connectivity planes because one overloaded notion of “connection” is too weak to describe cognition, routing, plasticity, and governance without semantic collapse.

## 1. Plane model

A plane describes what kind of relation is being asserted, not where the endpoints live physically.

Allowed initial planes:

| Plane | Core question | Typical relations |
| --- | --- | --- |
| `STRUCTURAL` | Could these endpoints exchange or influence anything under some allowed configuration? | `STRUCTURALLY_CONNECTS`, `READS`, `WRITES` eligibility |
| `FUNCTIONAL` | Are these endpoints currently co-active/coupled in a statistically or operationally meaningful way? | `FUNCTIONALLY_COUPLES`, `COOPERATES_WITH` |
| `EFFECTIVE` | Is one endpoint currently exerting directed influence on another? | `ACTIVATES`, `INHIBITS`, `ROUTES`, `GATES`, `ARBITRATES` |
| `MODULATORY` | Is one endpoint changing another endpoint’s gain, threshold, salience, plasticity, or routing behavior? | `MODULATES` |
| `PLASTIC` | Is a relation/state eligible for learning-driven modification, consolidation, decay, or reweighting? | `CONSOLIDATES`, `GENERALIZES_FROM`, plastic-update eligibility |
| `TEMPORAL` | What timing, synchronization, delay, cadence, recency, or ordering relation applies? | temporal alignment/order relations |
| `GOVERNANCE` | What policy/authority/constraint governs an operation? | `AUTHORIZES`, `RESTRICTS`, `VALIDATES`, `QUARANTINES` |

## 2. Structural plane

Structural connectivity expresses reachability or interface availability.

It may encode:

- an input/output interface exists;
- a message type is accepted;
- one memory system may be queried by another;
- a sensor channel is physically/logically available;
- a candidate write path exists.

Structural connectivity does **not** imply:

- the edge is currently active;
- the target is attending;
- the source is trusted;
- the source has write authority;
- the target will incorporate the signal;
- a learned effective path currently prefers this route.

## 3. Functional plane

Functional connectivity expresses present co-activity/coupling or task-related coordination.

It may be inferred from:

- correlated activation;
- shared task state;
- repeated co-participation in a coalition;
- synchronization measures;
- mutual information or another coupling metric;
- explicit runtime coordination state.

Functional connectivity is descriptive and may be symmetric even when effective influence is directed.

`FUNCTIONALLY_COUPLED(A,B)` does not establish `A_CAUSES_B`.

## 4. Effective plane

Effective connectivity expresses directed current influence.

Examples:

- one node activates an interpretation candidate;
- an inhibitory controller suppresses a motor program;
- a router directs a signal to one destination;
- a gate allows a working-memory update;
- an arbiter selects one action candidate;
- a semantic correction invalidates an obsolete interpretation route.

Effective edges should be context-sensitive and may exist only for the duration of a coalition.

## 5. Modulatory plane

Modulatory relations change how another process behaves without being ordinary content transport.

Potential dimensions:

- gain;
- threshold;
- salience;
- plasticity rate;
- attention weighting;
- consolidation probability;
- exploration/exploitation bias;
- route preference;
- persistence duration;
- inhibitory sensitivity.

A modulator must declare:

- target(s);
- dimension(s);
- bounded effect or policy;
- onset/decay or validity;
- source/provenance where relevant.

If a downstream component must interpret semantic payload content, the transmission is also or instead a typed `SIGNAL`.

## 6. Plastic plane

Plastic connectivity expresses how relations may change over time.

A plastic edge may carry:

- eligibility;
- current weight;
- allowed range;
- update rule;
- update budget;
- consolidation policy;
- decay/reversion policy;
- protected-invariant class;
- provenance requirements.

Plastic eligibility is not a standing instruction to change.

A learning signal proposes a change; a plasticity transaction decides whether the change is admitted and whether it becomes provisional or durable.

## 7. Temporal plane

Temporal relations express timing facts and uncertainty.

Possible fields:

- source event time;
- reference-time interval;
- clock domain;
- sequence;
- timestamp resolution;
- latency/jitter bound;
- drift/holdover state;
- cadence;
- synchronization state;
- definite/unresolved order;
- recency/validity window.

Temporal metadata may alter effective routing or currentness evaluation, but time alone does not determine semantic authority.

## 8. Governance plane

Governance relations constrain operations.

Possible scopes:

- read permission;
- write permission;
- effect authority;
- privacy boundary;
- memory-admission policy;
- plasticity policy;
- source-admission policy;
- broadcast audience;
- escalation/quarantine rule;
- recovery rule.

A governance edge can block an otherwise structurally and effectively available path.

Example:

```text
STRUCTURAL: motor_planner -> actuator_gateway exists
EFFECTIVE: motor_planner selects action A
GOVERNANCE: action A lacks required effect grant
RESULT: action candidate remains unexecuted
```

## 9. Plane interaction

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

## 10. Multi-plane endpoint example

Two nodes can have several simultaneous relations:

```text
STRUCTURAL: episodic_memory ..> semantic_memory
FUNCTIONAL: episodic_memory == semantic_memory during recall task
EFFECTIVE: retrieved_episode --> semantic_hypothesis
MODULATORY: novelty ~~> episodic_encoding_gain
PLASTIC: replay_event => candidate semantic consolidation
TEMPORAL: episode_time precedes current_task_time
GOVERNANCE: consolidation requires provenance/currentness policy
```

The relations refer to the same broad systems but assert different propositions.

## 11. Failure rules

A plane-aware implementation should fail closed on semantic mismatch:

- unknown plane → `INVALID`;
- relation incompatible with plane → `INVALID`;
- missing governance required for protected write/effect → `UNRESOLVED` or `DENIED` according to contract;
- missing timing evidence for a timing-sensitive claim → `UNRESOLVED`;
- functional correlation presented as causal influence → `INVALID_CLAIM` or equivalent;
- plastic candidate presented as durable update without consolidation → `INVALID_STATE_TRANSITION`.

## 12. Design consequence

The hyperconnectome is not “fully connected” in the naive sense that every node continuously exchanges everything with every other node.

It is hyperconnected because the architecture supports rich many-to-many, dynamically reconfigurable, multi-plane relationships and coalitions without imposing anatomical hemispheres or a fixed module hierarchy.
