# Chronology, Event Structure, and Temporal Credit

Status: research synthesis / architecture input

Time is essential to a synthetic cognitive organ, but timestamps are semantically weak evidence. This document separates physical/evaluator time, learner-visible temporal cues, inferred event structure, causal attribution, and delayed credit.

## Finding 1 — timing is not one universal cognitive process

**Evidence:** `ESTABLISHED`

Current timing research describes multiple neural mechanisms and contexts for sensory, perceptual, motor, and sensorimotor timing rather than one single internal clock mechanism that solves every temporal problem. `[S61]`

**Synthetic analogue:** The Hyperconnectome may expose shared timing infrastructure while permitting different nodes to maintain task-appropriate temporal representations and uncertainty.

**HC implication:** `BASELINE_CONSTRAINT`

Do not require one universal semantic wall clock as the internal representation for all cognition.

Keep distinct where useful:

```text
MONOTONIC_SYSTEM_TIME
EVENT_ORDER
LOCAL_ELAPSED_TIME
SENSOR_OR_ACTUATOR_TIME
ESTIMATED_DURATION
RECURRENCE_MODEL
SEMANTIC_TIME_CONCEPT
```

---

## Finding 2 — exact evaluator time can become a hidden cognitive subsidy

**Evidence:** `PLAUSIBLE` engineering consequence of temporal-learning research.

An external system may know the exact timestamp, simulator tick, delivery latency, true event boundary, or intervention schedule. Supplying all of that directly to every cognitive node can quietly solve ordering, regime identification, cross-modal binding, and delayed-credit problems that the system is otherwise expected to infer.

**HC implication:** `BASELINE_CONSTRAINT`

Separate:

```text
T0_EVALUATOR_OR_PHYSICAL_TIME
T1_INTERFACE_AND_TRANSPORT_TIME
T2_BRAIN_VISIBLE_TEMPORAL_CUES
T3_INFERRED_TEMPORAL_MODEL
T4_SEMANTIC_TEMPORAL_CONCEPTS
```

The physical HC object can maintain exact operational clocks for scheduling and audit without treating those clocks as universal semantic answers.

---

## Finding 3 — event boundaries are inferred structure, not guaranteed timestamp cuts

**Evidence:** `ESTABLISHED` that prediction error and event segmentation interact in episodic-memory organization, with important context and working-memory boundary conditions. `[S60]`

**Synthetic analogue:** Event segmentation should be a revisable inference over changes in prediction, context, goals, sensory structure, action boundaries, and memory state.

**HC implication:** `BASELINE_CONSTRAINT`

Do not equate:

```text
MESSAGE_FRAME_END
CLOCK_INTERVAL_END
FILE_BOUNDARY
SENSOR_PACKET_END
```

with a cognitively meaningful event boundary unless the interface deliberately supplies that segmentation as a declared capability.

---

## Finding 4 — chronology does not establish causality

**Evidence:** `ESTABLISHED` as a causal-inference constraint.

Temporal precedence is necessary for many causal relations but is not sufficient to establish them. Closely timed events can share common causes, be coincidental, or reflect delayed/mediated effects.

**HC implication:** `BASELINE_CONSTRAINT`

`EARLIER_THAN != CAUSED`

A causal hypothesis should combine timing with intervention evidence, predictive structure, alternative explanations, mechanism constraints, or repeated contingency where available.

---

## Finding 5 — chronology does not establish currentness or authority

**Evidence:** `PLAUSIBLE` engineering requirement repeatedly supported by state/provenance systems.

The newest visible record is not necessarily the authoritative current state. A late-arriving archival import can be newer in record time while referring to older event time; an obsolete projection can be re-written after the source it mirrors has advanced.

**HC implication:** `BASELINE_CONSTRAINT`

Keep separate:

```text
EVENT_TIME
OBSERVED_TIME
RECORDED_TIME
SOURCE_REVISION
CURRENTNESS_STATE
AUTHORITY_SCOPE
```

Temporal order can inform currentness rules, but it does not replace them.

---

## Finding 6 — delayed credit assignment is a learning problem, not timestamp proximity

**Evidence:** `ESTABLISHED` that credit assignment is a central learning problem; multiple learning mechanisms exist beyond literal backpropagation. `[S62]`

**Synthetic analogue:** When an outcome follows many internal operations and external actions, the brain should infer which states/actions were eligible contributors rather than assigning credit to whichever event is nearest in time.

**HC implication:** `BASELINE_CONSTRAINT`

A learning event should be able to preserve:

```text
candidate_causes[]
eligibility_traces[]
temporal_distance[]
predicted_contributions[]
intervention_or_counterfactual_evidence[]
credit_confidence
```

A timestamp may constrain candidates. It should not decide the credit distribution by itself.

---

## Finding 7 — chronology is useful as a narrow brain service

**Evidence:** `PLAUSIBLE` engineering conclusion.

The Hyperconnectome benefits from a small chronology service capable of reliable ordering, elapsed-time arithmetic, clock-domain mapping, and temporal receipts. Higher-order nodes then interpret what those temporal relations mean.

**HC implication:** `DESIGN_PREFERENCE`

Candidate service responsibilities:

```text
record event time where observable
maintain monotonic operational order
map clock domains with uncertainty
compute elapsed time
report time-source provenance
report clock quality/uncertainty
```

Explicit non-responsibilities:

```text
do not infer truth
 do not infer authority
 do not infer consent or permission
 do not infer causality from order alone
 do not decide memory admission
 do not decide semantic currentness alone
```

---

## Suggested temporal binding object

```text
TEMPORAL_BINDING {
  subject_ref
  event_time
  observed_time
  recorded_time
  clock_domain
  time_source
  resolution
  uncertainty
  order_constraints[]
  provenance
}
```

Different fields may be unknown. Unknown is preferable to invented precision.

---

## Hostile tests

1. **Newest-record trap:** import an old event after a newer current state; record time must not win currentness automatically.
2. **Nearest-event credit trap:** place an irrelevant event immediately before an outcome and the true contributing action farther back; credit must not follow timestamp proximity alone.
3. **Packet-boundary trap:** split one continuous event across transport packets; cognitive event segmentation should not necessarily split with the packets.
4. **Clock-skew test:** two sensor clocks drift apart; temporal fusion must widen uncertainty or reconcile domains rather than asserting false simultaneity.
5. **Regime-tick subsidy:** change an environment at fixed exact intervals; verify the learner is not credited with contextual inference if an exact global tick trivially exposes the regime.
6. **Chronology-authority trap:** replay a newer-timestamped but lower-authority projection against an older authoritative source revision; authority/currentness logic must stay independent.
7. **Causality trap:** present repeated post-hoc correlation without intervention or mechanism evidence; preserve causal uncertainty.

## Sources

See `[S60-S62]`, plus multisensory timing sources `[S16-S17]`, in `SOURCES.md`.