# HC Topology Design Constraints

Status: canonical architecture design contract.

## Purpose

This document constrains the physical and effective topology of HC-series implementations without reducing the HC temporal hypergraph to a simple static graph or importing human hemispheric gross anatomy.

The HC is canonically a typed, attributed, multilayer temporal hypergraph. Physical wiring, logical eligibility, configured routing, transient higher-order coalitions, modulatory state, and learned plastic structure are different planes of that architecture.

## Selective hyperconnectivity

`HYPERCONNECTOME != ALL_TO_ALL_WIRING`

The term `Hyperconnectome` denotes unusually rich, adaptive, cross-system integration. It does not require every substrate element to connect directly to every other element.

A conforming implementation may use:

- dense local connectivity where local recurrence is useful;
- sparse or selective long-range pathways;
- redundant alternate routes for critical functions;
- high-capacity interregional tracts or links;
- adaptive routing and gating;
- dynamic higher-order coalitions instantiated only when context requires them;
- learned changes to effective topology over time.

The architecture should prefer the minimum connectivity that supports the required functional reachability, resilience, timing, and learning envelope rather than maximizing edge count as an end in itself.

`MORE_CONNECTIONS != MORE_INTELLIGENCE`

## Physical topology versus effective topology

The physical substrate determines what communication is possible, not what communication is active or authorized at a given moment.

A useful distinction is:

```text
physical substrate reachability
-> learned logical eligibility
-> configured routing/bindings
-> current effective pairwise relations
-> current higher-order hyperedges/coalitions
```

These layers must not be collapsed.

A physically available path may be dormant, inhibited, unlearned, quarantined, unauthorized, or irrelevant. Conversely, a functional higher-order coalition may span many regions without requiring a unique dedicated physical wire for that coalition.

## Timing is structural meaning

Conduction delay, processing latency, synchronization window, recurrence, persistence, onset/offset, and ordering are part of effective topology semantics.

Two implementations with identical reachability but materially different timing may implement different effective cognitive organizations.

The architecture therefore treats timing as more than transport metadata.

`SAME_REACHABILITY != SAME_EFFECTIVE_TOPOLOGY`

## Integration without pathological global coupling

The design goal is high integration with bounded synchronization, not global simultaneous activation.

A conforming implementation should support:

- local recurrent processing;
- selective global availability where useful;
- temporary coalition formation;
- inhibition and gating;
- resource-aware scheduling;
- fault isolation;
- competing interpretations/actions without forced global consensus;
- synchronization only at the granularity needed by the participating process.

A mechanism that requires the whole HC to enter one globally synchronized state for ordinary cognition should be treated as a design risk rather than the default architecture.

## Redundancy and graceful degradation

Critical capability should not depend on a single fragile route when the substrate can reasonably provide alternatives.

Redundancy may exist through:

- multiple physical paths;
- alternate functional coalitions;
- duplicated or distributed representations;
- fallback processing substrates;
- rerouting after local damage;
- relearning after changed latency or topology.

Redundancy does not mean every representation must be duplicated identically. Different paths may provide degraded, slower, narrower, or differently uncertain fallback behavior.

`REDUNDANT_PATH != IDENTICAL_CAPABILITY`

## Non-hemispheric organization

No HC generation requires left/right hemispheric decomposition, a corpus-callosum analogue, or bilateral copies of human functional regions.

Human anatomical terms may be used as mechanism analogies, but analogy does not impose location, bilateral duplication, or human tract geometry.

Preferred implementation descriptions identify the functional substrate and the exact regions/systems connected rather than relying on inherited human gross-anatomical shorthand.

## Regional specialization

Functional specialization is compatible with distributed cognition.

An implementation may contain specialized neural, hybrid, photonic, memory, endocrine, interoceptive, sensory, motor, or control substrates. Specialization does not make any one region the executive person or sole cognitive center.

A region may be:

- singular with internal redundancy;
- replicated as cooperating modules;
- physically distributed;
- topologically clustered;
- dynamically recruited into different coalitions;
- bypassed or degraded under fault conditions.

The exact packaging is implementation-specific.

## Cross-generation rule

HC-1 establishes the complete non-hemispheric cognitive topology.

HC-2 adds specialized accelerator substrate without creating a second cognitive side or separate executive lobe. Accelerator access appears in the HC temporal hypergraph as typed internal service relationships and transient task coalitions.

HC-3 adds richer distributed physiological affective substrate without creating an isolated emotion center. Endocrine, autonomic, interoceptive, affective, memory, salience, conative, and sensorimotor processes remain distributed and dynamically coupled.

## Physical-media neutrality

The architecture may be realized through neural tissue tracts, bioelectronic interfaces, photonic links, conventional electronic interconnects, or other qualified media.

Media choice changes latency, bandwidth, energy, fault, calibration, and maintenance properties, but does not by itself decide semantic authority or cognitive ownership.

## Conformance questions

A topology design should be able to answer:

1. Which physical routes are possible?
2. Which logical relationships are eligible to form over those routes?
3. Which routes are configured or learned now?
4. Which pairwise and higher-order relations are effective now?
5. What timing assumptions are required for each material process?
6. Which critical functions have alternate routes or fallback coalitions?
7. Which local failures can be isolated without global cognitive halt?
8. Does any region or route accidentally become a permanent homuncular executive?
9. Has human anatomical analogy silently reintroduced hemispheric constraints?
10. Does any claim of `hyperconnectivity` merely mean maximal edge count without functional justification?

## Evidence boundary

Selective connectivity, distributed networks, conduction delays, synchronization, and plasticity are grounded in real neuroscience and network science, but this document is an HC architecture contract rather than a claim that the complete HC topology is presently implemented or biologically demonstrated at synthetic-organ scale.

## Provenance

Selectively reconciled from PR #2 `docs/architecture/HYPERCONNECTOME_TOPOLOGY.md` with the canonical temporal-hypergraph model, connectivity planes, Noöplex Fabric, distributed arbitration, lifecycle rules, and evidence boundary. The source branch's static weighted-multigraph abstraction was not promoted as the HC's formal model, and language permitting a central integration core was not retained because current canon rejects a homuncular executive.
