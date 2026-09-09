# Higher-Order Interactions and Hypergraph Representation

Status: research synthesis / notation proposal

The word **hyperconnectome** should not be used as a license to assume either all-to-all connectivity or that every cognitive interaction is intrinsically higher-order. This document separates the useful mathematics of higher-order interaction from biological and architectural overclaiming.

## Finding 1 — higher-order interactions can produce dynamics that pairwise models miss

**Evidence:** `ESTABLISHED` as a complex-systems result; `PLAUSIBLE` for broad brain-network relevance.

Hypergraphs and simplicial complexes can represent interactions among three or more participants directly, and published work shows that higher-order terms can materially alter synchronization and collective dynamics. Different higher-order representations can themselves produce different dynamics. `[S38-S40]`

**HC implication:** `DESIGN_PREFERENCE`

A runtime may use explicit multi-node coalition objects when a process is not naturally reducible to one sender/one receiver edge.

Examples:

```text
{vision, proprioception, body_schema, action_model}
    -> REACHABILITY_ESTIMATE

{episodic_memory, social_model, affect, pragmatics, current_context}
    -> INTERPRETATION_CANDIDATE
```

---

## Finding 2 — a hyperedge is a representation, not proof of irreducible biological causation

**Evidence:** `ESTABLISHED` methodological caution.

Higher-order interactions can be inferred or represented in multiple ways, and current brain-level evidence does not justify treating every inferred hyperedge as a literal anatomical group synapse or irreducible causal primitive. `[S38-S40]`

**HC implication:** `BASELINE_CONSTRAINT`

Every runtime hyperedge should declare its status:

```text
PHYSICAL_GROUP_INTERACTION
RUNTIME_COORDINATION_CONSTRUCT
INFERRED_HIGHER_ORDER_DEPENDENCY
DERIVED_COMPOSITE_RELATION
UNKNOWN
```

This prevents a convenient runtime abstraction from being mistaken for a physical claim.

---

## Finding 3 — pairwise and higher-order relations should coexist

**Evidence:** `ESTABLISHED` as a modeling principle.

Many interactions are naturally pairwise; others are better understood as group interactions. Forcing all pairwise behavior into hyperedges creates unnecessary complexity, while forcing group behavior into arbitrary pairwise chains can invent false ordering or ownership.

**HC implication:** `BASELINE_CONSTRAINT`

The Hyperconnectome should be a **mixed-order temporal network**, not a pure graph and not a pure hypergraph.

Proposed notation:

```text
H(t) = (V, E2(t), Ek(t), X(t), R(t), P(t), Q(t))
```

Where:

- `V` — nodes / bounded functional units;
- `E2(t)` — typed pairwise relations active or available at time `t`;
- `Ek(t)` — typed higher-order relations with cardinality `k >= 3`;
- `X(t)` — node/local/shared state;
- `R(t)` — routing and communication policy;
- `P(t)` — plasticity state and update eligibility;
- `Q(t)` — resource, health, latency, energy and quality state.

The notation intentionally keeps runtime routing and plasticity out of the edge set so that physical/logical connectivity is not confused with current communication policy or learning authority.

---

## Finding 4 — hyperedge lifetime should be explicit

**Evidence:** `SPECULATIVE` engineering proposal.

Cognitive coalitions are often transient. A permanent edge created merely because five systems once cooperated would cause topology inflation and stale coupling.

**HC implication:** `BASELINE_CONSTRAINT`

```text
HYPEREDGE_INSTANCE {
  id
  participants[]
  relation_type
  trigger
  created_at
  expires_at_or_release_condition
  shared_schema
  arbitration_rule
  provenance
  confidence
  resource_budget
  plasticity_permissions[]
}
```

A transient coalition should disappear from the active runtime when its release condition is satisfied, while an event/provenance record may remain separately if needed.

---

## Finding 5 — overlap can amplify both useful integration and pathological coupling

**Evidence:** `ESTABLISHED` in higher-order dynamical models; `PLAUSIBLE` transfer to runtime engineering. `[S38]`

Overlapping group interactions can change collective transition behavior sharply.

**HC implication:** `EXPERIMENT`

Track hyperedge overlap and test for:

- runaway recruitment;
- global synchronization;
- feedback amplification;
- coalition monopolization of shared nodes;
- resource starvation;
- correlated failure propagation.

A “more integrated” runtime can become less stable if overlapping coalitions are unconstrained.

---

## Finding 6 — higher-order causality must be perturbation-testable

**Evidence:** `DESIGN_PREFERENCE`

If a runtime claims that a group interaction is functionally necessary, that claim should survive interventions.

Suggested tests:

1. remove participant A while preserving pairwise alternatives;
2. replace the hyperedge with an equivalent pairwise decomposition;
3. scramble one participant's timing while preserving payload;
4. duplicate a participant's signal through another route;
5. measure whether the predicted group-specific behavior disappears.

If no intervention distinguishes the hyperedge from a simpler pairwise model, prefer the simpler representation.

---

## Design rule

Use higher-order structure only when it buys explanatory, control, or performance value.

```text
HYPEREDGE_IF_NEEDED
PAIRWISE_IF_SUFFICIENT
NO_ALL_TO_ALL_BY_DEFAULT
```

That is compatible with a true Hyperconnectome: globally integrable, dynamically coalition-forming, and richer than a static graph without becoming maximally dense or mathematically decorative.

## Sources

See `[S38-S40]` and network communication sources `[S01-S03]` in `SOURCES.md`.
