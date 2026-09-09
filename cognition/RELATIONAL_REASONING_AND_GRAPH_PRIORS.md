# Relational Reasoning and Graph Priors

Status: canonical cognition contract.

## Purpose

HC cognition may construct temporary graph- or hypergraph-shaped reasoning workspaces to compare entities, evidence items, hypotheses, plans, memories, percepts, candidate actions, or abstract task elements.

The topology of such a reasoning workspace controls which interactions are computed. It therefore matters—but it must not be confused with physical HC topology, current functional HC topology, or the actual relation structure of the external world.

The governing rule is:

> **A reasoning topology is a computational hypothesis or comparison plan unless separately supported as a claim about the world or HC itself.**

## Core separations

`REASONING_GRAPH_PRIOR != WORLD_RELATION_TRUTH`

`REASONING_GRAPH != HC_PHYSICAL_TOPOLOGY`

`REASONING_GRAPH != HC_CURRENT_EFFECTIVE_TOPOLOGY`

`FIXED_MESSAGE_PATH != DISCOVERED_CAUSAL_STRUCTURE`

`ATTENTION_WEIGHT != EPISTEMIC_AUTHORITY`

`RELATION_MESSAGE != TRUE_RELATION`

`CANDIDATE_SCORE != FACT`

`HIGHER_MODEL_SCORE != EFFECT_AUTHORITY`

## Reasoning workspace

A bounded reasoning episode may instantiate a workspace containing:

- participating objects/hypotheses/evidence items;
- roles for each participant;
- candidate pairwise comparison relations;
- candidate higher-order relations;
- source/provenance references;
- uncertainty;
- chronology/currentness;
- task or question scope;
- selected comparison topology;
- topology-construction rationale;
- intermediate relation messages;
- competing interpretations;
- candidate outputs and confidence;
- expiry/lifetime.

The workspace itself can be represented as a transient HC hypergraph object, but the objects **represented inside the workspace** remain semantically distinct from the HC substrate relations carrying the computation.

## Topology construction modes

Reasoning topology may be created by different methods, including:

- fully connected comparison;
- sparse heuristic comparison;
- spatial/grid/sequence adjacency;
- semantic-neighborhood retrieval;
- task-template relations;
- learned relation proposal;
- causal-model candidate relations;
- shared-source/provenance relations;
- temporal adjacency;
- hierarchical or cluster-local relations;
- explicit higher-order participant sets.

The topology-construction mode is part of provenance.

A fixed topology can be legitimate when the task definition itself establishes the comparison structure. It should not be generalized beyond that scope without evidence.

## Relation messages

A relation-processing component may compute a message from one or more participants and propagate it along a reasoning relation.

Such a message is a derived intermediate representation.

It may encode:

- similarity/difference;
- compatibility;
- constraint satisfaction;
- predicted interaction;
- causal hypothesis;
- spatial/temporal relation;
- support/opposition;
- role compatibility;
- utility or consequence estimate.

Its type and evidence origin must remain recoverable when consequential.

A learned message function is not allowed to turn representation strength into semantic truth by itself.

## Attention and gating

Attention weights, learned gates, routing probabilities, and comparison scores may allocate computational effort or weight candidate relations.

They do not themselves establish:

- truth;
- authority;
- consent;
- identity;
- causal fact;
- currentness;
- durable memory admission;
- action permission.

`ATTENDED_RELATION != TRUE_RELATION`

`LOW_ATTENTION != FALSE_RELATION`

Attention may prioritize examination without erasing low-weight alternatives when those alternatives remain decision-relevant.

## Multi-scale and multi-view reasoning

HC may reason over several representational scales or views.

A preferred pattern when scale/view identity matters is:

```text
source-local evidence
-> scale/view-local relational hypotheses
-> provenance-preserving cross-scale/view fusion
-> integrated candidate evaluation
```

This allows local structure to be processed before fusion and prevents immediate flattening from erasing disagreement or resolution-specific meaning.

`CROSS_SCALE_FUSION != SCALE_EQUIVALENCE`

`SHARED_REASONER != SHARED_SEMANTICS`

A shared processing mechanism can operate over different views without proving those views have identical ontology.

## Candidate-scoped reasoning

Some tasks are naturally evaluated by constructing a separate workspace for each candidate interpretation/action/answer and comparing the resulting scores.

Candidate-scoped computation must preserve the fact that each workspace is conditional on its candidate.

Evidence generated under one candidate's assumed topology cannot silently become unconditional fact.

`CANDIDATE_CONDITIONAL_RESULT != UNCONDITIONAL_BELIEF`

Competing candidates and their evidence should remain available until the governing arbitration process resolves the relevant scope.

## Learned hierarchy and modules

A reasoning component may learn clusters, communities, modules, or hierarchical abstractions to reduce complexity.

Those groupings are representation hypotheses unless separately established as protected or physical architecture.

`LEARNED_CLUSTER != FUNCTIONAL_ONTOLOGY_TRUTH`

`HIERARCHICAL_POOL != COGNITIVE_MODULE_PROOF`

`CLUSTER_ASSIGNMENT != AUTHORITY_DOMAIN`

Learned groupings can be revised through governed learning and should preserve enough lineage to identify what evidence and objective produced them.

## Relation to the HC temporal hypergraph

The HC temporal hypergraph is the architecture's formal model of the cognitive organ and its effective cognitive relations over time.

A reasoning workspace is an HC-internal transient object/process represented **within** that architecture.

Therefore:

- the HC fabric may instantiate a coalition that runs a reasoning workspace;
- the workspace may itself contain graph/hypergraph representations of a problem;
- those internal problem-representation edges/hyperedges are not automatically physical/logical/effective HC substrate edges/hyperedges;
- a reasoning output may propose changes to beliefs, plans, learned topology, or actions, but those proposals still pass through the governing admission/arbitration/authorization paths.

This prevents recursive graph notation from erasing semantic levels.

## Dependency lineage and corroboration

Multiple reasoning outputs may share upstream evidence, model initialization, retrieved memory, preprocessing, template, or generated state.

The system should preserve dependency lineage when independence matters.

`NUM_OUTPUTS != NUM_INDEPENDENT_SOURCES`

`REPLICA != INDEPENDENT_SOURCE`

`PERTURBED_COPY != INDEPENDENT_CORROBORATION`

Agreement among dependent reasoners can be useful evidence about model stability without being counted as independent real-world corroboration.

## Failure modes

- fully connected candidate graph is interpreted as proof every object is truly related;
- row/column/task adjacency leaks into the world model as causal structure;
- attention score is treated as confidence/truth without epistemic support;
- candidate-conditional relation becomes unconditional memory;
- learned cluster becomes permanent ontology or authority scope;
- scale-local disagreement disappears during concatenation/fusion;
- reasoning graph is confused with HC physical/effective topology;
- multiple replicas from one evidence source are counted as independent corroboration;
- a high-scoring candidate bypasses ordinary action authorization.

## Conformance questions

1. What does each node/participant in the reasoning workspace represent?
2. Why does each pairwise or higher-order comparison relation exist?
3. Is the topology fixed by the task, proposed heuristically, learned, or evidence-derived?
4. Is any reasoning relation being mistaken for a world or HC-topology fact?
5. Are attention/gating weights being treated as truth or authority?
6. Are scale/view identities and disagreements preserved through fusion?
7. Are candidate-conditional results clearly marked as conditional?
8. Are learned clusters/modules being promoted beyond their evidence?
9. Do apparently independent conclusions share upstream evidence or model lineage?
10. Does the output enter ordinary epistemic, memory, conative, and action-governance paths rather than bypassing them?

## Evidence provenance

This contract was informed by graph-based relational-reasoning and hierarchical-integration patterns studied in `basiralab/MSRGNN`, `basiralab/Dual-HINet`, and related graph-learning material, together with the established HC temporal-hypergraph, epistemic-control, multimodal-inference, and distributed-arbitration contracts.

The external methods demonstrate computational strategies within bounded tasks. They do not establish that their chosen reasoning graph topologies are biological mechanisms or canonical HC cognitive topology.

See `docs/research/BASIRA_FEDERATED_REPLICA_AND_RELATIONAL_REASONING_2026-09-09.md` for source-level observations and transfer limits.