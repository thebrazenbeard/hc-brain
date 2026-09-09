# Resolver Architecture

Status: canonical subsystem architecture.

## Purpose

`resolver` manages technical and semantic conflict surfaces that arise when the HC contains competing interpretations, incompatible state claims, stale dependencies, duplicated operations, failed routes, version conflicts, calibration disagreement, or unresolved cross-system assertions.

It does not act as a universal truth oracle or central executive.

`RESOLVED_FOR_OPERATION != PROVEN_TRUE`

`CONFLICT_DETECTED != ONE_SIDE_FALSE`

`TECHNICAL_RECONCILIATION != MORAL_ADJUDICATION`

`RESOLVER != CENTRAL_EXECUTIVE`

## Architectural role

The HC is a distributed temporal hypergraph. Multiple subsystems can legitimately produce claims that disagree because they use different evidence, models, timescales, scopes, or purposes.

`resolver` provides shared mechanisms for making those disagreements explicit, tracing dependencies, selecting bounded technical remedies, preserving unresolved alternatives, and preventing stale or contradictory state from silently contaminating downstream cognition.

It answers questions such as:

- what exactly conflicts?;
- are the claims actually about the same scope/time/referent?;
- is one state stale or superseded?;
- did a correction invalidate dependent conclusions?;
- can both claims remain valid under different contexts?;
- can a bounded operational choice be made without erasing uncertainty?;
- should processing retry, quarantine, dead-letter, or request more evidence?;
- what downstream state must be reconsidered after reconciliation?

## Conflict classes

The resolver should support, at minimum:

- semantic/propositional contradiction;
- competing interpretation hypotheses;
- currentness/version conflict;
- duplicate/idempotency conflict;
- stale dependency after correction;
- source/provenance mismatch;
- calibration disagreement;
- body-schema/embodiment mismatch;
- route/subscription/configuration conflict;
- action-policy/authorization conflict;
- timing/order ambiguity;
- synchronization/replica conflict;
- social/relationship-model disagreement;
- memory lineage/supersession conflict;
- subsystem health/qualification disagreement;
- resource/availability conflict;
- external-service result disagreement.

Different classes require different resolution rules. One generic "pick a winner" algorithm is insufficient.

## Conflict object

A generic conflict should be able to carry:

```text
CONFLICT_RECORD {
  conflict_id
  conflict_class
  claims_or_states[]
  source_refs[]
  evidence_refs[]
  scope
  time_scope
  dependency_refs[]
  authority_refs[]
  confidence_by_claim
  currentness_by_claim
  severity
  affected_capabilities[]
  affected_actions[]
  proposed_resolution_modes[]
  status
  provenance
}
```

The conflict object should preserve enough information to revisit the decision if evidence, currentness, or authority changes.

## Pre-resolution normalization

Before treating two statements as contradictory, the resolver should test whether the conflict disappears after clarifying:

- referent identity;
- time interval;
- spatial/embodiment scope;
- relationship/group scope;
- modality;
- measurement versus inference;
- source authority;
- lifecycle state;
- model/version;
- units/calibration;
- descriptive versus normative claim;
- simulation/prediction versus observation.

Many apparent contradictions are scope mismatches rather than mutually exclusive facts.

## Resolution modes

Possible bounded resolution modes include:

- preserve both as context-scoped states;
- prefer newer valid state under an explicit currentness rule;
- prefer stronger/directer evidence while retaining alternatives;
- mark one state superseded without deleting history;
- split an overbroad claim into narrower scoped claims;
- reconcile multiple predecessors into a successor representation;
- request discriminating evidence;
- defer/leave unresolved;
- quarantine suspect output;
- retry technical operation;
- deduplicate/idempotently collapse one technical effect;
- route to a domain-specific authority gate;
- terminate/reform a coalition;
- dead-letter a failed operation for later inspection.

A resolution mode must fit the conflict class and scope.

## Correction propagation

A correction is not complete merely because one source record changed.

When a materially used claim is corrected or superseded, the HC should be able to identify dependent state such as:

- derived interpretations;
- current-state projections;
- behavioral models;
- social/relationship models;
- action plans;
- predictions;
- semantic conclusions;
- memory summaries;
- learned calibration;
- active coalitions.

Affected dependents should be marked for reevaluation, invalidation, supersession, or explicit retention with justification.

`CORRECTION != GLOBAL_RESET`

`CORRECTION != SILENT_LOCAL_EDIT`

Dependency-aware propagation should be narrow enough to avoid unnecessary whole-organ disruption while broad enough to prevent stale conclusions from surviving unnoticed.

## Contradiction semantics

A contradiction does not automatically imply that one assertion should be inverted or deleted.

`CONTRADICTION != AUTOMATIC_INVERSION`

Possible states include:

- one claim false;
- both partially wrong;
- different scopes;
- different time intervals;
- source corruption;
- ambiguous referent;
- unresolved evidence;
- model mismatch;
- genuine inconsistency that must remain explicit until more evidence exists.

## Currentness and lineage

The resolver should use chronology and explicit lineage rather than "latest row wins" as a universal rule.

A newer statement may be weaker, mistaken, out of scope, or merely a new observation rather than a correction.

A supersession edge indicates lineage, not semantic truth by itself.

`NEWER != TRUER`

`SUPERSEDES != VERIFIED_TRUE`

## Technical conflict handling

For routing, synchronization, storage, and effect infrastructure, the resolver should support explicit technical semantics such as:

- operation IDs;
- idempotency keys;
- expected prior versions;
- compare-and-set style transitions;
- deterministic duplicate handling;
- retry bounds;
- timeout/expiry;
- dead-letter state;
- delivery versus incorporation distinction;
- provider/write/readback receipt distinction.

Technical success does not establish semantic correctness.

`DELIVERED != INCORPORATED`

`WRITE_SUCCEEDED != SEMANTICALLY_CORRECT`

## Action and authority conflicts

When an action candidate conflicts with safety, consent, permission, maintenance state, developmental qualification, or other authority constraints, resolver may expose the conflict and route it to the appropriate authorization/arbitration mechanism.

It must not invent authority simply to eliminate the conflict.

`NO_CLEAR_AUTHORITY != RESOLVER_MAY_AUTHORIZE`

A blocked action may remain blocked while the cognitive conflict stays unresolved.

## Local fail-closed behavior

A severe conflict may justify failing closed for one effect, route, memory write, or subsystem interaction without halting all cognition.

Whole-organ inhibition should be reserved for conflicts whose consequence genuinely crosses protected system boundaries or threatens continuity/safety at organ scale.

`LOCAL_FAIL_CLOSED != WHOLE_BRAIN_HALT`

## Dead-letter and unresolved state

Unresolvable technical or cognitive conflicts must remain visible.

A dead-letter/unresolved record should carry enough context to answer:

- what failed or conflicted?;
- what was attempted?;
- what evidence/state existed?;
- what was blocked?;
- whether retry is safe;
- what new evidence or authority is required;
- what downstream state may remain affected.

Silence is not successful resolution.

## Domain authority boundary

`resolver` owns reconciliation mechanics, not every domain's substantive decision.

It does not independently decide:

- moral truth;
- personal identity;
- consent;
- sexuality boundaries;
- values/commitments;
- social legitimacy;
- epistemic truth merely from conflict count;
- whether an external effect is authorized.

Those remain with the relevant HC systems and arbitration/authority contracts.

## Learning boundary

Repeated conflict patterns may generate learning/plasticity candidates, such as improved routing, better source reliability estimates, narrower social rules, updated calibration, or better conflict classifiers.

Conflict frequency itself does not authorize durable global policy change.

A temporary reconciliation strategy must not silently become a permanent control path without plasticity/admission governance.

## External compute and providers

External models, databases, synchronization services, or adjudication tools may supply evidence or technical service results.

They cannot become the sole conflict authority for essential HC cognition merely because they host a canonical-looking record or return a confidence score.

External conflict results remain typed evidence and are reconciled inside the HC.

## Failure modes

- treating disagreement as proof one side is false;
- latest-write-wins used as universal semantic truth;
- correction failing to invalidate dependents;
- correction triggering unnecessary global reset;
- technical success promoted to semantic truth;
- unresolved conflict silently discarded;
- resolver inventing action authority;
- dead-letter state hidden from downstream health monitoring;
- duplicate action effect executed twice because cognitive and technical idempotency were conflated;
- stale calibration retained after embodiment change;
- social disagreement flattened into one privileged narrative without evidence;
- external provider treated as authoritative cognitive arbiter;
- resolver becoming a permanent executive/homunculus.

## Cross-system interfaces

`resolver` is cross-cutting and strongly coupled with:

- `semantics` and `pragmatics` for interpretation conflicts;
- current/deep memory for lineage/currentness/correction;
- `chronology` for ordering and time scope;
- `cognition` for competing hypotheses and discriminating evidence;
- `self identity`, `Empathy`, `sociological behaviors`, `sexuality`, and `psychological behaviors` for domain-scoped conflict;
- `adaptable I-O handler` and `somatics` for calibration/embodiment conflict;
- routing/neuroplasticity for route/plasticity reconciliation;
- `integration-arbitration` for scoped decision formation;
- `kinesis` for action conflict without authority leakage;
- `basic operating instructions` for lifecycle/health/implementation-state conflicts.

## Evidence boundary

This architecture defines conflict-management semantics. It does not claim a universal algorithm can resolve every semantic, social, ethical, epistemic, or identity dispute.

## Provenance

Expanded from `resolver/CONFLICT_AND_RECONCILIATION.md` and reconciled against current memory-lineage, chronology, epistemic-control, lifecycle, routing, action-authority, external-compute, and temporal-hypergraph contracts.
