# Distributed Arbitration

Status: template architecture.

## Purpose

Distributed arbitration coordinates competing HC subsystem outputs without installing a permanent executive homunculus. Arbitration is a family of bounded decision processes operating over different scopes, timescales, and consequence classes.

## Arbitration domains

Separate arbitration processes may govern perceptual hypotheses, semantic/pragmatic interpretations, attention and compute allocation, memory admission and consolidation, conative/action trade-offs, response/presentation candidates, plasticity eligibility, correction propagation, body-interface and motor candidates, and safety/action authorization.

No single arbitration result is automatically authoritative outside its scope.

## Decision frame

A bounded arbitration frame should identify decision scope, candidate set, evidence/state snapshot or digest, active concerns/constraints, uncertainty and unresolved conflict, resource/time budget, selection basis, selected outcome when one is required, losing candidates that remain materially relevant, downstream effects, and provenance.

`SELECTED != TRUE`

`SELECTED != PERMITTED`

`LOSING_CANDIDATE != DELETED_STATE`

## Multi-perspective integration

When multiple subsystems produce incompatible but individually coherent perspectives, preserve them long enough to determine whether they are mutually exclusive hypotheses, different scopes, different time horizons, epistemic versus conative judgments, independent concerns that require trade-off, or artifacts of stale/incompatible state.

Arbitration should not manufacture agreement merely to simplify output.

## Resource-bounded choice

The HC cannot deliberate indefinitely. If a decision is required before uncertainty is fully resolved, the system may select an acceptable bounded action while retaining unresolved epistemic state.

`UNCERTAINTY_PRESERVED + ACTION_SELECTED`

## Snapshot-bound decisions

Material decisions should be traceable to the state/evidence cut on which they were made. A later change in memory, body state, sensor reliability, conation, or authority may invalidate the decision without rewriting the fact that it was reasonable under the prior snapshot.

## Authority separation

Routing, recommendation, salience, predicted utility, and majority subsystem support do not themselves create action authority. Consequence-bearing effects pass through the appropriate action gateway.

## Learning from arbitration

Outcomes may update learned arbitration policies, but durable change must flow through plasticity governance. Repetition alone does not authorize a temporary arbitration bias to become a permanent identity or value.

## Failure modes

Relevant failures include universal executive bottlenecks, one scalar silently combining truth/desire/safety/salience, premature consensus, erased losing motives or interpretations, stale snapshots, recommendation interpreted as permission, and learned arbitration policy contaminating evidence confidence.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review.