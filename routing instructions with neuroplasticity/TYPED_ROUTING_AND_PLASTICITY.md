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

## Plasticity classes

Routing-related durable updates may include connection weight change, new/remapped capability association, inhibition/gating change, fault-compensation route, learned context/regime route, latency/reliability adaptation, structural hyperedge creation/removal, and modality calibration change.

Every material durable update should carry scope, provenance, evidence, version/supersession, reversibility/rollback information where applicable, and a learning class.

## Protection from accidental personality formation

Repeatedly selected pathways must not silently become identity, value, or permanent cognitive-mode state merely through frequency. Durable change should pass the relevant consolidation/metaplasticity criteria.

## Topology

Routing is non-hemispheric and function/capability based. Dynamic specialization may emerge without imposing human lobe or left/right cerebral structure.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review.