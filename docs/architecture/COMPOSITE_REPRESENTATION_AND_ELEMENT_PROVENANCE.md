# Composite Representation and Element Provenance

Status: canonical architecture contract.

## Purpose

HC representations can be assembled from multiple observations, memories, templates, generated candidates, modalities, timepoints, or source agents. A fused representation may be useful without ever having existed as one jointly observed state.

Object-level provenance alone is sometimes too coarse. When joint occurrence, compatibility, chronology, authority, or causal interpretation matters, the HC must preserve enough element- or region-level ancestry to prevent a synthetic composite from masquerading as a coherent observation.

## Core separations

`COMPOSITE_REPRESENTATION != OBSERVED_INSTANCE`

`OBJECT_LEVEL_SOURCE_SET != ELEMENT_LEVEL_ANCESTRY`

`ELEMENT_SELECTED_FROM_SOURCE != COMPOSITE_IS_THAT_SOURCE`

`COMMON_FEATURE != UNIVERSAL_FEATURE`

`MOSAIC_REPRESENTATION != COHERENT_OBSERVED_STATE`

`INDIVIDUALLY_SUPPORTED_ELEMENTS != JOINTLY_SUPPORTED_CONFIGURATION`

`FUSED_COMPATIBILITY != OBSERVED_COOCCURRENCE`

## Granularity rule

Provenance should be retained at the coarsest granularity that still supports every material downstream question.

Examples:

- whole-object provenance is sufficient when all material claims apply uniformly to one source event;
- region/edge/field provenance is required when different portions descend from different sources and downstream reasoning may rely on their joint origin;
- clause/claim provenance is required when a semantic summary combines independently sourced propositions;
- temporal-segment provenance is required when a state trajectory splices observed, imputed, forecast, and reconstructed intervals;
- authority provenance is required per governed field/effect when different grants cover different scopes.

The architecture does not require scalar-level lineage for every internal activation. Provenance cost should be proportional to consequence and to the risk of false joint-evidence inference.

## Composite object

A consequential composite may expose:

```text
COMPOSITE_REPRESENTATION {
  representation_id
  source_set[]
  construction_method
  element_or_region_lineage[]
  joint_observation_status
  compatibility_status
  chronology_scope
  uncertainty
  currentness
  transform_or_model_version
  qualification_scope
  provenance
}
```

`joint_observation_status` can distinguish cases such as `JOINTLY_OBSERVED`, `COMPOSED_FROM_MULTIPLE_OBSERVATIONS`, `GENERATED`, `MIXED`, or `UNKNOWN`.

## Temporal composites

A trajectory containing observed t0, imputed t1, forecast t2, and reconstructed t3 is one useful working object but not one uniform evidence class.

Downstream systems must be able to recover which intervals/relations are observed versus derived.

`ONE_TRAJECTORY_OBJECT != ONE_EPISTEMIC_ORIGIN`

Corrections to an ancestor segment should invalidate or re-evaluate dependent composite descendants without erasing historical provenance.

## Graph and hypergraph composites

A population graph/template may contain edges selected, averaged, generated, aligned, or fused from different source graphs.

Such a template may be a valid reference representation while failing to correspond to any one observed graph.

For the HC temporal hypergraph, higher-order relations must not be inferred merely because individually sourced pairwise elements coexist in one fused template.

`PAIRWISE_ELEMENTS_FROM_DIFFERENT_SOURCES != JOINT_HYPEREDGE_EVIDENCE`

A fused graph can support a candidate relation or prior without establishing that all included relations co-occurred in one cognitive/world state.

## Semantic and memory composites

Summaries, person models, autobiographical syntheses, and world-model objects frequently combine evidence across time and source.

The HC should preserve enough claim-level ancestry to distinguish:

- same-event co-occurrence;
- repeated but separate observations;
- mutually incompatible historical states;
- source disagreement;
- corrected/superseded claims;
- generated interpolation or inference.

A fluent summary must not erase those distinctions when they are material.

## Authority and consent composites

Authority and consent cannot be composited by unioning unrelated fragments into a broader grant than any source authorized.

`GRANT_A_FOR_SCOPE_X + GRANT_B_FOR_SCOPE_Y != UNIVERSAL_GRANT`

A composite state should retain scope boundaries and expiry/currentness per source grant.

## Qualification tests

Useful negative tests include:

- build a template whose edges come from different source instances and verify it is not labeled observed-instance evidence;
- compose two individually observed relations that were never jointly observed and verify no joint hyperedge is inferred without separate support;
- combine attributes from incompatible timepoints and verify chronology/currentness conflict remains visible;
- summarize conflicting source claims and verify minority/dissent provenance survives;
- correct one source element and verify dependent composite regions are marked stale/recomputed;
- merge permissions from separate scopes and verify no broader authority is synthesized;
- feed a downstream reasoner a composite and verify it can query whether a claimed conjunction was jointly observed.

## Failure modes

- population CBT/template treated as if it were a real individual instance;
- multi-source summary presented as one witness statement;
- fused graph edges imply a higher-order relation that no source supports jointly;
- person model combines context-specific traits into an asserted simultaneous state;
- mixed observed/forecast trajectory loses per-segment epistemic origin;
- composite permission object silently unions unrelated grants;
- a correction changes one source but stale derived elements remain current because only whole-object provenance was stored.

## Governing invariant

> **A composite may be useful without being jointly observed. HC provenance must remain fine-grained enough that combining supported parts cannot silently create unsupported joint evidence, coherence, currentness, or authority.**

## Provenance

Generalized from HC evidence, temporal-hypergraph, representation-alignment, memory, authority, and correction contracts and reinforced by code-level study of BASIRA GRN `netNorm`, whose connectional brain template may select different graph edges from different source subjects. See `docs/research/BASIRA_GRN_COMPOSITE_TEMPLATE_AND_ELEMENT_PROVENANCE_2026-09-09.md`.
