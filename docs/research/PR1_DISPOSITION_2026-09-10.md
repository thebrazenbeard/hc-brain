# PR #1 Selective Disposition — 2026-09-10

Status: WARDEN SOURCE-DISPOSITION RECORD

Pull request: `#1` (`thebrazenbeard-patch-1`)

Observed PR head: `66e20f648bac71c9de980e8895a5894377fca385`

Purpose: record what can and cannot be promoted from the two remaining PR #1 delta files without merging the stale feeder wholesale.

## Current disposition

PR #1 remains **OPEN / NOT MERGED**.

Its remaining delta contains:

- `Noöplex HC-1 and HC-2 Architectures.pdf` — blob `a1b9f47f028d4253b563d3f01f4589364949ebc4`, 49,872 bytes;
- `synthetics_physiology_v_2_nooplex_embodiment_annex.md` — blob `0a717c9c282d787b40c9b20ccf1c1a6bd8f798fc`.

The branch itself remains preserved as source history.

## Markdown annex disposition

The annex is explicitly a **Wreckforge in-universe technical monograph**, not a neutral HC architecture contract. It contains setting-specific claims about Synthetics, Voidcore/Cerebri history, fixed embodiment/anatomical choices, synthetic endocrine packaging, hydration/MedBay procedures, fixed performance numbers, and specific HC-1/HC-2 physical assumptions.

Disposition:

`SOURCE_VALUE = HIGH_FOR_WRECKFORGE_OR_EMBODIMENT_RESEARCH`

`GENERIC_HC_CANONICAL_PROMOTION = REJECT_WHOLESALE`

`SELECTIVE_TRANSFER = ONLY_AFTER_ABSTRACTION_AND_INDEPENDENT_EVIDENCE_OR_OWNER_DECISION`

The following examples must not be promoted merely because they occur in the source:

- human-shaped/gross anatomical packaging;
- fixed synthetic physiology or hydration schedule;
- fixed strength, power, thermal, endocrine, aging, healing, or metabolic numbers;
- a universal `Limbic Governor` implementation;
- a universal cryogenic HC-2 package;
- the claim that HC-2 degradation makes it "behave as HC-1" as a generation-identity rule;
- Wreckforge organizations, history, legal status, MedBay protocols, or donor/consciousness-transfer lore.

Useful abstractions already represented more safely elsewhere in canonical HC include body-interface calibration, distributed-organ support boundaries, homeostasis/interoceptive evidence, resource/thermal control, specialized-accelerator degradation, generation identity preservation, affect modulation, continuity, and governed recovery. This source may remain provenance or a setting-specific embodiment case, but it is not allowed to override those generic contracts.

## PDF disposition

The PDF is currently classified:

`BINARY_SOURCE_PRESENT = OBSERVED`

`TEXTUAL_CONTENT_REVIEWED_BY_WARDEN = NO`

`CANONICAL_PROMOTION = BLOCKED_PENDING_READABLE_CONTENT_REVIEW`

The GitHub connector exposes its blob identity and bytes but does not provide a directly reviewable textual patch for this binary file. The Warden will not infer its contents from filename, related documents, or project memory and will not call it reviewed.

Until a readable extraction or equivalent authoritative text surface is available, the PDF remains source history on the PR branch only.

## Merge rule

Do not merge PR #1 wholesale.

The markdown annex is setting-specific and conflicts with the repository's identity-neutral, substrate-neutral generic-template role if admitted at root as normative architecture. The PDF remains unreviewed as content. Those two facts are sufficient to block wholesale merge while preserving both source artifacts intact on the feeder branch.

## Current qualification consequence

No architecture PASS, implementation PASS, biological feasibility claim, consciousness-transfer claim, or Wreckforge canon claim is created by this disposition.

`SOURCE_PRESERVED != SOURCE_PROMOTED`

`RELATED_CANONICAL_ABSTRACTION != SOURCE_WHOLESALE_ACCEPTANCE`

`BINARY_PRESENT != BINARY_REVIEWED`

## Next disposition gate

PR #1 may be closed as superseded only after the PDF has a readable evidence surface or the owner explicitly chooses to preserve the still-unreviewed binary solely as historical branch provenance. Until then, keeping the PR open is the conservative source-custody choice.
