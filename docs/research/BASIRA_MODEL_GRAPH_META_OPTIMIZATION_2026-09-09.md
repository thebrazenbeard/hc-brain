# BASIRA Model-Graph and Meta-Optimization Scour — 2026-09-09

Status: research/provenance only. These sources provide computational patterns and failure cases; they do not define HC update authority or prove HC implementation feasibility.

## Sources inspected

- `basiralab/uGNN`
- `basiralab/UnifiedFL`
- related context from `basiralab/Meta-RegGNN`

## uGNN — heterogeneous models as graph state

DOCUMENTED from the uGNN README: heterogeneous neural architectures are converted to graphs where weights are represented as edges and biases as nodes, then a GNN operates over the disjoint union of those model-graphs to guide optimization across models.

The key transferable pattern is **model graphification**: implementation state can be represented as typed graph state for analysis, comparison, bounded optimization, and cross-model transfer.

HC boundary:

`MODEL_GRAPH != COGNITIVE_TOPOLOGY`

A graph encoding of software/model parameters is a representation of an implementation artifact. It does not automatically become the HC temporal cognitive hypergraph, even if the model participates in cognition.

`MODEL_PARAMETER_EDGE != COGNITIVE_RELATION_EDGE`

## UnifiedFL — proposed dynamic meta-optimization across heterogeneous models

DOCUMENTED from the current README: UnifiedFL describes a framework in which heterogeneous local models are converted to model-graphs and a shared GNN parameterization governs their updates. The README also describes dynamic client clustering based on Euclidean distance between GNN parameter vectors and more frequent synchronization within similar clusters.

DOCUMENTED status from that README: the work is described as submitted to Medical Image Analysis in 2025 and under review. Treat claims as research claims, not peer-reviewed established results unless separately verified later.

OBSERVED from current code:

- `unifiedfl/graphs/convert.py` explicitly converts MLP/CNN weights into graph edges and biases into node state;
- `unifiedfl/graphs/unify.py` concatenates multiple model-graphs into one disjoint-union graph while retaining per-model node/layer/index lists and optional kernel/layer maps;
- `unifiedfl/train/train_unifiedfl.py` trains the unified model over a loader, averages per-model losses, updates shared model state, saves per-model graph states and the best global model.

OBSERVED source-snapshot discrepancy: a repository-wide code search for federation-related terms returned the README but did not expose a client/server communication or dynamic federation implementation, and the inspected training module is a centralized training loop. The inspected default-branch tree also does not visibly contain a dedicated federation/client/server module.

This does **not** prove no dynamic-federation implementation exists elsewhere, in another branch, unpublished code, or omitted artifact. It means the specific current default-branch source inspected here does not independently verify the full dynamic-federation behavior claimed in the README.

Epistemic status:

- README architecture description: DOCUMENTED as repository claim.
- model graphification and unified training mechanics: OBSERVED in code.
- full dynamic client clustering/federation as executed behavior: UNKNOWN from the inspected source snapshot.

This is exactly the kind of source/implementation distinction HC qualification must preserve.

`DESCRIBED_ARCHITECTURE != VERIFIED_EXECUTED_ARCHITECTURE`

## Meta-RegGNN context — adaptation is not unrestricted self-modification

DOCUMENTED from the previously inspected Meta-RegGNN source: meta-learning is used to adapt a regression GNN quickly to unseen connectome distributions.

HC transfer remains bounded:

`META_LEARNING != PROTECTED_SELF_MODIFICATION_AUTHORITY`

`FAST_PARAMETER_ADAPTATION != PROTECTED_ARCHITECTURE_UPDATE`

## HC transferable mechanisms

### 1. Model-graph introspection

HC may benefit from representing internal learned modules, adapters, routing models, predictors, or other computational components as inspectable graph objects containing implementation-relevant structure.

Potential uses:

- dependency analysis;
- parameter-sharing candidates;
- compatibility analysis;
- regression-impact analysis;
- fault localization;
- resource planning;
- migration planning;
- learned optimization proposals;
- comparing alternative implementations.

The representation must retain a namespace separating implementation/model structure from the cognitive topology it supports.

### 2. Shared optimizers as proposal generators

A learned optimizer may propose updates across multiple heterogeneous components.

That can be useful, but it creates a high-leverage failure point. A shared meta-optimizer must not acquire update authority merely because it can technically write or predict parameter changes.

`META_OPTIMIZER_REACHABILITY != UPDATE_AUTHORITY`

`PROPOSED_PARAMETER_UPDATE != AUTHORIZED_UPDATE`

`LOW_LOSS_UPDATE != SEMANTICALLY_SAFE_UPDATE`

### 3. Similarity-based coordination

Parameter distance or learned model similarity may support scheduling, clustering, knowledge-transfer proposals, or evaluation allocation.

It must not be treated as semantic, identity, authority, or functional equivalence.

`PARAMETER_SIMILARITY != SEMANTIC_SIMILARITY`

`PARAMETER_SIMILARITY != FUNCTIONAL_EQUIVALENCE`

`SAME_CLUSTER != SAME_AUTHORITY_SCOPE`

### 4. Synchronization frequency is not authority

Adaptive communication frequency may improve efficiency. It does not change who/what is authorized to mutate protected state or which evidence is current.

`SYNCHRONIZATION_FREQUENCY != AUTHORITY`

`FREQUENT_PARAMETER_EXCHANGE != INDEPENDENT_CORROBORATION`

## Failure modes relevant to HC

- a model-graph representation is mistaken for cognitive topology;
- a shared GNN/meta-optimizer becomes a de facto central executive because all component adaptation routes through it;
- optimizer success grants protected-update authority;
- parameter-space similarity is treated as semantic identity or compatibility;
- one global optimization objective homogenizes specialized HC components and erases necessary disagreement/specialization;
- a meta-model updates its own update-governance boundary through ordinary learning;
- centralized training code is assumed to implement federated/dynamic behavior because the README says so;
- per-model best-score checkpoints silently replace coherent whole-organ version sets;
- cross-model parameter sharing bypasses generation/component qualification.

## Recommended canonical transfer

HC should support **model-graph introspection and meta-optimization proposals** while explicitly firewalling those capabilities from protected update authority.

The safest abstraction is:

```text
implementation/model state
-> model-graph representation
-> analysis or learned optimization proposal
-> classify target state/change class
-> scope-matched authority and protected-governance checks
-> shadow/simulation/canary where appropriate
-> coherent activation transaction
-> qualification
```

The meta-optimizer is an advisor/proposal mechanism unless a specific update class grants it bounded autonomous authority.

## Current disposition

KEEP as research/provenance. The model-graph idea is useful enough to justify a generic HC operating boundary, but neither uGNN nor UnifiedFL should become an HC runtime dependency, and UnifiedFL's full README-described federation behavior remains unverified from the default-branch code inspected here.