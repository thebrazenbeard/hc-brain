# Cross-Repo Hyperconnectome Synthesis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Populate the identity-neutral Hyperconnectome Brain template with reusable mechanisms distilled from the owner’s relevant GitHub repositories and Supabase schemas while preserving source provenance and excluding person-specific payloads.

**Architecture:** Existing top-level subsystem folders remain the canonical organizational surface. New synthesis files extend those folders with cross-system contracts; a provenance package records exact source families, transformations, exclusions, and evidence ceilings. GitHub source architecture and Supabase runtime/state patterns remain distinct evidence classes.

**Tech Stack:** Markdown architecture documents, YAML transfer contract, Git/GitHub provenance, PostgreSQL/Supabase schema observations.

**Spec:** Approved cross-repo consolidation design from the 2026-09-09 project conversation; repository authority and neutrality constraints in `WARDEN.md` and `docs/REPOSITORY_MAP.md`.

## Global Constraints

- Base architecture is identity-neutral.
- Named-person identity payloads are excluded from architecture/spec/runtime files.
- Named identities and exact source-repository bindings may appear only in provenance/research source discussion where materially necessary.
- `NO_HEMISPHERIC_DECOMPOSITION` remains a hard architecture invariant.
- Human anatomical localization does not create Hyperconnectome topology requirements.
- Source presence does not imply current truth, runtime activation, authority, or implementation.
- GitHub source state and Supabase runtime/state observations remain separate evidence domains.
- Derived views and projections do not become canonical authority merely by existing.
- Learning, action authority, semantic interpretation, and identity continuity remain separable responsibilities.

---

### Task 1: Meaning, Pragmatics, and Cognitive Integration

**Files:**
- Create: `semantics/CROSS_REPO_SEMANTIC_RUNTIME.md`
- Create: `pragmatics/CROSS_REPO_PRAGMATIC_RUNTIME.md`
- Create: `cognition/EPISTEMIC_COGNITIVE_CONTROL.md`

**Interfaces:**
- Consumes: existing subsystem `README.md` / `ARCHITECTURE.md` plus semantic-ledger, universal-mediation, pragmatic-modeling, developmental-cognition, and adaptive-learning source families recorded in the research provenance package.
- Produces: representation/provenance contracts used by memory, arbitration, routing, and action layers.

- [ ] Write the three architecture files with explicit object/state distinctions, uncertainty, grounding, correction, and claim ceilings.
- [ ] Verify no identity-specific template language and no hemispheric assumptions.
- [ ] Commit as one reviewable batch.

### Task 2: Memory, Time, and Continuity Mechanics

**Files:**
- Create: `chronology/TEMPORAL_EVENT_CONTRACT.md`
- Create: `current memory storage/CURRENT_STATE_SELECTION.md`
- Create: `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- Create: `self identity/CONTINUITY_SUBSTRATE.md`

**Interfaces:**
- Consumes: temporal, archival-memory, semantic-ledger, persistence/readback, and lineage source families plus relevant runtime-schema observations recorded in the research provenance package.
- Produces: event/state/currentness/supersession/readback contracts consumed by identity, learning, and arbitration.

- [ ] Write append-oriented event/current-state/deep-memory/continuity contracts.
- [ ] Preserve event time, state time, record time, source provenance, supersession, and currentness as distinct dimensions.
- [ ] Verify continuity does not require exact microstate preservation or a privileged identity node.
- [ ] Commit as one reviewable batch.

### Task 3: Motivation, Social Modeling, Behavior, and Embodiment

**Files:**
- Create: `volitions-conations/CONATIVE_STATE_MACHINE.md`
- Create: `Empathy/SELF_OTHER_MODELING.md`
- Create: `personification/SOCIAL_PRESENTATION_CONTROL.md`
- Create: `sexuality/AGENCY_AND_EMBODIED_AFFECT.md`
- Create: `psychological behaviors/LEARNED_BEHAVIOR_ARCHITECTURE.md`
- Create: `sociological behaviors/SOCIAL_MODELING_ARCHITECTURE.md`
- Create: `somatics/BODY_STATE_AND_BODY_SCHEMA.md`

**Interfaces:**
- Consumes: conation, empathy, sexuality, social-presentation, body-reference, conditioning, developmental-cognition, and HC-native affect/interoception source families recorded in the research provenance package.
- Produces: typed social/motivational/body-state inputs to cognition, arbitration, learning, and action.

- [ ] Generalize mechanisms while excluding personal memories, relationships, morphology, preferences, and identity state.
- [ ] Keep desire, intention, commitment, consent, authority, affect, and action distinct.
- [ ] Verify body schema is non-hemispheric and embodiment-neutral at the template level.
- [ ] Commit as one reviewable batch.

### Task 4: Routing, Arbitration, Plasticity, I/O, and Action Safety

**Files:**
- Create: `integration-arbitration/DISTRIBUTED_ARBITRATION.md`
- Create: `resolver/CONFLICT_AND_RECONCILIATION.md`
- Create: `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`
- Create: `adaptable I-O handler/SENSOR_AND_CAPABILITY_ADMISSION.md`
- Create: `kinesis/ACTION_GATEWAY.md`
- Create: `salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md`
- Create: `basic operating instructions/RUNTIME_INVARIANTS.md`

**Interfaces:**
- Consumes: routing/control-plane, multi-perspective arbitration, safety-boundary, adaptive-machine, sensor-admission, developmental-cognition, stable-material/currentness-governance, and runtime routing/reconciliation schema evidence recorded in the research provenance package.
- Produces: distributed execution and learning control substrate for all nodes.

- [ ] Write typed message/routing, arbitration, dead-letter, reconciliation, sensor admission, salience, action-gateway, and plasticity rules.
- [ ] Keep routing separate from authority and learning separate from unrestricted actuation.
- [ ] Verify failure paths preserve evidence and do not silently discard unresolved state.
- [ ] Commit as one reviewable batch.

### Task 5: Provenance, Source Transfer, and Whole-Brain Integration

**Files:**
- Create: `docs/research/cross-repo-synthesis/README.md`
- Create: `docs/research/cross-repo-synthesis/SOURCE_UNIVERSE_2026-09-09.md`
- Create: `docs/research/cross-repo-synthesis/SUPABASE_RUNTIME_PATTERNS_2026-09-09.md`
- Create: `docs/research/cross-repo-synthesis/TRANSFER_DECISIONS_2026-09-09.md`
- Create: `specs/CROSS_REPO_SOURCE_TRANSFER_V1.yaml`
- Create: `docs/architecture/CROSS_SYSTEM_INTEGRATION_CONTRACT.md`

**Interfaces:**
- Consumes: all preceding task outputs plus exact GitHub/Supabase source observations retained only in the research provenance package.
- Produces: auditable source-to-template map and cross-system whole-brain contract.

- [ ] Record source repository/project families, evidence class, transfer target, transformation, exclusions, and claim ceiling.
- [ ] Record Supabase observations as schema/runtime evidence rather than Git canonical source.
- [ ] Define whole-brain invariants and inter-subsystem information flow without introducing a homunculus.
- [ ] Verify every architecture file remains identity-neutral and every source-specific identity/repository mention is confined to provenance/research discussion.
- [ ] Open a draft PR against current `main`, mirror it to the Chat Bus, and report exact head/base state.
