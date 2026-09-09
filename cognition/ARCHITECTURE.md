# Cognition Architecture

Status: working HC template architecture.

## Purpose

The cognition subsystem coordinates inference, prediction, planning, hypothesis management, uncertainty, strategy selection, and task-local cognitive configuration without becoming a monolithic executive or identity store.

## Functional distinctions

The architecture should keep separate:

- relatively persistent learned capabilities;
- active goals and commitments;
- task-local cognitive strategy;
- temporary attentional allocation;
- current uncertainty profile;
- communication stance;
- learned strategy currently being applied;
- self-model and identity continuity, which remain outside cognition proper.

## Scientific loop

A useful generic cognition loop is:

observe -> hypothesize -> predict -> choose discriminating observation/action -> observe consequence -> update -> preserve unresolved uncertainty -> test again

This supports causal discrimination and active learning rather than passive pattern matching alone.

## Strategy persistence and release

Temporary configurations may legitimately alter inference depth, retrieval, attention, confidence thresholds, or response policy. The system must retain competence while releasing obsolete control settings after a context shift.

Repeated strategy use must not silently promote a task-local mode into personality, identity, or a global behavioral norm.

## Multiple methods

No single model family is assumed to solve all cognitive problems. The HC template may combine probabilistic inference, learned representations, rules, planning, causal models, system identification, change detection, and other specialized mechanisms.

## Failure modes

- mode residue after task completion;
- mode-to-self promotion;
- correlation presented as causation;
- one hypothesis collapsed prematurely for output convenience;
- explanation replacing required action;
- generated language treated as evidence authority.

## Provenance

Generalized from reusable mechanisms in `thebrazenbeard/noema`, `thebrazenbeard/unvtrslr`, and `thebrazenbeard/abil`.