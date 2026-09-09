# Index-Lineage Minimal Probes — 2026-09-09

Status: OBSERVED LOCAL VALIDATION / RESEARCH PROVENANCE

## Purpose

Test the arithmetic/index-space claims behind two source-specific static findings without running the full research pipelines or requiring their external datasets/dependencies.

These are deterministic minimal probes of index semantics, not reproductions of the published experiments.

## Probe 1 — HADA appended-test position

The inspected HADA fold stacks `n-1` training rows followed by the one held-out source row.

For `n = 150`:

```text
train length = 149
expected appended test local index = 149
code expression = (train_length - 2) + testingSubject
with testingSubject = 1 -> 148
```

Local probe output:

```text
HADA (149, 148, 149, False)
```

**OBSERVED:** the inspected arithmetic selects local position 148 while the appended test row occupies 149 under ordinary zero-based stacking.

This strengthens the static code finding in `BASIRA_HADA_TRANSDUCTIVE_EVALUATION_AND_POSITIONAL_TRACE_2026-09-09.md`.

It still does not quantify the downstream effect on the paper's reported metrics or establish which exact historical code/data revision produced the paper results.

## Probe 2 — BGSR filtered LR versus unfiltered HR positions

A six-entity toy identity list was used:

```text
original = [0, 1, 2, 3, 4, 5]
held out = 2
filtered LR identities = [0, 1, 3, 4, 5]
```

If a downstream routine uses the filtered LR local positions directly against the unfiltered HR list, the mapping is:

```text
local 0 -> filtered LR entity 0 -> direct HR entity 0   MATCH
local 1 -> filtered LR entity 1 -> direct HR entity 1   MATCH
local 2 -> filtered LR entity 3 -> direct HR entity 2   MISMATCH
local 3 -> filtered LR entity 4 -> direct HR entity 3   MISMATCH
local 4 -> filtered LR entity 5 -> direct HR entity 4   MISMATCH
```

**OBSERVED generic result:** deleting an interior entity shifts every later local position. Raw local-position reuse against an unfiltered related view misbinds those later entities.

**Source-specific connection:** the inspected BGSR demo filters low-resolution training data for leave-one-out evaluation while passing the full high-resolution feature matrix into the prediction routine, and the inspected prediction routine uses selected local neighbor positions directly against that HR array.

**INFERRED runtime consequence:** if a selected local neighbor lies at or beyond the removed position, direct positional lookup can bind it to a different original subject; at the removed position itself the unfiltered HR array refers to the held-out subject. The exact frequency and quantitative effect require instrumented execution of the full BGSR pipeline.

## Qualification outcome

Tested capability: deterministic reproduction of the local-index-shift and appended-test arithmetic claims.

Outcome: **PASS** for the narrow arithmetic/index-semantics probe.

This PASS does not qualify BGSR, HADA, or HC behavior. It only demonstrates the index mechanics used by the source-specific hypotheses.

## Canonical HC relevance

The probe strengthens the need for:

`POSITIONAL_INDEX != STABLE_ENTITY_ID`

`FILTERED_INDEX != ORIGINAL_INDEX`

`INTENDED_TEST_ROLE != VERIFIED_LOCAL_POSITION`

and the negative tests in:

- `docs/architecture/REFERENCE_IDENTITY_AND_INDEX_LINEAGE.md`
- `specs/HC_REFERENCE_IDENTITY_INDEX_LINEAGE_V1.yaml`

A future implementation-level HC conformance harness should inject stable IDs into equivalent filtering/reordering paths and fail closed when cross-view binding cannot be proven.
