# BASIRA Lab Deep Scour — Continuation Cut 2 — 2026-09-09

Status: research/provenance only. No source code is copied and no method below is promoted directly into canonical cognition.

## FALCON — feature/label-preserving graph collapse

**DOCUMENTED from README blob `5f2a6b13b78dc0502970961800c33e74a1b7344b`:** FALCON performs feature-label constrained graph collapse for memory-efficient GNN training and compares against graph coarsening and several scalable GNN families. Its collapse strategy can explicitly prioritize features versus labels and operates under a node budget.

**HC transfer:** resource-aware coarsening should be consequence-aware rather than purely centrality-aware. The HC cannot discard a low-centrality node merely because it is cheap to remove if that node carries unique provenance, authority state, continuity-bearing memory, fault evidence, or a rare but high-consequence capability.

`COMPUTE_BUDGET != PERMISSION_TO_ERASE_STATE`

`FEATURE_PRESERVATION != AUTHORITY_OR_CONTINUITY_PRESERVATION`

`COARSENING_OBJECTIVE != COGNITIVE_VALUE_FUNCTION`

A conforming HC coarsener would need protected retention constraints in addition to graph/feature reconstruction objectives.

## DuoGNN — interaction decoupling under homophily/heterophily

**DOCUMENTED from README blob `ab7dc577d787edaf23f84fa196124dab23d9b2a2`:** DuoGNN is a topology-aware GNN with an interaction-decoupling stage intended to handle homophilic and heterophilic interactions separately. It uses topological measures such as curvature in experiments.

**HC transfer:** this strengthens the research case for not treating all neighboring messages as one homogeneous aggregation channel. Different relation types, support directions, modulatory roles, and agreement/disagreement patterns may require separate paths before integration.

`NEIGHBOR != SAME_SEMANTIC_RELATION`

`DISAGREEMENT != NO_INFORMATION`

`TOPOLOGICAL_CHANNEL != AUTHORITY_CHANNEL`

Any HC adaptation must use typed temporal relations rather than homophily/heterophily as a universal cognitive ontology.

## RBGM — edge-based recurrent trajectory mapping

**DOCUMENTED from README blob `7a8f5ab479c0d499db275f13bc94fdb118152b54`:** Recurrent Brain Graph Mapper predicts follow-up brain graphs from a baseline using recurrent mappers, teacher forcing, topological loss, and a time-dependency regularizer between consecutive graph states.

**HC transfer:** useful as a comparison class for autoregressive topology forecasting and for testing exposure-bias failure when predictions feed later predictions.

`TEACHER_FORCED_TRAINING != FREE_RUNNING_RELIABILITY`

`PREDICTED_PREVIOUS_STATE != OBSERVED_PREVIOUS_STATE`

`TOPOLOGICAL_SMOOTHNESS_PRIOR != EVIDENCE_OF_NO_ABRUPT_CHANGE`

An HC predictor must preserve whether each causal predecessor in a trajectory was observed, inferred, imputed, or itself predicted.

## GLGExplainer — logic combinations of learned explanatory concepts

**DOCUMENTED from README blob `d160bc3a57d32faf5391367194ac0772dcafa096`:** GLGExplainer builds global explanations by embedding/grouping local GNN explanations and learning logic combinations of concepts/prototypes.

**HC transfer:** explanations may be structured as compositional logic over evidence-backed concepts rather than unconstrained prose. This is potentially useful for self-monitoring and inspectability if explanation provenance remains tied to the underlying model/evidence.

`EXPLANATION_FORMULA != CAUSAL_MECHANISM`

`GLOBAL_EXPLANATION != UNIVERSAL_RULE`

`LEARNED_CONCEPT != SEMANTIC_CANON`

A compact logical explanation can still be wrong, incomplete, unstable under perturbation, or post-hoc.

## FairnessExpressivenessinGNNs — architecture choice changes downstream distributional behavior

**DOCUMENTED from README blob `226c74d166ba6eb9962982e2a2b3fd98d8fac215`:** the project studies whether GNN architectural expressiveness changes measured fairness across datasets and reports that the relationship varies by dataset; it also uses repeated seeds/splits, statistical testing, and mixed-effects analysis.

**HC transfer:** architecture/topology changes can systematically alter behavior distributions even when the nominal task is unchanged. Therefore a protected architecture update cannot be qualified solely on aggregate accuracy or one functional benchmark.

`HIGHER_EXPRESSIVENESS != UNCONDITIONALLY_BETTER_BEHAVIOR`

`TASK_ACCURACY_PASS != DISTRIBUTIONAL_BEHAVIOR_PASS`

`ARCHITECTURE_CHANGE != VALUE_NEUTRAL_CHANGE`

For HC qualification, material routing/topology/model changes should include stratified behavioral regression tests relevant to the affected scope rather than only average performance.

## Cross-source synthesis

This cut adds three important engineering lessons to the existing topology-evidence work:

1. **Resource reduction requires protected retention semantics.** Graph contraction/coarsening is not just an approximation problem when some low-centrality state is uniquely consequential.
2. **Relation disagreement can be information.** Decoupled interaction paths are a useful implementation research direction for typed HC relations, but graph-local similarity must not become ontology or authority.
3. **Predictive chains need predecessor provenance.** Autoregressive topology forecasts must say whether each previous state was observed or predicted, otherwise error can silently compound while appearing historical.
4. **Explainability must remain epistemically bounded.** A logic formula is an explanation artifact, not proof of causal mechanism or semantic canon.
5. **Architecture changes need behavioral-distribution regression.** More expressive or efficient topology can change downstream behavior in ways not captured by headline task metrics.

## Candidate additional negative tests

- low-centrality node with unique revocation/authority state survives compute-pressure coarsening;
- low-centrality node carrying the only continuity-bearing copy cannot be collapsed away;
- heterophilic/disagreeing evidence is not erased merely because neighbors disagree;
- free-running temporal predictor exposes compounding uncertainty after predicted predecessors;
- abrupt observed topology change is not smoothed away solely to satisfy a temporal regularizer;
- explanation formula changes under perturbation without being promoted to semantic canon;
- architecture update with improved mean task score but materially degraded protected subgroup/scope behavior fails qualification until disposition.

## Disposition

**KEEP as research/provenance.** Feed these findings into the topology-evidence, protected-update, Noöplex flow-control, and qualification workstreams. Canonical transfer should occur only after Four implementation-readiness analysis and Vera hostile review.