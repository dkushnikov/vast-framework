# Governance — accountability across levels and depths

VAST governance has two dimensions:

1. **Level** — at what organizational scope is the framework applied (company / product / function)
2. **Composition depth** — how rich is the framework at this level (deep / medium / light / vocabulary-only — see [`applicability.md`](./applicability.md))

The accountability shape is the same at every level (one named accountable role per layer); the specific role names map to whatever titles your organization uses. The mechanics scale with depth — deep composition warrants dedicated governance bodies; lighter composition relies on existing exec rhythms.

## Three levels of governance

VAST is recursive across organizational scopes. The four-layer shape (V/A/S/T) reappears at each level with appropriately scoped accountable roles. The framework does not require any specific titles to exist in your org; it requires that you map the abstract roles to whoever holds the accountability.

### Level 1 — Company

| Layer | What it owns at company level | Mapped to (typical) |
|-------|-------------------------------|---------------------|
| Vision | What the company becomes. Market stance. Why this company exists. | CEO (or a single founder DRI), informed by the founder team |
| Architecture | How the company is structured to deliver the Vision: org design, capability portfolio, technology investment strategy | CEO as DRI, informed by the leadership team (architecture of the company-as-system) |
| Strategy | Which capabilities to develop in what sequence. Allocation of resources to functions and bets. | Function leaders / heads of organizations |
| Tactics | Execution within each function | Teams, individual contributors |

At company level, "Architecture" is mostly organizational and capability-portfolio architecture, not technical architecture. The composition-framework framing applies less directly; the four-layer shape applies as vocabulary for thinking about company-wide intentionality.

### Level 2 — Product (the primary VAST application)

| Layer | What it owns at product level | Mapped to (typical) |
|-------|-------------------------------|---------------------|
| Vision | What experiences the product enables, for whom, why | CPO / product leadership |
| Architecture | The composition framework — skill library, interfaces, invariants, implementations | CTO / engineering leadership |
| Strategy | Which experiences to compose next, sequencing, customer validation | Product Directors / Product Managers |
| Tactics | Personalized instance delivery | Engineering Managers / delivery teams |

This is where VAST's claims are sharpest. The composition-framework concept (invariants vs implementations) directly applies. Deep composition with full discipline is appropriate when the product is AI-first and the substrate matters.

### Level 3 — Function / Department

| Layer | What it owns at function level | Mapped to (typical) |
|-------|--------------------------------|---------------------|
| Vision | What the function becomes. The function's strategic stance. | Function leader (e.g., VP Marketing, VP CX, VP Operations) |
| Architecture | The function's composition framework — what tools, processes, AI integrations, automations make up the function's capability set | Function tech lead, ops lead, or designated process owner |
| Strategy | Which capabilities to invest in next, sequencing within function | Function sub-leaders / direct reports of function leader |
| Tactics | Function team execution | Function teams |

At function level, composition framework depth varies by function's AI integration. Marketing with heavy AI content systems = medium-to-deep composition. Finance with AI-assisted forecasting = medium composition. HR with standard tooling = light composition. The framework applies as deeply as the function's actual AI substrate engagement warrants.

### Recursion

The levels recurse — within a function, sub-teams may have their own V/A/S/T at sub-function scope. Within a product, components may have their own V/A/S/T (Matryoshka — see [`vast.md`](./vast.md)). The pattern repeats; accountability roles re-map at each level.

## Accountability pattern (level-agnostic)

At any level and depth, the structural commitment is:

- **One accountable role per layer.** One neck. Not committee, not collective ownership.
- **Accountability publicly known.** Not implicit. The accountable person is named in writing.
- **Decisions captured as named artifacts**, not procedural meeting minutes. Each significant decision references its accountable layer and signing role.

These are the minimum. Below them, the framework is vocabulary, not application — see [`applicability.md`](./applicability.md) on minimum viable depth.

## Decision propagation

Capturing a decision is not the same as making it findable. The common failure: Architecture gets decided in commits, chat threads, or one team's head — *captured*, perhaps, but the downstream consumers who must operate within it can't discover *what* was decided or *why* at the moment they need it. The framework's decisions then function as a black box, and downstream layers re-create architecture-by-default around them.

Making those records *findable* is a **recommended (Guide-level) pattern, not a Kernel invariant.** Capturing significant decisions as named artifacts is already part of the accountability pattern above; this section is the next step — discoverability — and it scales with composition depth rather than acting as a conformance floor.

**The pattern:** when an Architecture decision changes a *material* inherited constraint — an invariant, an interface, a skill boundary, a trust contract, or cross-consumer behavior — make its record discoverable, not merely captured. *Material* excludes routine implementation migrations that leave inherited constraints intact.

- **Minimum discoverability:** the record is (a) indexed from the parent Architecture's decision record and (b) linked from the work surfaces of the consumers the change affects. That is the achievable bar — reachable by the consumers who must operate within it — not "broadcast to every consumer," which is an aspirational poster ([AP-08](./anti-patterns.md)), not a mechanism.
- **The medium is fungible:** an ADR repository, PR-to-ticket links, a decision-doc index, an RFC archive. The pattern recommends discoverability; it never mandates the tool.
- **Vocabulary-only depth:** no composition framework exists to propagate decisions about — the pattern doesn't apply.

This is the same concern [`scaling.md`](./scaling.md) raises: as agents and teams multiply, decisions need to live in a discoverable record, not tribal knowledge. A decision no downstream consumer can find is, operationally, a decision that didn't propagate.

## Governance-body intensity scales with depth

**Deep composition (typically product engineering, shared platform):** a dedicated governance body aligns the four layer accountabilities — often three people, when Vision and Strategy are held by the same role.

| Layer pair | Why it's a governance body |
|------------|----------------------------|
| Vision + Strategy | Same accountable role often, but the body forces explicit re-examination at each cycle |
| Architecture | Cross-consumer decisions (skill library evolution, invariant changes) benefit from formalized review |
| Tactics | Surfaces signals up; receives clarity down |

Decisions about composition-framework evolution, invariant changes, skill-library additions, cross-consumer effects pass through this body. Without alignment of the accountable roles, the framework doesn't work — it becomes ceremony.

**Medium composition (function-level AI integration):** accountability is named per layer but no dedicated governance body. Cross-layer signals handled in existing exec rhythms (1-1s, function reviews, OKR check-ins).

**Light composition / vocabulary-only:** accountability is still named per layer (this is the minimum). No additional ceremony.

**Reach across levels.** Accountability recurses at *every* level (one neck per layer per scope); the governance *body* recurses only at **deep-composition** levels. Most feature teams operate *within* the parent's invariants (Matryoshka) and escalate via the Challenge & Escalation Protocol rather than standing up their own committee. A nested instance needs its own body only when it crosses the recursion threshold (`vast.md`) *and* sits at deep composition — otherwise the parent's body plus the escalation path suffices.

## Vision Falsification Protocol

A key v3 addition. Vision-as-committed-hypothesis is operational only if there's a protocol for what happens when falsification triggers fire. Without the protocol, "Vision is a hypothesis with revision triggers" is aspirational epistemology.

### Protocol shape

**Step 1 — Triggers must be observable and named.**

Every Vision commitment includes 2-5 named triggers. Each trigger is:

- **Observable** — measurable in real metrics, not interpretive judgment. Not "users seem unhappy"; "weekly retention drops below 35% for 4 consecutive weeks."
- **Bounded** — has a concrete threshold. Not "engagement falls"; "AI-feature daily-active rate fails to exceed 20% by end of Q3."
- **Owned** — a named role monitors the trigger continuously. Trigger-owner is typically a function leader (Strategy layer) close to the relevant signal.

**Step 2 — Trigger fires.**

When the trigger threshold is reached, the trigger owner:

- Reports to Vision accountable role within 1 week of confirmation
- Provides supporting data and the trigger interpretation
- Does NOT make Vision-revision decision unilaterally

**Step 3 — Vision review session.**

Within 2 weeks of trigger fire, a Vision review session convenes:

- Vision accountable role + governance body (Architecture and Strategy accountable roles)
- Optional: trigger owner presents data; outside experts as needed
- Three questions: Was the trigger interpretation correct? Is the underlying signal what we thought? What are the alternative Vision hypotheses?

**Step 4 — Decision, documented.**

One of three outcomes, captured as named artifact:

- **Confirm Vision.** Trigger interpretation didn't survive review; current Vision continues. Document why the trigger fire was misleading.
- **Revise Vision.** Trigger interpretation correct; Vision is updated. Document new commitment, new triggers, and effective date.
- **Extend monitoring.** Insufficient evidence for confirm-or-revise; new trigger thresholds set with shorter horizon.

**Step 5 — Architecture re-examination (if Vision revised).**

Within 4 weeks of Vision revision, Architecture review session:

- Each significant Architecture commitment under old Vision is assessed: still aligned, partially aligned (refactor required), or invalidated (rebuild)
- Documented decision per commitment. No automatic invalidation; each decision explicit.
- Migration plan and cost estimate for changes required by revised Vision

### Why this is necessary

Without the protocol, Vision-as-hypothesis defaults to "Vision is committed; we'll figure out revision when we see it." That collapses to either fixed Vision (the original survivorship-bias risk) or ad-hoc revision (no discipline). The protocol creates the conditions under which Vision can both anchor Architecture intentionally AND be revised when evidence demands it — without either failure mode.

## Challenge & Escalation Protocol

Challenge Flow (see [`vast.md`](./vast.md)) names the *direction* of cross-layer influence: challenge flows down — only Vision may challenge Architecture — while feedback flows up (Strategy *informs*, Tactics *escalates*) and Architecture *self-corrects*. This protocol names the *operation*: what a lower layer actually does when it hits something the layer above doesn't support. Without it, "Strategy informs, never challenges" is a rule with no procedure — and the vacuum gets filled by the failure mode it exists to prevent ([anti-pattern](./anti-patterns.md) AP-12, Strategy overriding Architecture).

Enforcement scales with depth: at deep composition the routing runs through the governance body; at lighter depths, through existing exec rhythms. The routing is the same either way.

### Trigger and triage

A lower layer hits something the layer above doesn't support — most commonly **Strategy wants a composition the current Architecture can't deliver** (a use-case with no supporting skills, interfaces, or invariants).

Tactics surfaces the same class of problem from below by **escalating to Strategy** — never directly to Architecture or Vision. Strategy triages: a pure execution issue → Tactics resolves it; a sequencing or use-case issue → Strategy resolves it; an architectural mismatch → enter the routing below.

### The forbidden move

Strategy may **not** challenge or override Architecture — not drop an invariant, not dictate a framework change. That is AP-12, and it re-creates the default-by-accumulation decision-making VAST replaces. The misfit must be *routed*, not forced.

### The discriminator

Route by scope:

> **Does the use-case serve the committed Vision *as currently scoped* — same audience, promise, domain — without requiring a new or revised Vision commitment?**

- **Yes (within scope) → Architecture gap.** The commitment stands for routing purposes; the framework just can't express it yet. → **Route A.**
- **No (it needs a new/changed audience, promise, domain, success criterion, or value tradeoff) → Vision question.** → **Route B.**

The trap to avoid: a use-case that *both* serves the current Vision and quietly expands its scope — a new segment, channel, or regulated domain. That is a Vision question, not an Architecture gap; route it **B**. When it's genuinely unclear, run both questions explicitly — "how would we build this?" *and* "does this change what we've promised, and to whom?" — rather than letting Strategy resolve it unilaterally. Architecture-feasibility can be analyzed in parallel, but a scope change is Vision's call.

### Route A — inform Architecture (Vision unchanged)

The common case. Strategy hands Architecture first-class evidence: the desired composition, the customer/market signal, the cost of its absence. Architecture — the accountable owner — returns a **documented response**: **accept** (with a closure path), **defer** (with a criterion or timebox), or **decline** (with rationale, owner, and date). A real decision artifact is what makes "respond substantively" more than ceremony.

If Architecture defers or declines a gap that Strategy believes leaves a *committed* Vision promise unsupported, Strategy still does not override — it **informs Vision** of the unresolved mismatch. Vision may then direct Architecture to re-examine (its challenge right), narrow or revise the promise (it may be infeasible — Vision is a hypothesis, not a guarantee), or confirm the use-case is out of scope. This appeal keeps Route A from dead-ending into AP-12, and is the mitigation for the *overpowered* failure mode — Architecture vetoing legitimate Strategy moves (see [Dual-risk calibration](#dual-risk-calibration)).

### Route B — escalate to Vision (the scope may need to change)

The use-case implies an experience outside the committed scope. Strategy cannot challenge Architecture, so it routes *upward* — informing **Vision** that a live use-case sits outside current scope. Vision convenes a review using the decision-and-documentation shape of the [Vision Falsification Protocol](#vision-falsification-protocol) — call it *falsification* only if a named trigger fired, otherwise an out-of-cycle scope review — and decides:

- **Vision expands or revises** → if the Vision changes, **Vision** (the only layer with downward challenge right) challenges Architecture, which re-examines per that protocol's Step 5.
- **Vision declines** → the use-case is deliberately out of scope. It is *not* built by routing around Architecture. "No — not this, not yet" is a first-class outcome: scope discipline, not failure.

### Grounded, not circular

The legitimacy is Kernel Principle 6, not the mere avoidance of AP-12: Strategy may *inform* upward and Architecture *decides*; only Vision *challenges* downward. AP-12 is the prohibited inversion — Strategy grabbing the downward lever. This protocol is the allowed routing: two legitimate levers (inform Architecture, escalate to Vision) plus a scope discriminator that stops a Vision-change from being smuggled in as an Architecture gap, and a genuine Architecture gap from being inflated into a Vision crisis.

## Political dimensions — named explicitly

Governance is not neutral. Naming changes:

**Architecture authority consolidation.** Whoever holds Architecture accountable gains explicit decision rights. If decisions were previously diffuse (consensus committees, default by accumulation), the consolidation is a real political change. Name it openly.

**Strategy authority sharpening.** Whoever holds Strategy accountable narrows from implicit architecture-influence to explicit composition-selection within architectural constraints. Real narrowing — minimizing it ("nothing changes") invites backlash when the change becomes visible.

**Challenge rights formalization.** Vision-can-challenge-Architecture is explicit; Strategy-only-informs is explicit. This codifies a hierarchy that may have been informal. Adversarial review noted the risk: asymmetric challenge rights can produce architecture-vetoes-product symmetric dysfunction. Mitigation: Strategy layer's ability to inform must operate with real weight; Architecture treats Strategy signals as first-class evidence, not noise to be dismissed.

**Tactics-layer dignity.** Whoever holds Tactics accountable operates within structure they didn't design. Framework legitimacy with this layer depends on Challenge Flow actually working — when Tactics escalates architectural mismatch, Architecture must respond substantively.

## Dual-risk calibration

Governance design faces two failure modes simultaneously:

- **Underpowered.** Framework becomes ceremony; architecture decided by default anyway. Original pre-VAST dysfunction persists.
- **Overpowered.** Framework becomes gatekeeping; Architecture authority vetoes legitimate Strategy moves; shadow composition patterns emerge.

Both real. Calibrating between them is ongoing work. Signals to watch:

- Are Strategy-to-Architecture signals flowing, or being dismissed?
- Are Architecture decisions being made inside the body, or retrofitted post-hoc?
- Are teams running shadow composition patterns to route around slow governance?
- Does the accountable-role signature process take days, weeks, or months?
- Has the Vision Falsification Protocol fired at least once when triggers indicated it should?

See [`consequences.md`](./references/consequences.md) for extended discussion of political dynamics.

## References

- [`vast.md`](./vast.md) — core framework definition (including invariants vs implementations split)
- [`applicability.md`](./applicability.md) — composition depth and minimum viable depth threshold
- [`consequences.md`](./references/consequences.md) — political consequences and calibration signals
