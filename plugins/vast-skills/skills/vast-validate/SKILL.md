---
name: vast-validate
description: 'Validate a document that claims VAST shape — a single layer (e.g. a Vision doc) or a full V/A/S/T doc — checking that each layer is what it claims to be, scope is consistent across layers, and framework discipline holds. Detects layer drift (Vision written as a feature/deadline list, Architecture written as a project plan), mixed scope (company-level Vision + product-UI Architecture), missing Vision falsification triggers, incomplete composition frameworks, and Challenge Flow violations. Use when reviewing a Vision/Architecture/Strategy/Tactics doc, stress-testing whether a doc respects VAST layer purity, or auditing a framework artifact before adoption. Triggers: "validate this VAST doc", "is this layer pure", "check VAST shape", "проверь VAST", "does this Vision hold up", "validate Architecture doc".'
---

# vast-validate

## When to use

Invoke when you have a document that claims VAST shape — one layer (a standalone Vision, Architecture, Strategy, or Tactics doc) or a full V/A/S/T set — and want to verify it respects the framework: each layer contains content appropriate to its level, the doc operates at one consistent scope, and framework discipline (Vision falsification, composition completeness, Challenge Flow) holds.

Common triggers:
- "Validate this VAST doc"
- "Is this layer pure?"
- "Check the VAST shape of this"
- "Проверь VAST"
- "Does this Vision hold up?"

This skill is distinct from `vast-okr-audit`: that one audits OKR-shaped docs (Objectives + KRs) for triad conflation; this one validates docs that explicitly claim a VAST layer structure.

## VAST recap (condensed)

A VAST doc names up to four layers, each owning a distinct level of commitment:

| Layer | Owns | Drift looks like |
|---|---|---|
| **Vision** | What experiences we enable, for whom, why — as a falsifiable hypothesis with named revision triggers. | A feature list or roadmap with deadlines (Tactics drift); market positioning swallowing the product (Strategy/scope drift). |
| **Architecture** | The composition framework — skill library, interfaces, invariants, implementations. The structural domains and their guarantees. | A project/task list (Tactics drift); market stance (Vision drift). |
| **Strategy** | Which experiences to compose next — sequencing, customer validation, investment direction *within* the framework. | Concrete deliverables with dates (Tactics drift); redefining the framework (Architecture drift). |
| **Tactics** | Personalized instance delivery — specific compositions for specific users at specific times. | (Tactics is the floor — content rarely drifts *up*, but generic aspiration with no concrete delivery is hollow.) |

Two cross-cutting disciplines: **Vision is a hypothesis with named falsification triggers** (governance.md Vision Falsification Protocol), and **challenge flows down, feedback flows up** (Vision *challenges* Architecture; Strategy *informs*, never overrides; glossary.md Challenge Flow).

For the four layers, the triad, and the invariants/implementations split, see `../../references/vast-essentials.md`. For the four-scope model (company / product / function / WoW) and per-scope identifying signals, see `../../references/layer-definitions.md`. The eight common confusions are in `../../references/anti-patterns.md`. Detailed validation heuristics are in `references/validation-heuristics.md` — read those if any classification is ambiguous.

## Process

For the doc under review:

1. **Identify scope + layers present** — which of company / product / function / WoW does this doc operate at, and which of V/A/S/T are present? (Scope signals: `references/validation-heuristics.md#scope-homogeneity`; the full per-scope signal lists are in `../../references/layer-definitions.md`.)
2. **Run layer purity per present layer** — does each layer's content match its level, or has it drifted up/down? (See `references/validation-heuristics.md#layer-purity`.)
3. **Check scope homogeneity across layers** — do all present layers operate at the *same* scope, or is e.g. a company Vision paired with product-UI Architecture? (See `references/validation-heuristics.md#scope-homogeneity`.)
4. **Check Vision falsification triggers** — if a Vision is present, does it name observable, bounded, owned revision triggers? (Only when Vision present. See `references/validation-heuristics.md#falsification-triggers`.)
5. **Check composition framework completeness** — if the doc is product-scope and has an Architecture, does it contain all four sub-elements and the invariants-vs-implementations split? (Only when product Architecture present; adapt for non-product scopes. See `references/validation-heuristics.md#composition-completeness`.)
6. **Check Challenge Flow respect** — if the doc describes cross-layer interactions, do they follow the rules (Vision challenges, Strategy informs, Architecture self-corrects, Tactics escalates)? (Passes by default if no cross-layer interactions described. See `references/validation-heuristics.md#challenge-flow`.)
7. **Generate report** per Output format below.

## Checks

| # | Check | Heuristic (1-liner) | Detail reference |
|---|---|---|---|
| 1 | Layer purity | Each present layer holds content appropriate to its level. Vision = why/experiences/outcomes (not features/deadlines). Architecture = composition framework / structural domains (not a project list, not market stance). Strategy = investment direction/sequencing. Tactics = concrete delivery. Content belonging to another layer → Fail; mild bleed → Warn. | `references/validation-heuristics.md#layer-purity` (primary); `../../references/anti-patterns.md` (#1 Vision-as-Use-Case, #2 Architecture-by-default) |
| 2 | Scope homogeneity | The doc operates at ONE scope (company / product / function / WoW). Layers at different scopes (e.g. company Vision + product-UI Architecture) → Fail; a single ambiguous layer → Warn. | `references/validation-heuristics.md#scope-homogeneity` (primary); `../../references/layer-definitions.md` (per-scope identifying signals) |
| 3 | Vision falsification triggers | If a Vision is present, it names observable + bounded + owned revision triggers. No triggers at all → Fail; present-but-vague/unowned → Warn. (Skip if no Vision present.) | `references/validation-heuristics.md#falsification-triggers` |
| 4 | Composition framework completeness | If product-scope Architecture is present, it contains all four sub-elements (skill library, interfaces, invariants, implementations) AND splits invariants from implementations. Partial → Warn; absent (Architecture claimed but framework empty/hand-wavy) → Fail. Non-product scopes adapt to org capabilities / process building blocks. (Skip if no Architecture present.) | `references/validation-heuristics.md#composition-completeness` (primary); `../../references/vast-essentials.md` (invariants/implementations split) |
| 5 | Challenge Flow respect | If cross-layer interactions are described, they follow: Vision *challenges* Architecture (only downward challenge right); Strategy *informs* Architecture (never overrides); Architecture self-corrects; Tactics escalates. Violations (esp. Strategy overriding Architecture) → Fail. Passes by default if no cross-layer interactions described. | `references/validation-heuristics.md#challenge-flow` (primary); `../../references/anti-patterns.md` (#8 Strategy challenging Architecture) |

> Check numbers above are stable identifiers, not an execution order. The Process runs scope+layers → purity → scope homogeneity → falsification → composition → Challenge Flow; the report groups findings by severity. Reference checks by **name** (e.g. "Layer purity"), not by number, in the report.

## Output format

Produce a markdown report with this exact structure:

```markdown
# VAST Validation Report — {doc title or filename}

**Scope detected:** company | product | function | WoW | mixed
**Layers present:** {V / A / S / T — which of the four appear}

## ✅ Pass
- {layer or quote} — {check name} — {brief evidence}

## ⚠️ Warn
- {layer or quote} — {check name}: {what's borderline} — {suggested reframe}

## 🚨 Fail
- {layer or quote} — {check name}: {why fails} — {evidence quote} — {suggested fix}

## Summary
{1-3 sentences: overall state, top 1-2 fixes recommended.}
```

If a severity section has no items, write `- (none)` under it — keep all three sections present so report structure is identical across clean and flagged docs. Checks that are skipped (e.g. falsification when no Vision present, composition when no Architecture present) do not appear in the report at all — only checks that actually ran produce Pass/Warn/Fail lines.

## Examples

See:
- `../../examples/04-vast-clean/` — well-formed product-scope V/A/S/T, no findings expected
- `../../examples/05-vast-layer-impure/` — Vision-as-feature-list + Architecture-as-project-plan, expect layer-purity / falsification / composition fails
- `../../examples/06-vast-scope-mixed/` — company-level Vision + product-UI Architecture, expect scope-homogeneity + layer-purity + falsification fails
