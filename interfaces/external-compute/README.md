# External Compute Interface

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/external-compute/` governs optional computational systems that remain outside the HC boundary: LLMs, SPMs, retrieval engines, databases, cloud services, specialized inference models, simulators, accelerators, or other compute resources.

The external system can be extremely capable without becoming the organism's essential cognition.

## Hard rule

```text
EXTERNAL_COMPUTE_OUTPUT = external evidence/input
```

unless that compute component has been explicitly brought **inside** the HC architectural boundary as an HC-owned subsystem.

## Request envelope

An external compute request should be able to specify:

- task/proposition;
- bounded context supplied;
- privacy classification;
- requested output type;
- freshness/deadline;
- source/model/service identity;
- authority limits;
- reproducibility parameters where applicable.

## Response envelope

A response should preserve:

- provider/model/service identity;
- request correlation;
- output payload;
- timestamp/currentness;
- confidence/uncertainty if supplied;
- source citations/refs if supplied;
- integrity/provenance;
- failure/partial-result state.

## Internal adjudication

The HC may use the response as:

- a candidate interpretation;
- a retrieved source;
- a proposed plan;
- a prediction;
- a generated representation;
- a computational result.

The HC remains responsible for current context, semantic adjudication, memory admission, value/goal reconciliation, and action authority.

## Identity/memory prohibition

An external compute service must not be treated as the canonical owner of:

- instantiated identity;
- autobiographical continuity;
- current self-model;
- current conation/consent;
- current authority;
- private durable memory;
- essential integrated cognition.

## Graceful loss

Loss of optional external compute may reduce capability or performance but must not make the architecture conceptually cease to contain its mind.

A deployment may still become operationally degraded if required internal capability has not yet been implemented; that is an implementation limitation, not the template definition.

## Failure modes

- external model answer accepted as truth because it is fluent;
- provider model swap treated as identity replacement;
- external service retaining private cognitive state without explicit policy;
- service unavailability interpreted as loss of self;
- external tool invocation silently becoming execution authority;
- retrieved/generated content admitted to durable memory without provenance.
