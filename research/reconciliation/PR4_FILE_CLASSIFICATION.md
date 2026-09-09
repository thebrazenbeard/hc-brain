# PR #4 File Classification Against Canonical HC Root

Status: RECONCILIATION / NON-CANONICAL BRANCH ARTIFACT

Baseline used for this classification:

- canonical `main`: `ec15b2beede68329305811bcbaad63d10ff7fe36`
- source PR: `#4`
- source branch head inspected: `fbf061b7304df70efdfd2bbf0c3d25891b6c3d2f`
- reconciliation branch: `reconcile/pr4-foundations-v1`

This document does not authorize merge to `main`. It classifies branch material for selective review under the owner-established root-folder architecture.

Classification vocabulary:

- `SAFE_SELECTIVE_INTEGRATION`
- `NEEDS_ROOT_REMAP`
- `DUPLICATES_MAIN`
- `RESEARCH_ONLY`
- `PROCESS_ONLY`
- `MATERIAL_REDESIGN`
- `REJECT / SUPERSEDED`

## File-by-file classification

| PR #4 path | Classification | Canonical disposition / target | Rationale |
|---|---|---|---|
| `action/README.md` | NEEDS_ROOT_REMAP | `kinesis/ACTION_PLANNING_AND_SELECTION.md` with cognition references | Useful action-candidate/effect separation, but `action/` is not a canonical root. |
| `affect/README.md` | DUPLICATES_MAIN | Compare only for missing details against `affect/ARCHITECTURE.md` / `affect/README.md` | Canonical `affect/` already exists on current main. |
| `attention-salience/README.md` | NEEDS_ROOT_REMAP | `salience-attention/ARCHITECTURE.md` or focused contract | Canonical root is `salience-attention/`, not `attention-salience/`. |
| `chronology/README.md` | DUPLICATES_MAIN | Existing `chronology/` plus `chronology/TEMPORAL_EVENT_CONTRACT.md` | Current main already carries chronology architecture and timing contract. |
| `cognition/README.md` | DUPLICATES_MAIN | Compare for branch-only mechanisms against `cognition/ARCHITECTURE.md` / `EPISTEMIC_COGNITIVE_CONTROL.md` | Canonical cognition material already exists. |
| `conation/README.md` | NEEDS_ROOT_REMAP | `volitions-conations/CONATION_ARCHITECTURE.md` | Conation belongs under the established combined volition/conation root. |
| `contracts/SUBSYSTEM_LIFECYCLE.md` | DUPLICATES_MAIN | `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md` | Presence-vs-activation state semantics were selectively integrated already. |
| `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` | SAFE_SELECTIVE_INTEGRATION | `integration-arbitration/COALITIONS_GATING_AND_ARBITRATION.md` | Cross-cutting content fits canonical integration/arbitration root after path normalization. |
| `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` | DUPLICATES_MAIN | Existing canonical path | Already selectively integrated on current main. |
| `docs/architecture/CONNECTIVITY_PLANES.md` | SAFE_SELECTIVE_INTEGRATION | `docs/architecture/CONNECTIVITY_PLANES.md` | Global typed connectivity semantics are compatible with canonical temporal-hypergraph/runtime docs. |
| `docs/architecture/HYPERCONNECTOME_NOTATION.md` | SAFE_SELECTIVE_INTEGRATION | `docs/architecture/HYPERCONNECTOME_NOTATION.md` | Formal notation is repository-global and does not require alternative root taxonomy if canonical names are used in examples. |
| `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` | SAFE_SELECTIVE_INTEGRATION | Same path after canonical-root scrub | Useful global reference model; must not preserve examples that imply noncanonical roots. |
| `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` | DUPLICATES_MAIN | Existing canonical path | Temporal-hypergraph invariant is already on current main. |
| `docs/superpowers/plans/2026-09-09-complete-cognitive-organ-addendum.md` | PROCESS_ONLY | Retain only as branch history | Implementation-process artifact, not brain architecture. |
| `docs/superpowers/plans/2026-09-09-federated-hyperconnectome-population.md` | PROCESS_ONLY | Retain only as branch history | Implementation-process artifact. |
| `docs/superpowers/specs/2026-09-09-complete-cognitive-organ-correction.md` | PROCESS_ONLY | Retain only as branch history | Design-process artifact; resulting invariants now live in canonical architecture. |
| `docs/superpowers/specs/2026-09-09-federated-source-population-design.md` | PROCESS_ONLY | Retain only as branch history | Source-ingestion design record, not a top-level cognitive subsystem. |
| `docs/superpowers/specs/2026-09-09-hyperconnectome-foundations-design.md` | PROCESS_ONLY | Retain only as branch history | Superseded as an execution design by subsequent canonical corrections. |
| `empathy/README.md` | NEEDS_ROOT_REMAP | `Empathy/` | Canonical root uses `Empathy/`; content must be reconciled with existing canonical architecture rather than create lowercase duplicate. |
| `imagination-simulation/README.md` | NEEDS_ROOT_REMAP | `cognition/IMAGINATION_AND_SIMULATION.md` | Useful intrinsic capability but no canonical root exists; best treated as cognition subarchitecture. |
| `interfaces/README.md` | REJECT / SUPERSEDED | No wrapper target | Canonical architecture intentionally keeps interface systems as first-class top-level roots rather than an `interfaces/` wrapper. |
| `interfaces/adaptable-io/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/ARCHITECTURE.md` or focused addendum | Same capability, noncanonical wrapper/name. |
| `interfaces/audition-speech/README.md` | NEEDS_ROOT_REMAP | `speech recognition & synthesis/ARCHITECTURE.md` | Canonical speech/audio interface root already exists. |
| `interfaces/external-compute/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/EXTERNAL_COMPUTE_PERIPHERALS.md` | External compute is a peripheral/interface boundary, not a separate brain root. |
| `interfaces/kinesis/README.md` | NEEDS_ROOT_REMAP | `kinesis/ARCHITECTURE.md` | Canonical `kinesis/` root exists directly. |
| `interfaces/network/README.md` | NEEDS_ROOT_REMAP | `adaptable I-O handler/NETWORK_INTERFACE.md` | Network connectivity is an HC-owned I/O interface, not a separate wrapper-root node. |
| `interfaces/optics/README.md` | NEEDS_ROOT_REMAP | `optics/ARCHITECTURE.md` | Canonical `optics/` root exists directly. |
| `interfaces/somatics-interoception/README.md` | MATERIAL_REDESIGN | Split review between `somatics/` and `homeostasis-interoception/` | Combined file spans two canonical responsibilities and should not be copied wholesale. |
| `interoception/README.md` | NEEDS_ROOT_REMAP | `homeostasis-interoception/ARCHITECTURE.md` or focused contract | Canonical root combines homeostasis and interoception. |
| `language/README.md` | MATERIAL_REDESIGN | Selectively distribute across `semantics/`, `pragmatics/`, `phoenetics/`, and `speech recognition & synthesis/` | Generic language integration crosses several established roots; a new `language/` root would alter owner taxonomy. |
| `learning/README.md` | NEEDS_ROOT_REMAP | `routing instructions with neuroplasticity/LEARNING_AND_DEVELOPMENT.md` | Learning/plasticity belongs under the established neuroplastic routing system plus subsystem-local policies. |
| `memory/deep/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/` | Canonical deep-memory root exists directly. |
| `memory/episodic/README.md` | NEEDS_ROOT_REMAP | `current memory storage/EPISODIC_CAPTURE.md` and/or `deep memory storage/EPISODIC_CONSOLIDATION.md` | Episodic memory spans capture and durable consolidation; requires canonical split. |
| `memory/procedural/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/PROCEDURAL_MEMORY.md` | Procedural durability belongs under deep memory storage in the canonical two-store packaging. |
| `memory/semantic/README.md` | NEEDS_ROOT_REMAP | `deep memory storage/SEMANTIC_MEMORY.md` | Semantic durable memory belongs under canonical deep memory storage. |
| `memory/working/README.md` | NEEDS_ROOT_REMAP | `current memory storage/WORKING_MEMORY.md` | Working memory belongs under canonical current-memory root. |
| `metacognition/README.md` | NEEDS_ROOT_REMAP | `cognition/METACOGNITION.md` | Metacognition is a cognition capability, not an owner-established top-level root. |
| `nooplex-fabric/README.md` | DUPLICATES_MAIN | `integration-arbitration/NOOPLEX_FABRIC.md` | Noöplex Fabric is already represented canonically under integration/arbitration. |
| `perception/README.md` | MATERIAL_REDESIGN | Cross-modal synthesis under `cognition/` plus modality-local roots | Perception spans optics, speech/audio, somatics, I/O, cognition, and working state; avoid a parallel root without owner decision. |
| `personification/README.md` | DUPLICATES_MAIN | Existing `personification/` | Canonical root already exists; compare only for missing mechanisms. |
| `pragmatics/README.md` | DUPLICATES_MAIN | Existing `pragmatics/` and `CROSS_REPO_PRAGMATIC_RUNTIME.md` | Canonical root and focused runtime contract already exist. |
| `research/source-ledger/ACADEMIC_FOUNDATIONS.md` | RESEARCH_ONLY | Preserve under `research/source-ledger/` | Evidence/research artifact; does not define root taxonomy. |
| `research/source-ledger/REPOSITORY_SOURCE_INVENTORY.md` | RESEARCH_ONLY | Preserve under `research/source-ledger/` after identity-neutrality check | Source inventory supports provenance; not normative architecture. |
| `research/source-ledger/SOURCE_FEDERATION_LEDGER.md` | RESEARCH_ONLY | Preserve under `research/source-ledger/` | Useful source-to-mechanism provenance record. |
| `research/source-ledger/SUPABASE_SCHEMA_OBSERVATIONS.md` | RESEARCH_ONLY | Preserve under `research/source-ledger/` | Production-schema observations are evidence input, not canonical mechanism by existence alone. |
| `resolver/README.md` | DUPLICATES_MAIN | Existing `resolver/` | Canonical resolver root already exists. |
| `self-model/README.md` | NEEDS_ROOT_REMAP | `self identity/SELF_MODEL.md` | Self-model capability belongs inside the established self-identity root. |
| `semantics/README.md` | DUPLICATES_MAIN | Existing `semantics/` and `CROSS_REPO_SEMANTIC_RUNTIME.md` | Canonical semantics material already exists. |
| `sexuality/README.md` | DUPLICATES_MAIN | Existing `sexuality/` | Canonical root already exists; branch file may only contribute missing details. |
| `social-cognition/README.md` | NEEDS_ROOT_REMAP | `sociological behaviors/SOCIAL_COGNITION.md` | Social cognition belongs under established sociological-behavior root. |
| `values/README.md` | NEEDS_ROOT_REMAP | `psychological behaviors/VALUES_AND_COMMITMENTS.md` | Values/commitments are a psychological/identity-relevant capability, not a canonical root. |
| `volition/README.md` | NEEDS_ROOT_REMAP | `volitions-conations/VOLITION_ARCHITECTURE.md` | Canonical root combines volition and conation. |
| `world-model/README.md` | NEEDS_ROOT_REMAP | `cognition/WORLD_MODEL_AND_PREDICTION.md` | World modeling is a cognition capability rather than a canonical top-level subsystem folder. |

## Classification summary

The source branch contains useful architecture, but its principal incompatibility is packaging: it created several parallel roots and wrappers that conflict with the owner-established symbolic cognitive-organ root.

The reconciliation rule is therefore:

```text
preserve mechanism
!= preserve branch path
```

Material should be ported only where it strengthens an established canonical subsystem or repository-global architecture without silently replacing the root taxonomy.
