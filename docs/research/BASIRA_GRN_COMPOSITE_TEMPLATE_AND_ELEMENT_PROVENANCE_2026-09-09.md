# BASIRA GRN Composite Template and Element Provenance — 2026-09-09

Status: RESEARCH PROVENANCE / NON-CANONICAL SOURCE STUDY

## Sources inspected

- `basiralab/GRN@main/README.md`
- `basiralab/GRN@main/gGAN.py`
- `basiralab/GRN@main/main_trainer.py` / code-search trace around CBT construction

## DOCUMENTED source framing

GRN is described as a graph-registration network that maps input brain graphs toward a fixed population connectional brain template (CBT) before downstream GNN classification. The README describes the CBT as capturing common population features and the registration step as preserving connectional/structural information while exposing discriminative structure relative to that center.

## OBSERVED netNorm construction

In the inspected `gGAN.py`, `netNorm`:

1. vectorizes each subject graph's upper-triangular edge values;
2. for every edge/feature position, computes how far each subject's value lies from the other subjects' values at that same position;
3. selects the subject index with the minimum aggregate distance for that individual edge/feature;
4. constructs a new feature vector by taking each edge from its independently selected subject;
5. reconstructs the symmetric CBT from that feature vector.

Therefore the resulting CBT can be a mosaic whose different edges originate from different source subjects. The CBT is not required to be identical to any one observed subject graph.

`main_trainer.py` also separates a `for_cbt` subset from the folds used by the downstream train/validation/test split before constructing the CBT. This provides source-set provenance that should remain associated with the learned template.

## HC transfer lesson

Population summaries and fused/generated representations may have provenance at finer granularity than the whole object.

`COMPOSITE_TEMPLATE != OBSERVED_INSTANCE`

`OBJECT_LEVEL_SOURCE_SET != ELEMENT_LEVEL_ANCESTRY`

`EDGE_SELECTED_FROM_SOURCE != TEMPLATE_IS_THAT_SOURCE`

`COMMON_FEATURE != UNIVERSAL_FEATURE`

`MOSAIC_REPRESENTATION != COHERENT_OBSERVED_STATE`

A template whose components were independently selected or fused can combine individually plausible elements into a combination never jointly observed in any source instance.

## Why this matters to HC

For consequential reasoning, it can matter whether two properties were jointly observed in one source/state or independently assembled from different sources.

Examples include:

- a world-model object assembled from attributes extracted from different observations;
- a person model containing traits inferred from different contexts/times;
- a body model fused across incompatible calibration epochs;
- a graph/template composed from edges selected from different source states;
- a memory summary whose clauses descend from different records;
- an action prediction assembled from independently generated consequences.

Without element-level lineage, downstream cognition can incorrectly infer joint occurrence, compatibility, or causal coherence from a synthetic composite.

## Proposed HC rule

Consequential composite representations should retain source lineage at the finest granularity required to answer material questions about joint observation, compatibility, currentness, uncertainty, and authority.

This does not require provenance on every scalar in every internal tensor. It requires enough lineage to prevent a fused object from gaining stronger joint-evidence semantics than its construction supports.

## Scope and caution

This is a static reading of the repository implementation. It establishes the algorithmic construction visible in the inspected `netNorm` code; it does not by itself establish how every experiment or later revision was run.
