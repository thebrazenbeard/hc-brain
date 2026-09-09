# basic operating instructions

Top-level HC subsystem for invariant operating rules, bootstrap behavior, baseline constraints, core process expectations, and foundational execution semantics.

Canonical contracts in this subsystem currently include:

- `ARCHITECTURE.md` — subsystem purpose and cross-cutting operating invariants;
- `RUNTIME_INVARIANTS.md` — compact runtime separations across evidence, memory, affect, authority, routing, embodiment, and effects;
- `CAPABILITY_ACTIVATION_STATES.md` — capability presence/activation semantics;
- `SUBSYSTEM_LIFECYCLE_CONTRACT.md` — orthogonal presence, activation, maturity, health, implementation, authorization, learning, fault, recovery, and requalification state;
- `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md` — scoped authority, consent, revocation, expiry, maintenance boundaries, and effect governance;
- `BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md` — self-contained startup, continuity restoration, crash consistency, safe degradation, stale-authority revalidation, lineage/fork handling, and recovery without external essential cognition;
- `PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md` — protected-state classification, scoped update authority, coherent activation, version-skew handling, continuity-safe rollback/forward repair, and requalification after protected change.

These documents constrain distributed HC behavior. They do not create a central executive, personality, identity payload, or external control plane that becomes the real cognitive organ.

Machine-readable counterparts and conformance checks live under `../specs/`, especially `HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`, `HC_CONFORMANCE_SUITE_V1.yaml`, `HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`, `HC_BOOTSTRAP_RECOVERY_V1.yaml`, and `HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`.
