---
type: design-spec
created: 2026-05-21
status: proposed
target: VAST Skills Plugin — V1
related:
  - vast.md (framework v3.3)
  - applicability.md
  - governance.md
  - standard-framework.md
  - glossary.md
---

# VAST Skills Plugin — V1 Design

A Claude Code plugin shipping 5 skills that operationalize VAST framework against real docs — validating, transforming, connecting, OKR-auditing, and drafting docs in VAST shape. Skills point to framework as source of truth, ship co-located with framework repo, ready for both self-use and public distribution.

> [!info] How to read this doc
> Short spec (~300 lines). TL;DR has the 5 decisions. Decision blocks have rationale + trade-offs. Build plan section has 1-week breakdown. Skip appendices unless debugging.

## TL;DR — 5 decisions to greenlight

> [!decision] What you're accepting
> - **D1.** Packaging: framework-co-located plugin (`~/Code/vast-framework/plugins/vast-skills/`)
> - **D2.** Source of truth: hybrid (condensed in-skill refs + framework as canonical, version-pinned)
> - **D3.** Invocation: manual via description-trigger (V1); auto/pattern later
> - **D4.** Skills inventory: 5 in V1 — validate, transform, connect, OKR-audit, draft
> - **D5.** Build order: okr-audit → validate → transform → connect → draft (pattern probe first, foundation second, derived skills after)

> [!implementation] What gets built
> Plugin directory inside `vast-framework` repo with `plugin.json`, 5 SKILL.md files, shared + per-skill `references/`, and an `examples/` directory carrying ≥3 test cases per skill (≥15 total). Plugin installable via Claude Code plugin marketplace or direct path. Framework docs in repo remain canonical source; plugin references are regenerated extracts version-pinned to framework release.
>
> Effort: ~1 week active work. Critical path: build skill #1 (okr-audit) reveals plugin scaffolding cost — pivot to standalone if overhead too high.

---

## Decisions

### D1 — Packaging: framework-co-located plugin

> [!decision] Plugin lives inside vast-framework repo as `plugins/vast-skills/` subdirectory
> Framework and skills versioned atomically in one repo. Plugin form preserved (portable, installable). When framework updates, plugin references regenerated and committed in same change.

**What it looks like:**

```
~/Code/vast-framework/
├── (existing canonical docs: vast.md, applicability.md, etc.)
└── plugins/
    └── vast-skills/
        ├── plugin.json
        ├── README.md
        ├── references/         ← shared across all skills
        ├── skills/
        │   ├── vast-validate/
        │   ├── vast-transform/
        │   ├── vast-connect/
        │   ├── vast-okr-audit/
        │   └── vast-draft/
        └── examples/            ← ≥15 test cases
```

**Why:** Atomic versioning solves drift problem structurally (single commit ships framework change + skill heuristic update together). Plugin pattern preserved (still installable, portable). Single repo simplifies maintenance over time.

> [!risk] Trade-off accepted
> Slight upfront scaffolding overhead vs standalone `~/.claude/skills/` (Approach A). Acceptable because Dima's audience is "both self + public" — we'd repackage standalone → plugin later anyway, and the repackage cost compounds.

> [!example]- Alternatives considered
> - **A. Standalone in `~/.claude/skills/`** — fastest V1 iteration, but requires future repackage. Loses on "ship public" goal.
> - **B. Separate `vast-skills-plugin` repo** — public-ready immediately, but framework + skills decoupled → drift risk over time. Loses on cohesion.
> - **C. Framework-co-located (chosen)** — atomic versioning, plugin form, minor upfront scaffolding cost.

### D2 — Source of truth: hybrid with version-pinning

> [!decision] Framework docs = canonical SoT. Plugin `references/` = condensed extracts pinned to framework version
> SKILL.md carries condensed heuristics (1-2 lines per check); `references/` carries detail; framework docs (`~/Code/vast-framework/vast.md` etc.) remain the canonical authority. When framework updates, references regenerate.

**What it looks like:**

Plugin's shared `references/` directory:

```
plugins/vast-skills/references/
├── vast-essentials.md            ← 4 layers + triad + invariants/implementations
├── layer-definitions.md          ← Vision/Arch/Strategy/Tactics per scope (company/product/function)
├── anti-patterns.md              ← Vision-as-Use-Case, OKR conflation, etc.
├── applicability-decision-tree.md ← composition depth selector
└── version-pinning.md            ← "extracted from framework v3.3 — regenerate via scripts/sync-refs.sh"
```

Each per-skill `references/` carries skill-specific detail (e.g., `vast-validate/references/checks.md`).

**Why:** Pure embedding risks drift (skill heuristics fall behind framework evolution). Pure pointing forces AI to re-read framework on every invocation (slow, token-heavy). Hybrid gives fast-path heuristics for common case + canonical authority for edge cases.

> [!risk] Trade-off accepted
> Version-pinning requires discipline (regenerate refs when framework changes). Mitigation: a `scripts/sync-refs.sh` (V1.1) automates extraction; manual until then. V1 acceptable because framework recently stabilized at v3.3 (low churn expected near-term).

### D3 — Invocation: manual via description-trigger

> [!decision] V1 ships manual invocation only. User types intent; Claude Code matches description; skill activates
> No auto-discovery, no file-watcher, no pattern matching against file paths. Skill description field carries trigger phrases (`"validate VAST"`, `"check VAST"`, `"проверь VAST"`, etc.) that Claude Code matches against user prose.

**What it looks like:**

| Skill | Sample triggers |
|---|---|
| vast-validate | "validate this against VAST", `/vast-validate <file>`, "проверь VAST" |
| vast-transform | "transform this to VAST", "VAST-ify this" |
| vast-connect | "do these two docs cascade", "check VAST connection" |
| vast-okr-audit | "audit these OKRs", "check OKR conflation" |
| vast-draft | "draft VAST for X", "scaffold VAST" |

**Why:** Auto-invocation requires confidence in description-matching heuristics + risk of triggering on false positives. V1 keeps surface narrow — user explicitly invokes, learns the skill set, then auto-invocation can be added once trigger conditions are well-understood.

> [!risk] Trade-off accepted
> Users must remember skills exist. Mitigated by README + plugin's natural surfacing in Claude Code skill list. V1.1+ can add auto-suggestion (e.g., "this looks like a strategy doc — want me to vast-validate?").

### D4 — Skills inventory: 5 in V1

> [!decision] vast-validate, vast-transform, vast-connect, vast-okr-audit, vast-draft

**Brief specs:**

| Skill | Input | Core checks/process | Output |
|---|---|---|---|
| **vast-validate** | Doc claiming VAST shape | (1) Layer purity (Vision ≠ Use Cases, Arch ≠ Tactics) (2) Однородность scope (company-V не как product-Use-Case) (3) Vision Falsification triggers present (4) Composition framework completeness for product VAST (5) Challenge Flow respect | Structured report (pass/warn/fail per check) |
| **vast-transform** | Prose description | Identify Vision (or flag absence); map remaining to A/S/T; suggest composition depth | VAST-shaped draft + notes on gaps |
| **vast-connect** | Parent VAST + child VAST docs | Child Vision compatible with parent Strategy? Child Architecture within parent's invariants? Vision drift? | Cascade break-points report + suggestions |
| **vast-okr-audit** | OKR doc (Objectives + KRs) | Objectives = Outcomes? KRs mix Use Cases + Outputs? Per-KR layer classification | Per-OKR classification + flagged conflations + reframe suggestions |
| **vast-draft** | Scope + minimal context | Q-by-Q in commit-priority order: Vision → Architecture → Strategy → Tactics | VAST doc skeleton + open questions |

> [!risk] Trade-off accepted — drafter scope ambitious
> vast-draft is the only interactive (multi-turn) skill; others are analytical (single-pass). Different UX paradigm increases scope risk. If V1 timeline slips, drafter is the first to drop to V1.1. Validate/transform/connect/OKR-audit are the load-bearing four.

### D5 — Build order: okr-audit first

> [!decision] Build in this order: vast-okr-audit → vast-validate → vast-transform → vast-connect → vast-draft

| Day | Skill | Why this position |
|---|---|---|
| 1 | vast-okr-audit | Smallest viable surface, sharp checks. **Pattern probe** — validates plugin layout / SKILL.md template / examples mechanics on simple case before committing to larger skills. |
| 2-3 | vast-validate | Biggest (5 sub-checks). Uses learnings from #1. **Becomes foundation** that other skills may depend on. |
| 4 | vast-transform | Generative; output checkable via vast-validate. |
| 5 | vast-connect | Mostly composes validate (#2) twice + pair-check logic. Light if foundation is strong. |
| 6 | vast-draft | Different UX paradigm (interactive). Last; first to drop if V1 slips. |

**Why:** Build dependency-direction (pattern probe → foundation → derived) mirrors framework's own "use depth the work requires" principle. Small first surface plugin cost early; cheaper to pivot to Approach A (standalone) if scaffolding overhead is excessive.

---

## SKILL.md template (using vast-validate as example)

```markdown
---
name: vast-validate
description: Validate a document for VAST shape — checks layer purity (Vision ≠ Use Cases, Architecture ≠ Tactics), однородность scope, composition framework completeness, Vision Falsification triggers, Challenge Flow adherence. Use when reviewing strategy docs, product specs, vision statements, or anything claiming VAST shape. Triggers: "validate VAST", "check VAST", "проверь VAST", "audit doc against VAST".
---

# vast-validate

## When to use
[2-3 sentence trigger context + examples]

## VAST recap (condensed)
[~15 lines: 4 layers, invariants/implementations split, applicability spectrum.
Anchor: "See references/vast-essentials.md for canonical version (extracted from
~/Code/vast-framework/vast.md@v3.3)"]

## Process
1. Identify doc scope (company / product / function / WoW)
2. Identify which layer(s) the doc claims
3. Run checks (table below; full heuristics in references/checks.md)
4. Generate report (format below)

## Checks (condensed)
[Compact table: check name → 1-line heuristic → ref link]

## Output format
[Structured markdown template — see "Output format" section]

## Examples
See `../../examples/01-valid-vision/` and `../../examples/02-conflated-okr/`
```

---

## Output format

**Analytical skills** (validate/connect/okr-audit) — structured markdown report:

```markdown
# {Skill Name} Report — {target}

**Doc scope:** {company|product|function|WoW}
**Layers claimed:** [list]

## ✅ Pass
- {check} — {evidence quote}

## ⚠️ Warn
- {check} — {evidence} — {suggestion}

## 🚨 Fail
- {check} — {evidence} — {why fails} — {fix suggestion}

## Summary
{1-3 sentences — overall judgement + key next action}
```

**Generative skills** (transform/draft) — proposed VAST doc + sidebar notes:

```markdown
# Proposed VAST doc — {scope}

[Generated VAST-shaped content]

---

## Notes
- **Gaps surfaced:** [...]
- **Open questions:** [...]
- **Decisions deferred:** [...]
- **Composition depth recommended:** [deep|medium|light|vocabulary-only] — [reason]
```

---

## Build plan & V1 success criteria

### 1-week build sequence

| Day | Task | Deliverable |
|---|---|---|
| 1 | Plugin scaffolding + vast-okr-audit end-to-end | plugin.json valid, skill discovered, 3 examples pass |
| 2 | vast-validate skeleton + checks 1-2 (layer purity, scope однородность) | 3 examples pass for checks 1-2 |
| 3 | vast-validate checks 3-5 (falsification, composition completeness, Challenge Flow) | 3 examples pass for all 5 checks |
| 4 | vast-transform | 3 examples (prose → VAST shape) |
| 5 | vast-connect | 3 examples (parent + child pair) |
| 6 | vast-draft | 3 examples (scope + context → skeleton) |
| 7 | README, install docs, final examples polish | Plugin clone-and-install verified |

### V1 acceptance criteria

1. **Plugin loads cleanly** — `plugin.json` valid, all 5 skills discovered via description-matching
2. **Each skill has ≥3 examples** in `examples/` directory (good case + edge case + failure case)
3. **Each example has expected output documented** — manual verification: run skill, compare output, iterate to match
4. **vast-validate catches canonical anti-patterns**:
   - Vision-stated-as-Use-Case (company Vision drifting into product space)
   - OKR conflation (Objectives mixing Outcomes + Outputs)
   - Missing Vision Falsification triggers
   - Architecture without named accountable role
5. **Plugin installable from clean clone** — someone clones `vast-framework`, installs plugin, all 5 skills work

---

## Parallel async track — VAST Integration project fix

Non-blocking. Background subagent can:
1. Draft `~/Obsidian/Atlas/Projects/VAST Integration/project.md` from 32 existing files + commit history
2. Draft row for `Projects/index.md`
3. Audit which `vast-review-report.md` findings closed by recently-pushed 10 commits

Drafts return to main thread for review. Can launch immediately after spec is approved; doesn't gate skill build.

---

## Open / deferred (V1.1+)

- Auto-invocation / pattern-trigger (`docs/strategy/*.md` triggers vast-validate suggestion)
- Multi-turn interactive UX for vast-draft (V1 is single-pass scaffolding)
- `vast-vocabulary-translator` (product VAST ↔ org-design VAST ↔ WoW VAST)
- `vast-role-summarizer` (VAST doc → audience-specific summary; logic exists in `guides/`, just needs skill wrapper)
- `scripts/sync-refs.sh` — automated regeneration of plugin references from framework docs
- Composition-framework auditor as standalone skill (currently a check inside vast-validate)
- Vision Falsification monitor — periodically checks if any falsification trigger fired

---

## Status

V1 design proposed 2026-05-21. All 5 decisions accepted in brainstorming. Next: writing-plans skill produces implementation plan with verification checkpoints. Optional gate before implementation: Nestor council review (single-model spec review per `feedback_single-model-spec-review` — pal.chat with gpt-5.5-pro is the lighter alternative).

---

## Appendix A — Insights from brainstorming

- **Skills + framework = recursive cycle.** Framework says "make Architecture explicit." Skills enforce this against real docs. Building skills will surface gaps in framework's own precision (e.g., "how exactly to distinguish company-Vision from product-Use-Case?") — recursive refinement.
- **Examples are framework's missing case studies in skill form.** ≥15 examples across 5 skills act as: (a) test cases, (b) learning examples for VAST adopters, (c) raw material for future `case-studies/001-ai-platform.md`. Double-duty asset.
- **Co-location solves drift structurally, not procedurally.** Framework + skills in one repo, atomic commits, version-pinned references. Same pattern as Astro docs+components or React+types.
- **Pattern probe first (okr-audit) saves overcommitment.** If plugin scaffolding cost is excessive, pivot to Approach A (standalone) is cheap. After committing to 5 skills in plugin form, pivot is expensive.

## Appendix B — Framework anchors (skill → consumed docs)

| Skill | Consumes |
|---|---|
| vast-validate | vast.md (layers, invariants/implementations), glossary.md (definitions), governance.md (accountability + falsification protocol), applicability.md (composition depth) |
| vast-transform | vast.md, applicability.md (depth selection), architecture-levels.md (per-scope content) |
| vast-connect | governance.md (recursion / matryoshka), glossary.md (Challenge Flow) |
| vast-okr-audit | standard-framework.md (OKR conflation thesis), vast.md (triad) |
| vast-draft | quick-start.md (V→A→S→T order), guides/ (per-role framing), applicability.md |
