# Procedural Memory

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `deep memory storage/`, procedural memory stores learned skills, routines, action policies, control sequences, and compiled strategies that can be proposed or executed without reconstructing every declarative step each time.

Procedural capability is not effect authority.

## Procedure record

A procedure may declare:

- stable procedure ID/version;
- capability/goal;
- preconditions;
- required inputs/resources;
- action/transform sequence or policy;
- expected outcomes;
- uncertainty/operating envelope;
- safety/authority requirements;
- learned-from evidence references;
- qualification/evaluation evidence;
- failure/recovery behavior;
- embodiment compatibility where relevant;
- supersession state.

## Learning sources

Procedures may arise from:

- deliberate instruction;
- repeated successful execution;
- imitation;
- planning compilation;
- reinforcement/credit assignment;
- simulation/practice;
- post-embodiment calibration.

The learning source and qualification evidence should remain distinguishable.

## Execution boundary

```text
PROCEDURE_AVAILABLE
!= PROCEDURE_SELECTED
!= PROCEDURE_AUTHORIZED
!= PROCEDURE_EXECUTED
!= EFFECT_VERIFIED
```

A motor/control routine may be internally well learned yet blocked by current safety, context, body capability, resource, or authority policy.

## Adaptation

Procedures may support parameter tuning, body-specific calibration, and context-specific variants while preserving stable lineage and an operating envelope.

A body change may require requalification or adaptation without requiring replacement of the underlying HC cognitive organ.

## Plasticity

Observed consequences may propose procedural updates. Durable change should preserve:

- trigger evidence;
- prior version;
- candidate delta;
- evaluation/qualification result;
- successor version;
- rollback or supersession relation where applicable.

One anomaly should not silently rewrite a broadly qualified procedure.

## Failure modes

- historically successful procedure executes outside its qualified context;
- skill presence is treated as permission;
- learned sequence updates from one anomaly without evaluation;
- silent drift occurs with no version/provenance;
- declarative explanation is mistaken for procedural competence;
- procedural fluency is mistaken for verified external effect;
- body-specific calibration is applied to an incompatible embodiment.

## Provenance

Reconciled from PR #4 `memory/procedural/README.md` into the canonical `deep memory storage/` root and aligned with `kinesis/` and governed plasticity.