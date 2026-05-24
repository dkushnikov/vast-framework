# VAST

A sequencing framework for product development in AI-first environments. Motivated by the commoditization of code and the shift to personalized-by-default software. Designed to enable agentic scaling — growth through extending the composition library and the agents that execute compositions, rather than primarily through extending human headcount.

**Vision → Architecture → Strategy → Tactics.** Intentional priority of commitment, not strict sequence.

## The framework at a glance

```
       ┌────────────────────────────────────────────┐
       │                  VISION                    │
       │   what experiences enabled, for whom, why  │
       │   committed hypothesis with falsifications │
       └────────────────────────────────────────────┘
                          │
                  challenges │
                          ▼
       ┌────────────────────────────────────────────┐
       │              ARCHITECTURE                  │
       │       the composition framework            │
       │  ┌──────────────────────────────────────┐  │
       │  │ INVARIANTS (substrate-portable):     │  │
       │  │ skill boundaries, quality contracts, │  │
       │  │ fallback policies, trust contracts,  │  │
       │  │ observability, safety guarantees     │  │
       │  └──────────────────────────────────────┘  │
       │  ┌──────────────────────────────────────┐  │
       │  │ IMPLEMENTATIONS (substrate-coupled): │  │
       │  │ orchestration patterns, prompts,     │  │
       │  │ retry values, format mechanisms,     │  │
       │  │ cost optimization                    │  │
       │  └──────────────────────────────────────┘  │
       └────────────────────────────────────────────┘
              ▲                          │
       informs│                  enables │
              │                          ▼
       ┌────────────────────────────────────────────┐
       │                STRATEGY                    │
       │   which experiences to compose next        │
       │   sequencing, customer validation          │
       └────────────────────────────────────────────┘
              ▲                          │
     escalates│                  delivers│
              │                          ▼
       ┌────────────────────────────────────────────┐
       │                TACTICS                     │
       │     personalized instance delivery         │
       │     specific composition moments           │
       └────────────────────────────────────────────┘
```

Challenge flows down. Feedback flows up. All four layers iterate continuously; intentional priority of commitment runs V → A → S → T.

## One-paragraph summary

Code is becoming commoditized. LLMs make any software writable on demand; personalized-by-default software is the emerging norm. In this shift, the product surface moves from "shipped artifact" to "composed experience," and what remains defensible and distinctively yours is the composition framework — what skills exist in your library, how they compose, what invariants hold, what experiences they enable. VAST is the operating model that organizes around this shift: four layers (Vision, Architecture, Strategy, Tactics), each with named accountability, with Vision and Architecture committed intentionally upfront because cheap iteration at Strategy and Tactics cannot substitute for missing commitment upstream. The framework's core architectural distinction is between composition INVARIANTS (substrate-portable: skill boundaries, quality contracts, fallback policies) and composition IMPLEMENTATIONS (substrate-coupled: orchestration patterns, prompt strategies). This split makes the framework substrate-aware rather than substrate-agnostic — invariants persist across substrate change; implementations migrate. The end state VAST enables is **agentic scaling** — composition library and agents grow as the company's primary scaling dimension, while human roles concentrate at Vision, Architecture stewardship, and edge judgment.

## How to read this repository

Two tiers of documents. **Foundational** documents define the framework and must be mutually consistent — read them together when learning or applying VAST. **References** are auxiliary — context, integrations with adjacent practice, applied case studies.

### Foundational

The following documents are the framework. Together they form a self-consistent description of what VAST is, how to apply it, and where it applies.

- [`kernel.md`](./kernel.md) — the mandatory portable core. The 7 Principles, 4 Rules, published non-goals, and VAST's own self-falsification criterion. What makes something *actually* VAST; everything else is Guides / Adapters / Experiments.
- [`vast.md`](./vast.md) — framework essence. Four layers, what each owns, the composition-framework definition (invariants vs implementations split), intentional priority, challenge flow, delivery vs discovery, Matryoshka.
- [`anti-patterns.md`](./anti-patterns.md) — the authoritative failure-mode catalogue (13 patterns, `AP-NN` IDs, 5 themes), each mapped to the Kernel principle/rule it violates.
- [`layer-handoffs.md`](./layer-handoffs.md) — the downward V→A→S→T handoffs: what each layer must hand the next, as invariants (medium-agnostic).
- [`fitness.md`](./fitness.md) — thin per-layer fitness questions ("is each layer doing its job?"), extending the Vision Falsification Protocol downward. Not a maturity ladder; not a metric model.
- [`evolution.md`](./evolution.md) — how the framework evolves itself: the Kernel / Guides / Adapters / Experiments lifecycle (canonization test, retirement), refusal protection, and VAST applied to its own changes.
- [`why-now.md`](./why-now.md) — the commoditization argument. Why VAST rather than Lean Startup / MVP / Agile. Iteration economics. Probabilistic-substrate objection addressed via the invariants/implementations split.
- [`applicability.md`](./applicability.md) — combined composition-depth × organizational-scope decision guide. Spectrum (deep / medium / light / vocabulary-only). **Minimum viable depth** — five observable conditions that distinguish "VAST applied" from "VAST vocabulary used." Also: **what VAST does not cover for AI transformation** — explicit scope limits.
- [`governance.md`](./governance.md) — accountability across three levels (company / product / function), abstracted from specific role titles. **Vision Falsification Protocol** — five-step process for what happens when Vision revision triggers fire. Governance-body intensity scales with composition depth.
- [`scaling.md`](./scaling.md) — agentic scaling end-state. Why VAST exists structurally — to enable growth through composition library + agents, not primarily through headcount. Connects to Dorsey/Botha "From Hierarchy to Intelligence" thesis.
- [`architecture-levels.md`](./architecture-levels.md) — Architecture at three levels (product / org-design / ways-of-working). Shows the recurring structural pattern: same VAST shape, different content per level. Closes the gap for non-product readers wondering how Architecture applies in their domain.
- [`applications.md`](./applications.md) — cross-domain instantiations (company transformation) and worked VAST examples per function (CX, Marketing, People, Finance, Operations). Shows what Vision, Architecture (capability framework), Strategy, and Tactics look like in each domain.
- [`standard-framework.md`](./standard-framework.md) — how VAST relates to the standard corporate stack (Vision/Mission/Values/Strategy/OKRs). VAST as extension at complexity threshold, not replacement. OKR critique, Values anchored in Architecture, prior art table (BSC, Wardley, VSM, OODA, TOGAF, NCT), feature comparison matrix.
- [`glossary.md`](./glossary.md) — shared vocabulary used consistently across all foundational documents. Reference when terms are unclear; if a foundational doc uses a term differently from the glossary, file the discrepancy. Includes vocabulary aliases ("composition framework" / "capability framework" / "process framework") for non-product domains.

### References

Auxiliary documents — context, integrations with adjacent practice, applied case studies. Read selectively as needed.

- [`references/consequences.md`](./references/consequences.md) — political and structural effects of applying VAST. Middle-management sorting (routing roles redundant, composition specialists strengthen). Authority shifts. Premature-platformization concern explicitly rejected within VAST scope. Dual-risk calibration (underpowered vs overpowered).
- [`references/okrs.md`](./references/okrs.md) — VAST and OKRs as complementary. OKRs cascade through VAST layers as commitment-and-measurement; VAST prescribes accountability and priority.
- [`references/external-validation.md`](./references/external-validation.md) — engagement with adjacent frameworks. Direct alignment (Dorsey/Botha, Bek). Complementary frameworks (DDD, Team Topologies + Inverse Conway, Wardley Mapping, Cynefin). What VAST does not claim. Caveats about convergent framing as evidence.

### Case studies

- [`case-studies/`](./case-studies/) — applied examples. Each follows the same structure: context, layers, challenge flow in action, what VAST prevented, artifacts, lessons.
  - [`case-studies/001-ai-platform.md`](./case-studies/001-ai-platform.md) — an AI composition platform at the pilot company (primary pilot)

## Suggested reading order

For first-time readers (general):

1. This README
2. [`kernel.md`](./kernel.md) — the mandatory core: what makes something *actually* VAST
3. [`vast.md`](./vast.md) — the full framework essence
4. [`why-now.md`](./why-now.md) — why this matters now
5. [`scaling.md`](./scaling.md) — what end state this enables
6. [`applicability.md`](./applicability.md) — when to use it (and when not)
7. [`governance.md`](./governance.md) — accountability + the Challenge & Escalation Protocol
8. [`glossary.md`](./glossary.md) — verify vocabulary
9. The operating mechanics, as you apply it: [`anti-patterns.md`](./anti-patterns.md), [`layer-handoffs.md`](./layer-handoffs.md), [`fitness.md`](./fitness.md), [`evolution.md`](./evolution.md)
10. References as needed

For non-product leaders (CX, Marketing, People, Finance, Operations leaders):

1. This README
2. [`kernel.md`](./kernel.md) — the mandatory core (what makes something *actually* VAST)
3. [`vast.md`](./vast.md) — framework essence
4. [`applications.md`](./applications.md) — see your function explicitly
5. [`architecture-levels.md`](./architecture-levels.md) — understand how Architecture applies in your domain
6. [`applicability.md`](./applicability.md) — what VAST does and does not cover (for setting realistic expectations)
7. [`governance.md`](./governance.md) — three-level accountability pattern
8. References as needed

For readers who already know the framework and want to verify a specific question:

- "Where is X defined?" → `glossary.md`
- "Does VAST apply to my function?" → `applications.md` (worked example) + `applicability.md`
- "What does Architecture mean at my scope?" → `architecture-levels.md`
- "How does my org structure map?" → `governance.md` (three levels)
- "What does VAST not cover for our AI transformation?" → `applicability.md` (scope-limits section)
- "What's the political effect?" → `references/consequences.md`
- "How does VAST relate to [adjacent framework]?" → `references/external-validation.md`

## Who this is for

Teams building AI-first products where:

- Code is becoming commoditized (LLM-assisted development is routine)
- Personalization-by-default is becoming the product shape
- The substrate is volatile (foundation models evolve quickly)
- The team has some validation of what experiences they enable — i.e., past initial product-market fit discovery
- A Head of Product / Head of Engineering / Head of Technology triad (or functional equivalent) exists with mutual trust

If you are pre-PMF in a domain where Vision is genuinely unknown before market contact, Lean Startup / MVP-driven discovery remains the right framework; VAST would be over-engineered for your context. If your product domain is hardware, physical-process, or other non-software substrate, VAST's composition-layer framing does not translate directly.

The framework emerged from AI composition platform delivery at the pilot company (April 2026). Case studies show applications across three problem domains.

## Version history

- **v1** (2026-04-14 initial) — Strict-sequence formulation with Strict/Lite modes. Strong emphasis on iteration-economics argument. Adversarial review (multi-model council) flagged structural objections: overgeneralization, survivorship-bias on Vision-upfront, waterfall pattern-matching, cite-farming concerns, two-mode structural concession.
- **v2** (2026-04-14 revision) — Composition-layer reframing. Architecture redefined as composition framework rather than substrate lock. "Intentional priority" replaces "strict sequence." Modes collapsed into composition-depth spectrum. Explicit engagement with DDD, Team Topologies, Wardley Mapping, Cynefin. Sequoia references recast as genuine corroboration.
- **v3** (2026-04-15 revision) — Second adversarial review surfaced "Leaky Abstraction Fallacy" (composition layer relocates substrate volatility). Fixes: composition INVARIANTS vs IMPLEMENTATIONS split (substrate-aware framework, not substrate-agnostic); Vision Falsification Protocol; minimum viable depth threshold; governance abstracted across three levels (company / product / function); premature-platformization concern explicitly rejected within VAST scope.
- **v3.1** (2026-04-15 organization) — Documents reorganized into foundational (root) + references (subfolder). Glossary added for vocabulary consistency. Scaling document added articulating the agentic-scaling end-state that VAST exists to enable. Diagram added in README.
- **v3.2** (2026-04-15 cross-function accessibility) — Two new foundational documents added to close the gap for non-product leaders: `architecture-levels.md` (Architecture at product / org-design / WoW with the recurring structural pattern made explicit) and `applications.md` (worked VAST examples for CX / Marketing / People / Finance / Operations). Glossary expanded: invariants list now includes regulatory compliance, audit trails, fairness controls (first-class for several functions); vocabulary aliases ("composition framework" / "capability framework" / "process framework") noted for non-product accessibility. `applicability.md` extended with "what VAST does not cover for AI transformation" — explicit scope limits positioning VAST as one layer of broader transformation playbook.

- **v3.3** (2026-04-27 philosophy extension) — VAST repositioned as sequencing philosophy for complex systems (not product-only). New foundational document `standard-framework.md`: comparison with standard corporate stack, OKR critique, prior art table, feature comparison matrix. Values anchored in Architecture. Cross-domain instantiations (company transformation). Bidirectionality clarified (logical priority, not temporal lockstep). Adversarial review by 5 frontier models (Nestor council).
- **v3.4** (2026-05-24 self-formalization + public release) — Extracted the mandatory **Kernel** (`kernel.md`: 7 Principles, 4 Rules, published non-goals, self-falsification) and the framework-wide **Kernel → Guides → Adapters → Experiments** layering. Added the operating mechanics: the **anti-patterns** catalogue (`anti-patterns.md`, 13 patterns with `AP-NN` IDs), **layer handoffs** (`layer-handoffs.md`), **layer fitness** (`fitness.md`), and **self-evolution governance** (`evolution.md`) — VAST applied to VAST — plus the **Challenge & Escalation Protocol** in `governance.md`. De-personalized for public release (personal/KosmOS content removed; KosmOS lives in its own repo). Added a release-consistency lint (`scripts/consistency-lint.py`). Each new doc reviewed single-model; cross-doc lint passes 0/0.

## Status

Early draft. v3.4 formalizes the mandatory **Kernel** and adds the operating mechanics (anti-patterns, layer handoffs, fitness, self-evolution governance) — VAST now applies its own machinery to itself — and de-personalizes the repo for public release. Applied validation pending 6–18 month horizons; case studies in progress.
