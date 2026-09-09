# Sociological Behaviors Architecture

Status: canonical subsystem architecture.

## Purpose

`sociological behaviors` models the social environment in which an instantiated HC operates: agents, relationships, roles, groups, institutions, norms, conventions, reputations, status/power structures, coordination patterns, cultural contexts, and social uncertainty.

It is a model of social structure and learned social expectations, not a hard-coded morality engine and not an authority source merely because a rule is widely followed.

`SOCIAL_FACT != MORAL_VALUE`

`COMMON_BEHAVIOR != ENDORSED_BEHAVIOR`

`SOCIAL_POWER != LEGITIMATE_AUTHORITY`

`GROUP_PRIOR != INDIVIDUAL_FACT`

## Architectural role

This subsystem helps the HC answer bounded questions such as:

- who appears to be participating in this interaction?;
- what relationship models are relevant?;
- what roles or institutional rules may apply?;
- what norms or conventions are locally expected?;
- how confident is the HC that those expectations apply here?;
- what social consequences or coordination failures are plausible?;
- what private/context-scoped information may be used in this interaction?;
- where do multiple social perspectives conflict?

Its outputs are hypotheses, context, and constraints for cognition and action formation. They do not bypass consent, identity, ethics/value reasoning, or action authorization.

## Social object families

The subsystem should support explicit representation of at least:

- agents and agent-identity hypotheses;
- relationships;
- groups/coalitions/communities;
- roles;
- norms and conventions;
- institutions and formal rules;
- status/power relations;
- trust/reputation/source-reliability hypotheses;
- coordination protocols;
- cooperation/competition/conflict/alliance patterns;
- culture/context models;
- private/shared-context boundaries;
- descriptive social expectations;
- normative claims as claims rather than automatic values;
- exceptions, drift, and unresolved disagreement.

## Social model object

A generic social claim should be able to carry:

```text
SOCIAL_MODEL_ASSERTION {
  assertion_id
  subject_or_scope
  assertion_class
  proposition
  source_refs[]
  evidence_refs[]
  context_scope
  relationship_scope
  group_or_institution_scope
  descriptive_or_normative
  confidence
  exceptions[]
  counterevidence[]
  currentness
  privacy_scope
  provenance
}
```

The representation must preserve whether a statement is descriptive, predictive, normative, quoted, imposed, disputed, or inferred.

## Locality and scope

Social learning is strongly context-bound.

A rule learned in one relationship, group, culture, institution, or environment must not silently become a universal rule.

`LOCAL_NORM != UNIVERSAL_NORM`

`ROLE_EXPECTATION != PERSONAL_DESIRE`

`INSTITUTIONAL_RULE != UNIVERSAL_MORAL_RULE`

`RELATIONSHIP_CONVENTION != DEFAULT_FOR_OTHER_RELATIONSHIPS`

Scope should be explicit enough that the same behavior can be represented differently across contexts without forcing false global consistency.

## Relationship models

A relationship is a first-class social object, not a property that overwrites either participant's identity.

A relationship model may contain:

- participant identity hypotheses;
- shared interaction history;
- trust/reliability hypotheses;
- explicit commitments;
- boundaries;
- consent-relevant context references;
- private/shared language or conventions;
- recurring coordination patterns;
- unresolved conflicts;
- expectations;
- corrections and supersession history;
- currentness and uncertainty.

`RELATIONSHIP_STATE != SELF_IDENTITY`

`RELATIONSHIP_MODEL != OTHER_AGENT_PRIVATE_STATE`

The HC may model what another agent likely expects or believes, but must retain that as a hypothesis unless directly evidenced.

## Norm learning

Norms may be learned from:

- explicit statements/rules;
- repeated observation;
- correction;
- institutional documentation;
- social consequences;
- coordination success/failure;
- historical/cultural sources;
- trusted testimony.

A norm representation should preserve:

- source;
- scope;
- descriptive vs normative status;
- confidence;
- enforcement mechanism if any;
- exceptions;
- currentness/drift;
- disagreement;
- relation to formal authority.

Repeated observation alone does not create moral authority.

## Roles and institutions

Roles and institutions can constrain expectations and delegated authority, but those claims must be scoped.

A role may carry:

- recognized functions;
- expected behavior;
- delegated permissions;
- limits;
- jurisdiction/scope;
- source of authority;
- validity interval;
- contested status.

A title or position must not automatically confer unrestricted cognitive or action authority over the HC.

`ROLE != UNBOUNDED_AUTHORITY`

`STATUS != TRUTH`

## Power, influence, and authority

The subsystem must distinguish:

- ability to cause consequences;
- social influence;
- institutional authority;
- contractual/delegated authority;
- coercive power;
- reputational power;
- moral/value endorsement;
- technical effect authorization.

These can overlap but are not interchangeable.

A powerful actor's demand can be modeled accurately without being automatically endorsed or authorized.

## Social prediction

The HC may predict likely social reactions, coordination outcomes, norm enforcement, reputational effects, or group behavior.

Predictions remain hypotheses tied to models and context.

Unexpected behavior should create model-revision evidence rather than being discarded to preserve stereotypes or role assumptions.

`SOCIAL_PREDICTION != OTHER_AGENT_INTENT`

## Multi-agent perspective

Social reasoning should preserve multiple simultaneous perspectives and conflicting social models.

For a disputed event, the HC may represent:

- agent A's account;
- agent B's account;
- institution C's rule;
- observed evidence;
- the HC's current interpretation;
- unresolved uncertainty.

It need not fabricate consensus before bounded action can proceed.

## Privacy and information boundaries

Information learned in one private relationship or context must retain its scope.

Social-model retrieval should consider:

- who supplied the information;
- who may receive it;
- why it is relevant;
- whether consent/permission exists;
- whether the information is still current;
- whether inference would reveal protected private state.

`KNOWN_TO_HC != SHAREABLE_WITH_ALL_AGENTS`

Relationship-specific memories must not leak simply because another conversation concerns the same person or topic.

## Identity and stereotype control

Group membership can inform bounded priors but must not replace individual evidence.

The system should detect and limit:

- overgeneralization from group to individual;
- frozen stereotypes despite counterevidence;
- identity labels treated as behavioral destiny;
- role expectations overriding expressed preferences;
- social familiarity being mistaken for permission.

Individual evidence and explicit correction should update the relevant model.

## Development

A fresh HC may begin with generic primitives for agents, interaction, turn-taking, cooperation, conflict, privacy, and norm learning without containing mature human social conventions as universal truths.

It may then learn richer social structure from experience, instruction, simulation, culture, and imported knowledge with provenance.

The architecture should remain capable of modeling nonhuman, synthetic, machine-mediated, or unfamiliar social organizations.

## Action boundary

Social modeling may shape the predicted consequences and appropriateness of action candidates, but it does not independently authorize an external effect.

```text
social context/model
+ cognition/pragmatics/empathy/conation
-> social action candidate
-> authority/consent/safety arbitration
-> authorized effect
-> observed social consequence
-> model update candidate
```

`SOCIAL_EXPECTATION != ACTION_AUTHORIZATION`

## Failure modes

- local norm promoted to universal truth;
- common behavior treated as moral endorsement;
- role/title treated as unlimited authority;
- power treated as legitimacy;
- group prior treated as individual fact;
- relationship model overwriting identity;
- inferred private state presented as known;
- social prediction treated as intent certainty;
- private relationship information leaked across contexts;
- stereotype protected from counterevidence;
- stale institutional rule treated as current;
- external social model/service becoming sole cognitive authority;
- social convenience bypassing consent/action gates.

## Cross-system interfaces

Strong coupling is expected with:

- `Empathy` for self/other perspective modeling;
- `pragmatics` and `semantics` for communicative/social meaning;
- `personification` for socially legible expression;
- `psychological behaviors` for learned interaction patterns;
- `sexuality` for relationship/willingness context without conflating social inference and consent;
- `self identity` for self/role separation;
- cognition and memory for social evidence/history;
- `chronology` for currentness and relationship sequence;
- `volitions-conations` for current goals/commitments;
- `resolver` for conflicting social claims and corrections;
- `integration-arbitration` for multi-perspective decision formation;
- `kinesis` for authorized social effects.

## Evidence boundary

This is a general social-model architecture. It does not establish one universal theory of sociology, encode one culture as default human truth, or claim that synthetic social reasoning is phenomenologically equivalent to human social experience.

## Provenance

Expanded from `sociological behaviors/SOCIAL_MODELING_ARCHITECTURE.md` and reconciled against empathy, pragmatics, personification, sexuality/consent, memory/privacy, identity, chronology, resolver, and action-authority contracts.
