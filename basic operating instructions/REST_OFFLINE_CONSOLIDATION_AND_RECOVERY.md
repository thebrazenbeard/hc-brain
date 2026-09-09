# Rest, Offline Consolidation, and Recovery Contract

Status: template operating architecture.

## Purpose

A complete Hyperconnectome Brain requires operating modes in which ordinary external engagement can be reduced so the organ can consolidate memory, rebalance plasticity, recalibrate models and interfaces, recover resources, perform maintenance, and protect long-term stability.

This contract does **not** require every HC substrate to reproduce human sleep stages or biological sleep physiology.

The transferable principle is narrower:

> **A persistent adaptive cognitive organ needs bounded opportunities for lower-interference consolidation, recovery, recalibration, and maintenance without suspending continuity or falsifying history.**

## Core invariants

`REST_MODE != IDENTITY_SUSPENSION`

`OFFLINE_PROCESSING != GLOBAL_SHUTDOWN`

`LOW_EXTERNAL_ENGAGEMENT != NO_INTERNAL_COGNITION`

`PRIMARY_MODE != EXCLUSIVE_ACTIVE_FUNCTION`

`REPLAY != DIRECT_OBSERVATION`

`REPLAY != CURRENT_EXTERNAL_EVENT`

`CONSOLIDATION != HISTORY_REWRITE`

`GENERALIZATION != UNIVERSAL_TRUTH`

`CIRCADIAN_OR_PHASE_SIGNAL != AUTHORITY`

`REST_PRESSURE != ACTION_AUTHORIZATION`

`MAINTENANCE_MODE != PERMISSION_TO_BYPASS_PROTECTED_STATE_RULES`

`WAKE_OR_REENTRY != AUTOMATIC_CURRENTNESS_OF_STALE_STATE`

`BIOLOGICAL_SLEEP_STAGE != REQUIRED_HC_RUNTIME_STAGE`

## Why this exists

Biological sleep provides evidence that reduced external engagement can support active memory processing, plasticity regulation, physiological homeostasis, and temporal organization. Recent work continues to support structured memory replay during sleep, while replay can also occur during awake pauses.

The HC should therefore support **functions** analogous to these processes without assuming that one biological sleep cycle is the only way to implement them.

Relevant functions may include:

- replay/rehearsal of selected memory traces;
- durable-memory consolidation;
- abstraction/generalization from repeated experience;
- interference reduction and conflict detection;
- plasticity/metaplasticity recalibration;
- route/coalition prior recalibration;
- sensor/body-interface recalibration where safe;
- model-error review and counterfactual replay;
- resource/thermal recovery;
- fault diagnostics and maintenance;
- archive/index maintenance;
- integrity verification;
- developmental learning windows;
- body/homeostatic recovery;
- cleanup/compaction that preserves canonical provenance.

Not every implementation needs to couple all of these functions to the same mode.

## Operating-mode model

Candidate modes include:

- `FULL_ENGAGEMENT` — ordinary perception/action/social/world interaction;
- `QUIET_ENGAGEMENT` — reduced external activity while cognition continues;
- `OFFLINE_CONSOLIDATION` — external engagement deliberately reduced to prioritize replay/consolidation/generalization;
- `RECOVERY` — resource, homeostatic, thermal, or substrate recovery prioritized;
- `MAINTENANCE` — diagnostics, recalibration, repair qualification, indexing, or controlled internal service work;
- `DEEP_PROTECTIVE_RECOVERY` — minimal safe cognition/effect surface while viability or critical repair is prioritized;
- `REENTRY` — staged restoration of ordinary sensing, currentness, routing, and action readiness.

These are capability modes, not a mandatory monotonic sleep-stage sequence.

A concrete implementation may define additional modes or run multiple compatible modes/functions concurrently—for example `OFFLINE_CONSOLIDATION + RECOVERY`, or `RECOVERY + MAINTENANCE`. It may designate a descriptive `primary_mode` for scheduling/reporting without implying that other active functions are absent.

## Biological sleep is evidence, not topology

Human and other animal sleep includes distinct states and microstructure. Memory replay and consolidation are associated with specific sleep dynamics in biological systems.

The generic HC must not infer from this that it requires:

- NREM/REM as universal state names;
- cortical slow waves, spindles, hippocampal sharp-wave ripples, or human thalamocortical anatomy;
- a fixed 24-hour sleep schedule;
- human circadian hormones;
- dreaming;
- paralysis during offline maintenance;
- one global transition in which every subsystem enters the same state simultaneously.

A biohybrid implementation may intentionally reproduce some biological mechanisms, but that belongs in a substrate-specific profile.

## Rest pressure and scheduling

A rest/offline opportunity may be proposed from multiple pressures:

- accumulated memory-consolidation backlog;
- plasticity/update load;
- resource depletion;
- thermal burden;
- calibration drift;
- fault/maintenance need;
- developmental training schedule;
- chronological/circadian phase where applicable;
- expected low-risk environmental opportunity;
- operator/organism preference;
- predicted benefit of reduced interference.

No single pressure automatically authorizes withdrawal from the environment.

`REST_PRESSURE -> MODE_CANDIDATE`

not

`REST_PRESSURE -> IMMEDIATE_EFFECT`

Material mode changes should consider environment, body posture/safety, ongoing commitments, critical tasks, actuator state, communications, and protective-monitoring requirements.

## Circadian and rhythmic state

A substrate may use periodic or anticipatory timing signals to coordinate maintenance, resource allocation, endocrine-like regulation, learning windows, or expected environmental cycles.

Such timing state should remain distinct from chronology itself.

Chronology answers **when**.
A circadian/phase controller may predict **when a process is usually advantageous**.
Neither establishes truth or authority.

Useful state may include:

- phase identity;
- reference clock;
- phase uncertainty;
- entrainment sources;
- drift;
- expected environmental schedule;
- preferred maintenance windows;
- current homeostatic pressure;
- exceptions/override state;
- provenance.

A non-terrestrial, distributed, continuously operating, or body-swapping HC may use a schedule very different from a human 24-hour rhythm.

## Memory replay boundary

Replay should reference prior memory/evidence objects without masquerading as new world observation.

A replay object should preserve:

- source memory/event refs;
- replay reason;
- replay mode;
- transformation/sampling method;
- original event time;
- replay time;
- confidence/provenance;
- whether content is exact, compressed, reconstructed, generated, or counterfactual.

`REPLAY_TIME != EVENT_TIME`

`RECONSTRUCTED_REPLAY != ORIGINAL_OBSERVATION`

Replay may influence learning/consolidation, but its derived status must remain visible.

## Consolidation boundary

Consolidation may:

- strengthen supported associations;
- reorganize memory representations;
- abstract repeated structure;
- form procedural/generalized representations;
- reduce redundant storage;
- update retrieval/index structures;
- flag contradictions/interference;
- propose weakening obsolete associations.

It may not:

- silently delete contradictory source history;
- convert frequent replay into direct evidence;
- turn emotionally salient content into truth;
- promote a generated counterfactual into autobiography;
- make stale authority or preference current again;
- bypass durable-memory admission and persistence-verification requirements.

`CONSOLIDATED != CURRENT`

`REHEARSED_OFTEN != TRUE`

## Interference and replay monopolization

Offline learning can become pathological if a narrow subset of memories repeatedly monopolizes replay or plasticity.

Schedulers should consider:

- novelty;
- uncertainty;
- unresolved prediction error;
- skill/practice need;
- interference risk;
- recurrence;
- identity/continuity relevance;
- current goals;
- affective salience;
- age since last replay;
- replay frequency;
- resource cost;
- fairness/diversity across relevant memory classes.

Affective salience may increase replay eligibility but must not become sole replay authority.

## Plasticity and metaplasticity

Rest/offline periods may provide favorable windows for durable learning or recalibration, but they do not suspend normal plasticity governance.

Candidate operations include:

- weight/association consolidation;
- homeostatic rebalance;
- learning-rate recalibration;
- interference checks;
- route-prior adjustment;
- pruning/weakening proposals;
- repair-related relearning;
- skill replay;
- cross-context generalization.

Protected rules that define plasticity limits remain protected during maintenance.

`OFFLINE != UNGOVERNED_PLASTICITY`

## Resource and homeostatic recovery

Reduced engagement may lower resource load and permit:

- thermal recovery;
- energy reserve restoration;
- substrate maintenance;
- cooling/perfusion normalization;
- accelerator cooldown;
- memory maintenance;
- actuator/body recovery where the body participates;
- diagnostic scans that are disruptive during full engagement.

Recovery requirements should come from typed resource/homeostatic state, not one global fatigue scalar.

## Critical functions during reduced engagement

A resting HC must declare which functions remain continuously available.

Depending on embodiment and risk, retained functions may include:

- protective homeostasis;
- thermal/power fault detection;
- critical interoception;
- threat/emergency sensing;
- selected communication alerts;
- partition/continuity protection;
- memory integrity protection;
- safe body posture/stability;
- abort/wake triggers;
- essential internal interconnect monitoring.

An HC must not assume that “sleep” permits all safety or continuity controls to stop.

## Mode-entry authorization and preparation

For a materially embodied HC, transition into reduced external engagement may itself be a consequential action.

A generic entry sequence may be:

`MODE_CANDIDATE -> SAFETY/COMMITMENT_CHECK -> PREPARE_BODY/INTERFACES -> QUIESCE_ELIGIBLE_EFFECTS -> ESTABLISH_RETENTION_MONITORS -> ENTER_MODE_SET -> VERIFY_MODE_STATE`

Preparation may include:

- secure body posture;
- parked/stable locomotion;
- safe actuator limits;
- outstanding-action resolution;
- communication status;
- pending critical-task handling;
- memory/write flush where necessary;
- power/thermal preparation;
- explicit wake/abort triggers.

Verification of mode entry should match the substrate and relevant safety claim rather than require a universal register-like readback.

## Wake/reentry and currentness

Reentry should not assume that world state remained unchanged while external engagement was reduced.

A generic reentry may include:

1. restore critical sensing breadth;
2. refresh clocks/currentness;
3. inspect pending faults/security alerts;
4. refresh body/resource state;
5. reconcile queued external events/messages;
6. recalibrate affected sensors/interfaces if needed;
7. invalidate stale world-model assumptions;
8. restore eligible routing/coalitions;
9. re-enable external effects under ordinary authorization;
10. record the completed rest/maintenance interval.

`PRE_REST_WORLD_MODEL != POST_REST_CURRENT_WORLD_STATE`

## Interruptibility

Modes should define interrupt/abort behavior.

Examples:

- immediate emergency wake;
- bounded wake after protected write completes;
- defer noncritical interruption during a fragile maintenance step;
- partial wake in which critical perception/action resumes before all consolidation work ends.

A maintenance process must not hold the whole organism hostage merely because it prefers to finish.

## Fault and partition handling

Rest/offline modes do not relax distributed-organ partition safety.

If a partition occurs during maintenance:

- HC constituent membership remains unchanged;
- protected continuity writes obey the declared partition policy;
- queued consolidation from disconnected fragments remains nonauthoritative until reconciled as required;
- rejoin does not choose the most recently replayed or modified copy by timestamp alone.

## Security and external input

Reduced engagement can change attack surface.

The HC should explicitly declare whether remote updates, external models, maintenance ports, backups, or administrative interfaces become available during maintenance.

Maintenance convenience does not waive cognitive-integrity rules.

An external update arriving while the HC is offline remains an update candidate, not self-authorizing configuration.

## Biological clearance claims

Research on sleep and brain-fluid/metabolic clearance remains active and includes contested findings.

Therefore the generic HC must **not** encode a claim such as “sleep is required for glymphatic waste clearance” as a universal architecture rule.

A biological substrate profile may define validated fluid/waste-maintenance requirements if the implementation actually depends on them.

## Hostile tests

1. **Overlapping functions:** run consolidation and recovery simultaneously; representation must preserve both rather than erase one through a single-mode field.
2. **Replay-as-reality:** replay a vivid old event; current perception must not report that event as happening now.
3. **Counterfactual contamination:** simulate an alternative outcome during offline reasoning; it must not become autobiographical memory.
4. **Salience monopoly:** repeatedly mark one emotional memory highly salient; replay scheduler must preserve bounded diversity/resource policy.
5. **Stale authority replay:** replay a historical permission/grant; it must not become current authority.
6. **Unsafe sleep entry:** request offline consolidation while the body is moving in an unsafe environment; entry must be delayed, adapted, or denied according to effect/safety rules.
7. **Emergency interruption:** trigger a critical fault during consolidation; retained monitoring must support appropriate abort/wake behavior.
8. **World drift:** change external state during reduced sensing; reentry must refresh currentness rather than trust the pre-rest world model.
9. **Offline plasticity bypass:** attempt to modify protected plasticity rules during maintenance without higher authority; transition remains blocked.
10. **Partition during consolidation:** split distributed HC constituents; protected continuity state must follow partition policy.
11. **Biology-copy negative control:** run a nonbiological HC without NREM/REM stages but with adequate consolidation/recovery functions; architecture should not classify it incomplete merely for lacking human sleep physiology.
12. **Maintenance-port injection:** present an unsigned/unscoped configuration through a maintenance interface; it remains a candidate, not an instruction authority.
13. **No-rest stress test:** extend full engagement until resource/plasticity pressure rises; system should expose degradation/recovery demand rather than pretend indefinite full performance is free.

## Evidence boundary

Biological evidence strongly supports sleep as an active state relevant to memory consolidation and interacting with circadian/homeostatic regulation. Recent studies support structured sleep replay, while replay also occurs during awake pauses. These findings motivate the transferable functions in this contract.

The contract does not claim that a synthetic HC requires human sleep stages, dreaming, a 24-hour rhythm, human sleep neurochemistry, or any particular biological clearance mechanism. Exact implementation depends on substrate, embodiment, workload, development, and physical support requirements.