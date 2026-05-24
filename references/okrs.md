# VAST and OKRs

A common question when VAST is introduced alongside existing OKR practice: *is VAST replacing OKRs? Are they the same thing? Is VAST a layer above or below OKRs?*

Short answer: **OKRs and VAST are complementary, not overlapping. OKRs are how commitments at each VAST layer are expressed and tracked.** VAST provides structural shape and accountability; OKRs provide measurable commitments within that shape.

## What VAST provides that OKRs don't

- **Priority of commitment.** V → A → S → T describes which layer gets intentionally named and committed first. OKRs don't tell you whether to set Architecture goals before Strategy goals — they treat each layer's goals as independently pursuable.
- **Accountability pattern per layer.** Who is accountable for composition-framework decisions vs Strategy decisions. OKRs assume ownership but don't prescribe the shape.
- **Challenge flow rules.** Who can challenge whom across layers. OKRs don't model cross-layer politics; they model outcome tracking.
- **Delivery vs discovery boundary.** When the framework applies (delivery) and when it doesn't (discovery). OKRs apply to any goal, not just delivery commitments.
- **Composition-framework stewardship.** VAST names the Architecture layer as the composition framework (skill library, interfaces, invariants). OKRs provide no vocabulary for this specific artifact.

## What OKRs provide that VAST doesn't

- **Measurable commitments.** Numeric Key Results that make "we succeeded" or "we missed" unambiguous. VAST doesn't specify how success at each layer is measured.
- **Cascade mechanism.** Company OKRs → function OKRs → team OKRs — a formal structure for alignment and traceability. VAST describes layers but not the cadence of goal-setting within them.
- **Check-in rhythm.** Weekly/biweekly/quarterly review practices. VAST doesn't prescribe check-in cadence.
- **Aspirational vs committed framing.** 0.7-target ambition conventions, stretch goals, graded scoring. Operational practice VAST doesn't address.

## The cascade mapping

OKRs cascade through VAST layers naturally:

| VAST layer | OKR correspondence |
|---|---|
| **Vision** | Company-level OKRs. CEO-owned. Reflect long-term direction as annual/quarterly commitments. "Become the AI-first platform for creator-small-business growth by Q4 2027." |
| **Architecture** | Composition-framework OKRs. CTO-owned. Measure framework evolution. "Reduce per-user composition inference cost 40% Q2." "Ship MCP-compliant skill layer by Q3." "Add N new skills to library with full invariant coverage." |
| **Strategy** | Function-level OKRs. Function leaders own. Cascade from Vision within composition-framework constraints. "Grow AI-assisted support handling rate from 30% to 55% Q3 using the customer-support composition skills." |
| **Tactics** | Team OKRs. Team-owned. Deliver function OKRs through specific composition instances. |

OKRs provide the "what result did we commit to at this layer" — VAST provides the "who decides what at this layer, in what priority."

## Common confusion — the "Strategy" word

VAST and OKRs both use "Strategy" but mean different things:

- **VAST Strategy** = composition selection, sequencing, customer validation, roadmap ownership — *within* composition-framework constraints. The layer name, not a goal type.
- **OKR Strategy** (when the term is used in OKR contexts) = measurable commitment framing for the direction a function is taking. A goal type, not a layer.

In practice: a function leader sets their function's OKRs *because* they are the VAST Strategy layer accountable role. The OKRs are their expression of commitment within VAST Strategy scope.

## Sequencing OKRs through VAST

If VAST is applied at deep composition with full discipline, OKR setting follows the same priority of commitment:

1. **Vision-level OKRs first.** Company sets direction commitments. Until these exist, downstream OKRs are speculative.
2. **Architecture-level OKRs next.** Composition-framework commitments that make Vision achievable. Without Architecture OKRs, Strategy OKRs risk committing to compositions the framework can't support.
3. **Strategy-level OKRs third.** Function leaders commit to outcomes within what the composition framework enables.
4. **Tactics-level OKRs last.** Teams commit to the increments that deliver Strategy OKRs.

At lighter composition depths, the priority still holds but strict temporal sequencing relaxes — all four layers can set OKRs in a given cycle, but the commitments are explicitly anchored to upstream layers' intents.

## Common anti-patterns

- **Skipping Architecture OKRs.** Most common failure: company sets Vision OKRs, function leaders set Strategy OKRs, composition-framework investments get neither explicit commitment nor measurement. Architecture then gets decided by accumulated tactical choices — the exact dysfunction VAST exists to prevent. Prevention: explicitly require Architecture OKRs (even if framed as "framework milestones" or "library-evolution goals") at the same cadence as Strategy OKRs.
- **OKR scoring as VAST compliance check.** OKRs measure outcomes; VAST orders commitments. If OKRs score well but the org is still hitting the architecture-by-default dysfunction, VAST is broken even though OKRs look healthy.
- **Using OKRs to paper over missing VAST accountability.** If Architecture OKRs exist but no-one is accountable for the composition framework at the governance body level, the OKRs are numbers without an owner — they'll drift.

## Relationship to other operating cadences

OKRs are one commitment mechanism. Others exist and coexist:

- **Roadmaps.** Product roadmaps live at VAST Strategy layer. Composition-framework roadmaps live at VAST Architecture layer. OKRs measure progress against roadmap commitments.
- **Sprint / delivery cadence.** Tactics-layer detail. Below OKR granularity in most cases.
- **Strategic planning cycles.** Annual planning often sets Vision OKRs + Architecture investments. Quarterly refinement sets Strategy OKRs. VAST shape holds across these cycles.
- **Reviews** (business, performance). Informational + adjustment vehicles. They check OKR status, surface signals through Challenge Flow, trigger re-decisions when needed.

None of these are VAST. All operate within the VAST shape.

## References

- [`vast.md`](../vast.md) — core framework definition
- [`governance.md`](../governance.md) — accountability per layer is what OKRs are committed against
- [`applicability.md`](../applicability.md) — composition depth affects OKR-setting intensity per layer
