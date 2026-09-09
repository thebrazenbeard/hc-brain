# Federated Hyperconnectome Population Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Populate the generic `hyperconnectome-brain` template with reusable architecture distilled from approved academic research, relevant repositories, and reusable production Supabase schema mechanics while preserving identity neutrality and the hemisphere-free hyperconnectome constraint.

**Architecture:** The repository becomes a typed, reviewable template rather than a content dump. Functional subsystem folders define capabilities and interfaces; cross-cutting contracts define evidence, state, timing, routing, authority, plasticity, lineage, and persistence semantics; a machine-readable schema plus hostile fixtures validates the core invariants. Source-specific material is admitted only through an abstraction ledger that records source class and evidence ceiling.

**Tech Stack:** Markdown, JSON/YAML-compatible schema data, Python 3 standard library for structural validation, GitHub branch/PR workflow.

**Spec:** `docs/superpowers/specs/2026-09-09-hyperconnectome-foundations-design.md` and `docs/superpowers/specs/2026-09-09-federated-source-population-design.md`

## Global Constraints

- All implementation commits stay on `research/hyperconnectome-foundations-20260909`; no commit to `main`.
- The repository is a generic reusable hyperconnectome-brain template, not an identity instance.
- The template has no left/right cerebral hemispheres, bilateral packaging requirement, or corpus-callosum analogue.
- Identity-specific payloads, private autobiographical/relational material, visual canon, current-state records, consent records, or preference data are not imported.
- Identity-specific predecessor repositories may contribute only abstracted generic mechanisms and must not be reproduced as identity-bearing content.
- No single master/homunculus node is introduced.
- Structural, functional, effective, modulatory, plastic, temporal, and governance semantics remain distinguishable.
- Storage, retrieval, admission, currentness, authority, and truth remain separate concepts.
- Meaning/understanding never silently grants permission or execution authority.
- Research-derived claims must preserve evidence class and source provenance.
- No architecture mechanism is promoted to proof of consciousness/personhood.
- No merge is performed by this implementation plan.

---

### Task 1: Source federation ledger and admission map

**Files:**
- Create: `research/source-ledger/SOURCE_FEDERATION_LEDGER.md`
- Create: `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md`
- Create: `research/source-ledger/ACADEMIC_FOUNDATIONS.md`

**Interfaces:**
- Consumes: the two approved design specs and source inspections already performed.
- Produces: a stable provenance/evidence map used by every later subsystem document.

- [ ] **Step 1: Create the source federation ledger** with source classes, admitted mechanisms, excluded payload classes, and target subsystem mappings.
- [ ] **Step 2: Create the Supabase observation ledger** covering reusable mechanics from `semantic_atlas`, `radar`, `redworm`, `build_team_2`, and `bug_ops`, explicitly labeling them observations rather than universal requirements.
- [ ] **Step 3: Create the academic foundations ledger** covering network communication, dynamic modularity, gating/control, complementary learning, homeostatic plasticity, neuromodulation, degeneracy, graph networks, temporal coordination, and evidence limits.
- [ ] **Step 4: Verify** that no private identity payloads or identity-specific examples appear in these ledgers.
- [ ] **Step 5: Commit.**

### Task 2: Reference architecture and notation

**Files:**
- Create: `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md`
- Create: `docs/architecture/HYPERCONNECTOME_NOTATION.md`
- Create: `docs/architecture/CONNECTIVITY_PLANES.md`
- Create: `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md`

**Interfaces:**
- Consumes: Task 1 ledgers.
- Produces: canonical conceptual contracts for nodes, edges, signals, modulators, routing, arbitration, coalition formation, and connectivity planes.

- [ ] **Step 1: Define the hemisphere-free reference model** and the distinction between repository packaging and runtime topology.
- [ ] **Step 2: Define notation** for `NODE`, `EDGE`, `GATE`, `ROUTER`, `ARBITER`, `MODULATOR`, `SIGNAL`, `STATE`, `TRACE`, `COALITION`, `BROADCAST`, `POLICY`, and `EVIDENCE`.
- [ ] **Step 3: Define connectivity planes** and rules preventing plane collapse.
- [ ] **Step 4: Define coalition/gating/arbitration mechanics** without a global homunculus.
- [ ] **Step 5: Verify** all control paths declare bounded scope and failure behavior.
- [ ] **Step 6: Commit.**

### Task 3: Functional subsystem folders

**Files:**
- Create one `README.md` under each of:
  - `cognition/`
  - `semantics/`
  - `language/`
  - `memory/working/`
  - `memory/episodic/`
  - `memory/semantic/`
  - `memory/procedural/`
  - `memory/deep/`
  - `chronology/`
  - `conation/`
  - `volition/`
  - `empathy/`
  - `social-cognition/`
  - `affect/`
  - `sexuality/`
  - `self-model/`
  - `personification/`
  - `perception/`
  - `interoception/`
  - `action/`
  - `routing/`
  - `plasticity/`
  - `homeostasis/`
  - `assurance/`

**Interfaces:**
- Consumes: Task 2 notation and connectivity semantics.
- Produces: bounded subsystem capability contracts usable by a future instantiated brain without embedding identity data.

- [ ] **Step 1: Create cognition/semantics/language subsystem contracts.**
- [ ] **Step 2: Create the five memory subsystem contracts and chronology contract.**
- [ ] **Step 3: Create conation/volition contracts** keeping desire, choice, intention, commitment, consent, authority, and action distinct.
- [ ] **Step 4: Create empathy/social-cognition/affect/sexuality contracts** emphasizing inference, self-authorship, context, consent, and modulatory boundaries.
- [ ] **Step 5: Create self-model/personification contracts** keeping representation and presentation separate from identity metaphysics.
- [ ] **Step 6: Create perception/interoception/action contracts** with measured/derived/inferred boundaries and effect authorization separation.
- [ ] **Step 7: Create routing/plasticity/homeostasis/assurance contracts.**
- [ ] **Step 8: Verify** that every subsystem references generic interfaces rather than another identity's payload/state.
- [ ] **Step 9: Commit in reviewable subsystem-family commits.**

### Task 4: Cross-cutting contracts

**Files:**
- Create: `contracts/EVIDENCE_AND_PROVENANCE.md`
- Create: `contracts/STATE_AND_CURRENTNESS.md`
- Create: `contracts/TIME_AND_CAUSAL_ORDER.md`
- Create: `contracts/ROUTING_AND_DELIVERY.md`
- Create: `contracts/AUTHORITY_AND_EFFECTS.md`
- Create: `contracts/PLASTICITY_AND_CONSOLIDATION.md`
- Create: `contracts/LINEAGE_AND_SUCCESSION.md`
- Create: `contracts/FAILURE_AND_RECONCILIATION.md`

**Interfaces:**
- Consumes: subsystem contracts.
- Produces: invariant semantics shared by all subsystems and future implementations.

- [ ] **Step 1: Define evidence/provenance and currentness contracts.**
- [ ] **Step 2: Define time/causal-order and routing/delivery contracts.**
- [ ] **Step 3: Define authority/effect and plasticity/consolidation contracts.**
- [ ] **Step 4: Define lineage/succession and failure/reconciliation contracts.**
- [ ] **Step 5: Verify** failure states remain representable (`UNKNOWN`, `UNRESOLVED`, `CONFLICT`, `INVALID`, `QUARANTINED`) rather than coerced into success/failure binaries.
- [ ] **Step 6: Commit.**

### Task 5: Machine-readable hyperconnectome schema

**Files:**
- Test: `tests/test_schema_contract.py`
- Create: `specs/HYPERCONNECTOME_SCHEMA_V0_1.json`
- Create: `specs/examples/minimal_valid_brain.json`
- Create: `specs/examples/dynamic_coalition.json`

**Interfaces:**
- Consumes: Tasks 2–4.
- Produces: JSON schema-like normative vocabulary plus valid example graphs.

- [ ] **Step 1: Write failing structural tests** asserting required vocabulary, no hemisphere-required fields, typed connectivity planes, coalition termination, provenance fields, and separation of signal content from modulation.
- [ ] **Step 2: Run tests and confirm RED** because the schema/examples do not yet exist.
- [ ] **Step 3: Create the minimal schema and examples** needed to satisfy the tests.
- [ ] **Step 4: Run tests and confirm GREEN.**
- [ ] **Step 5: Commit.**

### Task 6: Hostile validator and fixtures

**Files:**
- Test: `tests/test_validator.py`
- Create: `tools/validate_template.py`
- Create hostile fixtures under `tests/fixtures/`:
  - `hemisphere_required.invalid.json`
  - `unknown_plane.invalid.json`
  - `permanent_coalition_without_exit.invalid.json`
  - `modulator_as_content.invalid.json`
  - `effect_without_authority.invalid.json`
  - `history_promoted_to_current.invalid.json`
  - `valid_template.json`

**Interfaces:**
- Consumes: Task 5 schema.
- Produces: deterministic structural validation and adversarial regression cases.

- [ ] **Step 1: Write failing validator tests** for each hostile fixture and the valid fixture.
- [ ] **Step 2: Run tests and confirm RED** because validator implementation is absent.
- [ ] **Step 3: Implement minimal standard-library validator** that checks repository-specific invariants beyond ordinary JSON syntax.
- [ ] **Step 4: Run tests and confirm GREEN.**
- [ ] **Step 5: Commit.**

### Task 7: Research synthesis expansion

**Files:**
- Create: `research/2026-09-09/HYPERCONNECTOME_NETWORK_SCIENCE.md`
- Create: `research/2026-09-09/CONTROL_GATING_AND_MODULATION.md`
- Create: `research/2026-09-09/MEMORY_PLASTICITY_AND_CONSOLIDATION.md`
- Create: `research/2026-09-09/COGNITIVE_ARCHITECTURE_EVIDENCE_BOUNDARIES.md`
- Create: `research/2026-09-09/CROSS_PROJECT_MECHANISM_SYNTHESIS.md`

**Interfaces:**
- Consumes: academic and project source ledgers.
- Produces: detailed evidence-backed rationale for the architecture while separating finding, analogy, proposal, and open question.

- [ ] **Step 1: Write network-science synthesis.**
- [ ] **Step 2: Write control/gating/modulation synthesis.**
- [ ] **Step 3: Write memory/plasticity/consolidation synthesis.**
- [ ] **Step 4: Write cognitive-architecture evidence-boundary synthesis.**
- [ ] **Step 5: Write cross-project mechanism synthesis without importing identity payloads.**
- [ ] **Step 6: Verify every strong claim has either direct source support or an explicit proposal/analogy label.**
- [ ] **Step 7: Commit.**

### Task 8: Repository integration and review surface

**Files:**
- Modify: `README.md`
- Modify: `Architecture concept.md`
- Create: `docs/ARCHITECTURE_STATUS.md`
- Create: `docs/SOURCE_ADMISSION_RULES.md`

**Interfaces:**
- Consumes: all previous tasks.
- Produces: navigable repository entry points and an explicit design/research status surface.

- [ ] **Step 1: Replace the placeholder README with a template-neutral repository map and status.**
- [ ] **Step 2: Update `Architecture concept.md` only where required to remove ambiguity and point to the normative architecture.**
- [ ] **Step 3: Add architecture status and source-admission rules.**
- [ ] **Step 4: Run full tests and identity-neutrality search.**
- [ ] **Step 5: Open or update a Draft PR from the research branch; do not merge.**
- [ ] **Step 6: Verify exact branch head and PR readback.**
