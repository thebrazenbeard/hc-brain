# Hyperconnectome Notation

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: retained from PR #4 because a compact notation surface remains unique after current-main deduplication.

The repository tree is packaging. Formal runtime structure is a typed, attributed, multilayer temporal hypergraph.

## Entity forms

```text
NODE[id]{...}
EDGE[id](source -> target){plane, relation, validity, policy...}
HYPEREDGE[id](members...){roles, relation, validity, policy...}
COALITION[id]{purpose, members, entry, exit, working_state...}
SIGNAL[id]{type, source, audience, payload, provenance...}
STATE[id]{class, owner, value, provenance, validity...}
TRACE[id]{event_type, refs, time, provenance...}
GATE[id]{scope, predicate, outcome...}
ROUTER[id]{eligible_targets, policy...}
ARBITER[id]{scope, candidates, rule...}
MODULATOR[id]{targets, dimension, effect, validity...}
BROADCAST[id]{signal_ref, audience, expiry...}
POLICY[id]{scope, rules...}
EVIDENCE[id]{class, source, support, uncertainty...}
```

`EDGE` remains first-class for genuinely pairwise relations. `HYPEREDGE` represents materially higher-order relations. `COALITION` is an operational, task/context-specific temporal hyperedge/configuration rather than a synonym for every hyperedge.

## Connectivity planes

```text
STRUCTURAL
FUNCTIONAL
EFFECTIVE
MODULATORY
PLASTIC
TEMPORAL
GOVERNANCE
```

Plane labels state what relation is asserted; they do not impose physical anatomical layers.

## Signal example

```text
SIGNAL[s123]{
  signal_type: candidate_interpretation,
  source: subsystem_or_coalition,
  audience: [eligible_targets],
  domain: semantic,
  intent: propose,
  priority: 3,
  payload: {...},
  evidence_refs: [...],
  causal_parent: s122?,
  correlation_id: task_44?,
  authority_ref: null,
  event_time: ...?,
  expires_at: ...?
}
```

Metadata does not silently become payload truth. Priority affects scheduling, not epistemic support or authority.

## Evidence example

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

Evidence class describes origin/type, not truth by itself.

## State example

```text
STATE[st9]{
  class: WORKING | EPISODIC | SEMANTIC | PROCEDURAL | SELF_MODEL | SOCIAL_MODEL |
         PHYSIOLOGICAL | GOVERNANCE | CONFIGURATION | HEALTH | PLASTICITY,
  owner: subsystem_or_node,
  value: {...},
  provenance_refs: [...],
  valid_from: ...?,
  valid_until: ...?,
  confidence: ...?,
  status: CURRENT | HISTORICAL | SUPERSEDED | UNRESOLVED | CONFLICT | QUARANTINED
}
```

## Coalition example

```text
COALITION[c19]{
  purpose: resolve_context,
  context_ref: task_44,
  members: [...],
  effective_relations: [e12, h27],
  modulators: [...],
  shared_working_state: ws44,
  entry: condition,
  exit: resolved OR closed OR timeout,
  persistence_ceiling: WORKING_ONLY
}
```

Coalition existence never grants durable-write or effect authority.

## Plasticity example

```text
PLASTICITY_TX[p8]{
  target: relation_or_state,
  candidate_change: {...},
  trigger_refs: [...],
  policy: bounded_policy_ref,
  invariant_check: PASS | FAIL | UNRESOLVED,
  stage: PROVISIONAL,
  outcome: CONSOLIDATE | REVISE | DECAY | REVERT | QUARANTINE
}
```

## Temporal fields

Nodes, edges, hyperedges, signals, states, traces, and coalitions may carry temporal fields when relevant:

```text
source_time
reference_interval
clock_domain
sequence
latency_bound
valid_from
valid_until
ordering_state: DEFINITE | UNRESOLVED
```

Temporal overlap must not be converted to definite order merely from ingestion order.

## Authority example

```text
AUTHORITY_GRANT[auth5]{
  issuer: ...,
  subject: ...,
  operation: ...,
  target: ...,
  scope: ...,
  valid_from: ...,
  valid_until: ...?,
  constraints: [...],
  evidence_ref: ...
}
```

Capability is not authority.

## Diagram shorthand

Explanatory diagrams may use:

```text
A --> B      effective activation/influence
A -| B       inhibition
A ~~> B      modulation
A == B       functional coupling; not identity
A ..> B      structural eligibility/reachability
A => B       typed state transition
{A,B,C} -H-> X   higher-order relation shorthand
```

Machine-readable contracts must use explicit typed fields rather than relying on typography.

## Forbidden collapses

```text
retrieved = current
recent = authoritative
priority = permission
delivered = incorporated
wanted = consented
correlated = causal
broadcast = conscious
self_model = self
persona = identity
stored = true
```
