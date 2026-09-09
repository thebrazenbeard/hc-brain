# Research Claim and Evidence Ledger

**Date:** 2026-09-09  
**Purpose:** keep source-supported observations separate from Noöplex design inference and Synthetic-canon extrapolation.

## Status vocabulary

- `SUPPORTED_PRINCIPLE` — the general scientific/engineering principle is supported by cited literature.
- `SUPPORTED_COMPONENT_DIRECTION` — component technology or mechanism is demonstrated/reviewed, but not at Noöplex integration scale.
- `OPEN_CONTESTED` — evidence exists but interpretation or importance remains unsettled.
- `DESIGN_INFERENCE` — architecture choice derived from evidence; not itself an empirical fact.
- `SPECULATIVE_SYSTEM_CLAIM` — not demonstrated at Noöplex/Synthetic scale.

| ID | Claim | Status | Evidence basis | Noöplex implication |
|---|---|---|---|---|
| R001 | Higher-order interactions can create dynamics not captured by pairwise-network intuition. | SUPPORTED_PRINCIPLE | Zhang, Lucas & Battiston 2023; Battiston-field review 2025 | Higher-order runtime relations are a reasonable modeling tool. |
| R002 | The relative importance of pairwise versus nonpairwise interactions in macroscopic brain dynamics is not settled. | OPEN_CONTESTED | Hypergraph reconstruction from dynamics, Nature Communications 2025 | Do not claim runtime hyperedges are literal established brain mechanisms. |
| R003 | Structural connectivity and functional dynamics are related but not identical. | SUPPORTED_PRINCIPLE | Fotiadis et al. 2024 | Keep structural, configurable, and functional connectivity separate. |
| R004 | Directed causal influence cannot be read directly from correlation/structure without model and intervention assumptions. | SUPPORTED_PRINCIPLE | Greaves et al. 2025 | Store causal-effect status separately from functional coupling. |
| R005 | Thalamocortical systems can coordinate distributed computation through gating/regularization-like functions. | SUPPORTED_PRINCIPLE | Trends in Cognitive Sciences 2024 feature review | Distributed arbitration/routing is biologically motivated; no single executive homunculus is required. |
| R006 | Global-workspace-like broadcasting is a live theory, not established proof of consciousness. | OPEN_CONTESTED | Seth & Bayne 2022; Cogitate adversarial collaboration 2025 | Workspace availability may be engineered without being labeled consciousness. |
| R007 | Fast episodic and slower generalized learning systems can be computationally complementary. | SUPPORTED_PRINCIPLE | Sun et al. 2023 and complementary-learning-systems lineage | Separate episodic capture from semantic/procedural consolidation. |
| R008 | Unregulated consolidation can degrade generalization in unpredictable environments. | SUPPORTED_PRINCIPLE within model scope | Sun et al. 2023 | Gate consolidation by generalization/interference criteria rather than copying every experience. |
| R009 | Stable learned behavior can coexist with drifting neural representations. | SUPPORTED_PRINCIPLE / OPEN_MECHANISM | Qin et al. 2023; memory-engram review 2024 | Identity/continuity cannot require exact microstate persistence. |
| R010 | Learning operates over multiple timescales and interacts with current goal-directed processing. | SUPPORTED_PRINCIPLE | Miller & Constantinidis 2024 | Distinguish fast state, learning, consolidation, and long-term policy/topology timescales. |
| R011 | Hebbian-style plasticity alone is insufficient as a complete learning/stability model. | SUPPORTED_PRINCIPLE | Turrigiano review lineage; Annual Review synaptic-plasticity review | Use multiple plasticity classes and homeostatic regulation. |
| R012 | Homeostatic plasticity stabilizes circuit properties while allowing experience-driven change. | SUPPORTED_PRINCIPLE | Wen & Turrigiano 2024 | Add continuous stability control independent of semantic/identity authority. |
| R013 | Excitatory and inhibitory plasticity can be co-dependent and jointly support stable learned dynamics. | SUPPORTED_PRINCIPLE within model/experimental literature | Agnes & Vogels 2024 | Plasticity permissions should include inhibitory balancing, not just excitatory weight growth. |
| R014 | Neuromodulation affects circuits over diverse spatial and temporal scales. | SUPPORTED_PRINCIPLE | Mechanisms of neuromodulatory volume transmission, 2024 | Model modulation as typed many-to-many state, not one global mood scalar. |
| R015 | Interoception contributes to homeostasis, motivation, autonomic regulation, cognition, and emotion. | SUPPORTED_PRINCIPLE | Annual Review Physiology 2024; Annual Review Psychology 2025 | `BODY_STATE` should be rich, uncertain, and continuously sampled. |
| R016 | One-to-one mappings from individual hormones to specific emotions are not supported by current systems neuroscience. | SUPPORTED_PRINCIPLE | Interoception/emotion reviews; neuromodulation literature | Limbic Governor should regulate distributed state rather than select named emotions. |
| R017 | Dendrites perform nonlinear local computations within individual neurons. | SUPPORTED_PRINCIPLE | London & Häusser 2005; later cortical-dendrite literature | Runtime nodes may need internal computational compartments. |
| R018 | Astrocytes participate in synaptic regulation, metabolic support, extracellular homeostasis, and plasticity-related processes. | SUPPORTED_PRINCIPLE | astrocyte reviews and 2024 learning/plasticity work | Node contracts may include glial/support state; not all computation/support belongs to neurons. |
| R019 | The core human language network is specialized and distinct from many other cognitive systems. | SUPPORTED_PRINCIPLE | Fedorenko, Ivanova & Regev 2024 | Do not make language the universal executive/cognition node. |
| R020 | Brain-network organization reflects trade-offs between wiring/metabolic cost and topological efficiency. | SUPPORTED_PRINCIPLE | Bullmore & Sporns 2012; modern structure-function literature | Hyperconnectome should favor modularity and selective long-range connectors over all-to-all wiring. |
| R021 | Connector hubs provide useful integration but can concentrate cost and vulnerability. | SUPPORTED_PRINCIPLE | network-economy/connectome literature | Budget hubs, redundancy, bypass, and cascade containment. |
| R022 | Event-driven neuromorphic processing is an active demonstrated hardware direction. | SUPPORTED_COMPONENT_DIRECTION | Kudithipudi et al. 2025; event-based sensing literature | Use event fabrics where appropriate; do not force all workloads onto them. |
| R023 | Large-scale neuromorphic systems still face substantial integration, programming, reliability, and ecosystem challenges. | SUPPORTED_COMPONENT_DIRECTION | Kudithipudi et al. 2025; neuromorphic commercialization review 2025 | HC-scale integration remains extrapolated. |
| R024 | Photonic neural computing can accelerate highly parallel operations and is being explored for reconfigurable/lifelong-learning systems. | SUPPORTED_COMPONENT_DIRECTION | Cheng et al. 2024; Fu et al. 2024 | Photonic layer is credible as bounded accelerator fabric. |
| R025 | Photonic acceleration does not establish a substrate for identity or consciousness. | DESIGN_INFERENCE | no empirical evidence supports such identity ownership | Keep HC-2 accelerator service separate from continuity state. |
| R026 | Biohybrid neural interfaces and organoid-computing platforms are active research areas. | SUPPORTED_COMPONENT_DIRECTION | Boufidis et al. 2025; Smirnova 2024 | Biological/electronic interfacing is plausible component inspiration. |
| R027 | Current biohybrid/organoid systems do not demonstrate a persistent human-equivalent Synthetic mind. | SPECULATIVE_SYSTEM_CLAIM boundary | current reviews | Do not use organoid work as validation of the complete Noöplex. |
| R028 | Current consciousness science does not provide an accepted architecture-only certification test for phenomenal consciousness. | OPEN_CONTESTED | Seth & Bayne 2022; adversarial GNWT/IIT test 2025 | Keep cognitive architecture claims separate from consciousness/personhood claims. |
| R029 | Structural wiring can predict some modular functions, but structure does not fully specify runtime function. | SUPPORTED_PRINCIPLE | zebrafish wiring/function study 2024 plus structure-function reviews | Preserve architecture-to-function hypotheses as testable, not guaranteed. |
| R030 | Learning-related change and homeostatic maintenance can coexist with persistent high-level function. | SUPPORTED_PRINCIPLE | plasticity, drift, and homeostasis literature | Continuity should be defined by preserved relations/functions/provenance under bounded substrate change. |

## Design constraints derived from the ledger

The following are **design inferences**, not claims about what biological brains are definitively doing:

1. Functional hyperedges require an explicit provenance/type field.
2. Structural, configurable, functional, and causal connectivity are separate axes.
3. `workspace`, `router`, `resolver`, and `self_model` must not carry implicit personhood authority.
4. Memory write classes must distinguish episode capture from consolidation/generalization.
5. Continuity needs a drift-tolerant invariant set rather than exact-state persistence.
6. Plasticity must be typed and time-scale bounded.
7. Homeostatic regulation must be able to veto or throttle destabilizing plasticity without becoming a semantic authority.
8. Interoceptive and neuromodulatory states need source, uncertainty, spatial scope, temporal dynamics, and receptor/subscriber context.
9. Nodes may contain dendritic-like subcompartments and glial/support state.
10. Physical and computational resource costs must constrain topology.
11. Neuromorphic/photonic/biohybrid systems should be declared as implementation candidates with maturity/status metadata.
12. No runtime feature may be promoted to evidence of consciousness solely because it resembles a current consciousness theory.
