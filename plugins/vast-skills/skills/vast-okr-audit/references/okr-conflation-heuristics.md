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

**Borderline (flag as Warn):** vague action verb ("Improve", "Address", "Enhance", "Optimize") with NO named metric AND no named domain. Note: "Improve NPS to 60" is a valid Outcome (metric present) — the verb alone does not make it borderline; the *absence of both metric and domain* does.

## KR classification {#kr-classification}

**Use Case (Strategy layer KR):** where/how we invest the work — qualitative direction.
- Linguistic signals: "Focus on segment X", "Prioritize feature area Y", "Validate hypothesis Z with customers"
- Frame: investment direction, not measurable artifact
- Test: does this name a domain of effort? If yes → Use Case.

**Output (Tactics layer KR):** measurable deliverable.
- Linguistic signals: "Ship N features", "Hit X% metric", "Onboard Y customers"
- Frame: concrete + measurable
- Test: can you put a number on it directly? If yes → Output.

**Mixed (flag as Fail):** a single KR containing both a direction and a measurable artifact ("Validate segment X by shipping Y features by Q3") — split into two KRs.

**Borderline (flag as Warn):** a KR that is neither a named investment direction nor a measurable artifact — purely aspirational with no direction and no number ("Ensure customers are happy", "Make the product better"). Cannot be classified as Use Case or Output; flag for rewrite into one or the other.

## Domain trace {#domain-trace}

For each Objective, identify which **domain** it grows. Acceptable domains for VAST: any first-class business domain (e.g., for SaaS — Growth, Retention, Activation, Platform, Trust, etc.; for function-level — Talent Sourcing, CX Self-Service, etc.).

**Test:** can you point at an existing org domain map / capability portfolio and say "this Objective grows that domain"? If no → either the Objective is too vague (rewrite) or you don't have an Architecture (separate issue, flag as architecture-by-default).

## KR uniqueness {#kr-uniqueness}

Each KR should belong to exactly one Objective. Cross-cutting KRs (one KR claiming to advance multiple Objectives) often indicate that the KR is actually an Architecture element (skill, invariant, platform capability) leaking into Tactics.

**When to run this check:** only when (a) the same metric or artifact appears under multiple Objectives, or (b) a KR uses language naming a domain that belongs to a *different* Objective. For well-formed docs with no such overlap, this check passes by default — don't force hypothetical reassignment on every KR.

**Test:** if a KR triggers the condition above — remove it from Objective A; does it still meaningfully belong to Objective B alone? If both A and B genuinely need it → it's likely **Architecture leakage**: the KR describes a shared capability / skill / invariant (an Architecture-layer element) rather than a single Objective's output. Flag for Architecture review (consider promoting to Platform / capability investment, tracked outside OKRs).

## Scope detection {#scope-detection}

Operates at scope level. For each OKR, determine if it's:
- **Company-level:** market stance, multi-function impact, time horizons 1+ year
- **Function-level:** within one function (Eng / Marketing / People / etc.), 1-2 quarter horizons
- **Team-level:** specific delivery team, 1 quarter

Mixed-scope set = some OKRs at company level + some at team level in the same doc. Flag — usually means the doc is unclear about audience.

**This skill uses the OKR-native taxonomy (company / function / team)** — how orgs structure OKRs in practice. It maps to the framework's general VAST scope model (company / product / function / ways-of-working — see `../../../references/layer-definitions.md`) as: company↔company; function↔function; team-level ≈ Tactics execution within a function or product scope. Use this section as the primary authority for OKR scope detection; consult `../../../references/layer-definitions.md` for the full VAST scope model.

## Source

Heuristics derived from:
- `standard-framework.md` — "OKRs conflate three levels" thesis
- `vast.md` — "The triad" section
- `glossary.md` — layer definitions
- `governance.md` — scope/level mapping

(Paths relative to framework repo root.)
