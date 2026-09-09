# BASIRA GSR-Net Registered Runtime and Super-Resolution — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/GSR-Net@master/model.py`
- `basiralab/GSR-Net@master/layers.py`
- `basiralab/GSR-Net@master/ops.py`
- current PyTorch `ModuleList` / module-registration documentation

## OBSERVED implementation structure

`GSRNet` accepts a low-resolution adjacency matrix, normalizes it, runs a `GraphUnet`, passes the resulting representation through `GSRLayer`, then through graph-convolution layers and returns a symmetrized absolute high-resolution-looking matrix.

`GraphPool` learns a score per node, keeps a top-k subset, and records the selected local indices. `GraphUnpool` allocates a larger zero tensor and restores pooled features into positions named by those saved indices. This is useful implementation evidence that unpooling/restoration is an index-lineage problem rather than proof of information recovery.

`GSRLayer` derives a higher-dimensional representation from the eigensystem of the low-resolution graph and learned weights. The generated output is therefore model-derived high-resolution structure, not direct observation.

### Submodule-registration finding

In the inspected `GraphUnet.__init__`, `self.down_gcns`, `self.up_gcns`, `self.pools`, and `self.unpools` are initialized as ordinary Python lists and populated by appending `nn.Module` instances.

PyTorch documentation states that `nn.ModuleList` registers contained submodules so they are visible to `Module` methods; registered module parameters are what `parameters()`, device conversion, and state handling operate over.

OBSERVED: the inspected source does not wrap those four collections in `nn.ModuleList` or otherwise explicitly register the appended modules.

INFERRED from documented PyTorch registration semantics: parameters belonging only to those list-contained modules are not expected to be managed like registered child modules by parent-level `parameters()`, `to()`, or `state_dict()` operations. Exact execution should still be instrumented before claiming the behavior of a particular training run.

### Dimension-hardcoding finding

`GSRLayer` accepts `hr_dim` and uses it to size learned weights, but later constructs `idx = torch.eye(320, dtype=bool)` before assigning the diagonal of `X`. This embeds a literal 320-node assumption inside otherwise parameterized code.

OBSERVED: the implementation contains this fixed dimension.

HYPOTHESIS: configurations where the produced matrix is not 320x320 can fail or apply an incompatible mask. Execution across alternate `hr_dim` values is required to establish exact failure behavior.

## HC lessons

`DECLARED_MODULE != REGISTERED_RUNTIME_COMPONENT`

`CALLED_IN_FORWARD != MANAGED_BY_LIFECYCLE`

`LEARNABLE_PARAMETER_EXISTS != OPTIMIZER_CAN_REACH_PARAMETER`

`FORWARD_OUTPUT_EXISTS != CHECKPOINT_CONTAINS_ALL_CAUSAL_STATE`

`UNPOOL_POSITION_RESTORATION != INFORMATION_RECOVERY`

`PARAMETERIZED_INTERFACE != ACTUALLY_DIMENSION_AGNOSTIC_IMPLEMENTATION`

A component can participate in a forward computation while remaining outside the framework's parent-level registration, checkpoint, device, optimizer, telemetry, or lifecycle mechanisms. HC qualification must therefore inspect executable registration/state paths, not merely class names or forward diagrams.

## Transfer candidates

1. HC implementation conformance should distinguish architecture presence from runtime registration/management.
2. Every stateful cognitive component that is claimed to learn, persist, migrate, recover, or update should be traceable through the corresponding optimizer/plasticity, checkpoint/durability, device/substrate, lifecycle, and fault-management paths.
3. Pool/unpool or contraction/expansion systems must retain explicit index lineage and loss semantics; placing surviving values back into old positions does not restore dropped information.
4. Claimed dimension/morphology neutrality should be tested with off-nominal sizes rather than inferred from constructor parameters.

## Scope and caution

The registration and hard-coded-dimension observations are static code findings for the inspected source revision. This record does not claim the associated paper's reported experiments are invalid or that every run exercised the affected paths. Runtime instrumentation is required for stronger claims.
