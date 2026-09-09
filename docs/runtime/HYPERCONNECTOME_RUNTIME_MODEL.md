# Hyperconnectome Runtime Model

**Status:** conceptual / unimplemented  
**Applies to:** HC-1 Noöplex and HC-2 Noöplex-Q; forward-compatible with later HC-series variants

## 1. Runtime model

Represent the active Noöplex as a temporal attributed multilayer hypergraph:

```text
H(t) = (V, E_s, E_c(t), H_f(t), X(t), P(t), M(t), Q(t))
```

Where:

- `V` - functional nodes or bounded subsystems;
- `E_s` - structural reachability fixed by anatomy/hardware;
- `E_c(t)` - configurable routes, subscriptions, permissions, and bindings;
- `H_f(t)` - transient functional hyperedges active at time `t`;
- `X(t)` - local and shared runtime state;
- `P(t)` - plastic parameters governing future state transitions;
- `M(t)` - modulatory/interoceptive/endocrine state exposed to the runtime;
- `Q(t)` - resource and quality-of-service state: thermal, energy, bandwidth, latency, damage, confidence.

The critical distinction is that the Noöplex is not one giant all-to-all network. It is a dynamically composed system in which temporary coalitions form when several specialized systems jointly constrain one interpretation, prediction, memory update, or action.

## 2. Node contract

Every node must expose an explicit contract rather than relying on implicit global state.

```text
NODE {
  node_id
  node_class
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

A node may be neural tissue, a neuromorphic assembly, a conventional digital process, a memory subsystem, a sensor fusion process, a motor controller, or an HC-2 accelerator-backed service. The contract defines responsibility, not implementation technology.

### Node output record

A useful minimum output record is:

```text
OUTPUT {
  producer
  payload_type
  payload
  timestamp
  confidence
  provenance
  scope
  expiry_or_persistence_rule
  requested_effect
}
```

The distinction between `payload` and `requested_effect` is important. A node can report or recommend without automatically controlling what happens next.

## 3. Typed pairwise connections

Pairwise connections remain useful and should carry explicit semantics. Candidate relation types include:

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

A typed edge should not be used as shorthand for causal certainty unless the implementation actually enforces that causal relation.

## 4. Functional hyperedges

Many cognitively interesting events depend on more than two subsystems at once.

Example:

```text
{episodic_memory, partner_model, current_affect, pragmatics, self_model}
    -> interpretation_of_current_utterance
```

That is better modeled as a functional hyperedge than as a fictional chain in which one module owns the entire interpretation.

Minimal hyperedge record:

```text
HYPEREDGE {
  hyperedge_id
  participants[]
  trigger
  shared_schema
  arbitration_rule
  start_time
  ttl_or_dissolution_condition
  confidence
  provenance
  resource_budget
  plasticity_effects_allowed[]
  perturbation_handle
}
```

Hyperedges may be transient. A conversation, threat response, memory recollection, motor act, sexual response, or moral conflict can recruit different overlapping coalitions without permanently rewiring every participant.

## 5. Shared state protocols

Shared state should not mean unrestricted global memory. Each shared object needs ownership, provenance, versioning, and scope.

Candidate shared state families:

- `PERCEPTUAL_SCENE_STATE`
- `BODY_STATE`
- `CURRENT_CONTEXT`
- `WORKING_BINDINGS`
- `CURRENT_GOALS`
- `SELF_MODEL_SNAPSHOT`
- `PARTNER_MODEL_SNAPSHOT`
- `AFFECTIVE_MODULATORY_STATE`
- `UNCERTAINTY_AND_MODEL_DISAGREEMENT`
- `RESOURCE_STATE`
- `ACTION_CANDIDATES`

A shared state item may be uncertain, contested, stale, or contradicted. The runtime must preserve those distinctions rather than silently collapsing them to one truth value.

## 6. Distributed arbitration

The Noöplex needs arbitration but not a master mind.

Arbitration is the process that resolves competition among candidate interpretations, goals, actions, memory writes, and resource claims.

Candidate arbitration inputs include:

- expected consequence;
- confidence;
- urgency;
- body/homeostatic state;
- current commitments;
- safety and capability constraints;
- predicted regret or conflict;
- social/contextual relevance;
- resource cost;
- uncertainty and model disagreement.

Arbitration may be distributed across specialized loops. There can be an action-selection mechanism, a memory-admission mechanism, a language-production mechanism, and a resource scheduler without pretending that any one of them is the person.

### Resolver principle

A `resolver` node, if present, should implement bounded conflict-resolution policies. It must not become an epistemic superuser.

It can decide:

- which hypothesis is provisionally acted on;
- which memory candidate is admitted or deferred;
- which goal receives resources;
- which output is rendered externally.

It cannot make a false proposition true merely by selecting it.

## 7. Runtime loop

A generic closed-loop cycle is:

```text
sense
-> update local state
-> publish observations with provenance
-> form/revise functional coalitions
-> generate competing interpretations/predictions/goals
-> arbitrate under body, value, safety, and resource constraints
-> act or communicate
-> observe consequences
-> update confidence and eligible plastic state
-> consolidate only under the appropriate learning rule
```

This loop is descriptive, not a single synchronous clock. Different subsystems operate at different time scales.

## 8. Time-scale separation

At minimum, distinguish:

- reflex / actuator stabilization;
- fast sensory integration;
- conversational and working-memory cycles;
- deliberate planning and social reasoning;
- endocrine/interoceptive modulation;
- episodic encoding;
- semantic/procedural consolidation;
- long-term topology and policy adaptation.

A slow deliberative process must not block hard-real-time body protection, and a transient high-arousal state must not automatically rewrite deep identity or long-term semantics.

## 9. HC-1 integration

For HC-1, the runtime can be realized primarily through the hyperconnective neural/neuromorphic substrate and its bio-optic/ionic interface fabric.

The runtime model is intentionally implementation-neutral: a semantic node need not be one anatomical lobe, and a motor node need not be one software process. The node boundary is a responsibility/interface boundary.

## 10. HC-2 integration

HC-2 adds a quantum/photonic coprocessing path. Runtime rule:

> Acceleration changes how a workload is solved, not who owns the mind.

The Q-layer may accelerate search, optimization, sampling, simulation, or selected inference kernels. It should be invoked through explicit service contracts such as:

```text
Q_REQUEST {
  task_class
  input_digest_or_reference
  precision_requirement
  latency_budget
  fallback_required
  privacy_scope
  result_provenance
}
```

If the Q-layer is unavailable, the runtime should degrade to slower HC-1-compatible strategies where the task permits. Identity continuity must not depend on quantum availability.

## 11. Endocrine and Limbic Governor integration

The PR #1 physiology defines a synthetic endocrine plex and a Limbic Governor capable of voluntary gain control/detachment.

Runtime interpretation:

```text
LIMBIC_GOVERNOR != emotion_generator
LIMBIC_GOVERNOR != emotion_delete_button
```

It is a modulation interface affecting gain, routing, physiological expression, salience, pain gating, and possibly plasticity context.

A voluntary detachment request should therefore be represented as a bounded modulatory policy change with provenance and duration. The underlying event, appraisal, memory, and prior affective state remain represented unless separate learning or memory processes alter them.

This preserves the useful canon distinction between **feeling-capable** and **voluntarily regulating expression/intensity**.

## 12. Failure containment

Runtime failure classes include:

- node crash or silence;
- stale-state propagation;
- runaway recurrent coalition;
- excessive synchronization;
- arbitration deadlock;
- provenance loss;
- hallucinated shared state;
- memory write amplification;
- plasticity runaway;
- resource starvation;
- endocrine/modulatory saturation;
- accelerator dependence;
- false self-model certainty.

Each node and hyperedge should have a perturbation/observability handle so the architecture can be tested through lesioning, isolation, replay, rollback, or controlled degradation rather than being judged only by outward behavior.
