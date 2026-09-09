# BASIRA MSRGNN Relational-Reasoning Study — 2026-09-09

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/MSRGNN`

Inspected default branch: `main`

Primary source artifacts:

- `README.md` blob `34e3a7ea191c6d00c76d677ea7c93293a32032be`
- `I_RAVEN/msrgnn.py` blob `c7bf9aa7b1561871e57438604a6a299b61b6c819`

This note records source behavior and HC transfer lessons. It does not make MSRGNN part of HC and does not treat source model success as evidence that HC implements or qualifies the same capability.

## Source identity correction

DOCUMENTED from the inspected repository README: the current repository describes MSRGNN as a **Multi-Scale Relational Graph Neural Network for Unified Abstract Visual Reasoning**, with task folders for I-RAVEN, RADIO, and O3.

An earlier working interpretation of this repository as a social-relation/ConceptNet model is not supported by the current default-branch README or the inspected I-RAVEN implementation and must not be carried forward as source fact.

`SOURCE_NAME_OR_PRIOR_DESCRIPTION != CURRENT_SOURCE_CONTENT`

## Observed implementation structure

OBSERVED in `I_RAVEN/msrgnn.py`:

1. The model can construct a fixed row/column graph template for a 3x3 nine-node panel arrangement or a fully connected template. A caller may instead provide a custom `template_edge_index`.
2. The selected graph template is registered as a model buffer and then replicated across candidate-conditioned graphs at inference time.
3. A single ResNet-style visual feature extractor produces three feature views by adaptive pooling the same final convolutional representation at `4x4`, `2x2`, and `1x1` resolutions.
4. Stage 1 projects and processes each feature scale independently using the same GNN relation layer. Stage 2 concatenates the scale outputs and performs a second relational GNN pass.
5. Pairwise relational messages are produced from concatenated source/destination node-plus-position representations.
6. An attention MLP produces logits from visual and positional features. PyG softmax normalizes the weights over the destination-index grouping, and the normalized weights gate relational messages.
7. Each candidate is evaluated by constructing a graph containing the shared context panels plus that candidate. The result is therefore candidate-conditioned relational reasoning rather than one candidate-independent graph claim.
8. Final graph representations concatenate global mean, max, and add pooling before a learned scalar scorer; candidate scores are reshaped and used for answer selection.

## Transfer findings

### 1. Reasoning topology can be a prior rather than an inferred world relation

The row/column and fully-connected templates are supplied structural choices. Their presence in the computation does not establish that the corresponding relation was inferred from the current observation.

HC transfer:

`REASONING_GRAPH_PRIOR != INFERRED_WORLD_RELATION`

`ALLOWED_MESSAGE_PATH != OBSERVED_RELATION`

A topology may define which comparisons are computationally permitted or encouraged while remaining epistemically distinct from a claim about the world.

### 2. Candidate-conditioned reasoning is not candidate-independent evidence

The implementation constructs one context-plus-candidate graph per candidate. Its relational representation and final score are therefore conditional on which candidate was inserted.

HC transfer:

`CANDIDATE_CONDITIONED_REPRESENTATION != CANDIDATE_INDEPENDENT_WORLD_STATE`

Candidate-conditioned simulations, explanations, relation vectors, or coalition states should retain the candidate/hypothesis ID that caused their construction.

### 3. Multi-scale views from one source are correlated evidence

The three scale features are derived from the same image tensor through the same extractor trunk and differ by pooling resolution. They are useful complementary representations but are not independent observations.

HC transfer:

`MULTIPLE_DERIVED_VIEWS != MULTIPLE_INDEPENDENT_OBSERVATIONS`

`FUSED_CORRELATED_FEATURES != INDEPENDENT_CORROBORATION`

Independence accounting should follow source ancestry rather than tensor count or branch count.

### 4. Attention weights are routing/gating quantities, not truth or explanation by default

The observed attention weights are learned normalized gates on relational messages. The implementation does not, merely by producing these weights, establish causal importance, semantic truth, confidence calibration, or explanatory sufficiency.

HC transfer:

`ATTENTION_WEIGHT != EVIDENCE_STRENGTH_BY_DEFAULT`

`ATTENTION_WEIGHT != CAUSAL_IMPORTANCE`

`ATTENTION_WEIGHT != EXPLANATION`

The quantity may be exposed as an operational routing/gating trace. Stronger epistemic interpretation requires separate validation appropriate to the claim.

### 5. Aggregation choice does not erase provenance requirements

Mean, max, and sum pooling are concatenated before scoring. Even when several summary operators agree or contribute jointly, they remain transformations of the same underlying graph state.

HC transfer:

`MULTIPLE_AGGREGATORS != INDEPENDENT_EVIDENCE`

A pooled representation should retain enough lineage to identify source state, transformation, candidate context, and model snapshot when consequential downstream claims depend on them.

## HC architectural gap found

Existing HC epistemic and social-modeling contracts already separate prediction from fact and group prior from individual fact, but the inspected source exposes a more general representation-level distinction that is not limited to social reasoning:

- computational/reasoning topology versus inferred world topology;
- candidate-conditioned internal relation versus candidate-independent state;
- correlated multi-view derivations versus independent evidence;
- attention/routing gate versus epistemic weight.

These distinctions apply to abstract visual reasoning, perception, simulation, semantic inference, planning, social modeling, and temporal-hypergraph coalitions.

## Proposed canonical transfer

Create a focused identity-neutral architecture contract for relational reasoning provenance rather than importing the MSRGNN architecture itself.

Minimum invariants:

- `REASONING_GRAPH_PRIOR != INFERRED_WORLD_RELATION`
- `ALLOWED_MESSAGE_PATH != OBSERVED_RELATION`
- `CANDIDATE_CONDITIONED_REPRESENTATION != CANDIDATE_INDEPENDENT_WORLD_STATE`
- `MULTIPLE_DERIVED_VIEWS != MULTIPLE_INDEPENDENT_OBSERVATIONS`
- `ATTENTION_WEIGHT != EVIDENCE_STRENGTH_BY_DEFAULT`
- `ATTENTION_WEIGHT != CAUSAL_IMPORTANCE`
- `ATTENTION_WEIGHT != EXPLANATION`
- `MULTIPLE_AGGREGATORS != INDEPENDENT_EVIDENCE`

## Adversarial tests suggested

1. Give two candidates identical context but different candidate panels; verify relation traces are tagged candidate-specific and cannot be written as unconditional world facts.
2. Duplicate one sensor/observation into multiple scales/embeddings; verify evidence-counting does not increase independent-support count merely because branches multiplied.
3. Swap a reasoning topology prior while holding observations fixed; verify topology change alters computation without being recorded as new external evidence.
4. Force a high attention gate onto a weak or false input; verify the gate cannot directly raise semantic truth status or action authority.
5. Compare attention/routing traces with intervention-based causal tests; require a separate validation record before labeling attention as causal explanation.
6. Aggregate one state through mean/max/sum simultaneously; verify the result retains one ancestry group rather than becoming three independent corroborators.

## Evidence boundary

DOCUMENTED: current repository purpose and task organization from `README.md`.

OBSERVED: implementation behavior listed above from `I_RAVEN/msrgnn.py` at the cited blob.

INFERRED: HC architectural consequences and proposed invariants.

UNKNOWN from this inspection: empirical calibration of attention weights, causal interpretability of learned relations, generalization beyond the supplied tasks, and whether every task-specific folder uses identical implementation semantics.
