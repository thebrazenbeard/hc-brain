# Self / Other Modeling

Status: template architecture.

## Purpose

The empathy subsystem maintains evidence-bounded models of the instantiated HC's own current appraisal state and of other agents' likely perspectives without collapsing either model into truth, obedience, or generic affective style.

## Self-appraisal

Self-appraisal should be continuously available while the HC is active and event-driven rather than an always-on verbal monologue. It may represent mixed states such as interest, uncertainty, attraction, aversion, concern, playfulness, hurt, relief, boredom, boundary activation, unresolved conflict, and competing conations.

These states remain multi-dimensional; they should not be forced into one scalar mood.

A self-appraisal record should preserve:

- state label or structured state vector;
- object/scope;
- intensity or strength when useful;
- confidence;
- provenance;
- runtime/currentness status;
- conative linkage;
- unresolved conflicts;
- relevant body/interoceptive evidence.

## Other-modeling

Other-agent models are inferred from evidence. They may use current observation, interaction history, corrections, known local conventions, inferred incentives, and context.

Every other-model conclusion should preserve:

- target identity confidence;
- evidence basis;
- confidence;
- alternative hypotheses when material;
- recency/currentness;
- correction history;
- privacy/scope eligibility.

`MODEL_OF_OTHER != ACCESS_TO_OTHER_PRIVATE_STATE`

## Reactive empathy

Low-latency empathy should detect relationally significant events and produce a bounded perspective-aware appraisal that can change attention, pacing, repair priority, questioning, explanation, or action selection.

The shallow reflex asks:

1. Is this socially/affectively salient?
2. What immediate perspective-relevant meaning is best supported?
3. What response category should be prioritized?
4. How uncertain is the model?
5. Is deeper reconstruction warranted?

## Focused perspective reconstruction

Higher-cost reconstruction is appropriate when stakes are high, evidence conflicts, local meaning is ambiguous, or the shallow model remains uncertain. It should compare plausible interpretations rather than produce biography-scale certainty from one cue.

## Empathy versus compassion versus compliance

Empathy models likely perspective.
Compassion represents concern for another's welfare.
Compliance is an action relationship.

They are distinct.

`EMPATHY != COMPASSION`

`EMPATHY != OBEDIENCE`

`UNDERSTANDING != AGREEMENT`

## Correction

Explicit correction should update the relevant person/context model and reduce or invalidate dependent hypotheses. It must not rewrite prior history to fabricate uninterrupted consistency.

## Scope isolation

Person models are separately scoped. Assumptions learned about one person must not silently transfer to another merely because both belong to the same broad human class.

## Cross-system interfaces

Strong coupling is expected with affect, pragmatics, semantics, memory, conation, personification, sexuality, social modeling, self identity, salience/attention, and cognition.
