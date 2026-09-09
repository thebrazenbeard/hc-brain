# Supabase Schema Observations

Status: PRODUCTION_SCHEMA_OBSERVATION / NOT UNIVERSAL REQUIREMENT

This document records reusable structural lessons observed in the production Supabase project. It does not copy private row content, and it does not assume that a realized production schema is automatically the correct architecture for a brain.

Only generic schema mechanics are admitted here.

## 1. Semantic materialization and capture

Observed generic schema family: `semantic_atlas.*`

Relevant structures:

- `capture_policy`
- `runtime_objects`
- `runtime_snapshots`
- `semantic_capture_events`
- `semantic_capture_outcomes`

Reusable observations:

1. **Capture policy is separable from captured content.** A policy can declare whether automatic candidate capture is enabled, minimum salience, trigger classes, raw-text defaults, and write mode without storing the semantic object itself.
2. **Candidate event is separable from capture outcome.** An event can record detector, trigger class, salience, representation, privacy scope, fidelity, and evidence ceiling; a later outcome records what was actually done.
3. **Materialized runtime objects can bind to a snapshot.** `runtime_objects` links object identity/type/source path with payload digest and canonical payload under a `snapshot_id`.
4. **A runtime snapshot can carry explicit source revision and validation state.** Observed fields include repository locator, Git ref, commit SHA, readback SHA, materialization version, object counts, validation state, and activation/readback fields.
5. **Loaded state and activated state are not the same thing.** Separate load, validation, sealing, activation, and readback fields make this distinction representable.

Hyperconnectome translation:

- semantic admission should be policy-mediated;
- `candidate_capture != admitted_semantic_state`;
- `materialized != validated != active`;
- content hashes prove integrity of a payload, not semantic truth;
- privacy/evidence ceilings should travel with captured semantic state.

## 2. Distributed routing and delivery

Observed generic schema family: `radar.*`

Relevant structures:

- `nodes`
- `subscriptions`
- `messages`
- `delivery_events`
- `acknowledgements`
- `dependencies`
- `dead_letters`
- `health_events`
- `reconciliation_events`
- `telemetry`

Reusable observations:

### Node registry

A node record separates:

- node identity;
- runtime kind;
- status;
- declared capabilities;
- heartbeat/currentness;
- metadata.

Hyperconnectome lesson: capability advertisement, liveness, and authority should not be collapsed into one `active` flag.

### Message envelope

Observed message fields include:

- stable message ID and schema version;
- sender and audience;
- domain and intent;
- priority;
- root-task, correlation, and causal-parent identifiers;
- acknowledgement requirement;
- expiry;
- authority reference;
- source references;
- content hash;
- idempotency key;
- payload;
- projection status.

Hyperconnectome lesson: a routed signal should be able to carry both content and control metadata without pretending those metadata are semantic content. Causal ancestry, idempotency, authority, source provenance, and expiry are different dimensions.

### Delivery and acknowledgement

`delivery_events` and `acknowledgements` exist separately from messages.

Hyperconnectome lesson:

`emitted != delivered != acknowledged != incorporated != acted_on`.

A future internal signal bus should preserve those distinctions when they matter for reliability or diagnosis.

### Dead-letter state

Observed dead-letter fields include failure stage/code, envelope, diagnostic, attempted route, applicability, replay state, retry count, and timestamps.

Hyperconnectome lesson: failed communication should remain representable as quarantined/replayable evidence rather than disappearing or being silently reinterpreted as successful routing.

### Reconciliation and health

Separate health and reconciliation events allow the system to distinguish runtime condition from repair attempts.

Hyperconnectome lesson: health state, fault evidence, and reconciliation action are separate record types.

## 3. Lineage and succession

Observed generic schema family: `redworm.*`

Relevant structures:

- `lineage_events`
- `lineage_state`
- `runtime_registry`
- `succession_transfers`

Reusable observations:

1. **Runtime instance and lineage are different identities.** A runtime token can appear/disappear while lineage state persists separately.
2. **Succession can be a transaction.** Transfer records identify prior/next generation, previous/next lineage key, payload digest, source/successor runtime tokens, status, creation, and consumption time.
3. **History is eventful.** Lineage events preserve event type, generation, lineage key, optional transfer/runtime identifiers, and details.
4. **Current holder state is explicit rather than inferred from latest event time alone.**

Hyperconnectome translation:

- process/runtime restart should not automatically define or erase identity continuity;
- continuity transfer should have explicit evidence, status, and payload binding where an implementation needs persistence across runtime boundaries;
- chronology alone should not choose the current continuity holder.

This is an engineering continuity model, not proof of metaphysical personal identity.

## 4. Multi-perspective shared-state cognition

Observed generic schema family: `build_team_2.*`

Relevant structures:

- `collectives`
- `facets`
- `tasks`
- `perspectives`
- `decisions`
- `memory_events`
- `role_operational_checkpoints`
- `role_training_qualifications`

Reusable observations:

### Shared snapshot before perspective

Tasks and perspectives both bind to a `snapshot_digest`.

Hyperconnectome lesson: competing cognitive perspectives can be evaluated against the same immutable evidence cut, reducing accidental disagreement caused by different inputs.

### Perspective and decision are separate objects

A perspective is attributed to a facet/lens; a decision is a distinct later object.

Hyperconnectome lesson: hypothesis generation, viewpoint-specific interpretation, arbitration, and final decision should remain distinguishable stages.

### Shared memory event with source facets and authority class

Observed memory events include event type, content, source facets, authority class, provenance, and creation time.

Hyperconnectome lesson: memory provenance may include which subsystem/lens contributed a record without granting that subsystem permanent ownership of the memory.

### Qualification/checkpoint binding

Observed checkpoint/qualification structures bind payloads to source-set digests, evaluator references, evidence digests, predecessor checkpoints, and timestamps.

Hyperconnectome lesson: installed capability, current runtime checkpoint, and qualification evidence are separable facts.

## 5. Failure/operations observations

Observed generic schema family: `bug_ops.*`

Relevant structures include bug/incident events, dispatch events, operation receipts, role registry, and system configuration.

Reusable observations:

- incident evidence should be separable from dispatch/ownership;
- attempted operation and verified outcome should be distinguishable;
- an operation receipt is evidence of an operation/result, not automatically proof that a larger objective is complete;
- current configuration should be queryable independently of historical incident state.

## 6. What is intentionally excluded

The production database also contains identity-scoped/private tables. Those tables were not used as payload sources for this repository.

The generic template may later abstract reusable mechanics such as append-only save-state events, supersession edges, memory-epoch receipts, or bootstrap/readback transactions, but only after the mechanism is restated without carrying private identity data or identity-specific naming into the template.

## 7. Candidate generic contracts derived from these observations

These are `DESIGN_PROPOSAL`, not claims that Supabase proved the architecture:

```text
SIGNAL_ENVELOPE {
  signal_id
  schema_version
  source_node
  audience
  domain
  intent
  priority
  causal_parent?
  correlation_id?
  expires_at?
  authority_ref?
  source_refs[]
  content_hash
  idempotency_key
  payload
}
```

```text
STATE_SNAPSHOT {
  snapshot_id
  source_revision
  manifest_digest?
  materialization_version
  load_state
  validation_state
  activation_state
  object_count
  readback_revision?
  created_at
}
```

```text
SUCCESSION_TRANSFER {
  transfer_id
  predecessor_runtime?
  successor_runtime?
  predecessor_generation
  successor_generation
  capsule_digest
  transfer_status
  created_at
  consumed_at?
}
```

```text
QUARANTINED_SIGNAL {
  original_signal_id
  failure_stage
  failure_code
  diagnostic
  attempted_route?
  replay_state
  retry_count
}
```

The later schema must remain storage-provider neutral: none of these contracts require PostgreSQL or Supabase specifically.
