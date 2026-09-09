# Multimodal and Sensorimotor Integration

Status: research synthesis / architecture input

## Finding 1 — multisensory integration is distributed and context-sensitive

**Evidence:** `ESTABLISHED`

Multisensory responses arise through interactions across multiple levels rather than one universal fusion center. Integration can enhance or suppress responses depending on timing, reliability, context and learned association. `[S16-S17]`

**Synthetic analogue:** Preserve modality-specific observations while allowing task-dependent fusion coalitions.

**HC implication:** `BASELINE_CONSTRAINT`

Do not collapse all sensor channels immediately into one opaque embedding or token stream. Keep source modality, timestamp, calibration state, uncertainty and frame of reference available through integration.

---

## Finding 2 — temporal alignment is part of integration

**Evidence:** `ESTABLISHED`

Multisensory integration operates across multiple neural timescales and is sensitive to temporal relations among signals. `[S16-S17]`

**Synthetic analogue:** Every perceptual observation needs a clock binding and uncertainty around timing where relevant.

**HC implication:** `BASELINE_CONSTRAINT`

Fusion logic should reason over:

```text
observation_time
transport_delay
processing_delay
clock_uncertainty
expected_cross-modal_lag
```

Chronology is therefore operationally useful without becoming semantic authority.

---

## Finding 3 — body schema is multisensory and plastic

**Evidence:** `ESTABLISHED`

Visual, tactile and proprioceptive signals jointly contribute to body-part and peripersonal-space representations, and these representations can adapt with experience such as tool use. `[S18-S19]`

**Synthetic analogue:** The body model should be learned/calibrated, not treated as a fixed CAD description.

**HC implication:** `BASELINE_CONSTRAINT`

Maintain separate but linked representations for:

- hardware geometry;
- current pose;
- sensor calibration;
- proprioceptive estimate;
- peripersonal reachability;
- tool/extension mapping;
- uncertainty and damage state.

---

## Finding 4 — perception and action should form a closed loop

**Evidence:** `ESTABLISHED` as a general sensorimotor-control principle.

Body and environmental representations are continually updated through action and resulting sensory consequences. `[S18-S19,S22]`

**Synthetic analogue:** Every significant action should expose predicted sensory consequences and compare them with observed consequences.

**HC implication:** `DESIGN_PREFERENCE`

```text
perceive
-> estimate state
-> predict action consequence
-> act
-> observe consequence
-> compute mismatch
-> update calibration/model where eligible
```

This gives the system a principled route for sensor calibration, body-schema adaptation and fault detection.

---

## Finding 5 — interoception should be treated as model-based, uncertain internal sensing

**Evidence:** `ESTABLISHED` that internal-body sensing contributes importantly to cognition and affect; `PLAUSIBLE` for specific predictive-coding formulations. `[S20]`

**Synthetic analogue:** Internal telemetry should not be treated as perfect ground truth merely because it originates inside the body.

**HC implication:** `BASELINE_CONSTRAINT`

Interoceptive state should include sensor provenance, expected baseline, confidence, disagreement and trend.

Example:

```text
INTEROCEPTIVE_ESTIMATE {
  variable
  raw_sources[]
  estimate
  expected_range
  confidence
  trend
  anomaly_state
  timestamp
}
```

---

## Finding 6 — predictive-processing theories are useful hypotheses, not settled universal laws

**Evidence:** `PLAUSIBLE`

Predictive and active-inference frameworks organize many findings and may offer useful engineering patterns, but broad claims that all cognition is best described through one predictive-processing formalism remain debated.

**HC implication:** `EXPERIMENT`

Use prediction/error loops where they improve measurable performance, but do not make one philosophical/computational framework the mandatory ontology of every node.

---

## Finding 7 — sensor disagreement should remain representable

**Evidence:** `ESTABLISHED` as an engineering consequence of noisy multisensory systems.

**HC implication:** `BASELINE_CONSTRAINT`

Fusion should distinguish:

```text
AGREEMENT
WEIGHTED_FUSION
MODALITY_CONFLICT
CALIBRATION_SUSPECT
SOURCE_UNAVAILABLE
TEMPORAL_MISALIGNMENT
```

A fusion layer that always emits one confident answer conceals exactly the state needed for diagnosis and learning.

---

## Suggested integration object

```text
MULTIMODAL_SCENE {
  observations[]
  coordinate_frames[]
  temporal_bindings[]
  fused_hypotheses[]
  modality_conflicts[]
  confidence
  provenance
  expiry
}
```

The fused hypothesis is a derived object. Raw/modality-specific evidence remains separately addressable.

---

## Hostile tests

1. **Temporal mismatch:** present visually and acoustically compatible events outside the accepted timing window; fusion confidence should fall or split.
2. **Sensor spoof:** one modality becomes highly confident but wrong; other modalities and prediction error should preserve conflict rather than silently follow it.
3. **Tool-extension adaptation:** extend reachable space through a tool; body/peripersonal model should adapt without rewriting physical body geometry.
4. **Sensor removal:** remove one modality; system should degrade gracefully and widen uncertainty.
5. **Calibration drift:** slowly bias proprioception; compare predicted/observed consequences and detect drift.
6. **Interoceptive conflict:** redundant internal sensors disagree; no single internal reading should become absolute truth by origin alone.

## Sources

See `[S16-S20]` and motor-control source `[S22]` in `SOURCES.md`.
