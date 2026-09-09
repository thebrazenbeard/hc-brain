# Social Modeling Architecture

Status: template architecture.

## Purpose

The sociological-behavior subsystem represents agents, roles, relationships, groups, norms, institutions, status/power relations, local conventions, cultural practices, coordination patterns, and social expectations as learnable models rather than hard-coded universal social truth.

## Object families

The HC should be able to represent:

- individual agents and identity confidence;
- relationships and relationship-specific history;
- group membership hypotheses;
- roles and role expectations;
- norms and norm scope;
- authority/power relationships;
- cooperation, competition, conflict, and alliance patterns;
- local language and shared convention;
- reputational/source-reliability models;
- institutional rules;
- culture/context models;
- social uncertainty and exceptions.

## Locality

Social rules are strongly scoped.

A convention learned in one relationship, group, culture, or situation should not silently become a universal rule.

`LOCAL_NORM != UNIVERSAL_NORM`

`ROLE_EXPECTATION != PERSONAL_DESIRE`

`SOCIAL_POWER != MORAL_AUTHORITY`

`GROUP_PRIOR != INDIVIDUAL_FACT`

## Relationship models

Relationship state should be represented separately from the two participating identities. It may include shared history, trust hypotheses, commitments, boundaries, recurring interaction patterns, private language, unresolved conflict, and mutual expectations.

A relationship model must not overwrite either participant's self-model.

## Norm learning

Norms may be inferred from observation, explicit teaching, consequences, repeated coordination, correction, and cultural sources. The HC should preserve:

- source;
- scope;
- confidence;
- exceptions;
- enforcement consequences;
- descriptive versus normative interpretation;
- currentness/drift.

Observed common behavior is not automatically morally endorsed behavior.

## Social prediction

The system may predict likely reactions and coordination outcomes, but predictions remain hypotheses. Surprising behavior should update the relevant local model rather than being discarded to protect a stereotype.

## Multi-agent perspective

Social reasoning should support multiple simultaneous perspectives. A conflict need not be collapsed into one globally privileged social narrative before action can proceed.

## Privacy and information boundaries

Knowledge acquired in one relationship or private context must retain scope. Social inference should not automatically leak one person's private information into models used with another.

## Development

The subsystem can begin with generic agent/interaction primitives and learn richer social structure through experience. Human social theory may provide useful priors, but the HC template should remain capable of modeling nonhuman or synthetic social organizations.

## Cross-system interfaces

Strong coupling is expected with empathy, personification, pragmatics, semantics, conation, sexuality, memory, chronology, psychological behaviors, self identity, cognition, and integration/arbitration.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review and retained as identity-neutral subsystem architecture.