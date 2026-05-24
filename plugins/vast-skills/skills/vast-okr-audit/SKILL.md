---
name: vast-okr-audit
description: "Audit an EXISTING set of OKRs (objectives and key results that are already written) for VAST-triad conflation — objectives that are really Outputs (a project or feature like 'ship the new billing system' dressed up as an outcome), key results that fuse two layers (a strategy-level Use Case and a measurable Output crammed into one KR), and scope inconsistency (company-level and team-level objectives in the same set). Use this skill WHENEVER someone hands you OKRs — freshly drafted, in-progress, or finalized — and wants them checked, sanity-checked, sense-checked, reviewed for structure, or asks whether the objectives are genuine outcomes versus relabeled projects, whether the set is 'clean', or whether the objectives and key results sit at the right level — EVEN IF they never say 'VAST', 'conflation', or 'audit'. Reviewing OKR structure by hand is exactly what this skill does better than ad-hoc reading: it applies fixed structural heuristics and returns a per-OKR Pass/Warn/Fail report, so reach for it rather than eyeballing the set yourself. Triggers include: 'are these OKRs structured right', 'do our objectives trace to real outcomes', 'is this a clean OKR set', 'our KRs feel half-strategy half-task-list', 'sanity-check our OKRs', 'check our objectives and key results', 'проверь OKR на конфляцию'. This skill checks the STRUCTURE of OKRs that already exist; it does not generate brand-new OKRs from a blank page, judge whether targets are ambitious or stretchy enough, or evaluate non-OKR documents — those are separate tasks."
---

# vast-okr-audit

## When to use

Invoke when you have an OKR doc (Objectives + Key Results) and want to verify whether it respects the VAST triad: **Objectives ≈ Outcomes (Architecture layer), Key Results ≈ Use Cases (Strategy) + Outputs (Tactics)**.

Common triggers:
- "Audit these OKRs"
- "Check OKR conflation"
- "Are these OKRs VAST-clean?"
- "Проверь OKR на VAST"

## VAST recap (condensed)

OKRs span three VAST layers, often conflated:

| OKR element | VAST layer | What it should answer |
|---|---|---|
| **Objective** | Architecture (Outcomes) | What domain we're growing. What system property changes. |
| **Key Result (qualitative)** | Strategy (Use Cases) | Where/how we invest. Which compositions we sequence. |
| **Key Result (quantitative output)** | Tactics (Outputs) | What we concretely produce. Measurable artifact. |

**Conflation = Objective stated as Output** ("Ship X feature" instead of "Grow domain Y"); or **KRs mixing layers in unstructured way**; or **company-level mixed with team-level scope**.

For the triad and four-layer essentials, see `../../references/vast-essentials.md`. The OKR-conflation thesis is canonically in the framework's `standard-framework.md` ("OKRs conflate three levels"); detailed classification heuristics are in `references/okr-conflation-heuristics.md`. Read those if any classification is ambiguous.

## Process

For each Objective + KR set:

1. **Identify scope** — company / function / team. If unclear or inconsistent within the doc, flag as scope-mixed. (Scope signals: `references/okr-conflation-heuristics.md#scope-detection`.)
2. **Classify each Objective** — Outcome? Output? (See `references/okr-conflation-heuristics.md#objective-classification`.)
3. **Classify each KR** — Use Case (Strategy), Output (Tactics), Mixed (both → Fail), or neither (purely aspirational → Warn)?
4. **Detect cross-scope mixing** — does any OKR reference a different scope than declared?
5. **Generate report** per Output format below.

## Checks

| # | Check | Heuristic (1-liner) | Detail reference |
|---|---|---|---|
| 1 | Objective is Outcome, not Output | Objective phrased as system-property change ("Grow X to Y%"), not as deliverable ("Ship X") | `references/okr-conflation-heuristics.md#objective-classification` |
| 2 | KRs split cleanly into Use Cases + Outputs | Each KR is either an investment direction (qualitative) or a measurable artifact (quantitative). Mixed KRs (both) → Fail; KRs that are neither (purely aspirational) → Warn. | `references/okr-conflation-heuristics.md#kr-classification` |
| 3 | Scope consistency | All Objectives + KRs operate at one scope (company / function / team). Mixed scope flagged. | `references/okr-conflation-heuristics.md#scope-detection` (primary); `../../references/layer-definitions.md` (full VAST scope model) |
| 4 | Objective traces to a domain | The Objective's domain is identifiable. If the Objective could fit any domain, it's too vague — likely an Output. | `references/okr-conflation-heuristics.md#domain-trace` |
| 5 | KRs don't span multiple Objectives | Each KR belongs to exactly one Objective. Cross-cutting KRs may indicate Architecture leakage. | `references/okr-conflation-heuristics.md#kr-uniqueness` |

> Check numbers above are stable identifiers, not an execution order. The Process runs scope → objective → KR → cross-scope; the report groups findings by severity. Reference checks by **name** (e.g. "Objective is Outcome"), not by number, in the report.

## Output format

Produce a markdown report with this exact structure:

```markdown
# OKR Audit Report — {doc title or filename}

**Scope detected:** company | function | team | mixed
**OKRs reviewed:** {N Objectives, M Key Results}

## ✅ Pass
- {OKR ID or quote} — {check name} — {brief evidence}

## ⚠️ Warn
- {OKR ID or quote} — {check name}: {what's borderline} — {suggested reframe}

## 🚨 Fail
- {OKR ID or quote} — {check name}: {why fails} — {evidence quote} — {suggested fix}

## Summary
{1-3 sentences: overall state, top 1-2 fixes recommended.}
```

If a severity section has no items, write `- (none)` under it — keep all three sections present so report structure is identical across clean and flagged docs.

## Examples

See:
- `../../examples/01-okrs-clean/` — well-formed OKRs, no findings expected
- `../../examples/02-okrs-conflated/` — Objective-as-Output, expect 2-3 fails
- `../../examples/03-okrs-mixed-scope/` — scope inconsistency, expect scope flag
