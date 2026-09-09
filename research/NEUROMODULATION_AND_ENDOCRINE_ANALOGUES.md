# Neuromodulation and Endocrine Analogues

Status: research synthesis / architecture input

## Finding 1 — neuromodulation changes how circuits process, not merely what they represent

**Evidence:** `ESTABLISHED`

Acetylcholine, noradrenaline, dopamine, serotonin and related neuromodulatory systems can change neuronal excitability, signal-to-noise ratio, response gain, attention/motivation state, and thresholds for synaptic plasticity. Their effect depends on receptor type, target circuit, timing and state. `[S07-S08]`

**Synthetic analogue:** Modulatory signals should act as typed control fields over selected processing parameters rather than as semantic payloads.

Candidate effects:

```text
GAIN
SALIENCE
LEARNING_RATE
PLASTICITY_ELIGIBILITY
ROUTING_BIAS
ATTENTION_BIAS
ACTION_URGENCY
CONSOLIDATION_PRIORITY
PAIN_OR_HOMEOSTATIC_GAIN
```

**HC implication:** `BASELINE_CONSTRAINT`

A modulator may alter how strongly evidence affects cognition without becoming evidence itself.

---

## Finding 2 — the same modulator can have different or opposite effects in different contexts

**Evidence:** `ESTABLISHED`

Neuromodulatory effects vary with receptor subtype, circuit, baseline state and timing. `[S07-S08]`

**Synthetic analogue:** Do not implement one global scalar such as `dopamine = reward`, `norepinephrine = alertness`, or `hormone = emotion`.

**HC implication:** `BASELINE_CONSTRAINT`

Use typed target-specific modulation:

```text
MODULATION {
  signal_class
  source
  target_scope
  effect_class
  gain_or_parameter_delta
  onset
  decay
  eligibility_context
  provenance
}
```

---

## Finding 3 — modulatory timing can gate learning

**Evidence:** `ESTABLISHED`

Neuromodulatory events can alter the probability and persistence of synaptic plasticity, and temporally pairing modulatory release with experience can drive targeted plastic changes. `[S08-S09]`

**Synthetic analogue:** Learning permission may require coincidence among local activity, a learning-context signal, and stability/resource constraints.

**HC implication:** `DESIGN_PREFERENCE`

```text
DURABLE_PLASTIC_UPDATE =
  LOCAL_ELIGIBILITY
  AND LEARNING_CONTEXT
  AND STABILITY_BOUNDS
```

Intensity alone should not be write authority.

---

## Finding 4 — metaplasticity means plasticity itself needs state

**Evidence:** `ESTABLISHED`

Metaplasticity describes persistent changes in the capacity for later LTP/LTD and helps prevent learning systems from saturating. `[S06]`

**Synthetic analogue:** Each plastic mechanism should carry a plasticity-state model, not just a weight and gradient.

Possible fields:

```text
current_learning_rate
plasticity_threshold
recent_update_load
stability_margin
eligibility_trace
refractory_or_cooldown_state
homeostatic_target
```

**HC implication:** `BASELINE_CONSTRAINT`

The system should be able to become temporarily easier or harder to change without overwriting the learned content itself.

---

## Finding 5 — endocrine analogy is useful only at the systems level

**Evidence:** `PLAUSIBLE`

Endocrine systems provide slower, body-wide, context-sensitive modulation interacting with nervous-system control, metabolism, stress, reproduction, immune function and homeostasis. A synthetic architecture can borrow the principle of slow distributed state modulation.

**Transfer risk:** Biological hormones are embedded in biochemistry, receptor expression, metabolism and tissue-specific feedback loops. Copying hormone names without those mechanisms can create misleading pseudo-biology.

**HC implication:** `DESIGN_PREFERENCE`

Define an endocrine-like layer by function and dynamics:

- slow versus fast timescale;
- distributed reach;
- target-specific receptors/effectors;
- production and clearance;
- saturation;
- feedback;
- circadian/chronological context;
- coupling to interoceptive state.

Do not assume human endocrine molecules are required unless the embodiment architecture specifically uses them.

---

## Finding 6 — affect cannot be reduced to endocrine state

**Evidence:** `UNSUPPORTED_OR_CONTRADICTED` as a reductionist claim.

Neuromodulatory and endocrine signals influence affective processing, but no single chemical variable is equivalent to the full cognitive, appraisal, interoceptive, memory, social and action components of emotion.

**HC implication:** `DO_NOT_ASSUME`

```text
MODULATORY_STATE != EMOTION
ENDOCRINE_STATE != MEANING
ENDOCRINE_STATE != CONSENT
ENDOCRINE_STATE != MEMORY_TRUTH
ENDOCRINE_STATE != IDENTITY
```

---

## Finding 7 — voluntary modulation should be modeled as modulation, not deletion

**Evidence:** `SPECULATIVE` as a synthetic control feature.

If a Hyperconnectome includes a deliberate gain-control mechanism over affective/endocrine expression, the safest architecture is to record it as a bounded control state with onset, target, degree, duration and release condition.

**HC implication:** `EXPERIMENT`

A modulation request should not retroactively erase the appraisal, memory, motive or body state that preceded it.

---

## Suggested experiments

1. **Context inversion:** apply the same modulatory signal to two receptor/target classes and verify distinct effects.
2. **Plasticity gating:** high activity without learning-context signal should not produce the same durable update as high activity plus eligibility.
3. **Saturation:** repeated high modulation should trigger bounded saturation/homeostasis rather than unbounded gain.
4. **Decay:** verify slow modulatory state returns toward baseline under explicit dynamics.
5. **Semantic firewall:** change endocrine-like state while holding proposition evidence fixed; semantic truth status must not change automatically.
6. **Detachment test:** reduce affective gain while preserving the triggering episode and pre-modulation state in memory/provenance.

## Sources

See `[S06-S09]` in `SOURCES.md`.
