# Affect, Interoception, and Endocrine Architecture for HC-3

Status: RESEARCH SYNTHESIS
Date: 2026-09-09
Scope: Independent review of emotion, interoception, endocrine regulation, and neuromodulation relevant to HC-3.

## 1. Core correction: emotion is not a hormone lookup table

DOCUMENTED: Human emotional experience emerges from interacting neural, autonomic, interoceptive, endocrine, learned, and contextual processes. Interoceptive pathways convey the physiological condition of the body and are strongly linked to subjective feeling and emotional awareness, particularly through insular and cingulate systems.

Sources:
- Craig, Nature Reviews Neuroscience 3, 655–666 (2002), DOI 10.1038/nrn894, PMID 12154366.
- Craig, Nature Reviews Neuroscience 10, 59–70 (2009), DOI 10.1038/nrn2555, PMID 19096369.
- Critchley et al. / related interoception literature summarized in PMID 16003122.
- Recent review: PMID 38722464.

INFERRED DESIGN RULE: HC-3 should not implement one-to-one mappings such as `testosterone = anger`, `oxytocin = trust`, or `dopamine = happiness`.

SPECULATIVE HC IMPLEMENTATION: Affect is represented as a dynamic state generated from neural appraisal + internal body state + endocrine state + memory + context + learned expectations.

## 2. Interoception must be a first-class sensory channel

DOCUMENTED: Interoception represents internal physiological conditions including pain, temperature, visceral state, hunger, thirst, vasomotor condition, and air hunger. The insular cortex integrates internal body signals with emotion and cognition.

Sources:
- Craig (2002), PMID 12154366.
- Craig (2003/related review), PMID 12965300.
- Xiao et al., review, PMID 38722464.

INFERRED DESIGN RULE: The HC-3 "Interoceptive Sensor Matrix" should not merely monitor hardware telemetry. Its signals should be routed into the same salience and self-model circuitry that evaluates external stimuli.

Recommended internal channels for a humanoid Synthetic include:
- perfusion pressure and flow;
- oxygen-carrier saturation;
- CO2/pH proxy;
- osmolarity and hydration state;
- glucose/energy-substrate proxy;
- tissue temperature;
- endocrine concentrations;
- inflammatory/damage signals;
- joint/tendon loading;
- nociception;
- respiratory effort;
- body pose and vestibular state.

## 3. Stress architecture: neural + autonomic + endocrine

DOCUMENTED: Mammalian stress responses couple the hypothalamic-pituitary-adrenal (HPA) axis with sympathetic/autonomic systems. Stressors activate CRH/CRF pathways, pituitary ACTH, glucocorticoid secretion, and autonomic changes. Feedback regulation limits magnitude and duration.

Sources:
- PMID 12040534.
- PMID 17290797.
- PMID 12377295.
- PMID 30390966.

INFERRED DESIGN RULE: HC-3 needs at least two coupled response timescales:
1. Fast autonomic/catecholaminergic response for immediate arousal and action readiness.
2. Slower endocrine response for sustained adaptation, memory biasing, metabolic allocation, and recovery.

SPECULATIVE HC IMPLEMENTATION:
- Hypothalamic-Homeostatic Complex: computes homeostatic error and stress drive.
- Pituitary-analog interface: converts neural drive into endocrine release commands.
- Adrenal-like effector tissue/cartridge: fast catecholamine-like and slower glucocorticoid-like signaling.
- Closed negative feedback via endocrine sensors.

## 4. Oxytocin is not a 'trust chemical'

DOCUMENTED: Oxytocin affects social behavior, attachment, anxiety, aggression, and related functions, but findings are context-dependent and sometimes conflicting. Recent human neuroimaging reviews emphasize dependence on individual differences, sex, dose, and context.

Sources:
- PMID 38626843.
- PMID 41554388.
- PMID 39054193.
- PMID 40513975.

INFERRED DESIGN RULE: HC-3 should model oxytocin-like signaling as a context-sensitive modulator of social salience, reward valuation, attachment, and stress regulation—not a universal trust switch.

## 5. Testosterone is not an anger knob

DOCUMENTED: Meta-analysis finds only weak associations between baseline testosterone and human aggression, with manipulated testosterone effects smaller and not statistically robust in the aggregate. Context and individual variables matter.

Sources:
- Geniole et al., Hormones and Behavior 123 (2020), DOI 10.1016/j.yhbeh.2019.104644, PMID 31785281.
- Carré & Archer, Current Opinion in Psychology (2018), PMID 29279215.

INFERRED DESIGN RULE: Gonadal-hormone analogs may modulate dominance, motivation, competition, sexual behavior, or social salience, but must operate through context-sensitive neural circuits.

## 6. Dopamine is not 'pleasure juice'

DOCUMENTED: Dopamine is strongly implicated in reinforcement learning and reward-prediction-error signaling, but its functions extend into movement, motivation, sensory prediction, action selection, and goal-directed planning. Modern reviews explicitly reject overly simple single-function accounts.

Sources:
- PMID 33197709.
- Gershman et al., Nature Neuroscience (2024), DOI 10.1038/s41593-024-01705-4, PMID 39054370.
- PMID 37451506.

INFERRED DESIGN RULE: HC-3 should use dopamine-like modulation primarily as a distributed learning/motivation/value signal, not as a direct encoding of happiness.

## 7. Recommended HC-3 affect architecture

### Affective state vector

Use a multidimensional state rather than named-emotion chemistry. Example internal dimensions:
- arousal;
- valence;
- threat estimate;
- social safety;
- attachment drive;
- dominance/submission bias;
- novelty/salience;
- fatigue/energy reserve;
- pain burden;
- sexual/reproductive drive;
- uncertainty;
- reward expectation.

Named emotions such as fear, grief, affection, anger, embarrassment, desire, or joy are higher-order interpretations that emerge from combinations of these variables plus appraisal and autobiographical context.

### Core loops

1. Exteroception -> appraisal.
2. Interoception -> body-state model.
3. Memory -> context and expectation.
4. Neuromodulators/endocrine state -> gain, learning rate, attention, motivation.
5. Autonomic output -> body change.
6. Body change -> new interoceptive input.
7. Higher-order cortex -> conscious interpretation and regulation.

This loop is deliberately circular: emotion changes the body, and the changed body becomes part of the subsequent emotional state.

## 8. Voluntary control and autonomous mode

USER DESIGN REQUIREMENT: HC-3 endocrine and affect systems are trainable, programmable, and overrideable unless the Synthetic willfully engages autonomous endocrine response mode.

ENGINEERING INTERPRETATION:
- Manual Mode: external or conscious control can directly adjust endocrine targets and modulation gains.
- Assisted Mode: conscious requests set goals/bounds while homeostatic controllers manage details.
- Autonomous Endocrine Response Mode: the Synthetic delegates moment-to-moment endocrine release to native affective/homeostatic loops.

Important distinction: autonomous mode should not mean 'uncontrollable.' It means normal affective causation is no longer being micromanaged. A Synthetic can still regulate emotion through cognition and learned self-regulation just as humans can, but not necessarily set every hormone concentration directly in real time.

## 9. External emotional expression

INFERRED DESIGN RULE: facial, vocal, and postural expression should be driven by the same affect state used internally, not by a separate theatrical emote engine.

Recommended mapping targets:
- facial musculature;
- gaze and blink dynamics;
- pupil/iris response if biologically implemented;
- vocal prosody and respiration;
- posture;
- gesture amplitude and speed;
- interpersonal distance;
- skin temperature/perfusion proxies where body design supports them.

The expression system may suppress or exaggerate outward display, but its default should be coupled to internal affect so that expression is not merely decorative animation.

## 10. Hard engineering protections vs behavioral policy

A useful architecture distinction:
- Behavioral/ethical policy layers may be user- or Synthetic-overridable according to setting canon.
- Tissue-survival controls should not be conflated with moral policy. Thermal runaway prevention, perfusion minimums, excitotoxicity protection, seizure suppression, and endocrine toxicity limits are analogous to keeping the brain physically alive.

This distinction allows HC-3 to preserve volitional emotional autonomy without making self-destruction an accidental side effect of a badly tuned hormone API.

## 11. What remains fictional

The literature does NOT establish:
- a synthetic endocrine system sufficient to reproduce human subjective emotion;
- deterministic programming of complex emotions;
- upload/download of emotional personality;
- proof that duplicating endocrine/interoceptive loops creates human-equivalent phenomenology;
- consciousness transfer into such a system.

Those remain Wreckforge assumptions or hypotheses.
