# State, Provenance, Currentness, and Reconciliation

Status: cross-project engineering synthesis / architecture input

This document extracts repeated state-management mechanisms from semantic, memory, routing, diagnostics, canonical-material, database, and projection systems. It is engineering evidence: these patterns have survived multiple independent implementations and hostile reviews, but they are not biological facts and are not automatically architecture canon.

## 1. One `state` field is not enough

Independent systems repeatedly fail when source, interpretation, currentness, authority, and lifecycle are compressed into one status.

The HC should preserve these as orthogonal dimensions:

```text
SOURCE_ORIGIN
CONTENT_OR_PROPOSITION
EVIDENCE_CLASS
INTERPRETATION
CURRENTNESS
AUTHORITY_SCOPE
LIFECYCLE
CONFIDENCE
PRIVACY_SCOPE
SALIENCE
```

Examples of invalid collapses:

```text
persisted -> current
newest -> authoritative
retrieved -> admitted
selected -> true
delivered -> incorporated
high confidence -> measured
```

---

## 2. Evidence class must survive transport

A receiving node should not have to infer from prose whether a datum was measured, derived, inferred, retrieved, simulated, asserted, or corrected.

Candidate origin/evidence classes include:

```text
MEASURED_OR_DIRECT_OBSERVATION
DERIVED
INFERRED
DIRECT_ASSERTION
HYPOTHESIS
MEMORY_RETRIEVAL
SIMULATION
ACTION_ISSUANCE
ACTION_EFFECT_RECEIPT
EXTERNAL_IMPORT
CORRECTION
PROJECTION
```

These are not a universal trust ladder. A direct assertion can be wrong; an inference can be excellent; a measurement can be miscalibrated. The class answers **what kind of thing this is**.

### HC implication

`EVIDENCE_TYPE_SURVIVES_TRANSPORT` should be a system invariant.

---

## 3. Canonical source and projection are different objects

Multiple systems independently benefit from separating durable canonical source from read-optimized projections, indexes, caches, summaries, embeddings, or runtime-visible materializations.

A projection should bind itself to what produced it.

```text
PROJECTION_RECEIPT {
  projection_id
  source_subject
  source_revision_or_digest
  projection_revision_or_digest
  materialized_at
  transformation_ref
  fidelity_scope
  readback_or_validation_state
}
```

A projection that cannot identify its source revision is useful only within a lower evidence ceiling.

### HC implication

```text
PROJECTION != CANONICAL_SOURCE
PROJECTION_MATCH != SEMANTIC_AUTHORITY
```

A current working set may be disposable and rebuilt from authoritative history.

---

## 4. Persistence requires readback evidence

A successful write request proves that a write was attempted or accepted by an interface. It does not prove that the intended bytes/state are durably recoverable.

Candidate write lifecycle:

```text
WRITE_REQUESTED
WRITE_ACKNOWLEDGED
READBACK_OBSERVED
DIGEST_VERIFIED
PERSISTENCE_CLAIM_BOUNDED
```

### HC implication

Durable brain-state changes should produce receipts appropriate to their risk and importance.

```text
write_subject
expected_revision
written_digest
readback_digest
readback_time
storage_provider_or_device
verifier
result
limitations
```

Not every volatile working-state update needs heavyweight receipts. The requirement scales with persistence and consequence.

---

## 5. Currentness is proposition- and scope-specific

A record can be historically true and currently obsolete. A state can remain current for one scope while being superseded for another.

Candidate currentness states:

```text
CURRENT
HISTORICAL
SUPERSEDED
EXPIRED
REVOKED
CONFLICT
UNRESOLVED
NOT_APPLICABLE
```

### HC implication

Currentness should be computed from declared rules and successor/conflict evidence rather than `max(timestamp)`.

Examples:

- a calibration remains current until a newer calibration, hardware change, expiry rule, or anomaly invalidates it;
- an active task state expires when the task closes;
- an autobiographical event remains historical without being a current preference;
- a permission can expire while the historical grant remains recorded.

---

## 6. Correction creates a successor; it does not erase history

Semantic, memory, diagnostic, and event-ledger systems repeatedly converge on successor-linked correction.

```text
prior_record
-> correction_or_conflict_evidence
-> successor_record
```

The predecessor remains inspectable for history and provenance, while active projections stop using it where superseded.

### HC implication

A correction must change active reasoning state before the system receives credit for producing corrected language.

---

## 7. Identity must cross a decision boundary as data when identity matters

A recurring distributed-systems failure occurs when an exact decision is made using only a broad provider, route, collection, evidence class, or revision identifier.

If a decision concerns event B, a record about event A must not qualify merely because both came from the same source revision.

### HC implication

Use explicit selectors/bindings such as:

```text
subject_ref
proposition_ref
event_ref
actor_ref
source_ref
path_or_locator
logical_key
```

The minimal rule is:

> **If identity matters to a decision, that identity must cross the runtime boundary as data.**

Do not infer decisive identity from route names, timestamps, topic similarity, or evidence class.

---

## 8. Reconciliation and authority are separate gates

Two providers can contain byte-identical representations of the same record without either copy being authoritative for a different proposition.

A robust chain is:

```text
EXACT_INSTANCE_READ
-> INSTANCE_RECONCILIATION
-> EVIDENCE_TYPING
-> CURRENTNESS_CHECK
-> PROPOSITION/REFERENT_AUTHORITY_CHECK
-> ACTIVE_CONTEXT_ADMISSION
```

### HC implication

`VERIFIED_EXACT` should mean only what it says: the compared instances match under the declared binding. It must not silently mean `TRUE`, `CURRENT`, `AUTHORIZED`, or `ADMITTED`.

---

## 9. Dead letters and unresolved states preserve information

Distributed cognition cannot guarantee that every observation has a valid route, interpretable schema, reconcilable provenance, or currently qualified consumer.

Candidate states:

```text
UNRESOLVED
UNAVAILABLE
CONFLICT
ABSENT
DEAD_LETTER
RETRY_PENDING
QUARANTINED
REQUIRES_INTERVENTION
```

### HC implication

A dead-letter path is part of cognition's error model, not merely messaging plumbing. It prevents silent loss and gives later repair/reinterpretation a recoverable subject.

---

## 10. Canonicalization and hashing prove representation identity, not semantic truth

Deterministic canonical bytes and content hashes are powerful for persistence, projection, replication, and corruption detection.

They prove statements such as:

```text
these bytes match
this record is unchanged
this projection was built from this revision
```

They do not prove:

```text
this claim is true
this interpretation is correct
this state is current
this actor has authority
```

### HC implication

Cryptographic representation integrity belongs below semantic adjudication.

---

## 11. Suggested durable record envelope

```text
HC_RECORD {
  record_id
  record_type
  schema_version
  subject_ref
  actor_or_source_ref
  created_at
  observed_at
  event_time_if_known
  evidence_class
  provenance
  lineage_key
  predecessor_record_id
  currentness_rule
  authority_scope
  privacy_scope
  payload
  representation_digest
}
```

Not every field must be globally mandatory. Specialized record families may narrow the envelope, but they should not erase distinctions required by downstream decisions.

---

## Hostile tests

1. **Newest-wins trap:** write a late archival copy of old state; active current state must not regress.
2. **Wrong-instance exact-match:** return matching source/target revisions for event A while requesting event B; reconciliation must fail or remain unresolved.
3. **Projection-authority laundering:** make a cache newer than canonical source; the cache must not become source authority by timestamp.
4. **Write-without-readback:** acknowledge a write but corrupt the stored bytes; persistence claim must fail.
5. **Evidence-class laundering:** reserialize an inference as a generic record; provenance must preserve that it remains inference.
6. **Correction history:** supersede a prior record; current projection changes while predecessor stays inspectable.
7. **Cross-proposition admission:** provide correct evidence class for the wrong proposition; active-context admission must reject it.
8. **Unavailable provider:** remove one projection provider; canonical source remains usable if the route policy permits fallback.
9. **Digest-truth trap:** provide perfectly hashed false content; integrity passes while semantic truth remains separately unresolved.
10. **Dead-letter recovery:** route an unknown schema to quarantine, later install the schema, and recover the exact preserved subject without inventing missing history.

## Internal engineering provenance

This synthesis generalizes mechanisms already represented in `PROJECT_SOURCE_SYNTHESIS.md`, including canonical/source separation, typed evidence, append-oriented history, projection receipts, readback, reconciliation, scoped grants, semantic adjudication, dead letters, and deterministic record envelopes.