# vast-skills

Claude Code plugin operationalizing the [VAST framework](https://github.com/dkushnikov/vast-framework) against real docs.

## What ships

Five skills — three analytical (score/check an existing doc) and two generative (produce a doc):

- **vast-okr-audit** — Detects OKR conflation: Objectives mixing Outcomes with Outputs, KRs spanning multiple VAST layers, scope inconsistency. Use when reviewing OKR drafts or auditing existing OKR sets. _(analytical)_
- **vast-validate** — Validates a doc that already claims VAST shape: layer purity, Vision falsification triggers, Architecture invariants, scope consistency. Emits Pass / Warn / Fail per check. _(analytical)_
- **vast-connect** — Verifies a nested parent→child VAST pair genuinely cascades (Matryoshka): scope step-down, Vision lineage, invariant inheritance, cross-doc Challenge Flow, Strategy alignment. _(analytical)_
- **vast-transform** — Reshapes existing prose (a pitch, brief, backlog narrative) into a proposed VAST doc — extracting the latent Vision (or flagging its absence) and sorting the rest into A/S/T. _(generative)_
- **vast-draft** — Scaffolds a NEW VAST doc from a minimal seed (a scope + a sentence or two), guiding the author top-down V→A→S→T with guiding questions + what-good-looks-like + fillable stubs. Where the seed is silent it gives the question, not an invented answer. _(generative)_

## Install

Plugin lives co-located in the `vast-framework` repo. From a Claude Code session:

1. Clone `vast-framework`: `git clone https://github.com/dkushnikov/vast-framework.git`
2. Add the plugin directory to Claude Code per [plugin install docs](https://docs.anthropic.com/en/docs/claude-code/plugins)
3. Verify: list loaded plugins, confirm `vast-skills` appears

## Use

Invoke any skill by naming intent in prose. Example:

> "Audit these OKRs against VAST conflation patterns" → triggers `vast-okr-audit`

Output: structured markdown report (Pass / Warn / Fail per check + Summary).

Worked example — given an Objective phrased as a deliverable:

```
## Objective 1: Ship the new authentication service
- KR1.1: Launch SSO integration with Okta
- KR1.3: Reduce auth-related incidents by 50%
```

`vast-okr-audit` flags:

> 🚨 **Objective 1** — Output, not Outcome ("Ship X" = deliverable). Reframe to the underlying Outcome: "Reduce auth fragmentation across services." (Note: KR1.3 already hints at the real Outcome.)

See `examples/` for 15 full input → expected-output pairs across the five skills (numbered 01-15): okr-audit (01-03), vast-validate (04-06), vast-transform (07-09), vast-connect (10-12), vast-draft (13-15).

## Reference

Plugin uses condensed extracts from framework canonical docs (version-pinned). See `references/version-pinning.md` for details.

## Status

Full suite — all five skills ship (`vast-okr-audit`, `vast-validate`, `vast-transform`, `vast-connect`, `vast-draft`).

## Changelog

### V0.2 (2026-05-23)
- Suite completed — added `vast-validate`, `vast-transform`, `vast-connect`, `vast-draft`
- `vast-validate` — single-doc layer-purity validation (Pass / Warn / Fail)
- `vast-transform` — generative: reshapes prose into a proposed VAST doc, flags absent Vision rather than fabricating it
- `vast-connect` — verifies parent→child cascade integrity (Matryoshka condition)
- `vast-draft` — generative: scaffolds a new VAST doc from a seed; gives the question, not an invented answer, where the seed is silent
- 12 new examples (04-15), 3 per new skill

### V0.1 (2026-05-21)
- Initial release
- `vast-okr-audit` skill — detects Objective-as-Output, KR layer mixing, scope inconsistency
- 3 verified examples (clean / conflated / mixed-scope), validated via fresh-context skill runs
- Shared references: vast-essentials, layer-definitions, anti-patterns, version-pinning

### Backlog (from fresh-context verification of all 5 skills)

okr-audit:
- Add check for the all-Outputs / no-Use-Case degenerate case (OKRs collapsing to pure output lists — the most common real-world conflation)
- Clarify the Mixed-KR threshold for "direction + non-quantified activity"
- Severity rubric for scope-mixing findings; classification path for Architecture-shaped KRs

validate:
- When a layer is layer-*pure* but scope-*wrong*, specify whether the finding lands under layer-purity or scope-homogeneity (avoid ambiguous attribution)
- Strategy Tactics-drift threshold should key on absence of investment-logic, not presence of dates
- De-dup guidance when layer-purity and scope-homogeneity fire on the same layer

transform:
- Make explicit that non-AI product-scope work collapses toward light depth (no substrate to govern)
- Bucket for cross-layer tensions surfaced during mapping (Architecture-vs-Strategy) → Open questions
- Sharpen the "promote latent invariants" vs "don't pad Architecture" boundary

connect:
- Distinguish silent invariant-violation (Invariant-inheritance Fail only) from explicit override (Challenge-Flow Fail) to prevent double-counting across runs

draft:
- Guiding-question examples must be a menu of alternatives, never a single lean-in answer
- Show a partial-Answer shape in the output template (seed fills some of a layer, leaves the rest as questions)
