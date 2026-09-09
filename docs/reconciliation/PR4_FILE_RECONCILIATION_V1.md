# PR #4 File Reconciliation V1

Status: REVIEW ARTIFACT / NOT CANON / NO MERGE AUTHORITY

Source under review:

- canonical baseline: `main@ec15b2beede68329305811bcbaad63d10ff7fe36`
- source branch: `research/hyperconnectome-foundations-20260909@fbf061b7304df70efdfd2bbf0c3d25891b6c3d2f`
- source PR: `#4`

Purpose: classify every PR #4 changed file against the owner-established canonical root architecture. This document does not rename top-level subsystem folders and does not promote branch content to canon.

Classification vocabulary:

- `SAFE_SELECTIVE_INTEGRATION`
- `NEEDS_ROOT_REMAP`
- `DUPLICATES_MAIN`
- `RESEARCH_ONLY`
- `PROCESS_ONLY`
- `MATERIAL_REDESIGN`
- `REJECT / SUPERSEDED`

## File-by-file disposition

| PR #4 source path | Classification | Canonical target / disposition | Notes |
|---|---|---|---|
| `action/README.md` | NEEDS_ROOT_REMAP | `cognition/ACTION_PLANNING_AND_SELECTION.md` | Useful plan/selection/effect-boundary distinctions; do not create `action/` root. |
| `affect/README.md` | DUPLICATES_MAIN | no direct port | Current `affect/ARCHITECTURE.md` already carries the distributed affect/modulation model; harvest only genuinely unique failure tests if later found. |
| `attention-salience/README.md` | NEEDS_ROOT_REMAP | `salience-attention/` | Alternate root spelling/order; merge only unique control/failure semantics into canonical subsystem. |
| `chronology/README.md` | DUPLICATES_MAIN | no direct port | Canonical `chronology/ARCHITECTURE.md` and `TEMPORAL_EVENT_CONTRACT.md` are already more integrated. |
| `cognition/README.md` | DUPLICATES_MAIN | no direct port | Canonical cognition architecture plus epistemic control already exists. |
| `conation/README.md` | NEEDS_ROOT_REMAP | `volitions-conations/CONATION_STATE.md` | Preserve desire/preference/goal/intention/consent/authority distinctions without creating a new root. |
| `contracts/SUBSYSTEM_LIFECYCLE.md` | SAFE_SELECTIVE_INTEGRATION | `basic operating instructions/SUBSYSTEM_LIFECYCLE.md` | Complements existing capability-presence/activation model with inactive-learning policy, fault propagation, and maturity separation. |
| `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` | SAFE_SELECTIVE_INTEGRATION | `integration-arbitration/COALITIONS_GATING_AND_ARBITRATION.md` | Fits canonical Noöplex Fabric/integration responsibility; review for overlap before port. |
| `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` | DUPLICATES_MAIN | no direct port | Canonical boundary already exists on `main`. |
| `docs/architecture/CONNECTIVITY_PLANES.md` | SAFE_SELECTIVE_INTEGRATION | `routing instructions with neuroplasticity/CONNECTIVITY_PLANES.md` | Typed connectivity belongs under canonical routing/plasticity root. |
| `docs/architecture/HYPERCONNECTOME_NOTATION.md` | SAFE_SELECTIVE_INTEGRATION | `docs/architecture/HYPERCONNECTOME_NOTATION.md` | Useful generic notation; no root-taxonomy replacement required. |
| `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` | SAFE_SELECTIVE_INTEGRATION | `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` | Useful runtime reference model if canonical folder references are normalized before integration. |
| `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` | REJECT / SUPERSEDED | no port | Temporal-hypergraph correction was selectively integrated and corrected on current `main`; branch copy is no longer authoritative. |
| `docs/superpowers/plans/2026-09-09-complete-cognitive-organ-addendum.md` | PROCESS_ONLY | retain as branch provenance only | Planning history is not brain architecture. |
| `docs/superpowers/plans/2026-09-09-federated-hyperconnectome-population.md` | PROCESS_ONLY | retain as branch provenance only | Planning history is not brain architecture. |
| `docs/superpowers/specs/2026-09-09-complete-cognitive-organ-correction.md` | PROCESS_ONLY | retain as branch provenance only | Design-process evidence; integrate resulting contracts, not the process artifact by default. |
| `docs/superpowers/specs/2026-09-09-federated-source-population-design.md` | PROCESS_ONLY | retain as branch provenance only | Design-process evidence. |
| `docs/superpowers/specs/2026-09-09-hyperconnectome-foundations-design.md` | PROCESS_ONLY | retain as branch provenance only | Design-process evidence. |
| `empathy/README.md` | NEEDS_ROOT_REMAP | `Empathy/` | Canonical root is case-sensitive `Empathy/`; reconcile unique material against existing architecture. |
| `imagination-simulation/README.md` | NEEDS_ROOT_REMAP | `psychological behaviors/IMAGINATION_SIMULATION.md` | Capability is compatible, but alternate root is not. Keep simulation distinct from observation/evidence. |
| `interfaces/README.md` | REJECT / SUPERSEDED | no umbrella root | Canonical architecture exposes HC-owned interfaces through established roots rather than an `interfaces/` wrapper. Child material is remapped individually. |
| `interfaces/adaptable-io/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/ARCHITECTURE.md` or focused child contract | Preserve body/peripheral adaptation semantics under existing root. |
| `interfaces/audition-speech/README.md` | NEEDS_ROOT_REMAP | split between `speech recognition & synthesis/` and `phoenetics/` where appropriate | Do not create an audition-speech root; separate signal transduction/production from phonetic-linguistic representation. |
| `interfaces/external-compute/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/EXTERNAL_COMPUTE_INTERFACE.md` | External compute is a peripheral/service boundary, not essential cognition outside the HC. |
| `interfaces/kinesis/README.md` | NEEDS_ROOT_REMAP | `kinesis/ARCHITECTURE.md` | Canonical root already exists. |
| `interfaces/network/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/NETWORK_INTERFACE.md` | Network attachment is an interface capability; network output is not automatic cognition/authority. |
| `interfaces/optics/README.md` | NEEDS_ROOT_REMAP | `optics/ARCHITECTURE.md` | Canonical root already exists. |
| `interfaces/somatics-interoception/README.md` | NEEDS_ROOT_REMAP | split across `somatics/` and `homeostasis-interoception/` | One branch file spans two canonical responsibilities; port by concern, not by folder copy. |
| `interoception/README.md` | NEEDS_ROOT_REMAP | `homeostasis-interoception/` | Canonical root already combines homeostatic regulation and interoceptive inference. |
| `language/README.md` | NEEDS_ROOT_REMAP | split across `semantics/`, `pragmatics/`, `phoenetics/`, and `speech recognition & synthesis/` | Useful language/translation constraints, but a new language root would replace owner-established decomposition. |
| `learning/README.md` | NEEDS_ROOT_REMAP | `routing instructions with neuroplasticity/LEARNING_AND_DEVELOPMENT.md` plus cognition-specific references | Learning/plasticity is cross-cutting; do not introduce a new root without owner redesign. |
| `memory/deep/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/DEEP_MEMORY_MODEL.md` | Preserve long-horizon durability/provenance semantics. |
| `memory/episodic/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/EPISODIC_MEMORY.md` | Durable episodic class fits canonical deep-memory root. |
| `memory/procedural/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/PROCEDURAL_MEMORY.md` | Preserve `procedure available != authorized != executed != verified effect`. |
| `memory/semantic/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/SEMANTIC_MEMORY.md` | Long-lived generalized knowledge belongs under canonical durable-memory responsibility. |
| `memory/working/README.md` | NEEDS_ROOT_REMAP | `current memory storage/WORKING_MEMORY.md` | Fast volatile current context fits canonical current-memory root. |
| `metacognition/README.md` | NEEDS_ROOT_REMAP | `cognition/METACOGNITION.md` | Compatible capability; no canonical metacognition root exists. |
| `nooplex-fabric/README.md` | DUPLICATES_MAIN | no direct port | `integration-arbitration/NOOPLEX_FABRIC.md` is already canonical. |
| `perception/README.md` | MATERIAL_REDESIGN | no automatic port | Perception is required capability, but canonical responsibility is distributed across sensory roots, cognition, and resolver; creating a new top-level root needs owner/warden decision. |
| `personification/README.md` | DUPLICATES_MAIN | no direct port | Canonical subsystem exists; reconcile only demonstrably novel material. |
| `pragmatics/README.md` | DUPLICATES_MAIN | no direct port | Canonical pragmatics root already contains runtime material. |
| `research/source-ledger/ACADEMIC_FOUNDATIONS.md` | RESEARCH_ONLY | `research/source-ledger/ACADEMIC_FOUNDATIONS.md` | Preserve as non-canonical source/evidence support. |
| `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md` | RESEARCH_ONLY | `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md` | Preserve generic mechanism provenance; exclude identity payloads. |
| `research/source-ledger/SOURCE_FEDERATION_LEDGER.md` | RESEARCH_ONLY | `research/source-ledger/SOURCE_FEDERATION_LEDGER.md` | Useful provenance/reconciliation support, not brain canon by itself. |
| `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md` | RESEARCH_ONLY | `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md` | Schema-level reusable patterns only; no instance-specific rows. |
| `resolver/README.md` | DUPLICATES_MAIN | no direct port | Canonical resolver subsystem exists. |
| `self-model/README.md` | NEEDS_ROOT_REMAP | `self identity/SELF_MODEL.md` | Preserve self-model/identity distinction without introducing new root. |
| `semantics/README.md` | DUPLICATES_MAIN | no direct port | Canonical semantics root already has cross-repo semantic runtime material. |
| `sexuality/README.md` | DUPLICATES_MAIN | no direct port | Canonical sexuality subsystem exists; activation/presence rules are already cross-cutting. |
| `social-cognition/README.md` | NEEDS_ROOT_REMAP | `sociological behaviors/SOCIAL_COGNITION.md` with scoped interfaces to `Empathy/` | Preserve person-model fallibility and privacy boundaries. |
| `values/README.md` | NEEDS_ROOT_REMAP | `psychological behaviors/VALUES_AND_COMMITMENTS.md` with explicit links to `volitions-conations/` | Values/commitments influence choice but do not become truth/authority. |
| `volition/README.md` | NEEDS_ROOT_REMAP | `volitions-conations/VOLITION.md` | Canonical root already combines the relevant family. |
| `world-model/README.md` | NEEDS_ROOT_REMAP | `cognition/WORLD_MODEL_AND_PREDICTION.md` | Preserve predictive/model-state capability inside canonical cognition root. |

## Immediate selective-integration set

The first low-conflict set worth porting after content-level review is:

1. `contracts/SUBSYSTEM_LIFECYCLE.md` -> `basic operating instructions/SUBSYSTEM_LIFECYCLE.md`
2. `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` -> `integration-arbitration/COALITIONS_GATING_AND_ARBITRATION.md`
3. `docs/architecture/CONNECTIVITY_PLANES.md` -> `routing instructions with neuroplasticity/CONNECTIVITY_PLANES.md`
4. `docs/architecture/HYPERCONNECTOME_NOTATION.md` -> same architecture-doc path
5. `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` -> same architecture-doc path after canonical-root normalization
6. research source-ledger files -> research-only transfer surface

## Explicit non-actions

- no merge to `main`;
- no force-rewrite of PR #4;
- no top-level root rename or replacement;
- no reintroduction of the branch temporal-hypergraph copy over the canonical corrected version;
- no identity-specific payload admission into the generic template.
