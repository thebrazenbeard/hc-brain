# HC Brain — Current State

This is the repository entrypoint for currentness, not a replacement for canonical architecture documents.

For architecture and source layout, read `docs/REPOSITORY_MAP.md`.

## Canonical implementation state

Canonical `main` now contains the hardened reference-kernel lineage plus the first integrated executable cognitive core.

Exact implementation baseline promoted on 2026-09-18:

`272e3406dfce5001fc547e1a9ad20eb00f22a32a`

That baseline includes the closed R3/R4/R5/V2 hardening work and `runtime/cognitive_core/`.

This `CURRENT.md` may live on a later documentation-only descendant; use the implementation commit above when an exact executable baseline is required.

## Current executable evidence

Fresh local verification immediately before promotion:

- hardened reference kernel: **79/79 PASS**;
- architecture-conformance suite: **29/29 PASS**;
- integrated cognitive core: **53/53 PASS** (18 integrated-loop + 8 world-model + 8 deep-memory + 7 metacognition + 12 homeostasis/somatics);
- Python compilation: PASS;
- `git diff --check`: PASS.

The cognitive core is documented in:

- `runtime/cognitive_core/README.md`
- `docs/runtime/EXECUTABLE_COGNITIVE_CORE_STATUS_2026-09-18.md`
- `docs/runtime/CAPABILITY_IMPLEMENTATION_LEDGER.md`
- `docs/runtime/REFERENCE_KERNEL_IMPLEMENTATION_STATUS.md`

## What is executable now

Material reference implementation exists for:

- evidence classes, provenance, durable replay, authority/effect boundaries;
- current-memory projection and correction;
- semantic interpretation and ambiguity preservation;
- rival world models, forecast lineage and observation reconciliation;
- counterfactual simulation and action rehearsal with explicit simulated provenance;
- HC-internal deep-memory durability, privacy-scoped retrieval, consolidation and contradiction preservation;
- metacognitive monitoring of uncertainty, conflict, stale evidence, strategy failure and resource exhaustion;
- typed homeostatic/interoceptive sensing, fused estimates, regulatory targets/errors and bounded requests;
- narrowly scoped local protective control;
- morphology-neutral body-schema calibration, pose update and reachability prediction;
- regulatory-error coupling into affect/salience without epistemic promotion;
- body-schema prediction lineage carried into world-model forecasts;
- salience/attention appraisal;
- affective modulation and decay;
- conative concern lifecycle;
- transient coalition formation and expiry;
- current-memory integration;
- explicit deep-memory admission boundary;
- self-model candidate/admission boundary;
- action-candidate generation without authority bypass;
- route-use plasticity proposals and explicit consolidation;
- learned route weighting;
- developmental capability presence/activation/maturity state.

## Remaining high-value frontier

The largest remaining architecture-to-runtime gaps are:

1. learned relational/causal model discovery and richer multimodal perception;
2. large-scale associative memory indexing and bounded replay scheduling;
3. richer allostatic adaptation and motor/body-schema calibration beyond the bounded reference slice;
4. empathy/social modelling and pragmatics;
5. kinesis/embodiment integration;
6. distributed multi-process Noöplex execution;
7. resource/fault management for a physical distributed organ;
8. behavioral qualification beyond unit/integration tests.

## Review and claim ceiling

The integrated V2 lineage did not receive a materially independent exact-head PASS visible in the currently verified coordination state before source promotion.

Its source integration therefore does not become an independent qualification claim.

`AUTHORIAL_AND_UNIT_PASS != INDEPENDENT_REVIEW_PASS`

`REFERENCE_COGNITIVE_SLICE != COMPLETE_COGNITIVE_ORGAN`

`INTEGRATED_UNIT_TESTS != BEHAVIORAL_QUALIFICATION`

`BEHAVIORAL_QUALIFICATION != GENERAL_INTELLIGENCE`

`ANY_IMPLEMENTATION_PASS != CONSCIOUSNESS_OR_PERSONHOOD_PROOF`
