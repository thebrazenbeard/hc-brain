# Semantics

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`semantics/` represents meaning while preserving proposition, referent, scope, modality, pragmatic force, provenance, uncertainty, and currentness.

Semantics is not synonymous with language. Meaning may be grounded in perception, action, convention, timing, spatial relation, multimodal patterns, or other channels.

## Core separation

```text
RAW_OBSERVATION
!= PARSED_EVENT
!= CANDIDATE_SIGNAL
!= REFERENT_HYPOTHESIS
!= PROPOSITION
!= INTERPRETATION
!= ADJUDICATED_BELIEF
!= RENDERING
```

A fluent rendering must not erase those intermediate distinctions.

## Semantic object

A semantic object may carry:

- stable semantic key;
- proposition type;
- referent(s);
- polarity;
- modality (`asserted`, `denied`, `quoted`, `imagined`, `counterfactual`, `desired`, `questioned`, etc.);
- pragmatic force candidate;
- context requirements;
- source/provenance refs;
- evidence ceiling;
- confidence/ambiguity;
- privacy scope;
- currentness;
- supersession/contradiction refs.

## Uncertainty is content

If multiple interpretations remain plausible, preserve them.

```text
AMBIGUITY_PRESENT
→ candidate_set + support
```

not

```text
AMBIGUITY_PRESENT
→ renderer-forced single answer
```

## Provenance is content

Two identical propositions from different sources are not semantically identical records when provenance matters.

Examples:

- directly observed;
- communicated by another agent;
- remembered;
- inferred statistically;
- inferred causally;
- predicted;
- supplied by an operator;
- evaluator-only ground truth.

## Correction and supersession

A correction about a proposition/referent should stop the contradicted live interpretation for that referent while preserving historical trace.

A correction does not silently broaden to adjacent claims unless the corrected scope supports it.

## Grounding

Candidate meaning should connect, where possible, to:

- observations;
- actions/consequences;
- stable shared conventions;
- relational/contextual history;
- discriminating predictions.

Symbol-to-symbol mapping alone is not universal grounding.

## Semantic conservation

Transformations should be auditable using categories such as:

```text
PRESERVED
TRANSFORMED
INFERRED
OMITTED
ADDED
AMBIGUITY_COLLAPSED
UNRESOLVED
UNTRANSLATABLE
```

## Permission boundary

```text
UNDERSTOOD_REQUEST != PERMISSION != EXECUTION
```

Semantics may identify that an utterance is a request, command, promise, refusal, joke, threat, hypothesis, or desire. It does not grant the requested action authority.

## Failure modes

- answering a stronger proposition than was supplied;
- referent drift while preserving fluent words;
- quote/fiction/hypothesis promoted to asserted fact;
- historical semantics promoted to current state;
- pragmatic force flattened into literal sentence meaning;
- confidence or provenance omitted because a renderer wants simplicity;
- authority inferred from successful understanding.

## Interfaces

Consumes observations, parsed language/events, context, social signals, memory, and corrections.

Produces semantic objects, candidate interpretations, conservation ledgers, and typed meaning state for cognition/action/renderers.
