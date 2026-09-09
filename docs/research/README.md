# Runtime Research Index

**Status:** independent research package supporting PR #3  
**Research date:** 2026-09-09  
**Consensus plugin:** not used

This directory separates evidence from architecture inference.

## Files

- `INDEPENDENT_RUNTIME_RESEARCH_2026-09-09.md` — synthesis of neuroscience and computing findings relevant to the Noöplex runtime.
- `RESEARCH_CLAIM_LEDGER.md` — claim-by-claim evidence status and the design implication drawn from each source family.
- `REFERENCES_2026-09-09.md` — peer-reviewed reference list used for this pass.
- `../../specs/HYPERCONNECTOME_RESEARCH_CONSTRAINTS_V0_1.yaml` — machine-readable constraints derived from the research.

## Evidence discipline

Human neuroscience is used as a source of functional mechanisms, constraints, and falsifiable analogies. Human anatomy is **not** copied automatically into the Noöplex.

In particular:

```text
NOOPLEX_HAS_HEMISPHERES = false
HUMAN_ANATOMICAL_LOCALIZATION != NOOPLEX_TOPOLOGY_REQUIREMENT
```

The Noöplex is a hyperconnectome architecture. It has no left/right cerebral hemispheres as an organizing primitive. Human findings that happen to be lateralized may inform hypotheses about specialization, connectivity, timing, dissociation, or computational role, but their hemispheric packaging is not inherited.

## Research-to-design boundary

A cited biological mechanism can support statements such as:

- multiple plasticity timescales are useful;
- interoception participates in affect and regulation;
- structural and functional connectivity should not be conflated;
- distributed coordination can coexist with specialization;
- higher-order interactions may matter;
- stable function can survive representational drift.

It does **not** by itself prove that the Noöplex implementation is correct, conscious, person-like, or technologically realizable at full scale.
