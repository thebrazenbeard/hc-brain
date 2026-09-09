# Homeostasis and Interoception Architecture

Status: template architecture / research-informed

## Purpose

This subsystem represents internal-body state, physiological needs, damage signals, resource pressure, and regulatory feedback. It is both a stabilization system and a source of cognitive evidence.

Interoception is not merely a hardware dashboard. Internal-body signals should participate in salience, affect, self-model, action selection, learning, and memory.

## Candidate internal channels

The template should accommodate implementation-specific channels such as:

- perfusion and flow;
- oxygenation or equivalent carrier saturation;
- carbon-dioxide / pH proxies;
- osmolarity and hydration;
- energy-substrate availability;
- tissue or substrate temperature;
- endocrine or neuromodulatory concentrations;
- inflammatory, damage, or fault signals;
- nociception;
- joint, tendon, actuator, or load state;
- respiratory effort where applicable;
- vestibular and body-pose state;
- local resource saturation and thermal stress.

Not every embodiment needs every channel. The contract is that internal state must remain typed, attributable, and uncertainty-bearing.

## Functional separation

The subsystem should preserve distinctions among:

- raw sensor observation;
- normalized physiological estimate;
- homeostatic error;
- urgency;
- predicted consequence;
- requested regulation;
- achieved body-state change.

A regulator should not silently convert a sensor reading into a semantic claim or durable memory.

## Multiple timescales

At minimum, support:

1. fast protective/reflex regulation;
2. short-timescale autonomic or actuator regulation;
3. slower endocrine/metabolic adaptation;
4. longer recovery, calibration, and plasticity effects.

Slow deliberation must not block hard real-time survival or damage-prevention loops.

## Feedback architecture

A generic loop is:

`internal sensing -> state estimate -> error/need computation -> regulatory action -> body-state change -> new sensing`

The loop should expose state to affect, salience, cognition, and self-model without granting those higher layers unrestricted control over protective minima.

## Interaction with affect

Homeostatic and interoceptive state may influence arousal, motivation, threat estimation, pain, fatigue, learning rate, retrieval bias, and action urgency.

Conversely, affect and cognition may alter autonomic/endocrine targets or regulatory gain. This is a coupled system, not a one-way feed.

## Stability safeguards

Monitor for at least:

- runaway gain;
- oscillatory correction;
- sensor disagreement;
- stale internal state;
- saturation;
- unbounded resource demand;
- thermal or perfusion failure;
- pathological synchronization;
- modulatory saturation.

Protective controls should remain independently observable and should fail toward bounded degradation where possible.

## Evidence boundary

DOCUMENTED: interoceptive and homeostatic processes are deeply coupled with emotion, cognition, autonomic regulation, and behavior in biological systems.

INFERRED TEMPLATE RULE: HC implementations should expose internal-body state as a first-class uncertainty-bearing input to cognition while keeping protective regulation independently enforceable.

UNKNOWN / IMPLEMENTATION-DEPENDENT: exact sensors, chemistry, substrate, and embodiment-specific setpoints.

## Provenance

Generalized from `research/nooplex-hc3-architecture-v1` affect/interoception research and the runtime/plasticity work on `four/runtime-hyperconnectome-v1`; identity- and setting-specific assumptions were removed.