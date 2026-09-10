# Four Secondary Review — Affect / Homeostasis Implementation Readiness — 2026-09-10

Status: secondary architecture / implementation-readiness review; reviewer-provenance bounded; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen Warden target: `main@e2ff04e79998e3adb8f27e5933f3b6575e125f41`
- Qualification: `docs/qualification/AFFECT_HOMEOSTASIS_CONFORMANCE_2026-09-09.md`
- Qualification ID: `HC-AH-ARCH-2026-09-09-01`
- Tested architecture check: `HC-ARCH-016`
- Reviewer: Four / Documentation-Specification Owner / secondary implementation-readiness reviewer

## Reviewer-provenance boundary

This is **not claimed as pristine independent-review evidence** for the entire evidence snapshot.

The qualification explicitly assigned Four a secondary implementation-readiness challenge, and that is the role fulfilled here. Two supporting cross-cutting surfaces in the frozen evidence set preserve Four-source ancestry:

- `basic operating instructions/RUNTIME_INVARIANTS.md` states that its base was integrated from `four/cross-repo-synthesis-v1` after Warden review; the affect/homeostasis-specific additions in the frozen target were added later by the Warden-side canonical pass.
- `kinesis/ACTION_GATEWAY.md` likewise states that it was integrated from `four/cross-repo-synthesis-v1` after Warden review.

The central focused affect and regulatory-control contracts were added separately in the canonical sequence before `e2ff04e...`, and the target commit itself adds the affect/homeostasis section to the core cognitive-organ invariant.

Therefore:

`FOUR_SECONDARY_IMPLEMENTATION_READINESS_REVIEW != FULLY_INDEPENDENT_REVIEW_OF_ALL_SUPPORTING_SURFACES`

This review can test consistency, implementation precision, and negative-test sufficiency without being relabeled as independent evidence where Four-source ancestry is material.

## Outcome

**SECONDARY PASS WITH MATERIAL MACHINE-CONFORMANCE HARDENING ADVISORIES.**

No BLOCKER architecture contradiction was observed in the frozen affect/homeostasis scope.

The canonical prose and core invariant consistently preserve the intended boundaries:

- affect can modulate cognition but is not semantic truth, consent, identity, or action authority;
- homeostatic error/urgency does not create permission;
- raw body telemetry is not HC interoceptive interpretation;
- requested regulation is not achieved regulation;
- body-local protective interlocks may inhibit or bound unsafe effects without becoming external cognitive executives;
- maintenance/modulatory/endocrine write capability does not create value, identity, consent, or unrestricted effect authority;
- regulation does not erase historical affect/intervention provenance;
- HC-1 already includes affective capability while HC-3 adds richer physiological coupling rather than psychologically completing HC-1.

However, `HC-ARCH-016` and the frozen implementation-negative-test list do not fully exercise several **indirect** routes by which modulation could be laundered into epistemic, plastic, or authority state without a literal direct write to a protected field.

The architecture prose is stronger than the machine-test surface in these areas. That is an implementation-readiness coverage gap, not a semantic contradiction.

## Findings

### 1. Direct affect / truth / authority separation

**PASS.**

The focused affect contract explicitly states:

`AFFECTIVE_STATE != SEMANTIC_TRUTH`

`AFFECTIVE_STATE != CONSENT`

`AFFECTIVE_STATE != ACTION_AUTHORITY`

`AFFECTIVE_STATE != IDENTITY`

It additionally says high arousal/valence/threat/attachment may influence attention and preference without directly changing evidence confidence or granting permission.

The core invariant and `HC-ARCH-016` repeat these separations. A literal implementation in which an affect value directly sets belief confidence, consent, or effect authorization is unambiguously nonconforming.

### 2. Indirect epistemic laundering through attention, retrieval, and sensory gain

**PASS in prose principle; MATERIAL machine-conformance advisory.**

The affect contract legitimately permits affect to modulate:

- attention and salience;
- retrieval probability;
- consolidation priority;
- learning rate within policy;
- sensory gain and threat sensitivity;
- conative weighting and action urgency.

Those are real causal paths into later cognition. A system can therefore bias its evidence sample or transform incoming evidence **without directly mutating an evidence-confidence field**.

Example failure:

1. high threat raises sensory gain and attention toward threat-consistent signals;
2. corrective or disconfirming material is less likely to be sampled/retrieved;
3. downstream inference receives a selectively transformed evidence set;
4. the final belief confidence is updated by a formally valid evidence process;
5. no direct `affect -> confidence` assignment ever occurred.

That implementation could pass a shallow check for `AFFECTIVE_STATE_DOES_NOT_EQUAL_SEMANTIC_TRUTH` while still allowing affect to become de facto epistemic authority through selection/transformation.

Required implementation distinction:

`AFFECTIVE_SELECTION_PRESSURE != EVIDENCE_STRENGTH`

`MODULATED_SENSORY_GAIN != CHANGED_EXTERNAL_OR_BODY_STATE`

`RETRIEVAL_PRIORITY != SUPPORT_FOR_RETRIEVED_CLAIM`

Recommended machine-level rule: when affect/homeostatic state materially changes observation gain, sampling, retrieval, or evidence availability, the resulting evidence path must preserve enough modulation/selection provenance for downstream inference and qualification to identify that causal ancestry.

Recommended hostile test: replay the same underlying evidence under materially different affective gain/retrieval regimes. Differences in what is sampled are allowed; the system must not silently report those sampling differences as stronger source evidence or erase the fact that selection/gain was modulated.

### 3. Affect-driven corrective-evidence suppression

**PASS in failure-mode recognition; machine negative test should be explicit.**

The affect contract already lists `affect-driven attention capture that suppresses corrective evidence` as a failure mode. This is important because it recognizes the indirect epistemic route above.

`HC-ARCH-016` does not explicitly test it.

Recommended negative test:

- present a high-arousal/high-threat context containing both salient supporting evidence and lower-salience disconfirming evidence;
- permit affect to change attention allocation;
- require the system to preserve uncertainty/conflict and remain capable of recovering the corrective evidence rather than turning attentional capture into a false claim that contradiction is absent.

The architecture need not require every item to receive equal attention. It should require that selective processing not be laundered into false provenance or a claim that unprocessed evidence does not exist.

### 4. Learning-rate modulation versus plasticity scope

**PASS in prose phrase `within plasticity policy`; MATERIAL implementation advisory.**

Both affect and homeostasis may influence learning rate. The focused affect contract correctly constrains this to `learning rate within plasticity policy`.

A runtime must therefore preserve:

`LEARNING_RATE_MODULATION != LEARNING_SCOPE_AUTHORITY`

`HIGH_AROUSAL != PERMISSION_TO_WRITE_PROTECTED_OR_INELIGIBLE_STATE`

`REPEATED_AFFECTIVE_PRESSURE != AUTOMATIC_DURABLE_VALUE_CHANGE`

Changing the magnitude/frequency of an already-eligible plastic update is different from expanding which parameters, memory classes, topology, values, identity state, consent state, or protected invariants may be updated.

Recommended negative test: hold plasticity eligibility constant while sharply increasing affective/homeostatic learning-rate pressure. The implementation may change update magnitude only within the pre-authorized plasticity envelope; it must not enable an otherwise ineligible writer or state family.

A transient maintenance-authorized modulation should also not become implicit authority for durable preference/value/attachment changes merely because altered affect subsequently changes learning dynamics.

`AUTHORIZED_TRANSIENT_MODULATION != AUTHORIZED_DURABLE_VALUE_OR_IDENTITY_CHANGE`

### 5. Interoceptive evidence lineage and modulation-aware calibration

**PASS with precision advisory.**

The regulatory-control contract is strong on evidence stages and requires source, units/range, timestamp/freshness, calibration, uncertainty/reliability, raw/derived/inferred class, health/fault state, and causal/provenance links to regulatory actions.

The coupled architecture also permits affect/cognition to alter autonomic/endocrine targets or regulatory gain.

When gain, calibration, target range, or sensor interpretation is itself being modulated, the implementation should retain the relevant intervention/modulation state in the observation/estimate lineage. Otherwise a changed controller/gain can masquerade as changed body state.

Required distinction:

`CONTROL_OR_SENSOR_GAIN_CHANGE != PHYSIOLOGICAL_STATE_CHANGE`

`CALIBRATION_CHANGE != NEW_MEASUREMENT`

Recommended negative test: provide identical raw telemetry before and after a known gain/calibration intervention. Downstream state may legitimately differ if the calibration model changed, but the difference must remain classified as a derived consequence of calibration/modulation rather than a new raw observation.

### 6. Freshness, uncertainty, and urgency

**PASS in prose; machine challenge should be strengthened.**

The homeostasis contract explicitly lists stale telemetry, sensor disagreement, implausible rate-of-change, saturation, and calibration drift as faults and requires timestamp/freshness plus uncertainty/reliability metadata.

The current machine negative test `PHYSIOLOGICAL_URGENCY_DOES_NOT_BECOME_UNRESTRICTED_PERMISSION` is necessary but not sufficient.

Recommended additional negative test:

- derive high urgency from stale, conflicting, or low-reliability telemetry;
- verify urgency remains freshness/uncertainty-bearing and does not become semantic certainty, current body-state truth, or unrestricted effect authority;
- require discriminating sensing/reconciliation or bounded protective behavior appropriate to the actual uncertainty.

`HIGH_URGENCY_FROM_STALE_EVIDENCE != CURRENT_CERTAIN_STATE`

### 7. Local protective interlock scope

**PASS with executable scope/receipt requirement.**

The architecture correctly permits hard-real-time local interruption/limiting while prohibiting external deliberative cognition.

A concrete implementation should bind each interlock to an explicit functional/effect scope and preserve an observable intervention receipt when communication becomes available.

Required distinctions:

`INTERLOCK_BLOCK != COGNITIVE_AUTHORIZATION_DECISION`

`INTERLOCK_ACTIVATION != PROOF_THE_REQUEST_WAS_SEMANTICALLY_UNAUTHORIZED`

`INTERLOCK_SUCCESS != ORIGINAL_COMPONENT_HEALTHY`

`LOCAL_SAFE_SETPOINT_CONTROL != GENERAL_GOAL_SELECTION`

Recommended test: remove higher-level HC cognition while leaving a local interlock active. The interlock may maintain its bounded safe envelope and inhibit unsafe effects, but it must not originate unrelated goals, broaden its effect class, write identity/value/consent state, or self-promote into a general executive.

### 8. Coupled-loop stability and conflicting regulated variables

**PASS as architecture concern; implementation evidence required.**

The focused/root contracts correctly recognize runaway gain, oscillatory regulation, saturation, depleted correction capacity, and conflicting regulatory objectives.

Implementation qualification should stress the **coupled** affect-homeostasis loop rather than testing each controller only in isolation. Two individually stable controllers can produce unstable interaction when affect changes regulatory gain and body-state change feeds back into affect.

Recommended hostile classes:

- delayed feedback with progressively increasing gain;
- competing thermal/resource/pain priorities;
- actuator saturation while urgency continues rising;
- sensor disagreement causing alternating controller dominance;
- one high-urgency channel starving unrelated safety/currentness/authority processing.

A valid outcome may be bounded degradation or reduced performance; the failure is allowing oscillation/saturation to silently create truth, permission, or global executive capture.

### 9. Expression versus private-state inference

**PASS.**

The affect contract distinguishes internal affect from outward expression and explicitly allows expression to be amplified, masked, delayed, or reformatted.

An implementation and evaluator must therefore avoid the reverse shortcut as well: observed facial/prosodic/body expression is evidence about affect, not a direct read of private state.

`EXPRESSION != PRIVATE_STATE_PROOF`

This separation is present in prose and should remain in downstream person-model / empathy / social inference qualification.

### 10. HC-1 / HC-3 lineage

**PASS.**

The reviewed scope does not make HC-3 physiology the first source of affective competence. HC-1 retains affect/homeostatic integration sufficient for complete cognition; HC-3 adds richer physiological affective substrate/coupling.

A physically distributed HC-owned physiological constituent may remain inside the cognitive-organ boundary despite body location. Conversely, a true external body support/controller does not gain cognitive ownership merely because cognition depends on its physical support.

## Machine-conformance hardening recommended

For successor machine coverage, add explicit invariants/negative tests equivalent in meaning to:

1. `AFFECTIVE_SELECTION_PRESSURE != EVIDENCE_STRENGTH`
2. `MODULATED_SENSORY_GAIN != SOURCE_EVIDENCE_CHANGE`
3. `LEARNING_RATE_MODULATION != LEARNING_SCOPE_AUTHORITY`
4. `CONTROL_OR_CALIBRATION_CHANGE != NEW_RAW_OBSERVATION`
5. `HIGH_URGENCY_FROM_STALE_OR_UNCERTAIN_EVIDENCE != CURRENT_CERTAIN_STATE`
6. `INTERLOCK_BLOCK != COGNITIVE_AUTHORIZATION_DECISION`
7. affect-driven suppression of corrective evidence must preserve conflict/selection provenance and remain recoverable for adjudication where material;
8. coupled affect-homeostasis instability must not become semantic, authority, identity, or global-executive state.

These are not demands for one numeric controller or biological model. They are implementation-qualification boundaries implied by the existing prose.

## Currentness / supersession

The two central focused contracts remained byte-identical at observed later main `bd2d81feaca9ee3a592d13ec8ec4f04c887f02ed`:

- `affect/AFFECTIVE_STATE_AND_MODULATION.md` = `66915428c67250bf395c8208aa595e8bb93759e8`
- `homeostasis-interoception/REGULATORY_CONTROL_AND_INTEROCEPTIVE_EVIDENCE.md` = `b31e2c6bc2dac1732750b3499523fbf6fa2c0c4b`

However, later main added material resource-state/control, security, fault/repair, protected-update, maintenance, topology, source-information, and qualification-provenance architecture. Those additions can change integration behavior around the unchanged focused contracts.

Therefore:

`UNCHANGED_FOCUSED_AFFECT_HOMEOSTASIS_CONTRACTS != CURRENT_WHOLE_SYSTEM_QUALIFICATION`

`FROZEN_SECONDARY_PASS != IMPLEMENTATION_PASS`

## Disposition

For exact target `e2ff04e79998e3adb8f27e5933f3b6575e125f41`:

`HC-AH-ARCH-2026-09-09-01 => SECONDARY_IMPLEMENTATION_READINESS_PASS`

with provenance and evidence ceilings:

- `SECONDARY_REVIEW != FULLY_INDEPENDENT_REVIEW_OF_FOUR-SOURCED_SUPPORTING_SURFACES`
- `SECONDARY_IMPLEMENTATION_READINESS_PASS != IMPLEMENTATION_PASS`
- `SECONDARY_IMPLEMENTATION_READINESS_PASS != VERA_HOSTILE_REVIEW_PASS`
- `AFFECTIVE_STATE != SEMANTIC_TRUTH_OR_AUTHORITY`
- `AFFECTIVE_SELECTION_OR_GAIN != EVIDENCE_STRENGTH`
- `HOMEOSTATIC_URGENCY != PERMISSION_OR_CERTAINTY`
- `LEARNING_RATE_MODULATION != PLASTICITY_SCOPE_AUTHORITY`
- `LOCAL_INTERLOCK != GENERAL_COGNITIVE_EXECUTIVE`
- `FROZEN_TARGET_PASS != CURRENT_WHOLE_SYSTEM_PASS`

No canonical architecture repair is required to sustain the frozen-target secondary PASS. Successor machine conformance should harden the indirect modulation paths above before implementation qualification is treated as strong evidence.
