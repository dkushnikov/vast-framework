# Glossary

Shared vocabulary for VAST. Foundational documents (`vast.md`, `kernel.md`, `anti-patterns.md`, `layer-handoffs.md`, `why-now.md`, `applicability.md`, `governance.md`, `scaling.md`) all use these terms with the definitions given here. If a term appears with a different meaning in any foundational document, it's a bug — file the discrepancy.

## The four layers

**Vision.** The first VAST layer. What experiences the product enables, for whom, why. Committed as a falsifiable hypothesis with named revision triggers — neither emergent (Lean Startup) nor immutable (waterfall). The reason the product exists, articulated specifically enough that downstream layers can be designed against it.

**Architecture.** The second VAST layer. Owns the *composition framework* (defined below). Decisions about what skills exist in the library, how they compose, what invariants hold. Note: this is composition architecture, not traditional substrate architecture — the framework that organizes how AI capabilities combine into experiences, not the technology stack underneath.

**Strategy.** The third VAST layer. Which experiences to compose next. Sequencing. Customer validation. Roadmap of compositions. Done within the constraints of the composition framework; informs Architecture but does not override it.

**Tactics.** The fourth VAST layer. Personalized instance delivery — specific composition moments for specific users. Where iteration happens fastest and continuously.

## Composition framework concepts

**Composition framework.** The Architecture layer's primary artifact. Four sub-elements: skill library (what exists), composition interfaces (how skills combine), composition invariants (substrate-portable rules across compositions — see below), and composition implementations (substrate-coupled tactics — see below). The framework as a whole is the defensible artifact; within it, invariants persist across substrate change while implementations migrate.

**Vocabulary aliases.** "Composition framework" is engineering-native vocabulary appropriate for product engineering and shared platform contexts. In function-level applications (Operations, Marketing, People, Finance, etc.), equivalent meaning is sometimes more accessible under different terms:
- "Capability framework" — same concept, common in non-engineering org-design vocabulary
- "Process framework" — when the function's compositions are predominantly process workflows
- "Workflow framework" — when emphasizing end-to-end orchestration of human-and-AI steps

These aliases denote the same VAST Architecture artifact; the choice of label is per-audience accessibility, not a structural difference. Foundational documents primarily use "composition framework"; function applications may use the alias most natural to that domain.

**Skill.** An atomic capability in the composition framework's library. May be a wrapped LLM call, a tool invocation, an agent, a retrieval mechanism, a domain-specific operation. Skills have explicit boundaries, quality contracts, trust contracts, fallback policies.

**Skill library.** The full set of skills the composition framework supports. Grows as the org's understanding of what compositions matter deepens. A defensible asset; cannot be cloned by swapping the underlying model.

**Composition interfaces.** How skills combine — handoff protocols, state-sharing patterns, orchestration logic, error propagation. The composition framework's connective tissue.

**Composition invariants.** Substrate-portable properties of the composition framework. Examples (engineering-flavored): skill boundaries (what each skill is responsible for), quality contracts (what skills must guarantee about outputs), fallback policies (what happens on failure), trust contracts (what each skill is allowed to do), observability requirements, safety guarantees. Examples (function-flavored, equally first-class): regulatory compliance (EEOC for People, audit trails for Finance, GDPR for any function handling PII), fairness controls (bias monitoring in People, equal-treatment in CX routing), audit traceability (decision provenance for Finance, Legal, regulated industries), customer-trust contracts (CX response quality, marketing brand consistency). Invariants persist across substrate change. Adding or modifying an invariant is a major Architecture decision.

**Composition implementations.** Substrate-coupled tactics for achieving invariants on the current substrate. Examples: specific orchestration patterns (chain-of-prompts vs single-agent vs DSPy-compiled), prompt engineering strategies, retry/timeout values, output format mechanisms (JSON mode vs XML tags vs structured-output API), cost optimization techniques. Implementations migrate as substrate evolves; this is normal Architecture work, not major decisions.

**Substrate.** The underlying foundation model and runtime — specific LLM (GPT, Claude, Gemini), inference layer, agent orchestration platform. Volatile (capabilities shift every few months) and increasingly fungible (multiple substrates serve similar roles). The composition framework is designed to be substrate-aware: invariants persist across substrate change; implementations migrate.

## Sequencing and flow

**Intentional priority of commitment.** The V → A → S → T ordering. Not strict temporal sequence (all layers iterate continuously); priority of which layer must be intentionally named and owned first. Without committed Vision, Architecture drifts to defaults. Without intentional Architecture, Strategy selects compositions the framework can't support. The discipline forbids running cheap iteration at lower layers while upper layers are implicit.

**Challenge Flow.** Cross-layer interaction rules. Vision *challenges* Architecture (the only downward challenge right). Strategy *informs* Architecture (does not challenge). Architecture *self-corrects* based on signals from all layers. Tactics *escalates* execution blockers. Challenge flows down; feedback flows up.

**Delivery vs Discovery.** VAST applies to delivery (we've validated; we're building and scaling). Discovery (testing hypotheses, prototyping, customer validation) does not require VAST — it generates signals that enter VAST through the discoverer's layer per Challenge Flow. Graduation path: discovery → validated → delivery decision → VAST kicks in.

**Matryoshka.** Recursive V → A → S → T. After top-level Architecture is validated, component teams operate within its invariants and may have their own local V/A/S/T at component scope. Working Matryoshka requires validated top-level invariants; false Matryoshka delegates autonomy without them (the multi-service trap adapted to skills).

## Scope and depth

**Composition depth.** Spectrum (not binary mode-switch) describing how rich the composition framework is for a given piece of work. Four depths:
- **Deep** — rich skill library, complex interfaces, many invariants (typical: product engineering of AI-first features, shared platform).
- **Medium** — moderate library, explicit interfaces, core invariants (typical: AI-enabled function-level work).
- **Light** — small library or single-skill usage, simple interfaces (typical: function-level work with minimal AI substrate).
- **Vocabulary-only** — no formal library; V/A/S/T as language for planning conversations (typical: company-wide strategic discussions).

**Organizational scope.** The level at which VAST is applied: product engineering, shared platform, function/department, company-wide. Determines the appropriate composition depth and governance intensity.

**Minimum viable depth.** The threshold below which VAST is not applied — only its vocabulary is used. Five observable conditions must hold (see `applicability.md`):
1. Vision named, committed, has falsification triggers
2. Architecture has named accountable owner
3. Composition framework actually exists in some minimal form
4. Strategy decisions reference Architecture commitments explicitly
5. ≥1 observable Challenge Flow instance per quarter

If 5/5 hold: VAST is applied. If 4/5 hold: VAST is partially applied. If 0–3 hold: vocabulary used, not VAST applied.

## Governance

**Three governance levels.** VAST applies recursively at three scopes:
- **Company governance** — Vision = CEO; Architecture = leadership team for org/capability portfolio; Strategy = function leaders; Tactics = teams.
- **Product governance** (the primary VAST application for AI-first product orgs) — Vision = product leadership (CPO equivalent); Architecture = engineering leadership owning composition framework (CTO equivalent); Strategy = product directors; Tactics = engineering managers / delivery teams.
- **Function/department governance** — Vision = function leader; Architecture = function tech/process lead; Strategy = function sub-leaders; Tactics = function teams.

The framework does not require specific titles to exist; it requires that each layer has a named accountable role at each level of application.

**Vision Falsification Protocol.** Five-step process (in `governance.md`) for what happens when Vision revision triggers fire: (1) named observable triggers with owners; (2) trigger-fire reporting; (3) Vision review session within 2 weeks; (4) decision documented (confirm / revise / extend monitoring); (5) Architecture re-examination within 4 weeks if Vision revised. Prevents Vision-as-hypothesis from collapsing into either fixed-Vision or ad-hoc-revision.

**Governance body.** For deep composition, a named body holding Vision/Architecture/Tactics accountable roles in alignment. Decisions captured as named artifacts signed by the layer accountable role. For lighter depths, accountability remains explicit per layer but no dedicated body — handled in existing exec rhythms.

## Why-now concepts

**Code commoditization.** The collapse in cost of writing software, driven by LLM-assisted development. Not just speed: shifts what's possible. Personalized-by-default software becomes the natural form when any code can be written on demand.

**Personalized-by-default software.** The emerging product shape in which experiences are composed per-user, per-moment from atomic capabilities, rather than shipped as a fixed artifact. Block's operating model is the canonical reference (Dorsey & Botha).

**Iteration economics.** What becomes expensive when iteration becomes cheap. Pre-LLM era: development expensive → architecture cheap (might rebuild). Post-LLM era: iteration cheap → architecture invariants expensive (every cheap iteration depends on them). Vision must be committed because Architecture codifies it; Architecture invariants must be intentional because Implementations migrate against them.

## Adjacent concepts referenced

**Adjacent frameworks.** VAST engages explicitly with: Domain-Driven Design (bounded contexts ≈ skill-library-per-domain), Team Topologies (Inverse Conway: team types deliver composition framework), Wardley Mapping (situational awareness about commoditization across the value chain), Cynefin (composition layer places AI-first product in Complex domain). Each is complementary or builds-on, not replaced. See `references/external-validation.md`.

**Agentic SDLC.** A complementary execution discipline (Think → Decide → Execute → Log → Mature) that operates inside each VAST layer. VAST is the priority framework for which layer commits what; SDLC is the operating tempo within each layer. Formalized separately.

**OKRs.** Complementary commitment-and-measurement mechanism that cascades through VAST layers. OKRs express what each layer commits to numerically; VAST prescribes accountability and priority. Neither replaces the other. See `references/okrs.md`.
