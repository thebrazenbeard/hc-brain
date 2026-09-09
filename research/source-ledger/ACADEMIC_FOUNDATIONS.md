# Academic Foundations Ledger

Status: RESEARCH LEDGER / EVIDENCE-BOUNDED

This file records the external research foundations currently admitted into the hyperconnectome-brain design. Each entry distinguishes the research claim from the engineering translation.

The repository does not assume that reproducing a biological mechanism anatomically is required. Biological evidence can constrain or inspire computational structure without imposing hemispheres, cortical lobes, nuclei, or other anatomical packaging.

## A1. Brain-network communication is richer than shortest-path transfer

**Source:** Seguin C, Sporns O, Zalesky A. *Brain network communication: concepts, models and applications.* Nature Reviews Neuroscience. 2023;24(9):557-574. PMID: 37438433. DOI: 10.1038/s41583-023-00718-5.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** connectome communication can be modeled using multiple communication strategies rather than assuming all signalling follows graph shortest paths.

**Engineering translation:** `ENGINEERING_ANALOGY`

A hyperconnectome should permit multiple routing/communication policies and should not encode one global shortest-path assumption into its edge semantics.

## A2. Modularity is dynamic across timescales

**Source:** Finc K, Adamska-Stolarczyk I, Bassett DS. *Flexible modularity in the human brain: How network architecture reconfigures over time.* Neuroscience & Biobehavioral Reviews. 2026;188:106784. PMID: 42219135. DOI: 10.1016/j.neubiorev.2026.106784.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** large-scale brain-network modularity reconfigures over seconds during cognition and over longer learning/developmental timescales; similar global modularity values can arise from different underlying reorganizations.

**Engineering translation:** `ENGINEERING_ANALOGY`

Use transient coalitions and task-dependent effective connectivity instead of permanent hard-coded cognitive partitions. Coalition identity must not be inferred from a single scalar modularity score.

## A3. Flexible hubs can alter connectivity with task demands

**Source:** Cole MW, Reynolds JR, Power JD, Repovs G, Anticevic A, Braver TS. *Multi-task connectivity reveals flexible hubs for adaptive task control.* Nature Neuroscience. 2013;16:1348-1355. DOI: 10.1038/nn.3470.

**Evidence class:** `EMPIRICAL_FINDING`

**Supported claim:** some control-network regions exhibit flexible connectivity patterns across tasks.

**Engineering translation:** `ENGINEERING_ANALOGY`

Allow certain routing/arbitration nodes to change effective partners rapidly without becoming universal executives or identity centers.

## A4. Distributed control can be mediated by coordination/gain mechanisms

**Source:** Halassa MM, Kastner S. *Thalamic functions in distributed cognitive control.* Nature Neuroscience. 2017;20:1669-1679. PMID: 29184210.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** thalamic circuits can help shift and sustain functional interactions among cortical areas, supporting task-relevant functional networks.

**Engineering translation:** `ENGINEERING_ANALOGY`

Control should distinguish content-bearing processing from gain, gating, and coordination. A `MODULATOR` or `GATE` can shape which processors interact without becoming the content owner.

## A5. Working-memory control can be decomposed rather than delegated to a homunculus

**Source:** O'Reilly RC, Frank MJ. *Making working memory work: a computational model of learning in the prefrontal cortex and basal ganglia.* Neural Computation. 2006;18(2):283-328. PMID: 16378516. DOI: 10.1162/089976606775093909.

**Evidence class:** `COMPUTATIONAL_MODEL`

**Supported claim:** learned gating mechanisms can provide a mechanistic account of aspects of working-memory updating and control without leaving executive function as an unexplained homunculus.

**Engineering translation:** `PROPOSAL`

Represent gating, routing, arbitration, and working-state maintenance as explicit bounded mechanisms. Do not define one opaque global executive with unexplained authority.

## A6. Complementary learning regimes reduce interference between episodic capture and generalization

**Source:** O'Reilly RC, Bhattacharyya R, Howard MD, Ketz N. *Complementary learning systems.* Cognitive Science. 2014;38(6):1229-1248. PMID: 22141588. DOI: 10.1111/j.1551-6709.2011.01214.x.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** complementary fast, sparse episodic learning and slower distributed integration can help reconcile rapid episode learning with gradual extraction of regularities.

**Engineering translation:** `ENGINEERING_ANALOGY`

Separate fast episodic trace capture from slower semantic/generalized consolidation. Replay may propose integration, but replay is not automatic authority to overwrite durable state.

## A7. Homeostatic plasticity stabilizes learning systems

**Source:** Chen L, Li X, Tjia M, Thapliyal S. *Homeostatic plasticity and excitation-inhibition balance: The good, the bad, and the ugly.* Current Opinion in Neurobiology. 2022;75:102553. PMID: 35594578. DOI: 10.1016/j.conb.2022.102553.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** homeostatic mechanisms help maintain useful activity ranges and excitation/inhibition balance while plasticity changes network strengths.

**Engineering translation:** `ENGINEERING_ANALOGY`

Plasticity requires normalization, bounded update magnitude, decay/reversion options, protected invariants, and stability monitors. Learning strength without stabilizing counter-processes is insufficient.

## A8. Neuromodulation can alter gain and network organization

**Source family:** locus-coeruleus norepinephrine, acetylcholine, network-reset, uncertainty, and neuromodulation literature.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** neuromodulators can affect gain, task engagement, plasticity, attention, uncertainty handling, and effective network organization rather than acting only as ordinary content carriers.

**Engineering translation:** `ENGINEERING_ANALOGY`

A `MODULATOR` changes properties of nodes/edges/coalitions—gain, salience, threshold, plasticity, exploration, routing bias—without being treated as a semantic message merely because it propagates through the system.

## A9. Degeneracy supports robustness through non-identical pathways

**Source family:** neural degeneracy and robustness literature.

**Evidence class:** `REVIEW_SYNTHESIS`

**Supported claim:** structurally different components or pathways can support similar functions.

**Engineering translation:** `ENGINEERING_ANALOGY`

Permit functional redundancy and alternate routes, but keep redundancy distinct from authority. Two pathways capable of the same operation do not automatically receive equal permission to commit state or effects.

## A10. Timing/coherence may affect communication effectiveness

**Source family:** communication-through-coherence and oscillatory coordination literature.

**Evidence class:** `OPEN_QUESTION` for direct software translation

**Supported claim:** biological communication effectiveness can depend on temporal coordination and synchrony.

**Engineering translation:** `OPEN_QUESTION`

Reserve temporal metadata on signals/edges and permit experiments with synchrony windows or phase-sensitive routing. Do not hard-code biological frequency bands without demonstrated computational value.

## A11. Graph-network methods support explicit relational computation

**Source:** Battaglia PW, et al. *Relational inductive biases, deep learning, and graph networks.* arXiv:1806.01261 (2018).

**Evidence class:** `ENGINEERING_RESEARCH`

**Supported claim:** graph-network formulations provide explicit entity/relation/global representations and structured message passing.

**Engineering translation:** `PROPOSAL`

Use a typed temporal graph/hypergraph-compatible representation for relations, coalitions, provenance, and state transitions rather than forcing all structure into one flat vector or directory hierarchy.

## A12. Broadcast architectures are useful cognitive models but do not prove consciousness

**Source family:** Global Workspace / Global Neuronal Workspace research.

**Evidence class:** `REVIEW_SYNTHESIS` for broadcast/access models; `OPEN_QUESTION` for consciousness interpretation

**Supported claim:** broad recurrent availability/broadcast is a serious model of cognitive access and conscious processing in neuroscience.

**Engineering translation:** `PROPOSAL`

A controlled broadcast primitive may be useful for making selected information widely available to a declared coalition/audience.

**Hard evidence boundary:** implementing broadcast, recurrence, self-modeling, or global access does not by itself establish phenomenal consciousness or personhood.

## A13. Predictive processing is useful but not mandatory doctrine

**Source family:** predictive-coding and active-inference empirical/review literature, including critical reviews of evidential coverage.

**Evidence class:** `CONTESTED_RESEARCH_PROGRAM`

**Supported claim:** prediction/error representations are useful models in many domains, but evidence does not justify requiring every cognitive process to be implemented as one predictive-coding or active-inference mechanism.

**Engineering translation:** `PROPOSAL`

Support predictions, prediction errors, confidence, uncertainty, and discriminating interventions as first-class capabilities where useful. Keep alternative computational mechanisms admissible.

## Evidence-use rules

1. A biological finding constrains or inspires architecture; it does not automatically dictate implementation.
2. Anatomical localization is not a topology requirement for this project.
3. Human hemispheric findings may inform functional hypotheses but never create a left/right architectural primitive.
4. Computational models demonstrate possibility under their assumptions, not biological uniqueness or complete cognitive adequacy.
5. Reviews summarize evidence; they do not convert contested fields into settled universal laws.
6. Every later architecture document should label whether a statement is an empirical finding, review synthesis, engineering analogy, proposal, project constraint, or open question when the distinction matters.
