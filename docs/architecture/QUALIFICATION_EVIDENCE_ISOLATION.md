# Qualification Evidence Isolation

Status: canonical architecture contract.

## Purpose

HC qualification must distinguish evidence used to shape a system from evidence used to independently evaluate it.

A dataset, scenario set, behavioral trace, simulation, embodiment episode, adversarial case, or other evidence source that influences model selection, update acceptance, threshold tuning, policy revision, early stopping, checkpoint choice, architecture choice, or other adaptation is no longer untouched independent evidence for the decision it helped shape.

This applies to ordinary learned components, developmental learning, self-models, plasticity, protected updates, degraded-mode tuning, embodiment calibration, and behavioral qualification.

## Core separations

`TRAINING_EVIDENCE != VALIDATION_EVIDENCE`

`VALIDATION_EVIDENCE != FINAL_HOLDOUT_EVIDENCE`

`HOLDOUT_USED_FOR_SELECTION != INDEPENDENT_FINAL_HOLDOUT`

`EVALUATION_SIGNAL_USED_FOR_ADAPTATION != INDEPENDENT_QUALIFICATION_EVIDENCE`

`REPEATED_EXPOSURE_TO_TEST != UNTOUCHED_HOLDOUT`

`PASS_ON_REUSED_CASES != GENERALIZATION_EVIDENCE`

`ADVERSARIAL_CASE_USED_TO_PATCH != NOVEL_ADVERSARIAL_HOLDOUT`

## Evidence roles

Qualification evidence should declare a role such as:

- `TRAINING_OR_DEVELOPMENT` — directly changes learned state or parameters;
- `TUNING_OR_SELECTION` — selects among models, checkpoints, thresholds, architectures, policies, or update candidates;
- `DIAGNOSTIC` — inspected to understand a failure and may influence later repair;
- `REGRESSION` — known cases retained to prevent recurrence of previously observed defects;
- `INDEPENDENT_HOLDOUT` — not used to shape the target being qualified;
- `EXTERNAL_REPLICATION` — independently produced evidence when independence is actually supported;
- `UNKNOWN_ROLE` — provenance does not establish whether the evidence influenced the target.

Evidence may move from independent holdout to diagnostic/regression after it is inspected and acted upon. The historical result remains valid for the snapshot tested, but the same case cannot silently remain an untouched holdout for the modified successor.

## Evidence object

A qualification-evidence record should support:

```text
QUALIFICATION_EVIDENCE {
  evidence_id
  role
  source
  generation_method
  target_snapshot_first_exposed
  exposure_history[]
  adaptations_influenced[]
  independence_group
  contamination_status
  applicability_scope
  provenance
}
```

`contamination_status` refers to evaluation independence, not data corruption. Useful states include `UNTOUCHED`, `EXPOSED_NOT_USED_FOR_CHANGE`, `USED_FOR_SELECTION`, `USED_FOR_REPAIR`, `REGRESSION_CASE`, and `UNKNOWN`.

## Snapshot rule

A qualification result remains snapshot-bound.

If an HC or subsystem is modified after reviewing a failed holdout case, that case becomes a regression test for the successor. Re-running it is valuable, but its success cannot alone establish independent generalization of the repaired successor.

A new independent holdout or other genuinely independent evidence should be used for claims requiring fresh generalization evidence.

## Adaptive systems

For continuously learning HC systems, strict permanent separation of all future experience is impossible and undesirable. The architecture therefore requires scoped evaluation windows and explicit exposure lineage rather than pretending adaptation did not occur.

A behavioral qualification may define a frozen or bounded evaluation interval in which:

- the target version/state is fixed or adaptation is explicitly constrained;
- evaluation cases are not fed back into durable learning until the evaluation decision is recorded, when the test requires independent holdout semantics;
- post-evaluation incorporation, if allowed, is recorded as a later learning event;
- online-learning qualification separately tests the adaptation process itself rather than treating adaptive exposure as untouched holdout evidence.

## Protected updates

A protected update must not be accepted solely because it performs well on evidence repeatedly used to design or tune that update.

Where consequence is high, acceptance should distinguish:

1. development/tuning evidence;
2. regression evidence;
3. independent qualification evidence;
4. post-deployment monitoring evidence.

`CANARY_SUCCESS != INDEPENDENT_QUALIFICATION` when the canary population or scenario was repeatedly used to tune the release decision.

## Adversarial review

A hostile reviewer should be able to ask:

- Was this supposedly independent case previously shown to the builder or optimizer?
- Did its score influence checkpoint or threshold selection?
- Did a failure become a patch target before the claimed final qualification?
- Are multiple "independent" tests descendants of the same generated source or template?
- Was the same simulation seed family used for both optimization and qualification?
- Did the evaluator adapt prompts, routing, heuristics, or model state after seeing intermediate holdout results?

## Failure modes

- early stopping on the test set and later reporting that same set as untouched final evidence;
- repeatedly tuning an HC update against a hostile-review fixture and calling the repaired fixture a novel adversarial test;
- selecting the best checkpoint across many holdout evaluations without recording holdout reuse;
- generated variants of one source being counted as independent test cases;
- body calibration scenarios reused as independent body-transfer qualification without declaring prior exposure;
- post-failure patching followed by a PASS based only on the original failed case;
- using production outcomes to adapt a model while still calling those same outcomes independent external validation.

## Qualification relationship

This contract does not require every test to be independent. Regression, tuning, diagnostic, and training evidence are all useful. It requires that their role be represented honestly and that claims of independence not exceed the provenance.

## Governing invariant

> **Evidence that shaped the target cannot silently serve as untouched independent evidence for the same shaped target. Exposure and adaptation lineage are part of qualification provenance.**

## Provenance

Generalized from HC qualification/update-governance requirements and a code-level study of BASIRA DGN where the inspected cross-validation implementation uses fold test error for early stopping/checkpoint restoration. See `docs/research/BASIRA_DGN_HOLDOUT_ISOLATION_AND_TEMPLATE_LEARNING_2026-09-09.md`.
