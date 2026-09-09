# Hyperconnectome Runtime Model

Status: conceptual / unimplemented

## Runtime representation

The Hyperconnectome Brain is a temporal attributed multilayer hypergraph. An active implementation can be represented as:

`H(t) = (V, E_p, E_l(t), E_c(t), H_f(t), X(t), P(t), M(t), Q(t), G(t), K(t))`

Where:

- `V` = functional subsystem nodes;
- `E_p` = physically available substrate reachability fixed by current anatomy/hardware realization;
- `E_l(t)` = durable logical/structural eligibility that may change through governed plasticity without requiring hardware replacement;
- `E_c(t)` = currently configured routes, subscriptions, and bindings;
- `H_f(t)` = transient functional hyperedges/coalitions active at time `t`;
- `X(t)` = local and shared runtime state;
- `P(t)` = plastic parameters governing future state transitions;
- `M(t)` = modulatory and interoceptive state;
- `Q(t)` = resource and quality-of-service state such as energy, heat, bandwidth, latency, damage, and service health;
- `G(t)` = governance/authority state such as permissions, consent/boundary predicates, consequence gates, and action authorization;
- `K(t)` = epistemic support/uncertainty state associated with observations, hypotheses, interpretations, and outputs.

The separations are intentional:

`ROUTING != AUTHORITY`

`RESOURCE_QOS != EPISTEMIC_CONFIDENCE`

`PHYSICAL_REACHABILITY != LEARNED_LOGICAL_ELIGIBILITY`

A concrete implementation may co-locate these data physically, but a conforming model must preserve their semantic independence.

This representation is subordinate to the canonical temporal-hypergraph semantics in `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md`; it is not merely an optional visualization choice.

The HC is not an indiscriminate all-to-all network. It is a dynamically composed system in which specialized subsystems form transient coalitions when several domains jointly constrain an interpretation, prediction, memory update, or action.

## Subsystem contract

Each top-level HC subsystem should expose an explicit contract:

```text
SUBSYSTEM {
  subsystem_id
  accepted_inputs[]
  emitted_outputs[]
  local_state_schema
  update_rule
  confidence_or_uncertainty_model
  provenance_policy
  resource_budget
  plasticity_permissions
  observability_hooks
  failure_mode
}
```

Repository folders are architectural responsibility boundaries, not claims that each subsystem corresponds to one anatomical lobe, software process, or isolated mini-brain.

## Output contract

A useful minimum output record is:

```text
OUTPUT {
  producer
  payload_type
  payload
  event_time_or_interval
  observation_or_record_time
  clock_domain
  temporal_uncertainty
  epistemic_support
  provenance
  scope
  expiry_or_persistence_rule
  requested_effect
}
```

Timing fields may be omitted or coarse when timing is immaterial, but a single exact-looking timestamp must not silently stand in for uncertain event time, observation time, record time, or interval semantics.

`epistemic_support` is typed support for the output proposition/interpretation; it is not resource health, scheduling priority, or coalition-existence confidence.

`payload` and `requested_effect` remain separate. A subsystem may report, predict, or recommend without automatically controlling downstream action.

## Typed connections

Candidate pairwise relation types include:

- `OBSERVES`
- `QUERIES`
- `ROUTES_TO`
- `MODULATES`
- `EXCITES`
- `INHIBITS`
- `CONSTRAINS`
- `RECALLS_FROM`
- `WRITES_CANDIDATE_TO`
- `CONTEXTUALIZES`
- `PREDICTS_FOR`
- `ERROR_SIGNALS_TO`
- `PROPOSES_ACTION_TO`
- `ARBITRATES_WITH`
- `CONSOLIDATES_INTO`

A typed edge is not evidence of causal truth unless the implementation actually enforces that causal relation.

## Functional hyperedges

Many meaningful HC events involve more than two subsystems simultaneously. A transient coalition such as:

`{deep memory, current memory, pragmatics, affect, self identity} -> interpretation`

is a functional hyperedge rather than an artificial serial chain with one supposed owner.

Minimal form:

```text
HYPEREDGE {
  hyperedge_id
  participants[]
  trigger
  shared_schema
  arbitration_rule
  start_time_or_interval
  ttl_or_dissolution_condition
  relation_support
  membership_support
  provenance
  resource_budget
  plasticity_effects_allowed[]
  perturbation_handle
}
```

`relation_support` concerns evidence/support for the claimed higher-order relation or its produced interpretation. `membership_support` concerns confidence that the declared participants/roles are the operative coalition. Neither field is a generic scalar for resource health or authority.

A `COALITION` is the dynamically instantiated, task/context-scoped operational form of a temporal hyperedge.

## Shared state

Shared state is not unrestricted global memory. Every shared object needs ownership, versioning, provenance, scope, and stale/contested handling.

Candidate families include perceptual scene state, body state, current context, working bindings, current goals, uncertainty/disagreement, resource state, governance state, and action candidates.

A shared-state item may be uncertain, contradicted, stale, or disputed; the runtime must preserve those distinctions.

## Distributed arbitration

The HC requires arbitration without creating a homunculus or master mind.

Different arbitration loops may resolve candidate actions, memory writes, interpretations, resource claims, or output renderings. A resolver mechanism may select which hypothesis is provisionally acted upon or which candidate receives resources, but selection does not make a proposition true and route selection does not grant permission.

## External-compute anti-outsourcing rule

An external computational peripheral may accelerate, augment, retrieve, transform, or provide specialist results, but no essential cognitive function may exist only in that external peripheral.

Ablating all external computational peripherals may reduce performance, remove remote-data access, or eliminate optional specialist capabilities, but it must not remove the HC's only implementation of semantics, planning, memory, identity continuity, valuation, conation, arbitration, learning, or other essential cognition.

If loss of an external service removes an essential cognitive function, that service must be classified as HC-internal substrate for architectural conformance rather than as an external peripheral.

## Runtime loop

Generic closed-loop operation:

`sense -> update local state -> publish observations with provenance -> form/revise coalitions -> generate competing hypotheses/goals -> arbitrate under body, evidence, capability, governance, and resource constraints -> act/communicate -> observe consequences -> update epistemic support and eligible plastic state -> consolidate under the appropriate learning rule`

This is descriptive, not a single synchronous clock.

## Time-scale separation

At minimum, distinguish:

- reflex / actuator stabilization;
- fast sensory integration;
- conversational and working-memory cycles;
- deliberate planning and social reasoning;
- interoceptive/endocrine modulation;
- episodic encoding;
- semantic/procedural consolidation;
- long-term topology and policy adaptation.

Transient state must not automatically promote into deep memory, identity, or long-term semantics.

## Failure containment

Relevant failure classes include subsystem silence, stale-state propagation, runaway recurrent coalitions, excessive synchronization, arbitration deadlock, provenance loss, hallucinated shared state, memory-write amplification, plasticity runaway, resource starvation, modulatory saturation, governance-state mismatch, and false certainty.

Each subsystem and functional coalition should expose perturbation and observability handles sufficient for controlled lesioning, isolation, replay, rollback, and degradation testing.

## Provenance

Adapted from `four/runtime-hyperconnectome-v1/docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` after Warden review, then corrected to the canonical temporal-hypergraph invariant and hardened after hostile review. Identity-specific, embodiment-specific, and setting-specific material was deliberately excluded from the base runtime contract.
