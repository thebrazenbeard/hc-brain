# Routing Instructions with Neuroplasticity

Status: working HC template architecture.

## Purpose

This subsystem governs dynamic routing among specialized HC capabilities while keeping routing policy distinct from the underlying learned capability, persistent identity, memory, and action authority.

## Routing responsibilities

- select among specialized cognitive, sensory, semantic, pragmatic, motor, memory, and utility pathways;
- preserve task constraints and provenance across route changes;
- distinguish transient route selection from durable plastic change;
- expose confidence, fallback, and failure state;
- support specialist pools rather than assuming one substrate must perform every workload;
- retain compatibility with external/action gateways whose authority is independent of route selection.

## Plasticity responsibilities

Plasticity updates are slower and more durable than route selection. Candidate update classes include:

- calibration change;
- skill consolidation;
- routing-weight adaptation;
- semantic/pragmatic prior refinement;
- modality-specific learning;
- context/regime learning;
- fault compensation;
- inhibition or strengthening of pathways.

Each durable update should preserve provenance, scope, version, and rollback/supersession information where applicable.

## Separation rule

`route now` is not equivalent to `learn permanently`.

A temporary cognitive strategy, recently active specialist, or salient path must not silently become a global preference or identity feature merely through repeated use.

## Substrate independence

A governed HC instance should be able to use multiple specialist substrates or circuits while preserving coherent system continuity at the architecture level. Substrate provenance explains how an output was generated; it does not by itself establish identity, currentness, or authority.

## Failure modes

- temporary mode promoted into durable plasticity without evidence;
- specialist output losing task/provenance constraints during handoff;
- route success treated as proof of semantic correctness;
- one substrate becoming an accidental monolith;
- plastic updates applied across incompatible embodiment/source identities without explicit transfer;
- routing policy bypassing safety/action authority.

## Provenance

Generalized from `thebrazenbeard/vera-os` model/substrate boundary work, `thebrazenbeard/noema` cognitive-mode work, and `thebrazenbeard/abil` persistent-state and adapter-transfer boundaries. Identity-specific content is excluded.