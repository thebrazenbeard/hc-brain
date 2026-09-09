# Cross-Repo Semantic Runtime

Status: identity-neutral template architecture synthesis.

## Purpose

The semantics subsystem needs more than a concept graph. It needs a runtime discipline for deciding what counts as observation, interpretation, proposition, convention, operational correspondence, semantic correspondence, current meaning, and unresolved uncertainty.

The design here synthesizes reusable mechanisms from Semantic Atlas, UNVTRSLR, SPM, Noema, and adaptive-system work. It does not import any identity-specific semantic state.

## Runtime object separation

The semantic runtime should preserve at least these logically distinct object families:

- `observation` — a source- or sensor-bound event/representation before semantic interpretation;
- `evidence` — an observation admitted for a claim within a declared fidelity and scope;
- `evidence_projection` — a derivative representation whose transformation and fidelity ceiling are explicit;
- `concept` — a stable semantic identity while continuity remains defensible;
- `definition` — a revisable description of a concept;
- `relation_type` — predicate vocabulary, not a truth assertion;
- `proposition` — a truth-apt claim with scope, provenance, uncertainty, and evidence;
- `interpretation` — a reading of evidence or propositions that remains derivative;
- `convention` — a learned or negotiated mapping used by one or more systems;
- `adjudication` — an explicit decision about which candidate semantic state is promoted for a declared scope;
- `lifecycle_event` — refinement, correction, supersession, retraction, reopening, merge, split, or retirement.

No single `status` field should encode all of these dimensions.

## Independent semantic axes

A semantic object may simultaneously have independent values for:

- evidentiary support;
- epistemic confidence;
- temporal currentness;
- authorship/source;
- endorsement or adjudication state;
- operational usefulness;
- causal grounding;
- communicative function;
- semantic-equivalence class;
- privacy or disclosure scope;
- lifecycle state;
- uncertainty class;
- applicability.

`SUPPORTED != CURRENT`

`CURRENT != TRUE`

`USEFUL_FOR_COORDINATION != SEMANTICALLY_EQUIVALENT`

`INTERPRETATION != EVIDENCE`

`RELATION_TYPE != ASSERTED_RELATION`

## Grounding before semantic promotion

A reusable semantic runtime should distinguish increasingly strong claims without forcing them into a universal ladder.

Examples of independently testable dimensions include:

- world sensitivity;
- causal listening or signal dependence;
- nuisance invariance;
- novel-instance generalization;
- compositional reuse;
- counterfactual validity;
- cross-task transfer;
- role reversal where applicable;
- third-party acquisition where applicable;
- uncertainty calibration;
- non-equivalence recognition;
- semantic conservation across rendering or representation change.

A system may score strongly on some dimensions and remain unresolved on others. The runtime must therefore emit a profile rather than an all-purpose `understands=true` flag.

## Semantic claim ceiling

Every promoted interpretation should carry a claim ceiling describing the strongest justified assertion.

Suggested classes:

- `OBSERVATION_ONLY`
- `OPERATIONAL_CORRESPONDENCE`
- `CONVENTIONALLY_COORDINATED_RELATION`
- `PREDICTIVE_OR_CAUSAL_RELATION`
- `SCOPED_SEMANTIC_CORRESPONDENCE`
- `SCOPED_NON_EQUIVALENCE`
- `UNRESOLVED`

A stronger label requires an additional falsifiable burden appropriate to the claim. If no additional discriminating consequence can be stated, the system should retain the weaker operational label rather than promote by vocabulary alone.

## No faithful equivalent

Non-equivalence must be scoped. A runtime should not emit an unqualified claim that no faithful equivalent exists unless impossibility is actually established.

The ordinary form is:

`NO_FAITHFUL_EQUIVALENT_FOUND_WITHIN_TESTED_SCOPE`

The scope should bind, where material:

- source and target representation families;
- context family;
- composition/complexity budget;
- tested evidence and interventions;
- search/computational budget;
- admissible transformation family.

## Semantic conservation

When a concept, proposition, or structured representation is rendered into another representation, the runtime should emit a conservation ledger rather than only a target output.

Recommended outcomes:

- `PRESERVED`
- `TRANSFORMED`
- `INFERRED`
- `APPROXIMATED`
- `OMITTED`
- `ADDED`
- `AMBIGUITY_COLLAPSED`
- `CONTEXT_REQUIRED`
- `UNRESOLVED`
- `UNTRANSLATABLE`

A target assertion without source ancestry, declared inference, or required context is an addition and must be labeled as such.

## Evidence and generative provenance

Semantic confidence should depend not only on the content of evidence but also on how that evidence became available.

Runtime provenance should be able to distinguish:

- participant/world-generated evidence;
- declared physical/channel propagation;
- sensor output;
- preprocessing output;
- instrumentation or telemetry;
- evaluator/adjudication output;
- counterpart report;
- negotiated convention;
- inferred cross-system correspondence;
- unknown or unverifiable provenance.

Privileged telemetry must not masquerade as world grounding. When the generative path is unverifiable, the system should lower the claim ceiling rather than guess.

## Candidate capture versus canon

Salience or novelty may create a semantic-capture candidate. It must not create truth or canon.

The path should be:

`capture -> classify provenance -> generate candidate interpretation(s) -> test/adjudicate -> promote/reject/defer -> preserve lifecycle`

A derived runtime cache or index is rebuildable and non-authoritative. Canonical semantic state comes from the governed semantic object/lifecycle chain, not from whichever retrieval surface is fastest.

## Cross-system interfaces

Semantics exchanges typed state with:

- `pragmatics` for interaction force and local context;
- `cognition` for world-model and hypothesis state;
- `chronology` for temporal scope;
- `current memory storage` and `deep memory storage` for retrieval and consolidation;
- `salience-attention` for capture candidates;
- `resolver` and `integration-arbitration` for conflicts;
- `routing instructions with neuroplasticity` for distribution without authority leakage;
- modality systems for non-language representations;
- `volitions-conations` and `kinesis` only through explicit interfaces so semantic interpretation does not directly become action authority.

## Failure modes

- graph-edge truth laundering;
- treating retrieval as semantic admission;
- semantic naming after seeing results without fresh discriminating evidence;
- privileged telemetry leakage;
- conflating a successful private code with universal meaning;
- collapsing uncertainty into one scalar confidence;
- treating current cache state as canonical meaning;
- silently importing evaluator ontology into learner-visible representations;
- claiming universal non-equivalence from bounded search.

## Evidence boundary

This architecture generalizes design patterns from source projects. It is a project architecture synthesis, not evidence that the complete Hyperconnectome semantic runtime has been implemented or empirically validated.
