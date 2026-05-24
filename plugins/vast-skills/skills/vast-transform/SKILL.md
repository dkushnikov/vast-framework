---
name: vast-transform
description: 'Transform an abstract or prose description of a project, system, or initiative (NOT yet in VAST shape) into a VAST-shaped draft — extracting the latent Vision (or flagging its absence), mapping the rest to Architecture/Strategy/Tactics, and recommending composition depth. Generative, not analytical: it produces a proposed VAST document, it does not score one. Use when you have raw prose (a pitch, a project brief, a backlog narrative, a strategy memo) and want it reshaped into V/A/S/T, or when someone asks "put this in VAST terms" / "what would this look like as VAST". Triggers: "transform this into VAST", "make this VAST-shaped", "extract the VAST from this", "VAST-ify this", "переведи в VAST", "what is the Vision/Architecture here".'
---

# vast-transform

## When to use

Invoke when you have an abstract or prose description — a pitch, a project brief, a backlog narrative, a strategy memo, a feature list — that is **not yet in VAST shape**, and you want it reshaped into a proposed Vision / Architecture / Strategy / Tactics draft. This skill is **generative**: it produces a VAST-shaped document from prose, extracting the latent Vision and sorting the rest into layers.

Common triggers:
- "Transform this into VAST"
- "Make this VAST-shaped" / "VAST-ify this"
- "What's the Vision / Architecture here?"
- "Put this in VAST terms"
- "Переведи это в VAST"

This skill is distinct from the analytical siblings. `vast-validate` checks a doc that **already claims** VAST shape and emits Pass/Warn/Fail. `vast-okr-audit` audits OKR-shaped docs for triad conflation. `vast-transform` takes prose that makes **no** VAST claim and **produces** the shape. If the input already has V/A/S/T headings and you want it scored, use `vast-validate` instead.

## VAST recap (condensed)

The output sorts prose into four layers, each owning a distinct level of commitment:

| Layer | Owns — what prose content maps here |
|---|---|
| **Vision** | The why / for-whom / enabled-experience. The purpose the work serves, as a falsifiable hypothesis. Look for "we believe", "so that", "for {users} who {pain}". |
| **Architecture** | The structural domains and the composition framework — skill library, interfaces, invariants, implementations. The durable structure work is built *on*. Look for "the system is structured as", "capabilities", "guarantees", "what must always hold". |
| **Strategy** | Investment direction and sequencing — which experiences to compose next, in what order, validated how. Look for "first we'll", "prioritize", "sequence", "invest in", "validate with". |
| **Tactics** | Concrete deliverables — specific compositions for specific users at specific moments. Look for named features, screens, dated artifacts, per-user delivery. |

Two cross-cutting facts the transform respects: **Vision is a committed falsifiable hypothesis** (it needs named revision triggers — flag their absence as a gap, don't fabricate them), and the four layers form a **commitment-priority order** (Vision → Architecture → Strategy → Tactics), not a temporal sequence.

For the four layers, the triad (Outcomes / Use Cases / Outputs), and the invariants/implementations split, see `../../references/vast-essentials.md`. For the four-scope model (company / product / function / WoW) and per-scope identifying signals, see `../../references/layer-definitions.md`. The eight common confusions — which the *produced output* must not exhibit — are in `../../references/anti-patterns.md`. The composition-depth spectrum (deep / medium / light / vocabulary-only) is in the framework's `applicability.md`. Detailed transform heuristics are in `references/transform-heuristics.md` — read those if any extraction or mapping is ambiguous.

## Process

For the prose under transformation:

1. **Identify scope** — company / product / function / WoW. State it explicitly; it determines what each layer should contain and what "good" looks like. (Scope signals: `references/transform-heuristics.md#scope-identification`; the full per-scope signal lists are in `../../references/layer-definitions.md`.)
2. **Extract Vision** — find the why / for-whom / enabled-experience in the prose. If it is genuinely present, lift and tighten it. If it is genuinely **absent** (the prose is all features/deliverables with no stated purpose), **flag the absence** — do not fabricate a confident Vision. Offer a candidate Vision clearly labeled `⚠️ CANDIDATE (confirm)` that the user must confirm. (See `references/transform-heuristics.md#vision-extraction`.)
3. **Map to Architecture / Strategy / Tactics** — sort the remaining prose into layers: structural domains / composition framework → Architecture; investment direction / sequencing → Strategy; concrete deliverables → Tactics. Note thin or empty layers rather than padding them. (See `references/transform-heuristics.md#layer-mapping`.)
4. **Recommend composition depth** — deep / medium / light / vocabulary-only. Match depth to the work's actual AI-substrate engagement and scope; do not force deep where light fits (that is anti-pattern #6) nor claim vocabulary-only where deep is needed (anti-pattern #7). (See `references/transform-heuristics.md#depth-recommendation`.)
5. **Surface gaps** — what's missing for a complete VAST doc: no falsification triggers on the Vision, Architecture with no invariants, no for-whom in the Vision, no named accountable owner, scope ambiguity. (See `references/transform-heuristics.md#gap-surfacing`.)
6. **Emit the proposed VAST doc** per Output format below.

## Heuristics

| # | Heuristic | One-liner | Detail reference |
|---|---|---|---|
| 1 | Scope identification | Match prose against per-scope signals; pick ONE scope (company / product / function / WoW). If the prose mixes altitudes (company ambition + product-feature detail), pick the dominant scope and record the conflict as an open question — don't silently average. | `references/transform-heuristics.md#scope-identification` (primary); `../../references/layer-definitions.md` (per-scope signals) |
| 2 | Vision extraction | Lift why/for-whom/enabled-experience if present. If absent, mark status ABSENT and offer a `⚠️ CANDIDATE (confirm)` Vision derived from the deliverables — never present an inferred Vision as settled fact. Partial why → "partially inferred". | `references/transform-heuristics.md#vision-extraction` (primary); `../../references/anti-patterns.md` (#1 Vision-as-Use-Case, #4 missing falsification triggers) |
| 3 | Layer mapping | Sort prose: structural domains / composition framework → Architecture; investment direction / sequencing → Strategy; concrete deliverables → Tactics. Don't pad a thin layer — note what's needed. Don't promote a feature to Architecture just to fill it. | `references/transform-heuristics.md#layer-mapping` (primary); `../../references/vast-essentials.md` (triad; invariants/implementations) |
| 4 | Depth recommendation | Pick deep / medium / light / vocabulary-only by scope × AI-substrate engagement. One-line reason citing the signal that decided it. Don't force deep on light work (#6) or claim vocabulary-only where deep is needed (#7). | `references/transform-heuristics.md#depth-recommendation` (primary); `../../references/anti-patterns.md` (#6, #7) |
| 5 | Gap surfacing | Enumerate what's missing for a *complete* VAST doc: Vision falsification triggers, Architecture invariants, for-whom, named accountable owner, scope clarity. Gaps are honest absences to report, not things to invent. | `references/transform-heuristics.md#gap-surfacing` (primary); `../../references/anti-patterns.md` (#2 Architecture-by-default, #7 vocabulary-only) |

> Heuristic numbers above are stable identifiers, not an execution order. The Process runs scope → Vision → mapping → depth → gaps. Reference heuristics by **name** (e.g. "Vision extraction") if you annotate the output.

## Output format

Produce a markdown document with this exact structure — a *proposed* VAST doc, not a score:

```markdown
# Proposed VAST — {title} ({scope} scope)

## Vision
{extracted Vision — why / for-whom / enabled-experience. If genuinely absent,
write a single clearly-labeled candidate instead:
"⚠️ CANDIDATE (confirm): {inferred purpose} — derived from the deliverables below;
confirm or replace before use."}

## Architecture
{mapped structural content — domains, composition framework, invariants.
If thin or empty, state what the prose provides and what a complete Architecture
still needs (e.g. "no invariants stated — needs ≥1 quality + ≥1 fallback contract").}

## Strategy
{mapped investment direction / sequencing. If absent, note that no sequencing
logic was stated.}

## Tactics
{mapped concrete deliverables — features, screens, per-user delivery.}

---

## Notes
- **Vision status:** extracted | partially inferred | ABSENT (candidate offered — confirm before use)
- **Composition depth:** deep | medium | light | vocabulary-only — {one-line reason}
- **Gaps surfaced:** {bullets — what's missing for a complete VAST doc}
- **Open questions:** {bullets — what the author must decide}
- **Decisions deferred:** {bullets, if any}
```

Always include **all five Notes fields**. Where a field is empty, write `(none)` — keep every field present so the Notes block is identical in shape across clean and gap-heavy transforms (mirrors the exemplars' empty-state discipline).

The four layer sections always appear, even when a layer is thin or empty — an empty layer is itself a finding (state what's missing), not a section to omit.

## Examples

See:
- `../../examples/07-transform-clean/` — prose with a clear latent Vision + identifiable A/S/T material → clean transform, Vision status "extracted".
- `../../examples/08-transform-no-vision/` — a pure feature/deliverable list with no stated why → A/S/T mapped, Vision status "ABSENT", labeled candidate offered (not fabricated).
- `../../examples/09-transform-mixed-altitude/` — prose mixing company-level ambition with product-feature detail → transform picks a scope, records the altitude conflict as an open question.
