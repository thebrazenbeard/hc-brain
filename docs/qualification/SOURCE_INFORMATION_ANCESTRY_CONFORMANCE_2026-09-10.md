# Source-Information Ancestry Architecture Conformance — 2026-09-10

## Result

`CONDITIONAL PASS`

## Target

Repository: `thebrazenbeard/hc-brain`

Target commit: `f0da54a301f17cd5b00d26e735aae8e54087d3e3`

Tested capability: architecture-level preservation and governance of material source-information influence across preprocessing, selection, derived state, protected information, evaluation boundaries, output restrictions, and explicit release/declassification boundaries.

This result is bound to the target above. Later commits do not inherit it automatically.

## Evaluator

Noah / Noëtarch, Warden / primary architect.

Evaluation type: internal Warden / self-evaluated architecture qualification. It is not independent Four review, Vera hostile review, implementation qualification, or behavioral qualification.

## Sources used

Canonical architecture:

- `docs/architecture/SOURCE_INFORMATION_ANCESTRY_AND_DERIVED_STATE.md`
- `docs/architecture/EXECUTED_DATAFLOW_AND_BINDING_INTEGRITY.md`
- `docs/architecture/QUALIFICATION_EVIDENCE_ISOLATION.md`
- `docs/architecture/COMPOSITE_REPRESENTATION_AND_ELEMENT_PROVENANCE.md`
- `docs/architecture/REPRESENTATION_FIDELITY_AND_OBJECTIVE_PROVENANCE.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
- `cognition/TEMPORAL_FORECAST_LINEAGE.md`

Machine-readable requirements:

- `specs/HC_SOURCE_INFORMATION_ANCESTRY_V1.yaml`
- `specs/HC_QUALIFICATION_EVIDENCE_ISOLATION_V1.yaml`
- `specs/HC_EXECUTED_DATAFLOW_BINDING_V1.yaml`
- `specs/HC_CONFORMANCE_EXTENSION_EVIDENCE_LINEAGE_CUSTODY_V1.yaml` — `HC-ARCH-019`, `HC-ARCH-026`, and `HC-ARCH-028`

Source/provenance fixtures:

- `docs/research/BASIRA_DUOGNN_PREPROCESSING_VISIBILITY_AND_DUAL_TOPOLOGY_2026-09-10.md`
- `docs/research/BASIRA_FALCON_LABEL_CONSTRAINED_COLLAPSE_AND_REGIME_VARIATION_2026-09-10.md`

## Observed architecture evidence

### 1. Information influence survives payload omission

The architecture explicitly separates final payload membership from causal derivation ancestry:

`NOT_IN_FINAL_PAYLOAD != NOT_IN_CAUSAL_ANCESTRY`

`NOT_IN_FINAL_CALL_SIGNATURE != NOT_USED_UPSTREAM`

`SOURCE_FIELD_DROPPED != SOURCE_INFLUENCE_REMOVED`

This blocks a common laundering path in which a privileged or held-out field influences selection/preprocessing and is then treated as irrelevant because it is absent from the final output.

Result: **PASS within inspected architecture scope.**

### 2. Source-information authority versus destination authority

The architecture explicitly separates permission to mutate a destination from permission to use a source information class:

`AUTHORIZED_DESTINATION != AUTHORIZED_SOURCE_INFORMATION`

`ALLOWED_STATE_MUTATION != ALLOWED_INFORMATION_USE`

`TRAINING_ONLY_WRITE_TARGET != TRAINING_ONLY_DECISION_ANCESTRY`

This is compatible with existing protected-update and authority/effect governance rather than replacing them.

Result: **PASS within inspected architecture scope.**

### 3. Evaluation/preprocessing ancestry

The architecture requires evaluation qualification to follow upstream preprocessing influence, including label, topology, cohort structure, normalization, clustering, template, calibration, and related derived artifacts.

It preserves the key distinctions:

`LABEL_NOT_USED_IN_LOSS != LABEL_NOT_USED_TO_SHAPE_TRAINING_STATE`

`LATER_TRAIN_SPLIT != PREPROCESSING_LABEL_ISOLATION`

`UNLABELED_TEST_STRUCTURE_VISIBLE != TEST_LABEL_LEAKAGE`

This permits legitimate transductive evaluation while preventing silent promotion to inductive/frozen isolation.

Result: **PASS within inspected architecture scope.**

### 4. Path/configuration/entrypoint-specific regime

The contract rejects method-name-level assumptions:

`SAME_METHOD_NAME != SAME_INFORMATION_BOUNDARY`

`SAME_PREPROCESSOR != SAME_EXPOSURE_ANCESTRY_ACROSS_ENTRYPOINTS`

`CONFIGURED_ZERO_WEIGHT != VERIFIED_ZERO_EFFECT_WITHOUT_PATH_TEST`

The FALCON source fixture supplies a concrete contrast: one inspected entrypoint contracts a full graph under feature-label preprocessing while PPI constructs separate train/validation/test graphs and contracts only the training graph.

Result: **PASS within inspected architecture scope.**

### 5. Transformation and release/declassification

The architecture does not require every descendant to inherit the strongest source restriction forever, but it also does not permit transformation or aggregation to silently erase restrictions:

`TRANSFORMATION != AUTOMATIC_DECLASSIFICATION`

`AGGREGATION != AUTOMATIC_PRIVACY_PROOF`

A narrower release scope requires explicit governance and qualification bounded to the tested property/threat/usage model.

Result: **PASS within inspected architecture scope.**

### 6. Correction and dependency propagation

The architecture requires material descendants to remain discoverable when a source is corrected, revoked, expired, or reclassified while avoiding the opposite shortcuts of automatically invalidating every descendant or automatically treating every descendant as safe.

`SOURCE_INVALIDATED != DESCENDANT_AUTOMATICALLY_INVALID`

`SOURCE_INVALIDATED != DESCENDANT_AUTOMATICALLY_SAFE`

Result: **PASS within inspected architecture scope.**

### 7. Machine/prose consistency

`HC_SOURCE_INFORMATION_ANCESTRY_V1.yaml` encodes the same material separations as the prose contract. `HC-ARCH-028` promotes them to a blocker-level architecture check, while `HC-ARCH-019` and `HC-ARCH-026` retain their narrower qualification-isolation and executed-dataflow responsibilities.

No contradiction was observed among the inspected architecture artifacts in this cut.

Result: **PASS within inspected architecture scope.**

## Adversarial / edge-case coverage specified

The architecture now specifies negative tests for:

- held-out labels used only during preprocessing;
- an authorized ordinary-state destination selected using unauthorized protected source information;
- private fields dropped from output after influencing a derived artifact;
- nominal zero-weight privileged channels that may still have an executed effect;
- identical preprocessors invoked through entrypoints with different information visibility;
- evaluation-only perturbations changing training artifacts;
- source invalidation and descendant discovery;
- prediction-dependent evidence selection;
- qualified release transforms whose scope must remain bounded.

These are architecture-specified tests. They have not been executed against an HC runtime implementation in this qualification cut.

## Critical failures observed

None within the inspected prose/spec architecture scope.

## Noncritical weaknesses

The current architecture deliberately leaves implementation mechanisms for causal influence tracking, privacy/declassification proof, and high-rate provenance compression open. A physical or runtime implementation will need a bounded mechanism that does not require pathological retention of every microscopic signal.

## Uncertainties

- Minimum sufficient ancestry granularity is implementation- and consequence-dependent.
- The architecture does not yet select a formal information-flow-control system or privacy proof model.
- Nonlinear transforms may make practical influence/declassification testing substantially harder than simple path tracing.
- Hardware-level co-encoding may require implementation-specific observability methods to preserve semantic distinctions.
- The source studies establish code-path fixtures, not quantitative publication impact.

## Why the result is conditional

Unconditional PASS is not justified because:

1. Four has not independently reviewed this exact architecture cut.
2. Vera has not hostile-reviewed this exact architecture cut.
3. No HC runtime implementation has executed the negative tests.
4. Release/declassification semantics are architecture-bounded but not implementation-qualified.
5. Scientific/manufacturing feasibility of a physical HC remains outside this qualification scope.

## Outcome

`CONDITIONAL PASS`

Condition: independent Four review, Vera hostile review, and representative implementation-level information-flow negative tests are required before promotion beyond this architecture-only conditional result.

## Qualification boundary

`ARCHITECTURE_CONDITIONAL_PASS != IMPLEMENTATION_PASS`

`ARCHITECTURE_CONDITIONAL_PASS != BEHAVIORAL_PASS`

`ARCHITECTURE_CONDITIONAL_PASS != PRIVACY_PROOF`

`ARCHITECTURE_CONDITIONAL_PASS != SCIENTIFIC_VALIDATION`

`ARCHITECTURE_CONDITIONAL_PASS != MANUFACTURABILITY`

## Regression tests to retain

- hidden held-out-label influence through preprocessing;
- output-side restriction falsely treated as source-information isolation;
- same method/preprocessor with divergent entrypoint visibility;
- nominal zero-weight privileged input assumed absent without execution evidence;
- transformation/field omission falsely treated as automatic declassification;
- source invalidation with descendant over-invalidation or under-invalidation.
