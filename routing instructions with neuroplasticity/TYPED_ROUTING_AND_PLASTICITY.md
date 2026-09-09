# Typed Routing and Plasticity

Status: template architecture.

## Purpose

Routing connects HC subsystems through typed, provenance-bearing, failure-visible exchanges. Plasticity changes the routing/connectivity landscape over time. They interact but are not the same operation.

## Message/event envelope

A routed internal event should be capable of carrying stable message/event identity, schema version, source subsystem or coalition, intended audience/target capability, domain, intent/function, priority, root task/episode identity when applicable, correlation identity, causal-parent identity, acknowledgement requirement, expiration/TTL, source references/provenance, content hash and idempotency key where repeat delivery matters, payload, projection/incorporation state, and authority reference when material.

Routing metadata must not be mistaken for semantic truth or action permission.

`ROUTED != INCORPORATED`

`DELIVERED != BELIEVED`

`PRIORITY != AUTHORITY`

`AUDIENCE != CONSENT`

## Capability subscriptions

Nodes/subsystems may advertise capabilities and subscribe to domain/intent families with minimum priority thresholds or other eligibility conditions.

A subscription is a routing preference/eligibility declaration, not proof that the subscriber is competent, healthy, current, or authorized for all downstream effects.

## Priority

Priority represents scheduling urgency within a declared scope. It should be allowed to influence resource allocation without bypassing protected consequence gates.

High priority can preempt low priority processing; it cannot manufacture missing evidence or authority.

## Causal lineage

Where learning, debugging, credit assignment, or explanation depends on lineage, preserve causal-parent and correlation chains through routing. Derived events should retain references to their upstream evidence rather than becoming provenance-free internal facts.

## Idempotency and duplication

Repeated delivery should be detectable when the operation is intended to be idempotent. Duplicate inputs may be legitimate repeated observations, so deduplication must be contract-specific rather than globally hash-suppressing identical content.

## Failure paths

Unroutable, expired, schema-incompatible, unhealthy-target, or incorporation-failed events should become explicit unresolved/dead-letter state rather than disappearing.

## Route selection versus plasticity

Immediate route selection answers:

`Where should this event/process go now?`

Plasticity answers:

`How should future connectivity, weighting, gating, or node behavior change because of experience?`

A successful route may create plasticity evidence but never changes durable routing policy by itself.

## Temporary effective topology

Routing may change the **effective computational topology** inside a bounded task, coalition, layer, phase, or time interval without changing the HC's physical or durable logical topology.

Examples include:

- suppressing currently low-value candidate routes;
- opening a temporary route among jointly relevant subsystems;
- changing effective edge weight for one coalition;
- generating a task-local reasoning relation;
- restricting message propagation under resource pressure;
- temporarily rerouting around a degraded constituent.

These states must remain distinguishable:

`PHYSICAL_REACHABILITY != DURABLE_LOGICAL_ELIGIBILITY`

`DURABLE_LOGICAL_ELIGIBILITY != CONFIGURED_FLOW_POLICY`

`CONFIGURED_FLOW_POLICY != TEMPORAL_EFFECTIVE_TOPOLOGY`

`TEMPORAL_EFFECTIVE_TOPOLOGY != PLASTICITY_COMMIT`

`FORWARD_LOCAL_EDGE_FILTER != STRUCTURAL_EDGE_REMOVAL`

`TASK_LOCAL_ROUTE != DURABLE_LEARNED_ROUTE`

A transient relation may disappear when its task/coalition ends. Persistence beyond that scope requires the appropriate configuration or plasticity transition rather than accidental object reuse.

## Effective-topology provenance

Where effective topology is consequential or qualification-relevant, the HC should be able to recover enough lineage to establish:

- parent/base topology or eligibility state;
- execution/task/coalition identity;
- route/filter/generator that produced the effective relation;
- score/modulator/state snapshot used;
- onset and expiry or dissolution condition;
- retained, suppressed, generated, or reweighted relations;
- whether the relation is computational-only or evidence-bearing;
- whether it is eligible to produce a plasticity candidate;
- provenance and relevant authority/resource constraints.

This does not require durable logging of every microscopic routing event. Observability depth should scale with consequence, debugging, replay, safety, and qualification needs.

## Routing scores and epistemic/governance boundaries

A routing or flow score can determine which computation receives bandwidth or which relation is effective now. It does not establish what the world is like or what actions are authorized.

`COMPUTATIONAL_ROUTE_SCORE != WORLD_RELATION_EVIDENCE`

`FLOW_SCORE != EPISTEMIC_CONFIDENCE`

`FLOW_SCORE != CAUSAL_IMPORTANCE`

`FLOW_SCORE != SALIENCE_OUTSIDE_DECLARED_SCOPE`

`FLOW_SCORE != AUTHORITY`

`ACTIVE_COMPUTATIONAL_EDGE != WORLD_MODEL_FACT`

A generated reasoning graph or temporary route can contribute to inference while remaining typed as a computational relation rather than an observed relation.

## Plasticity classes

Routing-related durable updates may include connection weight change, new/remapped capability association, inhibition/gating change, fault-compensation route, learned context/regime route, latency/reliability adaptation, structural hyperedge creation/removal, and modality calibration change.

Every material durable update should carry scope, provenance, evidence, version/supersession, reversibility/rollback information where applicable, and a learning class.

An effective route being used repeatedly can create evidence for a plasticity candidate, but repetition alone is not the commit:

`ROUTE_USED_NOW != ROUTE_LEARNED_FOR_FUTURE`

`REPEATED_EFFECTIVE_EDGE != AUTOMATIC_DURABLE_EDGE`

`FORWARD_FILTER_RESULT != PLASTICITY_UPDATE`

## Integrity of generated routing objects

Dynamically generated graphs, hyperedges, route tables, masks, or weighted adjacency objects should satisfy their declared structural contract before activation. Relevant checks can include member/index/value cardinality, stable referent binding, schema/version compatibility, valid TTL/scope, and allowed topology plane.

`GENERATED_TOPOLOGY_OBJECT != VALID_TOPOLOGY_OBJECT_WITHOUT_CONTRACT_CHECKS`

A malformed task-local routing object should fail locally or enter explicit unresolved/fault state rather than silently mutating durable topology.

## Protection from accidental personality formation

Repeatedly selected pathways must not silently become identity, value, or permanent cognitive-mode state merely through frequency. Durable change should pass the relevant consolidation/metaplasticity criteria.

## Topology

Routing is non-hemispheric and function/capability based. Dynamic specialization may emerge without imposing human lobe or left/right cerebral structure.

The canonical HC topology is temporal: the currently effective routing graph/hypergraph is one bounded state of the larger typed multilayer temporal hypergraph, not the whole architecture and not a rewrite of its history.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review, then strengthened through source study of dynamic graph information-flow control. BASIRA DeltaGNN provided a concrete implementation fixture where activation-derived scores filter edges and generate a second task-local computational graph during forward processing. The mechanism is not imported as an HC requirement; it motivates explicit separation among base/logical/configured/effective/plastic topology and routing-score epistemic/authority boundaries.

See `docs/research/BASIRA_DELTAGNN_EFFECTIVE_TOPOLOGY_AND_FLOW_CONTROL_2026-09-09.md`.
