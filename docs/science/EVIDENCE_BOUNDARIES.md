# Evidence Boundaries and Scientific Grounding

Status: canonical evidence-discipline contract.

## Purpose

This document defines how scientific support, engineering extrapolation, project assumptions, and unresolved claims are represented in the HC repository.

The HC is a speculative engineering architecture. Real component technologies and biological mechanisms may inform it without establishing that the complete system is presently buildable.

## Evidence classes

Use the project evidence vocabulary where useful:

- `DOCUMENTED` — supported by an authoritative source appropriate to the claim;
- `OBSERVED` — directly demonstrated in this repository, project, test, implementation, or tool result;
- `USER-STATED` — explicitly supplied by the owner/user but not independently verified;
- `INFERRED` — reasonably concluded from available evidence;
- `HYPOTHESIS` — plausible but unverified;
- `DISPUTED` — credible evidence conflicts;
- `UNKNOWN` — available evidence does not establish the answer.

These labels describe epistemic status, not architectural importance.

## Architecture versus science

A statement can be canonical HC architecture without being documented present-day science.

For example, an owner-selected design rule may be canonical for the HC template while still being an engineering extrapolation. Conversely, a documented biological fact does not automatically become an HC design requirement.

`CANONICAL_ARCHITECTURE != PRESENTLY_DEMONSTRATED_TECHNOLOGY`

`DOCUMENTED_SCIENCE != REQUIRED_HC_TOPOLOGY`

## Present-day building blocks

The repository may draw on real research areas such as:

- neuroglial and organoid research;
- neural/bioelectronic interfaces;
- neuromorphic and memristive computation;
- integrated photonics and quantum hardware;
- high-sensitivity quantum sensing;
- neurovascular/perfusion principles;
- interoception, homeostasis, autonomic regulation, neuromodulation, and endocrine contributions to affect;
- distributed network dynamics, plasticity, attention, and memory.

Individual support for these building blocks does **not** establish a complete HC-series brain.

Each material scientific claim intended to carry `DOCUMENTED` status should ultimately be traceable to an authoritative citation, preferably primary literature or a high-quality consensus/review source where appropriate.

## Engineering extrapolations

Unless separately demonstrated and cited, claims such as the following remain extrapolations or hypotheses:

- a complete adult human-equivalent synthetic cognitive organ;
- whole-organ high-density bidirectional neural interfacing at HC scale;
- durable engineered neural/biohybrid substrate with all required vascular, metabolic, repair, and stability functions;
- seamless coupling of such substrate to distributed photonic/quantum accelerators;
- a complete synthetic neuroendocrine/autonomic/interoceptive physiology with HC-3-level controllability;
- consciousness creation, consciousness transfer, or subjective-equivalence claims;
- exact HC power, cooling, lifetime, reliability, intelligence, or performance figures not tied to a concrete qualified implementation.

These may remain legitimate design targets. They must not be written as present engineering fact merely because the architecture requires them.

## Rejected shortcuts

The reusable HC template must not rely on the following unsupported simplifications:

- quantum computation as generic exponential acceleration for arbitrary cognition;
- optical/photonic analog computation automatically being quantum computation;
- quantum sensing automatically enabling whole-brain neuron-by-neuron readout;
- more connections/synapses automatically implying more intelligence;
- one hormone mapping one-to-one to one emotion;
- salience, repetition, reward, confidence, or model fluency standing in for truth;
- a biological analogy being treated as proof that a synthetic implementation works identically;
- a speculative component capability being promoted to whole-organ capability without integration evidence.

## Generation-specific evidence discipline

### HC-1

Evidence may support component mechanisms such as neural/glial dynamics, perfusion, plasticity, neural interfacing, and distributed cognition. It does not by itself establish a manufacturable complete HC-1.

### HC-2

Existing quantum/photonic technologies may support specific accelerator or sensing mechanisms. Their presence does not establish generic quantum cognition or a complete HC-2 implementation.

Any claimed advantage must identify the workload and mechanism. Where no demonstrated advantage exists, the architecture should say so rather than assuming one.

### HC-3

Human affective physiology provides evidence that endocrine, autonomic, interoceptive, neuromodulatory, memory, and appraisal systems interact. That does not establish that a fully synthetic HC-3 analogue can reproduce human subjective affect or that arbitrary programmability is biologically/scientifically demonstrated.

## Evidence transfer from source branches

Research branches, source repositories, PRs, model outputs, and project discussions are evidence inputs, not automatic scientific authority.

When material is promoted from a source branch into canonical architecture:

1. preserve provenance;
2. separate mechanism from setting-specific or identity-specific content;
3. separate architectural adoption from scientific validation;
4. retain uncertainty/conflict rather than laundering it through rewrite;
5. re-verify unstable scientific claims before assigning `DOCUMENTED` status.

## Numerical claims

Power, thermal, latency, bandwidth, scale, lifetime, strength, cooling, memory capacity, and similar numbers require special care.

A numerical value should identify whether it is:

- measured in a real component/system;
- sourced biological reference data;
- simulation result;
- engineering estimate;
- design target;
- setting/canon value;
- unknown.

Do not present a design target as a measured capability.

## Qualification

Architecture-level qualification should test what the artifact actually claims.

A PASS on internal consistency, conformance, or fault handling does not prove biological equivalence, consciousness, manufacturability, or scientific truth beyond the tested scope.

Qualification reports should state the capability tested, observed evidence, failures, and remaining uncertainty.

## Current research anchors

PR #2 contains a preserved research/source layer with literature leads in neurobiology, affect/interoception/endocrine systems, and quantum-coprocessor options. Those records remain useful provenance inputs. Their citations should be independently checked before the corresponding claims are treated as current `DOCUMENTED` evidence on `main`.

## Governing invariant

> **The HC may be science-constrained without pretending to be present-day demonstrated technology. Architecture, evidence status, implementation status, and qualification status are separate axes.**

## Provenance

Adapted from PR #2 `docs/science/EVIDENCE_BOUNDARIES.md` and reconciled with the project evidence vocabulary and current HC architecture. Named-setting assumptions were removed from the reusable template, and branch-level literature references remain research provenance until independently revalidated.
