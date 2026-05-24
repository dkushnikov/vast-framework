# Why now — the commoditization argument

VAST is not a replacement for Lean Startup, Agile, or MVP-driven development. It is a response to a structural shift that those frameworks were not designed for. This document captures the shift and why it demands a different operating model.

## The shift — code commoditization and personalized software

The cost of writing code has collapsed. LLM-assisted code generation, AI-accelerated development tooling, agent-driven automation — each step has compounded. What used to take weeks now takes days; what took days now takes hours. And importantly: this trajectory is not just about speed. It is about what becomes possible.

When any code can be written on demand, **personalized-by-default software becomes the natural form**. Instead of shipping one product to many users, software begins composing per-user, per-moment experiences. The product is not a fixed artifact; it is a composition generated from a library of atomic capabilities.

This is not a future projection. It is a present direction confirmed by multiple practitioner and investor signals — most explicitly in Jack Dorsey and Roelof Botha's Sequoia piece "From Hierarchy to Intelligence," which describes Block's operational model as exactly this: atomic capabilities plus a composition layer that assembles them per-user, per-moment, at the edge.

The consequence for operating-model design: **what distinguishes a product shifts from "what code you've shipped" to "what compositions your framework enables."**

## What becomes expensive when code is cheap

In the pre-LLM era, the expensive parts of building software were:

- Writing the code (engineer time, craft specialization)
- Iterating (each cycle took weeks; pivots had real cost)
- Architecture migrations (moving between patterns required massive rewrites)

Lean Startup, Agile, and MVP-driven development were rational responses: minimize upfront commitment, ship thin, discover direction through cheap experiments. Architecture was treated as "just enough" because you might rebuild anyway. Vision was emergent because iteration was the only way to find it.

In the post-LLM era, the expensive parts shift:

- **Vision** — what experiences we actually want to enable, for whom, why. Code is fungible; intent about what code to compose is not.
- **Composition architecture** — the skill library, interfaces, invariants. Individual LLMs are fungible; the framework that composes them into consistent, defensible experiences is not.
- **Understanding** — what your company uniquely knows about the domain you're composing in. Julien Bek's Sequoia companion piece captures this: "Today's judgment becomes tomorrow's intelligence." Commoditization moves up the judgment stack; continuous deepening of domain understanding is the only way to stay ahead.

The failure mode of applying pre-LLM operating models (Lean / Agile / MVP) to post-LLM conditions: cheap iteration happens at the Tactics layer, while Vision, Architecture, and Strategy remain implicit. Composition frameworks accumulate by accretion rather than intent. What results is the architecture-by-default pattern — architectural decisions made by default, never named, never challenged, eventually incompatible with the strategy they're supposedly serving.

## What VAST actually claims — and what it doesn't

A careful adversarial review (multi-model council, documented) surfaced that earlier versions of this document oversold the "iteration economics inverted" argument. The stronger, more honest claim is not "iteration is cheap, therefore architecture must precede strategy in strict sequence."

The stronger claim is:

**When code commoditizes and personalized software becomes default, the composition framework becomes the durable artifact. Organizing the work of building this framework — deciding what belongs in the library, how skills compose, what invariants hold — requires intentional commitment at the Vision and Architecture layers, because cheap iteration at Strategy and Tactics cannot substitute for missing commitment upstream.**

The claim is about what becomes load-bearing, not about strict sequencing. All four VAST layers iterate continuously. What VAST disciplines is the specific failure mode of running cheap iteration at lower layers while upper layers drift by default.

## What VAST inherits from Lean Startup / Agile / MVP

Real inheritance, not rhetorical rejection:

- **Delivery cadence** — ship fast, learn from real use. VAST preserves and assumes this.
- **Customer-driven discovery** — understand user pain through contact, not guesswork. VAST maps discovery signals into Challenge Flow; they don't bypass the framework, they feed it.
- **Bias for action over deliberation** — preserved where Strategy and Tactics iterate cheaply within committed Vision and intentional Architecture.
- **Pivot as a legitimate response to falsification** — VAST does not forbid pivots; it names the layer at which they happen. A Tactics pivot is routine. A Strategy pivot is a signal worth examining. An Architecture pivot is a major event. A Vision pivot requires revisiting Architecture. Each level of pivot has its own cost and process.

## What VAST updates or inverts

- **Vision: emergent → committed hypothesis with falsification criteria.** Lean Startup's "pivot or persevere" assumed Vision emerges through iteration. VAST treats Vision as upfront commitment — but not as immutable. Vision is a hypothesis with named revision triggers. The discipline is that it's *named*, not that it's *fixed*.
- **Architecture: "just enough" → intentional composition framework.** Lean Startup treated Architecture as something you might rebuild anyway. In a world where the composition framework is the defensible artifact, "just enough" architecture produces what the council rightly calls "convergent churn: fast, confident, wrong." VAST treats Architecture as intentional and load-bearing.
- **Sequencing: emergent through iteration → priority of commitment.** Lean Startup's sequence was whatever the market signals produced. VAST names priority of commitment: Vision before Architecture before Strategy before Tactics. This is not temporal sequence of activity; all layers are active simultaneously. It is priority of intentional commitment — which layer gets named and owned first.

## The probabilistic-substrate objection, addressed honestly

The sharpest objection to VAST from adversarial review: *AI systems are built on volatile probabilistic substrates. Capabilities change every 3 months. You cannot lock architecture without behavioral validation. VAST mandates committing to architecture that will be obsoleted by the next foundation-model release.*

The first attempt at responding to this objection in v2 was: "Architecture is composition framework, designed to abstract over substrate volatility — new LLMs swap underneath, framework persists." A second adversarial review correctly noted this overpromises. Composition patterns themselves can be substrate-coupled — prompt-chaining strategies, orchestration patterns, retrieval architectures don't gracefully degrade when capability shifts (multimodal-native, reasoning-native, agentic-native models). The empirical evidence is real: LangChain's chain-of-prompts approach was substrate-coupled implementation; when models got better at instruction-following, that approach became outdated. DSPy and similar tools moved toward compiling composition based on actual model behavior because static composition fails under substrate change.

The honest response: **the composition framework is not substrate-agnostic; it is substrate-aware, with deliberate separation between what is portable and what is not.** This split is now central to the framework:

- **Composition INVARIANTS** (skill boundaries, quality contracts, fallback policies, trust contracts, observability requirements, safety guarantees) are substrate-portable. They survive substrate change. New foundation model arrives, invariants persist — every skill still must respect them.
- **Composition IMPLEMENTATIONS** (orchestration patterns, prompt strategies, retry values, output format mechanisms, cost optimization) are substrate-coupled. They migrate as substrate evolves. Same invariant (e.g., "skill must return validated structured output") gets re-implemented against new substrate (JSON mode on GPT-5, XML tags on Claude, native structured output API on Gemini).

The framework's architectural contribution is making this distinction explicit. Without it, "the composition framework" is a vague claim that overpromises stability. With it, the framework is honest about which decisions persist and which migrate — and accountability is structured accordingly.

What VAST does require: the composition framework's invariants must be intentional. The decision about what skills exist, what they must guarantee, how they fail safely — this cannot be deferred behind "we'll figure it out when we see what LLMs do next." That deferral is the architecture-by-default pattern VAST exists to prevent. Implementations can and should defer to substrate; invariants cannot.

Substrate volatility is expected. The framework absorbs it at the implementation layer while preserving the invariant layer that makes the composition framework defensibly yours.

## Testable claims — what "working" looks like

VAST's claim is testable at 6-18 month horizons. If the framework operates as intended:

**Success markers:**

- **Vision commitment holds across many cheap iterations.** The Vision statement is referenced when Strategy conflicts with it, not renegotiated every quarter.
- **Composition framework (Architecture) evolves through additions, not rebuilds.** Skills added to library; interfaces refined; invariants adjusted. Not periodic "scrap and rebuild the architecture" cycles.
- **Substrate changes don't cascade.** When a better LLM arrives, it's swapped underneath the composition framework without re-architecting the framework itself.
- **Iterations compound into deeper domain understanding.** What the company knows about its users and their experiences grows measurably. The "compounding understanding" question from Dorsey & Botha gets a concrete answer.
- **Strategy selections respect Architecture constraints.** Product Directors propose compositions the framework supports; architecture changes are signaled explicitly.

**Failure markers (framework not landing):**

- **Architecture keeps being re-done because Vision kept shifting.** Every major architectural choice has been reversed within 12 months.
- **Strategy-to-Architecture signals don't flow.** Challenge Flow is stated but never observed in action. Product Directors bypass architecture; shadow composition patterns emerge.
- **Vision becomes retrospective.** "What we're building" is articulated after the fact based on what shipped, rather than being the anchor shipped against.
- **Substrate volatility cascades into architecture churn.** New LLMs force re-architecture rather than being absorbed by composition abstraction.
- **Iterations produce feature churn, not compound understanding.** Teams ship, observe noise, reverse. Library accumulates orphaned skills rather than coherent composition patterns.

Presence of success markers at 12-18 months = framework has teeth. Presence of failure markers = framework is ceremony, or the conditions it assumes don't hold in this context.

## What is uniquely AI-first about this

Earlier framings located VAST's AI-first specificity in "iteration economics inverted." Adversarial review rightly noted that argument is weak — cheap iteration in general does not imply strict architecture-first sequencing.

The stronger AI-first specificity lives in the **composition-layer observation**, not the iteration-economics argument:

- Traditional software: product surface = shipped artifact. One product to many users.
- AI-first software: product surface = composed experience. Per-user, per-moment composition from library.
- What's durable in the traditional case: system architecture, technology stack, platform capabilities.
- What's durable in the AI-first case: composition framework — skills, interfaces, invariants. This is new, different from traditional architecture, and specifically demanded by the personalization-by-default shift.

If that observation is correct, VAST's claim that Architecture demands intentional upfront commitment is not "Lean Startup is wrong about everything." It is: "Lean Startup was right for its era; the AI-first era changes what constitutes architecture, which changes what is expensive to get wrong, which changes what must be committed upfront."

This is the defensible version of the "why now" argument. It survives the adversarial review's sharpest objections because it does not rest on the weaker iteration-economics claim.

## References

- [`vast.md`](./vast.md) — core framework, motivated by this argument
- [`external-validation.md`](./references/external-validation.md) — Dorsey/Botha and Bek engaged as corroboration of the composition-layer shift; Wardley, Cynefin, DDD, Team Topologies engaged as complementary frameworks
- [`consequences.md`](./references/consequences.md) — political consequences of applying VAST, including composition-framework authority dynamics
