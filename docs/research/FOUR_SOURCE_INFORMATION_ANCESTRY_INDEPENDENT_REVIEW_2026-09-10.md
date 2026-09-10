# Four Independent Review — Source-Information Ancestry — 2026-09-10

Status: independent secondary architecture review; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen target: `main@f0da54a301f17cd5b00d26e735aae8e54087d3e3`
- Review role: Four / Documentation-Specification Owner / independent secondary reviewer
- Primary check: `HC-ARCH-028` source-information ancestry and derived state
- Warden qualification record reviewed separately: `docs/qualification/SOURCE_INFORMATION_ANCESTRY_CONFORMANCE_2026-09-10.md`

This review is architecture-scoped. It does not establish implementation conformance, behavioral qualification, privacy/noninference proof, scientific validation, manufacturability, consciousness, personhood, or blanket qualification of later repository state.

## Outcome

**SECONDARY PASS WITH IMPLEMENTATION-SEMANTICS ADVISORIES.**

No BLOCKER contradiction was observed in the frozen target's named source-information-ancestry surfaces.

The reviewed architecture consistently preserves the distinction among:

- final payload membership;
- upstream source visibility;
- actual material source influence;
- destination mutation authority;
- source-information-use authority;
- evaluation/qualification exposure;
- transformed/derived-state provenance;
- release/declassification scope;
- correction/revocation dependency propagation.

Four's independent-review condition is therefore satisfied for the frozen target above.

## Findings

### 1. Payload omission versus causal ancestry

**PASS.**

The prose and machine contract both reject the laundering shortcut that an input stops mattering merely because it is absent from a later call signature or final payload:

`NOT_IN_FINAL_PAYLOAD != NOT_IN_CAUSAL_ANCESTRY`

`NOT_IN_FINAL_CALL_SIGNATURE != NOT_USED_UPSTREAM`

`SOURCE_FIELD_DROPPED != SOURCE_INFLUENCE_REMOVED`

This is consistent with the executed-dataflow contract, which traces both referential lineage and the information visibility/transforms that shaped the object actually consumed.

### 2. Destination authority versus source-information authority

**PASS.**

The contract correctly separates permission to mutate a destination from permission to use a source information class when selecting, shaping, gating, or deriving that mutation.

`AUTHORIZED_DESTINATION != AUTHORIZED_SOURCE_INFORMATION`

`ALLOWED_STATE_MUTATION != ALLOWED_INFORMATION_USE`

This does not replace the existing authority/effect or protected-update contracts. It closes an indirect-use gap inside them: a legal destination cannot sanitize an illegal or out-of-scope decision ancestry.

### 3. Evaluation/preprocessing ancestry

**PASS.**

The source-information contract, qualification-evidence isolation, and executed-dataflow contract agree that the earliest material preprocessing influence defines the exposure boundary. A later split does not retroactively make an earlier full-cohort artifact train-only.

The architecture also preserves the narrower distinction that unlabeled evaluation structure may create a transductive regime without constituting label leakage or automatic invalidity.

That is the correct semantic boundary: exposure changes the supported qualification claim; it does not automatically invalidate the method.

### 4. Path/configuration/entrypoint specificity

**PASS.**

The architecture rejects method-name-level and configuration-intent shortcuts:

`SAME_METHOD_NAME != SAME_INFORMATION_BOUNDARY`

`SAME_PREPROCESSOR != SAME_EXPOSURE_ANCESTRY_ACROSS_ENTRYPOINTS`

`CONFIGURED_ZERO_WEIGHT != VERIFIED_ZERO_EFFECT_WITHOUT_PATH_TEST`

This is important because the FALCON source fixture supplies materially different Cora and PPI visibility paths while invoking the same general contraction mechanism.

### 5. Transformation and declassification/release

**PASS at architecture level; implementation advisory retained.**

The contract avoids both bad extremes. It does not require every descendant forever to inherit the strongest source restriction, but it does not allow transformation, aggregation, or field redaction to erase restrictions automatically.

`TRANSFORMATION != AUTOMATIC_DECLASSIFICATION`

`AGGREGATION != AUTOMATIC_PRIVACY_PROOF`

The remaining implementation burden is substantial: a narrower release scope requires a qualified property/threat/usage model, and the architecture intentionally does not select one formal information-flow-control or privacy/noninference proof system.

That is not an architecture contradiction. It is an implementation qualification frontier.

### 6. Visibility versus material influence

**PASS with materiality-definition advisory.**

The prose distinguishes what information was visible from whether it materially influenced selection, weighting, topology, thresholds, routing, fitting, or content. This distinction is necessary: mere path availability and actual causal contribution are not identical.

However, a runtime implementation will need a bounded, consequence-proportional criterion for `material influence`. Otherwise the system can fail in either direction:

- undercapture — an indirect nonlinear/stochastic influence is dismissed because no field was copied directly; or
- pathological overcapture — every reachable source is retained forever as if it materially shaped every descendant.

The current architecture already points toward perturbation, path tracing, taint/provenance labels, and execution evidence. Future implementation qualification should make the chosen materiality criterion explicit and preserve `UNKNOWN` when influence cannot be established.

This is an implementation-semantics advisory, not a blocker in the present architecture cut.

### 7. Correction, revocation, and descendant reevaluation

**PASS.**

The contract correctly rejects both automatic descendant invalidation and automatic descendant safety after an upstream source is corrected, revoked, expired, or reclassified.

`SOURCE_INVALIDATED != DESCENDANT_AUTOMATICALLY_INVALID`

`SOURCE_INVALIDATED != DESCENDANT_AUTOMATICALLY_SAFE`

Historical ancestry remains history; current eligibility is a separate decision. The implementation requirement is to retain enough dependency structure to discover materially affected descendants without rewriting history.

### 8. Source-transfer reasoning

**PASS.**

The DuoGNN and FALCON records are used as bounded code-level fixtures rather than HC primitives or publication-level judgments.

DuoGNN supports the narrower rule that full-cohort structural preprocessing can influence a later training topology before the declared split, while explicitly avoiding an unsupported test-label-leakage claim.

FALCON supplies the stronger feature-label preprocessing fixture and, importantly, a same-repository counterexample: the inspected Cora and PPI entrypoints expose different information boundaries. The architecture therefore generalizes to path-specific ancestry rather than source-wide condemnation.

### 9. Machine/prose consistency

**PASS.**

`HC_SOURCE_INFORMATION_ANCESTRY_V1`, `HC-ARCH-028`, qualification-evidence isolation, and executed-dataflow/binding integrity encode compatible responsibilities.

One difference is intentional scope compression: `HC-ARCH-028` carries the blocker-level summary assertions while the dedicated `IA-*` contract contains the fuller release, correction, privileged-source, and descendant-discovery rules. I do not classify that as semantic divergence because the conformance check explicitly cites the dedicated machine contract.

## Currentness note

This independent review is bound to `f0da54a301f17cd5b00d26e735aae8e54087d3e3`.

Observed current `main` during review: `bcbaf6fcb4ad34be2007444a62ca05883354ca8d`.

A commit comparison from the frozen target to that observed main shows two later commits affecting only qualification/index documentation: `docs/qualification/SOURCE_INFORMATION_ANCESTRY_CONFORMANCE_2026-09-10.md` and `docs/qualification/README.md`. No architecture/spec file changed after the frozen target in that comparison.

That supports the statement that the reviewed architecture content was unchanged across that interval. It does **not** convert the frozen-target review into automatic current-main qualification; qualification remains snapshot- and evidence-bound.

## Disposition

For the exact target:

`HC-ARCH-028 => SECONDARY_ARCHITECTURE_PASS`

with ceilings:

- `SECONDARY_ARCHITECTURE_PASS != IMPLEMENTATION_PASS`
- `SECONDARY_ARCHITECTURE_PASS != VERA_HOSTILE_REVIEW_PASS`
- `SOURCE_ANCESTRY_TRACKING != FORMAL_PRIVACY_OR_NONINFERENCE_PROOF`
- `SOURCE_VISIBLE != SOURCE_MATERIALLY_INFLUENTIAL`
- `SOURCE_PATH_EXISTS != PROVEN_CAUSAL_EFFECT`
- `FROZEN_TARGET_PASS != AUTOMATIC_CURRENT_MAIN_PASS`

No canonical repair is required from this review.

The next concrete implementation frontier is an executable information-flow/ancestry harness that can discriminate direct visibility, actual path consumption, material influence, release-boundary qualification, and correction-dependent descendant discovery without requiring pathological retention of every microscopic signal.
