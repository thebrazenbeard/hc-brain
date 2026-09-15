# HC Capability Implementation Ledger

Status: current layer-separation ledger as of 2026-09-15.

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
| Evidence epistemic classes and causal/source lineage | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED | Narrow kernel-only | No independent behavioral qualification | `runtime/reference_kernel/`; R5 authorial 64/64 |
| Current-memory supersession / unique-head projection | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED | Narrow kernel-only | No | `current memory storage/`; reference kernel |
| Deep-memory archival/consolidation | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `deep memory storage/` |
| Typed routing / incorporation separation | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for narrow routing invariants | Narrow kernel-only | No | routing architecture + reference kernel |
| Distributed arbitration / coalition lifecycle | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete executable implementation | No | No | `integration-arbitration/`, `COALITIONS_GATING_AND_ARBITRATION.md` |
| Authority / consent / effect governance | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED for grant/effect invariants | Narrow kernel-only | Independent exact-head review pending | `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`; reference kernel |
| Authentic observed effect outcome | ARCHITECTURALLY_REQUIRED + SPECIFIED | REFERENCE_IMPLEMENTED as in-process capability boundary | Narrow kernel-only | Independent exact-head review pending | R4/R5 hardening; `runtime/reference_kernel/README.md` |
| Durable append/replay recovery semantics | SPECIFIED | REFERENCE_IMPLEMENTED | Narrow kernel-only | Independent exact-head review pending | `durable_kernel.py`; authorial clean-clone tests |
| Protected update governance / requalification | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete activation runtime | No | Architecture conformance records only | protected-update architecture/specs/qualification records |
| Learning/plasticity and update ancestry | ARCHITECTURALLY_REQUIRED + SPECIFIED | No general implementation | No | No | plasticity architecture, ancestry specs/research |
| Salience / attention | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `salience-attention/` |
| Volition / conation | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `volitions-conations/` |
| Affect | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `affect/`; focused architecture qualification only |
| Homeostasis / interoception | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `homeostasis-interoception/` |
| Somatics / body state / body schema | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `somatics/` |
| Kinesis / action gateway | ARCHITECTURALLY_REQUIRED + SPECIFIED | Only narrow effect-control invariants in reference kernel | No complete action system | No | `kinesis/`; reference kernel |
| Adaptable I/O / sensor & capability admission | ARCHITECTURALLY_REQUIRED + SPECIFIED | Narrow outcome-source capability mechanism only | No complete I/O runtime | No | `adaptable I-O handler/`; R4/R5 kernel |
| Optics | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `optics/` |
| Speech recognition & synthesis | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `speech recognition & synthesis/` |
| Semantics | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `semantics/` |
| Pragmatics | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `pragmatics/` |
| Phonetics | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `phoenetics/` |
| Cognition: perception, world model, counterfactuals, metacognition, relational reasoning | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete cognition runtime | No | No | `cognition/` |
| Self identity / continuity substrate | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete identity runtime | No | No | `self identity/` |
| Empathy / self-other modeling | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `Empathy/` |
| Sociological behavior / social modeling | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `sociological behaviors/` |
| Psychological / learned behavior | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `psychological behaviors/` |
| Personification / social presentation | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `personification/`; presentation must not silently own volition/action authority |
| Sexuality / embodied affect | ARCHITECTURALLY_REQUIRED + SPECIFIED | No | No | No | `sexuality/`; desire/arousal/attraction remain distinct from consent/effect authority |
| Chronology / temporal event contract | ARCHITECTURALLY_REQUIRED + SPECIFIED | Partial timestamp/restart semantics in reference kernel only | No full chronology runtime | No | `chronology/`; reference kernel |
| Resolver / conflict and reconciliation | ARCHITECTURALLY_REQUIRED + SPECIFIED | No complete implementation | No | No | `resolver/` |
| Resource / power / thermal control | ARCHITECTURALLY_REQUIRED + SPECIFIED | No full runtime | No | Architecture conformance records only | `docs/engineering/`, resource-state specs/qualification |
| Fault tolerance / repair / partition behavior | ARCHITECTURALLY_REQUIRED + SPECIFIED | No full distributed-organ implementation | No | Architecture conformance records only | fault-repair architecture/specs/qualification |
| Specialized accelerators / external compute boundary | Generation-dependent + SPECIFIED | No complete accelerator runtime | No | Architecture conformance records only | HC-2/HC-3 docs, accelerator specs/qualification |

## Current claim ceiling

The only materially executable HC surface in this repository is the narrow reference-kernel invariant slice. Its green authorial tests do not convert the many `SPECIFIED` rows above into `REFERENCE_IMPLEMENTED`, `DEMONSTRATED_INTEGRATED`, or `BEHAVIORALLY_QUALIFIED` states.

`ARCHITECTURALLY_REQUIRED + SPECIFIED != IMPLEMENTED`

`REFERENCE_IMPLEMENTED != DEMONSTRATED_INTEGRATED`

`DEMONSTRATED_INTEGRATED != BEHAVIORALLY_QUALIFIED`

Update this ledger whenever a capability crosses one of those evidence boundaries, and bind any qualification claim to the exact source/runtime subject that earned it.