# Hyperconnectome Notation

Status: RECONCILED REFERENCE NOTATION / DESIGN / NOT IMPLEMENTED

This notation gives the HC template a compact way to describe cognitive structure without treating repository folders as runtime topology.

```text
REPOSITORY_PATH != RUNTIME_ENTITY_ID
```

Logical runtime IDs may resemble subsystem names for readability, but they do not create, rename, or override canonical repository roots.

## 1. Entity forms

```text
NODE[id]{capabilities...}
EDGE[id](source -> target){plane, relation, policy...}
HYPEREDGE[id]{members, role_map, relation, plane, context, temporal_scope...}
GATE[id]{scope, predicate, outcome...}
ROUTER[id]{eligible_targets, policy...}
ARBITER[id]{scope, candidates, rule...}
MODULATOR[id]{targets, dimension, effect...}
SIGNAL[id]{type, source, audience, payload...}
STATE[id]{class, owner, value, provenance...}
TRACE[id]{event_type, refs, time, provenance...}
COALITION[id]{purpose, members, entry, exit, temporal_scope...}
BROADCAST[id]{signal_ref, audience, expiry...}
POLICY[id]{scope, rules...}
EVIDENCE[id]{class, source, support, uncertainty...}
```

Braces indicate typed properties, not free-form labels. A conforming implementation may encode the same semantics in JSON, YAML, protobuf, database rows, graph/hypergraph storage, event streams, or another substrate.

## 2. Pairwise edges and higher-order hyperedges

`EDGE` remains the appropriate primitive for genuinely pairwise relations.

```text
EDGE[e1](sensor_adapter -> feature_process){
  plane: EFFECTIVE,
  relation: ACTIVATES
}
```

`HYPEREDGE` represents a higher-order relation whose meaning depends on a joint participating set rather than an arbitrary collection of pairwise links.

```text
HYPEREDGE[h7]{
  members: [optics_state, semantic_context, current_memory, affective_appraisal],
  role_map: {...},
  relation: INTEGRATES,
  plane: EFFECTIVE,
  context: task_44,
  valid_from: t1,
  valid_until: t2?,
  activation_state: ACTIVE,
  temporal_constraints: {...},
  policy_refs: [...],
  provenance_refs: [...]
}
```

Pairwise relations must not be inflated into hyperedges merely because the HC is a hypergraph. Higher-order relations must not be flattened into unrelated pairwise edges when joint membership is semantically material.

## 3. Coalition as an operational temporal hyperedge

A `COALITION` is a specialized dynamically instantiated temporal hyperedge for task/context-local cognition.

```text
COALITION[c19]{
  purpose: "resolve ambiguous social utterance",
  context_ref: task_44,
  members: [speech_language, semantics, pragmatics, social_inference, current_memory, resolver],
  role_map: {...},
  effective_relations: [e12, h7, ...],
  modulators: [...],
  shared_working_state: ws44,
  valid_from: t1,
  exit: "resolved OR task_closed OR timeout",
  persistence_ceiling: WORKING_ONLY
}
```

A coalition may propose durable changes, but coalition membership does not itself authorize consolidation or plasticity.

## 4. Core relation vocabulary

### Connectivity and influence

```text
STRUCTURALLY_CONNECTS
FUNCTIONALLY_COUPLES
ACTIVATES
INHIBITS
INTEGRATES
MODULATES
GATES
ROUTES
ARBITRATES
BROADCASTS
```

### State and memory

```text
READS
WRITES
RETRIEVES
ENCODES
REPLAYS
CONSOLIDATES
GENERALIZES_FROM
SUPERSEDES
CONTRADICTS
```

### Cognition and context

```text
CONTEXTUALIZES
PREDICTS
EXPLAINS
COMPETES_WITH
COOPERATES_WITH
SUPPORTS
OPPOSES
```

### Provenance and governance

```text
DERIVED_FROM
OBSERVED_FROM
VALIDATES
AUTHORIZES
RESTRICTS
AUDITS
QUARANTINES
RECONCILES
```

A relation name alone is insufficient. The relation must declare its plane, scope, and temporal semantics where relevant.

## 5. Connectivity planes

Initial planes:

```text
STRUCTURAL
FUNCTIONAL
EFFECTIVE
MODULATORY
PLASTIC
TEMPORAL
GOVERNANCE
```

The same participants may be related on multiple planes simultaneously. The planes do not collapse into one generic connection field.

## 6. Temporal-hypergraph state

The notation must preserve the distinction among:

```text
LATENT_HYPERGRAPH
TEMPORAL_EFFECTIVE_HYPERGRAPH
HISTORY_OF_HYPERGRAPH_STATES
```

A relation may therefore carry fields such as:

```text
valid_from
valid_until
event_time
reference_time_interval
clock_domain
sequence
latency_bound
synchronization_window
ordering_state: DEFINITE | UNRESOLVED
```

A structurally possible relation is not automatically currently effective. A historical effective relation is not automatically current.

## 7. Signal notation

```text
SIGNAL[s123]{
  schema: 1,
  signal_type: "candidate_interpretation",
  source: semantic_process,
  audience: [arbitration_process],
  domain: "semantic",
  intent: "propose",
  priority: 3,
  payload: {...},
  source_refs: [...],
  evidence_refs: [...],
  causal_parent: s122?,
  correlation_id: task_44?,
  authority_ref: null,
  event_time: ...?,
  expires_at: ...?
}
```

Signal metadata must not silently become content. `priority: 0`, for example, changes scheduling treatment; it does not make the payload more true or more authorized.

## 8. Evidence notation

```text
EVIDENCE[ev7]{
  class: MEASURED | DERIVED | INFERRED | USER_DIRECT | RETRIEVED | MODEL_OUTPUT,
  source_ref: ...,
  observed_at: ...?,
  recorded_at: ...,
  support: ...,
  uncertainty: ...?,
  privacy_scope: ...?,
  currentness: ...?,
  digest: ...?
}
```

Evidence class describes origin/type. It does not itself define truth, authority, or currentness.

## 9. State notation

```text
STATE[st9]{
  class: WORKING | EPISODIC | SEMANTIC | PROCEDURAL | SELF_MODEL | SOCIAL_MODEL |
         PHYSIOLOGICAL | GOVERNANCE | CONFIGURATION | HEALTH | PLASTICITY,
  owner: node_or_subsystem,
  value: {...},
  provenance_refs: [...],
  valid_from: ...?,
  valid_until: ...?,
  confidence: ...?,
  status: CURRENT | HISTORICAL | SUPERSEDED | UNRESOLVED | CONFLICT | QUARANTINED
}
```

A `HISTORICAL` state is not automatically eligible as `CURRENT` input.

## 10. Gate notation

```text
GATE[g4]{
  operation: "memory_consolidation",
  scope: "episodic -> durable",
  requires: [evidence_floor, privacy_ok, conflict_check],
  outcomes: [ALLOW, DENY, DEFER, UNRESOLVED, CONFLICT, QUARANTINE],
  fail_default: DEFER
}
```

A gate may consume current state but must not manufacture missing authority or evidence merely to produce a convenient decision.

## 11. Modulator notation

```text
MODULATOR[m2]{
  source: affective_arousal,
  targets: [salience_attention, episodic_encoding_gate],
  dimension: gain,
  magnitude: bounded_value,
  onset: t0,
  decay: policy_ref,
  content_payload: null
}
```

If downstream systems must interpret semantic payload, that transmission is also or instead a typed `SIGNAL`.

## 12. Arbitration notation

```text
ARBITER[a3]{
  scope: "candidate_interpretations",
  inputs: [hypotheses, evidence, current_context, correction_state],
  rule: resolver_policy_v1,
  outputs: [SELECT, KEEP_MULTIPLE, DEFER, NO_ACTION, CONFLICT, ESCALATE]
}
```

`KEEP_MULTIPLE` is a valid outcome. The HC does not require false certainty merely because a renderer or actuator path prefers one candidate.

## 13. Plasticity notation

```text
PLASTICITY_TX[p8]{
  target: edge_or_hyperedge_ref,
  candidate_change: {...},
  trigger_refs: [trace_91, trace_94],
  policy: bounded_plasticity_v1,
  invariant_check: PASS,
  stage: PROVISIONAL,
  evaluation_window: ...,
  outcome: CONSOLIDATE | REVISE | DECAY | REVERT | QUARANTINE
}
```

A learned association may alter future routing, coalition formation probability, or relation weight without becoming a proposition, permission, value, or memory of a specific event.

## 14. Authority notation

```text
AUTHORITY_GRANT[auth5]{
  issuer: ...,
  subject: node_or_actor,
  operation: ...,
  target: ...,
  scope: ...,
  valid_from: ...,
  valid_until: ...?,
  constraints: [...],
  evidence_ref: ...
}
```

A capability declaration is not an authority grant.

## 15. Diagram shorthand

The following arrows may be used only in explanatory diagrams:

```text
A --> B      effective activation/influence
A -| B       inhibition
A ~~> B      modulation
A == B       functional coupling/correlation; not identity
A ..> B      structural eligibility/reachability
A => B       typed state transition, not logical implication unless explicitly stated
{A,B,C} -H-> X   explanatory shorthand for a higher-order relation
```

Every formal/machine-readable artifact must use explicit relation fields rather than relying on arrow typography.

## 16. Forbidden shorthand collapses

Do not write machine contracts that imply any of these equivalences:

```text
retrieved = current
recent = authoritative
high_priority = permitted
delivered = incorporated
wanted = consented
consented = authorized_for_every_effect
correlated = causal
broadcast = conscious
self_model = self
persona = identity
stored = true
structurally_possible = currently_effective
historically_effective = currently_effective
pairwise_coupling = higher_order_joint_relation
```

These distinctions are part of the architecture, not merely documentation style.
