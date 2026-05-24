# VAST validation heuristics — detailed

For use by `vast-validate` SKILL.md. Detail behind the condensed checks table. One section per check, anchored to match the SKILL.md detail-refs.

The five checks run conditionally: layer purity and scope homogeneity always run; falsification runs only if a Vision is present; composition completeness only if an Architecture is present; Challenge Flow only if cross-layer interactions are described. Skipped checks produce no report lines.

## Layer purity {#layer-purity}

Each present layer must hold content appropriate to its level. Drift = content that belongs to a *different* layer. The two most common drifts are **down-drift** (a higher layer written as the work of a lower one) and **up-drift** (a lower layer claiming higher-layer authority).

### Vision

**Pure Vision:** states *what experiences we enable, for whom, and why* — committed as a falsifiable hypothesis. Names the user, the pain, the enabled outcome.
- Linguistic signals (pure): "We enable {who} to {outcome}", "We believe {hypothesis}", "for {segment}, who {pain}"
- Test: could you derive multiple different feature sets that all serve this Vision? If yes → it's a Vision, not a spec.

**Drift to flag:**
- **Tactics drift (Fail):** the Vision is a feature list or a roadmap with deadlines — "Ship X, then Y by Q3, then Z." This is anti-pattern #1 (Vision-as-Use-Case) in its acute form. Signals: enumerated features/screens, dates, "we will build". Reframe: extract the *why* the features serve; move the feature list to Strategy/Tactics.
- **Strategy/Vision conflation (Warn):** Vision and the Strategy section are nearly interchangeable (both name compositions to build). Warn unless the Vision also lacks a why — then it compounds toward Fail.
- See `../../../references/anti-patterns.md` #1 (Vision-as-Use-Case).

### Architecture

**Pure Architecture:** the *composition framework* — the structural domains, the skills/capabilities and how they compose, the invariants that hold across compositions. It answers "what can be composed, how, under what guarantees" — not "what we'll build this quarter" and not "what market we win".
- Linguistic signals (pure): "skill library", "interfaces", "invariants", "fallback policy", "the domains we own", "composition framework", "capability set" (function-flavored)
- Test: would this content still hold if the roadmap changed? Architecture is durable structure; if it reads like a quarter's plan, it's drifted.

**Drift to flag:**
- **Tactics drift (Fail):** Architecture written as a project/task list — "Build the auth service, migrate services, onboard engineers." No skills, no interfaces, no invariants — just deliverables. This is anti-pattern #2 (Architecture-by-default) made concrete: the framework stays implicit while a backlog stands in for it. Reframe: name the skill boundaries, the invariants, the accountable owner; move the task list to Tactics.
- **Vision drift (Fail or Warn):** Architecture written as market positioning / "why we win" — "We become the default platform for X." That's Vision content. Fail when it fully displaces structural content; Warn when a positioning sentence sits atop otherwise-structural Architecture.
- **Org-chart / tech-stack drift (Fail):** Architecture is an org chart, a system/deployment diagram, or a tech-stack list — reporting lines or technologies — with no domains, invariants, interfaces, or values-as-constraints. The wrong object stands in for the decision-architecture. This is anti-pattern AP-03. Reframe: org charts and stacks *represent or implement* architectural choices; name the domains, invariants, interfaces, and values.
- See `../../../references/anti-patterns.md` #2 (Architecture-by-default) and #9 (AP-03, Architecture-as-org-chart/stack).

### Strategy

**Pure Strategy:** *which experiences to compose next* — sequencing, customer validation, investment direction — operating *within* the composition framework Architecture named.
- Linguistic signals (pure): "compose X next", "sequence", "validate with segment Y", "invest in", "roadmap of compositions", "prioritize"
- Test: does it choose *where to apply effort* given the domains Architecture named? Strategy selects within constraints; it doesn't define the constraints.

**Drift to flag:**
- **Tactics drift (Warn, → Fail if total):** Strategy is a list of dated concrete deliverables with no investment logic — "Ship feature A Feb 1, feature B Mar 1." The *why-this-sequence* is missing. Warn for partial; Fail if Strategy is purely a delivery calendar.
- **Architecture drift (Fail):** Strategy redefines the framework — declares new invariants, removes invariants, restructures the skill library. That is also a Challenge Flow violation (see `#challenge-flow`); flag under both checks. Reframe: Strategy *informs* Architecture with the signal; Architecture decides.

### Tactics

**Pure Tactics:** personalized instance delivery — concrete compositions for specific users at specific moments. This is the floor; content rarely drifts *up*.
- Linguistic signals (pure): specific compositions, specific user/segment + moment, concrete artifacts, metrics
- Drift to flag: Tactics that is generic aspiration with no concrete delivery ("make users happy") is hollow, not impure — flag as Warn ("Tactics names no concrete delivery"), not a layer-drift Fail.

### Severity rule for layer purity

- **Fail:** a layer's *primary* content belongs to another layer (Vision that is a feature list; Architecture that is a project plan; Strategy that redefines the framework).
- **Warn:** a layer is mostly pure but bleeds — one positioning sentence in Architecture, a dated deliverable in Strategy, Vision/Strategy near-interchangeable but Vision still has a why.

## Scope homogeneity {#scope-homogeneity}

VAST is recursive — the four-layer shape reappears at company / product / function / ways-of-working (WoW) scope. A single doc should operate at **one** scope across all its layers. The classic break: a company-level Vision ("become the default X globally") paired with product-UI-level Architecture detail ("the settings screen has these toggles"). The layers don't compose because they're describing different systems.

### Detecting scope per layer

Match each layer's content against the per-scope identifying signals in `../../../references/layer-definitions.md`. Compressed cues:

- **Company:** "market stance", "why this company exists", "capability portfolio", "org design", "allocation to functions and bets", "team archetypes", "re-org", "CEO / leadership team".
- **Product:** "composition framework", "skill library", "AI substrate / model / LLM", "invariants and implementations", "which experiences to compose next", "personalized instance delivery", "CPO / CTO / PM / EM".
- **Function:** "VP {Marketing/CX/Ops}", "the function's capability set", "tools/processes/AI integrations of a single function", "invest in next within the function", domain-native framings (ATS, forecasting tooling, CX routing).
- **WoW:** "review meetings / decision artifacts / planning cycle / retrospective", "tool migration (Slack → …)", "async-first / decisions-as-artifacts / blameless postmortems", "cadences / 1-1s / all-hands / RFC format".

### Severity rule for scope homogeneity

- **Fail:** two or more layers are at clearly *different* scopes (e.g. company Vision + product Architecture; product Vision + WoW Tactics). Report at doc level: name each layer's detected scope. Suggested fix: split into scope-specific docs, or re-pitch all layers to one scope.
- **Warn:** a single layer is scope-ambiguous (could read as product or function) while the rest are consistent — flag the ambiguous layer, ask for clarification.
- **Pass:** all present layers share one scope.

Note the interaction with layer purity: a company Vision paired with product-UI Architecture often *also* trips layer-purity (the "Architecture" is really a Tactics-level UI spec). Report both — scope-homogeneity at doc level, layer-purity per layer — rather than collapsing them into one finding.

## Vision falsification triggers {#falsification-triggers}

**Runs only if a Vision is present.** Vision in VAST is a *committed falsifiable hypothesis* — neither emergent (Lean) nor immutable (waterfall). That commitment is operational only if the Vision names the conditions under which it gets revisited. Source: `governance.md` Vision Falsification Protocol, Step 1.

A valid trigger is:
- **Observable** — measurable in real metrics, not interpretive judgment. "weekly retention < 35% for 4 consecutive weeks", not "users seem unhappy".
- **Bounded** — concrete threshold + (ideally) duration. "AI-draft acceptance fails to exceed 40% by end of Q3", not "engagement falls".
- **Owned** — a named role monitors the trigger. Typically a Strategy-layer leader close to the signal.

**Test:** can you point at the Vision and read off 2-5 named conditions, each measurable and each owned, under which the Vision is revisited? 

### Severity rule for falsification triggers

- **Fail:** the Vision states *no* revision conditions at all, or only "we'll revise if it's not working" (interpretive, unbounded, unowned). This is anti-pattern #4 (Missing Vision Falsification triggers). Suggested fix: add 2-5 observable + bounded + owned triggers; cite the 5-step protocol.
- **Warn:** triggers are present but incomplete — observable thresholds but no named owner, or named owner but vague threshold ("if growth slows"). Suggested fix: tighten to observable + bounded + owned.
- **Pass:** ≥1 trigger that is observable AND bounded AND owned (2-5 is the protocol's range; one solid trigger passes the check, note if fewer than two).

See `../../../references/anti-patterns.md` #4 for the bad/good fragment pair.

## Composition framework completeness {#composition-completeness}

**Runs only if an Architecture is present.** The Architecture layer's primary artifact is the composition framework, which has **four sub-elements** (glossary.md "Composition framework"):

1. **Skill library** — what atomic capabilities exist (agents, tools, model wrappers, retrievers, validators, classifiers, generators).
2. **Composition interfaces** — how skills combine (handoff protocols, state-sharing, orchestration, error propagation).
3. **Composition invariants** — substrate-portable rules (skill boundaries, quality contracts, fallback policies, trust contracts, observability, safety guarantees).
4. **Composition implementations** — substrate-coupled tactics (LLM choice, prompt strategies, retry/timeout values, output-format mechanisms, cost tactics).

Plus the **invariants-vs-implementations split** must be present and meaningful: the doc distinguishes what is portable (invariants — change rarely, deliberately) from what migrates with the substrate (implementations). Conflating them produces false substrate-agnosticism claims. See `../../../references/vast-essentials.md` §3 for the full split.

**Test:** can you locate all four sub-elements, and is the invariants/implementations distinction explicit (not just an undifferentiated "technical decisions" pile)?

### Severity rule for composition completeness

- **Fail:** Architecture is *claimed* but the framework is empty or hand-wavy — no skill boundaries, no invariants, no interfaces ("we'll compose the right skills as needed"). This is anti-pattern #7 (Vocabulary-only where deep is needed) and overlaps anti-pattern #2 (Architecture-by-default). Suggested fix: name skill boundaries + ≥1 quality invariant + ≥1 fallback invariant + an accountable owner, or honestly label the doc "VAST vocabulary, not VAST applied".
- **Warn:** partial — some sub-elements present (e.g. skill library + interfaces) but invariants and implementations are not split, or one of the four sub-elements is missing. Suggested fix: add the missing sub-element and/or separate invariants from implementations.
- **Pass:** all four sub-elements present and invariants/implementations split is explicit.

**Implementation-as-invariant (AP-04).** Distinct from absence: the split is *claimed* but the invariants tier is populated with substrate-coupled specifics — named models, prompts, vendors, retry/timeout values. Flag **Warn** if a few items are mislabeled; **Fail** if the whole "invariants" list is implementations (the framework then only *looks* portable). Reframe: state the portable rule ("every response carries provenance + a fallback") apart from the substrate tactic ("GPT-4o @ 0.2, 3× retry"). See `../../../references/anti-patterns.md` #10 (AP-04).

### Non-product scopes

For non-product Architecture, adapt the four sub-elements to the scope (per `../../../references/layer-definitions.md` and `architecture-levels.md`), and apply the depth-appropriate bar — do not demand product-runtime rigor of a light-composition function doc (that would itself be anti-pattern #6, forcing deep where light fits):

- **Company:** org composition framework — team archetypes (skills), how teams compose (interfaces), org-portable invariants (every decision has a named owner; span of control bounded; decisions at lowest competent layer), current org structure (implementations: titles, reporting lines, RACI). 
- **Function:** the function's capability set — sourcing/screening skills, ATS interfaces, compliance/fairness invariants, specific-vendor implementations. Bar scales with the function's AI engagement (medium for AI-heavy, light otherwise).
- **WoW:** process composition framework — process building blocks (review meetings, decision artifacts) as skills, end-to-end workflows as interfaces, durable principles (decisions-as-artifacts, async-first, blameless postmortems) as invariants, specific tools/cadences/templates as implementations.

For light/vocabulary-only depth, completeness reduces to the minimum-viable-depth floor (named Architecture owner + framework exists in minimal form); absence of a full invariant set is *not* a Fail at that depth.

## Challenge Flow respect {#challenge-flow}

**Runs only if the doc describes cross-layer interactions.** If the doc just states each layer's content without describing how layers interact, this check passes by default — note "no cross-layer interactions described" rather than forcing a finding.

The rules (glossary.md "Challenge Flow"): **challenge flows down, feedback flows up.**

- **Vision *challenges* Architecture** — the only downward challenge right. Vision may require Architecture to change.
- **Strategy *informs* Architecture** — feeds first-class signal up (customer pain, adoption friction, competitive movement). Strategy does **not** challenge or override Architecture.
- **Architecture *self-corrects*** — based on signals from all layers; the Architecture accountable role decides.
- **Tactics *escalates*** — surfaces execution blockers up; Architecture must respond substantively.

**Test:** scan for any sentence where a *lower* layer dictates to a *higher* one, or where the wrong layer claims challenge rights.

### Violations to flag (Fail)

- **Strategy overriding Architecture** — "Strategy decided to drop invariant X", "Product overrides the framework here", "Strategy review concluded the latency invariant is slowing us down, so we're removing it." This is anti-pattern #8. Reframe: Strategy *informs* ("the invariant is costing adoption in segment X — here's the data"); Architecture decides whether to relax/keep/re-engineer.
- **Tactics dictating up** — Tactics rewriting Architecture invariants rather than escalating.
- **Architecture treated as downstream of Strategy** — the framework presented as a derivative of the roadmap rather than the constraint the roadmap operates within.

### Severity rule for Challenge Flow

- **Fail:** an explicit violation (a lower layer overrides/challenges a higher one; wrong layer claims challenge right).
- **Warn:** ambiguous direction — interaction described but it's unclear whether Strategy is informing or overriding. Suggested fix: state explicitly that Strategy informs and Architecture decides.
- **Pass (by default):** no cross-layer interactions described, OR all described interactions follow the rules.

See `../../../references/anti-patterns.md` #8 (Strategy challenging Architecture instead of informing) for the bad/good fragment pair.

## Kernel floor {#kernel-floor}

The Kernel's four Rules are the floor that separates *VAST applied* from *VAST vocabulary*. Three are already covered by other checks; this check adds the one that isn't — **layer ownership** — and reads the floor as a whole.

| Kernel Rule | Checked by |
|---|---|
| All four present layers named, each with **one accountable owner** | here (ownership) |
| Architecture explicit **before** Strategy commits | layer purity (Architecture-by-default) + composition completeness |
| Vision is a **falsifiable hypothesis** | falsification-triggers check |
| **Invariants separated from implementations** | composition completeness (+ implementation-as-invariant) |

### Ownership (Rule 1)

Each present layer names **one** accountable owner (one neck) — not "the team", "leadership", a committee, or "TBD".

- **Fail:** a *present* layer has no single accountable owner — its owner is a collective / committee / "TBD", left blank while other layers are owned, or only a trigger/doer owner is named (not a layer owner). The Rule requires one neck per present layer, so a single missing or committee owner fails *that* layer. This is anti-pattern AP-09 (ownerless layers). Reframe: name exactly one accountable role per layer — consult many, decide one.
- **Warn:** the doc names *no* owners anywhere (an informal sketch) and does not claim VAST is *applied* — flag the gap rather than failing. Once the doc owns some layers or claims "VAST applied," a missing owner is a Fail (see `applicability.md` minimum-viable-depth condition 2).
- **Pass:** each present layer names exactly one accountable owner.

### Reporting the floor

In the Summary, note whether the Kernel floor holds (Rules 1–4 all pass for the present layers). Below the floor, the doc is *VAST vocabulary, not VAST applied* — say so, and cross-reference the failing sub-checks rather than duplicating their findings.

## Source

Heuristics derived from:
- `vast.md` — "The four layers", "Intentional, not strict" (architecture-by-default), "The triad"
- `glossary.md` — layer definitions, "Composition framework" (four sub-elements), "Challenge Flow"
- `governance.md` — "Vision Falsification Protocol" (5-step), "Challenge flow"
- `architecture-levels.md` — Architecture at product / org-design / WoW level (non-product composition adaptation)
- `applicability.md` — composition depth, minimum viable depth floor

(Paths relative to framework repo root.) The shared-reference paths cited inline above (`../../../references/...`) are relative to *this file's* location at `skills/vast-validate/references/`.
