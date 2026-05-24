# Architecture at three levels — product, org-design, ways-of-working

_New here? Start with [quick-start.md](quick-start.md) · [What is VAST?](vast.md) · [Find your role →](guides/)_

The VAST Architecture layer means different things at different scopes. The structural pattern is identical (composition framework with invariants + implementations); the content varies by what is being composed at each level.

This document articulates the recurring pattern. It supports the claim from `governance.md` that VAST applies at three levels (company / product / function) by showing what Architecture concretely owns at each — and demonstrates that the invariants vs implementations split is the same structural distinction at every level, not a product-engineering-specific concept.

## Why this matters

When non-product leaders read `vast.md`, "Architecture = composition framework" reads as engineering jargon. They struggle to map the framework to their domain. This document closes that gap by showing Architecture's content at three different scopes, demonstrating that the same shape (skills, interfaces, invariants, implementations) applies — only the contents change.

## Architecture at product level

The original VAST application. Architecture owns the AI composition framework.

| Element | What it is at product level |
|---------|----------------------------|
| **Skills (library)** | AI capabilities — agents, tools, model wrappers, retrievers, validators, classifiers, generators |
| **Interfaces (compositions)** | How skills combine — handoff protocols, state-sharing patterns, orchestration logic, error propagation |
| **Invariants (substrate-portable)** | Skill boundaries, output quality contracts, fallback policies, trust contracts, observability requirements, safety guarantees |
| **Implementations (substrate-coupled)** | Specific LLM choices, prompt strategies, retry/timeout values, output format mechanisms (JSON mode vs XML), cost optimization tactics |

When new foundation models arrive: implementations migrate, invariants persist. The composition framework is what makes the product defensibly yours, not the specific model running underneath.

## Architecture at org-design level

When the framework is applied at company or function level for organizational design, Architecture owns the **org composition framework** — what teams exist, how they compose to deliver value, what invariants govern accountability.

| Element | What it is at org-design level |
|---------|-------------------------------|
| **Skills (library)** | Team archetypes — using Team Topologies vocabulary: stream-aligned teams, platform teams, enabling teams, complicated-subsystem teams. Plus functional capabilities (engineering, product, design, data, ops, etc.) |
| **Interfaces (compositions)** | How teams compose — handoff patterns, escalation paths, decision-rights distribution, cross-functional protocols |
| **Invariants (org-portable, persist across re-orgs)** | Every decision has named accountable owner. Span of control bounded. Decisions made at lowest competent layer. Cross-functional dependencies have explicit interfaces. Escalation paths are defined and used. |
| **Implementations (specific to current org structure)** | Specific titles (Head of Engineering, Head of Product, Head of People — these are implementations of role-based invariants, not the invariants themselves). Specific reporting structures (functional vs matrix vs product-aligned). Specific cross-team coordination tools (RAPID, RACI, OKR cascades). |

When a re-org happens: implementations change (titles, reporting lines, structures), invariants should persist (the principles that govern healthy decision-making). Re-orgs that break invariants degrade the org; re-orgs that change implementations while preserving invariants merely refactor.

This framing also clarifies why `governance.md` explicitly maps roles abstractly ("Vision accountable role") rather than to specific titles — the abstract role is the invariant; the specific title is the implementation.

## Architecture at ways-of-working level

When the framework is applied to operating processes — how work actually gets done — Architecture owns the **process composition framework**.

| Element | What it is at WoW level |
|---------|------------------------|
| **Skills (library)** | Process building blocks — review meetings, decision artifacts, planning cycles, escalation flows, retrospective formats, communication patterns, status updates |
| **Interfaces (compositions)** | End-to-end workflows — annual planning cycle, performance review cycle, hiring process, incident response, product launch, decision-making chains |
| **Invariants (durable principles)** | Decisions captured as artifacts, not just discussions. Asynchronous-first communication preferred over synchronous. Customer impact considered before scope changes. Postmortems blameless and structurally-focused. Documentation precedes (or alongside) execution. |
| **Implementations (specific tools/cadences/templates)** | Specific tools (Notion, Linear, Slack, GitHub, Figma). Specific cadences (weekly all-hands, biweekly 1-1s, quarterly OKRs). Specific templates (decision doc format, RFC format, postmortem template). Specific norms (working hours, response time expectations). |

When the org migrates from Slack to a different communication platform: implementations change (the specific tool), invariants should persist (async-first, decisions-as-artifacts, the norms that make the tool effective regardless of vendor). Tool migrations that break invariants regress the org; tool migrations that swap implementations cleanly preserve operational quality.

## The recurring structural pattern

All three levels share identical structure:

1. **Skills** — what atomic capabilities exist (AI capabilities / team archetypes / process building blocks)
2. **Interfaces** — how those capabilities compose (orchestration / handoff / workflow)
3. **Invariants** — what holds across compositions, regardless of underlying substrate (model / org structure / tool stack)
4. **Implementations** — what's specific to current substrate, expected to migrate as substrate evolves

This pattern is the framework's actual structural claim. VAST is not "operating model for AI products" specifically — it is "operating model for any system where the substrate is volatile and the composition framework is the defensible artifact." AI products are the most visible current case because substrate volatility is highest there, but the pattern recurs at org-design and WoW levels too — substrate volatility just operates on slower timescales (re-orgs, tool migrations) than foundation model releases.

## When does each level need VAST applied?

Not every domain warrants VAST application at every level. Use the composition-depth criteria from `applicability.md` adapted per level:

- **Product Architecture** warrants deep VAST application when the AI substrate is load-bearing (AI-first products, shared AI platforms). Less so when AI is a minor feature.
- **Org-design Architecture** warrants deep VAST application when the org is going through major structural change (post-PMF scaling, AI transformation, mid-stage growth phases). Less so for small mature orgs running steady-state.
- **WoW Architecture** warrants deep VAST application when the org is large enough that implicit norms drift across teams or when tool/process change happens frequently. Less so for small teams with strong tacit alignment.

In all three cases, the minimum viable depth criteria from `applicability.md` apply: Vision named with falsification triggers; Architecture has named accountable owner; framework actually exists in some minimal form; Strategy references Architecture explicitly; observable Challenge Flow instances. These are level-agnostic — they apply equally whether the Architecture is product composition, org composition, or process composition.

## How this changes how the framework reads for non-product leaders

For Head of Operations: Architecture = the operating model framework (process building blocks + workflow compositions + principle invariants + tool implementations). Same VAST shape, content native to ops.

For Head of CX: Architecture = the customer experience framework (CX skills like routing/triage/response-drafting + customer journey compositions + service quality invariants + specific tooling implementations). Same VAST shape, content native to CX.

For Head of People: Architecture = the people framework (sourcing/screening/assessment skills + people workflow compositions + bias-and-compliance invariants + ATS/assessment-tool implementations). Same VAST shape, content native to people operations.

For Head of Finance: Architecture at company level = the capability portfolio framework (functional capabilities as skills + cross-function value flows as compositions + financial-controls and audit invariants + specific systems and vendors as implementations). Same VAST shape, content native to financial governance.

The framework was originally articulated from product engineering. The pattern transfers cleanly to other levels and functions because the structural claim — composition framework with invariants vs implementations split — is what's load-bearing, not the specific AI/composition vocabulary.

## Values: anchored in Architecture

Standard corporate frameworks place Values next to Vision/Mission — as aspirational. VAST anchors Values in Architecture, because that's where they have the most structural impact: constraining how domains interact and how decisions are made.

Values are architectural constraints: checks and balances of a complex system. Proto-institutions that define HOW decisions are made, not WHAT is optimized. "Customer obsession" is not aspiration — it's a structural constraint on how product, engineering, and support must interact. "Freedom" is not a goal — it's a decision filter.

Values technically cross-cut all VAST layers — they influence Vision (what purpose you choose), Strategy (where you invest), Tactics (how you execute). But they're **anchored** in Architecture because that's where they do their structural work. This is a deliberate simplification, not a precise categorization — the same way Scrum is "intentionally incomplete."

This reframe explains a common organizational failure: companies treat Values as posters on the wall because the standard framework places them in Vision (aspirational). Anchoring them in Architecture gives them a structural job — they become part of the composition framework's invariants, not decorative statements.

At each Architecture level:
- **Product:** "Customer obsession" → shapes skill library priorities, interface quality contracts, invariant definitions
- **Org-design:** "Win Together" → constrains team composition, handoff patterns, decision-rights distribution
- **Ways-of-working:** "Care Intensely" → constrains review process depth, feedback loop granularity, quality gates

See [`standard-framework.md`](./standard-framework.md) for the full mapping of standard corporate frameworks to VAST layers.

## Architecture must be concrete per instantiation

"Architecture" means different things at different scopes: composition framework (product), org capabilities (company), life domains (life application via [KosmOS](https://github.com/dkushnikov/kosmos), a separate project demonstrating cross-domain applicability). The abstract concept — "the structural domains of the system with their invariants and interfaces" — is shared. The content is scope-specific.

In each instantiation, Architecture must be defined concretely: specific domains, specific boundaries, specific interactions. Without this, Architecture risks becoming a label that sounds precise but means anything. The test: can you enumerate your Architecture's components and their interfaces? If not, you don't have Architecture — you have a word.

## References

- [`vast.md`](./vast.md) — core framework definition (foundational, this document extends it)
- [`governance.md`](./governance.md) — three governance levels (foundational, this document deepens with Architecture content per level)
- [`applicability.md`](./applicability.md) — composition depth and minimum viable depth (foundational, applies per level)
- [`applications.md`](./applications.md) — worked examples of VAST applied to specific functions (CX, Marketing, People, Finance, Operations)
- [`glossary.md`](./glossary.md) — shared vocabulary (foundational, includes vocabulary aliases note)
