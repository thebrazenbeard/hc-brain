# Power and Thermal Architecture

## Scope

This document defines engineering constraints for powering and cooling HC-1, HC-2, and HC-3. It distinguishes scientifically conservative design assumptions from Wreckforge-specific extrapolation.

## Thermal premise

Any compact high-performance synthetic brain is constrained by heat before it is constrained by abstract computation. Biological neural tissue operates within a narrow thermal envelope, while dense electronics and pumps add localized heat flux. Therefore the architecture should minimize active refrigeration and prioritize low-power computation, heat spreading, vascular/microfluidic transport, and staged thermal throttling.

## HC-1 thermal model

HC-1 is the least demanding platform thermally because it does not require specialized quantum accelerator hardware or endocrine hardware as intrinsic subsystems.

Primary heat sources:
- living or organotypic neural tissue metabolism;
- neuromorphic support electronics;
- signal conversion and peripheral interface electronics;
- microfluidic pumps;
- memory and telemetry hardware.

Preferred cooling stack:
1. tissue-scale perfusion and microfluidic heat pickup;
2. thermally conductive cranial spreader layer;
3. heat transfer into body-wide circulation or a dedicated coolant loop;
4. external heat rejection through scalp, neck, torso, or other radiating surfaces.

The critical design goal is not to chill the brain but to maintain a stable near-physiological tissue temperature while avoiding local hotspots near electronics.

## HC-2 thermal model

HC-2 retains HC-1 cooling and adds a quantum/photonic accelerator layer.

### Scientifically conservative configuration

The preferred configuration uses quantum technologies that minimize cryogenic burden in the cranial volume, such as integrated photonics, room-temperature quantum sensors, or accelerator hardware located outside sensitive neural tissue. The quantum layer is a coprocessor, not the substrate of consciousness.

### Cryogenic variant

If a Wreckforge implementation specifically uses superconducting qubits, the millikelvin stage should not be modeled as simply sitting next to living brain tissue. A physically coherent design would require:
- extreme vacuum isolation;
- multiple thermal stages;
- mechanical vibration isolation;
- a remote heat-rejection system;
- stringent separation between the cold stage and physiological-temperature neural tissue.

For a humanoid body, this is a severe engineering penalty. A body-scale cryogenic module could be located in the torso or dorsal chassis with optical/electrical links to the brain. This preserves the setting's superconducting-QPU option while avoiding an implausible dilution refrigerator occupying the skull.

## HC-3 thermal model

HC-3 adds endocrine microfluidics, distributed sensing, autonomic control, and affective embodiment. These systems add heat primarily through pumps, control electronics, chemical processing, and body-wide thermal regulation.

The endocrine layer should not materially dominate the heat budget. The greater engineering challenge is that HC-3's emotional and autonomic state changes can alter compute demand and body heat simultaneously. A fight-or-flight analogue, for example, may increase actuator output, pump load, sensory processing, and accelerator use at once.

HC-3 therefore requires predictive thermal allocation rather than simple thermostat control.

## Thermal control hierarchy

### Level 0 — Passive stability

Heat spreaders, conductive cranial structures, compliant thermal interfaces, and body circulation remove heat without active intervention.

### Level 1 — Flow control

Regional microfluidic and body-circulation flow is increased toward active regions.

### Level 2 — Workload migration

Non-critical compute is shifted away from thermally stressed regions or delayed.

### Level 3 — Accelerator throttling

Photonic, digital, or quantum accelerators reduce duty cycle.

### Level 4 — Protective degradation

HC-2/HC-3 may temporarily fall back toward HC-1-class functionality if an accelerator thermal fault occurs. Sensorimotor control, identity-bearing memory, and basic cognition must remain available.

### Level 5 — Emergency shutdown of nonessential subsystems

Only nonessential hardware is disabled. The conscious core should not be abruptly powered down as an ordinary thermal-control mechanism.

## Power domains

The brain should use physically separate but coordinated power domains:
- neural tissue support;
- neuromorphic compute;
- memory preservation;
- sensory/motor I/O;
- pumps and microfluidics;
- quantum/photonic accelerators;
- endocrine/autonomic control;
- diagnostic and service electronics.

Critical domains should have independent ride-through storage so that loss of one subsystem does not erase state or collapse the entire organism.

## Energy accounting

Exact wattage is intentionally left as a design variable until the material implementation is fixed. Earlier figures such as tens of watts for biological neural tissue are useful order-of-magnitude anchors, but HC-series totals depend strongly on whether the system uses living neural tissue, synthetic neurons, conventional CMOS, photonic logic, memristive arrays, superconducting qubits, or a mixed architecture.

Accordingly, repository documents should distinguish:
- measured real-world component power;
- extrapolated subsystem power;
- in-universe design targets.

## Compatibility with Synthetic body physiology

If the Synthetic body uses a body-wide coolant/blood analogue such as the vitreofluid concept proposed in PR #1, it can serve as the primary heat transport medium for the Noöplex. This is architecturally useful because it unifies metabolic transport, endocrine signaling, and heat rejection. However, the exact fluid chemistry and claimed performance remain Wreckforge-specific until separately supported.

## Design rule

The HC-series should fail gracefully from HC-3 -> HC-2 -> HC-1-like capability as optional accelerators or affective subsystems are thermally constrained. It should never require perfect operation of every advanced subsystem merely to remain conscious, embodied, and functional.