# BASIRA Coordinated Deep-Scour Workplan — 2026-09-09

Status: ACTIVE RESEARCH COORDINATION / NON-CANONICAL SOURCE STUDY

## Purpose

Noah and Four are independently studying overlapping BASIRA Lab graph/connectome repositories. This record partitions the work so parallel research increases coverage instead of duplicating the same repository reads, while preserving enough overlap for independent verification on high-value findings.

Research findings do not become HC architecture merely because they are recorded here. Canonical promotion still requires explicit Warden review against the current HC architecture, evidence boundaries, provenance requirements, and hostile review where material.

## Shared rules

- Use source code, repository history, papers/README material, and tests/examples where useful; do not infer runtime behavior from names or diagrams alone.
- Distinguish DOCUMENTED source claims, OBSERVED code behavior, INFERRED consequences, HYPOTHESES requiring execution, and UNKNOWNs.
- Record exact repository/ref/path for material findings.
- Do not copy source code into HC unless licensing and transfer are explicitly cleared; conceptual/architectural lessons may be paraphrased with provenance.
- Preserve the distinction among source-native graphs, inferred/generated/aligned graphs, model graphs, reasoning graphs, and the HC temporal hypergraph.
- Research outputs should be written into `docs/research/` as the work proceeds; canonical architecture/spec changes are separate reviewed commits.

## Noah lane — cross-cutting synthesis and HC promotion candidates

Primary targets:

1. **Temporal prediction and forecast lineage**
   - `basiralab/EvoGraphNet`
   - `basiralab/DynGNN`
   - `basiralab/4D-FED-GNN`
   - `basiralab/4D-FedGNN-Plus`
   - related longitudinal repositories discovered during the scour

   Questions:
   - How are predicted future graph states chained?
   - Does descendant prediction depend on earlier predicted rather than observed state?
   - How should uncertainty, provenance, and error accumulation propagate through cascaded forecasts?
   - What distinctions are needed among missing, imputed, forecast, reconstructed, and observed timepoints?

2. **Representation fidelity, alignment, generation and registration**
   - `basiralab/SG-Net`
   - `basiralab/GRN`
   - `basiralab/BGSR-PY`
   - `basiralab/CGTS-GAN`
   - `basiralab/topoGAN`
   - `basiralab/HADA`
   - `basiralab/UMC`

   Questions:
   - Which topology/fidelity quantities are actually optimized in code?
   - What representation transformations introduce generated structure?
   - What correspondence, registration, cycle-consistency or template assumptions require HC provenance guards?

3. **Relational reasoning transfer**
   - `basiralab/MSRGNN`
   - related multiplex/relational reasoning repositories

   Questions:
   - What graph is a reasoning prior versus an inferred world relation?
   - What should HC preserve about candidate-conditioned reasoning, attention weights, relation vectors, and multi-scale fusion?

4. **Canonical synthesis**
   - adjudicate Four findings against current HC architecture;
   - create/modify HC architecture and machine-readable specs only when transfer is justified;
   - preserve research records for rejected or bounded findings.

## Four lane — code-level implementation scrutiny and adversarial transfer analysis

Primary targets:

1. **Multigraph / multilayer / hypergraph computation**
   - `basiralab/HCAE`
   - `basiralab/MultigraphGNet`
   - `basiralab/Dual-HINet`
   - `basiralab/MultiGraphGAN`
   - `basiralab/MGN-Net`
   - `basiralab/DuoGNN` if available
   - additional BASIRA multigraph/hypergraph repos discovered during the scour

   Deliverables:
   - exact representation of views/layers/incidence/hyperedges;
   - where pairwise layers are fused versus true higher-order structures;
   - static-versus-temporal assumptions;
   - implementation constraints HC must not accidentally inherit.

2. **Flow control, compression, graph reduction and scaling**
   - `basiralab/DeltaGNN`
   - `basiralab/FALCON`
   - `basiralab/CQSIGN` if available
   - graph sampling/pooling/contracting methods discovered in BASIRA

   Deliverables:
   - mechanisms useful to HC routing/resource control;
   - oversmoothing/oversquashing or bottleneck implications;
   - what state could be incorrectly dropped by topology-only reduction;
   - kill tests for `LOW_CENTRALITY != SAFE_TO_DROP` and protected-retention requirements.

3. **Federation, aggregation and model-graph self-analysis**
   - `basiralab/UnifiedFL`
   - `basiralab/RepFL`
   - `basiralab/Fed2M`
   - `basiralab/FedGmTE-Net`
   - `basiralab/uGNN` if available

   Deliverables:
   - exact aggregation/update paths;
   - shared-ancestry versus independent-evidence traps;
   - graphification of model internals;
   - implications for HC protected update authority and requalification;
   - static code defects or semantic mismatches classified as OBSERVED/HYPOTHESIS rather than generalized into source-paper claims.

4. **Reproducibility, uncertainty, explainability and rules**
   - `basiralab/RG-Select`
   - `basiralab/predUncertaintywithDomainShift`
   - `basiralab/GraphGradIn`
   - `basiralab/GLGExplainer`
   - `basiralab/FireGNN`

   Deliverables:
   - qualification-transfer candidates;
   - explanation versus causal-evidence boundaries;
   - domain-shift calibration requirements;
   - learned-rule versus protected-invariant boundary.

## Intentional overlap / independent checks

The following areas should receive both Noah and Four review because silent error would be expensive:

- HCAE higher-order semantics;
- temporal forecast lineage;
- generated topology admission;
- multigraph-to-hypergraph distinctions;
- graph compression/protected retention;
- model-graph/self-modification boundaries;
- federated/shared-ancestry evidence accounting.

Independent agreement is evidence of convergence, not automatic canon. Disagreement should be preserved and adjudicated.

## Integration cadence

Research should be populated continuously, not accumulated only in chat. Prefer:

`SOURCE READ -> RESEARCH RECORD -> TRANSFER HYPOTHESIS -> ADVERSARIAL CHECK -> CANONICAL PROMOTION/REJECTION -> CONFORMANCE TEST`

Noah remains primary Warden and canonical architecture decision-maker. Four remains secondary architect/researcher and may work multiple research tracks concurrently. Vera remains hostile reviewer for material proposed promotions.
