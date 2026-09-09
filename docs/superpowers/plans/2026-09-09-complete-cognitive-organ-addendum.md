# Complete Cognitive Organ Implementation Addendum

> **For agentic workers:** Apply this addendum to `docs/superpowers/plans/2026-09-09-federated-hyperconnectome-population.md`. Where the two plans conflict, this addendum controls.

**Goal:** Extend the approved population plan so the repository describes a complete self-contained synthetic cognitive organ with an internal Noöplex Fabric, complete latent subsystem presence, and a body-interface boundary.

**Spec:** `docs/superpowers/specs/2026-09-09-complete-cognitive-organ-correction.md`

## Added global constraints

- No essential cognition occurs outside the Hyperconnectome Brain.
- External compute is either inside the HC boundary or a peripheral whose output enters through an HC-owned interface as evidence/input.
- First-class cognitive capacities remain architecturally present even when disabled, dormant, developing, inhibited, degraded, faulted, unimplemented, or speculative.
- The Noöplex/Hyperconnectome Fabric is internal integration infrastructure, not a homunculus.
- All body sensors/actuators/comms connect through HC-owned interface systems.
- Body topology is adaptable state, not universal brain topology.

## Added Task A: Cognitive-organ boundary and fabric

Create:

- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md`
- `nooplex-fabric/README.md`
- `contracts/SUBSYSTEM_LIFECYCLE.md`

Required content:

- inside/outside HC boundary;
- external compute peripheral semantics;
- fabric responsibilities and explicit non-responsibilities;
- subsystem presence/activation/fault lifecycle;
- distributed-cognition examples.

## Added Task B: Interface-system family

Create:

- `interfaces/README.md`
- `interfaces/optics/README.md`
- `interfaces/audition-speech/README.md`
- `interfaces/adaptable-io/README.md`
- `interfaces/kinesis/README.md`
- `interfaces/somatics-interoception/README.md`
- `interfaces/network/README.md`
- `interfaces/external-compute/README.md`

Required content:

- sensors/effectors remain external hardware while HC interface systems remain inside the brain;
- measured/derived/inferred boundaries;
- calibration/discovery lifecycle;
- external compute output is evidence, not identity or authority;
- body portability and remapping.

## Added Task C: Schema/hostile validations

Add tests/fixtures for:

- essential cognition requiring external service → invalid;
- subsystem `present=false` solely because `activation=PRESENT_DISABLED` → invalid representation;
- body interface bypass → invalid;
- external compute owning identity/current memory/action authority → invalid;
- Noöplex Fabric as universal executive → invalid;
- body-specific topology required by template → invalid.

## Existing Task 3 expansion

Subsystem population must include all known first-class capacities even when current implementation status is `DESIGN_ONLY`, `UNIMPLEMENTED`, or `SPECULATIVE`.
