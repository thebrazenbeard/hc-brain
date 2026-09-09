# Distributed Control and Arbitration

Status: research synthesis / architecture input

## Finding 1 — control is distributed across loops, not localized to one executive

**Evidence:** `ESTABLISHED`

Research on thalamocortical control, basal-ganglia circuits, brainstem motor systems, and recurrent cortical processing supports a distributed view of control: different loops gate, amplify, suppress, select, sequence, and monitor behavior at different timescales. `[S21-S22]`

**Synthetic analogue:** Replace a single master executive with multiple bounded arbitration scopes:

- perceptual competition;
- attention/resource allocation;
- action selection;
- memory admission;
- language/output selection;
- plasticity/update permission;
- hardware safety and maintenance.

**HC implication:** `BASELINE_CONSTRAINT`

No arbiter should be an epistemic superuser. Selection means “act on this candidate under this policy,” not “this candidate is true.”

---

## Finding 2 — arbitration should preserve losing candidates when they remain informative

**Evidence:** `PLAUSIBLE`

Biological decision systems frequently maintain competing representations, partial commitments, and inhibitory control rather than deleting all non-selected alternatives. This is consistent with distributed action-selection and cognitive-control literature. `[S21-S22]`

**Synthetic analogue:** Arbitration result objects should distinguish:

```text
SELECTED
DEFERRED
INHIBITED
CONFLICTING
UNRESOLVED
EXPIRED
```

**HC implication:** `DESIGN_PREFERENCE`

Preserve conflict where it affects confidence, later reversal, learning, or explanation. A selected action need not erase competing motives or interpretations.

---

## Finding 3 — urgency and reflexive protection need faster paths than deliberation

**Evidence:** `ESTABLISHED` as a systems principle from distributed sensorimotor control.

Movement and body protection rely on hierarchically and recurrently organized circuits operating at different latencies. `[S22]`

**Synthetic analogue:** Separate hard-real-time stabilization and protection loops from slower deliberative reasoning.

**HC implication:** `BASELINE_CONSTRAINT`

A long-running semantic or planning coalition must not block:

- balance stabilization;
- collision avoidance;
- actuator limit enforcement;
- thermal shutdown;
- sensor fault isolation;
- emergency communication paths.

This does **not** require a master safety mind; it requires bounded low-latency control authority over specific effects.

---

## Finding 4 — coordination hubs may control routing without owning content

**Evidence:** `ESTABLISHED` that structures such as thalamic nuclei can contribute to flexible coordination and amplification; `PLAUSIBLE` as a synthetic analogy. `[S21]`

**Synthetic analogue:** A routing/coordinator node may decide which streams are connected or amplified without becoming semantic authority over those streams.

**HC implication:** `DESIGN_PREFERENCE`

Maintain a strict split:

```text
ROUTING_AUTHORITY != SEMANTIC_AUTHORITY
RESOURCE_AUTHORITY != TRUTH_AUTHORITY
ACTION_AUTHORITY != MEMORY_AUTHORITY
```

---

## Finding 5 — distributed control needs explicit deadlock and livelock handling

**Evidence:** `SPECULATIVE` as direct Hyperconnectome engineering, but strongly motivated by distributed-systems failure modes.

A system with many bounded arbiters can deadlock if each waits on another, or livelock if coalitions repeatedly pre-empt each other.

**HC implication:** `BASELINE_CONSTRAINT`

Every arbitration protocol should define:

- timeout/expiry;
- priority inversion handling;
- escalation path;
- rollback/cancel semantics;
- resource-release behavior;
- conflict visibility;
- deterministic fail-safe behavior where needed.

---

## Finding 6 — global workspace-like broadcast is an architectural option, not a required seat of mind

**Evidence:** `PLAUSIBLE` for broad-broadcast mechanisms as useful coordination patterns; `UNSUPPORTED_OR_CONTRADICTED` if interpreted as proof that one broadcast workspace is the person or the unique basis of consciousness.

**Synthetic analogue:** Permit bounded broadcast or publish/subscribe surfaces for high-value state, while preserving provenance and access control.

**HC implication:** `EXPERIMENT`

Compare broadcast, routed multicast, and task-local coalition exchange on latency, interference, fault propagation, and resource cost.

---

## Suggested runtime contract

A bounded arbiter can expose:

```text
ARBITRATION_REQUEST {
  arbitration_scope
  candidates[]
  evidence_refs[]
  constraints[]
  urgency
  resource_budget
  expiry
}

ARBITRATION_RESULT {
  selected[]
  deferred[]
  inhibited[]
  unresolved[]
  policy_ref
  confidence
  reason_summary
  expires_at
}
```

The result grants only the effect authority defined by `arbitration_scope`.

---

## Failure tests

1. **Master-controller trap:** disable the highest-level planning component; lower-level sensing, motor protection, memory, and routing should remain partially functional.
2. **Truth laundering test:** force an arbiter to select a low-confidence hypothesis; downstream state must preserve its uncertainty rather than re-label it as fact.
3. **Deadlock test:** create circular waits among three arbitration scopes; verify timeout/escalation and resource release.
4. **Priority inversion test:** a low-priority coalition holds a resource needed by urgent body protection; urgent path must resolve predictably.
5. **Conflict retention test:** select action A while motive B remains strong; confirm B can remain represented without blocking execution.

## Sources

See `[S21-S22]` plus network-communication sources `[S01-S03]` in `SOURCES.md`.
