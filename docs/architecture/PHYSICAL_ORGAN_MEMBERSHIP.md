# Physical Organ Membership

Status: canonical architecture rule.

## Owner decision

The Hyperconnectome Brain is a **removable cognitive organ that may have physically distributed constituent hardware so long as all of that hardware belongs to the HC rather than the body**.

The cognitive-organ boundary is therefore authoritative over enclosure geometry.

`ONE_COGNITIVE_ORGAN != ONE_PHYSICAL_ENCLOSURE`

A conforming HC may occupy more than one physical location in an embodiment. For example, a primary wet/biohybrid or computational core may reside cranially while a quantum accelerator, specialized interconnect module, durable memory substrate, endocrine/neuromodulatory controller, or other HC-owned component resides in the torso or another protected location.

Those components remain parts of one HC organ when they satisfy the membership rules below.

## Three boundaries that must remain distinct

### Cognitive-organ boundary

This is the authoritative architectural boundary. It contains every substrate, state-bearing mechanism, processing capability, internal fabric component, and dedicated service required for essential HC cognition and continuity.

### Physical assembly/enclosure boundary

This describes where HC hardware is physically packaged. One HC may span multiple enclosures or body locations.

Enclosure location does not decide cognitive ownership.

### Body/peripheral boundary

The body provides replaceable embodiment, sensing, actuation, structural support, power/thermal/circulatory support, and other external-world interfaces through HC-owned interface contracts.

A component is not body hardware merely because it is mounted outside the skull.

## HC constituent membership test

A physically distributed component belongs to the HC cognitive organ when the architecture classifies it as HC-owned and the implementation preserves that classification through explicit integration. Relevant indicators include:

- it implements or stores an HC-internal cognitive capability or essential continuity-bearing state;
- it participates in the HC-internal Noöplex/Hyperconnectome Fabric rather than merely exposing a body peripheral interface;
- its authority, state, lifecycle, provenance, fault handling, and replacement semantics are governed as part of the HC;
- it is dedicated to the HC or partitioned strongly enough that body/platform ownership cannot silently supersede cognitive-organ ownership;
- loss of the component would constitute HC degradation/fault or generation-level capability loss rather than an ordinary body-peripheral disconnect;
- transplant/removal of the complete HC requires accounting for that component as part of the organ package, even if it occupies a separate enclosure.

No single indicator alone is sufficient in every implementation. The decisive question is architectural ownership: **does this component belong to the cognitive organ or merely serve it from the body?**

## Removability

"Removable" does not require a single skull-sized cartridge.

It means the complete HC has a definable constituent set and boundary that can, in principle, be disconnected from one compatible embodiment and transferred, serviced, or reinstalled without redefining essential cognitive functions as body-owned.

A distributed HC transplant may therefore involve disconnecting several HC-owned modules and their internal interconnects from the host body.

Body replacement may change sensors, effectors, support hardware, and embodiment mappings. It must not silently strand an essential HC constituent behind as if it were merely body hardware.

## HC-2 consequence

An HC-2 quantum coprocessor may physically reside in a torso or other non-cranial enclosure when cooling, shielding, mass, vibration, or engineering constraints make that preferable.

If that QPU uniquely implements an essential HC-2 cognitive capability, it is an HC constituent, not an external body peripheral, regardless of its location.

If it is merely optional acceleration and the HC retains the full essential function without it, it may instead be treated as an external computational peripheral.

Location alone does not decide the classification.

## HC-3 consequence

HC-3 may use physically distributed endocrine, autonomic, neuromodulatory, interoceptive, or related hardware.

Any such component that is part of the HC's essential cognitive regulation, learned internal state, or required generation-specific cognitive machinery belongs inside the HC cognitive-organ boundary even if physically distributed through the embodiment.

Body-support or effect-delivery machinery may remain peripheral when the HC retains the cognitive state, interpretation, regulation, and decision machinery internally.

## Interconnect consequence

Links between physically separated HC constituents are **internal HC interconnect**, not body I/O merely because they traverse the body.

They should be treated as part of the organ's own fault, timing, bandwidth, integrity, provenance, and degradation model.

A body bus or generic network may physically carry HC traffic only if the architecture preserves HC ownership, isolation, and integrity strongly enough that the transport does not become an external cognitive authority.

## Conformance questions

A physical implementation should be able to answer:

1. What exact components constitute the HC organ in this generation/build?
2. Which of those components are physically distributed outside the primary cranial enclosure?
3. Which links among them are HC-internal interconnects rather than body interfaces?
4. What essential cognition or continuity is lost if each component is removed?
5. Does body replacement leave every HC constituent accounted for as part of the organ transfer?
6. Could a body/platform controller override, replace, or become sole owner of an HC constituent's cognitive state or authority? If yes, the boundary is defective.
7. Are optional external accelerators/peripherals clearly distinguished from distributed HC-internal constituents?

## Governing invariant

> **The Hyperconnectome Brain is one cognitive organ whose physical substrate may be distributed. Cognitive ownership, not anatomical location or enclosure count, determines organ membership.**
