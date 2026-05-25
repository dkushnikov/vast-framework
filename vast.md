# VAST — framework definition

_New here? Start with [quick-start.md](quick-start.md) (5 min) or [find your role →](guides/)_

> VAST is a sequencing philosophy, deliberately layered. It builds on what already works — Balanced Scorecard's architecture, OKRs' alignment, Wardley's situational awareness — and adds one thing: an explicit cascade from Vision through Architecture to Strategy before Tactics. When systems grow complex enough that implicit structure stops working, VAST makes it visible.

_For the distilled mandatory core — the invariants that make something *actually* VAST — see [kernel.md](kernel.md)._

## The philosophy

VAST is a framework for operating companies and complex systems in the AI era — a time of unlimited possibilities where choosing the right architecture becomes the critical decision once you've fixed where you want to go.

VAST names a sequencing principle: **Vision → Architecture → Strategy → Tactics**, in that order of commitment priority. The sequence is not waterfall — it describes where to start, not a one-way cascade. In practice, the arrows are bidirectional: Strategy reveals Architecture gaps, Tactics inform Strategy. What makes the sequence load-bearing is logical priority: commitment at Vision and Architecture layers is what makes downstream iteration compound.

The Architecture layer here is not CTO-specific — it's **decision architecture and organizational design**: how domains are structured, how they interact, what constraints govern them, what values enforce boundaries. Product composition (skill libraries, APIs) is one instance of Architecture. Organizational design (team structure, capability maps, value flows) is another. Both are governed by the same principle: make structure explicit before committing to strategy.

VAST applies to any system complex enough that implicit structure stops working — products, organizations, and other domains where intent must become action through structure. See [standard-framework.md](standard-framework.md) for how VAST relates to existing frameworks (BSC, OKRs, Wardley Maps), and [applications.md](applications.md) for cross-domain instantiations.

## The product application

Code is becoming commoditized. LLMs make any software writable on demand; personalized-by-default software is the emerging norm. As the substrate commoditizes, the product surface shifts from "shipped artifact" to "composed experience." In that shift, what persists — what remains defensible and distinctively yours — is not the code you ship but the composition framework you've built: what skills exist in your library, how they compose, what invariants hold across compositions, what experiences the compositions enable.

In product delivery, VAST organizes around this shift. The four layers applied to product:

- **Vision** — what experiences we enable, for whom, why
- **Architecture** — the composition framework: skill library, interfaces between skills, invariants that govern how compositions work
- **Strategy** — which experiences to compose next, sequencing, customer validation
- **Tactics** — specific personalized instances delivered to specific users at specific moments

In an AI-first world, where iteration is cheap and substrate is fungible, the composition framework is the artifact that makes compounding possible.

See [`why-now.md`](./why-now.md) for the full economic and structural argument that motivates this framing.

## The triad: Outcomes / Use Cases / Outputs

Three VAST layers below Vision map to a universal triad:

| VAST layer | Triad role | What it answers |
|---|---|---|
| **Architecture** | **Outcomes** | What domains matter? What are we optimizing? |
| **Strategy** | **Use Cases** | Where do we work? How do we invest? |
| **Tactics** | **Outputs** | What do we concretely produce? |

This decomposition is sharper than alternatives (e.g., OKRs, which compress all three into one construct). Each level sets context for the next. Decisions at lower levels validate through upper levels.

The triad applies across instantiations: in product (business outcomes / user segments / features), in organizations (org domains / strategic priorities / OKRs), and in other complex systems.

**"Use case" has two senses — keep them distinct.** A use case names a product/strategic element — a **JTBD-shaped opportunity**: a **Problem + Solution + Value** triple. The triad's *Use Cases* role is the **strategic** sense — *where we work / how we invest*, a Strategy-layer construct. But "use case" is also used as an **experience / specification** — the description bridging Vision-intent to a build target, which decomposes across Vision (why / for whom) and Tactics/Outputs (the spec). A PM writing a "use case" may be writing a Strategy investment choice *or* a build spec; conflating the two re-creates OKR-conflation at the document level (see [`glossary.md`](./glossary.md) and [`anti-patterns.md`](./anti-patterns.md)).

## What's "architectural" in an AI-first world

Traditional architecture = system design, platform capabilities, technology stack, data model, runtime topology. Important but not uniquely AI-first — architectures of this kind have been the defensible artifact for databases, operating systems, and distributed systems for decades.

**Composition architecture is something new.** In AI-first products, architecture is:

- **Skill library** — what atomic capabilities exist (agents, tools, models, data access patterns, retrieval mechanisms, trust boundaries)
- **Interfaces** — how skills compose, handoff state, share context, chain together into experiences
- **Invariants** — properties that hold across every composition (latency bounds, trust contracts, observability, cost envelopes, safety guarantees)

Specific LLMs are fungible — you can swap GPT for Claude for Gemini without changing your composition framework. The composition framework itself — the unique way your company has structured what can be composed, how, and under what invariants — is the defensible artifact. It is also what accumulates understanding: every iteration on compositions teaches you something about what your users actually need from the library.

This is the form of architecture that matters in an era when the substrate beneath it is volatile and commoditizing. VAST is the operating model that makes this form of architecture intentional rather than accidental.

## The four layers

| Layer | What it owns |
|-------|--------------|
| **Vision** | What experiences we enable. For whom. Why this exists. |
| **Architecture** | The composition framework — skill library, interfaces, invariants, implementations. What can be composed, how, under what guarantees. |
| **Strategy** | Which experiences to compose next. Sequencing. Customer validation. Roadmap of compositions. |
| **Tactics** | Personalized instance delivery. Specific composition moments for specific users. |

Each layer has one named accountable role (singular — one neck) and named responsible roles (plural — doers). Accountability shape is described abstractly here and operationalized at three levels (company / product / function / equivalent) in [`governance.md`](./governance.md). The framework does not require specific titles (CTO, CPO, etc.) to exist in your org; what it requires is that for any given scope of work, each layer has a named accountable person before the work starts.

## What the composition framework actually owns — invariants vs implementations

The Architecture layer owns the composition framework, but the framework itself has two tiers with different durability characteristics. Conflating them is a real risk: it leads to claims that the framework is substrate-agnostic when in reality only part of it is.

**Composition INVARIANTS (substrate-portable, long-lived):**

- **Skill boundaries** — what each skill is responsible for; what it must not do
- **Quality contracts** — what skills must guarantee about their outputs (structured format, schema validity, latency bound, factuality requirements)
- **Fallback policies** — what happens when a skill fails or returns low-confidence output
- **Trust contracts** — what each skill is allowed to do (data access, side effects, escalation)
- **Observability requirements** — what must be measurable about every composition
- **Safety guarantees** — what must never happen (PII leakage, irreversible state changes without confirmation, untrusted code execution)

These are framework decisions that persist across substrate changes. New foundation models swap underneath, but the invariants remain — every skill still must respect the boundaries, contracts, fallbacks, and safety constraints.

**Composition IMPLEMENTATIONS (substrate-coupled, evolves with substrate):**

- **Orchestration patterns** — chain-of-prompts vs single multi-step agent vs compiled DSPy-style optimization
- **Prompt engineering strategies** — how to elicit reliable behavior from the current substrate
- **Specific retry / timeout values** — tuned for current model latency and error profile
- **Output format mechanisms** — JSON mode on one model, XML tags on another, structured-output API on a third
- **Cost optimization techniques** — model selection, caching strategies, batching tuned to current pricing
- **Latency tuning** — assumes specific substrate response characteristics

These migrate as substrate evolves. They are not framework-level commitments; they are implementation choices that change as model capabilities change.

**Why the split matters.** Earlier VAST formulations treated the composition framework as a single substrate-agnostic layer. Adversarial review correctly noted that this overpromises: the empirical evidence (LangChain → DSPy industry transition) shows that composition implementations have a half-life as substrate evolves. What persists are the invariants. What migrates are the implementations.

The Architecture accountable role owns both, but treats them differently:

- **Invariants change rarely and deliberately.** Adding or modifying an invariant is a major Architecture decision through governance.
- **Implementations migrate continuously as substrate evolves.** This is normal Architecture work, not a major decision per migration.

When a new foundation model arrives: implementations can be re-engineered against it without re-opening invariant decisions. When a market or capability shift requires changing what skills are even possible (e.g., reasoning-native models eliminating the need for explicit chain-of-thought orchestration as separate skills): that's an invariant-level change, governance-heavy.

This split is the framework's honest answer to "doesn't substrate volatility break the composition layer?" Implementations absorb substrate volatility. Invariants persist through it. The framework is not substrate-agnostic; it is substrate-aware with deliberate separation of what is portable from what is not.

## Intentional, not strict

Earlier versions of VAST emphasized "strict sequence" — "no other way, never differently." On honest adversarial review, that rhetoric conceded too much to waterfall pattern-matching. Reviewers heard "strict sequence" and read it as phase-gate, BDUF, or Rational Unified Process — frames that VAST does not actually match but that the rhetoric invited.

The revised claim is more precise: V → A → S → T describes **intentional priority of commitment**, not sequential phase gates. All four layers operate continuously. Tactics iterate constantly. Strategy adjusts as evidence accumulates. Architecture evolves as skills are added to the library and new composition patterns emerge. Vision revises when the Vision itself fails falsification tests.

What VAST disciplines is different from what waterfall disciplined:

- Waterfall: no Strategy work until Architecture is complete; no Tactics until Strategy is complete. Phase gates.
- VAST: no Architecture without intentional Vision commitment (else Architecture drifts to defaults); no Strategy without intentional Architecture (else Strategy selects compositions the framework doesn't support); no Tactics without intentional Strategy (else Tactics ships without coherent direction).

"Before" means priority of commitment, not temporal blocking of activity. All layers are active simultaneously. What's forbidden is running cheap iteration on the lower layers while the upper layers are implicit, unnamed, or unowned. That specific failure mode is the architecture-by-default pattern VAST exists to prevent.

## Vision as committed hypothesis

Vision is why the product exists, what experiences it enables, for whom. Under VAST, Vision is not "emergent through MVP iteration" (Lean Startup stance) and not "fixed commitment never revised" (waterfall stance). It is a **committed hypothesis with explicit falsification criteria and named revision triggers**.

Why committed, not emergent: Architecture codifies Vision by deciding what skills go in the library, what compositions are primary, what invariants are load-bearing. Without upfront Vision commitment, Architecture is designed against a moving target, which produces composition frameworks that don't cohere.

Why hypothesis, not fixed: the Vision may be wrong. The framework does not assume executive omniscience. What it requires is that the Vision is named, committed, and has explicit conditions under which it gets revisited. "We believe we enable X for Y because Z; revise if data shows W" is a Vision statement. "We believe in making people happy" is not.

This distinguishes VAST from both Lean Startup (Vision emerges; pivot or persevere) and waterfall (Vision fixed; execute the plan). Both make the same implicit assumption — that Vision revision is a phase change, not a continuous discipline. VAST names Vision revision as part of the operating model.

## Challenge flow

Not every layer can challenge every other layer. The shape:

- **Vision → challenges Architecture.** If the composition framework doesn't serve the Vision, the CPO (Vision owner) can challenge. Vision is the only layer with downward challenge right.
- **Strategy → informs Architecture.** Product Directors surface signals — customer pain, adoption friction, competitive movement — into the Architecture layer. They do not challenge. They feed knowledge; Architecture decides.
- **Architecture → self-corrects.** The composition framework evolves through skill additions, interface refinements, and invariant adjustments based on signals from all layers plus discovery.
- **Tactics → escalates.** Delivery teams escalate execution blockers that reveal architectural mismatch.

**Principle.** Feedback flows up (inform, not dictate); challenge flows down — but the *only* downward challenge right is Vision's, over Architecture. The V→A→S→T arrows are the commitment cascade, not a license for each layer to challenge the one below.

See [`governance.md`](./governance.md) for how Challenge Flow operates across composition depths.

## Delivery, not discovery

VAST is a **delivery** framework. Discovery — testing hypotheses, prototyping, customer validation — does not need VAST. You can test anything without the composition framework being stable. But the moment you move from "we validated this composition works for this user segment" to "we're building and scaling this composition across the library" — V→A→S→T.

Discovery generates signals. Signals enter VAST through the discoverer's layer and follow Challenge Flow rules:

- **PM discovered** (prototype showed an adoption problem) → signal through Strategy → informs Architecture.
- **Engineer discovered** (prototype showed a composition pattern breaks under scale) → signal through Architecture → self-corrects.
- **CPO discovered** (market shift, user behavior change) → signal through Vision → challenges Architecture.
- **EM discovered** (execution blocker rooted in composition-framework mismatch) → signal through Tactics → escalates.

Discovery doesn't bypass Challenge Flow. Discovery is the signal generator; VAST is the signal processor.

**Graduation path:** discovery → validated → delivery decision → VAST kicks in.

## Matryoshka — recursive composition

Once the top-level composition framework is validated, component teams operate within its invariants and interfaces. If a component grows in scope to warrant its own direction, it recursively gets its own V → A → S → T inside: its own local Vision for what experiences it enables, its own local Architecture (sub-library of skills + local composition patterns), its own Strategy and Tactics.

The critical distinction:

- **Working Matryoshka** = validated top-level composition framework + delegated V→A→S→T per component operating within top-level invariants.
- **False Matryoshka** = delegated autonomy without validated framework. Components invent their own composition patterns, interfaces drift, the library fragments — the multi-service trap adapted to skill composition.

The test: does the component team commit to the top-level invariants? If yes → real Matryoshka. If every component team defines its own handoff protocols, state-sharing patterns, trust contracts — false Matryoshka.

### Recursion threshold — when a scope earns its own V→A→S→T

**Recursion is available, not automatic.** Most work does *not* spawn a nested instance; it's Strategy/Tactics within the parent. Nesting is something a scope *earns*, not a default to apply at every level — a scope earns its own V→A→S→T only when all hold:

- **A distinct, falsifiable Vision** — its own committed hypothesis, not just a slice of the parent's.
- **Local invariants beyond the inherited ones** — guarantees that are its own, not only the parent's it operates within.
- **Clean accountability** — one accountable owner per layer (the Kernel floor); at small scope one person may hold several layer accountabilities.
- **Persistence** — a sustained scope, not a one-off effort (a one-shot is Tactics).

**Termination (the usual case):** a scope with no Vision distinct from its parent, no local invariants, and the parent's ownership is **not** a nested VAST — it's Strategy/Tactics *of* the parent. **A feature is the typical termination point:** most features are Use-Cases (Strategy) and Outputs (Tactics) of the product's VAST, not their own nesting. (This mirrors the *Platform threshold* in [`applicability.md`](applicability.md) — a defensive bar that stops everything from claiming its own recursion.)

### The mechanics compose across depths

For scopes that *cross* the recursion threshold, each operating mechanic nests the same way the layers do:

- **Kernel** — every nested instance that claims VAST honors the same [Kernel](kernel.md) floor; Kernel commitments are scope-portable, while the parent's Architecture invariants are inherited constraints at the child boundary.
- **Accountability** — the one-accountable-owner-per-layer rule remaps at each scope; a cross-scope dispute names the parent owner who holds the decision.
- **Handoffs** — the constraint-bearing parts of the parent's Architecture — invariants, interfaces, skill boundaries, values-as-constraints — are the child's *inherited constraint*; within that, the child runs its own V→A→S→T [layer handoffs](layer-handoffs.md).
- **Fitness** — the parent's Architecture-[fitness](fitness.md) question is a practical false-Matryoshka check: can nested components be supported while preserving the parent's invariants and interfaces, or are they drifting into shadow patterns?
- **Escalation** — when a child hits a use-case the parent's Architecture can't support, it routes *up* through the [Challenge & Escalation Protocol](governance.md) — informing the parent's Architecture for a gap, or escalating to the parent's Vision for a scope change — rather than forking its own contracts. So false Matryoshka has two forms: delegating *before* a validated parent Architecture exists is **AP-01** (architecture-by-default) at cross-scope scale; overriding an *existing* parent Architecture instead of routing is the cross-scope analogue of **AP-12**.

## Composition depth, not mode switch

Earlier versions distinguished "VAST Strict" (product-engineering, substrate-heavy) from "VAST Lite" (function-level, loose substrate). On adversarial review, the two-mode split conceded the core claim was narrower than presented — if Lite is "shared vocabulary + common sense," it undermines the framework's force.

The revised framing: VAST applies as a **spectrum of composition depth**, not a binary mode switch.

- **Deep composition** (product engineering, shared AI platform) — rich skill library, complex interfaces, many invariants, substantial architecture investment
- **Medium composition** (AI-enabled function-level work — Marketing content systems, CX routing, Finance forecasting tools) — moderate skill library, explicit interfaces, core invariants
- **Light composition** (function-level work with minimal AI substrate dependence) — small library or single-skill usage, simple interfaces
- **Compositional vocabulary only** (company-wide strategic discussions) — four-layer language for alignment, no formal library

Same discipline at every depth: Vision committed, Architecture intentional, Strategy operates within, Tactics delivers. Different richness of the composition framework.

See [`applicability.md`](./applicability.md) for the composition-depth × organizational-scope decision guide.

## Relation to adjacent frameworks

VAST does not exist in isolation. Several prior frameworks address adjacent questions; VAST complements rather than replaces them:

- **Domain-Driven Design** (Evans) — bounded contexts are the skill-library-per-domain in our framing. DDD's aggregate boundaries and interface design translate directly to composition interface design. VAST builds on DDD at the AI-composition layer.
- **Team Topologies + Inverse Conway Maneuver** (Skelton & Pais) — team types deliver the composition framework. If Architecture is composition framework, Team Topologies tells you what team structures produce it.
- **Wardley Mapping** — situational awareness about where commoditization happens in your value chain. VAST is how to organize product when code-generation commoditizes; Wardley tells you which components in your map face this pressure first. Complementary, different axes.
- **Cynefin** (Snowden) — the composition-layer framing places AI-first product work squarely in Cynefin's Complex domain (probe-sense-respond). VAST's Discovery-vs-Delivery boundary matches Cynefin's Complex-vs-Complicated distinction. Discovery probes the Complex; delivery stabilizes validated compositions into Complicated domain at the composition level.

These are explicitly acknowledged. Engagement with them is load-bearing for VAST's intellectual legitimacy, not optional.

See [`external-validation.md`](./references/external-validation.md) for detailed engagement with each.

## Tactics — inherited execution tempo

Tactics owns *personalized instance delivery* — specific compositions for specific users at specific moments. Its **operating tempo is inherited, not invented by VAST.** This is where Agile, Scrum, sprints, Kanban, and the product-delivery lifecycle live — and VAST is **agnostic to which**.

What VAST fixes at Tactics is *what the layer owns* (instance delivery) and *that* it runs an explicit execution loop — **not** the cadence mechanic. (The agentic SDLC below is a *compatible guide*, not a Kernel requirement.) Sprint-vs-Kanban, sprint length, the ceremony set: implementation choices, fungible, chosen per team. Mandating one would be a Kernel non-goal (a prescribed delivery cadence); integrating with whichever you already run is an [Adapter](./kernel.md). The precision is about ownership + execution tempo, not about prescribing how a team iterates.

## Relation to agentic SDLC

Within each VAST layer, execution runs via an agentic SDLC cycle: Think → Decide → Execute → Log → Mature. VAST is the *priority* framework (which layer commits what, in what intentional order). SDLC is the *operating tempo* inside each layer:

- At **Architecture** layer: SDLC cycles through skill-library additions, interface refinements, invariant adjustments.
- At **Strategy** layer: SDLC cycles through composition-selection and customer validation.
- At **Tactics** layer: SDLC cycles through personalized-instance delivery.

The connection is acknowledged but formalized separately. For now: VAST is the frame of priorities; SDLC is the motion inside each frame.

**Where the SDLC and discovery sit in the INVARIANTS/IMPLEMENTATIONS split.** The execution discipline is itself substrate-coupled. The specific cycle (Think → Decide → Execute → Log → Mature), the discovery method that feeds it, the cadence and ceremonies — these are *implementations*: chosen per team, migrated as tooling evolves, never prescribed by VAST. What is *invariant* is thinner and substrate-portable: **each layer runs an execution loop that closes.** Log records what happened; the loop is only fit when that record becomes extracted learning and a revised next bet — the Study step a bare Log → Mature omits. Run Scrum, P3.express, or a bespoke cycle; discover by any method — but a loop that logs without studying is unfit (it is what [`fitness.md`](fitness.md) catches at Tactics), because speed of execution without speed of learning compounds nothing. *How* discovery is run, and *what quality bar* it must clear before its signals become load-bearing, are likewise implementations — owned at the layer discovery feeds, not VAST invariants.

## Relation to OKRs

OKRs are complementary, not overlapping. OKRs express measurable commitments at each VAST layer; VAST prescribes accountability and priority. See [`okrs.md`](./references/okrs.md).

## Consequences

Applying VAST produces structural and political effects — middle-management sorting (routing roles become redundant; composition specialists and domain owners strengthen), authority shifts (composition-framework authority consolidates to CTO; Product Director scope narrows to customer-signal + composition-selection), political dynamics (framework provides cover for decisions that would otherwise face resistance, and equal risk that it becomes composition-framework gatekeeping that forbids legitimate strategic pivot). These are named explicitly rather than discovered mid-implementation. See [`consequences.md`](./references/consequences.md).

## Origin and external validation

VAST was formulated at an AI composition platform architecture workshop in April 2026 in response to a specific internal precedent where architectural decisions had been deferred behind product sequencing, producing months of rework. Formalized two days later in a Chief-of-Staff working session; received CPO endorsement the following week.

The composition-layer framing draws directly from Jack Dorsey and Roelof Botha's Sequoia interview "From Hierarchy to Intelligence" — their model of "atomic capabilities + AI composition layer at the edge" is structurally equivalent to VAST's "skill library + composition framework." Julien Bek's companion piece "Services: The New Software" articulates the commoditization argument from the economic side: today's judgment becomes tomorrow's intelligence; what your company uniquely understands is the moat. VAST operationalizes this at framework level.

Additional adjacent frameworks and practitioner signals are consolidated in [`external-validation.md`](./references/external-validation.md), with explicit caveats about what convergent framing does and does not prove.

## Applications

See [`case-studies/`](./case-studies/) for worked examples.

- **001** — AI composition platform architecture at the pilot company (primary pilot).

---

**Status:** framework v3.4 — adds the mandatory Kernel + operating mechanics (anti-patterns, layer handoffs, fitness, self-evolution governance); VAST applied to VAST. De-personalized for public release. Prior art positioning (BSC, Wardley, VSM); Values anchored in Architecture. Case studies in progress; applied validation pending.
