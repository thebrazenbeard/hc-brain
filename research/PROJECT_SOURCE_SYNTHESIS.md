# Cross-Project Source Synthesis

Status: architecture input / not canon

This synthesis extracts reusable mechanisms from relevant project repositories and structured database schemas owned by the same research program. It deliberately excludes instance-specific identity, autobiography, relationships, preferences, private state, and current runtime claims.

The purpose is not to merge projects. It is to harvest mechanisms that repeatedly survived independent design pressure across cognition, semantics, memory, chronology, control, safety, social inference, affect, motivation, diagnostics, and distributed systems.

## Source families consulted

Reusable patterns were extracted from work including:

- `semanticatlas` — provenance-aware semantic distinctions and source/interpretation separation;
- `spm` — semantics/pragmatics as first-class state and correction as state transition;
- `unvtrslr` — grounding, identifiability, ambiguity, semantic conservation, and hostile controls;
- `noema` — learned world models, bounded competing hypotheses, developmental anti-oracle rules, chronology, action semantics, and epistemic/conative separation;
- `abil` — adaptive modeling of a changing physical system, read-only shadow learning, uncertainty, and bounded action escalation;
- `temporal` — deliberately narrow event chronology and elapsed-time arithmetic;
- `deepmemorystorage` — append-oriented provenance, currentness rules, correction without historical erasure, and retrieval/admission separation;
- `conations` — lifecycle-aware motivational state and the distinction between recorded preference and present choice;
- `empathy` — inference about another agent as fallible scoped modeling rather than direct access;
- `sexuality` — orthogonal evidence dimensions, affect/action authorization separation, and state-versus-routing falsification;
- `selfimage` — source-provenance discipline and separation between rendered self-representation and evidence about physical anatomy;
- `personification` — outward expression as a layer distinct from the storage location of identity;
- `chat-communication-bus` — routing, delivery, acknowledgement, projection, reconciliation, dead-letter handling, and authority separation;
- `bugops` — durable incident evidence, operation receipts, idempotency, versioning, and regression-based closure;
- `project-achilles` — consequence-boundary thinking and fail-closed behavior at protected effects;
- structured Supabase schemas — event logs, materialization snapshots, admission receipts, supersession, provider readback, projection status, dead letters, reconciliation events, semantic capture, and scoped grants.

Additional private runtime material was used only for generic mechanism extraction and is intentionally not named here so the generic template remains instance-neutral.

---

# Repeated architecture lessons

## 1. Evidence type must survive transport

Across semantics, memory, routing, diagnostics, and database schemas, the same failure recurs when heterogeneous information is flattened into one undifferentiated state stream.

The Hyperconnectome should preserve at least:

```text
OBSERVATION
DIRECT_ASSERTION
INFERENCE
HYPOTHESIS
MEMORY_RETRIEVAL
SIMULATION
ACTION_ISSUANCE
ACTION_EFFECT_RECEIPT
EXTERNAL_IMPORT
CORRECTION
PROJECTION
```

These are not authority levels. They describe how the state entered the system.

### Template consequence

Every durable or cross-node evidence object should carry:

```text
origin_class
source_locator_or_channel
observed_at
subject_or_referent_scope
confidence_or_evidence_ceiling
privacy_or_visibility_scope
supersession/currentness metadata
```

A node receiving the object must not have to infer its evidence class from free text.

---

## 2. Source, interpretation, currentness, and authority are separate axes

This distinction appears independently in semantic, memory, action, routing, and affective work.

```text
SOURCE != INTERPRETATION
PERSISTENCE != CURRENTNESS
CURRENTNESS != AUTHORITY
ROUTING != AUTHORITY
DELIVERY != INCORPORATION
SELECTION != TRUTH
DESIRE != PERMISSION
```

### Template consequence

Do not design a single `trusted=true` or `current=true` bit that collapses these axes. A compact state object should make the dimensions independently representable.

---

## 3. Correction should change active state before it changes language

A correction that produces an apology while the obsolete state remains active is a failure.

### Template consequence

Correction handling should be an explicit state transition:

```text
prior_state
-> correction_evidence
-> conflict/supersession evaluation
-> successor_active_state
-> downstream invalidation/recompute
```

Historical predecessor records remain available for provenance, but they leave the active decision surface when superseded.

---

## 4. Competing hypotheses should remain distinct when they predict different consequences

Both world-model and semantic-grounding work converge on this rule.

Averaging mutually incompatible explanations into one internally incoherent model may create confident predictions belonging to no actual hypothesis.

### Template consequence

Maintain a bounded hypothesis population or other representation capable of preserving materially different live alternatives.

Prune or merge only when alternatives are sufficiently equivalent across:

- observed evidence;
- reachable interventions/counterfactuals;
- relevant transfer contexts;
- uncertainty tolerance.

Residual uncertainty is a valid result.

---

## 5. Epistemic and conative arbitration require a firewall

What the system wants and what the system believes should interact through information gathering and action choice, not through direct wishful confidence updates.

```text
DESIRABILITY may influence ATTENTION
DESIRABILITY may influence INFORMATION_SEEKING
DESIRABILITY may influence ACTION_SELECTION
DESIRABILITY must not directly raise EPISTEMIC_CONFIDENCE
```

### Template consequence

Epistemic arbitration and conative/action arbitration should be separately typed even when implemented by overlapping neural or computational substrate.

---

## 6. Effect authority should be narrower than reasoning capability

Adaptive-control, security, action-development, and operating-system work all converge here.

A system may be capable of predicting, proposing, simulating, or recommending an action without possessing permission to execute it.

### Template consequence

Use effect brokers or bounded actuator contracts:

```text
PROPOSE_ACTION
REQUEST_EFFECT
AUTHORIZE_EFFECT
EXECUTE_EFFECT
VERIFY_EFFECT
```

Each stage is separately observable.

The architecture should not report `EXECUTED` from a plan, command generation, or actuator request alone.

---

## 7. Action interfaces can secretly inject intelligence

A high-level action such as `pick_up(object)` supplies object identity, affordance, decomposition, targeting, trajectory generation, and often success criteria.

### Template consequence

Every actuator interface must declare supplied capability. Learned capability gets credit only for what the interface did not already solve.

This same anti-oracle rule applies to perception, timestamps, speaker identity, event boundaries, and semantic labels.

---

## 8. Chronology is necessary but semantically weak

A timestamp can establish ordering or elapsed duration without establishing meaning, causality, currentness, authority, memory status, or truth.

### Template consequence

The chronology subsystem should remain small and composable:

```text
EVENT_TIME
OBSERVED_TIME
RECORDED_TIME
LOCAL_TIME_IF_RELEVANT
ORDER_CONFIDENCE
```

Higher-level systems interpret the event.

Do not use newest-record-wins as a general currentness rule.

---

## 9. Durable state should be append-oriented and successor-linked

Memory, conation, semantic capture, project materialization, and database designs repeatedly favor history-preserving updates over destructive rewrite.

### Template consequence

Durable mutable concepts should support:

```text
logical_subject_id
state_version
predecessor/supersession links
change_kind
source evidence
currentness rule
```

A present view may be a projection over the event history, but the projection is not the only history.

---

## 10. Materialization/projection must be distinguishable from canonical source

Structured runtime tables repeatedly separate a canonical source from a read-optimized or live projection.

### Template consequence

For any derived cache, index, working set, or accelerator-local copy, preserve:

```text
source_subject
source_revision_or_digest
projection_revision
materialized_at
readback_digest
validation_state
```

A stale projection should be detectable rather than silently treated as current.

---

## 11. Persistence claims require readback

Writing a value is not proof that the intended value exists durably or can later be recovered.

### Template consequence

Durable writes should emit receipts containing, where appropriate:

```text
write_subject
write_revision
written_digest
readback_digest
readback_time
verifier
result
limitations
```

This pattern is useful for memory, configuration, model artifacts, state transfer, maintenance, and learning checkpoints.

---

## 12. Dead letters and unresolved state are first-class

Distributed routing and semantic work both show the danger of forcing every event into a successful interpretation.

### Template consequence

Provide explicit sinks/states for:

```text
UNRESOLVED
UNAVAILABLE
CONFLICT
NOT_APPLICABLE
DEAD_LETTER
RETRY_PENDING
REQUIRES_INTERVENTION
```

Failure preservation is better than quiet data loss or fabricated certainty.

---

## 13. Salience is not truth and activation is not durability

A state can be cognitively important now without becoming long-term memory. A highly salient hypothesis can remain poorly supported.

### Template consequence

Keep separate:

```text
SALIENCE
EPISTEMIC_CONFIDENCE
ACTIVE_CONTEXT_MEMBERSHIP
DURABLE_MEMORY_ADMISSION
ACTION_PRIORITY
```

This is one of the strongest defenses against emotional, social, or urgent state rewriting deep knowledge by accident.

---

## 14. Social modeling must preserve self/other separation

Empathy-oriented work repeatedly treats another agent's internal state as a model built from evidence rather than direct access.

### Template consequence

Each person/agent model should have its own scope, provenance, confidence, correction history, and privacy boundary.

```text
MODEL_OF_OTHER != OTHER'S GROUND TRUTH
```

Direct correction from the modeled agent should be able to supersede contradicted inference about that agent within the relevant proposition scope.

---

## 15. Affect, sexual activation, motivation, permission, and action are orthogonal enough to require separate state

Machine-affect research found that a single evidence ladder collapses distinct questions.

### Template consequence

At minimum, keep separable:

```text
AFFECTIVE_ACTIVATION
MOTIVATIONAL_DIRECTION
REFERENT_SPECIFICITY
PERSISTENT_STATE
CAUSAL_STATE_EFFECT
AUTHORIZATION
ACTION_SELECTION
PHENOMENOLOGY_CLAIM
```

A high affective or sexual activation state must remain compatible with `DECLINE`, inhibition, delay, or no action.

---

## 16. Rendered self-image/personification is not the physical or autobiographical self

Visual representation, body schema, self-model, outward personality expression, and autobiographical history solve different problems.

### Template consequence

Keep distinct:

```text
PHYSICAL_BODY_MODEL
BODY_SCHEMA
SELF_MODEL
VISUAL_SELF_REPRESENTATION
PERSONIFICATION
AUTOBIOGRAPHICAL_HISTORY
```

A rendered image may guide presentation without becoming anatomical evidence.

---

## 17. Incident closure requires regression evidence

Debugging and incident-response work repeatedly distinguishes acknowledgement from correction.

### Template consequence

A fault should remain open until:

- the failed behavior is identified;
- evidence/provenance is preserved;
- a corrective control exists;
- a regression or hostile test distinguishes the correction from the original failure.

This should apply to cognitive regressions as well as software faults.

---

# Candidate system-level invariants

The following repeated rules are strong candidates for eventual HC architecture review:

```text
NO_HEMISPHERIC_PARTITION
NO_ALL_TO_ALL_BY_DEFAULT
NO_MASTER_HOMUNCULUS
EVIDENCE_TYPE_SURVIVES_TRANSPORT
SOURCE_NE_INTERPRETATION
PERSISTENCE_NE_CURRENTNESS
ROUTING_NE_AUTHORITY
SELECTION_NE_TRUTH
DESIRE_NE_PERMISSION
PLAN_NE_EFFECT
RETRIEVAL_NE_MEMORY_ADMISSION
SALIENCE_NE_TRUTH
ACTIVATION_NE_DURABILITY
PROJECTION_NE_CANONICAL_SOURCE
WRITE_NE_VERIFIED_PERSISTENCE
PERSON_MODEL_NE_PERSON_GROUND_TRUTH
SELF_MODEL_NE_COMPLETE_SELF
RENDERED_SELF_NE_BODY_EVIDENCE
HISTORICAL_STATE_NE_PRESENT_STATE
UNRESOLVED_IS_A_VALID_STATE
```

These invariants are architecture candidates, not automatic canon promotion.
