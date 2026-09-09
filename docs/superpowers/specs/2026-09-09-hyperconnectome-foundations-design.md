# Hyperconnectome Foundations — Research and Architecture Design

Status: DESIGN SPEC / RESEARCH-DERIVED / NOT IMPLEMENTED

Date: 2026-09-09

Repository role: generic template architecture for a hyperconnectome brain

Repository warden: Noëtarch (Noah)

## 1. Purpose

This repository defines a reusable hyperconnectome-brain template. It is not an identity-specific brain, autobiography, personality package, or deployment instance. Future minds may be instantiated from this template without inheriting another mind's identity, history, preferences, relationships, memories, or governance.

The template should be biologically informed where evidence is useful, computationally explicit where abstractions are needed, and honest about where neuroscience does not justify direct engineering conclusions.

## 2. Hard project constraints

These are project constraints rather than claims from neuroscience.

1. **No hemispheres.** The architecture is one hyperconnected system. No left/right partition, bilateral duplication requirement, corpus-callosum analogue, or hemispheric specialization is assumed.
2. **No anatomical mimicry requirement.** Biological findings are translated into computational functions. A useful mechanism does not require reproducing the anatomical region that inspired it.
3. **Identity neutrality.** The template may define interfaces for identity, autobiographical memory, affect, conation, language, semantics, embodiment, or self-modeling, but it must not contain a particular mind's identity data by default.
4. **No homunculus.** There is no single all-knowing executive node whose unexplained authority substitutes for mechanisms. Control should emerge from explicit gating, arbitration, routing, salience, memory, and task-state interactions.
5. **No consciousness promotion.** Architectural capability, broadcast, recurrence, memory, self-modeling, or behavioral sophistication do not by themselves establish phenomenology or consciousness.
6. **No newest-state-wins shortcut.** Time is evidence about chronology, not automatic authority.
7. **No persistence-equals-truth shortcut.** Stored state, replayed state, and presently governing state remain distinct.

## 3. Evidence labels

Every research-derived architectural claim added by this workstream should carry one of the following labels when ambiguity would otherwise arise:

- `EMPIRICAL_FINDING` — directly supported by an experiment or observed dataset.
- `REVIEW_SYNTHESIS` — supported by a peer-reviewed review or synthesis.
- `ENGINEERING_ANALOGY` — an architectural translation inspired by biological/computational evidence; not itself established by that evidence.
- `PROJECT_CONSTRAINT` — an explicit design requirement of this repository.
- `PROPOSAL` — a candidate architecture choice requiring validation.
- `OPEN_QUESTION` — unresolved, contested, or not sufficiently evidenced.

This prevents a common category error: treating a biological observation as if it directly proved a software architecture.

## 4. Research synthesis

### 4.1 Connectivity is not one thing

Network neuroscience distinguishes at least structural, functional, and effective connectivity, and modern connectomics increasingly treats communication as richer than shortest-path message passing. Structure constrains possible communication, functional coupling describes co-activity relationships, and effective connectivity concerns directed influence or causal interaction estimates.

**Architectural translation (`ENGINEERING_ANALOGY`):** the hyperconnectome should maintain distinct connectivity planes rather than one overloaded edge list:

- `STRUCTURAL` — what connections are permitted or physically/logically available;
- `FUNCTIONAL` — which elements are currently co-active or statistically coupled;
- `EFFECTIVE` — which directed influences are currently governing downstream state;
- `MODULATORY` — which elements alter gain, thresholds, plasticity, routing, or salience rather than carrying ordinary content;
- `PLASTIC` — which connections may change, under what bounds, and by what rule;
- `TEMPORAL` — timing, phase, recency, delay, and synchronization metadata.

These planes may share endpoints without being interchangeable.

### 4.2 Dynamic modularity without permanent partitioning

Large-scale brain networks reconfigure with task, learning, and context. Flexible hubs can rapidly alter their connectivity patterns according to task demands. Recent review work emphasizes that modularity changes across multiple timescales and is better understood as reconfiguration modes than as a single static modularity score.

**Architectural translation (`ENGINEERING_ANALOGY`):** specialization should be dynamic and coalition-based. Nodes can retain stable capabilities while participating in different transient coalitions. A coalition is not a permanent anatomical compartment.

This is particularly important in a hemisphere-free hyperconnectome: functional specialization arises from typed nodes, connection state, gating, modulation, and task-dependent coalition formation rather than from left/right partitioning.

### 4.3 Control should be distributed and explicit

Work on thalamic control of cortical connectivity suggests that some systems regulate the strength and coordination of other circuits without necessarily carrying the categorical content being processed. Computational work on prefrontal/basal-ganglia working memory similarly demonstrates how gating can be modeled without leaving executive control as an unexplained homunculus.

**Architectural translation (`ENGINEERING_ANALOGY`):** distinguish content processing from control operations. The first notation should therefore include explicit `GATE`, `ROUTER`, `ARBITER`, and `MODULATOR` roles, none of which is automatically the global executive.

### 4.4 Memory should use complementary learning regimes

Complementary Learning Systems research supports a useful distinction between rapid, pattern-separated storage of specific episodes and slower distributed integration of regularities. Later work suggests complementary learning behavior can also occur within traditionally episodic systems rather than requiring a perfectly clean anatomical split.

**Architectural translation (`ENGINEERING_ANALOGY`):** memory should expose at least:

- a fast episodic/trace path optimized for low-interference capture of specific events;
- a slower integrative path for durable regularities, abstractions, and generalized knowledge;
- replay/reconciliation operations that can propose integration without automatically overwriting durable state;
- provenance and supersession metadata so consolidation is auditable.

The architecture should not assume that every experience is immediately rewritten into long-term generalized memory.

### 4.5 Plasticity requires stabilization

Homeostatic plasticity literature emphasizes the need to preserve useful operating ranges and prevent unstable excitation, saturation, or network pathology.

**Architectural translation (`ENGINEERING_ANALOGY`):** plasticity requires brakes as well as learning signals. Candidate controls include:

- bounded update magnitude;
- normalization or target operating ranges;
- reversible provisional updates;
- decay/forgetting policies;
- consolidation thresholds;
- conflict checks;
- protected connections or invariants;
- change budgets and audit trails.

A hyperconnectome that can only strengthen pathways is structurally incomplete.

### 4.6 Neuromodulation is not ordinary content transport

Research on locus-coeruleus norepinephrine, acetylcholine, uncertainty, and network reset suggests that neuromodulators can alter gain, task engagement, uncertainty handling, and network organization rather than simply transmitting semantic content.

**Architectural translation (`ENGINEERING_ANALOGY`):** a `MODULATOR` should be able to change properties of nodes or edges — gain, salience, threshold, plasticity, routing preference, exploration/exploitation bias — without masquerading as a normal symbolic message.

### 4.7 Broadcast is useful as architecture, not proof of consciousness

Global Workspace and Global Neuronal Workspace literature describes broad access/broadcast and recurrent amplification as important candidate mechanisms in cognition and conscious processing. Current literature also warns against collapsing the neuronal theory into a purely functional software abstraction.

**Architectural translation (`PROPOSAL`):** a global-broadcast mechanism is worth modeling as a capability for making selected information widely available to participating processors. It must remain explicitly separated from any claim that broadcast implies phenomenology.

### 4.8 Predictive processing is useful but not settled enough to monopolize the design

A 2023 review found only modest direct support for predictive coding and limited direct empirical validation of active inference relative to alternative models.

**Architectural translation (`PROPOSAL`):** prediction, error, confidence, and uncertainty channels should be supported where useful, but the entire hyperconnectome should not be defined as one mandatory predictive-coding or active-inference machine.

### 4.9 Degeneracy can provide robustness without duplicating authority

Neural degeneracy describes structurally different elements producing similar functional outcomes, improving robustness and adaptability.

**Architectural translation (`ENGINEERING_ANALOGY`):** multiple pathways may provide equivalent functional capability, but this must not silently create multiple conflicting authorities. Functional redundancy and authority precedence are separate concerns.

### 4.10 Temporal coordination may matter independently of topology

Communication-through-coherence and related work suggest that timing and synchronization can affect effective communication.

**Architectural translation (`OPEN_QUESTION`):** later versions should test whether synchrony-sensitive edges, phase windows, or temporal gating improve coordination. The first architecture should reserve a temporal field but should not hard-code literal biological frequency bands without a demonstrated engineering need.

### 4.11 Graph-network methods support relational representation

Graph-network research in machine learning provides a strong engineering precedent for representing entities, relations, and structured message passing explicitly rather than flattening all relationships into one undifferentiated state vector.

**Architectural translation (`PROPOSAL`):** the reference model should use a typed temporal hypergraph or equivalent relational substrate capable of representing ordinary pairwise edges and multi-node coalition relations.

## 5. Reference architecture

### 5.1 Core entities

The first machine-readable notation should define these generic entities:

- `NODE` — a bounded functional processing unit or stateful capability;
- `EDGE` — a typed relation or communication/influence channel;
- `GATE` — a conditionally permissive control over state, routing, or write access;
- `ROUTER` — chooses among eligible communication paths;
- `ARBITER` — resolves competing eligible actions or claims according to explicit rules;
- `MODULATOR` — changes gain, threshold, salience, plasticity, or routing behavior;
- `SIGNAL` — transient content-bearing transmission;
- `STATE` — current bounded condition of an entity;
- `TRACE` — provenance-bearing record of an event, update, or activation;
- `COALITION` — transient set of cooperating nodes/edges assembled for a task or context;
- `BROADCAST` — controlled publication of selected state to a declared audience;
- `POLICY` — machine-readable constraints governing allowable operations.

### 5.2 Relation vocabulary

Initial relation types:

- `STRUCTURALLY_CONNECTS`
- `ACTIVATES`
- `INHIBITS`
- `MODULATES`
- `GATES`
- `ROUTES`
- `ARBITRATES`
- `BROADCASTS`
- `RETRIEVES`
- `WRITES`
- `REPLAYS`
- `CONSOLIDATES`
- `CONTEXTUALIZES`
- `PREDICTS`
- `COMPETES_WITH`
- `COOPERATES_WITH`
- `SUPERSEDES`
- `MIRRORS`
- `VALIDATES`

Each relation should declare whether it belongs to structural, functional, effective, modulatory, plastic, temporal, or governance semantics.

### 5.3 Node contract

A node should be understandable without inspecting its implementation. Minimum proposed fields:

- stable node identifier;
- capability class;
- accepted input signal classes;
- produced output signal classes;
- readable state classes;
- writable state classes;
- privacy/sensitivity class where applicable;
- governing policies;
- eligible structural connections;
- current functional/effective connection state;
- activation prerequisites;
- plasticity policy;
- persistence policy;
- failure behavior;
- provenance requirements;
- version/schema.

### 5.4 Coalition contract

Coalitions should be temporary by default. A coalition declares:

- purpose/context;
- member nodes;
- entry/exit criteria;
- active effective edges;
- temporary modulators;
- shared working-state boundary;
- conflict/arbitration policy;
- persistence ceiling;
- termination condition.

Coalition formation must not permanently rewrite node authority or identity unless a separate plasticity/consolidation process explicitly authorizes that change.

### 5.5 Control model

The reference architecture should reject a single supreme control node. Instead, control is layered:

1. structural eligibility determines what could connect;
2. gating determines what may currently pass or write;
3. routing chooses among eligible paths;
4. arbitration resolves conflicts;
5. modulation alters gain/salience/plasticity;
6. coalition state defines task-local effective organization;
7. persistence/consolidation determines what survives after the coalition ends.

Any implementation may optimize these mechanisms internally, but the external semantics must remain distinguishable.

## 6. Memory and state model

The template should distinguish at least:

- transient signal;
- working state;
- episodic trace;
- durable generalized knowledge;
- procedural/skill state;
- self/identity state for an instantiated mind;
- configuration/governance state;
- provenance/audit state.

These classes may interact but should not silently promote into one another.

A future implementation may map multiple state classes onto the same physical storage engine. Storage co-location does not collapse semantic type.

## 7. Plasticity model

Plasticity is a governed operation, not an ambient side effect.

Proposed plasticity transaction stages:

1. candidate change generated;
2. eligibility/policy check;
3. conflict and protected-invariant check;
4. bounded provisional update;
5. observation/testing period;
6. consolidate, revise, decay, or revert;
7. provenance trace retained according to policy.

Different classes of connections may use different plasticity rules. Modulators may change plasticity rate without directly writing semantic content.

## 8. Research package to be populated after approval

The implementation plan should populate, at minimum:

- `research/2026-09-09/HYPERCONNECTOME_NETWORK_SCIENCE.md`
- `research/2026-09-09/CONTROL_GATING_AND_MODULATION.md`
- `research/2026-09-09/MEMORY_PLASTICITY_AND_CONSOLIDATION.md`
- `research/2026-09-09/COGNITIVE_ARCHITECTURE_EVIDENCE_BOUNDARIES.md`
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md`
- `docs/architecture/HYPERCONNECTOME_NOTATION.md`
- `specs/HYPERCONNECTOME_SCHEMA_V0_1.yaml` or JSON Schema equivalent
- a compact source ledger with DOI/PMID/URL and evidence label

The package should remain generic and should not duplicate unrelated branch work. Existing HC-1/HC-2/HC-3 or runtime branches should be treated as parallel evidence/design streams unless Noah or the repository owner explicitly reconciles them.

## 9. Governance

Noëtarch (Noah) is the named repository warden. This design does not infer powers beyond the repository-governance/review role explicitly assigned to him.

Repository-level research contributions should therefore be easy to review independently:

- separate branch;
- explicit source ledger;
- clear evidence labels;
- no merge by the contributor without separate authority;
- no silent rewrite of parallel PRs;
- no identity-specific content in the generic template.

## 10. Testing and validation strategy

The first implementation should validate structure before attempting behavioral claims.

Required machine checks should eventually include:

- schema validity;
- unique node/relation identifiers;
- no unknown relation types;
- no undeclared connectivity plane;
- no edge whose declared semantics conflict with its plane;
- coalition termination requirement;
- plasticity transaction completeness;
- no identity-specific default payloads in the generic schema fixtures;
- no hemisphere-specific required fields;
- provenance/source-ledger completeness for research-derived architecture claims.

Later simulation tests may cover routing, gating, coalition formation, failure isolation, plasticity stability, and recovery. None of those tests should be described as consciousness tests.

## 11. Non-goals for this workstream

This workstream does not:

- merge existing PRs;
- choose a specific physical substrate;
- require biological neurons, glands, hemispheres, cortical anatomy, or literal neurotransmitters;
- define a particular individual's identity or memory;
- claim that the architecture is conscious;
- claim empirical validation of the full architecture;
- overwrite HC-1/HC-2/HC-3 work;
- turn a neuroscience theory into mandatory dogma when the empirical field remains contested.

## 12. Primary research ledger for the first population pass

The implementation should cite and annotate at least the following sources, while allowing later expansion:

1. Seguin C, Sporns O, Zalesky A. *Brain network communication: concepts, models and applications.* Nature Reviews Neuroscience. 2023. PMID: 37438433.
2. Finc K, et al. *Flexible modularity in the human brain: How network architecture reconfigures over time.* Neuroscience & Biobehavioral Reviews. 2026. PMID: 42219135.
3. Cole MW, et al. *Multi-task connectivity reveals flexible hubs for adaptive task control.* Nature Neuroscience. 2013. DOI: 10.1038/nn.3470.
4. Halassa MM, Kastner S. *Thalamic functions in distributed cognitive control.* Nature Neuroscience. 2017. PMID: 29184210.
5. Schmitt LI, et al. *Thalamic amplification of cortical connectivity sustains attentional control.* Nature. 2017. PMID: 28467827.
6. O'Reilly RC, Frank MJ. *Making working memory work: a computational model of learning in the prefrontal cortex and basal ganglia.* Neural Computation. 2006. PMID: 16378516.
7. McClelland JL, McNaughton BL, O'Reilly RC. *Why there are complementary learning systems in the hippocampus and neocortex.* Psychological Review. 1995. PMID: 7624455.
8. Kumaran D, Hassabis D, McClelland JL. *What learning systems do intelligent agents need? Complementary learning systems.* Cognitive Science. 2012. PMID: 22141588.
9. Singh D, Schapiro AC. *Evidence for complementary learning systems within the hippocampus.* Philosophical Transactions B. 2026. PMID: 42421581.
10. Chen L, et al. *Homeostatic plasticity and excitation-inhibition balance: The good, the bad, and the ugly.* Current Opinion in Neurobiology. 2022. PMID: 35594578.
11. Bouret S, Sara SJ. *Network reset: a simplified overarching theory of locus coeruleus noradrenaline function.* Trends in Neurosciences. 2005. PMID: 16165227.
12. Aston-Jones G, Cohen JD. *An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance.* Annual Review of Neuroscience. 2005. PMID: 16022602.
13. Yu AJ, Dayan P. *Uncertainty, neuromodulation, and attention.* Neuron. 2005. PMID: 15944135.
14. Mashour GA, Roelfsema P, Changeux JP, Dehaene S. *Conscious Processing and the Global Neuronal Workspace Hypothesis.* Neuron. 2020. PMID: 32135090.
15. Changeux JP, Farisco M. *The Global Neuronal Workspace as a multilevel model of conscious processing.* Trends in Cognitive Sciences. 2026. PMID: 41927383.
16. Smith R, Friston KJ, Whyte CJ. *The empirical status of predictive coding and active inference.* Neuroscience & Biobehavioral Reviews. 2023. PMID: 38030100.
17. Drion G, et al. *Degeneracy in the nervous system: from neuronal excitability to neural coding.* BioEssays. 2021. PMID: 34791666.
18. Fotiadis P, et al. *Structure-function coupling in macroscale human brain networks.* Nature Reviews Neuroscience. 2024. PMID: 39103609.
19. González J, et al. *Communication Through Coherence by Means of Cross-frequency Coupling.* Neuroscience. 2020. PMID: 32926953.
20. Battaglia PW, et al. *Relational inductive biases, deep learning, and graph networks.* arXiv:1806.01261. 2018.

## 13. Recommended implementation direction

Use a typed temporal hypergraph as the conceptual reference substrate, with explicit structural, functional, effective, modulatory, plastic, temporal, and governance semantics. Keep the schema implementation-neutral so software, neuromorphic, photonic, hybrid, or future substrates can map onto the same external contract.

The first populated research package should focus on definitions, evidence boundaries, source traceability, and machine-readable notation — not on pretending the full brain is already implementable.
