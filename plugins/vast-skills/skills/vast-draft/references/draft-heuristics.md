# VAST draft heuristics — detailed

For use by `vast-draft` SKILL.md. Detail behind the condensed heuristics table. One section per step, anchored to match the SKILL.md detail-refs.

`vast-draft` is **generative**, like `vast-transform` — but where transform *restructures rich prose* into VAST, draft *elicits a new doc from a near-empty seed*. These heuristics govern *how to construct the scaffold* — the guiding questions, the what-good-looks-like, and the fillable stubs — for each layer. The governing discipline throughout, stated once and applied everywhere: **scaffold, don't fabricate.** Where the seed gives content, lift it into the stub; where the seed is silent, supply the *question to answer*, never an invented answer. A confidently fabricated Vision/invariant/trigger launders the skill's guesses as the author's commitments and propagates downstream as if real — strictly worse than an honest blank with a good question beside it.

The five steps run **top-down in commitment-priority order**: scope → Vision → Architecture → Strategy+Tactics → depth. Scope is decided first because it sets every downstream guiding question. Vision precedes the lower layers because VAST's load-bearing claim is that commitment at Vision (then Architecture) is what makes the layers below meaningful — the scaffold's *order* teaches the framework's discipline.

## Scope identification {#scope-identification}

Pick **one** scope for the scaffold: company / product / function / ways-of-working (WoW). The scope determines what each layer's guiding questions and what-good-looks-like say — a product Architecture asks for a composition framework; a company Architecture asks for org design; a function Architecture asks for a capability set. So scope is settled before any layer is scaffolded.

A seed is usually short, so scope often comes from one or two cues. Match the seed against the per-scope identifying signals in `../../../references/layer-definitions.md`. Compressed cues:

- **Company:** "company direction", "3-year ambition", "what the company becomes", "market stance", "capability portfolio", "org design", "where to allocate across functions/bets", "CEO / leadership".
- **Product:** "build a product / feature", "AI assistant / copilot / summarizer / generator", "for {user segment}", "the experience we want to enable", model/substrate language, "compose skills".
- **Function:** "our {People / Marketing / CX / Finance / Ops} team wants to…", "use AI in {recruiting / content / routing / forecasting}", "the function's tools/processes", a single function adopting AI.
- **WoW:** "how we run {meetings / planning / reviews / incidents}", "our operating model", "tool migration", "decision artifacts / cadences / retrospectives".

### When the seed names the scope

The task often hands you the scope outright ("Product scope.", "Function scope —"). When it does, **use it** — don't re-derive or second-guess it. The seed's stated scope is the commitment; honor it and move on.

### When the scope is ambiguous

If the seed gives an idea but no scope, and the cues are genuinely mixed (e.g. "we want to use AI for support" could be function-scope CX adoption or product-scope feature), do one of two things — never silently pick:

- **Ask** one crisp disambiguating question if interaction is available ("Is this the CX *function* adopting AI tooling, or a *product* feature you're shipping to customers?").
- **State the assumption explicitly** in the doc and proceed: lead the title and the Scope note with the assumed scope and *why*, and flag in the Scope Note that confirming it may shift the Architecture guiding questions. The assumption is visible and revisable, not buried.

**Test:** read off the scope cues you matched. If the seed states the scope → use it. If they cluster at one scope → that's it. If they genuinely split → ask, or assume-and-flag.

## Vision first {#vision-first}

Vision is scaffolded **first and foremost** — both because it is the highest commitment-priority layer and because the scaffold's top-down order is itself a teaching of the framework. The Vision section answers **what experiences we enable, for whom, and why**, committed as a *falsifiable hypothesis*. The scaffold's job is to elicit that from the author — not to author it.

### The commitment-priority gate (make it explicit)

The doc's lead line and the Notes' commit-order reminder both state the gate: **commit Vision before investing in the layers below it.** This is not decoration — it is the single most important thing the scaffold teaches. An Architecture designed against an uncommitted Vision is designed against a moving target; a Strategy that sequences compositions before the Vision is settled sequences toward an unfixed goal. Say so, plainly, at the top.

### Scaffolding the Vision section

- **`Answer:` stub** — pre-fill *only* with what the seed actually states. A seed like "an AI meeting-notes summarizer for sales teams" gives you a fragment of the enabled-experience (meeting-notes summarization) and a fragment of the for-whom (sales teams) — lift those, lightly tightened, into the stub, and leave the *why* as a question. A seed that states only "a 3-year company direction" with no content gives you nothing to pre-fill — the stub stays `{to fill}` and the guiding questions carry the section. Never write a declarative Vision sentence the seed didn't supply.
- **`Guiding questions:`** — the why / for-whom / enabled-experience triple, as questions: *What experience does this enable? For whom (which segment, specifically)? Why does it matter — what changes for them?* Tighten to the seed where you can (e.g. "for whom — sales teams broadly, or a specific sales role/segment?").
- **`What good looks like:`** — describe the *shape* of a good Vision answer, not the answer: "a committed falsifiable hypothesis that names the enabled experience + the audience + why it matters — not a feature list (that's Tactics, anti-pattern #1) and not a slogan ('make teams productive')." This is the line that steers the author away from Vision-as-Use-Case.

### Falsification triggers — always prompt, never invent

The Vision section **always** carries a `Falsification triggers (required):` sub-field. Seeds essentially never supply triggers, so this is almost always a prompt, not a pre-fill. The prompt names the *criteria a good trigger meets* — **observable** (a real metric, not "users seem unhappy"), **bounded** (a concrete threshold + duration), **owned** (a named role monitoring it) — and asks for 2-5. It does **not** invent thresholds, metrics, or owners. Inventing a trigger ("revise if retention < 35% for 4 weeks") fabricates a commitment the author never made; the most you do is give an *illustrative shape* clearly marked as an example of the form, e.g. "(shape, not a value: '{metric} stays below {threshold} for {duration} — owner: {role}')".

See `governance.md` (Vision Falsification Protocol) for the full observable/bounded/owned definition and the 5-step fire→review→decide process the triggers feed into; see `../../../references/anti-patterns.md` #4 for the missing-triggers anti-pattern this prompt exists to prevent.

**Test:** does the Vision section pre-fill *only* seed-stated content, lead with questions everywhere the seed is silent, and prompt for observable/bounded/owned triggers without inventing any? If yes, the Vision scaffold is honest.

## Architecture scaffold {#architecture-scaffold}

Architecture is the layer whose guiding questions shift *most* by scope — so the scaffold must ask the scope-appropriate structural questions, not a generic "what's your architecture." Use the per-scope Architecture content in `../../../references/layer-definitions.md` and the composition-framework detail (and vocabulary aliases) in `../../../references/vast-essentials.md`.

### Per-scope guiding questions

- **Product → composition framework.** Ask for the four sub-elements explicitly: *What skills/capabilities exist (the AI capabilities — generators, retrievers, classifiers, validators)? How do they compose (interfaces — handoffs, state-sharing, orchestration)? What invariants must always hold (skill boundaries, quality contracts, fallback policies, safety guarantees)? What's substrate-coupled (implementations — model choices, prompt strategies, retry/timeout values)?* This is the richest Architecture scaffold; product is where the invariants-vs-implementations split applies directly.
- **Function → capability set (use the "capability framework" alias).** Ask: *What tools, processes, AI integrations, and automations make up the function's capability set? Which steps are AI-assisted vs human? What must always hold (e.g. for recruiting: bias-and-compliance guarantees; for finance: financial-controls/audit invariants)?* Per `../../../references/vast-essentials.md` §4, "capability framework" / "process framework" are the same VAST Architecture artifact under a function-native label — use the label most natural to the domain.
- **Company → org / capability-portfolio design.** Ask: *What org capabilities and team structures deliver the Vision? What are the org-portable invariants (every decision has a named owner; span of control bounded; decisions at the lowest competent layer)? What's the current implementation (titles, reporting lines, RACI/OKR cascades)?* At company scope, "Architecture" is mostly organizational, and the composition-framework framing applies as vocabulary more than as a literal skill library — say so in the what-good line.
- **WoW → process framework.** Ask: *What process building blocks exist (review meetings, decision artifacts, planning cycles, retrospectives)? What end-to-end workflows do they compose into? What durable principles hold (decisions-as-artifacts, async-first, blameless postmortems, documentation-precedes-execution)? What are the current implementations (Notion/Linear/Slack, cadences, templates)?*

### Discipline

- **Don't invent structure to fill the stub.** If the seed names no skills, the `Answer:` stub stays `{to fill}` and the guiding questions do the work. Listing skills the author never mentioned is exactly the fabrication this skill exists to avoid — and it manufactures architecture-by-default (#2) by making structure *look* committed when it isn't.
- **The `What good looks like:` line carries the minimum-viable-depth floor.** For any scope that warrants a real framework (product, AI-heavy function), the good-answer shape names: at least skill/capability boundaries + ≥1 quality invariant + ≥1 fallback invariant + a single named accountable owner. For vocabulary-only-depth work (most company scope), the good-answer shape is honest about being shared *language* for org design, not a literal skill library — and says so, to avoid claiming vocabulary-only where deep is needed (#7) *and* to avoid forcing deep where light fits (#6).
- **Name the accountable owner as a question, every scope.** "Who is the single accountable owner for this Architecture?" is a guiding question at every scope — VAST requires one named neck per layer, and seeds essentially never supply it.

**Test:** are the Architecture guiding questions the ones *this scope* needs (composition framework for product, capability set for function, org design for company, process framework for WoW), and does the stub stay blank where the seed named no structure?

## Strategy + Tactics scaffold {#strategy-tactics-scaffold}

Strategy and Tactics share the same scaffold shape (question + what-good + stub) and are scaffolded together after Architecture, because both operate *within* the structure Architecture names. The triad (`../../../references/vast-essentials.md` §2) anchors the distinction: Strategy = Use Cases (where to invest), Tactics = Outputs (what to produce).

### Strategy — investment direction and sequencing

Guiding questions: *Which experiences/capabilities do you compose next? In what order? Validated with whom, and how? **Why this sequence** — what makes this the right order?* The why-this-sequence is the load-bearing Strategy content; a bare ordering with no rationale is a backlog, not a Strategy.

`What good looks like:` describe the shape: "a sequence that references the Architecture explicitly — 'we sequence experience X next because the framework supports skills Y and Z' — with validation logic (which segment, what signal confirms it), not an ad-hoc backlog." This steers toward minimum-viable-depth condition #4 (Strategy references Architecture) and away from architecture-by-default.

### Tactics — concrete delivery

Guiding questions: *What concrete outputs/deliverables? For which specific users or moments? How does delivery personalize per user/segment?* Tactics is the where-the-rubber-meets-road layer — named features, specific artifacts, per-user delivery.

`What good looks like:` "specific, dated or owned deliverables that instantiate the chosen Strategy compositions — concrete enough that someone could pick one up and build it."

### Discipline

- **Pre-fill only seed-stated content.** A seed rich enough to hint at sequencing ("start with transcription, add summary later") can pre-fill a Strategy fragment; most seeds can't, and the stub stays `{to fill}`. Don't invent a roadmap.
- **Don't let the scaffold imply Strategy challenges Architecture.** The guiding questions frame Strategy as operating *within* the framework (informing it with signals), never overriding it — anti-pattern #8 (Strategy challenging Architecture) is a thing the scaffold's framing should not seed.

**Test:** do the Strategy questions ask for *why-this-order* (not just an order), do the Tactics questions ask for *specific* deliverables, and is each stub pre-filled only where the seed actually sequenced or named something?

## Depth recommendation {#depth-recommendation}

Recommend one composition depth — **deep / medium / light / vocabulary-only** — per the framework's `applicability.md` spectrum. In draft, the depth recommendation has a specific job: it tells the author **how much rigor to bring to filling the scaffold**. A deep-depth scaffold should be filled with a full invariant set and named governance; a vocabulary-only scaffold should be filled as shared planning language, not a literal framework. Depth is a function of **scope × actual AI-substrate engagement**, not of how ambitious the seed sounds.

### The spectrum (from `applicability.md`)

| Depth | Fits when | Typical scope | Rigor to bring when filling |
|---|---|---|---|
| **Deep** | Rich skill library (many capabilities), complex interfaces, many invariants, substrate matters and is governed | Product engineering of core AI-first features; shared AI platform | Full composition framework — skills, interfaces, full invariant set, named owner, governance |
| **Medium** | A handful of capabilities, explicit interfaces, core invariants, ongoing but lighter architecture work | AI-enabled function-level work (recruiting AI, CX routing, content systems, forecasting) | Moderate framework — a few capabilities, explicit interfaces, core invariants, named owner; no dedicated governance body |
| **Light** | Small library (often single-skill), simple interfaces, minimal formal invariants | Function-level work with low AI-substrate dependence (standard HR/reporting tooling) | A small real framework + named accountable owner per layer — not "no framework at all" |
| **Vocabulary only** | No formal library; V-A-S-T as shared language for a planning conversation | Company-wide strategy; cross-function alignment; operating-model discussion | Four-layer language for alignment; named accountability per layer; no skill library |

### How to choose

1. **Start from scope.** Company-wide → usually vocabulary-only. Product → medium-to-deep. Function → medium-to-light by AI engagement. WoW → vocabulary-to-light unless the org is large / changes tooling often.
2. **Adjust by AI-substrate engagement.** Within product/function scope, the deciding signal is how much the work *depends on composing AI capabilities under guarantees*. Many composed skills + substrate volatility + personalization → deep. One wrapped API call → light.
3. **State the one signal that decided it**, plus the rigor implication: e.g. "medium — function-scope AI adoption in recruiting with a handful of AI-assisted steps under bias/compliance invariants; bring a moderate capability framework + named owner, not a full governance body."

### The two errors to avoid

- **Forcing deep where light fits (#6).** A seed that's a People-team tool adoption or a single A/B test does not warrant deep composition. Recommending deep here seeds ceremony without value. If the honest depth is light or vocabulary-only, say so — and tell the author *not* to over-build the scaffold.
- **Claiming vocabulary-only where deep is needed (#7).** A genuinely AI-first product seed with many composed skills must not be let off with "vocabulary-only" — that seeds architecture-by-default. Recommend medium/deep and signal (in the Architecture what-good line) that a real framework is expected.

For a near-empty seed, depth is necessarily a *recommendation under uncertainty* — name it as such where the seed is thin ("likely deep, pending how many skills the framework actually needs"), and tie it to the scope you detected.

See `../../../references/anti-patterns.md` #6 and #7 for both error fragments; `applicability.md` for the full spectrum and the minimum-viable-depth floor.

**Test:** name the scope, then name how many AI capabilities plausibly compose under what guarantees. Those two facts pick the depth. Write the reason as those two facts plus the rigor implication.

## Source

Heuristics derived from:
- `vast.md` — "The four layers", commitment-priority ordering ("Intentional, not strict" — Vision-before-Architecture-before-Strategy as priority of commitment), "Vision as committed hypothesis", "Composition depth, not mode switch"
- `governance.md` — "Vision Falsification Protocol" (observable / bounded / owned triggers; 5-step process), accountability per layer (one named neck)
- `glossary.md` — layer definitions, "Composition framework" (four sub-elements), "Vision" (committed falsifiable hypothesis)
- `quick-start.md` — how the framework onboards a newcomer (the four-layer questions per layer — "Why do we exist? / What domains matter? / Where do we invest? / What do we build?"), which shape the scaffold's guiding questions
- `layer-definitions.md` (shared ref) — per-scope content + identifying signals (scope identification; per-scope Architecture guiding questions)
- `applicability.md` — composition-depth spectrum (deep / medium / light / vocabulary-only), depth-to-work matching, minimum-viable-depth floor, common mistakes (#6, #7)
- `vast-essentials.md` (shared ref) — the four layers, triad, invariants/implementations split, composition-framework vocabulary aliases (capability/process framework)
- `anti-patterns.md` (shared ref) — the eight confusions the scaffold's *guidance* should steer the author away from (esp. #1 Vision-as-Use-Case, #2 architecture-by-default, #4 missing triggers, #6/#7 depth mismatch, #8 Strategy-challenges-Architecture)

(Framework canonical paths — `vast.md`, `governance.md`, `applicability.md`, `quick-start.md`, `glossary.md` — are relative to the repo root.) The shared-reference paths cited inline above (`../../../references/...`) are relative to *this file's* location at `skills/vast-draft/references/`.
