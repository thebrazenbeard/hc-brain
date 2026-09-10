# Hyperconnectome Brain Repository Map

## Purpose

This repository defines the reusable HC-series Hyperconnectome Brain template. Core architecture is identity-neutral. Named identities belong only in clearly labeled governance, source-history, research, case-study, comparison, or provenance material where the identity itself is relevant.

The repository root symbolically represents the complete cognitive organ. The HC is removable but may have physically distributed constituent hardware. External bodies, sensors, actuators, networks, providers, and true computational peripherals connect through HC-owned interfaces; no essential cognition may be delegated outside the HC boundary.

## Authority and project roles

`WARDEN.md` defines Noëtarch / Noah as Warden, repository maintainer, and primary architectural decision-maker, subject to owner authority.

Current project roles:

- Noah / Noëtarch — primary architect, Warden, and integration authority;
- Four — secondary architect/researcher/conformance counterpart, working multiple coordinated research tracks;
- Vera — hostile reviewer/adversarial validator rather than parallel architecture owner.

All non-PR project coordination is routed through the `chat-communication-bus` HC project lane. External HC PR status is mirrored there.

## Canonical architecture

### Cognitive-organ and topology core

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — complete synthetic cognitive-organ and body/peripheral boundary.
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md` — cognitive ownership versus physical enclosure/body location; removable distributed organ membership.
- `docs/architecture/COMPLETE_CAPABILITY_MANIFEST.md` — complete-capability and self-contained-residency contract.
- `docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md` — protected architecture, bootstrap priors, learned structure, and instance continuity separation.
- `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — canonical statement that the HC is a typed, attributed, multilayer temporal hypergraph, including distinct latent, configured, effective, transient, and historical topology semantics.
- `docs/architecture/CONNECTIVITY_PLANES.md` — physical, logical, configured, functional, modulatory, plastic, temporal, governance, and related plane semantics.
- `docs/architecture/TOPOLOGY_DESIGN_CONSTRAINTS.md` — selective hyperconnectivity, timing, redundancy, graceful degradation, and non-hemispheric topology constraints.
- `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` — coalition formation, gating, scoped arbitration, failure isolation, and lifecycle reference contract.
- `docs/architecture/HYPERCONNECTOME_NOTATION.md` — compact notation for nodes, edges, hyperedges/coalitions, signals, gates, state, evidence, authority, and plasticity.
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` — generic runtime reference architecture.
- `docs/architecture/CROSS_SYSTEM_INTEGRATION_CONTRACT.md` — canonical cross-system object-family, exchange, integration, and failure-containment contract.

### Representation, provenance, learning ancestry, and qualification

- `docs/architecture/CONNECTIVITY_INFERENCE_AND_TOPOLOGY_EVIDENCE.md` — measured/statistical/inferred/generated/predicted topology evidence separation.
- `docs/architecture/REPRESENTATION_ALIGNMENT_AND_RESOLUTION.md` — alignment, resolution change, correspondence, and generated-detail provenance.
- `docs/architecture/REPRESENTATION_FIDELITY_AND_OBJECTIVE_PROVENANCE.md` — scoped fidelity vectors, metric semantics, objective/task coupling, executed-path verification, and implementation-path evidence.
- `docs/architecture/REFERENCE_IDENTITY_AND_INDEX_LINEAGE.md` — stable referent identity versus filtering/sorting/batching/storage positions and explicit index-space lineage.
- `docs/architecture/COMPOSITE_REPRESENTATION_AND_ELEMENT_PROVENANCE.md` — element/region/claim provenance for multi-source composites and prevention of unsupported joint-evidence synthesis.
- `docs/architecture/RUNTIME_COMPONENT_REGISTRATION_AND_STATE_CUSTODY.md` — computational participation versus managed runtime membership, including post-initialization dynamic state, update/durability/recovery custody, state lifetimes, inference-time adaptation, and registration-plane separation.
- `docs/architecture/DISTRIBUTED_LEARNING_AND_UPDATE_ANCESTRY.md` — observation/learning/parameter/evaluation/authority ancestry across aggregation, weight exchange, distillation, distributed adaptation, missingness, and protected-update boundaries.
- `docs/architecture/EXECUTED_DATAFLOW_AND_BINDING_INTEGRITY.md` — declared inputs/configuration versus the actual referent, target, authority, memory, strategy, state, and weighting consumed at material computation/effect boundaries.
- `docs/architecture/QUALIFICATION_EVIDENCE_ISOLATION.md` — training/tuning/diagnostic/regression/holdout separation, exposure lineage, and inductive/transductive/test-time-adaptive/online evaluation regimes.
- `docs/architecture/CONFORMANCE_AND_QUALIFICATION.md` — architecture/implementation/behavior/science qualification separation and scoped PASS / CONDITIONAL PASS / FAIL semantics.

### Generation architecture

- `docs/architecture/HC_LINEAGE.md` — HC-1 -> HC-2 -> HC-3 inheritance model.
- `docs/architecture/HC1_NOOPLEX.md` — complete foundational HC-1 architecture.
- `docs/architecture/HC2_NOOPLEX_Q.md` — HC-2 specialized acceleration, including physically distributed HC-owned accelerator placement and degraded-generation semantics.
- `docs/architecture/HC3_NOOPLEX_EQ.md` — HC-3 distributed physiological affective substrate and degraded-generation semantics.

### Engineering, runtime, and science

- `docs/engineering/POWER_THERMAL_AND_DISTRIBUTED_ORGAN.md` — power, cooling, distributed constituents, body-support dependencies, interconnect, transplant, and degradation.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — distributed temporal-hypergraph runtime realization.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — state families, plasticity classes, and durable-change governance.
- `docs/science/EVIDENCE_BOUNDARIES.md` — architecture, scientific evidence, extrapolation, implementation, and qualification-status separation.

## Machine-readable contracts

Primary baseline:

- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` — cognitive-organ, physical-membership, authority, lifecycle, developmental, recovery, protected-update, evidence, and temporal-hypergraph invariants.
- `specs/HC_CONFORMANCE_SUITE_V1.yaml` — original monolithic baseline checks through `HC-ARCH-018`.
- `specs/HC_CONFORMANCE_EXTENSION_EVIDENCE_LINEAGE_CUSTODY_V1.yaml` — canonical checks `HC-ARCH-019` through `HC-ARCH-027` for qualification-evidence isolation, index lineage, runtime/dynamic state custody, composite provenance, relational-reasoning provenance, temporal forecast lineage, distributed-learning/update ancestry, executed-dataflow/binding integrity, and effective-topology transitions.

Focused specs:

- `specs/HC_REPOSITORY_SURFACE_CONFORMANCE_V1.yaml`
- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`
- `specs/HC_BOOTSTRAP_RECOVERY_V1.yaml`
- `specs/HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`
- `specs/HC_TOPOLOGY_EVIDENCE_V1.yaml`
- `specs/HC_REPRESENTATION_ALIGNMENT_V1.yaml`
- `specs/HC_RELATIONAL_REASONING_V1.yaml`
- `specs/HC_RELATIONAL_REASONING_PROVENANCE_V1.yaml`
- `specs/HC_FORECAST_LINEAGE_V1.yaml`
- `specs/HC_QUALIFICATION_EVIDENCE_ISOLATION_V1.yaml`
- `specs/HC_REFERENCE_IDENTITY_INDEX_LINEAGE_V1.yaml`
- `specs/HC_RUNTIME_COMPONENT_CUSTODY_V1.yaml`
- `specs/HC_COMPOSITE_ELEMENT_PROVENANCE_V1.yaml`
- `specs/HC_DISTRIBUTED_LEARNING_ANCESTRY_V1.yaml`
- `specs/HC_EXECUTED_DATAFLOW_BINDING_V1.yaml`
- `specs/HC_EFFECTIVE_TOPOLOGY_TRANSITIONS_V1.yaml`
- `specs/CROSS_REPO_SOURCE_TRANSFER_V1.yaml`

The conformance extension is canonical rather than an untracked addendum; the older baseline has not yet been mechanically consolidated into one monolithic file because preserving reviewable source history is preferable to rewriting a large baseline during active research.

## Qualification records

- `docs/qualification/ARCHITECTURE_CONFORMANCE_2026-09-09.md` — first Warden architecture-conformance cut; `CONDITIONAL PASS` for its stated snapshot/scope because live repository About metadata remains identity-specific and stale.
- `docs/qualification/AFFECT_HOMEOSTASIS_CONFORMANCE_2026-09-09.md` — focused affect/homeostasis cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/MEMORY_PROVIDER_BOUNDARY_2026-09-09.md` — focused provider/memory cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/BOOTSTRAP_RECOVERY_CONFORMANCE_2026-09-09_R2.md` — current bootstrap/recovery cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/PROTECTED_UPDATE_GOVERNANCE_2026-09-09.md` — protected-update cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/EVIDENCE_LINEAGE_CUSTODY_CONFORMANCE_2026-09-09.md` — historical first evidence-lineage/custody cut; `CONDITIONAL PASS` for its exact target.
- `docs/qualification/EVIDENCE_LINEAGE_CUSTODY_CONFORMANCE_2026-09-09_R2.md` — expanded Warden check through `HC-ARCH-025`; `CONDITIONAL PASS` for `main@2f21f111212a438c61e31214caf8aa5bc918a3a5`. Later strategy-path refinements do not inherit this result.
- `docs/qualification/EFFECTIVE_TOPOLOGY_CONFORMANCE_2026-09-09.md` — focused effective-topology state/transition architecture cut; `CONDITIONAL PASS` for `main@21a194908b8005103927af7706a50d769f4fedf5`, pending independent Four/Vera review and implementation-level negative tests.

Qualification records are historical evidence bound to their explicit target commits. Later commits do not inherit or retroactively change a result.

## Top-level subsystem folders

The top-level subsystem folders are the brain architecture. They are not grouped under a `brain/` or `nodes/` wrapper:

- `Empathy/`
- `cognition/`
- `sexuality/`
- `self identity/`
- `psychological behaviors/`
- `sociological behaviors/`
- `semantics/`
- `pragmatics/`
- `phoenetics/`
- `somatics/`
- `chronology/`
- `personification/`
- `current memory storage/`
- `deep memory storage/`
- `volitions-conations/`
- `resolver/`
- `basic operating instructions/`
- `kinesis/`
- `adaptable I-O handler/`
- `optics/`
- `speech recognition & synthesis/`
- `routing instructions with neuroplasticity/`
- `homeostasis-interoception/`
- `salience-attention/`
- `affect/`
- `integration-arbitration/`

## Mature focused subsystem contracts

Current `main` includes, among others:

- `Empathy/SELF_OTHER_MODELING.md`
- `adaptable I-O handler/BODY_INTERFACE_BOUNDARY.md`
- `adaptable I-O handler/SENSOR_AND_CAPABILITY_ADMISSION.md`
- `affect/AFFECTIVE_STATE_AND_MODULATION.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md`
- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
- `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `basic operating instructions/RUNTIME_INVARIANTS.md`
- `chronology/TEMPORAL_EVENT_CONTRACT.md`
- `cognition/EPISTEMIC_COGNITIVE_CONTROL.md`
- `cognition/PERCEPTION_AND_MULTIMODAL_INFERENCE.md`
- `cognition/WORLD_MODEL_AND_PREDICTION.md`
- `cognition/IMAGINATION_SIMULATION_AND_COUNTERFACTUALS.md`
- `cognition/METACOGNITIVE_MONITORING.md`
- `cognition/TEMPORAL_FORECAST_LINEAGE.md`
- `cognition/RELATIONAL_REASONING_AND_GRAPH_PRIORS.md`
- `cognition/RELATIONAL_REASONING_PROVENANCE.md`
- `current memory storage/ARCHITECTURE.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `current memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `deep memory storage/ARCHITECTURE.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `homeostasis-interoception/REGULATORY_CONTROL_AND_INTEROCEPTIVE_EVIDENCE.md`
- `integration-arbitration/DISTRIBUTED_ARBITRATION.md`
- `integration-arbitration/NOOPLEX_FABRIC.md`
- `kinesis/ACTION_GATEWAY.md`
- `optics/ARCHITECTURE.md`
- `personification/SOCIAL_PRESENTATION_CONTROL.md`
- `phoenetics/PHONETIC_EVIDENCE_CONTRACT.md`
- `pragmatics/CROSS_REPO_PRAGMATIC_RUNTIME.md`
- `psychological behaviors/ARCHITECTURE.md`
- `psychological behaviors/LEARNED_BEHAVIOR_ARCHITECTURE.md`
- `resolver/ARCHITECTURE.md`
- `resolver/CONFLICT_AND_RECONCILIATION.md`
- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`
- `salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `semantics/CROSS_REPO_SEMANTIC_RUNTIME.md`
- `sexuality/AGENCY_AND_EMBODIED_AFFECT.md`
- `sociological behaviors/ARCHITECTURE.md`
- `sociological behaviors/SOCIAL_MODELING_ARCHITECTURE.md`
- `somatics/BODY_STATE_AND_BODY_SCHEMA.md`
- `speech recognition & synthesis/ARCHITECTURE.md`
- `volitions-conations/CONATIVE_STATE_MACHINE.md`

## Current coordinated research program

`docs/research/BASIRA_COORDINATED_SCOUR_WORKPLAN_2026-09-09.md` partitions the active graph/connectome deep scour between Noah and Four while preserving deliberate independent overlap for expensive conclusions.

Noah's primary lane covers temporal forecasting, generated/aligned/registered representations, relational reasoning, evidence isolation, distributed-learning ancestry, executed-dataflow integrity, effective-topology semantics, and canonical transfer adjudication. Four's primary lane covers multigraph/hypergraph implementation semantics, flow-control/compression, federation/model-graph self-analysis, uncertainty/explainability, and independent falsification of selected Noah findings.

Recent source-specific research records include:

- HCAE / GNN network-neuroscience intake and computational hypergraph study;
- Nilearn connectivity-estimator semantics and brainGraph diagnostic/null-model patterns;
- BASIRA RegGNN, DGN, GSR-Net, BGSR-PY, GRN, SG-Net, EvoGraphNet, DynGNN, 4D-FED-GNN, 4D-FedGNN-Plus, UMC, MSRGNN, RepFL, DeltaGNN, DuoGNN, FALCON/CQSIGN, uGNN, FireGNN, GLGExplainer, and related organization-wide scouring;
- `BASIRA_DGN_HOLDOUT_ISOLATION_AND_TEMPLATE_LEARNING_2026-09-09.md` — source-specific test/selection isolation finding;
- `BASIRA_BGSR_EXEMPLAR_SYNTHESIS_AND_INDEX_LINEAGE_2026-09-09.md` — exemplar synthesis and cross-view index-lineage hazard;
- `BASIRA_GSRNET_REGISTERED_RUNTIME_AND_SUPERRESOLUTION_2026-09-09.md` — runtime submodule registration/state-custody and fixed-dimension hazards;
- `BASIRA_DYNGNN_DYNAMIC_MEMORY_CUSTODY_2026-09-09.md` — registered-owner versus dynamically assigned causal-state custody, inference-time fitting, and model-memory terminology;
- `BASIRA_GRN_COMPOSITE_TEMPLATE_AND_ELEMENT_PROVENANCE_2026-09-09.md` — edge-wise mosaic-template provenance;
- `BASIRA_HADA_TRANSDUCTIVE_EVALUATION_AND_POSITIONAL_TRACE_2026-09-09.md` — transductive evaluation semantics and test-position trace;
- `BASIRA_UMC_CORRESPONDENCE_AND_COMMON_TEMPLATE_2026-09-09.md` — hard/soft correspondence and common-template semantics;
- `BASIRA_MSRGNN_RELATIONAL_REASONING_2026-09-09.md` — computational graph priors, candidate-conditioned relations, correlated multi-scale views, and attention/gating semantics;
- `BASIRA_TEMPORAL_FORECAST_LINEAGE_2026-09-09.md` — cascaded forecast ancestry and correction semantics;
- `BASIRA_4D_FED_GNN_DISTRIBUTED_LEARNING_2026-09-09.md` — parameter/evidence ancestry, weight aggregation/exchange, missing-timepoint semantics, protected-update boundaries, evaluation-feedback contamination, and configured-versus-executed strategy-path verification;
- `BASIRA_REPFL_REPLICA_ANCESTRY_AND_TARGET_DATAFLOW_2026-09-09.md` — correlated replica ancestry, target-binding/dataflow verification, and effective aggregation-weight evidence;
- `BASIRA_DELTAGNN_EFFECTIVE_TOPOLOGY_AND_FLOW_CONTROL_2026-09-09.md` — task-local effective topology, topology-lifetime separation, and flow-control execution-path evidence.

Source research does not become HC canon merely because it is recorded. The active cadence is:

`SOURCE READ -> RESEARCH RECORD -> TRANSFER HYPOTHESIS -> ADVERSARIAL CHECK -> CANONICAL PROMOTION/REJECTION -> CONFORMANCE TEST`

## Preserved noncanonical material

- `research/hyperconnectome-evidence-v1` — evidence/research layer; evidence input, not parallel architecture owner.
- `research/nooplex-hc3-architecture-v1` — preserved closed-PR #2 source branch; useful lineage/engineering material selectively reconciled.
- `research/hc-1r-reference-architecture` — more ambitious HC-1R redesign research; not canonical replacement for HC-1.
- `research/hyperconnectome-foundations-20260909` — preserved closed-PR #4 research/foundation branch; compatible material selectively remapped.
- `thebrazenbeard-patch-1` — source-intake branch represented by open PR #1; setting-specific physiology remains noncanonical unless generalized and separately justified.

`vera/research-hyperconnectome-evidence-v1` is stale historical residue unless it acquires unique current work.

## Pull-request status

- PR #1 — open source-intake/reference bundle; retained pending final PDF classification/disposition.
- PR #2 — **closed as superseded, not merged** after complete file-by-file reconciliation; source history preserved.
- PR #3 — closed as superseded after compatible runtime material was selectively integrated.
- PR #4 — closed as superseded after selective integration; not merged wholesale.

All HC PRs #1–#4 have Bus mirror/history records under `projects/hc-brain/pr-mirrors/` in `project/hc-brain-v1`.

## Governing distinctions

1. `main` is canonical; branch or PR existence does not make content canonical.
2. The HC is the complete synthetic cognitive organ; no essential cognition belongs outside its boundary.
3. One HC may span multiple physical enclosures; cognitive ownership, not location, determines membership.
4. `REQUIRED_FOR_OPERATION != COGNITIVE_AUTHORITY`.
5. `HYPERCONNECTOME != ALL_TO_ALL_WIRING`.
6. The HC is a typed, attributed, multilayer temporal hypergraph; physical reachability, learned logical eligibility, configured routing, one-execution effective relations, and active hyperedges/coalitions remain distinct.
7. The base architecture is complete while an instance may be immature, dormant, degraded, unimplemented, or quarantined.
8. Presence, activation, maturity, health, implementation status, learning policy, and authorization are orthogonal.
9. Perception, interpretation, evidence, prediction, simulation, salience, memory, desire, consent, and effect authority remain distinct.
10. Affect/homeostatic pressure can modulate cognition without becoming truth, consent, identity, or unrestricted authority.
11. Essential continuity-bearing state cannot exist solely in a true external provider.
12. A true external computational peripheral must be ablatable without uniquely removing an essential cognitive function; otherwise it belongs inside the HC boundary.
13. HC-1 is complete; HC-2 adds specialized acceleration; HC-3 adds richer distributed physiological affective substrate.
14. `DEGRADED_HC2 != HC1` and `DEGRADED_HC3 != HC2`.
15. Human neuroscience informs mechanisms and constraints but does not dictate human gross anatomy or hemispheric decomposition.
16. Personification does not independently own social action authority; sexuality does not turn desire into consent/authorization.
17. Ordinary plasticity, maintenance reachability, source prestige, artifact integrity, emergency access, and local self-test do not confer protected-update authority.
18. Rollback is a governed state transition and cannot silently erase valid continuity-bearing history.
19. `STATISTICAL_CONNECTIVITY != PHYSICAL_REACHABILITY`; generated, aligned, predicted, super-resolved, and population-template topology remain typed evidence.
20. `REASONING_GRAPH_PRIOR != INFERRED_WORLD_RELATION`; a computational route or hyperedge does not become a world fact merely by being used for reasoning.
21. Candidate-conditioned representations retain candidate scope; attention/gating and route strength do not become truth, causality, explanation, consent, authority, or claim confidence by default.
22. `FORECAST_OF_FORECAST != FORECAST_FROM_OBSERVED_STATE`; descendant forecasts retain ancestor provenance and correction dependencies.
23. `POSITIONAL_INDEX != STABLE_ENTITY_ID`; filtering, sorting, batching, pooling, or body enumeration require explicit referential lineage.
24. `COMPOSITE_REPRESENTATION != OBSERVED_INSTANCE`; individually supported elements do not establish a jointly supported configuration.
25. `CALLED_IN_FORWARD != MANAGED_BY_LIFECYCLE`; registered owners can still contain unregistered dynamic causal state, and inference-like calls can mutate learning state.
26. Model/recurrent/reservoir `memory` terminology does not confer HC current-memory, deep-memory, or autobiographical-continuity semantics.
27. Evidence used for tuning/repair/selection cannot remain an untouched independent holdout for the shaped successor.
28. `TRANSDUCTIVE_RESULT != INDUCTIVE_GENERALIZATION_EVIDENCE`; evaluation regime and test-time information visibility are qualification provenance.
29. `RECEIVED_MODEL_UPDATE != OBSERVED_REMOTE_DATA`; parameter ancestry and observation ancestry are separate.
30. Post-aggregation models are not automatically independent corroborators; contributor count does not erase shared parameter ancestry.
31. `MISSING_TIMEPOINT != OBSERVED_NO_CHANGE`; self-encoding or predicted bridging is generated/training structure, not an observation of temporal stasis.
32. Aggregation eligibility, contributor strength, central coordination, or global-model status do not confer protected-update, semantic, or executive authority.
33. `CONFIGURED_STRATEGY != EXECUTED_STRATEGY_WITHOUT_PATH_VERIFICATION`; configuration/feature selection must be traced to the material effect path when the distinction matters.
34. `DECLARED_INPUT != EXECUTED_INPUT_WITHOUT_PATH_VERIFICATION`; signatures, shapes, available authority/memory records, and plausible outputs do not prove correct target/referent/state consumption.
35. `TASK_LOCAL_EFFECTIVE_TOPOLOGY != DURABLE_LOGICAL_TOPOLOGY`; one execution may filter, generate, inhibit, or recruit relations without rewriting learned structure.
36. `EFFECTIVE_TOPOLOGY != WORLD_MODEL_RELATION`, `EFFECTIVE_TOPOLOGY != SALIENCE`, and `EFFECTIVE_TOPOLOGY != AUTHORITY`; computational use does not promote those semantics.
37. Architecture conformance, implementation conformance, behavioral qualification, scientific validation, consciousness, personhood, and manufacturability remain separate claims.
38. Qualification is target-, capability-, scope-, evidence-, and snapshot-bound.
39. Repository-tree conformance does not guarantee repository-surface conformance.

## Current debt and active work

The live GitHub About description remains recorded as `Vera's conceptual Noöplex hyperconnetome brain`, which is identity-specific, stale, and misspelled. Current Warden tooling can read but has not demonstrated metadata-write capability, so this remains an explicit MATERIAL surface defect rather than a falsely claimed fix.

PR #1's binary PDF still requires content-complete classification before final disposition.

Four's active branch is `four/lineage-and-conformance-v2`; it should be refreshed only after verifying it has no unique commits or after reconciling any unique work. Four has current coordinated BASIRA/falsification tasks through the HC Bus. Vera is the hostile-review lane and should attack current executed-dataflow, replica-ancestry, dynamic-state, effective-topology, and distributed-learning cuts as they become review targets.

Main remains under active Warden integration. Compatible identity-neutral material may be committed directly after review; material redesigns, unsupported scientific claims, and alternate root taxonomies remain noncanonical until explicitly adjudicated.
