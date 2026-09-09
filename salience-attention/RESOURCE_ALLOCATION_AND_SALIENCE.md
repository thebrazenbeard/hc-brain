# Resource Allocation and Salience

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

`salience-attention/` allocates processing priority, working-state retention, routing preference, sensory sampling, and coalition recruitment according to context and resource limits.

Attention is selective resource/control state. Salience is a relevance/urgency weighting signal. Neither is truth, value, authority, or permission.

## Core invariant

```text
HIGH_SALIENCE
!= HIGH_TRUTH
!= HIGH_AUTHORITY
!= HIGH_VALUE
!= EFFECT_PERMISSION
```

## Salience contributors

Potential contributors include:

- exogenous sensory novelty or intensity;
- active goals and task relevance;
- affective/interoceptive modulation;
- prediction error;
- social significance;
- unresolved conflict;
- safety/assurance triggers;
- explicit task priority;
- learned relevance;
- memory-cue strength;
- correction/contradiction signals;
- resource or fault state.

Each contributor should retain its own provenance/type so a high aggregate salience score does not erase why something became salient.

## Attention operations

Attention control may:

- increase or decrease routing priority;
- recruit specialist systems into a coalition;
- retain or evict current-memory/working-state items;
- alter sensory sampling;
- alter processing gain through modulators;
- allocate bounded compute/energy/bandwidth;
- trigger coalition expansion;
- inhibit distractor paths;
- escalate unresolved/high-consequence state for broader integration.

## Temporal scope

Attention state is generally a transient property of the effective temporal hypergraph.

```text
SALIENT_AT(t1) != SALIENT_AT(t2)
ATTENDED != DURABLY_LEARNED
```

Temporary salience expires or decays with context unless a separate qualified plasticity process changes future salience policy.

## Coalition interaction

Salience may change the probability that a node or higher-order relation joins an active coalition. It does not by itself determine coalition output.

Example:

```text
unresolved sensory conflict
-> salience increase
-> recruit optics + current memory + cognition + resolver
-> bounded arbitration
```

The increased salience triggers resource allocation; it does not settle which sensory interpretation is true.

## Inhibition

Attention control may suppress distractor routes while preserving the underlying signal/state for later use where policy and resource constraints allow.

Inhibition must remain distinguishable from deletion, falsification, or durable forgetting.

## Resource competition

When several candidates compete for limited HC resources, arbitration may consider:

- urgency;
- expected information gain;
- goal relevance;
- uncertainty;
- potential consequence;
- time sensitivity;
- resource cost;
- subsystem health;
- dependency blocking;
- fairness/starvation constraints.

No single scalar is required to dominate all contexts.

## Failure modes

- repeated salience treated as objective importance or truth;
- threat/novelty monopolizes resources indefinitely;
- attention priority becomes action authority;
- low-salience but high-consequence evidence is dropped;
- self-reinforcing loop continuously amplifies its own salience;
- private salient material is broadcast outside scope;
- inhibition is mistaken for deletion;
- transient attention is promoted into durable identity state.

## Provenance

Reconciled from PR #4 `attention-salience/README.md` into the canonical `salience-attention/` root, preserving the existing correction/actionability architecture on `main` while adding general temporal-resource and coalition-recruitment semantics.