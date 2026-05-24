# VAST Layer Handoffs

The V → A → S → T cascade is only valid if each layer hands the next what that layer needs in order to commit. These handoffs are **operational expressions of the [Kernel](kernel.md) rules** — not a new class of invariants, but the concrete cash-out of *commit by priority* (Principle 2) and *Architecture explicit before Strategy commits* (a Kernel rule) at every boundary. The *content* of each payload varies by instance and scope; what must hold is the *presence* of the payload — otherwise the downstream layer is committing against a gap.

VAST does **not** mandate the medium. A handoff can live in a doc, a Notion page, a Miro board, or a ticket epic — what's required is that the payload exists and is named, not its format. (Mandating templates or tools is a deliberate Kernel non-goal.)

> **This file specifies the *downward* handoffs** — what each layer hands the next to commit. The *upward* direction follows the **Challenge Flow** rules ([`glossary.md`](glossary.md), [`vast.md`](vast.md)): Strategy *informs*, only Vision *challenges* Architecture, Tactics *escalates*. The concrete routing for a use-case that doesn't fit current Architecture — Architecture self-correction, or a Vision-level revisit via the Vision Falsification Protocol — is specified in the Challenge & Escalation Protocol ([`governance.md`](governance.md)).

| Handoff | What must pass (the required payload) |
|---|---|
| **Vision → Architecture** | the committed, falsifiable Vision + its triggers + the values to anchor |
| **Architecture → Strategy** | the named domains + composition framework + invariants + owner |
| **Strategy → Tactics** | the selected compositions + priority/sequence + validation intent |

## Vision → Architecture

**Must pass:** the committed Vision as a falsifiable hypothesis — *what* experiences, for *whom*, *why*; the named falsification triggers; and the values to be anchored as structural constraints.
**So that:** Architecture can design the composition framework against a *committed target* — what skills exist, how they compose, which invariants are load-bearing. Designed against a moving target, the framework won't cohere.
**Must hold:** a committed, falsifiable Vision exists *before* Architecture commits the framework. (Absent or mis-shaped → AP-05 Vision-as-Use-Case, AP-07 missing triggers: Architecture ends up codifying a feature list or an un-revisable wish.)

## Architecture → Strategy

**Must pass:** the explicit Architecture — the named structural domains; the composition framework (its skill library and *composition interfaces* — how skills compose, skill-level; or the scope's equivalent capabilities); the invariants and values-as-constraints; and the one accountable owner.
**So that:** Strategy can select *which* compositions to pursue next, knowing the solution space and its guarantees. Strategy operates **within** this — it *informs* Architecture, never overrides it (Kernel P6 / Challenge Flow).
**Must hold:** explicit Architecture exists *before* Strategy commits — the Kernel's *Architecture-before-Strategy* rule made concrete, and minimum-viable-depth condition 4 ("Strategy references Architecture explicitly"). (Absent → AP-01 architecture-by-default; AP-02 vocabulary-only if the Architecture section is hollow.)

## Strategy → Tactics

**Must pass:** the selected use-cases/compositions; their priority and sequence; and the validation intent — what success looks like and how it's checked.
**So that:** Tactics can deliver personalized instances — specific compositions for specific users — against a coherent direction rather than generic aspiration.
**Must hold:** a prioritized set of selected compositions, with their validation intent, exists *before* Tactics delivers. (Absent → Tactics ships without direction: motion without traction.)

## Why the payload is required, not its format

Each handoff names *what must be present*, not *how to format it*. The medium is free; the payload is mandatory. The discipline is visible in the breach: remove the **V→A** payload and Architecture codifies the wrong target; remove **A→S** and Strategy selects compositions the framework can't support (architecture-by-default); remove **S→T** and delivery loses direction. Naming the payloads is what lets the [anti-patterns](anti-patterns.md) be *caught at the boundary* rather than discovered later as drift.

---

**Sources:** `kernel.md` (Architecture-before-Strategy rule; invariants vs implementations); `vast.md` (the four layers; "Intentional, not strict"); `glossary.md` (Challenge Flow; composition framework; minimum-viable-depth condition 4); `governance.md` (Vision Falsification Protocol — relevant to the upward direction). Companion: `anti-patterns.md` (AP-01, AP-02, AP-05, AP-07).
