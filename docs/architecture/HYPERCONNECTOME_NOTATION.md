# Hyperconnectome Notation

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: selectively retained from Draft PR #4 because the notation is compatible with the canonical temporal-hypergraph model and does not require an alternative root taxonomy.

This notation gives the template a compact way to describe cognitive structure without treating the repository folder tree as the runtime brain.

## 1. Entity forms

```text
NODE[id]{capabilities...}
EDGE[id](source -> target){plane, relation, policy...}
HYPEREDGE[id](members...){relation, validity, policy...}
GATE[id]{scope, predicate, outcome...}
ROUTER[id]{eligible_targets, policy...}
ARBITER[id]{scope, candidates, rule...}
MODULATOR[id]{targets, dimension, effect...}
SIGNAL[id]{type, source, audience, payload...}
STATE[id]{class, owner, value, provenance...}
TRACE[id]{event_type, refs, time, provenance...}
COALITION[id]{purpose, members, entry, exit...}
BROADCAST[id]{signal_ref, audience, expiry...}
POLICY[id]{scope, rules...}
EVIDENCE[id]{class, source, support, uncertainty...}
```

`COALITION` is an operational temporal-hyperedge/configuration form, not a substitute for the general `HYPEREDGE` entity.

Braces indicate typed properties, not free-form labels. A future machine schema may encode the same structure in JSON, YAML, protobuf, database rows, or another representation.

## 2. Core relation vocabulary

### Connectivity and influence

```text
STRUCTURALLY_CONNECTS
FUNCTIONALLY_COUPLES
ACTIVATES
INHIBITS
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

A relation name alone is insufficient. The relation must also declare its plane, scope, and temporal validity where relevant.

## 3. Connectivity planes

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

The same endpoints may have multiple relations in different planes. A plane is not a claim of physical anatomical separation.

## 4. Signal notation

```text
SIGNAL[s123]{
  schema: 1,
  signal_type: "candidate_interpretation",
  source: semantic_processor,
  audience: [candidate_arbiter],
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

Signal metadata must not silently become semantic content. `priority: 0`, for example, changes scheduling treatment; it does not make the payload more true.

## 5. Evidence notation

```text
EVIDENCE[ev7]{
  class: MEASURED | DERIVED | INFERRED | DIRECT_ASSERTION | RETRIEVED | MODEL_OUTPUT,
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

`class` describes origin/type. It does not itself define truth or authority.

## 6. State notation

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

Historical state is not automatically eligible as current input.

## 7. Gate notation

```text
GATE[g4]{
  operation: "memory_consolidation",
  scope: "episodic -> semantic",
  requires: [evidence_floor, privacy_ok, conflict_check],
  outcomes: [ALLOW, DENY, DEFER, CONFLICT],
  fail_default: DEFER
}
```

A gate may consume current state but must not manufacture missing authority/evidence merely to return a convenient decision.

## 8. Modulator notation

```text
MODULATOR[m2]{
  source: affective_state,
  targets: [attention_gate, memory_encoding_gate],
  dimension: gain,
  magnitude: bounded_value,
  onset: t0,
  decay: policy_ref,
  content_payload: null
}
```

If downstream components must interpret semantic payload content, use a typed `SIGNAL` rather than hiding content in a modulator.

## 9. Coalition notation

```text
COALITION[c19]{
  purpose: "resolve ambiguous social utterance",
  context_ref: task_44,
  members: [language_processing, semantics, social_inference, working_memory, arbiter],
  effective_relations: [e12, e14, h27],
  modulators: [m2?],
  shared_working_state: ws44,
  entry: "ambiguity > threshold",
  exit: "resolved OR task_closed OR timeout",
  persistence_ceiling: WORKING_ONLY
}
```

A coalition may propose durable changes, but its existence does not authorize them.

## 10. Arbitration notation

```text
ARBITER[a3]{
  scope: "candidate_interpretations",
  inputs: [hypotheses, evidence, current_context, correction_state],
  rule: resolver_policy_v1,
  outputs: [SELECT, KEEP_MULTIPLE, DEFER, CONFLICT]
}
```

`KEEP_MULTIPLE` is a valid outcome.

## 11. Plasticity notation

```text
PLASTICITY_TX[p8]{
  target: relation_e17,
  candidate_change: {weight_delta: +0.08},
  trigger_refs: [trace_91, trace_94],
  policy: associative_bounded_v1,
  invariant_check: PASS,
  stage: PROVISIONAL,
  evaluation_window: ...,
  outcome: CONSOLIDATE | REVISE | DECAY | REVERT | QUARANTINE
}
```

A learned association may change future routing probability without becoming a proposition, value, permission, or memory of a specific event.

## 12. Temporal notation

Signals, relations, hyperedges, coalitions, states, and traces may carry:

```text
source_time
reference_time_interval
clock_domain
sequence
latency_bound
valid_from
valid_until
ordering_state: DEFINITE | UNRESOLVED
```

If conservative time intervals overlap, definite order should not be invented from ingestion order.

## 13. Authority notation

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

Capability is not an authority grant.

## 14. Reasoning-diagram shorthand

```text
A --> B      effective activation/influence
A -| B       inhibition
A ~~> B      modulation
A == B       functional coupling/correlation; not identity
A ..> B      structural eligibility/reachability
A => B       typed state transition, not logical implication unless stated
{A,B,C} -H-> X   explanatory shorthand for a higher-order relation
```

Formal machine-readable artifacts must use full typed fields rather than relying on typography.

## 15. Forbidden shorthand collapses

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
```

The notation exists partly to prevent these collapses.
