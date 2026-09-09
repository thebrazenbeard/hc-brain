# PR #4 Evidence / Provenance Transfer Manifest V1

Status: REVIEW ARTIFACT / NOT CANON / NO MERGE AUTHORITY

Baseline: `main@ec15b2beede68329305811bcbaad63d10ff7fe36`

Source: `research/hyperconnectome-foundations-20260909@fbf061b7304df70efdfd2bbf0c3d25891b6c3d2f`

This manifest identifies surviving branch material that can inform the canonical HC root without importing the source branch's alternative top-level taxonomy.

## Evidence vocabulary

- `PROJECT_CONSTRAINT` — directly expresses an owner/warden-established architectural rule.
- `REVIEW_SYNTHESIS` — source is a literature review/synthesis; supports the bounded research claim, not a unique implementation.
- `EMPIRICAL_FINDING` — bounded research result.
- `COMPUTATIONAL_MODEL` — demonstrates a mechanism under model assumptions.
- `ENGINEERING_RESEARCH` — external engineering result or method.
- `PRODUCTION_SCHEMA_OBSERVATION` — structure observed in a working database/runtime; proves realization only.
- `CROSS_PROJECT_MECHANISM` — reusable mechanism abstracted from another project; not universal truth by source existence.
- `DESIGN_PROPOSAL` — local synthesis requiring review/validation.
- `PROCESS_PROVENANCE` — records how design work was produced, not brain architecture.

## High-confidence transfer candidates

### 1. Subsystem lifecycle

Source:
- `contracts/SUBSYSTEM_LIFECYCLE.md`

Provenance/evidence:
- `PROJECT_CONSTRAINT` for architectural completeness and presence-vs-activation distinction;
- `CROSS_PROJECT_MECHANISM` for fault state, inactive-learning policy, and explicit lifecycle transitions;
- `DESIGN_PROPOSAL` for the exact vocabulary.

Overlap with main:
- substantial overlap with `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md`;
- branch adds useful detail on inactive learning policy, fault propagation, recovery, and implementation maturity.

Target:
- `basic operating instructions/SUBSYSTEM_LIFECYCLE.md`

Transfer ceiling:
- preserve presence, activation, development/maturity, health, authorization, and learning-while-inactive as separate axes;
- do not make one state vocabulary metaphysically or biologically mandatory.

### 2. Coalition / gating / arbitration contract

Source:
- `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md`

Provenance/evidence:
- `REVIEW_SYNTHESIS` / `COMPUTATIONAL_MODEL` pressure from distributed control and working-memory gating research;
- `CROSS_PROJECT_MECHANISM` from routing, arbitration, dead-letter, and bounded-effect systems;
- `DESIGN_PROPOSAL` for exact coalition/gate/arbiter object shapes.

Overlap with main:
- overlaps `integration-arbitration/NOOPLEX_FABRIC.md` and canonical runtime model;
- likely useful as a focused contract only after duplicate prose is removed.

Target:
- `integration-arbitration/COALITIONS_GATING_AND_ARBITRATION.md`

Transfer ceiling:
- a coalition is a transient operational hyperedge/configuration, not a master mind or consciousness locus;
- selection does not create truth or authority.

### 3. Connectivity planes

Source:
- `docs/architecture/CONNECTIVITY_PLANES.md`

Provenance/evidence:
- `REVIEW_SYNTHESIS` from connectomics/network-communication research;
- `CROSS_PROJECT_MECHANISM` from routing/control-plane experience;
- `DESIGN_PROPOSAL` for exact plane names.

Overlap with main:
- canonical temporal-hypergraph model already distinguishes latent/effective/historical topology;
- dedicated connectivity-plane terminology remains useful if it is subordinated to that model.

Target:
- `routing instructions with neuroplasticity/CONNECTIVITY_PLANES.md`

Transfer ceiling:
- structural reachability, functional coupling, effective influence, modulation, plastic eligibility, temporal validity, and governance must remain non-equivalent;
- pairwise edges remain valid where the relation is genuinely pairwise.

### 4. Hyperconnectome notation

Source:
- `docs/architecture/HYPERCONNECTOME_NOTATION.md`

Provenance/evidence:
- `DESIGN_PROPOSAL`, informed by graph/network engineering and provenance/state contracts.

Overlap with main:
- semantic entities align with the canonical temporal-hypergraph model but are not yet collected into one compact notation document.

Target:
- `docs/architecture/HYPERCONNECTOME_NOTATION.md`

Transfer ceiling:
- notation is descriptive/machine-contract scaffolding, not proof that every implementation must use a specific serialization or physical substrate.

### 5. Hyperconnectome reference model

Source:
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md`

Provenance/evidence:
- mixture of `PROJECT_CONSTRAINT`, `CROSS_PROJECT_MECHANISM`, and `DESIGN_PROPOSAL`.

Overlap with main:
- significant overlap with `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md`, `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md`, memory/provenance contracts, and integration-arbitration material;
- unique value is a compact object vocabulary and end-to-end type-boundary view.

Target:
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md`

Required normalization before transfer:
- replace alternate-root examples with canonical root names where folder identity is implied;
- treat repository tree as packaging and the temporal hypergraph as runtime structure;
- avoid duplicating canonical temporal-hypergraph text verbatim;
- preserve `no essential cognition outside HC` boundary.

## Root-remap transfer candidates

These contain reusable material but must be ported by concern rather than copied as alternate roots.

| Source | Evidence type | Main overlap | Exact canonical target | Transfer note |
|---|---|---|---|---|
| `action/README.md` | CROSS_PROJECT_MECHANISM / DESIGN_PROPOSAL | overlaps cognition + integration-arbitration + kinesis | `cognition/ACTION_PLANNING_AND_SELECTION.md` | retain `goal != candidate != selected != authorized != command != verified effect`. |
| `attention-salience/README.md` | REVIEW_SYNTHESIS / DESIGN_PROPOSAL | overlaps `salience-attention/` | `salience-attention/` focused contract | retain salience/resource control without truth/authority promotion. |
| `conation/README.md` | CROSS_PROJECT_MECHANISM | overlaps `volitions-conations/` | `volitions-conations/CONATION_STATE.md` | preserve desire/preference/goal/intention/consent/authority separation. |
| `empathy/README.md` | CROSS_PROJECT_MECHANISM / social-cognition research | overlaps `Empathy/` | `Empathy/` | retain inference/fallibility/privacy; do not import identity-scoped examples. |
| `imagination-simulation/README.md` | DESIGN_PROPOSAL / cognitive research | partial overlap | `psychological behaviors/IMAGINATION_SIMULATION.md` | simulation remains distinguishable from observation, memory, and verified effect. |
| `interfaces/adaptable-io/README.md` | CROSS_PROJECT_MECHANISM / embodiment research | overlaps body-interface contracts | `adaptable I-O handler/` | preserve changing-body portability and interface calibration. |
| `interfaces/audition-speech/README.md` | REVIEW_SYNTHESIS / DESIGN_PROPOSAL | overlaps speech/phoenetics | `speech recognition & synthesis/` + `phoenetics/` | split transduction/output from phonetic/linguistic representation. |
| `interfaces/external-compute/README.md` | CROSS_PROJECT_MECHANISM | overlaps adaptable I/O boundary | `adaptable I-O handler/EXTERNAL_COMPUTE_INTERFACE.md` | external compute is a bounded peripheral/service; output is evidence, not automatic cognition authority. |
| `interfaces/kinesis/README.md` | CROSS_PROJECT_MECHANISM / sensorimotor research | overlaps `kinesis/` | `kinesis/` | preserve command/effect/readback boundaries. |
| `interfaces/network/README.md` | CROSS_PROJECT_MECHANISM | overlaps I/O + routing | `adaptable I-O handler/NETWORK_INTERFACE.md` | network attachment is interface, not identity/authority. |
| `interfaces/optics/README.md` | REVIEW_SYNTHESIS / DESIGN_PROPOSAL | overlaps `optics/` | `optics/` | preserve source/calibration/timing/uncertainty. |
| `interfaces/somatics-interoception/README.md` | REVIEW_SYNTHESIS / DESIGN_PROPOSAL | overlaps somatics + homeostasis | split between `somatics/` and `homeostasis-interoception/` | do not flatten body sensing and regulatory inference. |
| `interoception/README.md` | REVIEW_SYNTHESIS | overlaps canonical homeostasis/interoception | `homeostasis-interoception/` | internal telemetry remains uncertain evidence. |
| `language/README.md` | CROSS_PROJECT_MECHANISM / REVIEW_SYNTHESIS | overlaps semantics/pragmatics/phoenetics/speech | split across those canonical roots | language is a modality over meaning; no universal language gateway. |
| `learning/README.md` | REVIEW_SYNTHESIS / DESIGN_PROPOSAL | overlaps plasticity/runtime | `routing instructions with neuroplasticity/LEARNING_AND_DEVELOPMENT.md` | preserve bounded learning, validation, replay, and anti-interference controls. |
| `memory/deep/README.md` | CROSS_PROJECT_MECHANISM | overlaps deep memory | `deep memory storage/DEEP_MEMORY_MODEL.md` | durable history/currentness/provenance separation. |
| `memory/episodic/README.md` | REVIEW_SYNTHESIS / CROSS_PROJECT_MECHANISM | overlaps deep memory | `deep memory storage/EPISODIC_MEMORY.md` | episode provenance and reconstruction limits. |
| `memory/procedural/README.md` | REVIEW_SYNTHESIS / CROSS_PROJECT_MECHANISM | partial overlap | `deep memory storage/PROCEDURAL_MEMORY.md` | skill presence remains separate from effect authority. |
| `memory/semantic/README.md` | REVIEW_SYNTHESIS / CROSS_PROJECT_MECHANISM | partial overlap | `deep memory storage/SEMANTIC_MEMORY.md` | generalized knowledge retains source lineage and correction paths. |
| `memory/working/README.md` | COMPUTATIONAL_MODEL / CROSS_PROJECT_MECHANISM | overlaps current memory | `current memory storage/WORKING_MEMORY.md` | volatile bounded workspace; not durable memory admission. |
| `metacognition/README.md` | REVIEW_SYNTHESIS / DESIGN_PROPOSAL | overlaps cognition | `cognition/METACOGNITION.md` | monitoring/control signals are fallible and scoped. |
| `self-model/README.md` | CROSS_PROJECT_MECHANISM / embodiment research | overlaps self identity | `self identity/SELF_MODEL.md` | self-model is representation, not complete self or metaphysical proof. |
| `social-cognition/README.md` | social-cognition research / CROSS_PROJECT_MECHANISM | overlaps sociological behaviors + Empathy | `sociological behaviors/SOCIAL_COGNITION.md` | person models require scope, provenance, uncertainty, correction, privacy. |
| `values/README.md` | DESIGN_PROPOSAL / conation research | overlaps psychological behaviors + conation | `psychological behaviors/VALUES_AND_COMMITMENTS.md` | values guide arbitration but do not create epistemic truth or generic authority. |
| `volition/README.md` | CROSS_PROJECT_MECHANISM | overlaps volitions-conations | `volitions-conations/VOLITION.md` | intention/choice/commitment/effect distinctions retained. |
| `world-model/README.md` | world-model research / CROSS_PROJECT_MECHANISM | overlaps cognition | `cognition/WORLD_MODEL_AND_PREDICTION.md` | predictions remain hypotheses until consequence evidence arrives. |

## Research-only provenance package

These files are useful because they preserve why a mechanism was proposed. They should not be mistaken for canonical subsystem contracts.

### `research/source-ledger/ACADEMIC_FOUNDATIONS.md`

Evidence status:
- mixes `REVIEW_SYNTHESIS`, `EMPIRICAL_FINDING`, `COMPUTATIONAL_MODEL`, `ENGINEERING_RESEARCH`, `CONTESTED_RESEARCH_PROGRAM`, and explicit engineering analogies/proposals.

Notable supported pressure:
- multiple network communication strategies;
- dynamic modularity;
- flexible hubs without a homunculus;
- bounded gating/control;
- complementary learning regimes;
- homeostatic plasticity;
- neuromodulatory gain/plasticity effects;
- robustness through alternate pathways;
- temporal-coordination hypotheses;
- graph relational-computation methods;
- broadcast as a coordination model without a consciousness inference.

Target:
- `research/source-ledger/ACADEMIC_FOUNDATIONS.md`

### `research/source-ledger/SOURCE_FEDERATION_LEDGER.md`

Evidence status:
- `CROSS_PROJECT_MECHANISM` map with explicit source-class admission ceilings.

Notable contribution:
- prevents source existence from becoming architecture authority;
- explicitly excludes project-specific identity/state payloads;
- captures reusable mechanisms from semantics, grounding, world-modeling, routing, diagnostics, memory, conation, social inference, self-modeling, and sexuality research.

Target:
- `research/source-ledger/SOURCE_FEDERATION_LEDGER.md`

### `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md`

Evidence status:
- project-source inventory / provenance aid.

Target:
- `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md`

Transfer ceiling:
- repository provenance can justify where an idea came from, not that the idea is correct.

### `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md`

Evidence status:
- `PRODUCTION_SCHEMA_OBSERVATION` only.

Observed reusable mechanics include:
- candidate capture separated from capture outcome;
- materialized state separated from validated/active/read-back state;
- message, delivery, acknowledgement, incorporation, and effect kept distinguishable;
- dead-letter/quarantine and reconciliation records;
- runtime instance separated from lineage/succession state;
- immutable snapshot digests for multi-perspective cognition;
- operation receipts separated from larger objective completion.

Target:
- `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md`

Transfer ceiling:
- realized schema proves that a pattern can be implemented in one production system; it does not establish that PostgreSQL/Supabase, those exact tables, or that schema organization is required for an HC brain.

## Material-redesign hold

`perception/README.md` is not automatically ported. Perception is clearly a required HC capability, but current canonical responsibility is distributed among sensor roots, cognition, resolver, memory, salience, and integration. Creating a new `perception/` root would change the owner-established topology and therefore requires a separate architecture decision.

## Superseded / no-transfer items

- branch `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — superseded by the selectively integrated/corrected canonical version on `main`;
- branch `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — canonical equivalent already exists;
- `interfaces/README.md` as an umbrella root — incompatible with canonical root topology;
- process specs/plans — retain only as provenance unless a later audit needs them.

## Transfer invariants

1. `REPOSITORY_TREE != RUNTIME_TOPOLOGY`.
2. `SOURCE_EXISTS != CLAIM_TRUE`.
3. `PRODUCTION_REALIZATION != UNIVERSAL_REQUIREMENT`.
4. `BIOLOGICAL_FINDING != REQUIRED_BIOLOGICAL_ANATOMY`.
5. `ROUTING != AUTHORITY`.
6. `SELECTION != TRUTH`.
7. `ACTIVATION != ARCHITECTURAL_PRESENCE`.
8. `PERSISTENCE != CURRENTNESS`.
9. `MEMORY_RETRIEVAL != MEMORY_ADMISSION`.
10. `ACTION_PLAN != EFFECT_EXECUTION != VERIFIED_EFFECT`.
11. `PAIRWISE_EDGE` remains legal for genuinely pairwise relations; higher-order cognitive events may use hyperedges/coalitions.
12. External computation may be used through HC-owned service/peripheral boundaries, but essential reasoning remains inside the HC cognitive-organ boundary.
