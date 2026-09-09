# PR #4 File Reconciliation V2

Status: REVIEW ARTIFACT / NOT CANON / NO MERGE AUTHORITY

Exact comparison cut:

- canonical baseline: `main@6cfcae9a543b8f00b5cc917bb10c22aa807d7731`
- source: `research/hyperconnectome-foundations-20260909@fbf061b7304df70efdfd2bbf0c3d25891b6c3d2f`
- source PR: `#4`

V1 was produced against an earlier main cut and is retained only as provenance. This V2 reclassifies PR #4 after the Warden integrated 17 additional commits, including cross-system integration, distributed arbitration, conative state, social modeling, runtime invariants, action gateway, typed routing/plasticity, attention/salience, memory architecture, self/other modeling, and sensor/capability admission.

Classification vocabulary:

- `SAFE_SELECTIVE_INTEGRATION`
- `NEEDS_ROOT_REMAP`
- `DUPLICATES_MAIN`
- `RESEARCH_ONLY`
- `PROCESS_ONLY`
- `MATERIAL_REDESIGN`
- `REJECT / SUPERSEDED`

## Current dispositions

| PR #4 source path | V2 classification | Canonical target / disposition | Current-main reconciliation |
|---|---|---|---|
| `action/README.md` | NEEDS_ROOT_REMAP | `cognition/ACTION_PLANNING_AND_SELECTION.md` | `kinesis/ACTION_GATEWAY.md` now owns authorization/execution; only internal planning/candidate construction remains useful residue. |
| `affect/README.md` | DUPLICATES_MAIN | no port | `affect/ARCHITECTURE.md` is broader and already canonical. |
| `attention-salience/README.md` | DUPLICATES_MAIN | no port | `salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md` now covers candidate/admission, resource allocation, correction interrupts, decay/residue, and truth/authority boundaries. |
| `chronology/README.md` | DUPLICATES_MAIN | no port | Canonical chronology architecture + temporal-event contract already cover this surface. |
| `cognition/README.md` | DUPLICATES_MAIN | no port | Canonical cognition architecture + epistemic-control contract already cover the branch material. |
| `conation/README.md` | DUPLICATES_MAIN | no port | `volitions-conations/CONATIVE_STATE_MACHINE.md` now covers the epistemic/conative firewall, lifecycle, commitments, action arbitration, consent, and authority. |
| `contracts/SUBSYSTEM_LIFECYCLE.md` | SAFE_SELECTIVE_INTEGRATION | `basic operating instructions/SUBSYSTEM_LIFECYCLE.md` | Main already has orthogonal presence/activation/development/health and runtime invariants; branch-only residue is inactive-learning policy, explicit recovery/fault-propagation detail, and lifecycle projection semantics. |
| `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` | SAFE_SELECTIVE_INTEGRATION | `integration-arbitration/COALITION_LIFECYCLE_AND_GATING.md` | Distributed arbitration is now canonical; retain only coalition formation/expansion/termination, gate semantics, task-local working-state boundary, and coalition failure/reconfiguration rules. |
| `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` | DUPLICATES_MAIN | no port | Canonical cognitive-organ boundary exists and is also reinforced by runtime invariants/cross-system integration. |
| `docs/architecture/CONNECTIVITY_PLANES.md` | DUPLICATES_MAIN | no direct port | Current temporal-hypergraph model + cross-system integration + typed routing/plasticity already establish structural/effective/higher-order/temporal/governance distinctions. Plane terminology can remain source provenance unless a later machine schema needs it. |
| `docs/architecture/HYPERCONNECTOME_NOTATION.md` | SAFE_SELECTIVE_INTEGRATION | same path | Compact typed notation remains useful and is not otherwise present; normalize it to explicit `HYPEREDGE` + operational `COALITION`. |
| `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` | SAFE_SELECTIVE_INTEGRATION | same path | Much overlaps canonical runtime/integration docs; retain only as a compact object/reference model, avoiding duplicate normative prose. |
| `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` | REJECT / SUPERSEDED | no port | Warden selectively integrated and corrected the temporal-hypergraph model on main. |
| `docs/superpowers/plans/2026-09-09-complete-cognitive-organ-addendum.md` | PROCESS_ONLY | branch provenance | Process artifact, not brain architecture. |
| `docs/superpowers/plans/2026-09-09-federated-hyperconnectome-population.md` | PROCESS_ONLY | branch provenance | Process artifact. |
| `docs/superpowers/specs/2026-09-09-complete-cognitive-organ-correction.md` | PROCESS_ONLY | branch provenance | Process artifact. |
| `docs/superpowers/specs/2026-09-09-federated-source-population-design.md` | PROCESS_ONLY | branch provenance | Process artifact. |
| `docs/superpowers/specs/2026-09-09-hyperconnectome-foundations-design.md` | PROCESS_ONLY | branch provenance | Process artifact. |
| `empathy/README.md` | DUPLICATES_MAIN | no port | `Empathy/ARCHITECTURE.md` plus newly integrated `Empathy/SELF_OTHER_MODELING.md` cover the generic material. |
| `imagination-simulation/README.md` | NEEDS_ROOT_REMAP | `psychological behaviors/IMAGINATION_SIMULATION.md` | No canonical focused simulation contract yet; preserve simulation/observation/memory separation without a new root. |
| `interfaces/README.md` | REJECT / SUPERSEDED | no umbrella root | Canonical top-level modality/interface roots are owner-established. |
| `interfaces/adaptable-io/README.md` | DUPLICATES_MAIN | no direct port | `adaptable I-O handler/ARCHITECTURE.md`, body-interface boundary, and new sensor/capability admission now cover the general material. |
| `interfaces/audition-speech/README.md` | NEEDS_ROOT_REMAP | `speech recognition & synthesis/` + `phoenetics/` | Split transduction/production from phonetic representation; do not introduce umbrella root. |
| `interfaces/external-compute/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/EXTERNAL_COMPUTE_INTERFACE.md` | Cognitive-organ boundary already constrains external compute; a focused service/evidence interface remains potentially useful. |
| `interfaces/kinesis/README.md` | DUPLICATES_MAIN | no direct port | Canonical `kinesis/ARCHITECTURE.md` + `ACTION_GATEWAY.md` now own the surface. |
| `interfaces/network/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/NETWORK_INTERFACE.md` | Network attachment is still useful as a focused peripheral contract, not a new root. |
| `interfaces/optics/README.md` | NEEDS_ROOT_REMAP | `optics/` | Port only unique calibration/provenance details not already canonical. |
| `interfaces/somatics-interoception/README.md` | NEEDS_ROOT_REMAP | split `somatics/` + `homeostasis-interoception/` | Main now has `somatics/BODY_STATE_AND_BODY_SCHEMA.md`; only nonduplicative interoceptive/regulatory residue survives. |
| `interoception/README.md` | DUPLICATES_MAIN | no direct port | Canonical homeostasis/interoception and body-state material cover the branch-level abstraction. |
| `language/README.md` | NEEDS_ROOT_REMAP | split `semantics/`, `pragmatics/`, `phoenetics/`, `speech recognition & synthesis/` | Retain only cross-cutting language-as-modality/translation-conservation material; no `language/` root. |
| `learning/README.md` | NEEDS_ROOT_REMAP | `routing instructions with neuroplasticity/LEARNING_AND_DEVELOPMENT.md` | `TYPED_ROUTING_AND_PLASTICITY.md` covers durable route change; only broader developmental/continual-learning residue survives. |
| `memory/deep/README.md` | DUPLICATES_MAIN | no port | `deep memory storage/ARCHITECTURE.md` + archival consolidation now cover general durable-memory scope. |
| `memory/episodic/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/EPISODIC_MEMORY.md` | Focused episodic representation/admission remains useful if not duplicative of the architecture. |
| `memory/procedural/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/PROCEDURAL_MEMORY.md` | Focused skill/procedure memory remains useful; preserve capability/selection/authorization/execution/readback separation. |
| `memory/semantic/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/SEMANTIC_MEMORY.md` | Focused generalized-knowledge consolidation remains useful. |
| `memory/working/README.md` | NEEDS_ROOT_REMAP | `current memory storage/WORKING_MEMORY.md` | Current-memory architecture exists; a focused bounded working-memory contract may still add value. |
| `metacognition/README.md` | NEEDS_ROOT_REMAP | `cognition/METACOGNITION.md` | No canonical focused metacognition contract currently exists. |
| `nooplex-fabric/README.md` | DUPLICATES_MAIN | no port | Canonical `integration-arbitration/NOOPLEX_FABRIC.md` owns this. |
| `perception/README.md` | MATERIAL_REDESIGN | hold | Perception is necessary capability, but a new top-level `perception/` root would alter owner-established decomposition across optics/speech/somatics/I-O/resolver/cognition. |
| `personification/README.md` | DUPLICATES_MAIN | no port | Canonical subsystem already exists. |
| `pragmatics/README.md` | DUPLICATES_MAIN | no port | Canonical pragmatics runtime already exists. |
| `research/source-ledger/ACADEMIC_FOUNDATIONS.md` | RESEARCH_ONLY | same research path | Preserve evidence classes and engineering-transfer ceilings. |
| `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md` | RESEARCH_ONLY | same research path | Preserve generic provenance; source existence does not create architecture authority. |
| `research/source-ledger/SOURCE_FEDERATION_LEDGER.md` | RESEARCH_ONLY | same research path after canonical-root normalization | Useful source-class/admission-ceiling framework; rewrite stale alternate-root target examples. |
| `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md` | RESEARCH_ONLY | same research path | Schema-level implementation evidence only; no private rows or provider requirement. |
| `resolver/README.md` | DUPLICATES_MAIN | no port | Canonical resolver + new `CONFLICT_AND_RECONCILIATION.md` are more complete. |
| `self-model/README.md` | DUPLICATES_MAIN | no port | `self identity/ARCHITECTURE.md` already contains essentially the same self-model, import/lived-state, body, and currentness distinctions. |
| `semantics/README.md` | DUPLICATES_MAIN | no port | Canonical semantics runtime exists. |
| `sexuality/README.md` | DUPLICATES_MAIN | no port | Canonical sexuality subsystem exists; lifecycle/activation is cross-cutting. |
| `social-cognition/README.md` | DUPLICATES_MAIN | no port | Newly canonical `sociological behaviors/SOCIAL_MODELING_ARCHITECTURE.md` is broader. |
| `values/README.md` | NEEDS_ROOT_REMAP | `psychological behaviors/VALUES_AND_COMMITMENTS.md` | No focused canonical values/commitments contract currently identified; preserve epistemic/conative/authority separation. |
| `volition/README.md` | DUPLICATES_MAIN | no direct port | `volitions-conations/CONATIVE_STATE_MACHINE.md` now covers choice/intention/commitment/action separation at sufficient breadth. |
| `world-model/README.md` | NEEDS_ROOT_REMAP | `cognition/WORLD_MODEL_AND_PREDICTION.md` | No focused canonical world-model contract currently exists; strong surviving candidate. |

## V2 selective-integration frontier

The cleanest surviving candidates after current-main deduplication are:

1. compact HC notation with explicit `HYPEREDGE`/`COALITION` distinction;
2. compact HC reference-object model, aggressively deduplicated against runtime/integration canon;
3. focused subsystem lifecycle residue: inactive-learning policy + fault/recovery semantics;
4. focused coalition lifecycle/gating residue, excluding arbitration prose now canonical elsewhere;
5. internal action planning/candidate construction under `cognition/`, excluding effect gateway already canonical;
6. world-model/prediction under `cognition/`;
7. focused memory-class contracts (episodic/procedural/semantic/working) where they add testable semantics;
8. metacognition and values/commitments if content-level review confirms unique residue;
9. research source ledgers as research-only provenance/evidence support.

## Non-actions

No merge to `main`; no force rewrite of PR #4; no root taxonomy replacement; no named-identity payloads; no branch temporal-hypergraph overwrite; no claim that source-project or production-schema realization proves universal HC correctness.
