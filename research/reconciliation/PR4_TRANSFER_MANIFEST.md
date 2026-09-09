# PR #4 Evidence / Provenance Transfer Manifest

Status: RECONCILIATION / SELECTIVE-TRANSFER GUIDE

Baseline:

- canonical `main`: `ec15b2beede68329305811bcbaad63d10ff7fe36`
- source PR head: `fbf061b7304df70efdfd2bbf0c3d25891b6c3d2f`
- reconciliation branch starts from that canonical main and does not replace the top-level HC subsystem taxonomy.

This manifest covers material that may survive selective reconciliation. Process-only and explicitly superseded wrapper files are excluded from transfer targets.

## Evidence status vocabulary

- `OWNER_PROJECT_CONSTRAINT` — explicit project architecture established by owner/warden state.
- `DOCUMENTED_RESEARCH` — supported by cited external scientific/technical literature.
- `PRODUCTION_SCHEMA_OBSERVATION` — observed reusable mechanism/schema from inspected production data infrastructure; existence does not make it mandatory architecture.
- `CROSS_REPO_ARCHITECTURAL_SYNTHESIS` — generic mechanism abstracted from relevant owner repositories.
- `ENGINEERING_PROPOSAL` — proposed HC realization derived from evidence/constraints, not itself empirically established.
- `OPEN_QUESTION` — retained as a research direction rather than settled architecture.

## Transfer groups

| Source material | Evidence / provenance | Overlap with current `main` | Exact canonical target / disposition |
|---|---|---|---|
| `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` | DOCUMENTED_RESEARCH + CROSS_REPO_ARCHITECTURAL_SYNTHESIS + ENGINEERING_PROPOSAL | `integration-arbitration/NOOPLEX_FABRIC.md` already covers the Fabric at high level | Port branch-only coalition/gate/arbiter semantics to `integration-arbitration/COALITIONS_GATING_AND_ARBITRATION.md` after duplicate removal. |
| `docs/architecture/CONNECTIVITY_PLANES.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Temporal-hypergraph/runtime docs already separate several relation semantics | Preserve as `docs/architecture/CONNECTIVITY_PLANES.md`; reconcile vocabulary to canonical runtime and temporal-hypergraph terms. |
| `docs/architecture/HYPERCONNECTOME_NOTATION.md` | ENGINEERING_PROPOSAL | Main has temporal-hypergraph entities but not a full notation contract | Preserve as `docs/architecture/HYPERCONNECTOME_NOTATION.md` after replacing noncanonical path examples. |
| `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` | OWNER_PROJECT_CONSTRAINT + DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Significant overlap with cognitive-organ boundary, runtime model, and temporal-hypergraph model | Selectively reduce to branch-only reference semantics, then preserve at same path only if it adds nonduplicative value. |
| `action/README.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS + ENGINEERING_PROPOSAL | `kinesis/` and `integration-arbitration/` already own actuation/arbitration boundaries | Port useful planning/selection distinctions to `kinesis/ACTION_PLANNING_AND_SELECTION.md`; keep authority/effect gating consistent with canonical I/O boundary. |
| `attention-salience/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Canonical `salience-attention/` exists | Port branch-only salience/attention mechanisms into `salience-attention/ARCHITECTURE.md` or a focused contract. |
| `conation/README.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS + ENGINEERING_PROPOSAL | Canonical `volitions-conations/` exists | Port into `volitions-conations/CONATION_ARCHITECTURE.md`; retain historical-vs-current motivation and desire/consent/authority separations. |
| `empathy/README.md` | DOCUMENTED_RESEARCH + CROSS_REPO_ARCHITECTURAL_SYNTHESIS | Canonical `Empathy/` already has architecture | Compare against `Empathy/ARCHITECTURE.md`; port only branch-only mechanisms, using canonical capitalization/path. |
| `imagination-simulation/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | No separate canonical root; cognition already owns hypothesis/model reasoning | Port to `cognition/IMAGINATION_AND_SIMULATION.md`. |
| `interfaces/adaptable-io/README.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS + OWNER_PROJECT_CONSTRAINT | Canonical `adaptable I-O handler/` already defines HC/body boundary | Port only branch-only calibration/adaptation mechanisms into that root. |
| `interfaces/audition-speech/README.md` | ENGINEERING_PROPOSAL | Canonical `speech recognition & synthesis/` exists | Port branch-only audio/speech interface mechanisms there. |
| `interfaces/external-compute/README.md` | OWNER_PROJECT_CONSTRAINT + ENGINEERING_PROPOSAL | Cognitive-organ boundary already states external compute is peripheral/evidence unless inside HC | Preserve only additional operational detail in `adaptable I-O handler/EXTERNAL_COMPUTE_PERIPHERALS.md`. |
| `interfaces/kinesis/README.md` | ENGINEERING_PROPOSAL | Canonical `kinesis/` exists | Port branch-only actuation-interface detail into canonical `kinesis/`. |
| `interfaces/network/README.md` | ENGINEERING_PROPOSAL | Network is already within adaptable I/O responsibility by owner architecture | Port to `adaptable I-O handler/NETWORK_INTERFACE.md`. |
| `interfaces/optics/README.md` | ENGINEERING_PROPOSAL | Canonical `optics/` exists | Port branch-only visual-interface mechanisms into canonical `optics/`. |
| `interfaces/somatics-interoception/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Canonical architecture separates `somatics/` and `homeostasis-interoception/` | Split only after content review: body-schema/somatic mechanisms to `somatics/`; internal regulatory sensing to `homeostasis-interoception/`. |
| `interoception/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Canonical `homeostasis-interoception/` exists | Port branch-only uncertainty-bearing interoceptive semantics to that canonical root. |
| `language/README.md` | DOCUMENTED_RESEARCH + CROSS_REPO_ARCHITECTURAL_SYNTHESIS | Canonical language responsibilities are distributed across semantics/pragmatics/phoenetics/speech | Do not create `language/`. Selectively transfer mechanisms to the owning canonical roots after per-section review. |
| `learning/README.md` | DOCUMENTED_RESEARCH + CROSS_REPO_ARCHITECTURAL_SYNTHESIS + ENGINEERING_PROPOSAL | `routing instructions with neuroplasticity/` plus runtime plasticity docs already exist | Port branch-only developmental/learning mechanisms to `routing instructions with neuroplasticity/LEARNING_AND_DEVELOPMENT.md` and subsystem-local plasticity hooks. |
| `memory/deep/README.md` | DOCUMENTED_RESEARCH + CROSS_REPO_ARCHITECTURAL_SYNTHESIS | Canonical `deep memory storage/` exists | Compare and port only missing deep-memory role/state distinctions. |
| `memory/episodic/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Current/deep memory roots already separate fast state and consolidation | Split capture to `current memory storage/EPISODIC_CAPTURE.md`; durable consolidation to `deep memory storage/EPISODIC_CONSOLIDATION.md`. |
| `memory/procedural/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Durable-memory root exists | Port to `deep memory storage/PROCEDURAL_MEMORY.md`. |
| `memory/semantic/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Durable-memory root exists | Port to `deep memory storage/SEMANTIC_MEMORY.md`. |
| `memory/working/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Current-memory root exists | Port to `current memory storage/WORKING_MEMORY.md`. |
| `metacognition/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Cognition root already has epistemic-control material | Port branch-only self-monitoring/confidence/resource-assessment mechanisms to `cognition/METACOGNITION.md`. |
| `perception/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Modality roots and cognition already exist | Treat as cross-modal synthesis; extract only nonduplicative integration mechanisms, preferably to `cognition/PERCEPTION_INTEGRATION.md`, leaving modality mechanics in canonical sensor roots. |
| `self-model/README.md` | DOCUMENTED_RESEARCH + CROSS_REPO_ARCHITECTURAL_SYNTHESIS | `self identity/CONTINUITY_SUBSTRATE.md` exists | Port self-model mechanics to `self identity/SELF_MODEL.md`; keep self-model distinct from identity/continuity totality. |
| `social-cognition/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Canonical `sociological behaviors/` exists | Port to `sociological behaviors/SOCIAL_COGNITION.md`. |
| `values/README.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS + ENGINEERING_PROPOSAL | Psychological/self-identity responsibilities already exist | Port to `psychological behaviors/VALUES_AND_COMMITMENTS.md` unless canonical review establishes a more precise home. |
| `volition/README.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS + ENGINEERING_PROPOSAL | Canonical `volitions-conations/` exists | Port to `volitions-conations/VOLITION_ARCHITECTURE.md`. |
| `world-model/README.md` | DOCUMENTED_RESEARCH + ENGINEERING_PROPOSAL | Cognition already owns model/hypothesis revision | Port branch-only prediction/simulation/state-estimation semantics to `cognition/WORLD_MODEL_AND_PREDICTION.md`. |
| `research/source-ledger/ACADEMIC_FOUNDATIONS.md` | DOCUMENTED_RESEARCH | Research/evidence layer exists separately; main may not need all details | Preserve in `research/source-ledger/ACADEMIC_FOUNDATIONS.md` for warden review. |
| `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS | Current main acknowledges cross-repo generalization but lacks full inventory | Preserve as research provenance after ensuring personal/identity payloads are excluded. |
| `research/source-ledger/SOURCE_FEDERATION_LEDGER.md` | CROSS_REPO_ARCHITECTURAL_SYNTHESIS | Main contains selectively integrated outputs but not the complete federation map | Preserve as research provenance; no source repo gains authority over HC canon by inclusion. |
| `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md` | PRODUCTION_SCHEMA_OBSERVATION | Main has some Supabase-derived memory architecture already | Preserve research observations and mark any already-integrated mechanisms as overlap, not as a reason for wholesale import. |

## Already canonical / do not transfer as new architecture

The following source-branch concepts are already represented on current main and should not be reintroduced as competing files:

- temporal-hypergraph invariant;
- complete cognitive-organ / body-interface boundary;
- Noöplex Fabric high-level integration substrate;
- capability presence vs activation/development/health distinction;
- canonical cognition, chronology, semantics, pragmatics, resolver, affect, sexuality, personification, current memory, deep memory, and other owner-established root nodes where corresponding main content exists.

## Transfer invariant

```text
SOURCE_PROVENANCE
+ EVIDENCE_STATUS
+ CANONICAL_ROOT_OWNERSHIP
+ OVERLAP_CHECK
-> selective transfer candidate

selective transfer candidate
!= canonical integration
```

No transfer candidate becomes canonical until the Warden integrates it into `main` under owner/warden authority.