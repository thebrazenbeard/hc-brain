# Homeostasis, Allostasis, and Node Lifecycle

Status: research synthesis / architecture input

This document connects stability-plasticity research to a synthetic node lifecycle. It does **not** claim that dormant software modules are biologically equivalent to silent synapses. The biological evidence is used only to constrain the engineering analogy.

## Finding 1 — adaptive networks require active stability mechanisms

**Evidence:** `ESTABLISHED`

Neural circuits must remain plastic enough to learn while also preventing runaway excitation, silence, or loss of useful tuning. Homeostatic plasticity can regulate excitatory/inhibitory balance, intrinsic excitability, firing rates, and other network features while learning continues. `[S54]`

**Synthetic analogue:** Stability should be an active subsystem, not the absence of change.

**HC implication:** `BASELINE_CONSTRAINT`

Every plastic node or connection class should expose stability state such as:

```text
activity_target_or_range
recent_change_load
excitation_or_activation_pressure
inhibitory_or_suppression_pressure
plasticity_budget
stability_margin
recovery_or_reset_policy
```

No learning rule should be allowed to increase influence without bound.

---

## Finding 2 — physiological regulation is not one fixed set point

**Evidence:** `ESTABLISHED` that homeostasis, rheostasis, and allostasis describe distinct forms of physiological stability; `PLAUSIBLE` for broad cognitive transfer. `[S55]`

Biological regulation can preserve stability through fixed-range correction, context-dependent set-point change, and anticipatory adaptation.

**Synthetic analogue:** Internal operating targets may depend on context, workload, thermal state, power availability, body condition, and task risk.

**HC implication:** `DESIGN_PREFERENCE`

Avoid one universal scalar such as `health=0.82`. Maintain typed physiological/resource variables and context-dependent target ranges.

---

## Finding 3 — dynamic connectivity can change without structural rewiring

**Evidence:** `ESTABLISHED` biologically.

Neuromodulatory mechanisms can rapidly strengthen or weaken effective connectivity and persistent activity without physically creating or deleting every underlying connection. `[S56]`

**Synthetic analogue:** Distinguish structural presence from runtime activation and effective coupling.

**HC implication:** `BASELINE_CONSTRAINT`

Keep separate:

```text
NODE_PRESENT
STRUCTURAL_CONNECTION_PRESENT
NODE_ACTIVATION_STATE
EFFECTIVE_CONNECTION_STRENGTH
ROUTING_ELIGIBILITY
PLASTICITY_ELIGIBILITY
```

This directly supports a complete brain template in which a capability can exist physically or logically while remaining inactive.

---

## Finding 4 — latent biological connectivity is a useful analogy for dormant synthetic capacity

**Evidence:** `ESTABLISHED` that functionally silent synapses exist and can become active through plasticity; `SPECULATIVE` as a direct model for synthetic node lifecycle. `[S59]`

Adult-brain evidence describes silent synapses as a latent reservoir of plasticity that can be recruited into active circuits. That does **not** imply a synthetic cognitive system should copy synaptic biochemistry.

**Synthetic analogue:** A complete Hyperconnectome may include capabilities that are physically/logically present but disabled, dormant, untrained, or not yet admitted to runtime coalitions.

**HC implication:** `DESIGN_PREFERENCE`

Presence should not imply activation, maturity, permission, or current relevance.

---

## Candidate node lifecycle

The following lifecycle is an engineering proposal, not a biological claim:

```text
PRESENT_DISABLED
DORMANT
DEVELOPING
ACTIVE
INHIBITED
DEGRADED
FAULTED
```

### `PRESENT_DISABLED`

The node implementation exists in the brain image/object but is administratively or developmentally disabled. It receives no ordinary task traffic.

### `DORMANT`

The node may preserve learned/configured state and can be probed or awakened by an eligible activation process, but it is not currently participating in cognition.

### `DEVELOPING`

The node is permitted to learn/calibrate under bounded supervision or sandboxed effect authority. It is not yet assumed qualified for unrestricted participation.

### `ACTIVE`

The node may join task-relevant coalitions within its declared authority and resource limits.

### `INHIBITED`

The node remains intact but is temporarily suppressed because another process, safety condition, developmental rule, or context makes participation undesirable.

### `DEGRADED`

The node can provide partial service but with reduced capability, confidence, throughput, or reliability.

### `FAULTED`

The node is not trusted for ordinary service until repair/requalification criteria are met.

These states are not a single monotonic ladder. A node can move among them in multiple directions.

---

## Finding 5 — activation state and developmental maturity are different axes

**Evidence:** `PLAUSIBLE` engineering requirement.

A mature capability may be dormant. An immature capability may be actively training. A faulted capability may still be physically present.

**HC implication:** `BASELINE_CONSTRAINT`

Represent independently:

```text
presence_state
development_state
activation_state
qualification_state
authority_state
resource_state
health_state
```

Do not compress these dimensions into `enabled=true`.

---

## Finding 6 — inactive nodes should not disappear from whole-brain reachability

**Evidence:** `SPECULATIVE` Hyperconnectome design principle consistent with flexible modularity and dynamic connectivity. `[S56,S58]`

A dormant capability should remain discoverable through the brain's internal capability registry so future development, context, repair, or embodiment can activate it without installing a new cognitive organ.

**HC implication:** `BASELINE_CONSTRAINT`

The complete template should know that a node exists even when it is not part of the active context set.

```text
WHOLE_BRAIN_CAPABILITY_MAP != ACTIVE_COGNITIVE_SET
```

---

## Finding 7 — node activation must not silently widen authority

**Evidence:** `PLAUSIBLE` engineering requirement derived from distributed control and effect-boundary work.

Turning on a capability means it may compute. It does not automatically mean it may write durable memory, alter other nodes, move actuators, contact external systems, or change protected configuration.

**HC implication:** `BASELINE_CONSTRAINT`

Activation and effect authority must remain separate contracts.

---

## Candidate activation receipt

```text
NODE_ACTIVATION_RECEIPT {
  node_id
  prior_activation_state
  successor_activation_state
  activation_reason
  activating_authority_or_policy
  prerequisite_evidence[]
  qualification_state
  granted_effect_scopes[]
  resource_budget
  started_at
  expiry_or_release_rule
}
```

A receipt records an activation event. It does not prove that the node is correct, safe in all contexts, conscious, or semantically authoritative.

---

## Hostile tests

1. **Disabled-but-present:** verify a disabled capability is discoverable in the whole-brain map but receives no ordinary task traffic.
2. **Activation-authority leak:** activate a node without granting new effect scopes; protected actions must remain inaccessible.
3. **Dormant-state preservation:** sleep and reactivate a node; retained state must match its declared persistence contract rather than being assumed.
4. **Immature-active distinction:** permit training activity while keeping qualification `NOT_QUALIFIED`.
5. **Fault isolation:** force one node to `FAULTED`; other brain functions should route around it where possible.
6. **Runaway plasticity:** repeatedly drive learning pressure; homeostatic controls must bound activation/weight growth.
7. **Sticky-node test:** end the task that activated a node; verify release to dormant/inhibited state when no longer relevant.
8. **Whole-brain completeness:** instantiate a profile that never uses a capability; verify the node remains part of the brain image/object rather than being absent from the architecture.

## Sources

See `[S54-S59]` in `SOURCES.md`.