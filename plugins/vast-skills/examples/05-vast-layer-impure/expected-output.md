# VAST Validation Report — Inbox Assistant — VAST Doc (v0 draft)

**Scope detected:** product
**Layers present:** V / A / S / T

## ✅ Pass
- Tactics — Layer purity — genuine instance-delivery content (per-user voice priming on recent sent mail; bulk-collapse of newsletter mail in the morning pass).
- All layers — Scope homogeneity — consistently product scope; the impurity here is layer drift, not scope drift.
- Strategy → Architecture — Challenge Flow respect — no cross-layer override described; Strategy does not challenge Architecture.

## ⚠️ Warn
- Strategy — Layer purity: borderline — reads mostly as a build calendar ("connect first, then fetch, then the three features … then billing") with only a thin investment rationale ("validate drafting quality before GA"). Tactics-leaning. Reframe: state *why* this sequence (e.g. trust before write-side) and which compositions, not just the order of construction.

## 🚨 Fail
- Vision — Layer purity: Tactics drift — the Vision is a feature list with deadlines ("drafts replies, summarizes threads, auto-tags … by Q3", then a Q3/Q4/Q1 roadmap, tiers, and platform order). No why, no for-whom-and-what-pain. This is Vision-as-Use-Case. Reframe: extract the underlying hypothesis (who loses what to inbox triage, and the experience we enable); move features/dates/tiers down to Strategy/Tactics.
- Vision — Vision falsification triggers: no triggers — the Vision states no observable, bounded, owned conditions under which it is revisited (it is a roadmap, not a hypothesis). Add 2-5 triggers (observable + bounded + owned), e.g. "draft acceptance fails to exceed 40% by end of Q3 — owner: PM".
- Architecture — Layer purity: Tactics drift — the section is a project/task list with eng estimates and milestones ("stand up the auth service", "build the fetch pipeline", "onboard 2 engineers", "M1/M2/M3"), not a composition framework. This is Architecture-by-default made concrete. Reframe: name skill boundaries, interfaces, and invariants; move the delivery plan to Tactics.
- Architecture — Composition framework completeness: absent — none of the four sub-elements is present (no skill library, no interfaces, no invariants, no implementations split). Architecture is claimed but the framework is a backlog. Define skill boundaries + at least one quality invariant + one fallback invariant + a named accountable owner, or label the doc "VAST vocabulary, not VAST applied".

## Summary
Two layers are inverted: the Vision is a dated feature roadmap (should be a falsifiable hypothesis with triggers) and the Architecture is a project plan (should be a composition framework with skills/interfaces/invariants). Fix the Architecture first — without a real framework, Strategy is sequencing compositions the doc can't support (architecture-by-default). Then reframe the Vision to its why and add falsification triggers.
