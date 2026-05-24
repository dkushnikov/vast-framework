# Layer definitions per scope

VAST is recursive: the four-layer shape (V/A/S/T) reappears at every organizational scope, but what each layer *owns* and who is accountable changes with scope. This reference gives the per-scope content plus identifying signals so a skill can detect which scope a document is operating at. Four scopes: **company / product / function / ways-of-working (WoW)**.

The accountability shape is identical everywhere — one named accountable role per layer ("one neck"). The framework requires no specific titles; it requires that the abstract role is mapped to whoever holds the accountability at that scope.

## Company scope

| Layer | What it owns at this scope | Typical mapping |
|---|---|---|
| Vision | What the company becomes. Market stance. Why this company exists. | CEO / founder team |
| Architecture | How the company is structured to deliver the Vision: org design, capability portfolio, technology-investment strategy. The **org composition framework** — what teams exist (team archetypes: stream-aligned, platform, enabling, complicated-subsystem) and how they compose to deliver value. Invariants are org-portable (every decision has a named owner; span of control bounded; decisions at lowest competent layer). Implementations are the current org structure (titles, reporting lines, RACI/OKR cascades). | CEO + leadership team (architecture of the company-as-system) |
| Strategy | Which capabilities to develop in what sequence. Allocation of resources to functions and bets. | Function leaders / heads of organizations |
| Tactics | Execution within each function. | Teams, individual contributors |

At company level "Architecture" is mostly organizational and capability-portfolio architecture, not technical architecture. The composition-framework framing applies less directly; the four-layer shape applies mainly as vocabulary for company-wide intentionality. A re-org that swaps implementations (titles, structures) while preserving invariants merely refactors; one that breaks invariants degrades the org.

**Identifying signals** — phrases in a doc suggesting this scope:
- "market stance" / "why this company exists" / "company vision"
- "capability portfolio" / "org design" / "technology-investment strategy"
- "allocation of resources to functions and bets" / "heads of organizations"
- "team archetypes" / "stream-aligned / platform / enabling teams" / "re-org"
- "CEO" / "leadership team" / "company-as-system"

## Product scope

| Layer | What it owns at this scope | Typical mapping |
|---|---|---|
| Vision | What experiences the product enables, for whom, why. | CPO / product leadership |
| Architecture | The **composition framework** — skill library, interfaces, invariants, implementations. Skills = AI capabilities (agents, tools, model wrappers, retrievers, validators, classifiers, generators). Interfaces = handoff protocols, state-sharing, orchestration, error propagation. Invariants (substrate-portable) = skill boundaries, output quality contracts, fallback policies, trust contracts, observability, safety guarantees. Implementations (substrate-coupled) = specific LLM choices, prompt strategies, retry/timeout values, output-format mechanisms, cost tactics. | CTO / engineering leadership |
| Strategy | Which experiences to compose next, sequencing, customer validation. | Product Directors / Product Managers |
| Tactics | Personalized instance delivery — specific composition moments for specific users. | Engineering Managers / delivery teams |

This is the primary VAST application and where its claims are sharpest: the invariants-vs-implementations split applies directly. Deep composition with full discipline is appropriate when the product is AI-first and the substrate matters. When new foundation models arrive, implementations migrate and invariants persist — the composition framework, not the model running underneath, is what makes the product defensibly yours.

**Identifying signals** — phrases in a doc suggesting this scope:
- "composition framework" / "skill library" / "skills and interfaces"
- "AI substrate" / "model" / "LLM" / "substrate-portable vs substrate-coupled"
- "invariants and implementations" / "quality contract" / "fallback policy" / "trust contract"
- "which experiences to compose next" / "customer validation" / "personalized instance delivery"
- "CPO" / "CTO" / "Product Director" / "Engineering Manager"

## Function scope

| Layer | What it owns at this scope | Typical mapping |
|---|---|---|
| Vision | What the function becomes. The function's strategic stance. | Function leader (e.g., VP Marketing, VP CX, VP Operations) |
| Architecture | The function's composition framework — what tools, processes, AI integrations, and automations make up the function's **capability set**. Same VAST shape, content native to the domain (e.g. People: sourcing/screening/assessment skills + bias-and-compliance invariants + ATS implementations; Finance: capability portfolio + financial-controls/audit invariants + specific systems and vendors). | Function tech lead, ops lead, or designated process owner |
| Strategy | Which capabilities to invest in next, sequencing within the function. | Function sub-leaders / direct reports of the function leader |
| Tactics | Function team execution. | Function teams |

Composition-framework depth varies by the function's AI integration: Marketing with heavy AI content systems = medium-to-deep; Finance with AI-assisted forecasting = medium; HR with standard tooling = light. Apply VAST as deeply as the function's actual AI-substrate engagement warrants — no more.

**Identifying signals** — phrases in a doc suggesting this scope:
- "VP Marketing" / "VP CX" / "VP Operations" / "function leader" / "Head of People/Finance"
- "the function's capability set" / "capability set" / "function's strategic stance"
- "tools, processes, AI integrations, and automations" of a single function
- "invest in next, sequencing within the function" / "function sub-leaders"
- domain-native framings: "ATS / assessment tools", "forecasting tooling", "CX routing", "marketing content systems"

## Ways-of-working (WoW) scope

| Layer | What it owns at this scope | Typical mapping |
|---|---|---|
| Vision | Why work is done this way — the operating intent the processes serve. (Per-instantiation; WoW Vision is the named purpose the operating model exists to deliver.) | Operating-model / process owner (e.g. Head of Operations) |
| Architecture | The **process composition framework**. Skills = process building blocks (review meetings, decision artifacts, planning cycles, escalation flows, retrospective formats, status updates). Interfaces = end-to-end workflows (annual planning cycle, performance-review cycle, hiring process, incident response, product launch). Invariants (durable principles) = decisions captured as artifacts not just discussions; async-first communication; customer impact considered before scope changes; blameless postmortems; documentation precedes execution. Implementations = specific tools (Notion, Linear, Slack, GitHub, Figma), cadences (weekly all-hands, biweekly 1-1s, quarterly OKRs), templates (RFC, postmortem), norms (working hours). | Operations / process lead |
| Strategy | Which processes/workflows to invest in or change next; sequencing of operating-model changes. | Process sub-owners / function operating leads |
| Tactics | Day-to-day execution of the processes — running the meetings, producing the artifacts. | Teams operating within the processes |

When the org migrates tools (e.g. Slack → another platform), implementations change but invariants should persist (async-first, decisions-as-artifacts). Tool migrations that swap implementations cleanly preserve operational quality; migrations that break invariants regress the org. Warrants deep VAST when the org is large enough that implicit norms drift across teams, or when tool/process change is frequent.

**Identifying signals** — phrases in a doc suggesting this scope:
- "review meetings" / "decision artifacts" / "planning cycle" / "retrospective" / "status updates"
- "tool migration" / "Slack → " / "Notion / Linear / GitHub / Figma" as the subject of change
- "async-first" / "decisions captured as artifacts" / "blameless postmortems" / "documentation precedes execution"
- "cadences" / "1-1s" / "all-hands" / "RFC format" / "postmortem template"
- "how work actually gets done" / "operating model" / "operating processes"

---

**Note:** The per-layer rows for company / product / function are extracted from `governance.md`@v3.3 ("Level 1 — Company", "Level 2 — Product", "Level 3 — Function / Department"); the Architecture-row detail and the WoW scope are extracted from `architecture-levels.md`@v3.3 ("Architecture at product / org-design / ways-of-working level"). WoW Vision/Strategy/Tactics rows are inferred from the WoW Architecture content (architecture-levels.md treats Architecture explicitly; the other three layers follow the recursive shape). See `version-pinning.md`.
