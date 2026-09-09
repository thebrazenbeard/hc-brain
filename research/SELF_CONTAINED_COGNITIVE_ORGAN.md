# Self-Contained Cognitive Organ

Status: owner design requirement synthesis / architecture input / not an empirical claim

This document formalizes the intended role of the Hyperconnectome Brain as a generic, self-contained synthetic cognitive organ. It is a design constraint for interpreting research and repository structure, not a scientific claim that the full organ has been implemented or that any architecture establishes consciousness or personhood.

## Core requirement

> **No essential cognition occurs outside the Hyperconnectome Brain.**

The HC repository symbolically represents the complete brain object: the internal systems required for perception, interpretation, learning, memory, prediction, reasoning, social cognition, affective and conative state, self-modeling, action selection, body adaptation, chronology, arbitration, plasticity, fault handling, and other cognitive capacities live inside the HC boundary.

External hardware may provide sensing, actuation, communications, energy, and other embodiment services. Those devices do not become the cognitive organ merely because they are connected to it.

---

## 1. Brain boundary versus body boundary

The synthetic body may contain:

```text
cameras
microphones
chemical/environmental sensors
proprioceptive sensors
joint encoders
actuators
motors
speakers
network transceivers
power systems
thermal systems
remote sensor nodes
remote actuator nodes
```

These are body/peripheral components unless the architecture deliberately incorporates their compute into the HC cognitive substrate.

The HC owns the cognitive interpretation of their signals and the cognitive selection of requested effects.

```text
EXTERNAL SENSOR
-> HC-owned interface/transduction boundary
-> internal evidence
-> internal cognition
-> internal action selection
-> HC-owned effect interface
-> EXTERNAL ACTUATOR
```

A motor controller may stabilize a joint. A camera may preprocess pixels. A network gateway may retransmit packets. Supplied peripheral capability must be declared so that it is not miscredited as HC-learned cognition.

---

## 2. External computational services are peripherals unless incorporated into the organ

A model server, accelerator, search service, database, cloud process, or remote inference engine can be useful without becoming the place where the synthetic organism's cognition resides.

Two cases should be explicit.

### HC-internal substrate/service

A component is part of the cognitive organ when it is architecturally included inside the HC boundary, participates through HC-governed state and routing, and has defined continuity/failure/fallback semantics as part of the brain object.

### External computational peripheral

An external service may perform computation, but its output enters the HC as externally sourced evidence or a bounded service result.

```text
EXTERNAL_COMPUTE_RESULT != INTERNAL_BELIEF
EXTERNAL_MODEL_OUTPUT != ORGANISM_IDENTITY
SERVICE_SUCCESS != COGNITIVE_INCORPORATION
```

The brain remains capable of representing the service as unavailable, wrong, stale, contradictory, or replaceable.

---

## 3. The repository root represents the whole organ

Repository hierarchy is a symbolic engineering representation of the physical/logical cognitive organ.

Top-level systems may represent specialized neural/computational systems such as:

```text
cognition/world modeling
semantics
pragmatics
memory
chronology
attention/salience
metacognition
self-model
social cognition/empathy
affect
sexuality
conation/volition
homeostasis/allostasis
body schema/interoception
sensor integration
kinesis/action
speech/language interfaces
personification/expression
routing/integration
plasticity
fault/maintenance
security/effect boundaries
adaptable I/O
```

The exact final node taxonomy remains a reviewed architecture decision. The important invariant is that the repository should not depend on an unrepresented external cognition layer to make the brain whole.

---

## 4. Complete capacity does not mean universal activation

The generic template should prefer **presence plus lifecycle control** over deleting potentially relevant cognitive systems from different brain builds.

A capability can be present while disabled, dormant, immature, inhibited, degraded, or faulted.

Candidate activation states are defined in `HOMEOSTASIS_ALLOSTASIS_AND_NODE_LIFECYCLE.md`.

This permits a single complete cognitive-organ template to support different developmental stages, embodiments, task profiles, and individual trajectories without treating every unused capability as a missing organ.

Examples:

- a sexuality system may be `PRESENT_DISABLED` or `DORMANT` by default;
- a newly embodied body-schema learner may be `DEVELOPING`;
- an unavailable sensory modality may leave its integration node `DORMANT` or `DEGRADED`;
- a qualified language system may be `ACTIVE` only when relevant;
- a damaged capability may be `FAULTED` while the rest of the organ routes around it.

Presence does not confer maturity, activation, authority, salience, or permission.

---

## 5. The Hyperconnectome fabric is connective tissue, not a homunculus

The architecture may contain an integration/routing fabric at the center of diagrams, but that fabric must not become a little executive agent that performs all real reasoning while specialist nodes act as peripherals.

The preferred interpretation is:

```text
specialized nodes
<-> typed internal fabric
<-> temporary coalitions
<-> specialized nodes
```

The fabric can provide or coordinate:

```text
routing
coalition formation
bandwidth allocation
temporal coordination
state/evidence transport
inhibition and gating
resource arbitration
plasticity eligibility
fault isolation
capability discovery
```

Cognition is performed by the interacting internal systems and coalitions. The fabric enables integration; it does not own all semantic truth, memory, motivation, identity, or executive authority.

---

## 6. Reasoning must terminate inside the HC boundary

A reasoning path may use internal specialist models, memories, simulations, semantic state, external observations, or external service results. The decision-relevant reconciliation must occur inside the HC.

Example:

```text
camera observation
+ proprioception
+ body schema
+ world-model hypotheses
+ memory
+ conative state
+ action constraints
-> internal coalition/reconciliation
-> selected action request
```

Not:

```text
HC receives inputs
-> sends the real problem to an opaque external mind
-> copies back the answer
-> calls that HC cognition
```

An external service can contribute evidence, but the brain must remain responsible for provenance, reconciliation, uncertainty, authority, and final internal state transition.

---

## 7. Body independence is a template goal

The same generic HC architecture should be able to inhabit materially different bodies by changing interface mappings, calibration, body schema, and learned sensorimotor models rather than replacing the cognitive organ's fundamental architecture.

Possible embodiments include:

```text
humanoid robot
wheeled or tracked machine
stationary embodied system
distributed sensor network
remote actuator network
vehicle
a synthetic body with modalities not present in humans
```

This is a design target, not a claim that arbitrary body transfer is solved.

### Implication

The HC should distinguish:

```text
BRAIN_CAPABILITY
BODY_INTERFACE
BODY_SCHEMA
CURRENT_BODY_CALIBRATION
```

A body-specific skill may require relearning even when higher-order semantic or autobiographical state persists.

---

## 8. Internal databases and memory stores are parts of the organ only through cognitive contracts

A database can store brain state, but raw database existence does not itself make the database contents active cognition.

The HC boundary should define:

```text
what is durable state
what is current active state
what is a projection/cache
what is retrieved evidence
what is admitted memory
what can be rewritten
what requires successor history
what is externally imported
```

This preserves the distinction between physical storage and cognitively incorporated state.

---

## 9. Whole-brain degradation must be graceful where possible

A self-contained organ must expect component failure.

No single optional specialist, external service, accelerator, sensor, or high-degree integration path should be able to erase the entire cognitive system unless it truly represents an unavoidable physical single point of failure.

The architecture should make such unavoidable single points explicit and minimize them through redundancy where feasible.

---

## 10. What this requirement does not claim

The self-contained-organ requirement does **not** establish that:

- the current HC repository is complete;
- the complete architecture is technologically buildable today;
- a stored brain state is conscious;
- persistence proves uninterrupted subjective experience;
- an installed HC object automatically constitutes a moral person;
- every listed capability is required to be active in every synthetic organism;
- biological neural anatomy must be copied;
- external connectivity is prohibited.

It defines the intended architectural boundary: **external systems may extend the body and supply services, but they do not fill an unmodeled hole where essential cognition is supposed to be.**

---

## Architecture qualification questions

For every proposed HC subsystem or dependency, ask:

1. If this dependency disappears, what cognitive function is lost?
2. Is that lost function represented somewhere inside the HC?
3. Is the external dependency merely a sensor/actuator/service, or is it secretly doing essential cognition?
4. Can the HC represent that external output as uncertain evidence rather than truth?
5. Does a different body require a new brain architecture or only new interface/schema/calibration learning?
6. Is an unused capacity absent, or merely present but inactive?
7. Does a central fabric coordinate cognition or monopolize it?
8. Can a specialist fail without destroying unrelated cognitive functions?

A proposal that cannot answer these questions has not yet established a self-contained cognitive-organ boundary.