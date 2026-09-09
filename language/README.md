# Language

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`language/` handles linguistic input/output as one communication modality over the broader semantic substrate.

Language is neither the whole mind nor the required internal representation format.

## Ingress

Language ingress may produce:

- token/segment structure;
- syntax candidates;
- discourse entities;
- quotation boundaries;
- pragmatic cues;
- prosodic/timing cues where available;
- ambiguity candidates;
- candidate referents;
- candidate speech acts.

These are inputs to semantics/pragmatics, not unquestionable meaning.

## Egress

Language egress renders selected semantic/intent state into a target linguistic form while preserving a semantic-conservation account when fidelity matters.

Renderer goals may include:

- truthfulness/fidelity;
- audience comprehension;
- style/register;
- brevity/detail;
- uncertainty expression;
- social appropriateness;
- channel constraints.

Renderer fluency must not add unsupported facts or remove meaningful uncertainty without recording that transformation.

## Communication is broader than language

The hyperconnectome must allow communication through:

- discrete symbols;
- continuous values;
- timing/rhythm;
- movement/orientation;
- spatial arrangement;
- visual signals;
- touch/force;
- environmental modification;
- multimodal combinations;
- deliberate silence/withholding.

A language node therefore cannot be the universal ingress/egress gate.

## Pragmatic force

Language processing should preserve distinctions such as:

```text
statement
question
request
command
promise
refusal
warning
joke
sarcasm
quotation
roleplay
hypothesis
counterfactual
```

Classification remains context-sensitive and revisable.

## Local grammar

Shared history can create local meanings for phrases, timing, callbacks, teasing, code words, or conventions. Such meaning must remain scoped to the relevant participants/context and must yield to fresh evidence that the convention changed or ceased to apply.

## Translation

Translation should operate as:

```text
source signal
→ grounded semantic candidate(s)
→ target rendering
```

not as a presumed one-to-one lexical replacement system.

A correct result may be `NO_FAITHFUL_EQUIVALENT`, `AMBIGUOUS`, or `PARTIAL_OVERLAP`.

## Failure modes

- linguistic surface treated as the only possible meaning;
- shared vocabulary assumed to imply shared ontology;
- target-language fluency laundering inference into fact;
- style treated as authority;
- local convention generalized beyond its participants/context;
- successful coordination mistaken for proven semantic equivalence.

## Interfaces

Consumes sensory/text/speech signals plus context and semantic candidates.

Produces parsed linguistic structures, pragmatic hypotheses, and rendered communication signals.
