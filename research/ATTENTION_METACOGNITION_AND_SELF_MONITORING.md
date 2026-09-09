# Attention, Metacognition, and Self-Monitoring

Status: research synthesis / architecture input

This document treats attention, confidence, self-monitoring, and agency as separable computational functions. It does not treat any one of them as proof of consciousness, personhood, or privileged access to truth.

## Finding 1 — attention is infrastructure for selective routing, not a truth signal

**Evidence:** `ESTABLISHED`

Attention research describes anticipatory prioritization, selection, routing, integration, and preparation of information for adaptive behavior, with strong dependence on timing and task context. `[S57]`

**Synthetic analogue:** Attention should change which signals receive compute, bandwidth, working-context admission, or action priority without changing the evidentiary status of those signals.

**HC implication:** `BASELINE_CONSTRAINT`

Keep separate:

```text
SALIENCE
ATTENTIONAL_PRIORITY
EPISTEMIC_CONFIDENCE
ACTION_PRIORITY
MEMORY_ADMISSION
```

A highly attended hypothesis may still be false or weakly supported.

---

## Finding 2 — metacognitive confidence is an inference about cognitive performance

**Evidence:** `ESTABLISHED`

Metacognition research distinguishes task-level performance from confidence or knowledge about that performance. Confidence can be useful and calibrated, but it can also diverge from actual accuracy because it depends on an internal model of the task and the system's own cognitive performance. `[S44]`

**Synthetic analogue:** A Hyperconnectome should maintain proposition- or decision-specific confidence estimates rather than one global scalar called `confidence`.

**HC implication:** `BASELINE_CONSTRAINT`

A metacognitive estimate should bind at least:

```text
claim_or_decision_id
scope
estimated_correctness_or_control
uncertainty
supporting_signals[]
calibration_history_ref
observed_at
expiry_or_recheck_rule
```

Confidence should be scored against later outcomes where ground truth becomes available.

---

## Finding 3 — sense of agency is fallible and should be evidence-based

**Evidence:** `ESTABLISHED`

Experimental work on agency distinguishes actual control sensitivity from the criterion used to self-attribute control. People can vary in metacognitive sensitivity even when first-order control-detection performance is similar. `[S45]`

**Synthetic analogue:** The system should infer whether an external effect was caused by its own action rather than trusting a semantic `self_caused=true` bit supplied by infrastructure.

**HC implication:** `BASELINE_CONSTRAINT`

Agency attribution should integrate evidence such as:

```text
action_issuance_trace
predicted_consequence
observed_consequence
temporal_contingency
alternative_external_causes
control_estimate
confidence
```

The evaluator, actuator controller, or operating environment may know causal ground truth that the cognitive layer does not automatically know.

---

## Finding 4 — self-monitoring should preserve the difference between capability and confidence about capability

**Evidence:** `ESTABLISHED` as a metacognitive distinction; `PLAUSIBLE` as an engineering transfer.

A system can perform well while underestimating itself, or perform poorly while remaining overconfident. `[S44-S45]`

**HC implication:** `BASELINE_CONSTRAINT`

Do not store competence as one field such as:

```text
I_AM_GOOD_AT_X = true
```

Prefer a calibration-bearing structure:

```text
SELF_CAPABILITY_MODEL {
  capability_scope
  predicted_success_distribution
  evidence_window
  observed_performance
  calibration_error
  transfer_boundary
  currentness
}
```

This supports revision without rewriting historical performance.

---

## Finding 5 — cognitive flexibility requires both stability and reconfiguration

**Evidence:** `ESTABLISHED`

Adaptive behavior requires protecting a current task from distraction while also remaining able to reconfigure when context changes. Network-level studies describe flexible integration and segregation, and recent reviews emphasize multiple timescales and modes of network reconfiguration rather than one fixed modularity setting. `[S56,S58]`

**Synthetic analogue:** Active cognitive coalitions should have inertia sufficient to complete work, but no coalition should remain globally dominant merely because it was recently active.

**HC implication:** `BASELINE_CONSTRAINT`

A task coalition should expose:

```text
activation_reason
member_nodes[]
working_set[]
priority
stability_window
interruptibility
release_conditions
residual_state_policy
```

This prevents both pathological distractibility and pathological stickiness.

---

## Finding 6 — metacognition should not become a privileged homunculus

**Evidence:** `PLAUSIBLE` engineering conclusion from distributed metacognition and control research.

Metacognitive judgments are themselves computations with uncertainty. Making a `self-monitor` node infallible would simply move the central-controller problem one layer upward.

**HC implication:** `BASELINE_CONSTRAINT`

The self-monitor may observe, summarize, predict, and challenge internal processes, but it should not automatically outrank direct evidence, current correction, hardware receipts, or independent evaluators.

`SELF_MODEL != GROUND_TRUTH`

---

## Suggested internal objects

```text
ATTENTION_ALLOCATION {
  target_refs[]
  reason
  urgency
  compute_budget
  bandwidth_budget
  expires_at
}

METACOGNITIVE_ESTIMATE {
  subject_ref
  proposition_or_decision_ref
  confidence
  uncertainty
  evidence_refs[]
  calibration_ref
  observed_at
}

AGENCY_HYPOTHESIS {
  effect_ref
  candidate_cause_refs[]
  self_action_refs[]
  estimated_control
  competing_causes[]
  confidence
}
```

These objects are typed evidence and control state, not declarations of subjective phenomenology.

---

## Hostile tests

1. **Attention-truth laundering:** make a weak hypothesis extremely salient; confidence must not rise merely because attention does.
2. **Overconfidence calibration:** induce repeated confident errors; the self-capability model must update calibration without deleting the historical mistakes.
3. **Agency spoof:** replay an external effect immediately after a self-issued action; the system must preserve alternative causal hypotheses.
4. **Task-stickiness:** keep one coalition highly activated, then switch the task domain; irrelevant members should release rather than staying globally hot.
5. **Self-model conflict:** make internal self-estimate disagree with external performance receipts; preserve the conflict and update only through evidence.
6. **Global-confidence negative control:** verify confidence in one domain does not silently transfer to unrelated domains.

## Sources

See `[S44-S45,S56-S58]` in `SOURCES.md`.