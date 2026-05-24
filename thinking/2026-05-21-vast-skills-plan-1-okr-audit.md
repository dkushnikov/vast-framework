# VAST Skills Plugin V0.1 — Scaffolding + OKR Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship working `vast-skills` plugin co-located in `vast-framework` repo, with `vast-okr-audit` skill that catches OKR conflation against ≥3 example docs.

**Architecture:** Plugin lives at `~/Code/vast-framework/plugins/vast-skills/`. SKILL.md frontmatter + body + per-skill `references/`. Shared `references/` extracts condensed heuristics from framework canonical docs (vast.md, applicability.md, etc.) with version pinning. Examples folder = test harness (input + expected output per case); manual verification (invoke skill, compare output, iterate SKILL.md until match).

**Tech Stack:** Claude Code plugin system, Markdown + YAML frontmatter, Git. No automated test framework V0.1 — examples-as-tests via manual verification.

**Source spec:** `~/Code/vast-framework/thinking/2026-05-21-vast-skills-design.md` (V1 design, commit 63c4a18). Read first if context unclear.

**Plugin schema reference:** When unsure about exact `plugin.json` field names or SKILL.md frontmatter conventions, invoke `plugin-dev:plugin-structure` and `plugin-dev:skill-development` skills.

---

## File Structure

Files to be created (all paths relative to `~/Code/vast-framework/`):

| File | Responsibility |
|---|---|
| `plugins/vast-skills/plugin.json` | Plugin manifest — name, version, description, homepage |
| `plugins/vast-skills/README.md` | Install instructions + V0.1 skills overview |
| `plugins/vast-skills/references/vast-essentials.md` | Condensed 4-layer + triad + invariants/implementations (extract from vast.md) |
| `plugins/vast-skills/references/layer-definitions.md` | Vision/Arch/Strategy/Tactics per scope (company/product/function/WoW) |
| `plugins/vast-skills/references/anti-patterns.md` | Common confusions: Vision-as-Use-Case, OKR conflation, missing falsification, etc. |
| `plugins/vast-skills/references/version-pinning.md` | "Extracts from framework v3.3 — regenerate via scripts/sync-refs.sh (V1.1)" |
| `plugins/vast-skills/skills/vast-okr-audit/SKILL.md` | Skill definition — frontmatter + body |
| `plugins/vast-skills/skills/vast-okr-audit/references/okr-conflation-heuristics.md` | OKR-specific detail: how to classify O/KR by layer |
| `plugins/vast-skills/examples/01-okrs-clean/input.md` | Example: 3 well-formed OKRs (Objectives = Outcomes; KRs split into Use Cases + Outputs cleanly) |
| `plugins/vast-skills/examples/01-okrs-clean/expected-output.md` | Skill should classify all KRs correctly, no conflation flags |
| `plugins/vast-skills/examples/02-okrs-conflated/input.md` | Example: OKRs where Objectives are Outputs (task lists masquerading as outcomes) |
| `plugins/vast-skills/examples/02-okrs-conflated/expected-output.md` | Skill should flag conflation in 2-3 of the OKRs |
| `plugins/vast-skills/examples/03-okrs-mixed-scope/input.md` | Example: OKRs that mix company-scope with team-scope items |
| `plugins/vast-skills/examples/03-okrs-mixed-scope/expected-output.md` | Skill should flag scope inconsistency |

Directory structure after Plan 1:

```
~/Code/vast-framework/plugins/vast-skills/
├── plugin.json
├── README.md
├── references/
│   ├── vast-essentials.md
│   ├── layer-definitions.md
│   ├── anti-patterns.md
│   └── version-pinning.md
├── skills/
│   └── vast-okr-audit/
│       ├── SKILL.md
│       └── references/
│           └── okr-conflation-heuristics.md
└── examples/
    ├── 01-okrs-clean/
    │   ├── input.md
    │   └── expected-output.md
    ├── 02-okrs-conflated/
    │   ├── input.md
    │   └── expected-output.md
    └── 03-okrs-mixed-scope/
        ├── input.md
        └── expected-output.md
```

---

## Tasks

### Task 1: Create plugin directory structure + plugin.json

**Files:**
- Create: `plugins/vast-skills/` (directory)
- Create: `plugins/vast-skills/plugin.json`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p ~/Code/vast-framework/plugins/vast-skills/skills/vast-okr-audit/references
mkdir -p ~/Code/vast-framework/plugins/vast-skills/references
mkdir -p ~/Code/vast-framework/plugins/vast-skills/examples
ls ~/Code/vast-framework/plugins/vast-skills/
```

Expected: 3 subdirs (`skills`, `references`, `examples`) listed.

- [ ] **Step 2: Invoke plugin-dev:plugin-structure for canonical plugin.json schema**

Invoke `plugin-dev:plugin-structure` skill to confirm exact `plugin.json` field names and required vs optional fields. Document the schema in scratch notes.

- [ ] **Step 3: Write plugin.json**

Create `~/Code/vast-framework/plugins/vast-skills/plugin.json` with the following content (adjust field names if Step 2 surfaces differences):

```json
{
  "name": "vast-skills",
  "version": "0.1.0",
  "description": "VAST framework skills: validate, transform, connect, OKR audit, draft. V0.1 ships vast-okr-audit.",
  "author": "Dmitry Kushnikov",
  "homepage": "https://github.com/dkushnikov/vast-framework"
}
```

- [ ] **Step 4: Verify plugin is discoverable**

Run Claude Code with plugin loaded (per `plugin-dev:plugin-structure` install instructions). Confirm `vast-skills` plugin appears in plugin list.

Expected: Plugin name `vast-skills` shows in Claude Code's loaded plugins.

- [ ] **Step 5: Commit scaffolding**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/plugin.json
git -C ~/Code/vast-framework commit -m "feat(plugins): scaffold vast-skills plugin (V0.1)"
```

---

### Task 2: README.md

**Files:**
- Create: `plugins/vast-skills/README.md`

- [ ] **Step 1: Write README**

Create `~/Code/vast-framework/plugins/vast-skills/README.md`:

```markdown
# vast-skills

Claude Code plugin operationalizing the [VAST framework](https://github.com/dkushnikov/vast-framework) against real docs.

## V0.1 — what ships

- **vast-okr-audit** — Detects OKR conflation: Objectives mixing Outcomes with Outputs, KRs spanning multiple VAST layers, scope inconsistency. Use when reviewing OKR drafts or auditing existing OKR sets.

## Future (V1+)

- `vast-validate` — Full VAST document validation
- `vast-transform` — Convert abstract description to VAST shape
- `vast-connect` — Verify cascade integrity between parent + child VAST docs
- `vast-draft` — Interactive scaffolding for new VAST docs

## Install

Plugin lives co-located in the `vast-framework` repo. From a Claude Code session:

1. Clone `vast-framework`: `git clone https://github.com/dkushnikov/vast-framework.git`
2. Add the plugin directory to Claude Code per [plugin install docs](https://docs.anthropic.com/en/docs/claude-code/plugins)
3. Verify: list loaded plugins, confirm `vast-skills` appears

## Use

Invoke any skill by naming intent in prose. Example:

> "Audit these OKRs against VAST conflation patterns" → triggers `vast-okr-audit`

Output: structured markdown report (Pass / Warn / Fail per check + Summary).

## Reference

Plugin uses condensed extracts from framework canonical docs (version-pinned). See `references/version-pinning.md` for details.

## Status

V0.1 — `vast-okr-audit` only. Build plan: `~/Code/vast-framework/thinking/2026-05-21-vast-skills-plan-1-okr-audit.md`. Spec: `~/Code/vast-framework/thinking/2026-05-21-vast-skills-design.md`.
```

- [ ] **Step 2: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/README.md
git -C ~/Code/vast-framework commit -m "docs(plugins): vast-skills README V0.1"
```

---

### Task 3: Shared reference — vast-essentials.md

**Files:**
- Create: `plugins/vast-skills/references/vast-essentials.md`

**Source material:** `~/Code/vast-framework/vast.md` sections "The four layers", "The triad", "What the composition framework owns — invariants vs implementations".

- [ ] **Step 1: Extract + condense**

Create `~/Code/vast-framework/plugins/vast-skills/references/vast-essentials.md`. Target length: ~150 lines. Sections:

1. **The four layers** (~30 lines): Table from vast.md "What it owns" — Vision/Architecture/Strategy/Tactics. Condense each cell to 1-2 sentences.

2. **The triad: Outcomes / Use Cases / Outputs** (~30 lines): Full table from vast.md "The triad" section. Add one sentence per row explaining the "what it answers" question.

3. **Invariants vs Implementations** (~50 lines): Condensed version of vast.md "What the composition framework actually owns" section. Both bullet lists (INVARIANTS + IMPLEMENTATIONS) verbatim. Skip the "Why the split matters" paragraph (too long for reference).

4. **Composition framework vocabulary aliases** (~15 lines): From glossary.md "Vocabulary aliases" — `composition framework` / `capability framework` / `process framework` / `workflow framework`. List with usage hint per audience.

5. **Source pinning** (~5 lines): "Extracted from vast.md@v3.3 + glossary.md@v3.3. Regenerate when framework version bumps. See `version-pinning.md`."

- [ ] **Step 2: Read-back verification**

Read the new `vast-essentials.md` back. Verify:
- Each section header matches above
- All 4 VAST layers are present in section 1
- Both invariants list and implementations list present in section 3
- File ends with source pinning note

- [ ] **Step 3: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/references/vast-essentials.md
git -C ~/Code/vast-framework commit -m "docs(plugins): vast-essentials.md (extract from framework v3.3)"
```

---

### Task 4: Shared reference — layer-definitions.md

**Files:**
- Create: `plugins/vast-skills/references/layer-definitions.md`

**Source material:** `architecture-levels.md` (product/org/WoW) + `governance.md` (company/product/function).

- [ ] **Step 1: Write file with 4 scope sections**

Create `~/Code/vast-framework/plugins/vast-skills/references/layer-definitions.md`. Target length: ~120 lines. Structure:

For each of 4 scope levels — company / product / function / WoW — write a section with:

```markdown
## {scope name} scope

| Layer | What it owns at this scope | Typical mapping |
|---|---|---|
| Vision | ... | ... |
| Architecture | ... | ... |
| Strategy | ... | ... |
| Tactics | ... | ... |

**Identifying signals** — phrases in a doc suggesting this scope:
- "[example phrase 1]"
- "[example phrase 2]"
- "[example phrase 3]"
```

Source content:
- **Company scope:** from governance.md "Level 1 — Company" + architecture-levels.md "Architecture at org-design level"
- **Product scope:** from governance.md "Level 2 — Product" + architecture-levels.md "Architecture at product level"
- **Function scope:** from governance.md "Level 3 — Function / Department"
- **WoW scope:** from architecture-levels.md "Architecture at ways-of-working level"

For identifying signals, derive 3-5 phrases per scope by reading the corresponding source sections and noting distinctive vocabulary (e.g., "company vision" / "5-year plan" / "market stance" suggest company; "skill library" / "AI substrate" / "model" suggest product).

- [ ] **Step 2: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/references/layer-definitions.md
git -C ~/Code/vast-framework commit -m "docs(plugins): layer-definitions.md — per-scope content"
```

---

### Task 5: Shared reference — anti-patterns.md

**Files:**
- Create: `plugins/vast-skills/references/anti-patterns.md`

**Source material:** `applicability.md` "Common mistakes" section + `standard-framework.md` "Where it breaks" + `thinking/vast-as-philosophy.md` failure modes.

- [ ] **Step 1: Write 8 anti-patterns**

Create `~/Code/vast-framework/plugins/vast-skills/references/anti-patterns.md`. Target length: ~150 lines. Structure:

Each anti-pattern as a section:

```markdown
## {N}. {Anti-pattern name}

**Pattern:** {1-2 sentence description of the dysfunction}

**How to spot it:** {observable signals in a doc — bullet list}

**Example fragment (anti-pattern):**
> {quoted bad example}

**Reframe (corrected):**
> {what it should look like}

**Source:** {framework doc + section reference}
```

The 8 anti-patterns:

1. **Vision-as-Use-Case** — Company Vision drifting into product-level use cases (Source: glossary "Vision" + standard-framework "Where it breaks")
2. **Architecture-by-default** — Strategy decisions without explicit Architecture; "we'll figure out the framework later" (Source: vast.md philosophy section)
3. **OKR conflation** — Objectives = Outputs (task lists) instead of Outcomes; KRs mixing layers (Source: standard-framework "OKRs conflate three levels")
4. **Missing Vision Falsification triggers** — Vision stated as immutable, no named revision conditions (Source: governance.md "Vision Falsification Protocol")
5. **Values-as-aspirational** — Values stated next to Vision as posters; not anchored in Architecture as structural constraints (Source: standard-framework "Values treated as aspirational")
6. **Forcing deep composition where light fits** — applying full VAST ceremony to work that needs vocabulary-only (Source: applicability "Common mistakes")
7. **Vocabulary-only where deep needed** — claiming VAST applies but no actual composition framework exists (Source: applicability "Common mistakes")
8. **Strategy challenging Architecture instead of informing** — Challenge Flow violation: Strategy should inform (not challenge) Architecture (Source: glossary "Challenge Flow")

- [ ] **Step 2: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/references/anti-patterns.md
git -C ~/Code/vast-framework commit -m "docs(plugins): anti-patterns.md — 8 common confusions"
```

---

### Task 6: Shared reference — version-pinning.md

**Files:**
- Create: `plugins/vast-skills/references/version-pinning.md`

- [ ] **Step 1: Write file**

Create `~/Code/vast-framework/plugins/vast-skills/references/version-pinning.md` with the following exact content:

```markdown
# Reference version pinning

Plugin references in this directory are condensed extracts from framework canonical docs.

## Current version

**Framework:** v3.3 (per `~/Code/vast-framework/vast.md` Status block)

**Last sync:** 2026-05-21

## Files and their canonical sources

| Plugin reference | Canonical source(s) |
|---|---|
| `vast-essentials.md` | `vast.md` (sections: "The four layers", "The triad", "What the composition framework owns"), `glossary.md` ("Vocabulary aliases") |
| `layer-definitions.md` | `architecture-levels.md` (all 3 levels), `governance.md` (Levels 1-3) |
| `anti-patterns.md` | `applicability.md` ("Common mistakes"), `standard-framework.md` ("Where it breaks"), `glossary.md` ("Challenge Flow"), `governance.md` ("Vision Falsification Protocol") |

Skill-specific references in `skills/*/references/` are sourced as documented in each file's header.

## Regeneration

V0.1: manual. When framework version bumps, manually re-extract per the source map above.

V1.1+: automated via `scripts/sync-refs.sh` (deferred — see design spec).

## Drift signal

If a finding from a skill cites framework content that differs from canonical, framework wins. Update plugin references and bump "Last sync" date.
```

- [ ] **Step 2: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/references/version-pinning.md
git -C ~/Code/vast-framework commit -m "docs(plugins): version-pinning.md — SoT mechanics"
```

---

### Task 7: vast-okr-audit SKILL.md

**Files:**
- Create: `plugins/vast-skills/skills/vast-okr-audit/SKILL.md`

- [ ] **Step 1: Invoke plugin-dev:skill-development for SKILL.md frontmatter schema**

Invoke `plugin-dev:skill-development` skill to confirm exact frontmatter field names (name, description, anything else required). Note the schema.

- [ ] **Step 2: Write SKILL.md**

Create `~/Code/vast-framework/plugins/vast-skills/skills/vast-okr-audit/SKILL.md` with the following content (adjust frontmatter to actual schema from Step 1):

````markdown
---
name: vast-okr-audit
description: Audit OKR docs for VAST conflation patterns — detects Objectives stated as Outputs (task lists masquerading as outcomes), KRs mixing layers (Use Cases + Outputs in one), and scope inconsistency (company-level mixed with team-level). Use when reviewing draft OKRs, auditing an existing OKR set, or stress-testing whether OKRs respect the VAST triad. Triggers: "audit OKRs", "check OKR conflation", "OKR VAST audit", "проверь OKR", "are these OKRs VAST-clean".
---

# vast-okr-audit

## When to use

Invoke when you have an OKR doc (Objectives + Key Results) and want to verify whether it respects the VAST triad: **Objectives ≈ Outcomes (Architecture layer), Key Results ≈ Use Cases (Strategy) + Outputs (Tactics)**.

Common triggers:
- "Audit these OKRs"
- "Check OKR conflation"
- "Are these OKRs VAST-clean?"
- "Проверь OKR на VAST"

## VAST recap (condensed)

OKRs span three VAST layers, often conflated:

| OKR element | VAST layer | What it should answer |
|---|---|---|
| **Objective** | Architecture (Outcomes) | What domain we're growing. What system property changes. |
| **Key Result (qualitative)** | Strategy (Use Cases) | Where/how we invest. Which compositions we sequence. |
| **Key Result (quantitative output)** | Tactics (Outputs) | What we concretely produce. Measurable artifact. |

**Conflation = Objective stated as Output** ("Ship X feature" instead of "Grow domain Y"); or **KRs mixing layers in unstructured way**; or **company-level mixed with team-level scope**.

Full canonical reference: `references/vast-essentials.md` (extracted from `~/Code/vast-framework/standard-framework.md` "OKRs conflate three levels"). Read it if any classification is ambiguous.

## Process

For each Objective + KR set:

1. **Identify scope** — company / function / team. If unclear or inconsistent within the doc, flag as scope-mixed.
2. **Classify each Objective** — Outcome? Output? (See heuristics in `references/okr-conflation-heuristics.md`.)
3. **Classify each KR** — Use Case (Strategy) or Output (Tactics)?
4. **Detect cross-scope mixing** — does any OKR reference a different scope than declared?
5. **Generate report** per Output format below.

## Checks

| # | Check | Heuristic (1-liner) | Detail reference |
|---|---|---|---|
| 1 | Objective is Outcome, not Output | Objective phrased as system-property change ("Grow X to Y%"), not as deliverable ("Ship X") | `references/okr-conflation-heuristics.md#objective-classification` |
| 2 | KRs split cleanly into Use Cases + Outputs | Each KR is either an investment direction (qualitative) or a measurable artifact (quantitative). Mixed KRs flagged. | `references/okr-conflation-heuristics.md#kr-classification` |
| 3 | Scope consistency | All Objectives + KRs operate at one scope (company / function / team). Mixed scope flagged. | `../../references/layer-definitions.md` |
| 4 | Objective traces to a domain | The Objective's domain is identifiable. If the Objective could fit any domain, it's too vague — likely an Output. | `references/okr-conflation-heuristics.md#domain-trace` |
| 5 | KRs don't span multiple Objectives | Each KR belongs to exactly one Objective. Cross-cutting KRs may indicate Architecture leakage. | `references/okr-conflation-heuristics.md#kr-uniqueness` |

## Output format

Produce a markdown report with this exact structure:

```markdown
# OKR Audit Report — {doc title or filename}

**Scope detected:** company | function | team | mixed
**OKRs reviewed:** {N}

## ✅ Pass
- {OKR ID or quote} — {check passed} — {brief evidence}

## ⚠️ Warn
- {OKR ID or quote} — {check}: {what's borderline} — {suggested reframe}

## 🚨 Fail
- {OKR ID or quote} — {check}: {why fails} — {evidence quote} — {suggested fix}

## Summary
{1-3 sentences: overall state, top 1-2 fixes recommended.}
```

## Examples

See:
- `../../examples/01-okrs-clean/` — well-formed OKRs, no findings expected
- `../../examples/02-okrs-conflated/` — Objective-as-Output, expect 2-3 fails
- `../../examples/03-okrs-mixed-scope/` — scope inconsistency, expect scope flag
````

- [ ] **Step 3: Verify SKILL.md is discoverable**

Restart Claude Code session (or reload plugin per plugin-dev docs). Confirm:
- Plugin still loads (`vast-skills`)
- New skill `vast-okr-audit` appears in skill list

- [ ] **Step 4: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/skills/vast-okr-audit/SKILL.md
git -C ~/Code/vast-framework commit -m "feat(plugins): vast-okr-audit SKILL.md (V0.1)"
```

---

### Task 8: Skill-specific reference — okr-conflation-heuristics.md

**Files:**
- Create: `plugins/vast-skills/skills/vast-okr-audit/references/okr-conflation-heuristics.md`

- [ ] **Step 1: Write detailed heuristics**

Create the file with these sections:

```markdown
# OKR conflation heuristics — detailed

For use by `vast-okr-audit` SKILL.md. Detail behind the condensed checks table.

## Objective classification {#objective-classification}

**Outcome (correct for Objective):** describes a system-property change, a domain state shift, a structural movement.
- Linguistic signals: "Grow X", "Increase Y to Z", "Establish capability for X", "Become the default choice for Y"
- Frame: the *world* changes, not just the *team's output*
- Test: if you achieve this Objective without shipping anything specific, is that meaningful? If yes → Outcome.

**Output (incorrect for Objective — should be a KR or a project):** describes a deliverable, a shipped artifact.
- Linguistic signals: "Launch X", "Ship Y", "Release Z", "Complete X project"
- Frame: the *team produces* something specific
- Test: could this be done as a single task? If yes → likely Output, not Objective.

**Borderline (flag as Warn):** "Improve X" without metric, "Address X" with vague action verb.

## KR classification {#kr-classification}

**Use Case (Strategy layer KR):** where/how we invest the work — qualitative direction.
- Linguistic signals: "Focus on segment X", "Prioritize feature area Y", "Validate hypothesis Z with customers"
- Frame: investment direction, not measurable artifact
- Test: does this name a domain of effort? If yes → Use Case.

**Output (Tactics layer KR):** measurable deliverable.
- Linguistic signals: "Ship N features", "Hit X% metric", "Onboard Y customers"
- Frame: concrete + measurable
- Test: can you put a number on it directly? If yes → Output.

**Mixed (flag as Fail):** a single KR containing both ("Validate segment X by shipping Y features by Q3") — split into two KRs.

## Domain trace {#domain-trace}

For each Objective, identify which **domain** it grows. Acceptable domains for VAST: any first-class business domain (e.g., for SaaS — Growth, Retention, Activation, Platform, Trust, etc.; for function-level — Talent Sourcing, CX Self-Service, etc.).

**Test:** can you point at an existing org domain map / capability portfolio and say "this Objective grows that domain"? If no → either the Objective is too vague (rewrite) or you don't have an Architecture (separate issue, flag as architecture-by-default).

## KR uniqueness {#kr-uniqueness}

Each KR should belong to exactly one Objective. Cross-cutting KRs (one KR claiming to advance multiple Objectives) often indicate that the KR is actually an Architecture element (skill, invariant, platform capability) leaking into Tactics.

**Test:** if you remove this KR from Objective A, does it still meaningfully belong to Objective B alone? If both A and B genuinely need it → flag for Architecture review (consider promoting to Platform / capability investment, not OKR).

## Scope detection

Operates at scope level. For each OKR, determine if it's:
- **Company-level:** market stance, multi-function impact, time horizons 1+ year
- **Function-level:** within one function (Eng / Marketing / People / etc.), 1-2 quarter horizons
- **Team-level:** specific delivery team, 1 quarter

Mixed-scope set = some OKRs at company level + some at team level in the same doc. Flag — usually means the doc is unclear about audience.

## Source

Heuristics derived from:
- `~/Code/vast-framework/standard-framework.md` — "OKRs conflate three levels" thesis
- `~/Code/vast-framework/vast.md` — "The triad" section
- `~/Code/vast-framework/glossary.md` — layer definitions
- `~/Code/vast-framework/governance.md` — scope/level mapping
```

- [ ] **Step 2: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/skills/vast-okr-audit/references/okr-conflation-heuristics.md
git -C ~/Code/vast-framework commit -m "docs(plugins): okr-conflation-heuristics — detail behind checks"
```

---

### Task 9: Example 01 — Clean OKRs

**Files:**
- Create: `plugins/vast-skills/examples/01-okrs-clean/input.md`
- Create: `plugins/vast-skills/examples/01-okrs-clean/expected-output.md`

- [ ] **Step 1: Write input.md (clean OKRs example)**

Create `~/Code/vast-framework/plugins/vast-skills/examples/01-okrs-clean/input.md`:

```markdown
# Q3 OKRs — Customer Experience Function

## Objective 1: Grow self-service resolution in tier-1 support

**KRs:**
- KR1.1: Focus on top-3 ticket categories (password reset, billing inquiry, integration config) — define automation scope per category by end of Q3
- KR1.2: Self-service resolution rate reaches 60% for the top-3 categories by Sep 30
- KR1.3: Customer satisfaction score on AI-handled tickets ≥ 4.2/5.0

## Objective 2: Establish proactive support capability

**KRs:**
- KR2.1: Validate predictive ticket model with the integration-team segment (top-100 accounts)
- KR2.2: Predictive trigger fires for 30% of would-be tickets before customer contacts support
- KR2.3: Time-to-resolution reduced by 25% for proactively-flagged cases
```

- [ ] **Step 2: Write expected-output.md (what skill should produce)**

Create `~/Code/vast-framework/plugins/vast-skills/examples/01-okrs-clean/expected-output.md`:

```markdown
# OKR Audit Report — Q3 OKRs — Customer Experience Function

**Scope detected:** function
**OKRs reviewed:** 2

## ✅ Pass
- Objective 1 ("Grow self-service resolution in tier-1 support") — Outcome correctly stated; domain identifiable (tier-1 self-service growth).
- Objective 2 ("Establish proactive support capability") — Outcome correctly stated; domain identifiable (proactive support).
- KR1.1 — Use Case (investment direction: top-3 category scoping).
- KR1.2 — Output (measurable: 60% rate).
- KR1.3 — Output (measurable: 4.2/5.0 score).
- KR2.1 — Use Case (investment direction: validation with segment).
- KR2.2 — Output (measurable: 30% predictive trigger rate).
- KR2.3 — Output (measurable: 25% time reduction).

## ⚠️ Warn
(none)

## 🚨 Fail
(none)

## Summary
Both Objectives are well-formed Outcomes. KRs cleanly split into Use Cases (1.1, 2.1) and Outputs (rest). No conflation, single function scope. Clean VAST OKR set.
```

- [ ] **Step 3: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/examples/01-okrs-clean/
git -C ~/Code/vast-framework commit -m "test(plugins): example 01 — clean OKRs"
```

---

### Task 10: Example 02 — Conflated OKRs

**Files:**
- Create: `plugins/vast-skills/examples/02-okrs-conflated/input.md`
- Create: `plugins/vast-skills/examples/02-okrs-conflated/expected-output.md`

- [ ] **Step 1: Write input.md (conflated OKRs)**

Create `~/Code/vast-framework/plugins/vast-skills/examples/02-okrs-conflated/input.md`:

```markdown
# Q3 OKRs — Platform Team

## Objective 1: Ship the new authentication service

**KRs:**
- KR1.1: Launch SSO integration with Okta
- KR1.2: Migrate all production services to new auth
- KR1.3: Reduce auth-related incidents by 50%

## Objective 2: Improve developer productivity

**KRs:**
- KR2.1: Validate new CI pipeline with two product teams by shipping their next 5 features through it
- KR2.2: Deploy frequency increases to 10/day
- KR2.3: Build 3 new dev-portal pages

## Objective 3: Establish observability standard across services

**KRs:**
- KR3.1: All services emit standard metrics by EOQ
- KR3.2: Define metric taxonomy + invariants for cross-service tracing
- KR3.3: Onboard 5 new engineers to the observability framework
```

- [ ] **Step 2: Write expected-output.md**

Create `~/Code/vast-framework/plugins/vast-skills/examples/02-okrs-conflated/expected-output.md`:

```markdown
# OKR Audit Report — Q3 OKRs — Platform Team

**Scope detected:** team (Platform)
**OKRs reviewed:** 3

## ✅ Pass
- Objective 3 ("Establish observability standard across services") — Outcome correctly stated; domain identifiable (observability standardization).
- KR3.1 — Output (measurable: all services emit metrics by EOQ).
- KR3.2 — Use Case (defining taxonomy + invariants = investment direction).

## ⚠️ Warn
- Objective 2 ("Improve developer productivity") — borderline. "Improve" without metric; domain (dev productivity) identifiable but Outcome framing is weak. Suggested reframe: "Grow deploy frequency and reduce time-to-merge across product teams."
- KR2.1 — mixed: contains both Use Case ("validate new CI pipeline with two product teams") and Output ("shipping their next 5 features through it"). Split into two KRs.
- KR3.3 — borderline scope: "onboard 5 new engineers" — Output, but possibly belongs to a People function objective, not Platform team observability objective. Verify scope.

## 🚨 Fail
- Objective 1 ("Ship the new authentication service") — Output, not Outcome. Phrased as deliverable ("Ship X"), not as system-property change. Suggested reframe: "Establish a unified authentication capability" or "Reduce auth fragmentation across services" — the underlying Outcome that shipping this service serves.
- KR1.1 ("Launch SSO integration") — Output classified correctly; but rolling up to Objective 1 (which is itself an Output) compounds the issue — the entire OKR is a project plan, not an OKR.
- KR1.2 ("Migrate all production services") — Output classified correctly; same issue as KR1.1.

## Summary
Objective 1 is a project disguised as an OKR — reframe to the underlying Outcome (e.g., "Reduce auth fragmentation"). Objective 2's framing is too vague to be a clean Outcome. KR2.1 mixes Use Case + Output. Recommend reframing Objective 1 first; that's the load-bearing fix.
```

- [ ] **Step 3: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/examples/02-okrs-conflated/
git -C ~/Code/vast-framework commit -m "test(plugins): example 02 — conflated OKRs (Objective-as-Output, mixed KR)"
```

---

### Task 11: Example 03 — Mixed-scope OKRs

**Files:**
- Create: `plugins/vast-skills/examples/03-okrs-mixed-scope/input.md`
- Create: `plugins/vast-skills/examples/03-okrs-mixed-scope/expected-output.md`

- [ ] **Step 1: Write input.md (mixed-scope OKRs)**

Create `~/Code/vast-framework/plugins/vast-skills/examples/03-okrs-mixed-scope/input.md`:

```markdown
# 2026 OKRs — Engineering Org

## Objective 1: Become the recognized leader in AI-first SaaS infrastructure

**KRs:**
- KR1.1: Establish industry presence — keynote at 2 major conferences, publish 3 technical whitepapers
- KR1.2: Open-source 1 core framework with 1000+ GitHub stars
- KR1.3: Inbound recruiting from FAANG engineers (≥10 qualified applications)

## Objective 2: Grow platform team velocity

**KRs:**
- KR2.1: Onboard 4 new platform engineers and have them productive within 60 days
- KR2.2: Reduce P0 incidents by 40%
- KR2.3: Deliver 3 cross-team enabling features (typed schema validator, distributed tracing layer, secrets rotation tooling)

## Objective 3: Ship voice integration in mobile app for Q1 launch

**KRs:**
- KR3.1: Voice SDK integration complete by end of Feb
- KR3.2: Beta test with 100 users in March
- KR3.3: Public release week of April 10
```

- [ ] **Step 2: Write expected-output.md**

Create `~/Code/vast-framework/plugins/vast-skills/examples/03-okrs-mixed-scope/expected-output.md`:

```markdown
# OKR Audit Report — 2026 OKRs — Engineering Org

**Scope detected:** mixed (company + team)
**OKRs reviewed:** 3

## ✅ Pass
- Objective 1 ("Become the recognized leader in AI-first SaaS infrastructure") — Outcome correctly stated for company scope (industry positioning).
- KR1.1 — Use Case (investment direction: industry presence via conferences + whitepapers).
- KR1.2 — Output (measurable: open-source release + stars threshold).
- KR2.2 — Output (measurable: 40% incident reduction).

## ⚠️ Warn
- KR1.3 ("Inbound recruiting from FAANG engineers") — borderline scope: this is a People function metric, not an Engineering Org capability metric. Either own it explicitly as a Strategy KR for Objective 1, or move to People function OKRs.
- KR2.1 ("Onboard 4 new platform engineers") — borderline: Output framing is fine, but onboarding outcomes typically belong to People function (talent acquisition + ramp). Verify ownership.

## 🚨 Fail
- **Scope inconsistency** — Objective 1 is company-scope (industry positioning), Objective 2 is team-scope (platform team velocity), Objective 3 is product-scope (mobile feature shipping). This doc mixes three scopes in one OKR set. Recommendation: split into 3 separate OKR docs at appropriate scopes, or, if intentional umbrella, mark each Objective with explicit scope label and verify all Objectives roll up to the company-level intent.
- Objective 3 ("Ship voice integration in mobile app for Q1 launch") — Output, not Outcome. Phrased as project deliverable. Suggested reframe: "Establish voice as a first-class input modality in our mobile experience" — the Outcome that shipping voice integration serves.
- KR3.1, KR3.2, KR3.3 — all Outputs nested under an Output Objective (#3). Same compounding issue as Example 02 Objective 1.

## Summary
Two issues: (1) scope inconsistency — company / team / product Objectives mixed in one set; (2) Objective 3 is a project plan, not an OKR. Recommend separating the doc into scope-specific OKR sets, and reframing Objective 3 to its underlying Outcome.
```

- [ ] **Step 3: Commit**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/examples/03-okrs-mixed-scope/
git -C ~/Code/vast-framework commit -m "test(plugins): example 03 — mixed-scope OKRs"
```

---

### Task 12: Verification — invoke skill against Example 01 (clean)

- [ ] **Step 1: Reload plugin if needed**

Per `plugin-dev:plugin-structure` skill — restart Claude Code or reload the plugin so changes are picked up.

- [ ] **Step 2: Invoke skill on Example 01**

In a Claude Code session, paste or reference:

> "Audit the OKRs in `~/Code/vast-framework/plugins/vast-skills/examples/01-okrs-clean/input.md`"

Expected: skill `vast-okr-audit` triggers automatically based on description match.

- [ ] **Step 3: Compare output to expected**

Compare skill's actual output to `examples/01-okrs-clean/expected-output.md`.

**Pass criteria:**
- Structure matches (Pass / Warn / Fail / Summary sections)
- Same classifications (Objectives as Outcomes, KRs split correctly into Use Cases vs Outputs)
- No false positives in Warn or Fail
- Summary captures "clean set, no findings"

If output diverges, iterate `SKILL.md` (Task 7) and `okr-conflation-heuristics.md` (Task 8) — typically by sharpening process steps or adding distinguishing heuristics. Re-run.

- [ ] **Step 4: Document iteration (if any)**

If you iterated heuristics, add a short note at the bottom of `examples/01-okrs-clean/expected-output.md` (after expected output) describing what was sharpened. This builds the case for the skill's edge cases.

- [ ] **Step 5: Commit any heuristic adjustments**

```bash
git -C ~/Code/vast-framework add -p plugins/vast-skills/skills/vast-okr-audit/
git -C ~/Code/vast-framework commit -m "fix(plugins): vast-okr-audit heuristic adjustments from example 01 verification"
```

(Skip commit if no adjustments needed.)

---

### Task 13: Verification — Example 02 (conflated)

- [ ] **Step 1: Invoke skill on Example 02**

> "Audit the OKRs in `~/Code/vast-framework/plugins/vast-skills/examples/02-okrs-conflated/input.md`"

- [ ] **Step 2: Compare output to expected**

**Pass criteria:**
- Objective 1 ("Ship the new authentication service") flagged as **Fail** (Output stated as Objective)
- KR2.1 flagged as **Warn** (Use Case + Output mixed)
- Objective 2 ("Improve developer productivity") flagged as **Warn** (vague Outcome framing)
- Summary captures the load-bearing fix (Objective 1 reframe)

- [ ] **Step 3: Iterate if needed, document, commit (as in Task 12)**

---

### Task 14: Verification — Example 03 (mixed-scope)

- [ ] **Step 1: Invoke skill on Example 03**

> "Audit the OKRs in `~/Code/vast-framework/plugins/vast-skills/examples/03-okrs-mixed-scope/input.md`"

- [ ] **Step 2: Compare output to expected**

**Pass criteria:**
- **Scope inconsistency** flagged as a top-level Fail (mixed company/team/product)
- Objective 3 ("Ship voice integration") flagged as Fail (Output as Objective)
- KR1.3 and KR2.1 flagged as Warn (cross-scope concerns to People function)
- Summary captures both issues (scope mix + Objective 3 reframe)

- [ ] **Step 3: Iterate if needed, document, commit**

---

### Task 15: README polish + V0.1 ship commit

**Files:**
- Modify: `plugins/vast-skills/README.md`

- [ ] **Step 1: Update README "Use" section with verified example**

Edit `plugins/vast-skills/README.md`. Replace the placeholder "Use" section with a real example showing one of the verified invocations + an excerpt of actual output (use Example 02 — most demonstrative).

- [ ] **Step 2: Add CHANGELOG entry inside README**

Append to README:

```markdown
## Changelog

### V0.1 (2026-05-21)
- Initial release
- `vast-okr-audit` skill — detects Objective-as-Output, KR layer mixing, scope inconsistency
- 3 verified examples
- Shared references: vast-essentials, layer-definitions, anti-patterns, version-pinning
```

- [ ] **Step 3: Commit README update**

```bash
git -C ~/Code/vast-framework add plugins/vast-skills/README.md
git -C ~/Code/vast-framework commit -m "docs(plugins): README V0.1 — verified usage + changelog"
```

- [ ] **Step 4: Verify clean state**

```bash
git -C ~/Code/vast-framework status
git -C ~/Code/vast-framework log --oneline -20
```

Expected:
- Working tree clean
- Recent commits show V0.1 build sequence (scaffold → references → SKILL.md → examples → verification → README polish)

- [ ] **Step 5: Tag V0.1 release**

```bash
git -C ~/Code/vast-framework tag -a vast-skills-v0.1.0 -m "vast-skills V0.1 — vast-okr-audit ships"
git -C ~/Code/vast-framework tag -l "vast-skills-*"
```

(Tag prefixed with `vast-skills-` to disambiguate from framework version tags. Push tags separately if/when ready: `git -C ~/Code/vast-framework push --tags`.)

- [ ] **Step 6: Final ship commit (optional consolidation)**

If the spec was edited during the build (e.g., decisions clarified, V0.1 scope adjusted), commit the spec update separately:

```bash
git -C ~/Code/vast-framework add thinking/2026-05-21-vast-skills-design.md
git -C ~/Code/vast-framework commit -m "docs(thinking): vast-skills spec adjustments from V0.1 build"
```

If no spec changes — skip.

---

## V0.1 acceptance — what "done" looks like

- [ ] Plugin loads cleanly in Claude Code
- [ ] `vast-okr-audit` skill discovered, triggers on "audit OKRs" / similar
- [ ] All 3 examples produce output matching expected (or expected updated to reflect verified output)
- [ ] Plugin can be cloned via `git clone` of `vast-framework` and installed without manual fiddling
- [ ] README accurately describes how to use
- [ ] Tag `vast-skills-v0.1.0` exists

## What comes next (Plan 2+)

Plan 2: `vast-validate` (Day 2-3 of design). Uses learnings from this plan's verification phase to refine the skill-building pattern. Build order continues: validate → transform → connect → draft (each = own plan).

## Self-review notes (post-write)

- Spec coverage: all 5 design decisions (D1-D5) reflected — co-located plugin (D1), hybrid SoT via references/ + version-pinning.md (D2), manual invocation (D3), vast-okr-audit as first of 5 (D4), pattern-probe first per build order (D5). ✓
- No placeholder language (all "[...]" are bracketed within actual content, not skipped sections). ✓
- Method names + field names consistent across tasks (plugin.json fields named once, SKILL.md frontmatter named once, both referenced consistently downstream). ✓
- Tasks 12-14 share verification pattern — repeated explicitly per skill's "Similar to Task N" forbidden rule. ✓
