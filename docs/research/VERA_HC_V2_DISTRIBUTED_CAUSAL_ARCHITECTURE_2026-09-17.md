# Vera HC V2 — Distributed/Causal Architecture Research Synthesis — 2026-09-17

Status: RESEARCH SYNTHESIS / NOT CANONICAL / NOT IMPLEMENTATION PROOF

## Question

What should HC Brain borrow from current network neuroscience and distributed-systems research to strengthen its temporal-hypergraph, recovery, and state-governance architecture without collapsing into a static graph, one universal consistency algorithm, or unsupported biological mimicry?

## Sources examined

### Hancock et al., 2025 — metastability review

Fran Hancock et al., “Metastability demystified - the foundational past, the pragmatic present and the promising future,” *Nature Reviews Neuroscience* 26(2):82-100 (2025), DOI `10.1038/s41583-024-00883-1`.

Source-supported lesson: healthy brain dynamics are often studied in terms of a balance between integration and segregation, and the review warns that “metastability” is frequently used heuristically or imprecisely. HC transfer: dynamic coalition formation should not be reduced to one scalar “metastability score.” If the term is used in HC qualification, the exact operational measure must be named and its claim scope bounded.

### Gallo et al., 2024 — temporal hypergraphs and memory

Luca Gallo, Lucas Lacasa, Vito Latora, Federico Battiston et al., “Higher-order correlations reveal complex memory in temporal hypergraphs,” *Nature Communications* 15, 4754 (2024), DOI `10.1038/s41467-024-48578-6`.

Source-supported lesson: temporal systems with group interactions can exhibit correlations across hyperedges of different orders and non-Markovian temporal structure. HC transfer: the repository’s decision to preserve higher-order coalition identity and history is defensible as a representation choice; however, temporal correlation or repeated coalition recurrence must not automatically become causal truth or durable plasticity.

### Greaves et al., 2025 — directed connectivity model dependence

Matthew D. Greaves, Leonardo Novelli, Sina Mansour L., Andrew Zalesky, Adeel Razi et al., “Structurally informed models of directed brain connectivity,” *Nature Reviews Neuroscience* 26:23-41 (2025), DOI `10.1038/s41583-024-00881-3`.

Source-supported lesson: conclusions about directed influence are strongly constrained by the inference/prediction model used, and reliability/out-of-sample validation remain important limitations. HC transfer: an executed route, inferred influence, or model-derived directed edge must retain model/estimator provenance. `DIRECTED_MODEL_EDGE != ESTABLISHED_CAUSAL_FACT`.

### NIST IR 8460 draft, 2023 — state-machine replication and consensus

Michael Davidson, “State Machine Replication and Consensus with Byzantine Adversaries,” NIST IR 8460 Initial Public Draft (2023), DOI `10.6028/NIST.IR.8460.ipd`.

Source-supported lesson: consensus/SMR are mechanisms for distributed processes to agree on command execution under an explicit fault/adversary model. HC transfer: “use consensus” is not an architecture requirement by itself. The HC must first declare which state family needs which semantic guarantee, then qualify whether the selected mechanism actually provides it under the implementation’s failure assumptions.

## Synthesis

### 1. Keep temporal higher-order structure, but separate representation from evidence

Current HC architecture is already ahead of a common failure mode: it does not treat a pairwise static graph as the whole brain. The research supports continuing to model transient higher-order configurations and their history.

The important hardening is epistemic:

`TEMPORAL_HYPEREDGE_PRESENT != WORLD_CAUSAL_RELATION_TRUE`

`RECURRENT_COALITION != DURABLE_PLASTICITY_COMMIT`

`MODEL_INFERRED_DIRECTION != OBSERVED_CAUSAL_DIRECTION`

The runtime should be able to say both “this coalition existed and shaped computation” and “the causal interpretation of why it mattered remains model-dependent.”

### 2. Metastability should become a qualification family, not a magic architectural variable

HC can benefit from the integration/segregation framing, but importing one scalar metastability measure would be premature. A stronger qualification bundle would compare several operational measures under perturbation and require them to agree only where theory justifies that expectation.

Suggested hostile bundle:

- same topology, different synchronization regime;
- same average synchrony, different switching/flexibility;
- high apparent metastability caused by noise;
- stable task-specialized coalition that should not be penalized for low switching;
- global synchronization that increases one metric while destroying specialization.

Failure condition: `ONE_METASTABILITY_METRIC_RELABELED_AS_GENERAL_COGNITIVE_HEALTH`.

### 3. State-family consistency is the correct distributed-systems abstraction

NIST’s survey reinforces that consensus guarantees are inseparable from the system/fault model. HC should therefore not say “the distributed organ uses consensus” globally.

Instead, each consequential state family declares semantics first:

- authority and consent state may need strong writer fencing;
- continuity-bearing memory may need strict currentness and explicit fork handling;
- append-only evidence can often tolerate concurrent admission if lineage remains intact;
- telemetry may allow labeled staleness;
- coalition scratch state may be local/ephemeral;
- effect receipts require duplicate/retry semantics strong enough to prevent non-idempotent replay.

Then an implementation chooses a mechanism—lease/epoch, quorum, SMR, mergeable state, designated continuity core, or another design—and qualification proves the mechanism satisfies the declared family contract.

### 4. Causal frontier should complement chronology

The HC chronology contract correctly distinguishes event, state, record, observation, and activation times. Distributed execution adds another need: semantic predecessor order.

A causal frontier should therefore be carried only where order matters for authority, continuity, reconciliation, or durable state. Wall clock remains metadata; it does not become a hidden consensus mechanism.

This provides a clean separation:

- chronology asks when;
- causal frontier asks depends-on-what;
- currentness asks which state is justified now;
- epistemics asks how well a proposition is supported;
- authority asks what may be done.

None substitutes for another.

### 5. Recovery should look more like a committed state transition than a loop of durable side effects

The current reference journal previously advanced recovery epoch and then persisted each unresolved-effect conversion separately. Distributed-systems and journaling principles both suggest the stronger semantic object is the recovery transaction itself.

HC V2 therefore represents one recovery fence binding:

`old epoch + exact set of REQUESTED effects -> new epoch + same set UNRESOLVED_AFTER_RESTART`.

A production implementation may encode that with one record, transaction framing, a committed manifest plus chunks, or an equivalent mechanism. Qualification should care about the observable atomic semantic boundary, not one specific storage algorithm.

## New research-derived qualification ideas

1. **Metastability measure divergence:** hold behavior fixed while varying the operational measure; prevent one metric from becoming architecture truth.
2. **Directed-edge estimator sensitivity:** same observations, multiple defensible directed-connectivity models; require model provenance and measure downstream route/plasticity sensitivity.
3. **Causal-frontier reorder:** inject clock skew and out-of-order delivery while preserving predecessor metadata; require semantic currentness to follow causal policy rather than timestamp.
4. **Partition policy substitution:** replace a strong-family mechanism with an eventually convergent one that passes happy-path tests; require conformance to fail because the declared semantics changed.
5. **Recovery-prefix attack:** persist only a prefix of a multi-step restart representation; require no externally usable state to expose a new epoch with unfenced prior effects.
6. **Higher-order recurrence laundering:** make one coalition recur frequently without positive outcome evidence; require recurrence not to become durable plasticity merely from frequency.

## Disposition

No external source reviewed here supplies a complete HC architecture. The useful transfer is narrower:

- keep higher-order temporal representation;
- preserve estimator/model dependence for inferred direction and influence;
- treat integration/segregation dynamics as a measurement family rather than one magic score;
- choose distributed mechanisms only after declaring state-family semantics;
- separate wall-clock chronology from causal ancestry;
- qualify restart as an atomic semantic boundary.

These findings support the V2 design in `docs/architecture/CAUSAL_AUTHORITY_RECOVERY_HARDENING_V2.md` and `docs/architecture/STATE_FAMILY_CONSISTENCY_AND_CAUSAL_FRONTIER.md`; they do not independently qualify those designs.
