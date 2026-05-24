# VAST essentials

Fast-path condensation of the VAST core: the four layers, the triad, the invariants/implementations split, and vocabulary aliases. Skills load this instead of re-reading the full framework on every invocation. Where this disagrees with canonical, canonical wins (see `version-pinning.md`).

VAST names a sequencing principle — **Vision → Architecture → Strategy → Tactics** — in that order of *commitment priority*, not temporal phase-gates. All four layers operate continuously; the arrows are bidirectional (Strategy reveals Architecture gaps, Tactics inform Strategy). What's load-bearing is logical priority: commitment at Vision and Architecture is what makes downstream iteration compound.

## 1. The four layers

| Layer | What it owns |
|---|---|
| **Vision** | What experiences we enable, for whom, and why this exists. Committed as a falsifiable hypothesis with named revision triggers — neither emergent (Lean) nor immutable (waterfall). |
| **Architecture** | The composition framework — skill library, interfaces, invariants. What can be composed, how, and under what guarantees. This is composition/decision architecture, not the substrate tech stack. |
| **Strategy** | Which experiences to compose next: sequencing, customer validation, roadmap of compositions. Operates *within* the composition framework — informs Architecture but does not override it. |
| **Tactics** | Personalized instance delivery — specific composition moments for specific users at specific times. Where iteration runs fastest and most continuously. |

Each layer has exactly one named accountable role (singular — "one neck") plus named responsible doers. The framework requires no specific titles (CTO, CPO); it requires that for any scope of work, each layer has a named accountable person *before* work starts. Roles map per scope — see `layer-definitions.md`.

## 2. The triad: Outcomes / Use Cases / Outputs

The three VAST layers below Vision map to a universal triad:

| VAST layer | Triad role | What it answers |
|---|---|---|
| **Architecture** | **Outcomes** | What domains matter? What are we optimizing? |
| **Strategy** | **Use Cases** | Where do we work? How do we invest? |
| **Tactics** | **Outputs** | What do we concretely produce? |

- **Architecture = Outcomes** — naming the structural domains and what each is optimized for; the "what matters" that downstream work serves.
- **Strategy = Use Cases** — choosing where to apply effort and how to invest, given the domains Architecture named.
- **Tactics = Outputs** — the concrete artifacts produced inside the chosen Use Cases.

This decomposition is sharper than alternatives (e.g. OKRs, which compress all three into one construct). Each level sets context for the next; decisions at lower levels validate through upper levels. The triad recurs across instantiations: product (business outcomes / user segments / features), org (org domains / strategic priorities / OKRs), and other complex systems.

## 3. Invariants vs Implementations

The Architecture layer owns the composition framework, but the framework has two tiers with different durability. Conflating them produces false claims that the framework is fully substrate-agnostic when only part of it is.

**Composition INVARIANTS (substrate-portable, long-lived)** — framework decisions that persist across substrate changes; new models swap underneath but these remain:

- **Skill boundaries** — what each skill is responsible for; what it must not do
- **Quality contracts** — what skills must guarantee about their outputs (structured format, schema validity, latency bound, factuality requirements)
- **Fallback policies** — what happens when a skill fails or returns low-confidence output
- **Trust contracts** — what each skill is allowed to do (data access, side effects, escalation)
- **Observability requirements** — what must be measurable about every composition
- **Safety guarantees** — what must never happen (PII leakage, irreversible state changes without confirmation, untrusted code execution)

**Composition IMPLEMENTATIONS (substrate-coupled, evolves with substrate)** — implementation choices that migrate as model capabilities change; not framework-level commitments:

- **Orchestration patterns** — chain-of-prompts vs single multi-step agent vs compiled DSPy-style optimization
- **Prompt engineering strategies** — how to elicit reliable behavior from the current substrate
- **Specific retry / timeout values** — tuned for current model latency and error profile
- **Output format mechanisms** — JSON mode on one model, XML tags on another, structured-output API on a third
- **Cost optimization techniques** — model selection, caching strategies, batching tuned to current pricing
- **Latency tuning** — assumes specific substrate response characteristics

The Architecture accountable role owns both but treats them differently: **invariants change rarely and deliberately** (a major Architecture decision through governance); **implementations migrate continuously** as substrate evolves (normal Architecture work, not a per-migration decision). Implementations absorb substrate volatility; invariants persist through it. The framework is not substrate-agnostic — it is substrate-aware with a deliberate split between what is portable and what is not.

## 4. Composition framework vocabulary aliases

"Composition framework" is engineering-native vocabulary, appropriate for product engineering and shared-platform contexts. In function-level applications, equivalent meaning is often more accessible under a different label — same VAST Architecture artifact, label chosen for per-audience accessibility, not a structural difference:

- **"Capability framework"** — same concept in non-engineering org-design vocabulary. Use with function/org-design audiences (People, Ops, Finance leadership).
- **"Process framework"** — use when the function's compositions are predominantly process workflows.
- **"Workflow framework"** — use when emphasizing end-to-end orchestration of human-and-AI steps.

Foundational docs primarily say "composition framework"; function applications may use whichever alias is most natural to that domain.

## 5. Source

Extracted from `vast.md`@v3.3 (sections "The four layers", "The triad: Outcomes / Use Cases / Outputs", "What the composition framework actually owns — invariants vs implementations") + `glossary.md`@v3.3 ("Vocabulary aliases"). See `version-pinning.md` for the full source map and drift policy.
