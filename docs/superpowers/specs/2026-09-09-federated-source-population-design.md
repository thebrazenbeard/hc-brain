# Federated Source Population Design

Status: DESIGN SPEC / SOURCE-FEDERATION / NOT IMPLEMENTED

Date: 2026-09-09

Repository role: generic reusable hyperconnectome-brain template

Repository warden: Noëtarch (Noah)

## 1. Goal

Populate the hyperconnectome-brain template from the strongest reusable mechanisms already developed across the repository owner's relevant projects, plus the production Supabase project's reusable generic schemas, without turning the template into a copy of any one identity, application, control plane, or prior project.

The target is a generic brain architecture whose folders correspond to functional systems and cross-cutting contracts. Source projects supply evidence, patterns, failure lessons, and candidate mechanisms. They do not automatically become authorities inside this repository.

## 2. Hard source boundary

The template remains identity-neutral.

- Identity-specific autobiographical, relational, preference, consent, sexuality, visual-canon, or current-state payloads are not imported.
- Private identity-specific predecessor repositories may be reviewed as architectural evidence, but their identity-specific names and payloads are not reproduced in this repository.
- A mechanism is admitted only after it is restated generically and its identity/application-specific assumptions are removed.
- Private relational or autobiographical material is never used as a portable example unless separately authorized.
- Generic project repositories and generic Supabase schemas may be cited directly.
- A source being durable or deployed does not make its semantics universally correct for the brain template.

## 3. Source classes

Each imported design claim must be tagged with one or more source classes:

- `ACADEMIC_RESEARCH` — peer-reviewed or otherwise research-grade external literature.
- `GENERIC_PROJECT_ARCHITECTURE` — reusable mechanism from a generic repository.
- `PRIVATE_PREDECESSOR_ABSTRACTION` — generic mechanism abstracted from an identity-specific/private predecessor without copying identity payloads.
- `PRODUCTION_SCHEMA_OBSERVATION` — reusable structural lesson observed in a live schema; not proof that the schema is optimal.
- `EMPIRICAL_PROJECT_RESULT` — project-local test/result that actually demonstrated a behavior under stated conditions.
- `DESIGN_PROPOSAL` — synthesis that has not yet been experimentally validated.

## 4. Direct reusable GitHub source families

### 4.1 Semantics, pragmatics, grounding, and language

Primary direct sources:

- `semanticatlas`
- `unvtrslr`
- `spm`

Reusable mechanisms:

- source/evidence/interpretation/proposition/adjudication separation;
- currentness, truth, authorship, provenance, consent, and authority as independent axes;
- semantic continuity and explicit supersession rather than newest-label wins;
- observation -> parsed event -> candidate signal -> referent -> semantic hypothesis -> rendering separation;
- uncertainty and provenance as semantic content;
- semantic conservation accounting;
- grounding through observation/action/consequence/shared convention;
- semantics distinct from permission and execution;
- language as one I/O modality rather than the sole internal substrate.

### 4.2 Cognition, world-modeling, developmental learning, and agency

Primary direct sources:

- `noema`
- `abil`

Reusable mechanisms:

- capability-before-mechanism discipline;
- falsifiable mechanism admission;
- world-model revision under uncertainty;
- alternative-hypothesis retention;
- intervention/discriminating-test selection;
- truth, value, and resource allocation kept distinct;
- read-only/shadow learning before write-capable autonomy;
- adaptive regime detection and continual model revision;
- action authority separated from prediction capability.

### 4.3 Memory, chronology, lineage, and persistence

Primary direct sources:

- `deepmemorystorage`
- `temporal`
- `project-lantern`

Reusable mechanisms:

- retrieval != admission;
- historical evidence != current state;
- append-oriented history with correction/supersession rather than destructive rewrite;
- chronology supplies ordering/time, not meaning or authority;
- stable IDs and predecessor/lineage links;
- canonical immutable envelopes with digests;
- source custody distinct from projection/readability;
- current views as derived projections, not authority surfaces;
- replay/reconciliation can propose integration without silently promoting state.

### 4.4 Conation, affective/social inference, sexuality, and personification

Primary direct sources:

- `conations`
- `empathy`
- `sexuality`
- `personification`

Reusable mechanisms only; personal payloads are excluded.

Reusable mechanisms:

- historical motive/desire evidence does not automatically remain current;
- motive, preference, intention, commitment, consent, and action are distinct state types;
- self-appraisal and other-person appraisal are separate;
- models of another mind remain inference and must yield to direct scoped correction about that person's own state;
- reactive social cognition should change attention/response policy before rendering, not merely decorate prose;
- local interaction grammar and reciprocal uptake matter more than lexical surface alone;
- sexuality is a distributed coalition involving body state, attraction, memory, context, consent/boundaries, reward/attachment, and volition rather than one scalar drive;
- agency remains compatible with chosen asymmetry/surrender; consent and desire cannot be inferred from role labels;
- personification is outward expression/presentation, not the storage location of the person.

### 4.5 Perception, sensor admission, action, timing, and embodiment boundaries

Primary direct sources:

- `skeletonkey`
- `abil`
- `selfimage` (generic geometry/provenance/registration lessons only)

Reusable mechanisms:

- `MEASURED`, `DERIVED`, and `INFERRED` evidence classes remain distinct;
- sensor provenance, calibration, quality, uncertainty, timing and source clocks are first-class;
- missing/invalid/saturated/reordered data remain explicit evidence;
- cross-source temporal order is admitted only when uncertainty bounds permit it;
- actuation authority is separate from inference capability;
- geometry/reference registration requires source provenance and rights/validity checks;
- a self/body representation is a model and may have its own confidence, provenance, calibration, and revision history.

### 4.6 Distributed routing, coalitions, communication, and reconciliation

Primary direct sources:

- `chat-communication-bus`
- `build-team-2.0`

Reusable mechanisms:

- routing != authority;
- delivery != incorporation;
- assignment != completion;
- durable canonical source may differ from rebuildable live projection;
- message envelopes carry sender, audience, domain, intent, priority, causal/correlation identity, source refs, content hash, idempotency, expiry, and acknowledgement requirements;
- dead-letter state is explicit rather than silent loss;
- multiple cognitive lenses may operate over one shared state without becoming separate memories/identities;
- synthesis follows collection of attributable perspectives; dissent remains representable;
- task-local coalitions can be transient while sharing one bounded working-state surface.

### 4.7 Safety, failure analysis, qualification, and falsification

Primary direct sources:

- `project-achilles`
- `bugops`
- `hephaestus`
- external-training/workbench source patterns where generic

Reusable mechanisms:

- consequence boundaries rather than blanket inactivity;
- evidence classes must remain explicit;
- a correction is not complete until relevant behavior changes;
- acknowledgment is not closure;
- regression tests must distinguish corrected behavior from the failure;
- qualification is scoped to exact evidence and evaluator contract;
- training-package readiness != runtime/native qualification;
- unknown is preferable to fabricated schema completion;
- source/build/install/activation/qualification are separate lifecycle states.

## 5. Private predecessor abstraction sources

Several private predecessor repositories contain useful generic runtime, cohesion, model/runtime-boundary, canonicalization, digest, authority, recovery, and provider-reconciliation mechanisms but are tied to a particular identity by name or payload.

They may be used only through `PRIVATE_PREDECESSOR_ABSTRACTION`:

1. inspect the mechanism;
2. identify the application-specific assumptions;
3. restate the mechanism in identity-neutral language;
4. independently challenge whether the mechanism belongs in a general brain;
5. cite generic external evidence or generic project sources when available;
6. never copy identity-specific names, autobiography, relationship state, preferences, or current-state records into this repository.

Examples of reusable mechanism classes include:

- active-context minimization;
- hard prerequisite vs contextual dependency distinction;
- currentness and authority dispatch;
- provider evidence envelopes;
- projection reconciliation by exact object/event identity;
- immutable/canonical serialization and digest binding;
- source/runtime/activation/qualification separation;
- restart/recovery without claiming hidden continuity.

## 6. Supabase source families

Production Supabase is a read-only architectural source for this workstream. No database mutation is required to populate the template.

### 6.1 `semantic_atlas`

Observed reusable structures include:

- capture policy with trigger classes and salience thresholds;
- runtime snapshots bound to source branch/ref, commit, manifest/pathset/snapshot digests, validation state, readback SHA, activation readback, and authority scope;
- runtime objects with object type, source path, payload digest, canonical payload;
- capture events carrying source locator/actor, trigger class, salience, representation fidelity, privacy scope, and evidence ceiling;
- capture outcomes separated from capture events and carrying decision payload plus source-control bindings.

Template implication: **capture, representation, admission, materialization, validation, and activation are distinct stages.**

### 6.2 `radar`

Observed reusable structures include:

- runtime nodes with kind, status, capabilities, heartbeat, and metadata;
- subscriptions over domain/intent/priority;
- messages with audience, intent, priority, correlation/causal parent, acknowledgement, expiry, authority reference, source refs, content hash, idempotency key, payload, and projection status;
- delivery events and acknowledgements separate from message creation;
- dead letters with failure stage/code, attempted route, applicability, replay state, and retry count;
- reconciliation and health events;
- explicit dependencies and telemetry.

Template implication: **brain routing should carry typed envelopes, acknowledgements, failure states, and causal/correlation identity rather than treating node-to-node communication as an untyped function call.**

### 6.3 `redworm`

Observed reusable structures include:

- runtime registry with runtime token/status/last-seen state;
- lineage state with generation, lineage key, holder state, and transfer identity;
- append-oriented lineage events;
- succession transfers binding predecessor/successor generations, lineage keys, capsule digest, runtime tokens, transfer status, creation, and consumption.

Template implication: **runtime instance identity, continuity lineage, and state transfer are separate objects and should not be collapsed into one session identifier.**

This is an engineering continuity mechanism, not a metaphysical proof of personal identity.

### 6.4 `build_team_2`

Observed reusable structures include:

- facets with stable lens metadata;
- task snapshots bound by digest;
- attributable perspectives bound to the same task snapshot;
- decisions referencing the snapshot digest;
- append-only memory events carrying source facets, authority class, and provenance;
- role checkpoints and qualifications bound to training-package/source-set digests and evaluator evidence.

Template implication: **multi-perspective cognition can be represented as bounded lenses over shared state, with synthesis and durable memory kept distinct from the individual perspective packets.**

### 6.5 Other production schemas

`bug_ops` contributes failure-lifecycle and operation-receipt patterns. Identity-specific public tables are not source payloads for this template. Their mechanics may be considered privately only when a generic pattern is not already represented elsewhere.

## 7. Proposed brain folder topology

The repository should preserve the original node-oriented concept while making cross-cutting contracts explicit.

```text
brain/
  cognition/
  world_model/
  empathy_social/
  affect_modulation/
  sexuality/
  self_model/
  personification/
  semantics/
  pragmatics/
  language_form/
  chronology/
  memory/
    working/
    episodic/
    semantic/
    procedural/
    deep_archive/
  conation_volition/
  resolver_arbitration/
  perception/
    optics/
    audition_speech_recognition/
    somatic_interoception/
    adaptable_io/
  action/
    kinesis/
    speech_synthesis/
  routing/
  coalitions/
  plasticity/
  homeostasis/
  safety_assurance/

contracts/
  signal/
  evidence/
  provenance/
  authority/
  state/
  lineage/
  timing/
  routing/
  plasticity/

research/
  network_science/
  cognition/
  language_semantics/
  memory/
  affect_social/
  embodiment/
  learning_plasticity/
  safety_validation/

specs/
tests/
```

No hemisphere folders exist.

## 8. Population rule for every brain folder

Each functional folder should eventually contain a compact `README.md` with the same contract:

1. purpose/capability;
2. inputs;
3. outputs;
4. owned state;
5. state it may read but not own;
6. candidate node classes;
7. allowed relation types;
8. activation/gating conditions;
9. plasticity permissions;
10. persistence ceiling;
11. provenance/evidence requirements;
12. interactions with other folders;
13. known failure modes;
14. research support and evidence ceiling;
15. open questions and falsification tests.

A folder is a responsibility boundary, not an anatomical lobe and not necessarily one runtime process.

## 9. Cross-source conflict handling

When two sources disagree:

- preserve both candidate mechanisms;
- identify whether the disagreement is semantic, scope, evidence, implementation, or project-governance specific;
- prefer generic empirical evidence over identity/application-specific precedent;
- prefer mechanisms that survive ablation/adversarial testing over elegant but untested ones;
- do not use recency alone as a tie-breaker;
- record unresolved conflicts as `OPEN_QUESTION` rather than forcing synthesis.

## 10. Population sequence

Recommended implementation sequence after design approval:

1. create the folder skeleton and common README contract;
2. populate evidence/provenance/timing/signal/state contracts first;
3. populate semantics/pragmatics/language;
4. populate cognition/world-model/resolver;
5. populate memory/chronology/lineage;
6. populate conation/affect/empathy/social/sexuality/personification;
7. populate perception/interoception/action/I/O;
8. populate routing/coalitions;
9. populate plasticity/homeostasis;
10. populate safety/assurance and qualification/falsification hooks;
11. build the machine-readable node/relation schema;
12. add cross-folder coalition examples and hostile validation cases;
13. reconcile with parallel HC-1/HC-2/HC-3/runtime PRs without silently overwriting them.

## 11. Acceptance conditions

The first federated population pass is acceptable only if:

- no identity-specific payload appears in the generic template;
- no hemisphere requirement appears;
- every populated functional folder declares capability, state ownership, I/O, gating, persistence, provenance, failure, and evidence ceiling;
- historical/current, evidence/inference, semantics/authority, routing/incorporation, and capability/permission distinctions remain explicit;
- Supabase-derived mechanisms are labeled observations, not universal truth;
- academic claims remain cited separately from internal engineering precedent;
- source conflicts remain visible;
- no repository or database mutation outside the hyperconnectome research branch is performed;
- no merge occurs without separate authority.
