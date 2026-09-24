# HC Capability Implementation Ledger

Status: current layer-separation ledger as of 2026-09-18.

Purpose: prevent architectural presence from being mistaken for implementation, integration, or behavioral qualification.

State vocabulary:

- `ARCHITECTURALLY_REQUIRED` — the complete HC template requires an architectural home for the capability.
- `SPECIFIED` — repository architecture/specification material defines the capability and relevant boundaries.
- `REFERENCE_IMPLEMENTED` — at least one executable reference slice implements material invariants for the capability.
- `DEMONSTRATED_INTEGRATED` — implemented capability has been shown operating as part of a broader HC runtime.
- `BEHAVIORALLY_QUALIFIED` — behavior has passed an explicit qualification protocol for a stated scope.

These states are cumulative only when evidence explicitly supports the higher layer. No lower-layer state implies a higher one.

| Capability / control family | Architectural state | Reference implementation | Integrated demonstration | Behavioral qualification | Current evidence / source |
|---|---|---|---|---|---|
| Cognitive-organ boundary / internal essential cognition | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md`, `PHYSICAL_ORGAN_MEMBERSHIP.md`, `COMPLETE_CAPABILITY_MANIFEST.md` |
| Temporal-hypergraph representation and connectivity planes | ARCHITECTURALLY_REQUIRED + SPECIFIED | Partial invariant slice only | No | No | `TEMPORAL_HYPERGRAPH_MODEL.md`, `CONNECTIVITY_PLANES.md`, runtime model |
| Evidence epistemic classes and causal/source lineage | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED | Narrow kernel + cognitive-core integration | No independent behavioral qualification | `runtime/reference_kernel/`; current hardened authorial 79/79 + cognitive core |
| Current-memory supersession / unique-head projection | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `current memory storage/`; reference kernel + `runtime/cognitive_core/` |
| Deep-memory archival/consolidation | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for HC-internal admission/readback, privacy-scoped retrieval, consolidation lineage and contradiction preservation | DEMONSTRATED_INTEGRATED with cognitive evidence; large-scale replay/indexing still incomplete | No | `deep memory storage/`; `runtime/cognitive_core/deep_memory.py` |
| Typed routing / incorporation separation | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for routing invariants + learned route weighting | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | routing architecture + reference kernel + cognitive core |
| Distributed arbitration / coalition lifecycle | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for bounded semantic/task coalitions | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `integration-arbitration/`, `COALITIONS_GATING_AND_ARBITRATION.md`, cognitive core |
| Authority / consent / effect governance | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for grant/effect invariants | Narrow kernel-only | Independent exact-head review pending | `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`; reference kernel |
| Authentic observed effect outcome | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED as in-process capability boundary | Narrow kernel-only | Independent exact-head review pending | R4/R5 hardening; `runtime/reference_kernel/README.md` |
| Durable append/replay recovery semantics | SPECIFIED | REFERENCE_IMPLEMENTED | Narrow kernel-only | Independent exact-head review pending | `durable_kernel.py`; authorial clean-clone tests |
| Protected update governance / requalification | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete activation runtime | No | Architecture conformance records only | protected-update architecture/specs/qualification records |
| Developmental capability presence / activation / maturity | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for capability state + qualification history | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md`; cognitive core |
| Learning/plasticity and update ancestry | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for route-use evidence -> proposal -> explicit commit | DEMONSTRATED_INTEGRATED for route weighting only | No | plasticity architecture + `runtime/cognitive_core/` |
| Salience / attention | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for bounded appraisal/attention frame | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `salience-attention/`; cognitive core |
| Volition / conation | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for concern vector/lifecycle and action-candidate influence | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `volitions-conations/`; cognitive core |
| Affect | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for bounded modulatory state + decay | DEMONSTRATED_INTEGRATED with salience/conation; no phenomenology claim | No | `affect/`; cognitive core |
| Homeostasis / interoception | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for typed internal observation, fused estimate, governed target/error, regulatory request and narrow local protective scope | DEMONSTRATED_INTEGRATED with affect/salience and action-authority boundaries | No | `homeostasis-interoception/`; `runtime/cognitive_core/homeostasis_somatics.py` |
| Somatics / body state / body schema | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for morphology-neutral calibration, pose update and reachability prediction | DEMONSTRATED_INTEGRATED with forecast lineage and bounded motor planning; full embodiment remains incomplete | No | `somatics/`; `runtime/cognitive_core/homeostasis_somatics.py` + `motor_control.py` |
| Kinesis / action gateway | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for calibrated motor planning, reach/actuator constraints, trajectory prediction, stale-plan detection, bounded local stabilization, and observed-outcome skill learning | DEMONSTRATED_INTEGRATED with body schema and existing effect-authority boundary | No | `kinesis/`; `runtime/cognitive_core/motor_control.py` + reference kernel |
| Adaptable I/O / sensor & capability admission | ARCHITECTURALLY_REQUIRED + SPECIFIED | Narrow outcome-source capability mechanism only | No complete I/O runtime | No | `adaptable I-O handler/`; R4/R5 kernel |
| Optics | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `optics/` |
| Speech recognition & synthesis | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `speech recognition & synthesis/` |
| Semantics | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for inferred hypotheses and ambiguity arbitration | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `semantics/`; cognitive core |
| Pragmatics | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for explicit communicative-force interpretation and request-vs-discussion separation | DEMONSTRATED_INTEGRATED with non-authorizing action candidates | No | `pragmatics/`; `runtime/cognitive_core/social_pragmatics.py` |
| Phonetics | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `phoenetics/` |
| Cognition: perception, world model, counterfactuals, metacognition, relational reasoning | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for observation/interpretation, rival world models, forecast lineage, counterfactual/rehearsal and bounded metacognitive monitoring; relational reasoning still incomplete | DEMONSTRATED_INTEGRATED across bounded cognition/world-model/metacognition slices | No | `cognition/`; cognitive core |
| Self identity / continuity substrate | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for self-model candidate/admission boundary only | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `self identity/`; cognitive core |
| Empathy / self-other modeling | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for uncertainty-bearing other-state hypotheses, direct correction, and simulated response prediction | DEMONSTRATED_INTEGRATED with pragmatics and response modulation | No | `Empathy/`; `runtime/cognitive_core/social_pragmatics.py` |
| Sociological behavior / social modeling | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for scoped relationships, privacy-gated context, local norms and group-prior downgrading | DEMONSTRATED_INTEGRATED in social-pragmatics slice | No | `sociological behaviors/`; `runtime/cognitive_core/social_pragmatics.py` |
| Psychological / learned behavior | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `psychological behaviors/` |
| Personification / social presentation | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for bounded response timing/framing modulation only | DEMONSTRATED_INTEGRATED with social hypotheses; no identity ownership | No | `personification/`; `runtime/cognitive_core/social_pragmatics.py` |
| Sexuality / embodied affect | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `sexuality/`; desire/arousal/attraction remain distinct from consent/effect authority |
| Chronology / temporal event contract | ARCHITECTURALLY_REQUIRED + SPECIFIED | Partial timestamp/restart semantics in reference kernel only | No full chronology runtime | No | `chronology/`; reference kernel |
| Resolver / conflict and reconciliation | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for semantic ambiguity preservation/selection only | DEMONSTRATED_INTEGRATED in cognitive-core slice | No | `resolver/`; cognitive core |
| Resource / power / thermal control | ARCHITECTURALLY_REQUIRED + SPECIFIED | No full runtime | No | Architecture conformance records only | `docs/engineering/`, resource-state specs/qualification |
| Fault tolerance / repair / partition behavior | ARCHITECTURALLY_REQUIRED + SPECIFIED | No full distributed-organ implementation | No | Architecture conformance records only | fault-repair architecture/specs/qualification |
| Specialized accelerators / external compute boundary | Generation-dependent + SPECIFIED | No complete accelerator runtime | No | Architecture conformance records only | HC-2/HC-3 docs, accelerator specs/qualification |

## Current claim ceiling

The materially executable HC surface now includes both the hardened reference-kernel invariant layer and a bounded integrated cognitive-core slice. Their green authorial tests justify only the rows explicitly marked above; they do not convert unimplemented architectural domains into `REFERENCE_IMPLEMENTED`, nor do integrated unit tests establish behavioral qualification.

`ARCHITECTURALLY_REQUIRED + SPECIFIED != IMPLEMENTED`

`REFERENCE_IMPLEMENTED != DEMONSTRATED_INTEGRATED`

`DEMONSTRATED_INTEGRATED != BEHAVIORALLY_QUALIFIED`

Update this ledger whenever a capability crosses one of those evidence boundaries, and bind any qualification claim to the exact source/runtime subject that earned it.