> **License:** Source-visible, not open source. Original material is proprietary. Private, noncommercial evaluation is permitted under [LICENSE](LICENSE); redistribution, commercial use, and hosted or commercial derivatives require separate written permission. See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md). Third-party material retains its own terms.

# Hyperconnectome Brain (HC)

**An identity-neutral architecture and executable reference toolkit for researching synthetic cognitive systems.**

Hyperconnectome Brain defines the HC-series cognitive-organ model: its subsystems, interfaces, state boundaries, evidence rules, conformance checks, and reference Python implementations. It is useful to system architects, researchers, and developers designing cognitive software with explicit memory, learning, authority, and embodiment boundaries.

**Current status:** The repository contains a substantial *specification* and **two bounded executable reference layers**. It is **not** a complete synthetic brain, autonomous agent, pretrained model, deployable robot controller, or demonstration of consciousness. The physical, distributed-organ requirements are design constraints—not verified manufactured hardware.

## What is available today?

| Reusable component | Current evidence-backed scope | Entry point |
| --- | --- | --- |
| HC-series architecture | Identity-neutral subsystem, cognitive-organ, temporal-hypergraph, embodiment, memory and effect contracts | [Repository map](docs/REPOSITORY_MAP.md) · [Architecture](docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md) |
| Machine-readable conformance specifications | Structural and semantic architecture checks; **not** implementation or behavioral qualification | [Conformance contract](docs/architecture/CONFORMANCE_AND_QUALIFICATION.md) · `specs/` · `tools/validate_hc_architecture.py` |
| Python reference kernel | Narrow provenance, current-memory, routing, grant/effect, immutable-payload and restart/reconciliation invariants | [Reference-kernel guide](runtime/reference_kernel/README.md) |
| Python cognitive core | Bounded integration of semantics, salience, affect, concerns, memory, world-model, metacognition, homeostasis and social-pragmatics slices | [Cognitive-core guide](runtime/cognitive_core/README.md) |
| Capability status and qualification lineage | Explicit distinction among required, specified, implemented, integrated and qualified functionality | [Implementation ledger](docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md) · [Qualification records](docs/qualification/README.md) |

The reference Python components use the standard library. They are exercised directly from the repository checkout; **there is no packaged HC runtime installer**.

## Try the implemented parts

With Python 3 and Git available:

```bash
git clone https://github.com/thebrazenbeard/hc-brain.git
cd hc-brain

# Architecture checks
python3 tools/validate_hc_architecture.py --root .
python3 -m unittest -v tests.test_validate_hc_architecture

# Integrated cognitive-core reference tests
python3 -m unittest -v \
  runtime.cognitive_core.test_cognitive_loop \
  runtime.cognitive_core.test_world_model \
  runtime.cognitive_core.test_deep_memory \
  runtime.cognitive_core.test_metacognition \
  runtime.cognitive_core.test_homeostasis_somatics \
  runtime.cognitive_core.test_social_pragmatics
```

Run the reference-kernel suite from its own folder:

```bash
cd runtime/reference_kernel
python3 -m unittest -v \
  test_hc_kernel.py test_durable_kernel.py \
  test_four_adversarial_kernel.py test_four_adversarial_kernel_r2.py \
  test_vera_adversarial_kernel_v2.py
```

Those commands exercise **reference implementation and architecture tests**, not a full cognitive organism or real-world actuator. The workflows in `.github/workflows/` target these source paths; a README-only change may not trigger those workflows.

## Design contract

The HC project describes the complete *intended* synthetic cognitive organ. It uses a typed, attributed, multilayer **temporal hypergraph** instead of treating a brain as a flat list of modules. Higher-order coalitions, routing, salience, arbitration, plasticity and memory relationships have distinct state and evidence roles. See [Temporal Hypergraph Model](docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md).

The central architectural requirements are:

1. **The organ boundary follows ownership, not enclosure location.** HC-owned computational parts may be physically distributed; external sensors, actuators, cloud models and databases must remain bounded peripherals unless deliberately admitted as HC-owned components. The rule that no essential cognition may be outsourced is a **conformance requirement**, not a claim about deployed hardware. See [Physical Organ Membership](docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md).
2. **Presence does not imply activation or implementation.** A complete architectural template names mandatory capabilities even if a real implementation has them dormant, developing, inhibited or not built. Presence, activation, maturity, health and authorization remain separate axes. See [Complete Capability Manifest](docs/architecture/COMPLETE_CAPABILITY_MANIFEST.md) and [Developmental Initialization](docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md).
3. **Evidence, desire and action authority are not interchangeable.** An observation, inference, prediction, recalled record, attention priority, model recommendation and authorized material effect require different admission rules. Tested in-process grant fixtures and opaque outcome handles are **not** a production, cryptographically bound host authorization service.
4. **Continuity-bearing state must be recoverable from HC-owned storage in a conforming implementation.** External replicas or retrieved context cannot silently become the only source of identity, memory or authoritative current state. The current reference implementation does not prove distributed physical recovery or general privacy-safe declassification.
5. **Development and plasticity are governed changes.** Use of a route, repeated reward or a successful simulation does not automatically promote a learned change, establish truth, transfer consent or grant permissions. See [Plasticity and State Governance](docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md).

The top-level subsystem folders are the architecture's responsibility domains (cognition, memory, empathy, salience, affect, identity, somatics, interfaces and more). Browse the [full folder contract](docs/REPOSITORY_MAP.md), rather than assuming each folder contains an independent runnable service. Identity-specific memories, relationships, personality and other continuity content belong in derivative implementations, not this generic template.

## Evidence and qualification limits

For each capability, ask separately whether it is **specified**, **reference-implemented**, **integrated**, and **behaviorally qualified**. The [capability ledger](docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md) records these distinctions. Existing passing unit tests support bounded Python invariants only; they do not prove general intelligence, conscious experience, complete memory governance, verified provider identity, host-owned immutable authority, safe physical control, scientific validity, or manufacturing feasibility.

The [reference-kernel guide](runtime/reference_kernel/README.md) documents concrete limitations in its current in-process capability handling, replay model and historical hostile test findings. Architectural qualification reports are snapshot-specific and must not be applied to later code or real-world systems without fresh tests.

## Reusing the work

For an authorized private, noncommercial evaluation:

1. Begin with the [repository map](docs/REPOSITORY_MAP.md) and [conformance contract](docs/architecture/CONFORMANCE_AND_QUALIFICATION.md).
2. Run the local checks above to establish an exact source baseline.
3. Choose one bounded subsystem or reference behavior to adapt; preserve the original distinction between data, model inference, authority and effects.
4. Record your implementation subject, tests, limits and provenance. Do not claim a system-wide pass from a passing reference slice.

The repository's [governance roles](WARDEN.md) are project-maintenance roles, **not** identities installed in a derived cognitive system. Reuse and distribution remain subject to [LICENSE](LICENSE).
