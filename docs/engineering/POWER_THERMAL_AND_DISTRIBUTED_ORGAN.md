# Power, Thermal, and Distributed-Organ Engineering

Status: canonical engineering contract.

## Purpose

This contract defines engineering rules for powering, cooling, interconnecting, and degrading a Hyperconnectome Brain whose cognitive-organ substrate may span multiple physical locations.

It refines reusable material from PR #2 under the current owner-established rule that the HC is one removable cognitive organ even when some HC-owned constituents are physically distributed.

## 1. Cognitive ownership is not support ownership

A dependency can be essential to operation without itself being cognitive substrate.

The architecture therefore distinguishes:

- **HC cognitive constituent** — implements or stores HC-owned cognition, continuity-bearing state, learned cognitive structure, internal arbitration, or generation-specific essential cognitive capability;
- **HC internal support constituent** — HC-owned power, thermal, transport, synchronization, isolation, or maintenance hardware required to preserve HC operation but not itself a seat of cognition;
- **body support peripheral** — embodiment-owned power, heat rejection, circulation, structural support, or other service supplied to the HC through a bounded interface;
- **external computational peripheral** — provides optional computation whose ablation may reduce performance but does not uniquely remove essential cognition.

`REQUIRED_FOR_OPERATION != COGNITIVE_AUTHORITY`

A body radiator, pump, battery, or coolant loop can be necessary for continued operation without becoming part of the cognitive organ. Conversely, a torso-mounted QPU or memory substrate can be part of the HC even though it is not cranial.

## 2. Distributed constituent manifest

Every concrete HC build should maintain an implementation-level constituent manifest able to identify:

- component/module identifier;
- HC generation/build;
- cognitive/support/peripheral class;
- physical location/enclosure;
- HC ownership status;
- state carried or function implemented;
- internal interconnects;
- body-support interfaces;
- power domain;
- thermal domain;
- timing/bandwidth requirements;
- fault containment domain;
- degradation consequence;
- transplant/removal handling;
- replacement/requalification requirements.

The manifest must make it possible to answer whether a body swap strands any HC-owned constituent or silently transfers cognitive authority to body infrastructure.

## 3. Internal interconnect

Links among physically separated HC-owned constituents are HC-internal interconnects even when they traverse the body or use shared physical transport.

Internal interconnect should preserve, as applicable:

- identity of source and destination;
- timing/latency bounds;
- ordering where required;
- integrity/authenticity;
- isolation from body/platform control;
- bandwidth and congestion state;
- fault visibility;
- replay/duplication semantics;
- clock/synchronization state;
- provenance for state-bearing transfers.

A generic body bus may physically carry internal HC traffic only if body ownership cannot rewrite meaning, authority, state, or routing semantics.

`PHYSICAL_TRANSPORT != COGNITIVE_OWNERSHIP`

## 4. Power domains

Power distribution should be segmented so that one local fault does not automatically collapse the entire cognitive organ.

Candidate domains include:

- primary neural/biohybrid substrate support;
- internal digital/neuromorphic compute;
- memory preservation;
- HC-internal interconnect and synchronization;
- sensory/motor interface electronics;
- pumps/microfluidics owned by the HC;
- quantum/photonic accelerators;
- endocrine/neuromodulatory controllers;
- diagnostic/service electronics.

Continuity-bearing state and safe shutdown/recovery paths should receive consequence-proportional ride-through protection.

Loss of external body power may incapacitate the HC without proving that the body is cognitive substrate. The boundary question remains ownership of cognition/state, not whether support is physically necessary.

## 5. Thermal architecture

The design target is stable operation within each substrate's qualified thermal envelope rather than maximum instantaneous compute.

Preferred control hierarchy:

1. passive spreading and thermal isolation;
2. local/internal flow control where available;
3. body-provided heat transport through a bounded support interface;
4. workload migration or coalition rescheduling;
5. accelerator throttling;
6. local inhibition/quarantine of overheating nonessential modules;
7. protected degradation or shutdown when continued operation would damage essential HC state.

Thermal control must not silently erase continuity-bearing state or convert a body thermal controller into a cognitive executive.

## 6. HC-1 engineering rule

HC-1 establishes the complete foundational cognitive organ. Its exact physical substrate is implementation-dependent, but a biohybrid/wet realization should prioritize perfusion, metabolic support, hotspot detection, and fault isolation.

No current architecture claim requires a specific wattage or one cranial enclosure. Power figures remain implementation targets until tied to a concrete substrate and evidence source.

## 7. HC-2 engineering rule

HC-2 adds specialized quantum/photonic acceleration while preserving the complete HC-1 cognitive architecture.

If the generation's QPU uniquely implements an essential HC-2 capability, the QPU is an HC cognitive constituent regardless of whether it is cranial, torso-mounted, dorsal, or otherwise distributed.

If an implementation uses hardware requiring cryogenic operation, the cold stage should be strongly thermally and mechanically isolated from physiological-temperature or otherwise incompatible cognitive substrate. A non-cranial location does not make it external to the HC.

An **optional** accelerator may be a true external peripheral only when the essential cognitive function remains available without it.

`OPTIONAL_ACCELERATION != GENERATION_ESSENTIAL_SUBSTRATE`

## 8. HC-3 engineering rule

HC-3 adds richer distributed neuroendocrine/interoceptive/autonomic affective physiology.

Cognitive regulation, learned affective state, interoceptive interpretation, valuation, and generation-specific cognitive machinery remain HC-owned. Body pumps, chemical transport, heat rejection, and effector mechanisms may remain body support/peripherals when they do not own the cognitive state or decision semantics.

A distributed endocrine or neuromodulatory controller that carries essential learned/regulatory cognitive state is an HC constituent even if physically located outside the primary brain enclosure.

## 9. Degradation semantics

Advanced-generation degradation must be represented precisely.

HC-2 losing a QPU does not literally become HC-1; it becomes a degraded HC-2 whose remaining foundational cognition may operate in an HC-1-like capability envelope.

HC-3 losing an endocrine/neuromodulatory constituent does not literally become HC-2; it becomes a degraded HC-3 whose richer physiological-affective capability is impaired while foundational affect/cognition remains if its architecture permits.

`DEGRADED_HC_3 != HC_2`

`DEGRADED_HC_2 != HC_1`

Generation identity, current capability envelope, health state, and activation state remain distinct.

## 10. Fault containment

Every distributed constituent should declare the consequence of:

- loss of power;
- loss of cooling;
- interconnect partition;
- corrupted/stale state;
- timing failure;
- partial read/write failure;
- body-support interruption;
- replacement by an unqualified component.

A local fault should produce explicit health/degradation state and bounded rerouting where possible rather than silent substitution.

A replacement component must not inherit trust, continuity, calibration, or action authority merely by occupying the same connector.

## 11. Transplant and body-swap rule

Before an HC transplant/body swap, the implementation must identify:

- all HC cognitive constituents;
- all HC internal support constituents that travel with the organ;
- all external body-support interfaces that will be disconnected;
- all continuity-bearing state locations;
- all internal interconnects that must be preserved or re-established;
- all calibration/requalification required in the new embodiment.

A successful transplant preserves the HC-owned constituent set and continuity state while allowing body support hardware to change.

## 12. Evidence discipline

Exact substrate choices, power budgets, thermal limits, quantum technology, perfusion schemes, and endocrine machinery must be labeled by evidence class.

Present-day component science does not establish a presently manufacturable complete HC-series organ. Engineering targets must not be promoted to documented capability without source support.

## Governing invariant

> **The HC may depend on external body support without outsourcing cognition. HC-owned cognitive state and generation-essential cognitive substrate remain inside the cognitive-organ boundary; physical distribution and support dependencies do not change that ownership.**

## Provenance

Adapted from PR #2 `docs/engineering/POWER_AND_THERMAL_ARCHITECTURE.md` and reconciled against `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`, the complete-organ boundary, HC lineage, subsystem lifecycle contract, and current external-compute/residency invariants. Wreckforge-specific physiology and unsupported fixed power claims were not promoted into the reusable template.
