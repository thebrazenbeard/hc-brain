# Connectivity Planes

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: selectively remapped from Draft PR #4 `docs/architecture/CONNECTIVITY_PLANES.md` into the owner-established routing/plasticity root.

The Hyperconnectome uses multiple connectivity planes because one overloaded notion of “connection” is too weak to describe cognition, routing, plasticity, chronology, and governance without semantic collapse.

## 1. Plane model

A plane describes what kind of relation is being asserted, not where endpoints live physically.

| Plane | Core question | Typical relations |
| --- | --- | --- |
| `STRUCTURAL` | Could these endpoints exchange or influence anything under some allowed configuration? | reachability, read/write eligibility |
| `FUNCTIONAL` | Are these endpoints currently co-active/coupled in a statistically or operationally meaningful way? | coupling, cooperation |
| `EFFECTIVE` | Is one endpoint currently exerting directed influence on another? | activation, inhibition, routing, gating, arbitration |
| `MODULATORY` | Is one endpoint changing gain, threshold, salience, plasticity, or routing behavior? | modulation |
| `PLASTIC` | Is a relation/state eligible for learning-driven modification, consolidation, decay, or reweighting? | update eligibility, consolidation, generalization |
| `TEMPORAL` | What timing, synchronization, delay, cadence, recency, or ordering relation applies? | alignment, ordering, validity |
| `GOVERNANCE` | What policy/authority/constraint governs an operation? | authorization, restriction, validation, quarantine |

These planes coexist with the canonical temporal-hypergraph distinction among latent, effective, and historical topology. They refine relation semantics; they do not replace that model.

## 2. Structural plane

Structural connectivity expresses reachability or interface availability. It may encode that an interface exists, a message type is accepted, one memory system may query another, a sensor channel is available, or a candidate write path exists.

Structural connectivity does not imply current activation, attention, trust, authority, incorporation, or preferred routing.

## 3. Functional plane

Functional connectivity expresses present co-activity/coupling or task-related coordination. It may be inferred from correlated activation, shared task state, repeated coalition membership, synchronization measures, mutual information, or explicit coordination state.

Functional coupling is descriptive and may be symmetric even when effective influence is directed.

```text
FUNCTIONALLY_COUPLED(A,B) != A_CAUSES_B
```

## 4. Effective plane

Effective connectivity expresses directed current influence, such as activation, inhibition, routing, gating, arbitration, or correction-driven invalidation of an obsolete route.

Effective pairwise edges remain valid when the relation is genuinely pairwise. Higher-order task organization may instead be represented through operational hyperedges/coalitions.

## 5. Modulatory plane

Modulatory relations change how another process behaves without being ordinary semantic content transport.

Potential dimensions include gain, threshold, salience, plasticity rate, attention weighting, consolidation probability, exploration/exploitation bias, route preference, persistence duration, and inhibitory sensitivity.

A modulator should declare targets, dimensions, bounded effect/policy, onset/decay or validity, and provenance where relevant.

## 6. Plastic plane

Plastic connectivity expresses how relations may change over time. A plastic relation may carry eligibility, current weight, allowed range, update rule, update budget, consolidation policy, decay/reversion policy, protected-invariant class, and provenance requirements.

```text
PLASTIC_ELIGIBILITY != STANDING_INSTRUCTION_TO_CHANGE
```

A learning signal proposes a change; a plasticity transaction decides whether the change is admitted, provisional, durable, revised, reverted, or quarantined.

## 7. Temporal plane

Temporal relations express timing facts and uncertainty. Possible fields include source event time, reference-time interval, clock domain, sequence, resolution, latency/jitter bounds, drift/holdover state, cadence, synchronization state, definite/unresolved order, and validity window.

Temporal metadata may alter effective routing or currentness evaluation, but time alone does not determine semantic authority.

## 8. Governance plane

Governance relations constrain operations such as read/write permission, effect authority, privacy, memory admission, plasticity, source admission, broadcast audience, escalation, quarantine, and recovery.

A governance relation can block an otherwise structurally and effectively available path.

```text
STRUCTURAL: planner -> actuator gateway exists
EFFECTIVE: planner selects action A
GOVERNANCE: action A lacks required grant
RESULT: candidate remains unexecuted
```

## 9. Plane interaction

A usable route may require multiple conditions simultaneously:

```text
structural reachability
AND target health
AND effective activation
AND governance eligibility
AND temporal validity
AND required modulation/plasticity constraints
```

No plane replaces the others.

## 10. Failure rules

A plane-aware implementation should reject or preserve uncertainty for:

- unknown plane;
- relation incompatible with its plane;
- protected write/effect missing governance;
- timing-sensitive claim missing timing evidence;
- functional correlation presented as causal influence;
- plastic candidate presented as durable update without consolidation.

## 11. Design consequence

The Hyperconnectome is not “fully connected” in the naive sense that every node continuously exchanges everything with every other node.

It is hyperconnected because it supports rich many-to-many, dynamically reconfigurable, multi-plane relations and higher-order coalitions without imposing anatomical hemispheres or a fixed module hierarchy.
