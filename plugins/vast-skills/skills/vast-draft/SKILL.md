---
name: vast-draft
description: 'Scaffold a NEW VAST document from a minimal seed — a scope plus a sentence or two about an initiative — guiding the author through the four layers in commitment-priority order (Vision → Architecture → Strategy → Tactics). Generative, like vast-transform, but the input is near-empty rather than rich prose: the output is a SCAFFOLD (guiding questions + what-good-looks-like + fillable stubs), not a filled doc. Where the seed is silent it provides the question to answer, never an invented answer. Prompts for Vision falsification triggers and recommends composition depth. Use when starting a VAST doc from scratch, when someone has only an idea and a scope and wants the structure to fill in, or asks "help me draft a VAST for this" / "scaffold a VAST" / "I want to write a VAST doc". Triggers: "draft a VAST", "scaffold a VAST doc", "start a VAST for", "new VAST from this idea", "help me write a VAST", "набросай VAST", "создай каркас VAST". Distinct from vast-transform (which reshapes existing prose) and vast-validate (which scores a finished doc).'
---

# vast-draft

## When to use

Invoke when you are **starting a VAST document from near-zero** — you have a scope and a sentence or two about an initiative, and you want the four-layer structure scaffolded so the author can fill it in. The output is a **scaffold**: for each layer, the question to answer + what a good answer looks like + a fillable stub (pre-filled only where the seed actually supplies content).

Common triggers:
- "Draft a VAST for {idea}" / "scaffold a VAST doc"
- "Start a VAST for this initiative"
- "I have an idea and a scope — help me write the VAST"
- "New VAST from this seed"
- "Набросай / создай каркас VAST"

This skill is **generative**, like `vast-transform`, but the two differ by *input richness and output completeness*:

- **`vast-transform`** takes **rich prose** (a pitch, a brief, a backlog narrative) that already contains latent V/A/S/T material and **RESTRUCTURES** it — sorting existing content into layers, extracting the latent Vision. Its output is a *proposed filled doc*.
- **`vast-draft`** takes a **near-empty seed** (a scope + an idea) and **ELICITS** a new doc — it provides the guiding questions and what-good-looks-like *per layer* so the author can author the content. Its output is a *scaffold to fill*, not a filled doc.

The deciding question: **does the input already contain the content, or does it need to be elicited?** Rich prose to sort → `vast-transform`. A seed to grow → `vast-draft`. If the input already has V/A/S/T headings and you want it scored, use `vast-validate`; if you want a nested pair checked for cascade, use `vast-connect`.

> **V1 is a single-pass scaffold** — one invocation produces the full four-layer scaffold from the seed. Interactive multi-turn use (the author fills Vision, then you scaffold Architecture against their committed Vision, layer by layer) is a *possible* usage but not required; the single-pass scaffold is the default deliverable.

## The cardinal rule — scaffold, don't fabricate

`vast-draft` works from a seed that is mostly silent. The failure mode to avoid is **filling that silence with invented content** — authoring a Vision, naming invariants, or inventing falsification triggers the author never committed to. A confidently-fabricated scaffold is worse than an honest one: it launders the skill's guesses as the author's commitments, and those propagate downstream as if real (this is how anti-pattern #1, Vision-as-Use-Case, and #7, vocabulary-only-where-deep-is-needed, get *manufactured*).

The discipline, in every section:

- **Where the seed gives content** → pre-fill the `Answer:` stub with it (lifted, lightly tightened — never embellished beyond what was said).
- **Where the seed is silent** → the `Answer:` stub stays a blank stub (`{to fill}`), and the value the skill adds is the **guiding question** + **what good looks like** — *the question to answer, not an invented answer*.
- **Never** write a declarative Vision, a concrete invariant, or a specific falsification trigger that the seed did not supply. Prompt for them.

Phrase guiding questions as questions ("What experience does this enable, and for whom?"), and what-good-looks-like as a *description of a good answer's shape* ("a falsifiable hypothesis naming the enabled experience + the audience + why it matters"), never as the answer itself.

## VAST recap (condensed)

The scaffold is built **top-down in commitment-priority order** — Vision → Architecture → Strategy → Tactics — because that is VAST's load-bearing sequence: commitment at Vision and Architecture is what makes the lower layers meaningful. The four layers and what each owns:

| Layer | What it owns — and what the scaffold elicits |
|---|---|
| **Vision** | What experiences we enable, for whom, why — as a *committed falsifiable hypothesis* with named revision triggers. Scaffold elicits the why / for-whom / enabled-experience **and** prompts for falsification triggers. |
| **Architecture** | The composition framework (product) or capability/process framework (function / company / WoW): the durable structure work is built on — skills, interfaces, invariants, implementations. Scaffold elicits the scope-appropriate structure. |
| **Strategy** | Investment direction and sequencing — which experiences/capabilities to compose next, in what order, validated how. Scaffold elicits the sequencing questions. |
| **Tactics** | Concrete delivery — specific compositions/outputs for specific users/moments. Scaffold elicits the concrete-delivery questions. |

Two cross-cutting facts the scaffold respects: **Vision is a committed falsifiable hypothesis** — so the Vision section *always* prompts for triggers (observable + bounded + owned), and never invents them; and the four layers form a **commitment-priority order**, not a temporal sequence — so the scaffold tells the author to commit Vision before investing in the layers below it.

For the four layers, the triad (Outcomes / Use Cases / Outputs), and the invariants/implementations split, see `../../references/vast-essentials.md`. For the four-scope model (company / product / function / WoW) and per-scope identifying signals, see `../../references/layer-definitions.md`. The eight common confusions the *scaffold's guidance* should steer away from are in `../../references/anti-patterns.md`. The composition-depth spectrum (deep / medium / light / vocabulary-only) is in the framework's `applicability.md`; the Vision Falsification Protocol (what a good trigger looks like) is in `governance.md`. Detailed draft heuristics are in `references/draft-heuristics.md` — read those for the per-step guiding-question banks and what-good-looks-like phrasing.

## Process

For the seed under scaffolding, build the scaffold **top-down in V→A→S→T order**:

1. **Identify scope** — company / product / function / WoW — from the seed. The scope decides what each layer's guiding questions and what-good-looks-like should say (a product Architecture asks for a composition framework; a company Architecture asks for org design). If the seed names the scope, use it; if it's ambiguous, ask, or state the assumption explicitly and proceed. (See `references/draft-heuristics.md#scope-identification`; per-scope signals in `../../references/layer-definitions.md`.)
2. **Vision first (commitment-priority gate)** — scaffold the Vision section with guiding questions (what experience / for whom / why) and **prompt for falsification triggers** (2-5 observable + bounded + owned conditions, per `governance.md`). Make explicit, in the doc's lead and the commit-order Note, that **Vision should be committed before the lower layers are meaningful**. Pre-fill the `Answer:` only with what the seed actually states; otherwise leave the stub and lead with the question. (See `references/draft-heuristics.md#vision-first`.)
3. **Architecture scaffold** — guide *per scope*: for **product**, the composition framework split (skill library / interfaces / invariants / implementations); for **company**, org / capability-portfolio design; for **function**, the function's capability set (use the "capability framework" alias); for **WoW**, the process framework. Ask the scope-appropriate structural questions; do not invent skills or invariants. (See `references/draft-heuristics.md#architecture-scaffold`.)
4. **Strategy + Tactics scaffold** — **Strategy** = investment-direction and sequencing questions (which to compose next, in what order, validated how — and *why this order*); **Tactics** = concrete-delivery questions (which specific outputs, for which users, at which moments). Same scaffold shape (question + what-good-looks-like + stub). (See `references/draft-heuristics.md#strategy-tactics-scaffold`.)
5. **Recommend composition depth** — deep / medium / light / vocabulary-only — so the author knows *how much rigor to bring* to filling the scaffold. Match depth to scope × actual AI-substrate engagement; don't force deep where light fits (#6) or claim vocabulary-only where deep is needed (#7). State the one signal that decided it. (See `references/draft-heuristics.md#depth-recommendation`.)
6. **Emit the scaffold** per Output format below, with the Notes block recording scope, depth, what-the-seed-gave, and the commit-order reminder.

## Heuristics

| # | Heuristic | One-liner | Detail reference |
|---|---|---|---|
| 1 | Scope identification | Read the seed against per-scope signals; pick ONE scope (company / product / function / WoW). If the seed names it, use it; if ambiguous, ask or state the assumption and proceed — the scope sets every downstream guiding question. | `references/draft-heuristics.md#scope-identification` (primary); `../../references/layer-definitions.md` (per-scope signals) |
| 2 | Vision first | Scaffold Vision with why / for-whom / enabled-experience questions AND a falsification-trigger prompt (observable + bounded + owned). Pre-fill only what the seed states; never author a Vision or invent triggers. Make the commitment-priority gate explicit. | `references/draft-heuristics.md#vision-first` (primary); `governance.md` (Falsification Protocol); `../../references/anti-patterns.md` (#1 Vision-as-Use-Case, #4 missing triggers) |
| 3 | Architecture scaffold | Ask scope-appropriate structural questions: product → composition framework (skills / interfaces / invariants / implementations); company → org/capability design; function → capability set; WoW → process framework. Don't invent structure to fill the stub. | `references/draft-heuristics.md#architecture-scaffold` (primary); `../../references/vast-essentials.md` (composition framework; invariants/implementations; aliases); `../../references/layer-definitions.md` (per-scope Architecture content) |
| 4 | Strategy + Tactics scaffold | Strategy = investment-direction/sequencing questions (what next, what order, validated how, why this order); Tactics = concrete-delivery questions (which outputs, which users, which moments). Same question + what-good + stub shape. | `references/draft-heuristics.md#strategy-tactics-scaffold` (primary); `../../references/vast-essentials.md` (triad) |
| 5 | Depth recommendation | Recommend deep / medium / light / vocabulary-only by scope × AI-substrate engagement, so the author knows how much rigor to bring. One-line reason naming the deciding signal. Don't force deep on light work (#6) or claim vocabulary-only where deep is needed (#7). | `references/draft-heuristics.md#depth-recommendation` (primary); `../../references/anti-patterns.md` (#6, #7); `applicability.md` (depth spectrum) |

> Heuristic numbers are stable identifiers, not an execution order. The Process runs scope → Vision → Architecture → Strategy+Tactics → depth, top-down in commitment-priority order. Reference heuristics by **name** (e.g. "Vision first") if you annotate the output.

## Output format

Produce a markdown scaffold with this exact structure — guiding questions + what-good-looks-like + fillable stubs, **not** a filled doc:

```markdown
# VAST Draft — {title} ({scope} scope)

> Fill top-down: commit Vision before investing in the layers below it. Each section gives the question to answer + what a good answer looks like. Stubs marked {to fill} are yours to author — where this scaffold left a question instead of an answer, that's deliberate: the seed didn't say, so the scaffold asks.

## Vision
**Answer:** {seed-derived starter if the seed states a why/for-whom/experience, else `{to fill}`}
**Guiding questions:** {what experience does this enable? for whom (which segment)? why does it matter / what changes for them?}
**What good looks like:** {a committed falsifiable hypothesis — names the enabled experience + the audience + why; not a feature list, not a slogan}
**Falsification triggers (required):** {to fill — name 2-5 conditions under which you'd revisit this Vision, each observable (a real metric) + bounded (a threshold + duration) + owned (a named role). Prompt only — do not invent thresholds.}

## Architecture
**Answer:** {seed-derived starter if any, else `{to fill}`}
**Guiding questions:** {scope-appropriate — product: what skills/capabilities exist, how do they compose (interfaces), what invariants must always hold, what's substrate-coupled (implementations)? function: what tools/processes/AI-integrations make up the capability set? company: what org capabilities/team structure deliver the Vision? WoW: what process building blocks + durable principles?}
**What good looks like:** {a real framework, even if minimal — at least skill/capability boundaries + ≥1 quality invariant + ≥1 fallback invariant + a named accountable owner; not "we'll figure it out as we go"}

## Strategy
**Answer:** {seed-derived starter if any, else `{to fill}`}
**Guiding questions:** {which experiences/capabilities to compose next? in what order? validated with whom / how? why this sequence?}
**What good looks like:** {a sequence that references the Architecture explicitly — "we sequence X because the framework supports skills Y and Z" — with validation logic, not an ad-hoc backlog}

## Tactics
**Answer:** {seed-derived starter if any, else `{to fill}`}
**Guiding questions:** {what concrete outputs/deliverables? for which specific users or moments? how does delivery personalize?}
**What good looks like:** {specific, dated/owned deliverables that instantiate the chosen Strategy compositions — the where-the-rubber-meets-road layer}

---

## Notes
- **Scope:** {detected | assumed} {company|product|function|WoW} — {why this scope; if assumed, what to confirm}
- **Composition depth:** {deep | medium | light | vocabulary-only} — {one-line reason naming the deciding signal; how much rigor to bring to filling the scaffold}
- **What the seed already gave us:** {bullets — which stubs are pre-filled from the seed vs left as questions; `(none)` if the seed filled nothing}
- **Commit-order reminder:** {one line — why Vision (and then Architecture) commitment precedes Strategy/Tactics: downstream layers are meaningless against an uncommitted Vision / implicit Architecture}
```

Always include **all four Notes fields**. Where a field is empty, write `(none)` — keep every field present so the Notes block is identical in shape across content-rich and near-empty seeds (mirrors the sibling skills' empty-state discipline).

The four layer sections always appear, each with all four sub-fields (`Answer` / `Guiding questions` / `What good looks like`; Vision additionally `Falsification triggers`). A section whose `Answer` is `{to fill}` is the normal case for a thin seed — the guiding questions are the deliverable there, not a defect.

## Examples

See:
- `../../examples/13-draft-product/` — a product-scope seed (a one-line AI meeting-notes summarizer idea) → product scaffold with composition-framework Architecture guidance (skills / interfaces / invariants / implementations), depth deep/medium. Most of the doc is questions; only the bare initiative is pre-filled.
- `../../examples/14-draft-function/` — a function-scope seed (a People team wanting AI in recruiting) → function scaffold using the capability-framework Architecture alias, depth medium/light. Shows the scope-shift in the Architecture guiding questions.
- `../../examples/15-draft-company/` — a company-scope seed (a two-line 3-year company ambition) → company scaffold with org-capability-portfolio Architecture, depth vocabulary-only/light, heavy emphasis on Vision falsification-trigger prompting (the company-scope Vision is where triggers matter most and seeds most often omit them).
