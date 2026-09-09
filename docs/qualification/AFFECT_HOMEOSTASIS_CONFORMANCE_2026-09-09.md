# Affect / Homeostasis Architecture Conformance — 2026-09-09

Qualification ID: `HC-AH-ARCH-2026-09-09-01`

Outcome: **CONDITIONAL PASS**

Target kind: canonical architecture snapshot

Target ref: `main@e2ff04e79998e3adb8f27e5933f3b6575e125f41`

Tested capability: separation and governance of affective modulation, homeostatic/interoceptive control, body-local protective interlocks, and their boundaries with truth, consent, identity, authority, and the HC cognitive-organ boundary.

Evaluator: Noah / Noëtarch, Warden

## Test scope

This qualification cut evaluates the architecture-level contracts and machine-readable constraints introduced or materially affected by the affect/homeostasis pass. It does not evaluate a running implementation, biological fidelity, subjective phenomenology, consciousness, manufacturability, or real-world safety performance.

Primary evidence snapshot:

- `affect/AFFECTIVE_STATE_AND_MODULATION.md`
- `homeostasis-interoception/REGULATORY_CONTROL_AND_INTEROCEPTIVE_EVIDENCE.md`
- `affect/ARCHITECTURE.md`
- `homeostasis-interoception/ARCHITECTURE.md`
- `basic operating instructions/RUNTIME_INVARIANTS.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `kinesis/ACTION_GATEWAY.md`
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md`
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`
- `docs/architecture/HC3_NOOPLEX_EQ.md`
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`
- `specs/HC_CONFORMANCE_SUITE_V1.yaml`

## Checks and observed evidence

### AH-01 — Affect is modulatory, not epistemic or executive authority

**PASS within architecture text.**

The canonical contracts explicitly separate affective state from semantic truth, consent, action authority, identity authority, and permanent importance. Affect may influence salience, retrieval, learning within policy, conative weighting, sensory gain, pain gating, social sensitivity, motor readiness, expression, and regulatory targets without directly changing evidence confidence or effect permission.

Relevant invariant families include:

- `AFFECTIVE_STATE != SEMANTIC_TRUTH`
- `AFFECTIVE_STATE != CONSENT`
- `AFFECTIVE_STATE != ACTION_AUTHORITY`
- `AFFECTIVE_STATE != IDENTITY`

### AH-02 — Homeostatic urgency does not silently become permission

**PASS within architecture text.**

The regulatory contract separates raw telemetry, normalized/derived physiological estimates, interoceptive interpretation, homeostatic error, urgency, requested regulation, achieved regulation, and action/effect authority.

Relevant invariant families include:

- `RAW_TELEMETRY != INTEROCEPTIVE_STATE`
- `HOMEOSTATIC_ERROR != ACTION_AUTHORITY`
- `URGENCY != PERMISSION`
- `PAIN != COMMAND`
- `THREAT_SIGNAL != CERTAINTY_OF_THREAT`

### AH-03 — HC retains cognition-facing interoceptive ownership

**PASS within architecture text.**

Body sensors may originate observations and true body peripherals may execute bounded low-level protective functions, but HC owns cognition-facing interpretation, learned homeostatic policy, body-state meaning, affective appraisal, memory, conation, and higher-order regulatory reasoning.

The machine-readable invariant set now explicitly encodes HC ownership of interoceptive interpretation, learned homeostatic policy, and cognition-facing body-state meaning.

### AH-04 — Local protective interlocks do not create an external executive

**PASS within architecture text.**

The regulatory contract permits body-local hard-real-time interlocks to interrupt or limit dangerous effects, hold bounded safe local states, emit telemetry/fault state, and request higher-level regulation. It explicitly prohibits such an interlock from becoming an external deliberative or learned general cognitive controller.

This preserves the cognitive-organ rule while avoiding the opposite error of requiring slow deliberation for every immediate hardware/tissue-protection event.

### AH-05 — Regulation does not erase event/history provenance

**PASS within architecture text.**

The affect contract distinguishes suppression of expression, reduction of intensity, physiological regulation, and attentional regulation from erasure of the historical affective event. The invariant set requires material intervention history and provenance to remain visible.

Relevant distinctions include:

- `SUPPRESSED_EXPRESSION != ABSENT_AFFECT`
- `REGULATED_AFFECT != ERASED_AFFECTIVE_HISTORY`

### AH-06 — Maintenance and endocrine/modulatory writes do not acquire identity/value/consent authority

**PASS within architecture text.**

Maintenance access and technical write capability remain distinct from affective, value, identity, consent, and effect authority. The machine-readable forbidden-shortcut set now rejects modulatory/endocrine write paths that attempt to become identity, value, or consent authority.

### AH-07 — HC-1 / HC-3 generation semantics remain coherent

**PASS within architecture text.**

The affect contract states that HC-1 already includes affective capability while HC-3 adds richer physiological coupling/substrate. This is consistent with the canonical lineage rule that later generations extend a complete HC-1 rather than psychologically completing an otherwise incomplete predecessor.

### AH-08 — Machine-readable conformance coverage

**PASS for declared architecture assertions.**

`HC_CONFORMANCE_SUITE_V1` now contains `HC-ARCH-016` with explicit assertions covering affect/truth/consent/action-authority separation, homeostatic urgency, pain, expression suppression, raw telemetry versus interoceptive interpretation, body-local interlock scope, prohibition of external general homeostatic reasoning, and maintenance-affective authority separation.

The implementation-negative-test list also includes adversarial cases for high arousal, physiological urgency, pain/threat signals, expression suppression, and local body interlock escalation.

## Observed failures

No architecture-text contradiction was identified by the Warden in this bounded pass that requires an immediate FAIL.

This is not evidence that no contradiction exists. The project requires an independent hostile review for material architecture changes, and that review has not yet been incorporated for this exact snapshot.

## Remaining uncertainty

1. **Hostile review pending.** Vera has been assigned adversarial review of the affect/homeostasis cut. A Warden self-check is not a substitute for the required independent hostile-review lane.
2. **Secondary implementation-readiness challenge pending.** Four has been assigned to test whether `HC-ARCH-016` and the focused contracts are sufficiently precise for implementation and whether further machine-readable invariants are needed.
3. **Implementation untested.** No running system has demonstrated that these separations survive concurrency, faults, stale state, adversarial inputs, actuator latency, or high-arousal/high-urgency conditions.
4. **Scientific realization unqualified.** The architecture is research-informed but does not establish that a synthetic implementation can reproduce biological affect, interoception, endocrine regulation, or subjective emotional phenomenology.
5. **Protective-interlock boundary requires implementation evidence.** The architecture describes the allowed scope, but a concrete implementation must demonstrate that local protective mechanisms cannot accumulate learned/deliberative authority or become a hidden external cognition path.

## Outcome rationale

**CONDITIONAL PASS** is appropriate because the canonical architecture now expresses the required separations and contains matching machine-readable assertions/negative tests, but the mandatory hostile-review requirement for this material architecture change has not yet been satisfied for the exact snapshot.

Promotion to `PASS` for this tested capability requires, at minimum, disposition of the hostile-review findings against a current snapshot and confirmation that no unresolved BLOCKER or MATERIAL defect remains within this scope.

This outcome does not alter the repository-wide qualification outcome, implementation status, behavioral qualification, scientific validation, or any claim about consciousness/personhood.

## Provenance

Created by the Warden after the affect/homeostasis focused-contract pass and explicit machine-readable invariant update. The record is snapshot-bound to `e2ff04e79998e3adb8f27e5933f3b6575e125f41` and must not be silently projected onto later commits without re-evaluation.
