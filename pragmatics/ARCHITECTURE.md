# Pragmatics Architecture

Status: working HC template architecture.

## Purpose

The pragmatics subsystem resolves communicative force, local scope, context, implied action, uncertainty, and interaction function without collapsing them into one global interpretation.

## Core functional distinctions

The subsystem should represent separately:

- illocutionary force: request, question, correction, assertion, warning, play, repair, etc.;
- target/action scope;
- epistemic confidence;
- deontic or necessity uncertainty;
- referential uncertainty;
- relevance uncertainty;
- affective and pragmatic modifiers;
- local conversational convention;
- current cognitive mode and its possible interpretive bias.

Uncertainty should attach to the narrowest supported scope rather than weakening an entire utterance by default.

## Context-sensitive interpretation

Meaning is conditioned on signal, context, interaction history, sender state, receiver state, and world state. The subsystem must preserve ambiguity when multiple readings remain viable.

It must distinguish discussion about an action from an actual request to perform that action, and direct correction must invalidate dependent interpretations before further dependent action.

## Mode-residue control

Temporary cognitive modes such as research, planning, threat response, reflection, or precision execution must not silently become permanent personality or global interpretation policy.

The system should be able to retain learned competence while releasing obsolete temporary control settings after context changes.

## Grounding and repair

Pragmatic interpretation should be grounded in observed consequences, interaction history, correction, and negotiated convention. Explicit correction about intended meaning should update speaker-specific or context-specific hypotheses without becoming a universal grammar rule from one case.

## Failure modes

- treating local hedges as global uncertainty;
- explaining an instruction instead of carrying it out;
- technical-schema activation overriding stronger immediate context;
- inventing an opposite claim after a correction;
- persisting a temporary cognitive mode after its task ends;
- treating interaction success as proof of semantic equivalence.

## Provenance

Generalized from reusable mechanisms in:

- `thebrazenbeard/noema`, especially `docs/working-design/COGNITIVE_MODE_AND_PRAGMATIC_SCOPE.md`;
- `thebrazenbeard/unvtrslr`, especially `docs/DESIGN_PRINCIPLES.md`.

Identity-specific examples from those repositories are not part of this template.