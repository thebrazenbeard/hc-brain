# Connectivity Planes

Status: RECONCILED REFERENCE CONTRACT / DESIGN / NOT IMPLEMENTED

The Hyperconnectome uses multiple connectivity planes because one overloaded notion of “connection” is too weak to describe cognition, routing, plasticity, temporal structure, and governance without semantic collapse.

## 1. Plane model

A plane describes what kind of relation is being asserted, not where the endpoints live physically.

Initial planes:

| Plane | Core question | Typical relations |
| --- | --- | --- |
| `STRUCTURAL` | Could these endpoints exchange or influence anything under some allowed configuration? | `STRUCTURALLY_CONNECTS`, read/write eligibility |
| `FUNCTIONAL` | Are these endpoints currently co-active or coupled in a statistically/operationally meaningful way? | `FUNCTIONALLY_COUPLES`, `COOPERATES_WITH` |
| `EFFECTIVE` | Is one endpoint currently exerting directed influence on another? | `ACTIVATES`, `INHIBITS`, `ROUTES`, `GATES`, `ARBITRATES` |
| `MODULATORY` | Is one endpoint changing another endpoint’s gain, threshold, salience, plasticity, or routing behavior? | `MODULATES` |
| `PLASTIC` | Is a relation/state eligible for learning-driven modification, consolidation, decay, or reweighting? | `CONSOLIDATES`, `GENERALIZES_FROM`, plastic-update eligibility |
| `TEMPORAL` | What timing, synchronization, delay, cadence, recency, or ordering relation applies? | temporal alignment/order relations |
| `GOVERNANCE` | What policy/authority/constraint governs an operation? | `AUTHORIZES`, `RESTRICTS`, `VALIDATES`, `QUARANTINES` |

## 2. Structural plane

Structural connectivity expresses reachability or interface availability in the latent temporal hypergraph.

It may encode:

- an input/output interface exists;
- a message type is accepted;
- one memory system may be queried by another;
- a sensor channel is physically/logically available;
- a candidate write path exists;
- a higher-order coalition is structurally eligible to form.

Structural connectivity does **not** imply:

- the edge/hyperedge is currently active;
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

Effective connectivity expresses directed current influence in the active temporal configuration.

Examples:

- one node activates an interpretation candidate;
- an inhibitory process suppresses a motor program;
- a router directs a signal to one destination;
- a gate allows a current-memory update;
- an arbiter selects one action candidate;
- a correction invalidates an obsolete interpretation route.

Effective edges/hyperedges are context-sensitive and may exist only for the duration of a coalition or bounded interval.

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

A modulator should declare:

- target(s);
- dimension(s);
- bounded effect or policy;
- onset/decay or validity interval;
- source/provenance where relevant.

If a downstream component must interpret semantic payload content, the transmission is also or instead a typed signal.

## 6. Plastic plane

Plastic connectivity expresses how relations may change over time.

A plastic relation may carry:

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

A learning signal proposes a change; a plasticity transaction determines whether the change is admitted and whether it becomes provisional or durable.

## 7. Temporal plane

Temporal relations express timing facts and uncertainty that are part of the HC's temporal-hypergraph semantics.

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

A governance relation can block an otherwise structurally and effectively available path.

Example:

```text
STRUCTURAL: action planner -> kinesis actuator gateway exists
EFFECTIVE: action arbiter selects action A
GOVERNANCE: action A lacks required effect grant
RESULT: action candidate remains unexecuted
```

## 9. Plane interaction

A complete route may require several planes simultaneously:

```text
structural reachability
AND target health
AND effective activation
AND governance eligibility
AND temporal validity
AND any required modulation/plasticity constraints
```

No one plane replaces the others.

## 10. Multi-plane example

The same systems may have simultaneous relations on multiple planes:

```text
STRUCTURAL: episodic trace ..> semantic memory
FUNCTIONAL: episodic and semantic memory are coupled during a recall task
EFFECTIVE: retrieved episode --> semantic hypothesis
MODULATORY: novelty ~~> episodic encoding gain
PLASTIC: replay event => candidate semantic consolidation
TEMPORAL: episode time precedes current task time
GOVERNANCE: consolidation requires provenance/currentness policy
```

These relations refer to overlapping systems but assert different propositions.

## 11. Failure rules

A plane-aware implementation should fail closed on semantic mismatch:

- unknown plane → `INVALID`;
- relation incompatible with plane → `INVALID`;
- missing governance required for protected write/effect → `UNRESOLVED` or `DENIED` according to contract;
- missing timing evidence for a timing-sensitive claim → `UNRESOLVED`;
- functional correlation presented as causal influence → `INVALID_CLAIM` or equivalent;
- plastic candidate presented as durable update without consolidation → `INVALID_STATE_TRANSITION`.

## 12. Design consequence

The Hyperconnectome is not “fully connected” in the naive sense that every node continuously exchanges everything with every other node.

It is hyperconnected because the architecture supports rich many-to-many, dynamically reconfigurable, multi-plane temporal relations and coalitions without imposing anatomical hemispheres or a fixed module hierarchy.
