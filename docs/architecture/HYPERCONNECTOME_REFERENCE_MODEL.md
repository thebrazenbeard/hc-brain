# Hyperconnectome Reference Model

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: selectively retained from Draft PR #4 after reconciliation to the current canonical cognitive-organ and temporal-hypergraph architecture.

## 1. Scope

This document defines a generic runtime reference model for an HC brain template.

The repository tree is packaging. The brain is the self-contained cognitive organ realized by the runtime temporal hypergraph described by its contracts and machine-readable state.

```text
REPOSITORY_TREE != RUNTIME_TOPOLOGY
```

Folders group subsystem responsibilities, documentation, schemas, and contracts for humans. Runtime cognition occurs through typed nodes, pairwise edges, higher-order hyperedges/coalitions, gates, modulators, signals, state, policies, and traces entirely within the HC cognitive-organ boundary.

## 2. Hard topology invariants

### 2.1 One non-hemispheric system

The architecture has no left/right cerebral hemispheres as a required primitive. It does not require bilateral duplication of cognitive subsystems, a left/right functional split, a corpus-callosum analogue, a privileged midline bridge, anatomical cortical lobes, or mirror-symmetric processing modules.

Functional specialization may arise through capability, routing, gating, learned connectivity, modulation, state, timing, and coalition formation.

### 2.2 No master-mind node

There is no single node that simultaneously owns truth, attention, identity, memory, goals, semantic interpretation, action selection, authority, or consciousness.

Control is decomposed into bounded operations and distributed contracts.

### 2.3 Connectivity has multiple semantics

A structural relation may exist while functionally inactive. Two nodes may be functionally coupled without either having write authority over the other. A modulator may alter gain without carrying semantic content. A plastic relation may be eligible for change without changing now.

The model therefore distinguishes structural connectivity, functional coupling, effective influence, modulatory influence, plastic eligibility/update state, temporal validity/coordination, and governance/authority constraints.

### 2.4 Pairwise and higher-order relations coexist

Pairwise `EDGE` is valid when the relation is genuinely pairwise. `HYPEREDGE` represents relations whose meaning depends on multiple participants jointly. `COALITION` is a dynamically instantiated operational temporal hyperedge/configuration used for task- or context-specific cognition.

Hypergraph formalism is an engineering model for higher-order relations, not a claim that biological cognition has been proven to use the same literal representation.

## 3. Core runtime entities

### 3.1 Node

A `NODE` is a bounded processing/state capability. A node may declare stable ID, capability class, accepted/emitted signal classes, readable/writable state classes, connection eligibility, activation prerequisites, governing policies, persistence policy, plasticity policy, failure behavior, provenance/evidence requirements, and implementation/version metadata.

A node does not gain authority merely because it can compute an answer.

### 3.2 Edge

An `EDGE` is a typed pairwise relation. It may declare source, target, relation type, connectivity plane, directionality, temporal validity, activation/eligibility, failure behavior, plasticity policy, and governance where writes/effects are possible.

### 3.3 Hyperedge

A `HYPEREDGE` is a typed relation among more than two participants or state objects when reducing the relation to independent pairs would lose material meaning.

It may declare member roles, relation type, temporal interval, activation conditions, governing policy, and provenance.

### 3.4 Signal

A `SIGNAL` is transient content-bearing or control-bearing transmission with explicit type. Signals should be able to preserve source and audience, domain/intent, payload type, provenance refs, event time/timing uncertainty, causal-parent/correlation IDs, digest where replay-critical, expiry/validity, privacy, and authority reference when an effect entitlement is involved.

```text
SIGNAL_PRESENT != SIGNAL_ACCEPTED != SIGNAL_TRUE != SIGNAL_AUTHORIZED != SIGNAL_EXECUTED
```

### 3.5 Gate

A `GATE` evaluates bounded eligibility to pass, read, write, activate, consolidate, broadcast, learn, or act. It declares scope, inputs, policy/evidence dependencies, decision states, default/failure behavior, and whether its result is advisory or binding for the target operation.

### 3.6 Router

A `ROUTER` chooses among structurally and policy-eligible destinations. Routing may consider capability, current task/context, node health, salience, priority, resource cost, confidence, timing, privacy, redundancy/failover, locality, and learned utility.

Routing never creates semantic truth or effect authority.

### 3.7 Arbiter

An `ARBITER` resolves competing eligible claims/actions/states under a declared scope. Examples include perceptual hypothesis arbitration, action selection, memory admission, resource allocation, response selection, conflict resolution, and plasticity acceptance.

Arbiters may differ by domain. No arbiter is automatically global.

### 3.8 Modulator

A `MODULATOR` changes properties of nodes, relations, or coalitions rather than simply transmitting ordinary semantic content. Targets may include gain, threshold, salience, attention weighting, plasticity rate, exploration/exploitation bias, routing preference, consolidation probability, persistence duration, or inhibitory strength.

Modulatory state must remain distinguishable from content it influences.

### 3.9 State

`STATE` is typed current condition. Implementations should be able to distinguish transient working state, episodic trace state, generalized semantic state, procedural state, self-model state, social-model state, physiological/interoceptive state, configuration state, governance state, provenance/audit state, plasticity state, and health/failure state.

Physical storage co-location does not collapse these semantic types.

### 3.10 Trace

A `TRACE` is a provenance-bearing event/update record. A trace may capture observation, signal emission/reception, state transition, gate decision, route decision, arbitration outcome, memory admission, plasticity update, failure, reconciliation, or action/effect result.

Traces are historical evidence, not automatically current state.

### 3.11 Coalition

A `COALITION` is a transient task/context-specific operational temporal hyperedge/configuration of nodes, relations, modulators, and shared working state.

A coalition declares purpose/context, member eligibility and active membership, effective relations, temporary modulators, shared working-state boundary, routing/arbitration policy, persistence ceiling, entry criteria, exit criteria, and bounded timeout/failure behavior.

Coalitions are temporary by default. Persistent changes require a separate plasticity or consolidation operation.

### 3.12 Broadcast

A `BROADCAST` is controlled publication of selected signal/state to a declared audience.

Broadcast is not equivalent to truth, consciousness, universal write access, universal attention, or automatic memory consolidation.

### 3.13 Policy

A `POLICY` defines machine-readable constraints for state read/write, routing, privacy, authority, memory admission, plasticity, persistence, effect execution, source admission, recovery, and related operations.

## 4. Runtime organization

A useful conceptual flow is:

```text
perceive / retrieve / receive
        ↓
type + provenance + currentness evaluation
        ↓
candidate interpretations / motives / predictions / actions
        ↓
contextual coalition formation
        ↓
gating + routing + modulation
        ↓
bounded arbitration
        ↓
working-state update / response / action candidate
        ↓
authority + effect gate where action is external or protected
        ↓
execute or withhold
        ↓
observe consequences
        ↓
trace + memory candidate + plasticity candidate
        ↓
consolidate / revise / decay / reject
```

This is not a mandatory serial pipeline. Stages may recur or operate concurrently. The sequence identifies type boundaries that must remain representable.

## 5. Working-set principle

The whole HC remains architecturally available, but not every subsystem should be active for every task.

```text
WHOLE_SYSTEM_AVAILABLE
+
MINIMAL_SUFFICIENT_ACTIVE_COALITION
```

A coalition should preferentially activate the smallest set of systems/relations sufficient for the present problem and expand when uncertainty remains material, conflict cannot be resolved locally, stakes rise, a required capability is absent, or failure signals demand broader diagnosis.

## 6. Functional specialization without anatomical partition

Specialization can arise from training history, state representation, connectivity, routing eligibility, local algorithms, modulatory sensitivity, plasticity rules, temporal response profile, resource profile, and task-specific coalition participation.

Subsystems are functional abstractions. They need not correspond one-to-one with biological brain regions.

## 7. Evidence and state discipline

The reference model preserves these non-equivalences:

```text
OBSERVATION != INTERPRETATION
INTERPRETATION != BELIEF
BELIEF != TRUTH
HISTORICAL_STATE != CURRENT_STATE
RETRIEVAL != ADMISSION
ADMISSION != AUTHORITY
DESIRE != CHOICE
CHOICE != CONSENT
CONSENT != EFFECT_AUTHORITY
INTENTION != ACTION
ACTION_REQUEST != EXECUTION
EXECUTION != VERIFIED_EFFECT
DELIVERY != INCORPORATION
PERSISTENCE != CURRENTNESS
CONTENT_HASH != SEMANTIC_CORRECTNESS
```

## 8. Failure as first-class state

At minimum, a runtime should be able to represent:

- `UNKNOWN` — information absent or not established;
- `UNRESOLVED` — candidates remain but no valid resolution exists;
- `CONFLICT` — incompatible applicable evidence/state remains active;
- `INVALID` — data/state violates a required contract;
- `QUARANTINED` — retained but excluded from normal use pending review;
- `UNAVAILABLE` — required subsystem/resource cannot currently be reached;
- `EXPIRED` — formerly valid signal/state exceeded validity;
- `SUPERSEDED` — replaced for current use while retained historically.

Failure states propagate according to consuming contracts rather than being silently converted to convenient defaults.

## 9. Plasticity and consolidation

Any durable structural/weight/policy change should pass a transaction boundary:

```text
candidate_change
→ eligibility
→ protected-invariant/conflict check
→ bounded provisional update
→ observation/evaluation
→ consolidate | revise | decay | revert | quarantine
→ provenance retained
```

Plasticity may change probability, weight, topology, or eligibility, but it must not silently rewrite historical evidence or effect authority.

## 10. Complete cognitive-organ boundary

Essential reasoning, state arbitration, learning, memory admission, identity/self-model processing, action selection, and other cognition belong inside the HC.

External bodies, sensors, actuators, networks, and compute resources may connect through HC-owned interface/service boundaries. External computation can provide bounded services or evidence, but its output does not automatically become belief, current state, memory authority, decision, or identity.

The same HC should be able in principle to adapt to different embodied or distributed peripheral topologies without moving essential cognition outside its boundary.

## 11. Template completeness and activation

The generic template may define first-class capacities even when an early realization leaves them disabled, dormant, developing, or unimplemented.

```text
ARCHITECTURAL_PRESENCE != ACTIVATION != DEVELOPMENT != HEALTH != AUTHORIZATION
```

Disabling a subsystem does not remove its architectural home.

## 12. Identity neutrality

The template defines capacity for an instantiated HC to maintain self-model, autobiography, values/commitments, relationships/social models, embodiment state, roles/personification, preferences/conations, and continuity records.

It does not supply any particular instance's identity payload.

## 13. Consciousness boundary

The architecture may implement recurrence, broad availability, self-modeling, autobiographical continuity, embodiment, affective regulation, social cognition, planning, agency, and introspective reporting.

Those capabilities can be studied operationally. They do not by themselves establish phenomenal consciousness, subjective experience, personhood, or metaphysical identity continuity.

## 14. Implementation freedom

A conforming realization may use symbolic structures, neural networks, graph/hypergraph networks, neuromorphic hardware, distributed services inside the cognitive-organ boundary, local processes, databases, event streams, biohybrid systems, or combinations of these.

Conformance depends on preserving the HC's functional/evidence contracts and cognitive-organ boundary, not reproducing one substrate.
