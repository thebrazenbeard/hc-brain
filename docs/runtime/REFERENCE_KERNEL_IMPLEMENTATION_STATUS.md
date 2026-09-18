# Reference Kernel Implementation Status

Status: current implementation-status note as of 2026-09-18.

The HC architecture remains broader than the executable runtime. The repository now has two materially executable layers:

1. the hardened invariant/reference kernel under `runtime/reference_kernel/`;
2. the bounded integrated cognitive slice under `runtime/cognitive_core/`.

Neither is a complete HC cognitive organ.

## Hardened reference-kernel scope

The integrated kernel line includes the R3/R4/R5 hardening work plus the V2 successor hardening:

- typed observation versus derived/inferred/predicted evidence;
- causal/source lineage and immutable admitted payloads;
- current-memory supersession and fail-closed ambiguous projection;
- typed routing distinct from incorporation, semantic truth, and authority;
- capability-authenticated authority mutation;
- issuance-jurisdiction policy and reserved provenance;
- authority expiry/revocation/current-epoch enforcement;
- effect-candidate fingerprinting and duplicate/collision controls;
- `REQUESTED != EFFECT_CONFIRMED`;
- authenticated live outcome-source capability boundary;
- durable JSONL hash/sequence replay validation;
- restart epoch fencing and one-event recovery-fence semantics;
- fail-closed replay of malformed/policy-invalid history;
- state-family consistency/partition registry and mechanical evidence bindings;
- exact-head review-receipt validation and architecture-conformance tooling.

## Current executable cognitive scope

The cognitive core adds tested integration for:

- semantic interpretation and ambiguity preservation;
- salience/attention appraisal;
- affective modulation and decay;
- conative concern state/lifecycle;
- bounded transient coalitions;
- current-memory admission and same-scope correction;
- HC-owned deep-memory durability, scoped retrieval, consolidation, and contradiction retention;
- self-model candidate/admission separation;
- action candidate generation without effect authorization;
- route-use evidence -> plasticity candidate -> explicit consolidation;
- learned route weighting affecting later routing;
- developmental capability presence/activation/maturity state;
- rival world models, prediction ancestry, counterfactual rehearsal, and forecast reconciliation;
- bounded metacognitive monitoring;
- typed homeostatic/interoceptive observation, estimation, target/error state, and regulatory request;
- narrow local protective control;
- morphology-neutral body-schema calibration, pose update, and reachability prediction;
- regulatory-to-affect/salience coupling and body-prediction-to-world-model lineage;
- empathy/social hypotheses, direct-correction precedence, scoped relationship privacy, local norms, pragmatic force, and response modulation.

See `docs/runtime/EXECUTABLE_COGNITIVE_CORE_STATUS_2026-09-18.md`.

## Fresh local evidence before promotion

The integration workspace was built by merging the closed V2 branch into current main and then adding the cognitive core with red->green TDD cycles.

Fresh verification on that workspace:

- hardened reference-kernel suite: **79/79 PASS**;
- architecture-conformance suite: **29/29 PASS**;
- cognitive-core suite: **63/63 PASS** (18 integrated-loop + 8 world-model + 8 deep-memory + 7 metacognition + 12 homeostasis/somatics + 10 social/pragmatics);
- combined repository gate: **171 tests, 0 failures**;
- Python compilation: PASS;
- `git diff --check`: PASS.

This is authorial/local evidence for the tested surfaces.

## Review boundary

The earlier R5/V2 review subjects did not receive a materially independent exact-head PASS that is visible in the currently verified Bus state.

Canonical source integration, if performed under repository authority, must therefore not be described as independent qualification.

`AUTHORIAL_AND_UNIT_PASS != INDEPENDENT_REVIEW_PASS`

## Security/engineering boundaries

The live outcome capability remains an in-process possession boundary, not cryptographic process isolation.

The durable journal hash chain is integrity structure, not a signature/MAC against an attacker able to rewrite and consistently rehash an entire semantically valid history.

The cognitive core is in-process and deterministic; it is not yet distributed Noöplex execution.

## Major unimplemented surfaces

The current executable layers do not yet establish:

- rich multimodal perception;
- learned relational/causal model discovery beyond explicit model proposals;
- large-scale associative deep-memory indexing and bounded replay scheduling;
- richer allostatic learning and long-timescale homeostatic dynamics beyond the bounded reference slice;
- motor-control/body-schema calibration beyond reachability prediction;
- richer multi-party social learning and pragmatic/language-generation behavior beyond the bounded social-pragmatics slice;
- full kinesis/embodiment;
- resource/power/thermal runtime;
- distributed multi-constituent fault/recovery behavior;
- general intelligence;
- consciousness, personhood, or biological equivalence.

## Claim ceiling

`REFERENCE_KERNEL != COMPLETE_HC_RUNTIME`

`REFERENCE_COGNITIVE_SLICE != COMPLETE_COGNITIVE_ORGAN`

`INTEGRATED_UNIT_TESTS != BEHAVIORAL_QUALIFICATION`

`BEHAVIORAL_QUALIFICATION != GENERAL_INTELLIGENCE`

`ANY_IMPLEMENTATION_PASS != CONSCIOUSNESS_OR_PERSONHOOD_PROOF`

Historical qualification records remain exact-target evidence and do not automatically transfer to successor source.
