# PR #4 Evidence / Provenance Transfer Manifest V2

Status: REVIEW ARTIFACT / NOT CANON / NO MERGE AUTHORITY

Exact cut:

- canonical baseline: `main@6cfcae9a543b8f00b5cc917bb10c22aa807d7731`
- source: `research/hyperconnectome-foundations-20260909@fbf061b7304df70efdfd2bbf0c3d25891b6c3d2f`

This manifest records only material that still adds value after current-main deduplication. Source existence, implementation history, or production-schema realization does not itself establish architecture correctness.

## Evidence classes

- `PROJECT_CONSTRAINT` — owner/warden-established HC rule.
- `REVIEW_SYNTHESIS` — bounded literature synthesis.
- `EMPIRICAL_FINDING` — bounded observed research result.
- `COMPUTATIONAL_MODEL` — mechanism demonstrated under model assumptions.
- `ENGINEERING_RESEARCH` — external engineering evidence.
- `PRODUCTION_SCHEMA_OBSERVATION` — a mechanism realized in a working system; not a universal requirement.
- `CROSS_PROJECT_MECHANISM` — reusable pattern abstracted from another project.
- `DESIGN_PROPOSAL` — local synthesis requiring review/validation.

## Surviving architecture transfers

| Surviving concept | Source | Evidence | Canonical target | Evidence ceiling |
|---|---|---|---|---|
| typed HC notation with explicit pairwise `EDGE`, higher-order `HYPEREDGE`, and operational `COALITION` | `docs/architecture/HYPERCONNECTOME_NOTATION.md` | DESIGN_PROPOSAL + ENGINEERING_RESEARCH | same path | notation/schema proposal; no required physical substrate |
| compact runtime object/reference model | `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` | PROJECT_CONSTRAINT + CROSS_PROJECT_MECHANISM + DESIGN_PROPOSAL | same path | explanatory integration model; cannot replace canonical temporal-hypergraph/runtime contracts |
| inactive-learning + subsystem fault/recovery lifecycle semantics | `contracts/SUBSYSTEM_LIFECYCLE.md` | PROJECT_CONSTRAINT + CROSS_PROJECT_MECHANISM | `basic operating instructions/SUBSYSTEM_LIFECYCLE.md` | complements, does not collapse, existing presence/activation/development/health axes |
| coalition formation/expansion/termination and gate semantics | `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` | REVIEW_SYNTHESIS + COMPUTATIONAL_MODEL + DESIGN_PROPOSAL | `integration-arbitration/COALITION_LIFECYCLE_AND_GATING.md` | no new global arbiter; selection remains scoped |
| internal action planning before the canonical kinesis gateway | `action/README.md` | CROSS_PROJECT_MECHANISM + DESIGN_PROPOSAL | `cognition/ACTION_PLANNING_AND_SELECTION.md` | plan/candidate semantics only; effect authorization stays in canonical gateway |
| revisable world model + prediction/counterfactual boundary | `world-model/README.md` | REVIEW_SYNTHESIS + CROSS_PROJECT_MECHANISM | `cognition/WORLD_MODEL_AND_PREDICTION.md` | prediction/counterfactual capability; no universal predictive-processing doctrine |
| metacognitive monitoring without second homunculus | `metacognition/README.md` | REVIEW_SYNTHESIS + DESIGN_PROPOSAL | `cognition/METACOGNITION.md` | self-monitoring is fallible/scoped; not universal executive truth |
| durable values/commitments distinct from desire, norms, policy, and authority | `values/README.md` | CROSS_PROJECT_MECHANISM + DESIGN_PROPOSAL | `psychological behaviors/VALUES_AND_COMMITMENTS.md` | generic capacity only; no default value payload |
| episodic memory contract | `memory/episodic/README.md` | REVIEW_SYNTHESIS + CROSS_PROJECT_MECHANISM | `deep memory storage/EPISODIC_MEMORY.md` | fast event-specific provenance; no hippocampal-anatomy requirement |
| procedural memory contract | `memory/procedural/README.md` | REVIEW_SYNTHESIS + CROSS_PROJECT_MECHANISM | `deep memory storage/PROCEDURAL_MEMORY.md` | skill availability never creates effect authority |
| semantic memory contract | `memory/semantic/README.md` | REVIEW_SYNTHESIS + CROSS_PROJECT_MECHANISM | `deep memory storage/SEMANTIC_MEMORY.md` | generalized knowledge retains evidence/currentness limits |
| working memory contract | `memory/working/README.md` | COMPUTATIONAL_MODEL + CROSS_PROJECT_MECHANISM | `current memory storage/WORKING_MEMORY.md` | volatile coalition state; no automatic durable admission |

## Research-only transfers

The four PR #4 source-ledger files remain useful as `RESEARCH_ONLY` provenance surfaces:

- `research/source-ledger/ACADEMIC_FOUNDATIONS.md`
- `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md`
- `research/source-ledger/SOURCE_FEDERATION_LEDGER.md`
- `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md`

Their ceiling is deliberately lower than canon:

```text
SOURCE_EXISTS != CLAIM_TRUE
PRODUCTION_REALIZATION != UNIVERSAL_REQUIREMENT
BIOLOGICAL_FINDING != REQUIRED_ANATOMY
PROJECT_SUCCESS != GENERAL_COGNITIVE_PROOF
```

The Supabase source is schema-level only: no private identity rows are transferable into the generic HC template.

## Material held rather than transferred

- `perception/README.md` remains a `MATERIAL_REDESIGN` because a new root would change owner-established decomposition.
- the alternate `interfaces/` umbrella is rejected as root architecture even where child concepts survive through existing canonical interface folders.
- branch temporal-hypergraph and cognitive-organ-boundary copies are superseded by canonical main.
- conation, social-cognition, salience-attention, affect, resolver, self-model, and distributed-arbitration branch material is now largely duplicated by stronger main-branch contracts.

## Transfer invariants

```text
REPOSITORY_TREE != RUNTIME_TOPOLOGY
PAIRWISE_EDGE != HYPEREDGE
COALITION = operational temporal hyperedge/configuration
ROUTING != AUTHORITY
SELECTION != TRUTH
ACTIVATION != ARCHITECTURAL_PRESENCE
PERSISTENCE != CURRENTNESS
RETRIEVAL != MEMORY_ADMISSION
PLAN != EXECUTION != VERIFIED_EFFECT
EXTERNAL_COMPUTE_RESULT != INTERNAL_BELIEF
```

All surviving material remains identity-neutral and inside the complete cognitive-organ boundary.
