# VAST transform heuristics — detailed

For use by `vast-transform` SKILL.md. Detail behind the condensed heuristics table. One section per step, anchored to match the SKILL.md detail-refs.

`vast-transform` is **generative**, not analytical: it produces a proposed VAST document from prose. These heuristics govern *how to construct* each part of that document — they are not Pass/Warn/Fail rules. The governing discipline throughout: **extract what the prose actually says; flag what it lacks; never fabricate commitment the author did not make.** A confidently-invented Vision is worse than an honestly-flagged absent one.

The five steps run in order: scope → Vision → layer mapping → depth → gaps. Scope is decided first because it determines what each layer should contain.

## Scope identification {#scope-identification}

Pick **one** scope for the proposed doc: company / product / function / ways-of-working (WoW). The scope determines what "Architecture", "Strategy", etc. should contain (a company Architecture is org design; a product Architecture is a composition framework), so it must be settled before mapping.

Match the prose against the per-scope identifying signals in `../../../references/layer-definitions.md`. Compressed cues:

- **Company:** "market stance", "why this company exists", "capability portfolio", "org design", "allocation to functions and bets", "team archetypes", "re-org", "CEO / leadership team".
- **Product:** "composition framework", "skill library", "AI substrate / model / LLM", "invariants and implementations", "which experiences to compose next", "personalized instance delivery", "CPO / CTO / PM / EM".
- **Function:** "VP {Marketing/CX/Ops}", "the function's capability set", "tools/processes/AI integrations of a single function", "invest in next within the function", domain-native framings (ATS, forecasting tooling, CX routing).
- **WoW:** "review meetings / decision artifacts / planning cycle / retrospective", "tool migration (Slack → …)", "async-first / decisions-as-artifacts / blameless postmortems", "cadences / 1-1s / all-hands / RFC format".

### When the prose mixes altitudes

Prose often blends scopes — a company-level ambition ("become the default platform for X") sitting next to product-feature detail ("the compose modal has a Send button"). Do **not** silently average them into a vague middle.

- **Pick the dominant scope** — the one most of the load-bearing content operates at, usually the scope of the *deliverables* (what actually gets built), since that is where the transform has the most concrete material to map.
- **Record the conflict as an open question** in the Notes block: name both altitudes, state which one you transformed at, and ask the author to confirm or split. Example: "Prose mixes company-level ambition (default platform globally) with product-feature detail (inbox UI) — transformed at product scope; the company ambition belongs in a separate company-scope Vision. Confirm split."
- The altitude conflict is itself a finding. Surfacing it is the value; resolving it is the author's call.

**Test:** read off the scope signals you matched. If they cluster at one scope → that's the scope. If they split across two → pick the deliverable scope, flag the conflict.

## Vision extraction {#vision-extraction}

The Vision answers **what experiences we enable, for whom, and why**. The transform's job is to *find* that in the prose — not to author a north star the author never committed to.

### Three outcomes

1. **Extracted (status: extracted).** The prose states a clear why + for-whom + enabled-experience. Lift it, tighten the language, drop the feature noise. Signals it's present: "we believe {users} struggle with {pain}", "so that they can {outcome}", "for {segment} who {problem}". Render it as the Vision verbatim-in-spirit; you may compress, you may not invent.
2. **Partially inferred (status: partially inferred).** The prose states *some* of the triple — e.g. an enabled-experience but no for-whom, or a for-whom but a fuzzy why. Lift what's there; mark the inferred/missing part inline (e.g. "for whom: not stated — inferred as {segment} from the deliverables; confirm"). Status is "partially inferred", not "extracted".
3. **ABSENT (status: ABSENT — candidate offered).** The prose is *purely* features/deliverables/tasks with **no** stated purpose, no for-whom, no enabled-outcome — only "what we will build". This is the critical case.

### Handling absence WITHOUT fabrication

When the Vision is absent, the failure mode to avoid is confabulation: writing a confident, declarative Vision that the author never endorsed, which then propagates downstream as if it were a real commitment (this is how anti-pattern #1, Vision-as-Use-Case, gets *manufactured* rather than merely detected).

Instead:

- **Mark the Vision section with a single clearly-labeled candidate**, prefixed exactly `⚠️ CANDIDATE (confirm):`. The label is load-bearing — it tells every downstream reader this is a suggestion, not a commitment.
- **Derive the candidate from the deliverables** — "given that the prose builds {X, Y, Z}, the implied purpose might be {inferred why} for {inferred who}" — and say so. Show the inference, don't hide it.
- **State, in the candidate, that it must be confirmed or replaced before use.**
- **Set Vision status to `ABSENT (candidate offered — confirm before use)`** in the Notes.
- **Add "no stated Vision" to Gaps surfaced** and "Confirm or replace the candidate Vision" to Open questions.

A candidate Vision is phrased tentatively ("might be", "appears to serve", "candidate purpose"), never declaratively ("we enable", "our north star"). The phrasing difference is how the reader tells a real extracted Vision from an inferred candidate at a glance.

### Falsification triggers are NOT invented here

Even when a Vision is cleanly extracted, the prose rarely supplies falsification triggers (observable + bounded + owned revision conditions). Do **not** invent them. Note their absence in Gaps surfaced ("Vision has no falsification triggers — needs 2-5 observable/bounded/owned conditions"). The transform surfaces the gap; the author fills it. See `../../../references/anti-patterns.md` #4 for what a good trigger looks like — as a *target to flag toward*, not a thing to autofill.

**Test:** can you point at a sentence in the prose stating *why* this exists or *for whom*? Yes → extract. Partially → partially inferred. No → ABSENT + labeled candidate.

## Layer mapping {#layer-mapping}

Sort the non-Vision prose into Architecture / Strategy / Tactics. The triad anchors the sort (`../../../references/vast-essentials.md` §2): Architecture = Outcomes (what domains matter), Strategy = Use Cases (where to invest), Tactics = Outputs (what we produce).

### What maps where

- **→ Architecture (structural domains / composition framework).** Content describing the durable structure the work is built *on*: the domains owned, the skills/capabilities and how they compose, the invariants that must always hold, the interfaces. Signals: "the system is structured as", "capabilities", "guarantees", "what must always hold", "the platform provides". For product scope, this is the composition framework (skill library / interfaces / invariants / implementations); for company scope, org design; for function scope, the function's capability set; for WoW, the process framework. Adapt per `../../../references/layer-definitions.md`.
- **→ Strategy (investment direction / sequencing).** Content choosing *where to apply effort and in what order*: "first we'll ship X, then Y", "prioritize segment Z", "validate with cohort", "invest in", "front-load". The *why-this-sequence* is the Strategy content; if only an ordering with no rationale is present, map it and note the missing rationale.
- **→ Tactics (concrete deliverables).** Named features, screens, specific artifacts, per-user/per-moment delivery. Signals: enumerated features, UI elements, dated artifacts, "for a user who {X}, the flow does {Y}".

### Discipline while mapping

- **Don't pad a thin layer.** If the prose gives no Architecture, the Architecture section says so and states what a complete one needs — it does not get backfilled with restated features. An empty layer is a finding (feed it to Gaps), not a blank to fill.
- **Don't promote a feature to Architecture to fill the section.** "We'll build a draft button" is Tactics; restating it under Architecture as "draft capability" with no skill boundary / invariant / interface is anti-pattern #2 (Architecture-by-default) — the framework stays implicit while a deliverable poses as structure. Only map to Architecture content that actually describes durable structure.
- **Down-map when the prose over-claims.** If the prose calls something "our architecture" but it's a UI screen list, map it to Tactics and note the mislabel — the transform corrects altitude, it doesn't honor the input's own (wrong) labels.
- **A deliverable can imply an Architecture element without being one.** "Drafts never send automatically" stated among features is actually an *invariant* (a safety guarantee) — lift it up to Architecture. Read deliverables for latent structural commitments and promote those (the inverse of the don't-promote rule: promote genuine invariants, not restated features).

**Test for each prose chunk:** is this *what we build on* (Architecture), *where/when we invest* (Strategy), or *what we ship* (Tactics)? Place it; if a layer ends up empty, that's the gap-surfacing step's input.

## Depth recommendation {#depth-recommendation}

Recommend one composition depth — **deep / medium / light / vocabulary-only** — per the framework's `applicability.md` spectrum. Depth is a function of **scope × actual AI-substrate engagement**, not of how ambitious the prose sounds.

### The spectrum (from `applicability.md`)

| Depth | Fits when | Typical scope |
|---|---|---|
| **Deep** | Rich skill library (many capabilities), complex interfaces, many invariants, substrate matters and is governed | Product engineering of core AI-first features; shared AI platform |
| **Medium** | A handful of capabilities, explicit interfaces, core invariants, ongoing but lighter architecture work | AI-enabled function-level work (AI-assisted CX routing, marketing content systems, finance forecasting) |
| **Light** | Small library (often single-skill), simple interfaces, minimal formal invariants | Function-level work with low AI-substrate dependence (standard HR/reporting tooling) |
| **Vocabulary only** | No formal library; V-A-S-T as shared language for a planning conversation | Company-wide strategy; cross-function alignment; operating-model discussion |

### How to choose

1. **Start from scope.** Company-wide → usually vocabulary-only. Product → medium-to-deep. Function → medium-to-light by AI engagement. WoW → vocabulary-to-light unless the org is large / changes tooling often.
2. **Adjust by AI-substrate engagement.** Within product/function scope, the deciding signal is how much the work *depends on composing AI capabilities under guarantees*. Many composed skills + substrate volatility + personalization → deep. One wrapped API call → light, even at product scope.
3. **State the one signal that decided it.** The output's depth reason is one line naming the deciding factor: "deep — multiple composed AI skills (draft/summarize/classify) with safety invariants and substrate that will migrate" or "vocabulary-only — company-wide strategic ambition, no skill library in play".

### The two errors to avoid

- **Forcing deep where light fits (#6).** Don't recommend deep composition (full invariant set, governance) for a single-skill function tool or an A/B test. That's ceremony without value. If the prose is a pricing-page tweak, the honest depth is light/not-VAST-work — say so.
- **Claiming vocabulary-only where deep is needed (#7).** Don't let a genuinely AI-first product with many composed skills off with "vocabulary-only" — that manufactures architecture-by-default. If the work needs a real framework, recommend medium/deep and flag (in Gaps) that the framework isn't yet specified.

See `../../../references/anti-patterns.md` #6 and #7 for both error fragments.

**Test:** name the scope, then name how many AI capabilities compose under what guarantees. Those two facts pick the depth. Write the reason as those two facts.

## Gap surfacing {#gap-surfacing}

After scope, Vision, mapping, and depth, enumerate what's missing for a **complete** VAST doc. Gaps are honest absences to *report* — never things to invent and slot in. This is the step that keeps the transform truthful: it makes the difference between "here's your prose reshaped" and "here's a finished VAST doc" explicit.

### The standard gap checklist

Run this checklist; report each item that's missing:

- **Vision falsification triggers** — absent almost always in raw prose. Report: "Vision has no falsification triggers — needs 2-5 observable + bounded + owned revision conditions" (see `../../../references/anti-patterns.md` #4).
- **For-whom in the Vision** — if the why is present but the audience isn't. Report: "Vision names no segment — for whom?"
- **Architecture invariants** — if Architecture content exists but states no guarantees / quality contracts / fallback policies. Report: "Architecture lists capabilities but no invariants — needs ≥1 quality + ≥1 fallback contract" (anti-pattern #2 territory).
- **Architecture entirely** — if no structural content was found at all. Report: "No Architecture stated — the prose jumps from intent to deliverables (architecture-by-default risk)".
- **Named accountable owner** — VAST requires one accountable role per layer. Raw prose rarely names them. Report: "No accountable owner named for {layers}".
- **Strategy rationale** — if a sequence is present but no why-this-order. Report: "Strategy gives an ordering but no investment rationale".
- **Scope clarity** — if step 1 found an altitude conflict, restate it here as a gap and as an open question.

### Gaps vs Open questions vs Decisions deferred

The Notes block separates three kinds of incompleteness — keep them distinct:

- **Gaps surfaced** = things *missing for completeness* that have a known shape (a falsification trigger, an invariant). The author knows what to add; they just haven't. Objective absences.
- **Open questions** = things *the author must decide* where the answer isn't obvious from the prose (which scope to commit to, whether the candidate Vision is right, which segment to target first). Genuine forks.
- **Decisions deferred** = choices the prose *explicitly* punts ("we'll pick the model later", "billing is out of scope for v1"). Only populate from explicit punts in the prose; otherwise `(none)`.

Each Notes field is always present; empty ones get `(none)` — identical block shape across clean and gap-heavy transforms.

**Test:** for each checklist item, is it present in the produced doc? If not, it's a gap. For each gap, is its fix a known-shape addition (→ Gaps) or a real decision (→ Open questions)?

## Source

Heuristics derived from:
- `vast.md` — "The four layers", "The triad", "Intentional, not strict" (architecture-by-default), commitment-priority ordering
- `glossary.md` — layer definitions, "Composition framework" (four sub-elements), "Vision" (committed falsifiable hypothesis)
- `governance.md` — "Vision Falsification Protocol" (observable / bounded / owned triggers), accountability per layer
- `layer-definitions.md` (shared ref) — per-scope content + identifying signals for scope identification
- `applicability.md` — composition-depth spectrum (deep / medium / light / vocabulary-only), depth-to-work matching, common mistakes (#6, #7)
- `anti-patterns.md` (shared ref) — the eight confusions the produced output must not exhibit

(Framework paths relative to repo root.) The shared-reference paths cited inline above (`../../../references/...`) are relative to *this file's* location at `skills/vast-transform/references/`.
