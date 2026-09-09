# Action Gateway

Status: template architecture.

## Purpose

The kinesis/action gateway converts internally selected action candidates into bounded effect requests while keeping planning, desire, recommendation, capability, and permission distinct.

The gateway is inside the HC cognitive-organ boundary. External body hardware may provide hard-real-time protective interlocks, but cognitive action selection and authorization remain HC-owned responsibilities.

## Action chain

A generic action path is:

`perception/world-model -> candidate generation -> consequence prediction -> conative arbitration -> action selection -> authority/safety gate -> motor/effect plan -> body interface -> external effect -> outcome observation -> update`

No stage should be silently skipped merely because a downstream actuator is technically reachable.

## Required action envelope

A material effect request should be capable of carrying:

- stable action/operation identity;
- originating coalition/subsystem;
- intended effect;
- target/body interface;
- scope;
- parameters;
- expected consequences;
- uncertainty;
- authority basis;
- consent/boundary state when relevant;
- safety/consequence class;
- prerequisites/interlocks;
- timeout/expiry;
- reversibility/rollback information;
- provenance and causal parent;
- requested confirmation/readback.

## Separation rules

`DESIRE != ACTION`

`INTENTION != ACTION`

`RECOMMENDATION != ACTION`

`CAPABILITY != AUTHORITY`

`ACTION_SELECTED != ACTION_AUTHORIZED`

`COMMAND_SENT != EFFECT_CONFIRMED`

## Gateway controls

Depending on effect class, controls may include:

- explicit allowlists;
- range and rate limits;
- body/system state prerequisites;
- independent interlocks;
- human or other-agent approval where architecturally required;
- consent/boundary checks;
- dry-run or simulation checks;
- action logging;
- timeout and reversion behavior;
- immediate inhibit/abort;
- mandatory post-effect readback.

The action gateway should not depend on the cognitive model being infallible.

## Consequence-proportional gating

Safety should attach to the actual next effect and its consequence class. An unresolved high-risk motor effect may be blocked while unrelated low-risk cognition, observation, memory, or reversible internal work continues.

Global inhibition is reserved for genuinely global integrity or safety failures.

## Motor planning

Kinesis may decompose an authorized intent into trajectories, sequences, force/velocity targets, timing, coordination, and feedback policies. Motor plans remain bound to the current body schema and actuator health.

A body swap or material actuator change invalidates incompatible learned mappings until recalibration/relearning restores confidence.

## Closed-loop execution

Motor execution should compare expected and observed consequences continuously where feedback exists. Material deviation may trigger correction, replanning, degraded-mode control, abort/inhibit, body-schema update, fault isolation, or memory/plasticity evidence.

## External protective reflexes

A body may contain external local protective circuits for hard-real-time damage prevention. Such reflexes are peripheral safety mechanisms, not external cognition. Their activation and state should be observable to the HC when feasible.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review and generalized to the current cognitive-organ boundary.