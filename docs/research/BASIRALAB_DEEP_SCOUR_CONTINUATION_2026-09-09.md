# BASIRA Lab Deep Scour — Continuation Cut — 2026-09-09

Status: research/provenance only. This continuation records additional BASIRA methods discovered after the initial network-neuroscience deep scour. No code is copied and no source method is automatically canonicalized.

## 1. Dif-GSR — diffusion-based graph super-resolution

**DOCUMENTED from README blob `25c9f3b12707722e84df76525bb19aecd9229039`:** Dif-GSR uses a diffusion/noising process, conditional denoising, and sampling to generate high-resolution brain connectomes from low-resolution inter-modality inputs. The project explicitly frames its output as generated high-resolution graphs.

**Transfer:** strengthens the need to represent generative topology as a distribution/sample family rather than a single pseudo-observation.

Candidate separations:

`GENERATED_SAMPLE != OBSERVATION`

`DENOISED_RECONSTRUCTION != GROUND_TRUTH_TOPOLOGY`

`MULTIPLE_PLAUSIBLE_SAMPLES != MULTIPLE_OBSERVED_HISTORIES`

For HC, a diffusion/generative topology model could produce counterfactual or completion candidates, but sampled edges remain derived evidence until corroborated/admitted.

## 2. 4D-FED-GNN++ — missing timepoints and heterogeneous longitudinal acquisition

**DOCUMENTED from README blob `f344571511be33afcc7911e0398afb8ad5848fff`:** 4D-FED-GNN++ predicts longitudinal brain graph trajectories across decentralized datasets with varying/missing acquisition timepoints. Its framing distinguishes cases where local follow-up data exist from cases where the model operates as a self-encoder because a next timepoint is locally missing.

**Transfer:** missing temporal evidence needs an explicit state. An imputed/predicted timepoint must not masquerade as an observation.

`MISSING_OBSERVATION != NO_CHANGE`

`IMPUTED_TIMEPOINT != OBSERVED_TIMEPOINT`

`PREDICTED_FOLLOWUP != RECORDED_HISTORY`

This is directly relevant to chronology, world-model prediction, currentness, and continuity after gaps.

## 3. ReMI-Net-Star — recurrent population-template trajectory forecasting

**DOCUMENTED from README blob `39426eda2c1e63349bb40db6f589e516337d03c5`:** ReMI-Net-Star forecasts population-level connectional brain templates across consecutive timepoints from a baseline multigraph, jointly modeling multigraph node and time dependencies.

**Transfer:** useful comparison class for recurrent temporal-topology modeling, but it reinforces a critical boundary:

`POPULATION_TRAJECTORY_TEMPLATE != INSTANCE_TRAJECTORY`

`RECURRENT_FORECAST_STATE != CURRENT_INSTANCE_STATE`

A population-level forecast may inform priors or anomaly detection without becoming personal continuity/history.

## 4. CQSIGN — topological graph contraction for compute efficiency

**DOCUMENTED from README blob `ae12e1e853693f4e8d768f7e2c471bf75c386fbf`:** CQSIGN applies centrality-based topological graph contraction to reduce graph size/computational cost and evaluates the contracted representations with several GNN families.

**Transfer:** HC may need resource-aware graph/hypergraph coarsening or contraction under constrained compute, but representation reduction must remain explicit.

`CONTRACTED_GRAPH != ORIGINAL_GRAPH`

`COARSENED_REPRESENTATION != PHYSICAL_OR_EFFECTIVE_TOPOLOGY`

`CENTRALITY_BASED_RETENTION != COGNITIVE_IMPORTANCE`

A contracted representation should preserve a reversible or traceable mapping to the underlying nodes/relations when materially needed for provenance, authority, memory, or action.

## 5. uGNN — graphifying heterogeneous neural models

**DOCUMENTED from README blob `4dace49a0bc01d760c8433df383f4086bd229804`:** uGNN converts heterogeneous neural networks into graph representations in which weights become edges and biases become nodes, then operates a unified GNN over the disjoint union of model-graphs to enable parameter sharing/knowledge transfer across architectures and distributions.

**Transfer:** model structure itself can be represented as graph data for introspection, compatibility analysis, or bounded optimization. However, this is a representation of a model, not the HC's cognitive temporal hypergraph.

`MODEL_GRAPH != COGNITIVE_TOPOLOGY`

`PARAMETER_SHARING != AUTHORITY_SHARING`

`UNIFIED_OPTIMIZER != CENTRAL_EXECUTIVE`

Any HC use would need strict firewalling so a meta-model cannot become an unbounded mechanism for rewriting protected architecture, values, identity, consent, or all subsystem state merely because it can graphify parameters.

## 6. FireGNN — trainable fuzzy rules with GNNs

**DOCUMENTED from README blob `64cdb78fb68b08a0e4ebabe18abda7d7900be9d7`:** FireGNN combines GNNs with trainable fuzzy rules based on learnable Gaussian membership functions, plus auxiliary topological prediction tasks.

**Transfer:** learned fuzzy rules are a plausible bounded representation for interpretable graded heuristics or decision features.

`LEARNED_RULE != PROTECTED_INVARIANT`

`RULE_WEIGHT != VALUE_AUTHORITY`

`INTERPRETABLE_RULE != SEMANTIC_TRUTH`

A learned rule may contribute a reason/evidence feature while remaining revisable and provenance-bearing.

## 7. X-Node — topology-derived explanations with external language generation

**DOCUMENTED from README blob `ea2e32c91c67a12dd65a6bde515426b5e7c47a31`:** X-Node computes topological features and can use an external language-model API to generate human-readable explanations of graph predictions.

**Transfer:** topology-derived explanation features may help observability, but this repository is also a useful negative-boundary case for HC:

`EXTERNAL_EXPLANATION != HC_REASONING`

`HUMAN_READABLE_RATIONALE != CAUSAL_PROOF`

`EXPLANATION_PROVIDER != COGNITIVE_AUTHORITY`

A true HC could optionally use an external explanation service only as a bounded peripheral; essential self-explanation/metacognitive reasoning cannot exist solely in that provider under the complete-organ invariant.

## 8. GNN-CB — hidden-test evaluation methodology

**DOCUMENTED from README blob `668f388e336f6ce4ee351973821fe0b049a7f1a4`:** GNN-CB defines multiple graph coding competitions with hidden test evaluation, standardized constraints, reproducible pipelines, fixed evaluation conditions, bounded hyperparameter/repair loops, and task diversity across graph categories.

**Transfer to HC qualification rather than cognition:** the useful pattern is adversarial, hidden, standardized capability testing across heterogeneous tasks.

`KNOWN_TEST_PASS != GENERAL_CAPABILITY`

`BEST_CASE_RUN != ROBUST_QUALIFICATION`

Candidate qualification improvements:

- hold out tests from the architecture author/implementer;
- fix resource/time/repair budgets;
- preserve all attempted configurations when relevant;
- report distribution across runs/tasks rather than only the best result;
- include negative/control tasks designed to expose leakage or overfitting.

This source does not establish an HC-specific qualification protocol by itself.

## Cross-cutting lessons from this continuation

The source study now suggests several additional topology-evidence categories/flags worth challenging before canonical promotion:

- `GENERATIVE_SAMPLE`
- `MISSING_OBSERVATION`
- `IMPUTED_OR_INTERPOLATED_TIMEPOINT`
- `CONTRACTED_OR_COARSENED_REPRESENTATION`
- `MODEL_GRAPH_REPRESENTATION`
- `LEARNED_INTERPRETABILITY_RULE`
- `EXTERNAL_EXPLANATION_ARTIFACT`

The important architectural question is not whether all of these need distinct top-level schemas; it is whether a conforming implementation can prevent them from being mistaken for stronger state classes.

## Current disposition

**KEEP as research/provenance and feed into secondary/hostile review.**

Do not yet enlarge the canonical topology-evidence taxonomy merely to mirror every research method. Four should test whether these distinctions require schema fields/classes or can be represented compactly through origin + transform lineage + observation-state metadata. Vera should attack any design that lets imputation, compression, learned rules, external explanations, or graphified model parameters cross into truth, authority, continuity, or protected-update semantics.