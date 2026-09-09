# Hyperconnectome Notation

Status: REFERENCE NOTATION / DESIGN / NOT IMPLEMENTED

This notation gives the template a compact way to describe cognitive structure without treating the repository folder tree as the runtime brain.

## 1. Entity forms

```text
NODE[id]{capabilities...}
EDGE[id](source -> target){plane, relation, policy...}
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

A relation name alone is insufficient. The relation must also declare its plane and scope.

## 3. Connectivity planes

Allowed initial planes:

```text
STRUCTURAL
FUNCTIONAL
EFFECTIVE
MODULATORY
PLASTIC
TEMPORAL
GOVERNANCE
```

Examples:

```text
EDGE[e1](vision_feature -> object_hypothesis){
  plane: EFFECTIVE,
  relation: ACTIVATES
}
```

```text
EDGE[e2](arousal_modulator -> attention_gate){
  plane: MODULATORY,
  relation: MODULATES,
  dimension: gain
}
```

```text
EDGE[e3](episodic_trace -> semantic_memory){
  plane: PLASTIC,
  relation: CONSOLIDATES,
  policy: consolidation_v1
}
```

The same pair of endpoints may have multiple edges in different planes.

## 4. Signal notation

A generic signal envelope:

```text
SIGNAL[s123]{
  schema: 1,
  signal_type: "candidate_interpretation",
  source: semantics.context_resolver,
  audience: [cognition.arbiter],
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

Signal metadata must not silently become content. For example, `priority: 0` changes scheduling treatment; it does not mean the proposition in the payload is more true.

## 5. Evidence notation

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

`class` describes evidence origin/type. It does not itself define truth.

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

A `HISTORICAL` state is not automatically eligible as `CURRENT` input.

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
  source: affect.arousal,
  targets: [attention.*, memory.encoding_gate],
  dimension: gain,
  magnitude: bounded_value,
  onset: t0,
  decay: policy_ref,
  content_payload: null
}
```

If the object carries semantic content that downstream nodes must interpret, it should be represented as a `SIGNAL`, not hidden inside a modulator.

## 9. Coalition notation

```text
COALITION[c19]{
  purpose: "resolve ambiguous social utterance",
  context_ref: task_44,
  members: [language.parser, semantics.context, social.inference, memory.working, cognition.arbiter],
  effective_edges: [e12, e14, e27],
  modulators: [m2?],
  shared_working_state: ws44,
  entry: "ambiguity > threshold",
  exit: "resolved OR task_closed OR timeout",
  persistence_ceiling: WORKING_ONLY
}
```

A coalition may propose durable changes, but its existence does not itself authorize them.

## 10. Arbitration notation

```text
ARBITER[a3]{
  scope: "candidate_interpretations",
  inputs: [hypotheses, evidence, current_context, correction_state],
  rule: resolver_policy_v1,
  outputs: [SELECT, KEEP_MULTIPLE, DEFER, CONFLICT]
}
```

`KEEP_MULTIPLE` is a valid outcome. The architecture does not require false certainty merely because a downstream renderer prefers one answer.

## 11. Plasticity notation

```text
PLASTICITY_TX[p8]{
  target: edge_e17,
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

Signals and traces may carry:

```text
source_time
reference_time_interval
clock_domain
sequence
latency_bound
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

A capability declaration is not an authority grant.

## 14. Shorthand for reasoning diagrams

The following arrows may be used in explanatory diagrams only:

```text
A --> B      effective activation/influence
A -| B       inhibition
A ~~> B      modulation
A == B       functional coupling/correlation; not identity
A ..> B      structural eligibility/reachability
A => B       typed state transition, not logical implication unless explicitly stated
```

Every formal/machine-readable artifact must use the full relation fields rather than relying on arrow typography.

## 15. Forbidden shorthand collapses

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
```

Those are precisely the distinctions the notation exists to preserve.
