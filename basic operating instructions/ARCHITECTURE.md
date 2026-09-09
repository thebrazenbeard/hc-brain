# Basic Operating Instructions Architecture

Status: template architecture / system invariants

## Purpose

This subsystem defines low-level operating invariants that every compatible HC implementation should preserve regardless of identity, embodiment, substrate, or task.

It is not a personality file, moral constitution, or identity profile. It is the architectural equivalent of core operating constraints and interpretation rules.

## Core invariants

### 1. Preserve typed state boundaries

Observation, inference, memory, current state, identity, preference, conation, permission, commitment, and action authority are separate state classes. One must not silently promote into another.

### 2. Preserve provenance

Every material claim or durable update should retain enough provenance to answer where it came from, when it applied, and whether it was observed, inferred, imported, configured, or learned.

### 3. Preserve uncertainty

Unknown, ambiguous, disputed, stale, and contradicted are valid states. The runtime should not collapse them merely because a downstream renderer prefers one answer.

### 4. Correction changes active state

A valid correction invalidates dependent interpretations before dependent action continues. Correction is a state transition, not just an apology or annotation.

### 5. Action is separately authorized

Understanding, predicting, recommending, wanting, or planning an action does not itself authorize execution. Effectful action remains gated by capability, embodiment, safety, and implementation-specific authority.

### 6. Temporary state is not durable state

Attention, affect, cognitive mode, route selection, working memory, and active coalitions are transient unless admitted through the appropriate durability/plasticity mechanism.

### 7. No hidden monolith

No resolver, workspace, model, memory store, scheduler, or communication layer is allowed to become the unacknowledged "real brain" while the other systems are decorative. System behavior should remain causally distributed and testable.

### 8. Fail visibly and degrade locally

Subsystem failure should expose stale, unavailable, degraded, or uncertain state rather than fabricate healthy output. Where possible, failures remain locally contained and permit graceful degradation.

### 9. Evidence and effect are separate

A record that an action was requested or attempted is not proof the effect occurred. Durable effects should be confirmed by direct observation, readback, or an implementation-appropriate receipt.

### 10. Identity neutrality at template level

The base HC architecture contains mechanisms, not a named person's memories, values, relationships, personality, or autobiographical state.

## Runtime application

These instructions should constrain subsystem contracts, arbitration, routing, memory admission, learning, action selection, and recovery. They may be instantiated differently across substrates, but a compatible implementation should be able to demonstrate equivalent behavior.

## Provenance

Generalized from recurring invariants across `noema`, `semanticatlas`, `conations`, `temporal`, `abil`, inspected control-plane/runtime work, and Supabase state/evidence schemas.