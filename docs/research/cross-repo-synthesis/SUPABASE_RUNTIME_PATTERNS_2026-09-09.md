# Supabase Runtime Patterns — 2026-09-09

Status: schema-level research/provenance observation.

This document records generic runtime patterns observed in the owner's available Supabase projects during the cross-repo synthesis pass. No personal row payloads, credentials, auth data, vault content, private messages, or raw memory content are transferred into the HC template.

GitHub source architecture and Supabase runtime/provider state remain separate evidence classes.

## Available projects observed

- Project `klmbpaigzeguvnpccqzz` — active provider project containing memory, semantic-runtime, routing, lineage, coordination, and Build Team schemas.
- Project Lantern `agvhmutlrolbaijzlbqk` — stable governed-material backend used here only for provenance/currentness patterns.

## Pattern 1 — append-only events plus derived current state

Observed structures include append-oriented event tables paired with current/head projections.

Reusable principle:

> Preserve historical events; compute current state from explicit lifecycle/supersession relationships rather than overwriting history.

Relevant observed fields included stable record IDs, lifecycle status, epistemic status, authorship/source, privacy scope, event time, state time, record time, explicit predecessor/supersession references, payload/evidence, and semantic tags.

HC transfer targets:

- `current memory storage/CURRENT_STATE_SELECTION.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `chronology/TEMPORAL_EVENT_CONTRACT.md`
- `self identity/CONTINUITY_SUBSTRATE.md`

## Pattern 2 — fail-closed head resolution

Observed current-state views resolve a record only when the supersession graph produces exactly one defensible head within the relevant logical scope. Chronology alone does not choose among competing heads.

Reusable principle:

`LATEST != CURRENT`

When competing unsuperseded states remain, represent ambiguity instead of selecting by timestamp.

## Pattern 3 — supplemental supersession graph

Observed designs support direct predecessor pointers plus separate child/parent supersession edges for cases where one linear predecessor field is insufficient.

Reusable principle:

State history may be a DAG rather than a simple list. Corrections, merges, forks, and reconciliation should remain explicit.

## Pattern 4 — provider readback receipts

Observed provider-receipt structures separately record write intent/effect evidence and readback confirmation, including provider class/identity/locator/version, operation identity, content digests, byte lengths, write observation, readback time/hash, verifier route, result, and limitations.

Reusable principle:

`WRITE_REQUESTED != STORED`

`STORED != READ_BACK_VERIFIED`

`READ_BACK_VERIFIED != SEMANTICALLY_CURRENT`

HC transfer targets: durable memory, continuity transfer, configuration/plasticity checkpoints, and any external storage peripheral whose exact persistence matters.

## Pattern 5 — derived runtime materialization bound to immutable source

The `semantic_atlas` schema contains runtime snapshots/objects bound to Git commit/ref/repository identity, manifest/pathset/snapshot digests, validation state, activation/readback state, loader/materialization version, and object counts.

Reusable principle:

A fast runtime projection may be disposable/rebuildable while the source ledger remains distinct. Runtime materialization does not create semantic authority by itself.

`DERIVED_RUNTIME != CANONICAL_SOURCE`

## Pattern 6 — semantic capture is candidate generation

Observed semantic capture structures separate the event that something appeared salient/semantically interesting from the outcome/admission decision. Capture records carry source surface/locator/actor, detector, trigger, salience, candidate kind, representation/fidelity, privacy scope, evidence ceiling, and sequence. Outcomes separately record disposition and Git/source binding where admitted.

Reusable principle:

`CAPTURED != TRUE`

`SALIENT != CANONICAL`

`CANDIDATE != MEMORY_OR_SEMANTIC_ADMISSION`

HC transfer target: salience/attention, semantics, and memory admission.

## Pattern 7 — typed routed-message envelope

Observed Radar message structures contain message ID, schema version, sender/source, audience, domain, intent, priority, root task, correlation ID, causal parent, acknowledgement requirement, expiry, authority reference, source references, content hash, idempotency key, payload, and projection status.

Reusable principle:

Routing should preserve lineage and delivery state while remaining separate from truth, incorporation, and authority.

`ROUTED != INCORPORATED`

`DELIVERED != BELIEVED`

`PRIORITY != AUTHORITY`

HC transfer target: Noöplex Fabric routing.

## Pattern 8 — capability registry and subscriptions

Observed node/subscription structures distinguish runtime node identity, status, capabilities, heartbeat/health, domain subscriptions, intent filters, minimum priority, and active state.

Reusable principle:

Capability advertisement and routing eligibility are separate from competence, semantic correctness, health, and action authorization.

## Pattern 9 — dead letters and reconciliation

Observed dead-letter structures preserve failure stage/code, original envelope, diagnostics, attempted route, applicability, replay state, retry count, and timestamps. Reconciliation events separately record repair class/source/detail.

Reusable principle:

Failed internal communication or state incorporation should remain inspectable and potentially replayable rather than disappearing silently.

HC transfer targets: resolver, routing, fault handling.

## Pattern 10 — multi-perspective snapshot-bound decisions

Observed Build Team structures separately represent perspectives and decisions, each bound to a task and snapshot digest. Append-only memory events retain source facets and authority/provenance separately.

Reusable principle:

Multiple coherent internal perspectives can coexist until arbitration. A decision should be traceable to the state cut it used.

HC transfer target: distributed arbitration.

## Pattern 11 — lineage and succession

Observed lineage/succession structures track generation, lineage key, transfer ID, runtime token, previous/next lineage, capsule digest, source/successor runtime references, transfer status, and timestamps.

Reusable principle:

Continuity across runtime/hardware generations should be represented as explicit provenance-bearing succession rather than assumed from labels or session chronology.

## Pattern 12 — stable material cut / read consistency

Project Lantern was consulted using its required B0 → payload → B1 stability sequence. The observed material cut was stable: the same facade/profile/policy digest and two exact members appeared at B0 and B1.

Reusable principle:

When a multi-read decision depends on mutable provider state, bind reads to a stable cut or fail closed if the cut changes. Do not mix observations from incompatible snapshots.

The Lantern material itself did not define HC architecture; only the stable-cut/provenance discipline was transferred.

## Explicit non-transfer

The synthesis did not inspect or transfer secret/vault/auth payloads, private identity rows, personal memories, intimate content, raw coordination messages, or named-person state from Supabase.

Schema existence is evidence of an implemented data model, not proof that an equivalent physical cognitive mechanism is necessary, sufficient, active, or conscious.
