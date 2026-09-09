# Procedural Memory

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`memory/procedural/` stores learned skills, routines, action policies, control sequences, and compiled strategies that can be executed or proposed without reconstructing every declarative step each time.

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
- learned-from evidence refs;
- qualification/evaluation evidence;
- failure/recovery behavior;
- supersession state.

## Learning

Procedures may arise from:

- deliberate instruction;
- repeated successful execution;
- imitation;
- planning compilation;
- reinforcement/credit assignment;
- simulation/practice.

The learning source should remain distinguishable.

## Execution boundary

```text
PROCEDURE_AVAILABLE
!= PROCEDURE_SELECTED
!= PROCEDURE_AUTHORIZED
!= PROCEDURE_EXECUTED
!= EFFECT_VERIFIED
```

A motor/control routine may be internally well learned yet blocked by current safety, context, or authority policy.

## Adaptation

Procedures can support parameter tuning and context-specific variants while preserving a stable lineage and operating envelope.

## Failure modes

- successful historical procedure executed outside its qualified context;
- skill presence treated as permission;
- learned sequence updated from one anomaly without validation;
- silent drift with no version/provenance;
- declarative explanation mistaken for procedural competence;
- procedural fluency mistaken for verified external effect.
