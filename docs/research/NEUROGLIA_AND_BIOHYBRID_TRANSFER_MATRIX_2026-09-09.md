# Neuroglia and Biohybrid Transfer Matrix — 2026-09-09

Status: research disposition / noncanonical architecture input.

## Purpose

This matrix converts the neuroglia/biohybrid evidence review into explicit transfer decisions for the generic Hyperconnectome Brain template.

It is intentionally conservative. The question is not merely “does biology contain this mechanism?” but:

> **How well is the claim supported, and separately, what may the generic HC architecture learn from it without copying human anatomy or overclaiming feasibility?**

## Independent axes

### Epistemic status

Uses canonical HC evidence vocabulary:

- `DOCUMENTED`
- `OBSERVED`
- `USER-STATED`
- `INFERRED`
- `HYPOTHESIS`
- `DISPUTED`
- `UNKNOWN`

### Transfer disposition

- `GENERIC_CONSTRAINT` — substrate-neutral design/engineering lesson;
- `BIOHYBRID_PROFILE_ONLY` — applies only to deliberate biological/biohybrid implementations;
- `RESEARCH_EVIDENCE_ONLY` — preserve as scientific context, not direct architecture;
- `DO_NOT_PROMOTE` — biological packaging/claim should not become generic HC architecture;
- `OPEN_RESEARCH` — potentially relevant but insufficiently demonstrated for stronger transfer.

`EPISTEMIC_STATUS != TRANSFER_DISPOSITION`

`DOCUMENTED != UNIVERSAL_HC_REQUIREMENT`

## Matrix

| Evidence/mechanism | Epistemic status | Transfer disposition | Generic HC consequence | Biohybrid-specific consequence | Explicit non-transfer |
|---|---|---|---|---|---|
| Modular/selective biological connectivity and network-cost constraints | `DOCUMENTED` biologically; generic consequence `INFERRED` | `GENERIC_CONSTRAINT` | Hyperconnectivity means reachable integration and dynamic coalition formation, not permanent all-to-all links | Long-range biological tracts should be selectively provisioned | Do not copy human connectome geometry |
| Communication latency and resource cost | `DOCUMENTED` biologically/physically | `GENERIC_CONSTRAINT` | Links/routes carry latency, bandwidth, reliability, synchronization and resource cost | Axonal path length/myelination contribute to those costs | Do not assume biological delay ranges for nonbiological substrates |
| Oligodendrocyte myelination | `DOCUMENTED` biologically | `BIOHYBRID_PROFILE_ONLY` + narrow `GENERIC_CONSTRAINT` abstraction | Physical communication timing/support may be plastic | Track myelin/insulation, axonal support, conduction delay, repair state | Oligodendrocytes are not mandatory generic HC nodes |
| Activity-dependent/adaptive myelination | `DOCUMENTED` for activity responsiveness; exact system-level rules remain partly `UNKNOWN` | `BIOHYBRID_PROFILE_ONLY` + narrow `GENERIC_CONSTRAINT` | Effective timing/plasticity may include physical-link properties | Activity/experience may alter myelin and conduction behavior | Do not equate myelin plasticity with the HC universal routing algorithm |
| Oligodendrocyte metabolic support of axons | `DOCUMENTED` biologically | `BIOHYBRID_PROFILE_ONLY` + generic support principle | Compute/communication substrates expose support dependencies | Track metabolic/support-cell health and axonal viability | Do not require vertebrate white matter |
| Astrocyte–neuron metabolic coupling | `DOCUMENTED` biologically | `BIOHYBRID_PROFILE_ONLY` + generic support principle | Physical compute substrate exposes resource/support dependencies | Track metabolic homeostasis, substrate delivery, waste handling, support-cell state | Do not invent mandatory `astrocyte` cognitive subsystem |
| Neural signaling energy cost | `DOCUMENTED` biologically; HC abstraction `INFERRED` | `GENERIC_CONSTRAINT` | Cognition/routing/plasticity are not resource-free; resource cost is explicit state | Biological firing/synaptic cost participates in viability model | Do not infer generic HC wattage target |
| Heat generation and removal | `DOCUMENTED` physical constraint | `GENERIC_CONSTRAINT` | Power/thermal architecture is part of whole-organ feasibility | Perfusion/microfluidics may be required by wet tissue | Do not require biological circulation for nonbiological HC builds |
| Organoid developmental/cellular modeling | `DOCUMENTED` as a current experimental platform with bounded scope | `RESEARCH_EVIDENCE_ONLY` | Present organoids do not validate complete-HC feasibility | Useful platform for specific developmental/circuit questions | Do not call current organoids complete brains or mature HC substrates |
| Organoid/assembloid perfusion/vascularization and support limits | `DOCUMENTED` as material research constraints | `BIOHYBRID_PROFILE_ONLY` / `OPEN_RESEARCH` for HC scale | Complete biohybrid viability claims require demonstrated support | Perfusion/vascularization or alternative nutrient/waste system must be explicit | Do not assume scale-up is solved |
| Incomplete/variable organoid neuronal and glial maturity | `DOCUMENTED` as a current modeling limitation | `BIOHYBRID_PROFILE_ONLY` | Maturation becomes an implementation evidence dimension | Define developmental/maturation/qualification state | Do not infer adult-like cognition from morphology alone |
| Missing or incomplete meaningful sensory/physiological input in many in-vitro models | `DOCUMENTED` for model limitations; general HC developmental implication `INFERRED` | `GENERIC_CONSTRAINT` at developmental level + `BIOHYBRID_PROFILE_ONLY` | Claimed grounded development needs interaction/evidence channels appropriate to capability | Biohybrid maturation should include structured sensory/embodied coupling | Do not equate spontaneous activity with grounded cognition |
| PEDOT:PSS and flexible conductive neural interfaces | `DOCUMENTED` component-level research; HC-scale capability `UNKNOWN` | `RESEARCH_EVIDENCE_ONLY` / `BIOHYBRID_PROFILE_ONLY` | Interface results remain measured/derived evidence, not cognition | Candidate material family for flexible local read/write interfaces | Do not claim complete-brain chronic interface is solved |
| Distributed electro-optical neural interfacing | Component mechanisms `DOCUMENTED`; complete-HC integration `UNKNOWN` | `OPEN_RESEARCH` | Interfaces declare bandwidth, precision, invasiveness, drift and evidence class | Candidate biohybrid interface stack | Do not claim lossless neural/digital state translation |
| Adaptive conduction timing | Biological route `DOCUMENTED`; universal synthetic method `UNKNOWN` | `GENERIC_CONSTRAINT` at abstraction + `BIOHYBRID_PROFILE_ONLY` implementation | Temporal-hypergraph relations may carry plastic timing state where substrate permits | Myelin can be one physical realization | Do not require one global synchronization scheme |
| Glial/support failure affecting cognition | `DOCUMENTED` biologically; generic fault transfer `INFERRED` | `GENERIC_CONSTRAINT` at support/fault level + `BIOHYBRID_PROFILE_ONLY` | Substrate-support failures remain visible in health/degradation state | Support-cell/perfusion failure becomes physical HC fault | Do not classify all glial processes as cognitive nodes |
| Adult human gross neuroanatomical regions | `DOCUMENTED` human anatomy | `DO_NOT_PROMOTE` as generic topology | Functional lessons may inform responsibilities | A deliberately human-like biohybrid build may choose analogues | No hemispheres, corpus-callosum requirement, or mandatory named-region nodes |
| Human hemispheric specialization | `DOCUMENTED` for humans at various scopes | `DO_NOT_PROMOTE` as HC topology | Functional specialization may exist without bilateral architectural decomposition | None required | `HUMAN_ANATOMICAL_LOCALIZATION != HC_TOPOLOGY_REQUIREMENT` |
| Consciousness/identity transfer into neural tissue | `UNKNOWN` / not established | `DO_NOT_PROMOTE` as scientific fact | None | May remain separately labeled speculative hypothesis if relevant elsewhere | Do not use organoid/interface evidence as proof of transfer |
| Whole-brain neuron-by-neuron read/write | `UNKNOWN` / not established at complete-brain scale | `OPEN_RESEARCH` | Interface capability must be evidence-bounded | Future biohybrid profile declares actual read/write scope | Do not assume arbitrary full-state access |

## Generic HC abstractions justified only at the stated claim level

These are conceptual families, not newly canonical machine schemas.

```text
PHYSICAL_LINK_STATE {
  latency
  latency_uncertainty
  bandwidth
  reliability
  resource_cost
  thermal_cost
  support_state
  plasticity_state
  repair_state
}
```

```text
SUBSTRATE_SUPPORT_STATE {
  substrate_ref
  support_domains[]
  resource_state
  thermal_state
  maintenance_state
  degradation_state
  fault_refs[]
  provenance
}
```

```text
INTERFACE_EVIDENCE_STATE {
  interface_ref
  directly_measured_scope
  derived_scope
  inferred_scope
  calibration_state
  drift_state
  precision_or_resolution
  latency
  chronic_stability_evidence
  provenance
}
```

## Candidate future biohybrid substrate profile

A biohybrid implementation could eventually bind evidence using a profile such as:

```text
BIOHYBRID_NEUROGLIAL_PROFILE {
  build_or_substrate_id
  neural_cell_classes[]
  glial_support_classes[]
  tissue_maturation_state
  perfusion_or_metabolic_support
  physical_connection_classes[]
  conduction_delay_model
  adaptive_insulation_or_timing_model
  interface_classes[]
  read_scope
  write_scope
  repair_and_turnover_model
  resource_and_thermal_model
  chronic_stability_evidence
  developmental_training_state
  qualification_state
  provenance
}
```

This profile remains implementation-specific unless/until a concrete biohybrid HC program requires it.

## Evidence/claim ceilings

This research package alone does not support claims that:

- the complete HC is physically realizable today;
- neural tissue is necessary or sufficient for HC cognition/personhood;
- a scaled organoid constitutes a complete synthetic brain;
- present interfaces enable complete-brain read/write;
- human gross anatomy is required for cognition;
- glial/myelin mechanisms instantiate semantics, identity, or consciousness;
- biological energy/timing values should be copied into nonbiological builds.

## Recommended canonical use

Use this matrix to constrain future:

- biohybrid implementation profiles;
- physical-link timing/resource models;
- power/thermal/resource architecture;
- fault/repair models;
- sensor/interface evidence ceilings;
- developmental/maturation qualification;
- research claims about organoid or biohybrid feasibility.

Do **not** use it to revise the generic functional folder topology into a human anatomical brain map.

## Source binding

Primary preserved internal sources:

- open PR #2 `research/nooplex-hc3-architecture-v1` neurobiology/evidence material;
- `research/hyperconnectome-evidence-v1` neuroscience/connectomics and physical-compute research;
- canonical `main` non-hemispheric temporal-hypergraph and complete-cognitive-organ contracts.

Independent literature verification and corrected bibliography are summarized in `NEUROGLIA_AND_BIOHYBRID_EVIDENCE_2026-09-09.md`.
