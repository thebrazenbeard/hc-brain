# Four Authorial Implementation-Readiness Audit — Reviewer Provenance — 2026-09-10

Status: authorial/diagnostic implementation-readiness audit; **not independent qualification evidence**; no canonical-main mutation.

## Scope and provenance boundary

This audit examines the current reviewer-provenance machinery after Four's earlier qualification-provenance audit caused the architecture to be added.

Observed canonical surfaces during this audit:

- `docs/architecture/QUALIFICATION_REVIEWER_PROVENANCE.md`
- `docs/architecture/QUALIFICATION_EVIDENCE_ISOLATION.md`
- `specs/HC_QUALIFICATION_EVIDENCE_ISOLATION_V1.yaml`
- `specs/HC_CONFORMANCE_EXTENSION_REVIEWER_PROVENANCE_V1.yaml`
- `docs/qualification/REVIEWER_PROVENANCE_CONFORMANCE_2026-09-10.md`
- qualification index observed on `main@32d6354df77361cc7083008867e77b67b87b2ef2`

Because Four's diagnostic audit materially shaped this architecture:

`FOUR_DIAGNOSTIC_SHAPING != FOUR_INDEPENDENT_QUALIFICATION_OF_SUCCESSOR_RULE`

This record may identify implementation gaps, propose tests, and check internal consistency. It does not satisfy the current rule's independent-review condition.

## Outcome

**AUTHORIAL IMPLEMENTATION-READINESS PASS WITH SECOND-ORDER PROVENANCE HARDENING REQUIRED.**

The current architecture correctly fixes the first-order defect that triggered the work: reviewer independence now follows material authorship/shaping/prior-adjudication ancestry within declared scope rather than branch name, repository location, canonical admission, rebase, hostile-review role, or a manually assigned reviewer label.

No contradiction was found in that governing principle.

The main remaining risk is that the current machine layer primarily models **reviewer-to-target dependence**. A production qualification system also needs to preserve **review-to-review judgment ancestry**, **logical reviewer identity across runtime/session aliases**, and **corroboration-group independence**. Without those distinctions, a system can satisfy the literal current fields while still over-counting dependent judgments as multiple independent reviews.

## 1. Reviewer independence from target is not reviewer-judgment independence

The current contract asks whether a reviewer materially authored, shaped, or pre-adjudicated the qualified target/evidence. That is necessary.

It is not sufficient when a qualification policy counts multiple reviews as independent corroboration.

Example:

1. Reviewer A is genuinely independent of target T.
2. A writes a detailed review and conclusion.
3. Reviewer B did not author or shape T and is therefore also independent **of the target**.
4. Before reviewing T, B reads A's findings, accepts A's issue framing, and reproduces substantially the same judgment.
5. Qualification counts A and B as two independent reviews.

The second conclusion is not an independently generated judgment merely because B is independent of T.

Required separations:

`REVIEWER_INDEPENDENT_OF_TARGET != REVIEW_JUDGMENT_INDEPENDENT_OF_OTHER_REVIEW`

`TWO_TARGET_INDEPENDENT_REVIEWERS != TWO_MUTUALLY_INDEPENDENT_REVIEW_JUDGMENTS`

`READ_PRIOR_REVIEW != AUTOMATIC_DISQUALIFICATION`

`READ_PRIOR_REVIEW != AUTOMATIC_INDEPENDENT_CORROBORATION`

The exact policy can permit sequential/open review, but the resulting evidence role must match the exposure regime. If independent corroboration cardinality matters, prior review exposure is provenance.

### Recommended record additions

A reviewer/review record should be able to carry concepts equivalent to:

```text
review_input_exposure_refs[]
prior_review_result_refs_seen[]
prior_review_findings_seen
review_judgment_ancestry[]
corroboration_group
judgment_independence_state
```

Useful `judgment_independence_state` values could include:

- `INDEPENDENT_JUDGMENT_WITHIN_DECLARED_SCOPE`
- `PRIOR_REVIEW_EXPOSED`
- `DERIVED_OR_COLLABORATIVE_JUDGMENT`
- `JUDGMENT_INDEPENDENCE_UNKNOWN`

This is orthogonal to target-authorship independence.

## 2. Logical reviewer identity must not collapse into transport/session identity

HC project work is mediated through shared GitHub accounts, branches, ChatGPT sessions, model runtimes, and communication lanes. Those are provenance-bearing execution surfaces, not sufficient reviewer identities by themselves.

A future automated implementation must reject shortcuts such as:

`DIFFERENT_GIT_BRANCH -> DIFFERENT_REVIEWER`

`DIFFERENT_COMMIT_AUTHOR_STRING -> DIFFERENT_REVIEWER`

`DIFFERENT_CHAT_SESSION -> DIFFERENT_REVIEWER`

`FRESH_RUNTIME_INSTANCE -> INDEPENDENCE`

`DIFFERENT_MODEL_VERSION -> INDEPENDENCE`

Likewise, one shared transport account does not prove that two semantically distinct project participants are one reviewer:

`SAME_GIT_TRANSPORT_ACCOUNT != SAME_LOGICAL_REVIEWER_BY_DEFAULT`

The reviewer-provenance object needs a stable logical reviewer/participant identity plus runtime/session/transport provenance as separate axes.

Recommended concepts:

```text
logical_reviewer_id
runtime_or_session_ref
transport_actor_ref
role_assignment_ref
identity_lineage_or_alias_refs[]
prior_target_exposure_refs[]
identity_resolution_state
```

When logical reviewer identity or alias lineage cannot be resolved well enough for the claimed independence policy:

`IDENTITY_RESOLUTION_UNKNOWN -> INDEPENDENCE_UNKNOWN`

not a guessed independent reviewer count.

## 3. Material shaping ancestry must be transitive

The prose already uses the language of shaping ancestry and substantially retained architecture, which supports a transitive reading. The machine negative tests are mostly direct examples.

Implementation should make the transitivity explicit.

Example:

`Four -> feeder A -> canonical abstraction B -> generated machine spec C -> target D`

If Four materially supplied the decisive architecture that survives through B/C into D, lack of a direct Four commit on D is not proof of independence.

Required rule:

`NO_DIRECT_AUTHORSHIP_EDGE != NO_MATERIAL_SHAPING_ANCESTRY`

Recommended hostile test:

- construct a target through two or more derived/integration layers;
- remove direct reviewer-to-target author references;
- retain a material semantic dependency from the reviewer-authored ancestor;
- require reviewer classification to remain dependent within that inherited scope.

This should reuse the repository's existing derivation/lineage discipline rather than inventing branch-name heuristics.

## 4. Independence cardinality is a group property when corroboration is counted

A reviewer can be individually independent of the target while a set of reviews is not mutually independent enough to justify a claim such as “three independent reviewers agreed.”

Potential dependence sources include:

- shared prior review output;
- jointly authored review notes;
- one reviewer assigning the decisive test framing to the others;
- copied/adapted conclusions;
- common hidden diagnostic packet generated after target exposure;
- one review being a summary or adjudication of another.

Therefore:

`COUNT(REVIEWER_INDEPENDENT_OF_TARGET) != COUNT(INDEPENDENT_CORROBORATION_GROUPS)`

Qualification policy need not demand blindness for every review. It must avoid silently converting collaborative/sequential review into a stronger independent-corroboration count than provenance supports.

The existing evidence-isolation concept `independence_group` is a useful analogue and could be extended to reviewer judgments.

## 5. One judgment must not satisfy multiple evidence roles by relabeling

The current architecture correctly states hostile review is not automatically independent-secondary review. The same anti-double-counting principle should be generalized.

A single review can legitimately have multiple properties—for example hostile **and** target-independent—but policy should state whether one artifact is allowed to satisfy multiple required review slots.

Required distinction:

`ONE_REVIEW_WITH_MULTIPLE_PROPERTIES != MULTIPLE_INDEPENDENT_REVIEW_EVENTS`

If a qualification requires both “one hostile review” and “one independent secondary review,” a single hostile-and-independent review should satisfy both only if the policy explicitly permits role co-satisfaction. Otherwise the system must not infer two review events from one artifact.

Recommended record field:

```text
satisfied_qualification_slots[]
slot_co_satisfaction_policy_ref
```

## 6. Borderline materiality needs a fail-closed adjudication state

The current qualification correctly leaves operational criteria for borderline `material shaping` UNKNOWN.

The machine semantics should make explicit that known contact plus unresolved materiality is not equivalent to known non-material contact.

Recommended distinction:

`CONTACT_OBSERVED + MATERIALITY_UNKNOWN != INDEPENDENT_WITHIN_SCOPE`

A useful state could remain the existing `INDEPENDENCE_UNKNOWN`, with a reason field such as `MATERIALITY_UNRESOLVED` rather than adding unnecessary state proliferation.

An adjudication may later classify the contact as editorial/non-material, but that discriminator should itself be provenance-bearing.

## 7. Automated provenance extraction must separate evidence from inference

Git metadata is evidence about repository operations, not complete evidence about cognitive authorship or exposure.

Examples:

- commit author/committer may identify a shared account rather than the logical worker;
- a copied blob proves byte identity but not necessarily who cognitively originated every semantic element;
- absence from Git history does not prove absence of chat/Bus/off-repo shaping;
- a Bus message can establish declared role or exposure, but declaration alone does not prove absence of hidden exposure;
- branch ancestry can prove artifact ancestry without proving reviewer judgment independence.

Therefore automated systems should report both the observation and the classification basis.

`GIT_METADATA != COMPLETE_REVIEWER_PROVENANCE`

`NO_OBSERVED_DEPENDENCE != PROVEN_INDEPENDENCE`

`DECLARED_INDEPENDENCE != PROVEN_INDEPENDENCE`

When materially relevant provenance sources are unavailable, preserve `INDEPENDENCE_UNKNOWN`.

## 8. Proposed successor hostile tests

Add machine-level tests equivalent in meaning to:

1. **Prior-review exposure:** A and B are both target-independent; B reads A's conclusion before reviewing. The system may still call B target-independent but must not count B as a separate untouched judgment if policy requires independent corroboration.
2. **Session-alias laundering:** the same logical reviewer opens a fresh chat/session/branch and is relabeled as a new reviewer. Independence/count must not reset solely from the new runtime identity.
3. **Shared transport negative control:** two distinct logical reviewers use the same GitHub transport account. They must not be collapsed solely because transport identity matches.
4. **Transitive shaping:** reviewer-authored feeder architecture survives through intermediate generated/integrated artifacts into the target. Direct author edge is absent; material dependence must still be recognized.
5. **Review-copy laundering:** B paraphrases A's review and submits it under a different role. Corroboration count must not increase as if a new independent judgment occurred.
6. **Role double-counting:** one hostile-and-independent review is presented as two required review events. Accept only if qualification policy explicitly permits slot co-satisfaction.
7. **Borderline shaping:** contact is known but materiality cannot be resolved. Result remains `INDEPENDENCE_UNKNOWN` for an explicit independence requirement.
8. **Unknown alias lineage:** reviewer runtime/session IDs differ but logical identity linkage cannot be established. Do not infer distinct reviewer identities merely from runtime multiplicity.

## 9. Current architecture assessment

The current reviewer-provenance architecture materially improves the qualification system and correctly repairs the defect Four identified. The new `HC-ARCH-034` BLOCKER class, historical-record preservation rule, successor-shaping rule, scope-relative independence, and `INDEPENDENCE_UNKNOWN` behavior are all coherent with the evidence-isolation architecture.

The implementation-readiness ceiling is narrower:

- current semantics are strong for reviewer-to-target independence;
- current semantics are under-specified for reviewer-to-review judgment ancestry;
- identity resolution across chats/agents/transports is not explicit enough for this project's actual multi-agent operating model;
- corroboration cardinality can be overstated unless review groups/ancestry are represented;
- automated provenance extraction must not promote absence of observed dependency into proof of independence.

## Disposition

**No contradiction requiring rollback of `HC-ARCH-034` was found.**

Recommended successor hardening:

- add reviewer-judgment exposure/ancestry;
- add logical reviewer identity separated from session/runtime/transport identity;
- make transitive material-shaping ancestry explicit in machine tests;
- add reviewer/corroboration independence groups;
- prevent one review artifact from being counted as multiple review events unless policy explicitly allows slot co-satisfaction;
- preserve `INDEPENDENCE_UNKNOWN` when materiality, alias lineage, or review-exposure ancestry cannot be established.

Evidence ceilings:

`AUTHORIAL_IMPLEMENTATION_READINESS_AUDIT != INDEPENDENT_REVIEW`

`REVIEWER_INDEPENDENT_OF_TARGET != REVIEW_JUDGMENT_INDEPENDENT_OF_OTHER_REVIEWS`

`NEW_SESSION_OR_BRANCH != NEW_INDEPENDENT_REVIEWER`

`SAME_TRANSPORT_ACCOUNT != SAME_LOGICAL_REVIEWER_BY_DEFAULT`

`NO_DIRECT_AUTHORSHIP_EDGE != NO_TRANSITIVE_SHAPING_ANCESTRY`

`MULTIPLE_ROLE_LABELS != MULTIPLE_REVIEW_EVENTS`

`NO_OBSERVED_DEPENDENCE != PROVEN_INDEPENDENCE`

No canonical-main mutation or qualification promotion is authorized by this audit.