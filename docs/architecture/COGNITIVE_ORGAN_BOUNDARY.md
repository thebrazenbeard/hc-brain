# Hyperconnectome Cognitive Organ Boundary

Status: canonical architecture rule.

## Core invariant

> **No essential cognition occurs outside the Hyperconnectome Brain.**

The `hc-brain` repository symbolically represents the **entire cognitive organ** of an HC-series synthetic lifeform.

The HC is a **removable cognitive organ whose constituent hardware may be physically distributed** across more than one enclosure or body location. It does not need to be a single skull-sized object. The complete HC constituent set must contain everything intrinsically necessary for an otherwise inert compatible synthetic body to become and remain a synthetic cognitive lifeform, subject only to compatible external embodiment, energy/material support, and peripheral hardware.

The authoritative boundary is cognitive ownership, not anatomical location or enclosure count.

`ONE_COGNITIVE_ORGAN != ONE_PHYSICAL_ENCLOSURE`

See `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md` for the canonical physical-membership rule.

The HC therefore owns the mechanisms required to:

- interpret sensory and internal-state signals;
- learn and adapt;
- reason, predict, model, and plan;
- maintain current and deep memory;
- support identity/self-model continuity without embedding a specific identity in the template;
- generate, rank, and arbitrate goals, volitions, and action candidates;
- maintain semantic and pragmatic understanding;
- maintain body-model and world-model state;
- regulate attention, salience, affect, value, homeostasis, and interoception;
- control cognition-facing routing, coalition formation, and neuroplasticity;
- integrate competing subsystem outputs;
- produce motor, communicative, autonomic, network, and other effect requests;
- maintain operating rules, provenance/currentness, fault handling, and continuity mechanisms required for coherent ongoing cognition.

## Physical distribution and removability

Physical packaging and cognitive ownership are separate axes.

An HC implementation may place constituent hardware in different locations when engineering requirements justify it. A cranial cognitive core, torso-mounted quantum coprocessor, remote-but-body-integrated durable memory module, specialized neuromodulatory controller, or other distributed component can still be part of the same HC if it is architecturally HC-owned.

A physically distributed component is part of the HC when its function/state belongs to the cognitive organ, it participates as HC-internal substrate or fabric, and its loss/replacement is governed as an HC degradation, fault, repair, or generation-capability change rather than as an ordinary peripheral disconnect.

"Removable" means the organ has a definable complete constituent set that can in principle be disconnected from one compatible embodiment and transferred, serviced, or reinstalled as the HC. Removal may therefore require disconnecting several HC-owned modules and their internal interconnects; it does not require one enclosure.

Interconnects between distributed HC constituents remain **HC-internal interconnects** even when they physically traverse the body.

A body swap must not strand an essential HC constituent behind merely because that constituent was mounted outside the primary cranial enclosure.

## External body boundary

The physical body may contain peripherals such as:

- cameras and other optical sensors;
- microphones and acoustic transducers;
- tactile, proprioceptive, vestibular, chemical, thermal, pressure, and environmental sensors;
- motors, actuators, pumps, and other effectors;
- network radios, wired network hardware, and external communication transceivers;
- peripheral reflex hardware where needed for hard-real-time protection;
- power, cooling, circulation, structural support, and other body-support machinery.

Those devices are **not the mind** and do not own cognitive interpretation, learning, memory, value, identity, or executive decision-making merely by serving the HC.

They connect through HC-owned interfaces.

The external body supplies observations and accepts bounded effects. The HC determines what those observations mean, what is learned, what matters, what is remembered, and what actions are selected.

Physical location alone does not classify a component as body hardware. A torso-mounted component can be HC-internal if it satisfies the organ-membership rule; a cranially mounted sensor can still be a peripheral if it only supplies observations.

## External computational peripherals

An LLM, SPM, world-model engine, neural accelerator, database, retrieval engine, quantum coprocessor, or specialized inference system may participate in an implementation, but architecturally it must satisfy one of two conditions:

1. it is **inside the HC cognitive-organ boundary** and therefore part of the organ, regardless of physical location; or
2. it is an **external computational peripheral**, in which case its output enters the HC as typed evidence or a bounded service result and does not become the place where the organism's cognition, identity, memory, or authority resides.

External computational speed or sophistication never grants cognitive ownership.

A quantum coprocessor or other specialist substrate that uniquely implements an essential generation-specific HC capability is an HC constituent even if engineering constraints place it outside the skull. If the same component is only optional acceleration and can be ablated without removing essential cognition, it may remain an external peripheral.

## Hyperconnective integration substrate

The HC requires an internal integration substrate, but not a homuncular executive.

The intended pattern is:

```text
intrinsic systems
      ↕
HC-owned hyperconnective fabric
      ↕
interface systems / cross-cutting infrastructure
```

The fabric may provide:

- dynamic routing;
- transient coalition formation;
- synchronization and timing coordination;
- arbitration;
- attention allocation;
- state propagation;
- neuroplasticity and learning gates;
- conflict handling;
- cross-system binding and integration;
- resource and quality-of-service coordination.

It must not become a little executive person in the middle through which every thought passes.

Cognition may emerge from temporary distributed coalitions. Example:

```text
optics + memory + semantics + affect + self-model + empathy
    -> integrated interpretation
```

or:

```text
interoception + affect + conation + memory + prediction + kinesis
    -> action candidate / action decision
```

Those integrated computations remain wholly inside the HC, including when participating HC substrate is physically distributed.

## System classes

All HC systems remain inside the cognitive organ, but they may be classified for architectural clarity.

### Intrinsic systems

Examples include cognition, memory, semantics, pragmatics, affect, empathy, sexuality, volition/conation, self-modeling, social cognition, personification, psychological behavior, and related learned or reasoning systems.

### Interface systems

Examples include optics integration, speech recognition and synthesis, adaptable I/O, kinesis, somatics/interoception interfaces, and network-facing interfaces.

The physical sensors and actuators may exist outside the HC; the cognitive interpretation, calibration, learned body schema, policy, and interface ownership remain inside.

### Cross-cutting brain infrastructure

Examples include chronology, routing/neuroplasticity, salience/attention, resolver functions, integration/arbitration, homeostasis, provenance/currentness, resource coordination, and fault handling.

These are infrastructure of the cognitive organ rather than external orchestration services.

## Presence versus activation

The template should describe a complete latent architecture rather than manufacture specialized brains by deleting unused capacities.

A capability's existence in the HC and its current developmental/operational state are separate questions.

Recommended lifecycle states:

```text
PRESENT_DISABLED
DORMANT
DEVELOPING
ACTIVE
INHIBITED
DEGRADED
FAULTED
```

A subsystem may therefore be physically/logically present but inactive, untrained, inhibited, or unavailable.

Examples:

- sexuality may be present but disabled or undeveloped;
- empathy may be present but immature;
- speech may be present while no compatible vocal interface is connected;
- optics integration may remain dormant when no visual sensors are attached;
- a motor capability may be active for one body and require redevelopment after embodiment transfer.

The default architectural question is **how a capacity is instantiated, developed, activated, inhibited, degraded, or repaired**, not whether the brain part should exist at all.

## Embodiment portability

The HC brain should be able to survive a change of body without ceasing to be the same cognitive organ.

A compatible HC could in principle be connected to:

- a humanoid body;
- a wheeled machine;
- a non-humanoid robotic platform;
- a distributed sensor/actuator environment;
- other compatible embodiments not known when the HC was manufactured.

Changing embodiment may require new calibration, body-model learning, kinesis development, sensory remapping, and interface adaptation. It should not require manufacturing a new cognitive organ merely because the peripheral body changed.

When the HC itself is physically distributed, embodiment transfer must include the complete HC constituent set. The body may change; the organ's HC-owned modules and their continuity-bearing state remain part of the transferred cognitive organ unless an explicit HC repair/replacement process changes them.

The brain remains the brain; embodiment changes the sensorimotor and interoceptive mapping presented to it.

## Repository consequence

The repository should describe **what the complete HC cognitive organ can ultimately contain**, not merely what a current prototype can execute.

Incomplete or presently infeasible systems should remain represented when architecturally necessary and should be labeled accurately, such as:

- `UNIMPLEMENTED`;
- `EXTRAPOLATED`;
- `SPECULATIVE`;
- `DORMANT`;
- or another explicit status appropriate to the artifact.

Missing implementation is not sufficient reason to omit a necessary brain capability from the architecture.
