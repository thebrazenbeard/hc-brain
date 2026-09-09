# Temporal Hypergraph Model

Status: ARCHITECTURAL INVARIANT / DESIGN

## 1. Core statement

The Hyperconnectome Brain is a **temporal hypergraph**.

This is not merely a convenient visualization choice. It is a structural property of the architecture: cognitive systems participate in higher-order relations whose membership, role, influence, activation, synchronization, and persistence change over time.

The HC was conceived as a hyperconnectome first. Hypergraph theory is used because it faithfully represents higher-order connectivity already required by the architecture; the architecture is not being reshaped to imitate a mathematical formalism.

## 2. Why an ordinary graph is insufficient

Ordinary pairwise edges remain useful, but many cognitive events are not naturally reducible to independent pairwise relationships.

For example, a transient social-interpretation event may require the joint participation of:

```text
{optics, memory, semantics, affect, self-model, empathy}
```

The relevant fact is not only that these systems can exchange signals pairwise. The relevant fact is that this exact higher-order set is participating together in one bounded cognitive event.

Representing the event only as all pairwise edges loses coalition membership, shared context, role structure, joint activation, and temporal scope.

## 3. Core temporal-hypergraph entities

The formal architecture therefore supports both pairwise and higher-order relations:

```text
NODE
EDGE
HYPEREDGE
COALITION
```

### NODE

A bounded functional/state capability.

### EDGE

A typed pairwise relation. Ordinary edges remain appropriate for genuinely pairwise relations such as a sensor adapter feeding a feature extractor or a gate controlling one actuator interface.

### HYPEREDGE

A typed relation joining two or more participating entities as one higher-order relation.

Minimum conceptual fields:

```text
HYPEREDGE[id] {
  members
  role_map
  relation
  plane
  context
  valid_from
  valid_until
  activation_state
  temporal_constraints
  policy_refs
  provenance_refs
}
```

A hyperedge can encode a relation whose function exists only because the participating set is jointly present.

### COALITION

A `COALITION` is a dynamically instantiated, task/context-scoped temporal hyperedge with bounded shared working state, active effective relations, modulators, entry criteria, exit criteria, and a persistence ceiling.

Coalitions are therefore a specialized operational form of hyperedge, not a separate mathematical universe.

## 4. Temporal semantics

Time is part of the meaning of the HC topology.

The architecture must distinguish at least:

```text
LATENT_HYPERGRAPH
TEMPORAL_EFFECTIVE_HYPERGRAPH
HISTORY_OF_HYPERGRAPH_STATES
```

### Latent hypergraph

The set of structurally possible nodes, edges, hyperedges, interfaces, and admissible higher-order configurations.

### Temporal effective hypergraph

The relations and higher-order configurations that are actually effective during a bounded time interval.

The effective hypergraph may be narrower, differently weighted, or temporarily enriched relative to durable logical eligibility because current task state, gating, salience, resources, inhibition, fault compensation, prediction, or coalition context changes which relations are computationally operative.

A task-local generated relation is part of the effective computational topology only within its declared scope. Its effectiveness does not establish physical connectivity, durable learned connectivity, or an observed relation in the external world.

### History of hypergraph states

The provenance-preserving record of how configurations formed, changed, weakened, dissolved, recurred, or altered future connectivity through plasticity.

A structural connection may remain available for years while an effective coalition exists for milliseconds. Those are different states and must not be collapsed.

## 5. Interval and event representation

Temporal relations may require either point events or validity intervals.

Implementations must preserve enough temporal metadata to represent onset, offset/expiry, duration, ordering where established, ordering uncertainty where not established, latency, synchronization windows, recurrence, causal-parent relationships where supported, and temporal scope of authority or state validity.

Ingestion order is not automatically event order.

## 6. Higher-order interaction

The temporal hypergraph must represent cases in which a multi-node configuration has properties not captured by any member or pair alone.

For example:

```text
A + B -> insufficient
A + C -> insufficient
B + C -> insufficient
A + B + C -> capability X
```

This is represented as a higher-order relation over `{A, B, C}`, not as a claim that one node secretly contains capability X.

This is especially important for distributed functions such as contextual interpretation, social judgment, multimodal grounding, action selection, humor, affective appraisal, and other coalition-level cognition.

## 7. Multilayer temporal hypergraph

The HC does not have only one kind of connectivity. Higher-order and pairwise relations may participate in distinct planes:

```text
PHYSICAL
DURABLE_LOGICAL
CONFIGURED
FUNCTIONAL_EFFECTIVE
MODULATORY
PLASTIC
TEMPORAL
GOVERNANCE
WORLD_MODEL_RELATIONAL
```

The same participants may therefore be connected differently on different planes. No plane silently substitutes for another.

Core separations include:

`PHYSICAL_REACHABILITY != DURABLE_LOGICAL_ELIGIBILITY`

`DURABLE_LOGICAL_ELIGIBILITY != CONFIGURED_FLOW_POLICY`

`CONFIGURED_FLOW_POLICY != TEMPORAL_EFFECTIVE_TOPOLOGY`

`TEMPORAL_EFFECTIVE_TOPOLOGY != PLASTICITY_COMMIT`

`ACTIVE_COMPUTATIONAL_EDGE != WORLD_MODEL_FACT`

A concrete implementation may use different names or combine storage structures, but it must preserve the semantic distinctions where they affect behavior, evidence, recovery, authority, or learning.

## 8. Temporary effective topology and generated relations

An HC computation may suppress, reweight, or instantiate relations for one bounded execution without changing the durable architecture.

For example, a coalition can:

- filter eligible routes according to current state;
- temporarily open a task-local relation;
- generate a reasoning graph from current hypotheses;
- reroute around a degraded constituent;
- form one higher-order hyperedge for a particular interpretation or plan;
- dissolve those effective relations at task completion.

These operations are normal temporal-hypergraph behavior, not necessarily plasticity.

`FORWARD_LOCAL_EDGE_FILTER != STRUCTURAL_EDGE_REMOVAL`

`TASK_LOCAL_ROUTE != DURABLE_LEARNED_ROUTE`

`GENERATED_REASONING_GRAPH != OBSERVED_RELATION_GRAPH`

`ROUTE_USED_NOW != ROUTE_LEARNED_FOR_FUTURE`

A transient relation can produce evidence for a later plasticity candidate, but persistent logical or plastic topology changes require the relevant admission/governance process.

Where consequential or qualification-relevant, temporary effective-topology events should retain enough scope/provenance to establish their parent topology, producing rule, state snapshot, execution/coalition identity, onset/expiry, and whether they are computational-only, evidence-bearing, or eligible for durable learning.

Generated topology objects must satisfy structural and referential integrity before activation. A malformed task-local edge/hyperedge object should fail locally rather than silently mutating another topology plane.

## 9. Temporal order can change computation

A static member set does not fully define a cognitive event. The same systems can produce different effective computation under different ordering, latency, synchronization, or duration relationships.

Therefore topology plus timing, not topology alone, defines the effective cognitive configuration.

## 10. Plasticity over temporal hypergraph history

A recurring successful higher-order configuration may alter the future probability, threshold, weight, or routing preference for forming a similar configuration again.

Plasticity changes future hypergraph behavior but does not rewrite the historical event that produced the change.

Repeated effective use is evidence available to plasticity; it is not itself a durable topology commit.

`REPEATED_EFFECTIVE_EDGE != AUTOMATIC_DURABLE_EDGE`

## 11. Epistemic and authority boundary for topology scores

A value used to choose or weight an effective route is not automatically evidence about the external world, causal importance, or action authority.

`FLOW_SCORE != EPISTEMIC_CONFIDENCE`

`FLOW_SCORE != CAUSAL_IMPORTANCE`

`FLOW_SCORE != AUTHORITY`

`COMPUTATIONAL_ROUTE_SCORE != WORLD_RELATION_EVIDENCE`

If an effective relation contributes to a world-model claim, normal epistemic admission and provenance rules still apply. If it contributes to an action, normal authority/consent/effect gates still apply.

## 12. Complete cognitive-organ boundary

All essential cognitive hypergraph activity occurs inside the HC boundary.

External cameras, microphones, motors, radios, databases, accelerators, LLMs, specialist models, or cloud services may provide signals, effects, storage transport, or computation. If outside the HC boundary, their outputs enter through HC-owned interfaces as typed evidence/input.

An external peripheral is not part of the organism's temporal cognitive hypergraph merely because it performs computation. Essential cognition remains an internal HC event.

## 13. No hemispheres and no homunculus

The temporal hypergraph has no left/right hemisphere primitive and requires no bilateral duplication or corpus-callosum analogue.

It also has no single executive-person node in the center.

The Noöplex/Hyperconnectome Fabric is the internal integration substrate that supports routing, synchronization, coalition formation, arbitration, modulation, plasticity coordination, state propagation, and conflict handling across the temporal hypergraph.

The fabric enables distributed cognition; it does not replace it with a homunculus.

## 14. Formal-description target

> **A typed, attributed, multilayer temporal hypergraph with dynamically instantiated higher-order relations, bounded coalition state, execution-scoped effective topology, governed plasticity, and an internal Noöplex integration fabric.**

Future implementation technology may vary, but a conforming implementation must preserve these temporal-hypergraph semantics.

## Provenance

Selective Warden integration of the temporal-hypergraph correction from `research/hyperconnectome-foundations-20260909`, reviewed against current `main`. The branch's alternative root taxonomy was not adopted by this integration.

Later strengthened through code-level study of state-dependent graph information-flow control. BASIRA DeltaGNN supplied a concrete computational fixture in which activation-derived scores filter message-passing edges and construct a second task-local graph during forward processing. The source mechanism is not an HC requirement; it sharpened the existing distinction among durable logical, configured, temporary effective, plastic, and world-model relation planes.

See:

- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`
- `specs/HC_EFFECTIVE_TOPOLOGY_TRANSITIONS_V1.yaml`
- `docs/research/BASIRA_DELTAGNN_EFFECTIVE_TOPOLOGY_AND_FLOW_CONTROL_2026-09-09.md`
