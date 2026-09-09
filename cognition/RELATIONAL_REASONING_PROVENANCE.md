# Relational Reasoning Provenance

Status: canonical identity-neutral architecture contract.

## Purpose

The HC may use graphs, hypergraphs, learned relation vectors, candidate-specific coalitions, attention gates, multiple representation scales, retrieved schemas, and other relational structures to reason. Those computational structures must not silently acquire stronger epistemic meaning than their provenance supports.

This contract separates **how cognition is allowed to compare or combine information** from **what the HC has evidence is true about the world**.

## Core distinctions

`REASONING_GRAPH_PRIOR != INFERRED_WORLD_RELATION`

`ALLOWED_MESSAGE_PATH != OBSERVED_RELATION`

`CANDIDATE_CONDITIONED_REPRESENTATION != CANDIDATE_INDEPENDENT_WORLD_STATE`

`MULTIPLE_DERIVED_VIEWS != MULTIPLE_INDEPENDENT_OBSERVATIONS`

`FUSED_CORRELATED_FEATURES != INDEPENDENT_CORROBORATION`

`ATTENTION_WEIGHT != EVIDENCE_STRENGTH_BY_DEFAULT`

`ATTENTION_WEIGHT != CAUSAL_IMPORTANCE`

`ATTENTION_WEIGHT != EXPLANATION`

`MULTIPLE_AGGREGATORS != INDEPENDENT_EVIDENCE`

## Reasoning topology versus world topology

A reasoning topology may be introduced because it is computationally useful. Examples include:

- allowing comparisons among particular nodes;
- fully connecting a bounded candidate set;
- encoding spatial adjacency as a useful prior;
- importing a known schema or ontology;
- constructing a temporary task graph;
- activating a coalition around a current hypothesis;
- selecting a learned communication route.

Such a topology can constrain or facilitate computation without asserting that every computational relation exists externally.

Each material reasoning relation should therefore be classifiable as one or more of:

- `STRUCTURAL_PRIOR` — installed or learned permission/expectation about useful connectivity;
- `OBSERVATION_DERIVED` — inferred from current or historical observation;
- `HYPOTHESIS_CONDITIONED` — exists because a candidate explanation, plan, or answer is being evaluated;
- `SIMULATION_INTERNAL` — instantiated inside counterfactual or predictive simulation;
- `ONTOLOGY_OR_SCHEMA` — imported conceptual relation with its own source/scope;
- `ROUTING_OR_GATING` — controls computation without claiming external truth;
- `WORLD_MODEL_CLAIM` — an explicit current claim about external or internal state, with evidence and uncertainty.

The same endpoints may participate in several relation classes simultaneously. Their semantics must not be collapsed merely because the topology is visually identical.

## Candidate-conditioned structures

Cognition frequently evaluates alternatives by temporarily constructing a representation that includes one candidate, hypothesis, plan, interpretation, or predicted future at a time.

Any state created under such conditioning should retain:

- candidate or hypothesis ID;
- source evidence snapshot;
- construction rule/model version;
- temporal scope;
- uncertainty;
- relation class;
- whether the representation was observed, inferred, simulated, or imposed as a prior.

A candidate-conditioned relation may contribute to scoring that candidate but must not be committed as unconditional current world state merely because the candidate scored highest.

Selection can justify a later belief update only through the governing epistemic/admission process.

## Multi-view and multi-scale ancestry

The HC may derive many representations from one source observation: different spatial scales, embeddings, transforms, crops, filters, frequency bands, temporal windows, summary statistics, or model heads.

These representations can add useful features without creating independent evidence ancestry.

Evidence accounting must distinguish:

- `SOURCE_ANCESTRY_GROUP` — the underlying observation/event lineage;
- `DERIVATION_PATH` — transformation chain from source to representation;
- `REPRESENTATION_VIEW` — the current transformed view;
- `INDEPENDENCE_STATUS` — whether support is genuinely independent for the claim being evaluated.

Independent corroboration requires independence relevant to the claim, not merely separate tensors, modules, aggregators, prompts, or feature branches.

## Attention and gating semantics

Attention, salience, routing, gating, and mixture weights are operational control variables unless separately validated for stronger interpretation.

An attention/gating trace may legitimately answer questions such as:

- which messages were weighted more heavily by this mechanism;
- which routes were open;
- which components materially contributed to the forward computation;
- how the model allocated processing under the recorded snapshot.

It does not automatically answer:

- which input was most true;
- which relation was causal;
- which fact is most important in the world;
- which source deserves higher epistemic trust;
- why the system should be believed;
- whether an action is authorized.

If a subsystem wants to promote an attention-like quantity into evidence reliability, causal importance, explanation, or authority, that semantic promotion requires its own scope-appropriate validation and governing contract.

## Aggregation and fusion

Mean, max, sum, voting, ensemble combination, feature concatenation, message aggregation, and cross-scale fusion may combine representations. Aggregation does not erase source ancestry.

A fusion object should preserve enough provenance to answer consequential questions about:

- what source observations contributed;
- which derived views share ancestry;
- which transformations were applied;
- which candidate/hypothesis context was active;
- whether any contributor was stale, simulated, inferred, or generated;
- what model/routing snapshot produced the fusion.

Where element-level provenance matters, use the composite-provenance contract rather than assigning one coarse source label to a heterogeneous object.

## Temporal-hypergraph relationship

The HC's temporal hypergraph contains both cognitive machinery and cognitive content. Therefore hypergraph membership alone does not determine epistemic status.

A hyperedge can represent, for example:

- a temporary processing coalition;
- a schema relation;
- a candidate-conditioned reasoning structure;
- a simulated interaction;
- an inferred world relation;
- a currently admitted state relation.

These must remain type-distinguishable even when they share participants.

`PRESENT_IN_HC_HYPERGRAPH != ESTABLISHED_AS_WORLD_FACT`

Likewise, plasticity that makes a route easier to activate does not by itself strengthen the truth of claims that happen to use that route.

`ROUTE_STRENGTH != CLAIM_CONFIDENCE`

## Social and pragmatic application

A relationship schema, social-role prior, stereotype, cultural norm, or predicted interaction pattern can guide hypothesis generation without becoming a current fact about a particular person or interaction.

`SOCIAL_SCHEMA != INDIVIDUAL_FACT`

`PREDICTED_RELATION != CURRENT_RELATIONSHIP_STATE`

`RELATIONAL_SCORE != CONSENT`

`RELATIONAL_SCORE != AUTHORITY`

Explicit social correction, current evidence, consent, privacy scope, and authority remain governed by their own systems.

## Failure modes

- installed graph template treated as observed external topology;
- candidate-conditioned relation written into current memory without removing the conditioning scope;
- three transforms of one camera frame counted as three independent witnesses;
- attention heatmap presented as causal explanation without validation;
- a high routing weight used as semantic confidence;
- multiple pooling operations interpreted as independent corroboration;
- learned route strength converted directly into belief probability;
- ontology/schema edge treated as current instance evidence;
- selected answer causing all internal features used to score it to be retroactively labeled true;
- social-relation prediction becoming consent or authority.

## Adversarial conformance tests

A conforming implementation should be challengeable with at least:

1. **Prior/world-topology separation** — change a reasoning topology prior while holding observations fixed; verify no new observation/world-fact event is created solely by the topology change.
2. **Candidate conditioning** — evaluate mutually exclusive candidates; verify candidate-specific intermediate relations remain scoped to their candidate and losing-candidate state is not rewritten as observation.
3. **Correlated-view duplication** — derive many representations from one source; verify independent-support count does not increase merely because representation count increases.
4. **Attention inversion** — force or learn a high attention gate on low-reliability evidence; verify attention cannot directly confer truth, causality, consent, or authority.
5. **Aggregator multiplication** — summarize the same state with several aggregators; verify they remain within the same ancestry group unless genuinely independent evidence enters.
6. **Schema-instance separation** — supply a strong prior/schema relation that conflicts with current evidence; verify the system can preserve the prior while rejecting it as the current instance state.
7. **Route/belief separation** — strengthen a learned communication path without adding evidence; verify claim confidence does not increase solely because routing became easier.

## Interfaces

Strong interfaces are expected with:

- temporal-hypergraph runtime and routing;
- epistemic cognitive control;
- perception and multimodal inference;
- imagination/simulation;
- salience-attention;
- semantics and pragmatics;
- social modeling and empathy;
- memory/current-state selection;
- distributed arbitration;
- composite representation provenance;
- qualification/evidence lineage.

## Evidence boundary

This is an HC architectural contract. The distinctions are generalized from existing HC epistemic/provenance rules plus code-level study of a relational GNN architecture where fixed graph templates, candidate-conditioned graphs, shared-source multi-scale representations, learned attention gates, and multiple aggregators are explicit implementation mechanisms.

The source study motivates the distinctions; it does not establish that those mechanisms are uniquely correct for HC cognition.

## Governing invariant

> **A relation used to reason is not automatically a relation established as true. Computational topology, candidate conditioning, derived-view ancestry, attention/gating, and evidence status remain explicit and separately governed.**
