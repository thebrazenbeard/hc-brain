# HC Conformance and Qualification

Status: canonical architecture conformance contract.

## Purpose

This document defines what it means to test the HC repository, an HC implementation, or an HC behavior claim without collapsing architecture, implementation, evidence, and qualification into one status.

A repository can conform to the HC architecture while no physical HC exists. An implementation can conform structurally while remaining behaviorally unqualified. A behavioral test can pass within scope without proving consciousness, biological equivalence, universal intelligence, or manufacturability.

`ARCHITECTURE_CONFORMANCE != IMPLEMENTATION_CONFORMANCE`

`IMPLEMENTATION_CONFORMANCE != BEHAVIORAL_QUALIFICATION`

`BEHAVIORAL_QUALIFICATION != SCIENTIFIC_VALIDATION`

`TEST_PASS != CONSCIOUSNESS_PROOF`

## Qualification object

A qualification result should identify:

```text
QUALIFICATION_RESULT {
  qualification_id
  target_kind
  target_ref
  tested_capability
  test_scope
  evidence_snapshot
  checks[]
  observed_failures[]
  unresolved_uncertainty[]
  outcome
  timestamp
  evaluator
  provenance
}
```

`target_kind` may include repository architecture, implementation, subsystem, interface, runtime behavior, degraded mode, embodiment, or scientific claim set.

## Outcomes

Use only:

- `PASS` — every required check in the stated scope passed with adequate observed evidence;
- `CONDITIONAL_PASS` — the tested scope substantially passed, but explicit unresolved limits, unavailable evidence, or non-blocking defects prevent an unconditional pass;
- `FAIL` — one or more required checks failed, or required evidence is absent enough that the claimed capability is not established.

A PASS is always scoped. It must never be silently generalized beyond the tested target, evidence snapshot, and capability.

## Conformance layers

### 1. Repository architecture conformance

Tests whether canonical repository material preserves the intended HC architecture.

This may test:

- required top-level subsystem coverage;
- complete cognitive-organ boundary;
- distributed physical-organ membership;
- temporal-hypergraph semantics;
- state-axis separation;
- authority/consent/effect separation;
- intrinsic current/deep memory ownership;
- body independence and remapping;
- generation inheritance;
- identity-neutral base-template rules;
- evidence and implementation-status separation;
- explicit failure/degradation semantics;
- provenance and source-transfer discipline.

File existence alone is insufficient. A present file can still violate the architecture semantically.

### 2. Implementation conformance

Tests whether a concrete implementation actually realizes required architectural properties.

Examples include:

- required intrinsic capabilities are implemented or explicitly represented at the claimed implementation level;
- essential cognitive state is HC-owned and recoverable without a true external provider;
- distributed HC constituents remain under HC lifecycle/fault/transfer semantics;
- external peripherals cannot become silent cognitive authority;
- authority gates are enforced at consequential effect boundaries;
- lifecycle axes remain independent in actual state storage and transitions;
- failure states are observable and localizable;
- body replacement does not strand essential HC state or substrate.

An implementation must not obtain a pass from documentation claims alone.

### 3. Behavioral qualification

Tests an implemented capability through observed behavior under defined conditions.

Behavioral qualification should include positive cases, negative cases, ambiguity/conflict cases, stale-state cases, revocation cases where relevant, degraded/fault cases, and adversarial counterexamples proportional to consequence.

A model producing a correct answer once does not establish a durable cognitive capability.

### 4. Scientific validation

Tests scientific or engineering claims against appropriate external evidence.

Repository adoption does not establish scientific truth. A scientific claim marked `DOCUMENTED` requires authoritative support appropriate to that claim. Engineering extrapolation, design target, simulation result, observed prototype behavior, and documented present-day science remain distinct.

## Canonical architecture conformance domains

The machine-readable suite in `specs/HC_CONFORMANCE_SUITE_V1.yaml` defines the baseline canonical checks. Its domains are:

- repository structure and complete capability presence;
- cognitive-organ ownership;
- distributed physical membership and removability;
- temporal hypergraph and distributed integration;
- orthogonal lifecycle/state dimensions;
- memory and continuity residency;
- external compute/provider boundaries;
- authority, consent, and effect governance;
- embodiment/body independence;
- generation lineage and graceful degradation;
- developmental initialization and identity neutrality;
- epistemic/evidence discipline;
- failure visibility, dead-letter, correction, and reconciliation;
- provenance and source-transfer control.

## Required evidence discipline

Qualification should distinguish at least:

- expected architecture or requirement;
- evidence actually inspected;
- observation made from that evidence;
- pass/fail criterion;
- outcome;
- unresolved uncertainty.

Do not claim that a check passed because the evaluator intended it to pass.

For repository checks, exact branch/head or commit should be recorded. For runtime checks, the implementation version/configuration and test conditions should be recorded. For scientific checks, citations and their relevance to the exact claim should be recorded.

## Hostile review

Material architecture changes should be testable against adversarial review rather than only constructive review.

Useful hostile-review questions include:

- Can an external provider become the sole owner of essential cognition or continuity?
- Can a route, credential, capability, social role, maintenance path, or successful prior action silently become authority?
- Can a subsystem state transition mutate another lifecycle axis implicitly?
- Can a correction leave stale dependents active?
- Can a body swap strand essential HC substrate?
- Can a generation-specific fault silently rewrite generation identity?
- Can a temporary coalition become a permanent executive path without admission?
- Can a learned tendency, salience signal, reward, or prediction change truth status directly?
- Can a named identity, relationship, preference, or setting-specific assumption leak into the reusable template?
- Can a research citation, source branch, or model output acquire `DOCUMENTED` status without verification?

A hostile reviewer should report concrete counterexamples, exact paths/claims, severity, and a falsification or repair test where possible.

## Negative tests

A conformance suite is incomplete if it tests only intended success paths.

At minimum, implementations should be challengeable with cases involving:

- expired or revoked authority;
- ambiguous consent;
- conflicting current-state heads;
- stale memory or provider readback;
- degraded or quarantined subsystem state;
- unavailable body peripheral;
- distributed HC constituent loss;
- external service hallucination or contradiction;
- routing success without authority;
- capability availability without authorization;
- high salience with weak evidence;
- learned/rewarded behavior conflicting with current values or boundaries;
- out-of-order or duplicate events;
- body replacement with incompatible mappings;
- temporary loss of HC-2/HC-3 generation-specific substrate.

## Qualification boundaries

A repository architecture PASS means only that the inspected canonical material satisfied the tested architecture checks.

It does not establish:

- that the architecture is physically manufacturable;
- that a complete implementation exists;
- that the implementation is conscious or sentient;
- that the implementation is human-equivalent;
- that every scientific claim is documented;
- that all future branches or commits remain conforming;
- that a passed subsystem is safe or competent outside its tested scope.

## Governing invariant

> **Qualification is evidence-bound, target-bound, capability-bound, and snapshot-bound. No PASS may be silently promoted into a stronger claim than the tests actually establish.**

## Provenance

Synthesized from `docs/science/EVIDENCE_BOUNDARIES.md`, `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml`, the subsystem lifecycle contract, cognitive-organ and physical-membership rules, authority/effect governance, resolver/failure semantics, and the project qualification protocol.
