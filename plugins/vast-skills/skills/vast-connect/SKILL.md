---
name: vast-connect
description: 'Verify that a child VAST doc genuinely cascades from its parent — that a product VAST nested under a company VAST (or a component VAST under a product VAST) is actually VAST-connected, not two unrelated docs wearing the same vocabulary. Checks scope step-down (child one recursion level narrower than parent), Vision lineage (child Vision refines / serves a parent Strategy use-case or Architecture domain), invariant inheritance (the core Matryoshka condition — child Architecture operates WITHIN parent invariants, never violates one), cross-doc Challenge Flow (child informs parent upward, parent constrains child downward — no inversions), and Strategy alignment (child invests with, not against, the parent direction). Use this WHENEVER someone has TWO VAST docs in a parent/child or nested relationship and wants to know whether they actually fit together, cascade, or cohere — EVEN IF they never say "VAST" or "Matryoshka". Tracing whether a child honors a parent invariant is exactly what this skill does better than reading both docs side by side, so reach for it. Triggers: "are these two VAST docs connected", "does this child cascade from the parent", "check the Matryoshka", "is this product VAST nested correctly", "validate the parent-child VAST link", "проверь связь VAST", "do these nest". Needs two docs — for a single doc use vast-validate.'
---

# vast-connect

## When to use

Invoke when you have **two** VAST docs in a parent→child relationship — a company VAST and a product VAST nested under it, a product VAST and a component/function VAST under it, or any outer→inner pair — and you want to verify the child genuinely *cascades* from the parent. The question this skill answers is not "is each doc well-formed?" but "are these two docs **VAST-connected** — a real Matryoshka — or are they two unrelated docs that happen to share the vocabulary?"

Common triggers:
- "Are these two VAST docs connected?"
- "Does this child cascade from the parent?"
- "Check the Matryoshka" / "do these nest correctly?"
- "Validate the parent-child VAST link"
- "Проверь связь между этими VAST"

This skill assumes **each doc is individually well-formed**. It checks the *connection*, not the internal purity of either doc. If you suspect a doc is internally broken (layer drift, mixed scope, no falsification triggers), run `vast-validate` on each doc first — this skill may recommend that, but its own job is the relationship between the two. It is distinct from `vast-validate` (single-doc layer purity), `vast-okr-audit` (OKR triad conflation), and `vast-transform` (generative — prose → VAST shape).

## VAST recap (condensed)

VAST is **recursive** (vast.md "Matryoshka"; governance.md "Recursion"): the four-layer V/A/S/T shape reappears at nested scopes — company contains products, a product contains components/functions, each with its own local V/A/S/T. A nesting is sound only when the inner doc operates *within* the outer one:

| Relationship rule | What it means | Source |
|---|---|---|
| **Scope steps down** | The child is one recursion level narrower than the parent (company→product, product→component/function). Not same scope, not broader. | layer-definitions.md (4-scope model) |
| **Vision descends** | The child Vision is a *refinement/instance* of the parent — it serves one of the parent's Strategy use-cases or advances a parent Architecture domain. It does not contradict the parent Vision. | vast.md "Matryoshka" |
| **Invariants inherit (Matryoshka core)** | The child Architecture operates **within the parent's Architecture invariants** and must not violate one. "Working Matryoshka = validated top-level framework + child V/A/S/T operating within top-level invariants. The test: does the component commit to the top-level invariants?" | vast.md "Matryoshka"; governance.md |
| **Challenge flows down, feedback flows up** | Across docs: child *informs* parent upward (signals, feedback); parent *constrains* child downward. No inversions — child does not dictate to parent; parent Tactics does not reach into child Architecture. | glossary.md / vast.md "Challenge Flow" |
| **Strategy aligns** | The child's Strategy advances (does not contradict) the parent's Strategy/Architecture priorities. | vast.md; glossary.md |

The load-bearing idea is the **Matryoshka condition**: a working nesting requires the child to respect the parent's validated top-level invariants. *False Matryoshka* delegates autonomy without that respect — the child invents its own invariants, interfaces drift, the relationship is nominal only.

For the four layers, the triad, and the invariants/implementations split, see `../../references/vast-essentials.md`. For the four-scope model (company / product / function / WoW) and per-scope identifying signals — used to confirm the step-down — see `../../references/layer-definitions.md`. The eight common confusions are in `../../references/anti-patterns.md` (#8 Challenge-Flow inversion is directly relevant cross-doc). Detailed connection heuristics are in `references/connection-heuristics.md` — read those if any classification is ambiguous.

## Process

Given the two docs:

1. **Identify each doc's scope + layers** — for the parent and the child separately, which of company / product / function / WoW does it operate at, and which of V/A/S/T are present? (Scope signals: `../../references/layer-definitions.md`.)
2. **Confirm parent/child direction** — establish which doc is the broader (parent) and which is the narrower (child). The relationship is **parent→child confirmed** when one is unambiguously broader; **direction-unclear** when both read at the same scope (can't tell which contains which); **not-nested** when neither contains the other (e.g. two sibling products with no containment). Report this as the `Relationship` line. If direction is unclear or not-nested, the downstream checks still run but their findings are framed by that ambiguity. (See `references/connection-heuristics.md#scope-step-down`.)
3. **Scope step-down** — confirm the child is exactly one recursion level down from the parent. Same-or-broader child, or a skipped level with nothing bridging (company→team with no product/function between) → flag. (See `references/connection-heuristics.md#scope-step-down`.)
4. **Vision lineage** — confirm the child Vision refines/instantiates the parent — serves a parent Strategy use-case or advances a parent Architecture domain. Unrelated or contradicting child Vision → flag. (See `references/connection-heuristics.md#vision-lineage`.)
5. **Invariant inheritance (Matryoshka)** — confirm every child Architecture choice operates within the parent's Architecture invariants. Any child choice that breaks a parent invariant → Fail. This is the core Matryoshka condition. (See `references/connection-heuristics.md#invariant-inheritance`.)
6. **Cross-doc Challenge Flow** — confirm child informs parent upward and parent constrains child downward; flag inversions (child dictating to parent; parent Tactics reaching into child Architecture). (See `references/connection-heuristics.md#cross-doc-challenge-flow`.)
7. **Strategy alignment** — confirm the child's Strategy advances the parent's stated direction; flag a child investing against it. (See `references/connection-heuristics.md#strategy-alignment`.)
8. **Generate report** per Output format below.

## Checks

| # | Check | Heuristic (1-liner) | Detail reference |
|---|---|---|---|
| 1 | Scope step-down | Child operates one recursion level narrower than parent (company→product, product→component/function). Same-or-broader child, or a skipped level with no bridging layer → Fail; a single ambiguous-scope layer that could read as either level → Warn. | `references/connection-heuristics.md#scope-step-down` (primary); `../../references/layer-definitions.md` (per-scope signals) |
| 2 | Vision lineage | Child Vision is a refinement/instance of the parent — serves a named parent Strategy use-case or advances a parent Architecture domain. Unrelated to or contradicting the parent Vision → Fail; plausibly-related but no explicit thread to a parent use-case/domain → Warn. | `references/connection-heuristics.md#vision-lineage` (primary) |
| 3 | Invariant inheritance | Child Architecture operates WITHIN parent Architecture invariants — violates none. This is the core Matryoshka condition (working Matryoshka = child respects validated top-level invariants). Any child choice that breaks a parent invariant → Fail; a child choice that strains/under-specifies against an invariant without an explicit reconciliation → Warn. | `references/connection-heuristics.md#invariant-inheritance` (primary); `../../references/vast-essentials.md` (invariants/implementations split) |
| 4 | Cross-doc Challenge Flow | Child *informs* parent upward (signals, feedback); parent *constrains* child downward. Inversions — child dictating a change to the parent's layers, or parent Tactics reaching into child Architecture — → Fail; ambiguous direction (interaction described but unclear who constrains whom) → Warn. Passes by default if no cross-doc interactions are described. | `references/connection-heuristics.md#cross-doc-challenge-flow` (primary); `../../references/anti-patterns.md` (#8 Challenge-Flow inversion) |
| 5 | Strategy alignment | Child Strategy advances (does not contradict) the parent's Strategy/Architecture priorities. A child investing directly against the parent's stated direction → Fail; a child whose sequencing is merely orthogonal / unjustified against the parent priorities → Warn. (Skip if either doc lacks a Strategy layer.) | `references/connection-heuristics.md#strategy-alignment` (primary) |

> Check numbers above are stable identifiers, not an execution order. The Process runs scope+layers → direction → step-down → Vision lineage → invariant inheritance → cross-doc Challenge Flow → Strategy alignment; the report groups findings by severity. Reference checks by **name** (e.g. "Invariant inheritance"), not by number, in the report.

## Output format

Produce a markdown report with this exact structure:

```markdown
# VAST Connection Report — {parent title} → {child title}

**Parent:** {parent title} ({detected scope})
**Child:** {child title} ({detected scope})
**Relationship:** parent→child confirmed | direction-unclear | not-nested — {one-line basis}

## ✅ Pass
- {check name} — {brief evidence of the connection holding}

## ⚠️ Warn
- {check name}: {what's borderline} — {suggested tightening}

## 🚨 Fail
- {check name}: {why the connection breaks} — {evidence quote from each doc} — {suggested fix}

## Summary
{1-3 sentences: is the pair genuinely VAST-connected? top 1-2 fixes if not.}
```

If a severity section has no items, write `- (none)` under it — keep all three sections present so report structure is identical across connected and broken pairs. Checks that are skipped (e.g. Strategy alignment when either doc has no Strategy layer) do not appear in the report at all — only checks that actually ran produce Pass/Warn/Fail lines.

When the `Relationship` line is **direction-unclear** or **not-nested**, the report still runs the remaining checks but frames them against that finding (e.g. scope step-down will itself Fail, and downward-cascade checks note that direction could not be confirmed). State the connection verdict honestly in the Summary rather than forcing a clean Pass.

## Examples

See:
- `../../examples/10-connect-clean/` — company parent + product child that cascades cleanly (child Vision serves a parent use-case, child Architecture respects parent invariants, scope steps down). Two input docs (`parent.md` + `child.md`); all checks pass.
- `../../examples/11-connect-invariant-violation/` — child whose Architecture ships data cross-region while the parent invariant says all user data stays in-region. Invariant-inheritance Fail.
- `../../examples/12-connect-scope-skip-or-drift/` — child Vision unrelated to / contradicting the parent (Vision-lineage Fail) plus a child pitched at the same scope as the parent (scope-step-down Fail).
