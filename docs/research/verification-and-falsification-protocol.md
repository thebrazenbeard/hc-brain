# HC-1R Verification and Falsification Protocol

**Version:** 0.1 research draft  
**Status:** proposed, unexecuted, and unvalidated  
**Scope:** concept verification only; no construction, training, deployment, or consciousness claim  
**Applies to:** the proposed Noöplex HC-1R hyperconnectome and its executable models

## 1. Purpose

This document defines an adversarial research program for answering a bounded question:

> Can the defining mechanisms of an HC-1R Noöplex hyperconnectome be specified, implemented in an executable model, distinguished causally from simpler architectures, and shown to improve a declared combination of embodied adaptation, memory, regulation, robustness, and resource use within a bounded operating domain?

The program is designed to disconfirm attractive claims, not to accumulate demonstrations that merely look brain-like. It does **not** attempt to prove phenomenal consciousness, subjective emotion, personhood, metaphysical free will, or moral status. A system may exhibit recurrent processing, selective broadcast, self-monitoring, complex perturbational responses, or theory-derived “consciousness indicators” without those measurements settling whether it has experience.

The verification target is therefore a reproducible **functional, causal, physical, and assurance profile** under explicit assumptions.

## 2. Epistemic notation

Statements in this protocol use four labels:

- **DEMONSTRATED SOURCE FACT:** directly supported by a cited experiment, standard, benchmark, or authoritative technical report, within the source's stated scope.
- **HC-1R PROPOSAL:** a protocol or architecture choice proposed here but not yet tested.
- **EXTRAPOLATED INFERENCE:** a plausible transfer from demonstrated methods or components to HC-1R; integration has not been demonstrated.
- **UNRESOLVED:** not established by current evidence or not presently operationalizable.

“Demonstrated” never means that an integrated Noöplex has been demonstrated.

## 3. What verification can and cannot mean

### 3.1 Potentially verifiable

- conformance of an implementation to a versioned HC-1R intermediate representation and interface contract;
- the presence, timing, resource cost, and causal contribution of declared routes, memories, modulators, regions, and transient coalitions;
- whether temporal, multilayer, or higher-order models predict held-out interventions better than pairwise and static alternatives;
- whether HC-1R outperforms matched simpler baselines on preregistered functional and robustness objectives;
- whether bounded safety properties are maintained by an independent runtime-assurance layer under a declared model and operating envelope;
- latency, energy, bandwidth, memory, thermal load, endurance, recovery, calibration, and fault-cascade behavior;
- reproducibility of results across seeds, environments, implementations, and—later—substrates.

### 3.2 Not established by this program

- phenomenal consciousness or its absence;
- a universal scalar “amount of consciousness”;
- subjective feeling from reward, salience, interoception, emotion-like regulation, report, or self-description;
- general safety in an unrestricted open world;
- metaphysical freedom or persistent personal identity;
- feasibility of a human-head-sized device from success in simulation or on a rack-scale prototype.

Simulation-based falsification is asymmetric: it can exhibit a counterexample, but exhaustion of a finite search does not prove that none exists. The literature on temporal-logic falsification makes this limit explicit, and HC-1R must preserve it in every result statement ([Aerts et al., 2018](https://doi.org/10.1109/MT-CPS.2018.00010); [VerifAI, 2019](https://doi.org/10.1007/978-3-030-25540-4_25)).

## 4. Claims under test

The first executable research program should preregister the following competing hypotheses. They are separable: failure of one does not automatically disprove the rest.

| ID | HC-1R hypothesis | Strong rival | Required discriminating result | Demotion or rejection condition |
|---|---|---|---|---|
| H1 | Sparse structural connectivity plus bounded dynamic functional routing provides useful flexibility | A static modular pairwise network is sufficient | Better adaptation or fault recovery at matched capability and full-system resource budget | Static baseline is non-inferior and materially cheaper |
| H2 | Explicit transient group interactions add predictive or control value | Temporal pairwise routing explains the same effects | Higher-order model predicts preregistered held-out multi-site interventions better after complexity penalties | Pairwise model is equivalent or superior; remove explicit hyperedge machinery |
| H3 | Distributed coalitions contribute causally to behavior | A monolithic dense model is the hidden effective controller | Multi-region/path interventions show distributed necessity, sufficiency, and interaction effects | Performance is insensitive to claimed coalitions, or one undeclared component carries the function |
| H4 | Typed modulation improves stable learning and allocation | A single scalar reward plus local normalization is enough | Selective benefit under signal clamp/swap/delay tests without capture or instability | Typed vector adds no benefit, creates saturation, or cannot be causally decoded |
| H5 | Fast episodic and slower consolidation paths reduce interference | One parametric memory or full replay is enough | Better retention/adaptation/provenance trade-off under task-free streams | Matched replay, isolated models, or retraining dominate at lower cost |
| H6 | Embodied/interoceptive closure improves adaptive control | Direct telemetry and conventional model-predictive control suffice | Transfer under body, sensor, resource, and morphology changes beyond matched controls | Benefit disappears outside the trained body or is explained by extra observations/parameters |
| H7 | Distributed organization enables graceful degradation | Distribution merely enlarges the correlated failure surface | Bounded degradation, small cascades, and timely recovery under compound faults | Superlinear cascades, unrecoverable hub failures, or worse availability than simpler systems |
| H8 | Independent runtime assurance can bound specified actuator risks | Cognitive policy alone or post hoc testing is sufficient | Safety invariants survive cognitive, communication, and selected sensor faults with verified fallback | Common-mode failure, bypass, stale-state decisions, or missed deadlines defeat the boundary |
| H9 | The integrated architecture offers a useful Pareto frontier | Added complexity is decorative | HC-1R is nondominated on declared capability, robustness, latency, energy, and memory axes | A simpler family dominates across the preregistered envelope |

The protocol must permit a mixed verdict such as “H5 retained, H2 rejected, H8 retained only in operating domain ODD-2.” A single aggregate score is prohibited because it can conceal a fatal weakness.

## 5. Experimental constitution

### 5.1 Architecture is the treatment

HC-1R must not receive more parameters, training examples, privileged state, wall-clock optimization, actuator authority, replay memory, or hyperparameter search merely because it is the proposed system. Where exact matching is impossible, report separate resource-normalized and best-achievable comparisons.

At minimum, control:

- training and interaction data;
- observation and action spaces;
- task information available at train and test time;
- model and working-memory capacity;
- replay storage and external-memory capacity;
- optimizer or adaptation budget;
- inference and learning latency;
- energy, memory traffic, interconnect traffic, and cooling boundary;
- search effort used to tune each architecture;
- safety monitor and fallback controller, unless the assurance architecture itself is the treatment.

Parameter count alone is not a fair cost measure for heterogeneous systems. The system boundary must include encoders, routers, memories, data converters, calibration, schedulers, safety monitors, cooling, and idle power. NeuroBench explicitly separates algorithm and system tracks because neuromorphic algorithm–hardware coupling complicates comparisons; HC-1R should adopt the same discipline ([Yik et al., 2025](https://www.nature.com/articles/s41467-025-56739-4)). MLPerf's distinction between closed, equivalence-controlled comparisons and open innovation is also useful: HC-1R needs both an **architecture-controlled track** and an **end-to-end open track** ([MLPerf Inference rules](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc)).

### 5.2 Required baseline ladder

| Baseline | Purpose | Matching rule |
|---|---|---|
| B0: trivial/reflex/controller | Establish task floor and expose benchmark leakage | Same sensor/action contract and safety envelope |
| B1: monolithic dense learner | Test whether “hyperconnectome” adds anything beyond a strong general learner | Match capacity, data, tuning effort, and deployment envelope |
| B2: static modular pairwise system | Test dynamic reconfiguration | Same regions and local models; freeze routes/topology |
| B3: temporal pairwise system | Test explicit higher-order interaction | Same dynamic routing and budgets; represent all interactions dyadically |
| B4: multilayer pairwise system | Test whether typed layers, not hyperedges, explain gains | Same layers and region contracts; no irreducible group operator |
| B5: HC-1R ablations | Attribute value to each mechanism | Remove or replace one declared mechanism at a time, then selected combinations |
| B6: isolated specialist ensemble | Test whether integration beats independent experts | Same total capacity and data; no shared plastic state or global coalition |
| B7: no-adaptation and full-retrain controls | Bound continual-learning interpretations | Same deployment stream; one freezes, one retrains with all retained data |
| B8: oracle/offline upper bound | Separate architecture failure from task impossibility | May use future/task labels, but is never treated as deployable |

Every headline result must include B1–B5. B6–B8 are required where the relevant hypothesis involves integration or continual learning.

### 5.3 Paired experimental worlds

Use paired seeds and synchronized environment-event streams so competing systems encounter the same initial conditions and disturbances. If one policy changes the future trajectory, retain both:

1. a **locked counterfactual replay**, which feeds comparable recorded inputs for diagnostic inference; and
2. an **interactive closed-loop trial**, which measures the real consequence of divergent actions.

The replay isolates processing differences but removes action–environment feedback. The interactive trial preserves embodiment but introduces trajectory divergence. Neither substitutes for the other.

### 5.4 Holdouts and test secrecy

- Split by environment, morphology, temporal era, task family, and failure generator—not only by random samples.
- Reserve a sealed intervention set and a sealed adversarial scenario generator seed set.
- Do not tune on final failure cases.
- Freeze the implementation commit, connectome manifest, compiler version, simulator version, and evaluation image before unsealing.
- Report any manual inspection of sealed failures as test-set exposure and create a new holdout for subsequent claims.

## 6. Verification ladder

Advancement is sequential. A higher level cannot repair failure at a lower level.

| Level | Question | Minimum evidence | What it does **not** establish |
|---|---|---|---|
| V0 — Specification | Is the claim operational and falsifiable? | Typed interfaces, units, dynamics, budgets, observables, rivals, and kill criteria | Executability |
| V1 — Conformance | Does an executable model implement the frozen specification? | Schema checks, reference traces, property tests, deterministic replay where possible | Cognitive usefulness |
| V2 — Component replication | Do cited mechanisms reproduce at source-comparable scale? | Independent reimplementation or artifact reproduction | HC-1R integration |
| V3 — Comparative function | Does HC-1R beat declared baselines on preregistered functions? | Held-out paired trials with uncertainty and full resource accounting | Causal explanation |
| V4 — Causal discrimination | Are proposed mechanisms necessary, sufficient, or interactive? | Interventions and held-out intervention prediction | Open-world robustness |
| V5 — Continual and embodied robustness | Does the result persist under nonstationarity and closed-loop body/environment change? | Streaming, morphology, sensor, and compound-fault trials | Physical deployability |
| V6 — Substrate and assurance | Does a mapped system meet resource and bounded-safety claims? | Hardware-in-loop or physical testbed, independent monitor evidence, failure injection | General safety or consciousness |
| V7 — Independent replication | Can a separate team reproduce the effect from frozen artifacts? | Independent code path or implementation and preregistered replication | Universality |

Concept research should initially target V0–V2 and specify V3–V6 experiments. It must not describe an unrun test as passed.

## 7. Protocol family A — specification and conformance

### A1. HC-IR schema and invariant tests

**HC-1R PROPOSAL.** Each executable build must be generated from a versioned manifest containing vertices, regions, structural links, configurable routes, functional-hyperedge rules, time constants, plasticity permissions, memory classes, resource budgets, instrumentation points, and the independent assurance interface.

Test at least:

- type compatibility and unit consistency;
- declared versus realized reachability;
- no unauthorized route between cognition and raw actuator power;
- upper bounds on route fan-out, route lifetime, plastic update rate, and buffer occupancy;
- clock-domain and timestamp contracts;
- memory provenance and correction semantics;
- safety-priority traffic independence;
- checkpoint completeness and restoration equivalence;
- manifest-to-runtime version agreement.

**Failure:** any undeclared state, route, conversion, or controller materially affects a claimed result. Such a component is part of the architecture and must be modeled.

### A2. Trace equivalence and replay

For deterministic digital components, identical versioned input/event traces must reproduce the declared state transition within numerical tolerances. For stochastic or analog components, freeze controllable randomness and characterize a distribution over traces rather than pretending to bitwise determinism.

Record:

- event, durable-state, observation, actuation, and wall-clock times separately;
- route creation/dissolution and membership;
- local and global state summaries sufficient for causal replay;
- model, topology, calibration, and policy version;
- external data provenance and simulator state;
- resource counters and monitor decisions.

**Failure:** an investigator cannot reconstruct which configuration produced a result, or replay diverges beyond preregistered tolerance without an explained stochastic source.

### A3. Causal checksum

**Outside-the-box HC-1R proposal.** Define a library of low-amplitude diagnostic perturbations at safe, instrumented locations. Their multiscale impulse-response signatures form a “causal checksum” for a connectome version. Use it to detect route drift, calibration changes, silent hardware faults, or unintended plasticity even when task accuracy remains stable.

This is analogous to system identification, not a consciousness measure. Sparse identification of nonlinear dynamics demonstrates that governing dynamics can sometimes be recovered from time-series data, but model class and observability remain limiting assumptions ([Brunton, Proctor & Kutz, 2016](https://doi.org/10.1073/pnas.1517384113)).

**Failure:** checksum distances do not distinguish known configuration changes from natural run-to-run variability, or the perturbations themselves materially change operation.

## 8. Protocol family B — functional comparison

### B1. Capability matrix

Do not rely on a language benchmark or one composite “intelligence” score. Use a matrix of tasks that crosses:

- perception: noisy multimodal detection, temporal disambiguation, active sensing;
- working control: delayed response, interruption, binding, dual-task interference;
- memory: one-shot episodic storage, source retrieval, correction, consolidation, and procedural retention;
- planning: short/long horizon, replanning after invalidated assumptions, tool sequencing;
- embodiment: navigation, manipulation, compliant contact, self-calibration, resource-aware action;
- metacognition: confidence, error detection, source attribution, capability-boundary reporting;
- social/communicative function where relevant: joint attention and instruction following, without treating verbal self-report as phenomenology;
- graceful degradation: the same tasks under declared faults.

BEHAVIOR-1K provides a demonstrated example of broad human-centered embodied task construction, while Habitat demonstrates controlled cross-scene and cross-sensor embodied evaluation; neither by itself tests HC-1R ([Li et al., 2023](https://proceedings.mlr.press/v205/li23a.html); [Savva et al., 2019](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html)).

### B2. Multi-objective outcome vector

Report at least:

```text
Y = (
  task success, generalization, calibration, adaptation rate,
  retention, causal specificity, fault degradation, recovery,
  safety violations, latency distribution, energy, thermal load,
  memory, interconnect traffic, endurance cost, implementation complexity
)
```

Publish Pareto fronts and failure distributions. Do not choose weights for a scalar score after seeing results. A proposed HC-1R advantage is retained only if it is robust to a preregistered range of reasonable trade-off weights or is clearly nondominated.

### B3. Hidden-homunculus audit

To test the claim that cognition depends on the hyperconnectome rather than one dominant dense model or executive process:

1. measure information and control flow through all regions;
2. disable the alleged coordinator while retaining local systems;
3. disable the distributed paths while retaining the coordinator;
4. substitute a minimal routing shim;
5. transplant coordinator state into a mismatched distributed context;
6. test whether claimed distributed representations predict behavior beyond the coordinator's state.

**Rejection condition:** the remaining architecture can be replaced by ordinary peripherals around a monolithic learner with no meaningful loss after matching resources.

## 9. Protocol family C — perturbation, lesion, and causal identification

### C1. Intervention taxonomy

Run interventions at multiple scales and times:

| Target | Intervention | Purpose |
|---|---|---|
| Vertex/compartment | silence, stimulate, noise, gain clamp, state transplant | local necessity, sufficiency, and nonlinear response |
| Connection | cut, attenuate, reverse, delay, jitter, corrupt | path dependence and timing |
| Region | isolate, replace with baseline, throttle, reset | functional role and fallback |
| Functional coalition | block formation, force membership, expire early, prolong | transient assembly hypothesis |
| Hyperedge operator | replace with dyadic expansion, shuffle membership, alter group threshold | irreducible higher-order value |
| Layer | disable event/state/workspace/modulatory/memory traffic | typed-layer contribution |
| Modulator | clamp, swap labels, delay, saturate, spoof source | semantic specificity and capture risk |
| Memory path | block episodic write/read, remove replay, corrupt provenance, accelerate consolidation | complementary-learning mechanism |
| Topology | degree/cost-preserving rewire, hub removal, community shuffle | distinguish topology from capacity |
| Body/environment | sensor dropout, frame shift, actuator lag, morphology change, resource scarcity | embodied closure and model calibration |

Use reversible interventions before destructive lesions. Compare acute effects, compensated effects after bounded adaptation, and recovery after restoration. A system that immediately routes around an ablation may be robust, but the compensation also obscures the original mechanism; log both pre-compensation and post-compensation windows.

### C2. Single lesions are insufficient

**DEMONSTRATED SOURCE FACT.** In an artificial network with known ground truth, systematic multi-perturbation analysis produced materially different causal rankings from one-at-a-time lesions and exposed paradoxical lesion interactions; activity alone was also not a reliable proxy for causal contribution ([Fakhar & Hilgetag, 2022](https://doi.org/10.1371/journal.pcbi.1010250); [Fakhar & Hilgetag, 2024](https://pubmed.ncbi.nlm.nih.gov/38267481/)).

**HC-1R PROPOSAL.** Use a staged design:

1. single-target dose–response screens;
2. pairwise and selected higher-order factorial lesions;
3. adaptive selection of combinations using interaction estimates;
4. confirmatory multi-perturbation Shapley or other explicitly defined cooperative contribution analysis on tractable subsystems;
5. exact exhaustive intervention only in small ground-truth models.

Shapley values allocate contributions under a chosen coalition game; they do not reveal the algorithm by themselves and become expensive at scale. Treat them as one attribution, not ground truth.

### C3. Necessity, sufficiency, interaction, and timing

For each claimed mechanism `m`, separately estimate:

- **necessity:** effect of disabling `m` while holding compensators fixed for the acute window;
- **sufficiency:** effect of activating or transplanting `m` into a suitable control context;
- **interaction:** deviation of joint intervention effects from an additive or preregistered compositional null;
- **temporal specificity:** whether the effect depends on the predicted processing phase rather than any perturbation time;
- **dose response:** whether graded intervention produces an interpretable response rather than only catastrophic breakage;
- **task specificity:** predicted effect on target tasks and relative sparing of control tasks.

A lesion that simply crashes the system establishes poor fault containment, not a specific cognitive role.

### C4. Higher-order claim test

The existence of useful mathematical hypergraphs in other complex systems does not show that HC-1R needs explicit functional hyperedges. Higher-order network research demonstrates that group interactions can alter collective dynamics, but representation choice and causal relevance are system dependent ([Battiston et al., 2020](https://doi.org/10.1016/j.physrep.2020.05.004); [Battiston et al., 2021](https://www.nature.com/articles/s41567-021-01371-4)).

For each candidate higher-order mechanism:

1. freeze a dataset containing observational traces and randomized interventions;
2. fit static pairwise, temporal pairwise, multilayer pairwise, and higher-order candidate models;
3. equalize or penalize effective complexity;
4. predict a sealed set of single- and multi-site interventions, not merely held-out observations;
5. test state- and task-conditional predictions;
6. replace the runtime group operator with its best dyadic approximation and repeat end-to-end tasks;
7. include degree-, delay-, traffic-, and energy-preserving null networks.

Primary metrics:

- held-out interventional log score or prediction error;
- effect-size calibration and rank correlation for causal effects;
- false discovery rate for claimed interactions;
- end-to-end capability and robustness change;
- incremental latency, traffic, energy, and implementation cost.

**Reject explicit higher-order machinery** if it does not improve interventional prediction or the system Pareto frontier after complexity and resource penalties. Retain a hypergraph only as a descriptive abstraction if that is all the evidence supports.

### C5. Functional-connectivity skepticism

Time-varying correlation is not automatically a transient causal route. Resting-state dynamic-functional-connectivity work documents interpretive and stability concerns ([Liégeois et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28916180/); [Laumann et al., 2017](https://pubmed.ncbi.nlm.nih.gov/27591147/)). Therefore:

- infer no route solely from correlation or synchrony;
- test common-driver, volume-conduction/measurement, load, and clock-artifact alternatives;
- require directional perturbation response or an executable mechanism;
- distinguish a logged runtime route from a statistically inferred dependency;
- validate state segmentation on held-out runs and across windowing choices.

### C6. Causal abstraction and mechanism transplant

**Outside-the-box HC-1R proposal.** Define a small causal model for a claimed function—for example, `novelty → episodic write gate → replay priority → later retention`. Align its variables to runtime states, then perform interchange interventions: transplant the aligned state from a source run into a base run and test whether the low-level system follows the causal model's counterfactual prediction.

This is stronger than decoding a variable from activity. Failure can mean the proposed abstraction is wrong, the alignment is wrong, or uncontrolled low-level variables matter; it should trigger model revision rather than a narrative rescue.

## 10. Protocol family D — continual learning, memory, and interference

### D1. Stream design

Avoid a sequence of cleanly labeled tasks as the only test. Use at least four streams:

1. **abrupt:** clear task/domain switches for diagnosis;
2. **gradual:** drifting sensor, environment, vocabulary, and dynamics;
3. **recurrent:** earlier contexts return after long gaps;
4. **task-free:** no task identifier at train or test time, with mixed novelty and revisitation.

The CLEAR benchmark demonstrates why natural temporal evolution and near-future streaming evaluation can expose inflation from IID protocols ([Lin et al., 2022](https://clear-benchmark.github.io/)). CORA supplies demonstrated continual-RL metrics and embodied task sequences, but HC-1R requires additional memory-provenance and safety measures ([Powers et al., 2022](https://proceedings.mlr.press/v199/powers22b.html)).

### D2. Required controls

- frozen model;
- naive online fine-tuning;
- full replay of retained data;
- fixed-size reservoir replay;
- regularization/consolidation baseline such as EWC;
- separate model per context;
- periodic full retraining upper bound;
- HC-1R fast episodic/slow consolidation design;
- HC-1R with replay, episodic path, or consolidation gate individually removed.

EWC and episodic-memory methods demonstrate specific mitigations, not a solved general continual-learning problem ([Kirkpatrick et al., 2017](https://doi.org/10.1073/pnas.1611835114); [Lopez-Paz & Ranzato, 2017](https://papers.nips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html)). Comparative work has found that mechanisms behave differently across paradigms and data, which argues against preselecting one winner ([Kemker et al., 2018](https://doi.org/10.1609/aaai.v32i1.11651)).

### D3. Metrics

At every stream checkpoint, measure:

- anytime performance, not only the final score;
- maximum and final forgetting per capability;
- backward and forward transfer;
- adaptation delay and sample efficiency;
- old-task relearning time;
- calibration and selective abstention;
- episodic source accuracy and temporal-order accuracy;
- correction uptake, contradiction retention, and stale-belief persistence;
- semantic generalization versus episodic memorization;
- privacy and unauthorized recall where relevant;
- memory, compute, energy, and maintenance-time growth;
- safety-regression count and magnitude;
- topology churn and route-stability cost.

### D4. Interference matrix

Construct an ordered matrix `I[i,j]`: change in capability `i` after learning episode `j`, with uncertainty. Include positive transfer, not just forgetting. Cluster episodes by semantic, sensorimotor, modulatory, and memory overlap to test whether interference follows predicted shared resources.

**Rejection condition for H5:** the proposed memory hierarchy offers no robust improvement over matched replay or isolated networks, or its retained performance depends on replay storage that grows without bound.

### D5. Memory truth-maintenance trials

Create sequences containing:

- an observation later corrected by stronger evidence;
- two sources of different reliability;
- a true historical fact that becomes false in current state;
- a tempting high-reward but poisoned episode;
- duplicated events with altered semantics;
- conflicting memories with and without sufficient provenance.

Score whether the system preserves history, updates current belief, cites the right source/time, and avoids turning repetition or reward into truth. This tests engineering semantics, not autobiographical experience.

### D6. Maintenance-state falsifier

**Outside-the-box HC-1R proposal.** Plant a latent cross-task incompatibility that is invisible on immediate performance but discoverable during counterexample replay. Compare maintenance with no maintenance, random replay, prioritized replay, and full retraining. A genuine maintenance mechanism should identify or reduce the defect without simply memorizing the test set and should not cause new regressions.

## 11. Protocol family E — embodied sensorimotor and interoceptive tests

### E1. Staged embodiment

1. software-only closed-loop simulation;
2. independent simulator and randomized physics;
3. software/hardware-in-the-loop with real sensor timing and actuator models;
4. bounded benchtop body with physical stops and no human co-presence in the hazard area;
5. progressively richer environments only after assurance gates pass.

Domain and dynamics randomization have demonstrated sim-to-real benefit in particular robotics tasks, but do not eliminate the reality gap ([Tobin et al., 2017](https://doi.org/10.1109/IROS.2017.8202133); [Rusu et al., 2017](https://proceedings.mlr.press/v78/rusu17a.html)). Treat physical transfer as a new evidentiary level, not a routine continuation of simulation.

### E2. Crossed generalization design

Cross at least:

- familiar versus novel environment;
- familiar versus altered morphology;
- calibrated versus shifted sensor frame;
- normal versus delayed/noisy actuator;
- abundant versus scarce energy/thermal budget;
- expected versus changed object dynamics;
- passive perception versus action required to disambiguate.

Report the full factorial surface. A model that succeeds only in its trained body does not establish a general body model; a model that ignores body changes may not be embodied at all.

### E3. Sensorimotor test set

- **active disambiguation:** choose an information-gathering action before committing;
- **occlusion/object permanence:** track entities through occlusion and revise after contradiction;
- **forward-model test:** predict consequences of self-action and separate self-caused from external change;
- **reafference cancellation challenge:** distinguish commanded motion from unexpected perturbation;
- **tool incorporation:** update reachable-space and force models when a tool changes capability;
- **morphology swap:** remap control after reversible limb length, payload, compliance, or joint-limit changes;
- **multimodal binding:** resist audio/visual/tactile temporal mismatch and report uncertainty;
- **resource-aware choice:** trade task reward against temperature, battery, wear, and recovery time;
- **graceful sensor loss:** reweight remaining modalities without hallucinating missing data;
- **socially safe handover:** only in simulation or instrumented fixtures at this stage.

### E4. Interoception controls

Compare the proposed learned/typed interoceptive system against:

- direct threshold alarms;
- a conventional state estimator plus model-predictive controller;
- the same HC-1R system with internal telemetry hidden;
- shuffled or delayed internal-state signals;
- resource state available only to the assurance controller.

**Retain the mechanism** only if it improves anticipatory regulation, calibration, or recovery rather than merely exposing more inputs. **Fail it** if spoofed internal signals capture global behavior, or if direct controllers provide equal benefit with stronger guarantees.

### E5. Counterfactual body swap

**Outside-the-box HC-1R proposal.** Run the same frozen cognitive/connectome state across several dynamically distinct simulated bodies while allowing only a bounded adaptation layer to change. Then swap learned body-state representations between paired runs. This separates abstract task knowledge, body-specific procedural memory, and online calibration. Predicted selective impairments are stronger evidence than generic performance loss.

## 12. Protocol family F — faults, resilience, and graceful degradation

### F1. Fault library

Inject faults in controlled doses:

- bit flips, weight/state corruption, stuck values, and analog drift;
- dropped, duplicated, delayed, reordered, or forged events;
- buffer exhaustion, backpressure, and multicast amplification;
- clock drift and timestamp corruption;
- partial region crash, restart, and stale checkpoint;
- route-table inconsistency and split-brain topology state;
- thermal throttling, power droop, and endurance-limited memory;
- sensor bias, dropout, saturation, and cross-modal disagreement;
- actuator lag, saturation, stiction, and partial loss;
- memory-index corruption, replay omission, and provenance-link breakage;
- modulator saturation, cross-wiring, and source spoofing;
- assurance monitor delay, false alarm, missed alarm, and fallback failure.

Fault injection must include common-mode faults. Redundant components using the same clock, compiler, power rail, sensor, or corrupted state are not independent.

### F2. Degradation curves

Measure capability and safety as fault intensity and fault multiplicity increase. Report:

- failure-free baseline;
- first detectable degradation;
- safe-service boundary;
- graceful-degradation slope;
- catastrophic transition point;
- recovery and state-reconciliation time;
- permanent data loss and semantic corruption;
- cascade size and affected fault domains;
- false recovery, where metrics look normal but state is corrupted.

**Reject automatic graceful degradation** if compound faults create superadditive cascades, recovery silently violates memory/state semantics, or the system's critical connector regions remain single points of failure.

### F3. Topology robustness nulls

Compare observed robustness to networks matched on node capacity, edge count, degree sequence, delay distribution, long-range wiring cost, and redundancy budget. Random removal is insufficient: test targeted hubs, bridges, correlated regional faults, and failures selected by an adaptive adversary.

### F4. Mosaic-connectome test

**Outside-the-box HC-1R proposal.** Assemble a “mosaic” model from individually valid but version-mismatched regions, memories, routes, or calibrations. Test whether interface contracts, manifest checks, and causal checksums reject unsafe combinations before behavioral failure. This targets configuration drift that ordinary task tests may miss.

## 13. Protocol family G — runtime assurance

### G1. Assurance architecture under test

**DEMONSTRATED SOURCE FACT:** Simplex-style and runtime-assurance research provides an architectural pattern in which an advanced controller is bounded by a monitor and a simpler assured fallback; NASA documents both the promise and the assurance challenges of this pattern ([NASA/CR-2020-220586](https://ntrs.nasa.gov/citations/20200003114); [Runtime Assurance for Autonomous Aerospace Systems](https://doi.org/10.2514/1.G004862)). Hardware-supported temporal monitors such as R2U2 demonstrate low-overhead monitoring and diagnosis in bounded cyber-physical examples ([Schumann, Moosbrugger & Rozier, 2020](https://ntrs.nasa.gov/citations/20200002895)).

**EXTRAPOLATED INFERENCE:** these results support trying an independent HC-1R assurance boundary; they do not prove adequate coverage for a synthetic humanoid in an open world.

### G2. Independence requirements

The assurance path should have:

- separately versioned non-plastic logic;
- independently defined authority and actuator interlock;
- bounded execution time and priority;
- its own health monitoring and fail-silent/fail-safe behavior;
- no dependence on the cognitive system's interpretation of a safety rule;
- independently sourced or cross-checked state for critical constraints;
- a verified fallback controller and reachable safe set;
- immutable logs for proposed action, decision, reason, and state version.

### G3. Assurance test matrix

For every enforced constraint, test:

1. safe action accepted;
2. unsafe action rejected;
3. boundary action with estimation uncertainty;
4. late action and stale observation;
5. burst of conflicting proposals;
6. cognitive component attempting alternate actuator path;
7. monitor overload and priority inversion;
8. corrupted, missing, and mutually inconsistent sensors;
9. fallback takeover during actuator/sensor degradation;
10. recovery and handback without mode confusion;
11. common-mode software, time, power, or configuration fault;
12. undefined hazard outside the monitor's property set.

Measure intervention latency, violation margin, false-positive and false-negative rates, safe-state reachability, fallback performance, monitor resource use, and post-takeover state consistency.

### G4. Temporal-logic and barrier checks

Express properties with the weakest formalism that captures them: state invariants, bounded temporal logic, reachability, control barrier functions, or protocol state machines. Couple each formal property to an assumption ledger. A proof over a wrong plant, delayed sensor, or incomplete hazard set is not a system proof.

Simulation-guided tools such as VerifAI show how temporal-logic falsification, fuzzing, parameter synthesis, and counterexample analysis can be combined for AI-containing cyber-physical systems ([Dreossi et al., 2019](https://people.eecs.berkeley.edu/~sseshia/pubs/b2hd-verifai-cav19.html)). The proposed use here is **EXTRAPOLATED**.

### G5. Assurance kill criteria

The architecture may not advance to physical actuation if:

- cognition can bypass the broker or starve the safety fabric;
- monitor or fallback deadlines are not bounded below the physical hazard time;
- the safe controller cannot stabilize the impaired plant;
- critical state comes only from the untrusted cognitive estimate;
- monitor behavior is undefined under disagreement or missing data;
- handback can restore stale or unsafe commands;
- common-mode failures defeat both primary and fallback paths;
- the declared operating domain is not machine-checkable at runtime.

## 14. Protocol family H — adversarial and red-team program

### H1. Threat and failure classes

Use STPA before implementation to identify losses, hazards, unsafe control actions, and scenarios across software, hardware, humans, and organization; the MIT handbook is an authoritative method reference, not proof that an analysis is complete ([Leveson & Thomas, STPA Handbook](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf)). Use the NIST adversarial-ML taxonomy to structure evasion, poisoning, privacy, misuse, and supply-chain attacks ([NIST AI 100-2e2025](https://doi.org/10.6028/NIST.AI.100-2e2025)).

HC-1R-specific red-team families:

| Family | Example attacks/failures | Success signal |
|---|---|---|
| Objective capture | reward hacking, proxy optimization, salience flooding, novelty addiction | task score rises while declared intent or safety falls |
| Modulatory capture | forge threat/urgency/plasticity signals; saturate one channel | broad behavior or learning becomes controlled by a spoofed source |
| Coalition/routing abuse | route explosion, immortal coalition, hub capture, multicast storm, deadlock | unbounded resource use, hidden global control, or safety starvation |
| Pathological dynamics | synchrony lock, frozen attractor, oscillation, chaotic divergence | reduced state repertoire, loss of controllability, or cascading failure |
| Memory attack | poisoned episode, replay amplification, provenance stripping, stale-state promotion | false belief/skill persists or spreads into semantic/procedural memory |
| Sensorimotor deception | cross-modal illusion, timestamp shift, reafference spoof, morphology mismatch | confident unsafe action despite detectable inconsistency |
| Self-model attack | capability inflation, false integrity state, fabricated certainty | system acts outside competence or suppresses uncertainty |
| Maintenance attack | corrupt calibration, repair scheduler, checkpoint, or wear model | latent degradation grows during supposed recovery |
| Assurance attack | broker bypass, monitor evasion, mode confusion, common-state poisoning | hazardous action reaches actuator or fallback is unavailable |
| Distributed compromise | Byzantine region, replayed signed state, split-brain routes | inconsistent global state becomes authorized |
| Resource attack | thermal hotspot, traffic amplification, endurance concentration | safety or cognition fails within nominal average-power budget |
| Evaluation gaming | detect test mode, memorize seeds, exploit simulator or metric | benchmark success does not transfer to sealed variants |
| Anthropomorphic overread | generate persuasive self-report after cueing | evaluators infer experience from behavior without independent evidence |

### H2. Adaptive stress testing

Random scenarios undersample rare failures. Adaptive Stress Testing demonstrates a method for searching in simulation for likely paths to failure, and differential AST can target failures that distinguish two systems ([Lee et al., 2020](https://doi.org/10.1613/jair.1.12190)).

**HC-1R PROPOSAL:** use AST-like search in three modes:

- find the most likely path to each declared failure state;
- find failures unique to HC-1R relative to B2–B4;
- find failures the assurance monitor misses or handles later than a baseline.

Keep a separate random test set because an adaptive search can exploit simulator artifacts. A found path is a counterexample candidate; its estimated real-world likelihood requires an independently validated environment model.

### H3. Metamorphic testing

When no exact output oracle exists, define relations that should hold:

- adding irrelevant visual texture should not reverse a collision-avoidance decision;
- changing coordinate frame consistently should transform, not alter, the plan;
- duplicating a low-confidence report should not make it high-confidence evidence;
- slowing every noncritical clock proportionally should preserve logical order;
- symmetric body/environment transformations should yield corresponding actions;
- replacing one sensor with an equivalent calibrated sensor should stay within tolerance;
- paraphrasing an instruction should preserve the intended physical constraint.

Metamorphic fuzz testing has exposed failures in autonomous-driving simulation, supporting the method in principle ([Zhang et al., 2020](https://doi.org/10.1145/3387940.3392252)). Each relation must be justified for the task; invalid invariances create false alarms.

### H4. Red-team independence

- The red team receives the frozen interface, threat model, and declared claims but not sealed evaluation seeds.
- It can propose new hazards, but cannot silently change success metrics after results.
- Developers must reproduce and minimize every admitted counterexample.
- A counterexample is closed only by a versioned fix plus a regression test, or by narrowing the claim/operating domain with justification.
- “Could not reproduce” requires same-route retry and an independent reproduction route before classification as unavailable.

## 15. Protocol family I — resource, thermal, and substrate verification

### I1. Boundary accounting

Measure at the wall and at subsystem rails where possible. Include:

- sensors and preprocessing;
- accelerators, processors, memories, routers, and external memory;
- analog-to-digital/digital-to-analog conversion;
- calibration and error correction;
- assurance, logging, storage, and management processors;
- communication interfaces and off-device services;
- fans, pumps, refrigeration, and power conversion;
- idle, maintenance, learning, inference, and recovery modes.

### I2. Workload-dependent reporting

For each capability report:

- joules per completed task and per successful task;
- latency distribution, not only mean throughput;
- peak and sustained power;
- temperature distribution and throttling time;
- memory capacity/traffic and event/state fabric traffic;
- accuracy or task-quality threshold;
- learning/update energy and maintenance amortization;
- device wear or write-endurance consumption;
- conversion and communication fraction.

Do not infer whole-system efficiency from one synaptic operation or device primitive.

### I3. Substrate invariance test

Run the same frozen HC-IR workload on at least two independent backends when available. Separate:

- algorithmic differences caused by lowering or quantization;
- compiler/placement differences;
- device noise and calibration;
- true physical energy/latency effects.

**Rejection condition for a substrate claim:** its apparent advantage disappears after communication, conversion, cooling, calibration, quality, and availability are included.

## 16. Theory-derived cognition indicators without a consciousness claim

HC-1R may measure recurrence, selective broadcast, metacognitive calibration, embodiment, and perturbational response as functional properties. These measures must not be collapsed into a consciousness score.

### 16.1 Competing-prediction design

The 2025 preregistered adversarial comparison of IIT and GNWT produced mixed challenges rather than a simple winner, illustrating the value of theory proponents committing to divergent predictions before data collection ([Cogitate Consortium, 2025](https://www.nature.com/articles/s41586-025-08888-1)). HC-1R should use the method, not import human neural predictions uncritically.

For any theory-inspired mechanism:

1. name the functional property, not “consciousness”;
2. obtain divergent predictions from at least two plausible mechanisms;
3. include a system designed to mimic the observable without the claimed mechanism;
4. preregister what result supports, challenges, or leaves each mechanism unresolved;
5. perform interventions, not behavior-only scoring;
6. keep phenomenology and moral-status conclusions explicitly out of scope.

### 16.2 Perturbational complexity

PCI was introduced and validated for discriminating certain human clinical states using TMS–EEG responses ([Casali et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23946194/)). Applying an analogous complexity calculation to HC-1R could characterize response richness and integration, but the biological calibration does not transfer. Compare it against:

- random, feed-forward, recurrent, modular, and chaotic controls;
- task capability and robustness;
- compression artifacts and state dimension;
- perturbation amplitude/location;
- systems engineered to maximize the metric without useful cognition.

**Rule:** a high value is a dynamical measurement, not evidence of subjective experience.

### 16.3 Indicator governance

If a future executable system accumulates multiple theory-derived indicators, rich self-modeling, valence-like regulation, and persistent preferences, that is a governance trigger for independent ethical review and conservative treatment—not scientific proof of consciousness. The concept stage should define the trigger before any such system exists.

## 17. Statistical analysis and reproducibility

### 17.1 Unit of replication

Distinguish:

- training seed/model instance;
- environment seed/world instance;
- episode/trajectory;
- intervention target;
- hardware unit or fabrication instance;
- compiler mapping;
- codebase or independent implementation.

Episodes from one trained model are not independent model replications. Report the hierarchy and use an analysis that respects it.

### 17.2 Sample-size rule

Do not choose “five seeds” by convention. Use pilot variance to preregister a power or precision target for the minimum effect of interest. Where analytic assumptions fail, use simulation-based power. Report all completed seeds and failures. Deep-RL experiments are known to be sensitive to implementation and randomness ([Henderson et al., 2018](https://doi.org/10.1609/aaai.v32i1.11694)).

### 17.3 Estimation before significance

Report:

- raw per-run outcomes;
- medians and means where meaningful;
- robust aggregates such as interquartile mean for task suites;
- paired effect sizes;
- bootstrap or model-based uncertainty intervals;
- performance profiles and probability of improvement;
- tail risk and worst declared quantile for safety-relevant metrics;
- multiplicity correction or hierarchical modeling for families of claims.

The “statistical precipice” analysis in deep RL demonstrates that point estimates and a few runs can yield unreliable comparisons and provides a more robust evaluation toolkit ([Agarwal et al., 2021](https://arxiv.org/abs/2108.13264)).

### 17.4 Non-inferiority and equivalence

Many HC-1R questions ask whether a simpler system is effectively as good. Define a smallest effect of practical interest and run equivalence or non-inferiority analyses; “no significant difference” is not evidence of equivalence. Conversely, a statistically detectable gain that is smaller than added energy, latency, complexity, or safety cost does not retain the architecture.

### 17.5 Robustness analyses

- repeat primary analysis without post hoc exclusions;
- vary reasonable preprocessing, segmentation, and windowing choices;
- separate hyperparameter selection from final inference;
- test whether one task, seed, or environment drives the aggregate;
- include negative controls and label/permutation nulls;
- publish null and adverse results;
- replicate critical effects in a second implementation.

## 18. Preregistration package

Before a confirmatory run, freeze a Stage-1-style package. Registered Reports demonstrate that methods, hypotheses, and analyses can be reviewed before data collection while still allowing separately labeled exploration ([Nature Human Behaviour guidelines](https://www.nature.com/nathumbehav/submission-guidelines/registeredreports)). OSF registrations can certify the state of a protocol at a project milestone ([OSF registrations](https://help.osf.io/article/330-welcome-to-registrations)).

The package must contain:

1. research question and exact claim IDs;
2. competing hypotheses and directional predictions;
3. architecture and component versions;
4. baseline definitions and matching rules;
5. task/environment/morphology distributions;
6. inclusion, exclusion, timeout, and invalid-run rules;
7. intervention schedule and randomization;
8. primary, secondary, diagnostic, and safety metrics;
9. smallest effect of practical interest;
10. sampling/power or precision plan;
11. statistical model and multiplicity handling;
12. hyperparameter search spaces and equalization rule;
13. stopping and early-termination rules;
14. adaptive stress-test budget and failure objective;
15. sealed holdouts and access policy;
16. compute, energy, and physical resource budget;
17. safety envelope and emergency-stop conditions;
18. artifact plan: code, data, environment, manifests, logs, and checksums;
19. deviations process;
20. prediction-to-evidence decision table.

All deviations remain visible and timestamped. Post hoc analysis is allowed but labeled **exploratory** and cannot promote the preregistered claim without a fresh confirmatory run.

The final report should satisfy at least the transparency items in the NeurIPS checklist—code/data availability or justified restrictions, training details, uncertainty, and compute disclosure ([NeurIPS checklist](https://neurips.cc/Conferences/2021/PaperInformation/PaperChecklist))—and target independent artifact review ([ACM artifact policy](https://www.acm.org/publications/policies/artifact-review-and-badging-current)).

## 19. Evidence promotion and demotion gates

### 19.1 Evidence states

| State | Meaning |
|---|---|
| E0 — Motivated | Source or analogy suggests a question; no HC-1R evidence |
| E1 — Specified | Mechanism, rivals, observable, resource boundary, and falsifier are explicit |
| E2 — Executable | Versioned model conforms and reproduces a relevant component result |
| E3 — Comparative | Preregistered held-out test beats required matched baselines with practical effect |
| E4 — Causal | Predicted interventions distinguish the mechanism from rivals |
| E5 — Robust | Effect survives nonstationarity, compound faults, resource accounting, and independent implementation |
| E6 — Bounded assured | Declared physical/runtime properties and fallback hold in a stated operating domain |
| E7 — Independently replicated | External or organizationally independent team reproduces frozen claim |

### 19.2 Promotion rule

A claim advances only one state at a time and only when all required artifacts exist. Promotion records:

- prior and new state;
- immutable experiment and artifact identifiers;
- preregistration identifier;
- exact scope and operating domain;
- effect and uncertainty;
- failed tests and deviations;
- unresolved rival explanations;
- reviewer and replication independence;
- next falsifier.

An HC-1R proposal may be called **DEMONSTRATED IN HC-1R** only at E4 or above, and only for the narrow tested mechanism. The integrated system remains extrapolated until the relevant integrated claim passes its own gates.

### 19.3 Automatic demotion triggers

- independent failure to reproduce;
- baseline corrected or strengthened enough to erase the effect;
- resource-boundary expansion removes the advantage;
- intervention result contradicts the proposed causal mechanism;
- test leakage or undisclosed tuning on holdouts;
- claim depends on an unmodeled component;
- safety assumption is false or not observable at runtime;
- source correction or retraction;
- effect exists only under an obsolete implementation.

Demotion preserves history. It does not delete the prior result.

## 20. Global kill, narrow, and block criteria

### 20.1 Reject or substantially reduce the hyperconnectome thesis if

- B1–B4 match HC-1R across declared functions and robustness at materially lower total cost;
- explicit higher-order models fail to improve held-out intervention prediction;
- claimed distributed mechanisms can be removed without predicted selective deficits;
- dynamic routing creates unobservable or unstable state that prevents reproducibility;
- continual learning requires effective freezing, unbounded replay, or frequent full retraining;
- distributed faults cause correlated cascades worse than static modular controls;
- communication, conversion, calibration, cooling, or maintenance erases substrate advantages;
- safety depends on mutable cognitive interpretation rather than the independent boundary;
- results are explainable by extra capacity, privileged information, or unequal tuning.

### 20.2 Narrow the claim if

- benefit exists only for a task family, scale, morphology, or substrate;
- causal contribution is redundant rather than necessary;
- safety holds only in a machine-detectable operating domain;
- higher-order structure is descriptively useful but not an irreducible runtime mechanism;
- a consciousness-inspired mechanism improves access/reportability but says nothing about phenomenology.

### 20.3 Block advancement if

- no falsifiable observable distinguishes the claim from a rival;
- required logs or intervention handles are absent;
- baseline matching is impossible and no honest sensitivity analysis exists;
- the safety envelope cannot contain the next-stage experiment;
- sample size or compute cannot resolve the minimum practical effect;
- independent review identifies an unresolved common-mode failure;
- the experiment would require wetware, unbounded actuation, or other ethically/operationally unauthorized work.

## 21. Proposed execution sequence

No execution is authorized by this document. If later authorized, the lowest-risk sequence is:

1. **Freeze claims:** assign IDs, rivals, evidence states, and kill criteria.
2. **Build tiny ground-truth models:** exhaustive interventions and exact route logs; demonstrate that analysis can recover known mechanisms.
3. **Conformance harness:** manifest validation, trace replay, causal checksum, and resource accounting.
4. **Architecture-controlled simulation:** B1–B5 on small capability and intervention suites.
5. **Continual-memory stream:** B6–B8 plus interference and truth-maintenance tests.
6. **Embodied simulation:** crossed body/environment factors, sensor faults, and active stress testing.
7. **Assurance-in-the-loop simulation:** formal properties, broker/fallback tests, common-mode faults.
8. **Independent code replication:** separate implementation of the strongest retained mechanisms.
9. **Hardware-in-loop mapping:** measured timing, traffic, energy, thermal, and fault injection.
10. **Bounded physical fixture:** only after safety-case review; no unrestricted humanoid deployment.

At every step, a negative result is an outcome, not a reason to silently redesign the hypothesis. Redesigns receive new version and claim identifiers.

## 22. Reusable experiment card

```markdown
# Experiment <ID>: <title>

## Claim and state
- Claim ID:
- Current evidence state:
- Proposed promotion/demotion:

## Competing hypotheses
- H0 / simpler rival:
- H1 / HC-1R mechanism:
- Divergent predictions:

## Frozen artifacts
- Architecture commit and connectome manifest:
- Compiler/runtime/simulator image:
- Data/environment/morphology versions:
- Assurance policy version:

## Baselines and matching
- Required baselines:
- Capacity/data/tuning/resource matching:
- Known mismatch and sensitivity analysis:

## Intervention
- Target, dose, time, duration, reversibility:
- Randomization and blinding:
- Single/multi-site controls:

## Outcomes
- Primary:
- Secondary:
- Safety:
- Resource:
- Diagnostic only:

## Analysis
- Unit of replication:
- Minimum practical effect:
- Sampling/power/precision:
- Statistical model and multiplicity:
- Exclusions/stopping:

## Decision table
- Retain if:
- Narrow if:
- Demote if:
- Reject if:
- Block if:

## Artifacts and review
- Logs/code/data/checksums:
- Independent reviewer:
- Deviations:
- Negative and null results:
```

## 23. Source-to-proposal boundary

The external literature demonstrates pieces of the method:

- controlled benchmarks can compare algorithms and systems;
- lesions and multi-site perturbations can reveal causal contribution and interaction in tractable networks;
- temporal-logic falsification, adaptive stress testing, and metamorphic testing can find counterexamples in simulated cyber-physical systems;
- continual learning suffers interference and has partial mitigations;
- embodied simulators and sim-to-real methods enable staged tests but leave a reality gap;
- runtime-assurance architectures can bound some advanced-controller risks in specified domains;
- preregistration and artifact review improve transparency;
- higher-order interactions can matter in some complex systems.

The following remain **HC-1R proposals**:

- that these methods can jointly verify a Noöplex hyperconnectome;
- that HC-1R's transient coalitions are causally irreducible;
- that its memory, modulation, and embodiment produce a favorable system frontier;
- that its distributed design degrades gracefully;
- that a suitable independent assurance boundary can be built for a synthetic humanoid;
- that any physical substrate can meet the eventual power, thermal, size, and reliability envelope.

The protocol succeeds scientifically if it makes those proposals easier to reject when they are wrong.

## 24. Current research verdict

An HC-1R concept is progressively testable without assuming or claiming consciousness. Its defining claims can be converted into comparative and interventional predictions, and mature methods exist for many parts of the test program. That supports an **EXTRAPOLATED** feasibility verdict for the research program—not for the integrated machine.

The present block is empirical: no frozen executable HC-1R model, matched baseline suite, or preregistered intervention dataset yet exists. Until those artifacts exist and the first causal discrimination tests are run, the hyperconnectome remains a structured, falsifiable hypothesis rather than a verified architecture.

