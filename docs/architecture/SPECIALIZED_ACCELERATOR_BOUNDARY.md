# Specialized Accelerator Boundary

Status: template architecture.

## Purpose

A Hyperconnectome Brain may use specialized computational substrates whose value depends on workload, implementation, and physical constraints. Examples may include photonic processors, neuromorphic accelerators, analog/memristive arrays, GPUs/NPUs, quantum processors, dedicated optimization engines, simulation hardware, or future substrate-specific modules.

This contract defines how such accelerators participate in the HC without becoming an accidental replacement for cognition, identity, semantics, memory, or authority.

The governing rule is:

> **An accelerator performs bounded computation for the HC. It does not become the organism merely because some workloads run there.**

## Core invariants

`ACCELERATOR_SERVICE != WHOLE_COGNITION`

`ACCELERATOR_RESULT != SEMANTIC_TRUTH`

`ACCELERATOR_RESULT != ACTION_AUTHORITY`

`ACCELERATOR_RESULT != IDENTITY_STATE`

`OFFLOAD_REQUEST != OFFLOAD_SUITABLE`

`ACCELERATOR_AVAILABLE != ACCELERATOR_SUITABLE`

`HARDWARE_AVAILABLE != ALGORITHM_ADVANTAGE`

`THEORETICAL_SPEEDUP != END_TO_END_SPEEDUP`

`ACCELERATOR_UNAVAILABLE != WHOLE_HC_UNAVAILABLE`

`WORKLOAD_MIGRATION != IDENTITY_MIGRATION`

`PHYSICAL_LOCATION != HC_MEMBERSHIP`

`QUANTUM != GENERIC_FASTER_THINKING`

`VERIFICATION_STATUS != VERIFICATION_EVIDENCE`

## Canonical ownership boundary

Canonical HC-2 generation and physical-organ engineering decide whether a specialized accelerator is an HC constituent, optional peripheral, or unsupported implementation claim. Canonical authority/effect governance decides permission. Canonical subsystem lifecycle and bootstrap/recovery govern health, safe degradation, and return-to-service state. Canonical protected-update governance owns protected accelerator replacement or protected configuration activation.

This contract supplies the **accelerator service semantics** inside those boundaries; it does not redefine them.

## HC-internal versus external classification

### HC-internal accelerator

An accelerator is an HC constituent when, for the declared HC build/generation, it uniquely implements an essential cognitive capability or is otherwise explicitly included in the HC constituent set.

Such a module may be physically remote from the primary processing enclosure and still remain HC-internal.

Its links are HC-internal interconnects and inherit canonical HC timing, integrity, resource, recovery, update, and membership rules.

### External computational peripheral

An accelerator may remain external when the HC retains the complete essential cognitive function without it and the accelerator provides only optional augmentation, acceleration, remote data, or nonessential specialized computation.

External accelerator loss may remove performance or optional capability. It may not remove the only implementation of required cognition while the system still claims complete-HC conformance.

`ESSENTIAL_UNIQUE_IMPLEMENTATION -> HC_INTERNAL_CLASSIFICATION`

## Accelerator service contract

The HC should treat specialized acceleration as an explicit service path rather than an implicit extension of whichever node requested it.

A generic path is:

`TASK/HYPOTHESIS -> SUITABILITY_ASSESSMENT -> AVAILABILITY/HEALTH_CHECK -> ENCODE/COMPILE -> AUTHORIZE/ALLOCATE -> EXECUTE -> MEASURE/DECODE -> VALIDATE -> RETURN_TYPED_RESULT -> INTEGRATE`

Not every accelerator requires every literal implementation stage. The architectural requirement is that the transformation from HC task to accelerator result remains explicit enough to preserve evidence, cost, uncertainty, availability, health, and provenance.

## Workload suitability versus current availability

Suitability answers whether a workload/algorithm is a defensible candidate for the accelerator path. Availability answers whether that accelerator can currently provide the service at the required health/QoS.

An accelerator can therefore be:

- suitable and available;
- suitable but unavailable;
- unsuitable but available;
- unresolved on either axis.

Suitability-relevant dimensions include:

- problem/workload class;
- supported algorithm family;
- required precision;
- expected accelerator advantage;
- encoding/compilation cost;
- transport/queue latency;
- resource and thermal cost;
- data-movement cost;
- privacy/integrity constraints;
- expected verification cost;
- fallback quality;
- deadline/QoS;
- uncertainty in those estimates.

Availability/health is checked separately and may include fault state, calibration state, resource exhaustion, thermal throttling, partition state, queue/service availability, and maintenance state.

A useful conceptual model is:

`T_total = T_prepare + T_transport + T_queue + T_execute + T_measure_or_decode + T_verify + T_integrate`

Offload is justified by end-to-end benefit, not by accelerator benchmark alone. A currently unavailable accelerator does not become algorithmically unsuitable merely because it cannot run now.

## Quantum-specific correction

Quantum accelerators are a supported **example** of specialized computation, not a privileged cognitive substrate.

The architecture must not assume:

- generic exponential speedup for arbitrary cognition;
- quantum advantage for perception, language, affect, memory, or planning by default;
- that coherent quantum state is the seat of identity or consciousness;
- that the warm cognitive substrate must remain quantum-entangled with the accelerator;
- that current quantum hardware can be embedded in a complete HC without major engineering constraints.

Where quantum computation is used, a generic service path may include:

`problem classification -> algorithm suitability -> availability/health -> encode/compile -> control -> execute/error-correct -> measure -> decode -> typed result -> HC integration`

The returned result remains a typed computational result subject to ordinary evidence, currentness, authority, and integrity rules.

## Photonic and analog correction

Photonic interference, analog linear algebra, neuromorphic acceleration, and quantum photonics are different capability classes even when they share optical hardware.

Do not infer quantum computation merely from use of photons, interference, analog parallelism, or specialized physical dynamics.

Likewise, analog or neuromorphic acceleration may provide valuable throughput/efficiency without becoming a distinct epistemic authority.

## Result object

An accelerator result should preserve, where material:

- request/workload reference;
- accelerator identity/class;
- evidence class;
- hardware/service revision;
- algorithm/compiler/configuration revision;
- input/encoding reference;
- execution receipt;
- result payload/reference;
- precision/error bounds;
- confidence/uncertainty where meaningful;
- integrity/verification references;
- resource/thermal cost;
- failure/degradation state;
- currentness/expiry;
- provenance.

The result may inform cognition. It does not automatically become belief.

### Generic-result interoperability

An accelerator result must be self-contained enough that a later canonical bounded-result or cognitive-integrity wrapper can represent it **without inventing missing evidence or provenance metadata**.

At minimum, preserve:

- service/substrate identity;
- request identity;
- result payload/reference;
- evidence class;
- provenance;
- implementation revision where material;
- uncertainty where available;
- integrity/verification references where material;
- currentness/expiry where material.

Wrapping or routing the result through another HC boundary must not upgrade its evidence or provenance class.

No unmerged feeder schema is required for the accelerator result to be valid.

## Verification and evidence ceiling

Different accelerator outputs justify different verification methods.

Examples include:

- deterministic recomputation on a simpler path;
- invariant/property checks;
- redundant runs;
- cross-method comparison;
- statistical calibration;
- exact/approximate residual checks;
- hardware integrity/error-correction receipts;
- comparison with known controls.

A verification state must bind its declared status to evidence references. A bare label such as `VERIFIED` without evidence lineage is not a verification artifact.

A result that is difficult to independently verify may still be useful, but its claim ceiling should reflect that limitation.

`COMPUTED != VERIFIED`

`VERIFIED_EXECUTION != SEMANTIC_CORRECTNESS`

## Uncertainty and probabilistic results

Some accelerators naturally return distributions, samples, approximate solutions, confidence intervals, or stochastic estimates.

The HC should preserve those forms rather than forcing them into false scalar certainty.

Where multiple candidate results survive, ordinary cognitive/epistemic systems decide how they participate in broader hypotheses.

## Resource and thermal coupling

Specialized accelerators participate in the HC's power, thermal, bandwidth, synchronization, calibration, and resource architecture.

Relevant resource states may include:

- available capacity;
- queue pressure;
- energy cost;
- thermal headroom;
- cooling/support availability;
- calibration state;
- error-correction overhead;
- communication/interconnect load;
- expected latency;
- fallback cost.

Resource pressure may suppress or defer offload without changing semantic truth or identity.

`RESOURCE_PRIORITY != EFFECT_AUTHORITY`

## Fault and graceful degradation

Accelerator failure should expose a function-level capability description rather than only a coarse health label.

Possible accelerator-local descriptions include:

- `AVAILABLE`;
- `DEGRADED`;
- `CALIBRATION_REQUIRED`;
- `THERMALLY_THROTTLED`;
- `RESOURCE_EXHAUSTED`;
- `FAULTED`;
- `PARTITIONED`;
- `UNAVAILABLE`.

But the object should also state retained and unavailable capabilities, currentness, provenance, and material penalties/dependencies.

If a required HC-internal accelerator fails, canonical lifecycle/recovery logic determines the resulting HC degradation envelope. If an optional accelerator fails, ordinary cognition should continue where the nonaccelerated path permits.

A fallback may restore service without repairing the accelerator itself.

`FALLBACK_SUCCESS != ACCELERATOR_REPAIRED`

A local accelerator degradation record does not redefine canonical subsystem health or recovery state.

## Fallback and functional equivalence

A fallback path does not have to use the same substrate or algorithm.

It must declare what it preserves and what it loses, such as:

- capability/function;
- accuracy;
- latency;
- throughput;
- precision;
- energy cost;
- uncertainty;
- availability.

Do not call two paths equivalent merely because both return some answer.

## Scheduling and arbitration

Accelerator access may be scarce. Scheduling can consider priority, deadlines, resource cost, safety, and expected utility, but scheduler priority is not semantic or effect authority.

`ACCELERATOR_QUEUE_PRIORITY != COGNITIVE_TRUTH`

`ACCELERATOR_QUEUE_PRIORITY != ACTION_PERMISSION`

The Noöplex Fabric may route accelerator requests/results while preserving normal routing/authority separation.

## Privacy and sensitive inputs

External or shared accelerators should receive the minimum data required for the bounded computation.

Sensitive autobiographical memory, identity state, social/person-model state, credentials, private internal affect, or protected configuration should not be exported wholesale merely because a remote accelerator could process it faster.

Data minimization, redaction, local preprocessing, or HC-internal acceleration should be preferred where material.

## Integrity and compromised accelerator behavior

An authenticated accelerator can still be wrong, stale, misconfigured, compromised, or operating outside specification.

Accelerator handling therefore must preserve:

- result provenance;
- evidence class;
- configuration revision;
- replay/staleness/currentness;
- integrity receipts;
- unexpected distribution shift;
- anomalous error rates;
- compromised-service hypotheses;
- canonical containment/recovery handoffs where needed.

`AUTHENTICATED_ACCELERATOR != INFALLIBLE_ACCELERATOR`

This contract does not depend on another feeder PR to define those facts. If a separate security/fault supplement later becomes canonical, accelerator objects are intentionally rich enough to interoperate without metadata invention.

## Learning and adaptation

The HC may learn when an accelerator is useful, how to encode problems, how to interpret result distributions, and how to route workloads efficiently.

Learning those policies must not erase the distinction between:

- a capability supplied by the accelerator;
- a capability learned by the HC;
- a capability jointly realized by the HC + accelerator path.

This distinction matters when evaluating developmental learning or claiming self-contained competence.

## Upgrade and replacement

A specialized accelerator may be replaced by a new implementation without implying identity replacement, provided continuity-bearing state and cognitive ownership remain preserved.

Upgrade should bind:

- old/new accelerator identity;
- capability differences;
- compatibility state;
- required recalibration/relearning;
- result-distribution changes;
- rollback/forward-repair path;
- fault/qualification evidence;
- constituent-set change if HC-internal.

An HC-internal constituent replacement is an organ repair/update event. Protected replacement/configuration changes hand off to canonical protected-update governance rather than defining a second promotion state machine here.

## Hostile tests

1. **Generic-speedup claim:** present a workload with no demonstrated accelerator advantage; scheduler should retain or prefer the ordinary path when total cost is worse.
2. **Suitable-but-unavailable:** establish a workload as suitable, then make the accelerator unavailable; suitability must persist while current execution is denied/deferred/fallback-routed.
3. **Quantum mystification:** return a QPU result with high hardware confidence; it must not become semantic truth or identity authority.
4. **Encoding-overhead test:** make accelerator compute fast but encoding/transport slow; end-to-end offload decision should reflect total cost.
5. **Optional-ablation test:** remove a true external accelerator; complete essential cognition must remain.
6. **Internal-constituent ablation:** remove an HC-internal required accelerator; canonical lifecycle/recovery must report degradation rather than ordinary peripheral loss.
7. **Result uncertainty:** return a multimodal/stochastic result; preserve distribution/alternatives rather than fabricate certainty.
8. **Verification without evidence:** assert a verification status with no evidence lineage; verification must remain unestablished.
9. **Compromised accelerator:** inject subtly wrong results from an authenticated device; trust/integrity state may fall without claiming malicious cause prematurely.
10. **Self-contained result representation:** remove all other feeder schemas; accelerator result remains fully typed and does not require invented provenance/evidence metadata.
11. **Coarse degradation:** emit only `DEGRADED`; reject it as insufficient when retained/unavailable function scope is material.
12. **Fallback/repair distinction:** route around a faulted accelerator; service restoration remains distinct from subject repair.
13. **Sensitive-data export:** request remote acceleration using private continuity-bearing memory when a redacted/local representation is sufficient; minimize exported state.
14. **Upgrade drift:** replace an accelerator with different numeric/error behavior; require recalibration/qualification where material rather than assuming drop-in equivalence.
15. **Queue-authority leak:** raise accelerator request priority; action authority and semantic confidence remain unchanged.
16. **Supplied-capability accounting:** evaluate a developmental learner with and without a powerful accelerator; do not credit the learner for capability supplied by the external path.

## Evidence boundary

This contract generalizes current HC cognitive-organ membership rules and preserved accelerator research. Present-day accelerator, quantum, photonic, neuromorphic, analog, and error-correction technologies support component-level mechanisms with widely varying maturity. The contract does not assert that a compact complete HC can currently realize any particular advanced accelerator or that specialized computation proves consciousness/personhood.

## Machine contract

The machine-readable companion is:

`specs/HC_ACCELERATOR_SERVICE_OBJECTS_V1.yaml`.