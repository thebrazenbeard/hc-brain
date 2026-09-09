# Hyperconnectome Brain Research Layer

Status: independent research contribution / not architecture canon

This directory grounds the generic Hyperconnectome Brain template in current neuroscience, cognitive science, computing research, cross-project engineering evidence, and explicit owner design requirements while preserving a strict separation between observation, engineering analogy, architectural implication, and speculation.

## Cognitive-organ boundary

The HC is intended to represent a **self-contained synthetic cognitive organ**. Essential cognition belongs inside the HC boundary. External sensors, actuators, networks, bodies, and computational services may supply observations or effects, but they must not silently fill an unmodeled external hole where the brain's own reasoning is supposed to occur.

See `SELF_CONTAINED_COGNITIVE_ORGAN.md` for the design-boundary synthesis.

## Non-hemispheric invariant

The Hyperconnectome Brain has **no hemispheres**.

Biological studies of lateralization may still be useful as evidence that specialization can coexist with global integration, but the architecture must not instantiate left/right halves, a corpus-callosum analogue, paired hemispheric executives, or any assumption that cognitive specialization requires anatomical bilateral partitioning.

The target is specialization through distributed nodes, dynamic coalitions, typed connectivity, multiple timescales, and plastic routing.

## Complete-capability invariant

The generic brain template should prefer **presence plus lifecycle control** over deleting potentially useful cognitive systems from different builds. A capability may be physically/logically present while `PRESENT_DISABLED`, `DORMANT`, `DEVELOPING`, `ACTIVE`, `INHIBITED`, `DEGRADED`, or `FAULTED`.

Presence does not imply activation, maturity, qualification, salience, authority, permission, or current relevance.

See `HOMEOSTASIS_ALLOSTASIS_AND_NODE_LIFECYCLE.md`.

## Evidence labels

- `ESTABLISHED` — strong enough to use as a baseline design constraint at the stated claim scope.
- `PLAUSIBLE` — evidence-backed, but not stable or universal enough to hard-code without validation.
- `SPECULATIVE` — a reasoned proposal that requires dedicated validation.
- `UNSUPPORTED_OR_CONTRADICTED` — should not be assumed in the baseline architecture.

## Translation rule

Each research finding should be read through five questions:

1. What does the source actually show?
2. Is the claim local to biology or a specific implementation, or does it express a more general systems principle?
3. What synthetic analogue is proposed?
4. What can go wrong when transferring that principle?
5. What experiment would justify promotion into architecture canon?

Project/database lessons use the same discipline: an implementation pattern is evidence that a mechanism can be made explicit, not proof that it is the unique correct brain design.

## Research conclusions that currently look robust

1. **Do not build an all-to-all brain.** Efficient biological networks combine local clustering/modularity with selective long-range integration; wiring, latency, energy, and vulnerability impose real costs. `[S01-S04]`
2. **Do not build one master executive.** Control and action selection are distributed across recurrent loops and specialized structures; coordination is not equivalent to a homunculus. `[S21-S22]`
3. **Treat communication policy as part of cognition.** Network function depends not only on what is connected but on how signals are routed, delayed, gated, prioritized, and transformed. `[S03]`
4. **Plasticity needs plasticity control.** Metaplasticity, homeostasis, and neuromodulation show that learning rate, eligibility, and effective connectivity themselves need state-dependent regulation. `[S06-S09,S41,S54,S56]`
5. **Separate fast acquisition from slow integration.** Complementary-learning-system research strongly supports avoiding one uniform learning rate for episodic capture and general semantic integration. `[S10-S14]`
6. **Memory retrieval may change memory, but retrieval is not permission to rewrite it.** Reconsolidation evidence argues against a model in which recall is always a read-only operation while engineering provenance requires explicit successor transitions. `[S15]`
7. **Multimodal fusion must preserve modality, timing, frame, and uncertainty.** Integration is context-sensitive and multi-timescale rather than a one-time conversion into a single undifferentiated stream. `[S16-S20]`
8. **Attention and salience are not truth.** Allocation of processing resources must remain separate from epistemic confidence, memory admission, and effect authority. `[S44,S57]`
9. **Self-monitoring and agency are fallible inferences.** Confidence and self-attribution can diverge from actual performance/control and therefore require calibration rather than privileged truth status. `[S44-S45]`
10. **Person models are models.** Social inference is distributed, multidimensional, confidence-bearing, and compatible with self/other separation; a model of another agent is not direct access to that agent's private state. `[S46-S49,S64]`
11. **Language, semantics, pragmatics, and grounding are related but not identical.** Meaning should remain action-relevant, provenance-sensitive, referent-preserving, and capable of retaining ambiguity. `[S50-S53]`
12. **Time is a family of operational and inferred relations, not one semantic oracle.** Exact clocks can support audit and scheduling without establishing causality, authority, currentness, or event boundaries. `[S60-S61]`
13. **Credit assignment is not timestamp proximity.** Learning must determine which internal states/actions contributed to outcomes under delayed and distributed causation. `[S62]`
14. **Inactive capacity can remain present.** Biological latent-plasticity evidence supports the broader principle that structural availability and functional activation are separate; the synthetic node lifecycle is an engineering analogue, not anatomical imitation. `[S56,S59]`
15. **Keep compute close to state where possible.** Neuromorphic and in-memory architectures show large potential benefits from reducing data movement, but precision, programmability, routing, device variability, and endurance remain hard constraints. `[S23-S30]`
16. **Photonic compute is promising but should remain heterogeneous.** Photonics can provide exceptional bandwidth and latency for selected operations; nonlinearities, memory, training, conversion, calibration, and integration remain practical bottlenecks. `[S31-S37]`
17. **No substrate result proves a mind.** Hardware capability, network topology, memory persistence, self-modeling, affective modulation, and complex behavior do not by themselves establish consciousness or personhood.

## Navigation

- `NEUROSCIENCE_AND_CONNECTOMICS.md` — topology, communication, hubs/modules, wiring cost, dynamic organization.
- `HIGHER_ORDER_INTERACTIONS_AND_HYPERGRAPHS.md` — higher-order representations and their evidence limits.
- `DISTRIBUTED_CONTROL_AND_ARBITRATION.md` — distributed selection, control loops, arbitration, graceful degradation.
- `ATTENTION_METACOGNITION_AND_SELF_MONITORING.md` — selective attention, confidence, agency, self-monitoring, task flexibility.
- `SEMANTICS_PRAGMATICS_AND_GROUNDING.md` — language/meaning separation, pragmatic inference, grounding, ambiguity, referent identity.
- `SOCIAL_COGNITION_AND_PERSON_MODELS.md` — mentalizing, self/other separation, relationship context, person-model privacy/currentness.
- `NEUROMODULATION_AND_ENDOCRINE_ANALOGUES.md` — gain control, salience, learning-context signals, endocrine transfer limits.
- `HOMEOSTASIS_ALLOSTASIS_AND_NODE_LIFECYCLE.md` — stability control, dynamic activation, dormant/disabled/degraded/faulted capability states.
- `PLASTICITY_MEMORY_AND_CONTINUAL_LEARNING.md` — metaplasticity, complementary learning systems, consolidation, reconsolidation, interference.
- `CHRONOLOGY_EVENT_STRUCTURE_AND_TEMPORAL_CREDIT.md` — clock layers, event segmentation, chronology/currentness separation, delayed credit.
- `MULTIMODAL_SENSORIMOTOR_INTEGRATION.md` — multisensory fusion, body schema, interoception, timing, action-perception loops.
- `SELF_CONTAINED_COGNITIVE_ORGAN.md` — owner design requirement for the HC as the whole cognitive organ with body/peripheral boundary.
- `COMPUTE_MATERIALS_AND_INTERCONNECTS.md` — neuromorphic, in-memory, memristive, photonic, energy/thermal/interconnect constraints.
- `PROJECT_SOURCE_SYNTHESIS.md` — reusable mechanisms extracted from relevant project repositories and structured database schemas.
- `EVIDENCE_LIMITS_AND_OPEN_QUESTIONS.md` — claims that remain uncertain, unsupported, or experimentally bounded.
- `HC_IMPLICATIONS_MATRIX.md` — concise architecture-facing map.
- `SOURCES.md` — bibliography.

## Governance

Research documents may recommend changes to HC-1/HC-2/HC-3 but do not silently rewrite those architectures. Integration should happen through explicit repository review. Repository stewardship, architecture promotion, and implementation qualification remain separate from research contribution.