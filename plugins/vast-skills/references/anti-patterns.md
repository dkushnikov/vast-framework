# VAST anti-patterns — detection-tuned companion

The recurring ways VAST documents go wrong, tuned for automated detection: each entry gives the dysfunction, observable signals a skill can detect in a doc, a bad example fragment, the corrected reframe, and the canonical source. Example fragments are illustrative inventions that exhibit the named pattern — they are not quotes from real docs.

**Source of truth:** the framework catalogue is [`anti-patterns.md`](../../../anti-patterns.md) at the repo root — 13 patterns, each mapped to the Kernel principle it violates. This file is its detection-tuned companion: the eight patterns that can be reliably flagged in a written doc. Mapping to canonical IDs:

| This file | Canonical ID |
|---|---|
| 1. Vision-as-Use-Case | AP-05 |
| 2. Architecture-by-default | AP-01 |
| 3. OKR conflation | AP-06 |
| 4. Missing Vision Falsification triggers | AP-07 |
| 5. Values-as-aspirational | AP-08 |
| 6. Forcing deep composition where light fits | AP-11 |
| 7. Vocabulary-only where deep is needed | AP-02 |
| 8. Strategy challenging Architecture | AP-12 |

Canonical-only (operating-level or newer doc patterns): AP-03 (Architecture-as-org-chart/stack), AP-04 (implementation-as-invariant), AP-09 (ownerless layers), AP-10 (VAST-as-waterfall), AP-13 (Kernel-erosion). AP-03/04/09 are doc-detectable — candidates for a future skill bump.

## 1. Vision-as-Use-Case

**Pattern:** A Vision statement drifts down into product-level use cases or feature lists. Instead of "what experiences we enable, for whom, why" — articulated as a falsifiable hypothesis — it reads as a roadmap of things to build. At company scope this is acute: company Vision collapses into product specifics.

**How to spot it:**
- Vision section enumerates features, screens, or specific compositions
- No falsification triggers; no "for whom / why" — only "what we will ship"
- Vision and Strategy are nearly interchangeable in the doc

**Example fragment (anti-pattern):**
> **Vision:** Ship an AI inbox assistant that drafts replies, summarizes threads, and auto-tags messages by Q3, then expand to calendar and docs.

**Reframe (corrected):**
> **Vision:** We believe solo operators lose hours to inbox triage; we enable them to clear a day's mail in minutes by composing draft/summarize/tag skills into one flow. Revise if, after launch, median triage time fails to drop below 10 min/day for 4 consecutive weeks. (Specific features — drafting, tagging — are Strategy/Tactics, not Vision.)

**Source:** `glossary.md` ("Vision" — committed falsifiable hypothesis, named revision triggers); `standard-framework.md` ("Where it breaks").

## 2. Architecture-by-default

**Pattern:** Strategy decisions get made without explicit Architecture — the team selects what to build while the composition framework stays implicit, unnamed, or unowned ("we'll figure out the framework later"). This is the exact dysfunction VAST exists to prevent: cheap iteration runs on lower layers while the upper layer is implicit, so Strategy selects compositions the framework can't actually support.

**How to spot it:**
- Doc jumps from Vision/goals straight to a roadmap or backlog
- No named Architecture owner; no skill library / invariants section
- Phrases deferring structure: "we'll define the framework as we go", "architecture TBD"

**Example fragment (anti-pattern):**
> We don't need to lock the composition framework yet — let's start shipping experiences and let the architecture emerge from what we build.

**Reframe (corrected):**
> Before sequencing experiences, name the Architecture: skill boundaries for draft/summarize/tag, the quality + fallback contracts each must hold, and a single accountable owner. Strategy then selects compositions the framework supports — not the reverse.

**Source:** `vast.md` ("Intentional, not strict" — the architecture-by-default failure mode; "before" = priority of commitment); `applicability.md` ("Common mistakes" — vocabulary-only where deep is needed → architecture-by-default).

## 3. OKR conflation

**Pattern:** OKRs flatten three VAST layers into one construct. Objectives are written as Outputs (task lists) instead of Outcomes (Architecture — what domains matter), and Key Results mix Strategy (Use Cases — where to invest) with Tactics (Outputs — what to produce). Works while Architecture is implicit and shared; degenerates into a task list once Architecture is invisible.

**How to spot it:**
- Objectives phrased as deliverables ("Launch X", "Ship Y") rather than domains/outcomes
- KRs are a grab-bag mixing investment choices and concrete outputs at one level
- No traceability from an Objective back to a structural domain (Architecture)

**Example fragment (anti-pattern):**
> **Objective:** Ship the AI inbox assistant.
> **KR1:** Launch drafting feature. **KR2:** Hit 20% DAU. **KR3:** Write 4 prompt templates.

**Reframe (corrected):**
> **Objective (Outcome / Architecture):** Inbox-triage time is a domain we own and optimize.
> **KR (Use Case / Strategy):** Validate the draft+summarize composition with the solo-operator segment.
> **KR (Output / Tactics):** Ship 4 production-ready draft templates. (Layers labeled, not blended.)

**Source:** `standard-framework.md` ("OKRs conflate three levels" — Objectives ≈ Outcomes, KRs ≈ Use Cases + Outputs); `vast.md` ("The triad").

## 4. Missing Vision Falsification triggers

**Pattern:** Vision is stated as immutable — committed but with no named, observable, owned conditions under which it gets revisited. This collapses Vision-as-hypothesis into either fixed-Vision (survivorship-bias risk) or ad-hoc revision (no discipline). Without triggers, "Vision is a hypothesis we'll revise when needed" is aspirational epistemology, not an operating commitment.

**How to spot it:**
- Vision has no revision conditions at all, or vague ones ("revise if it's not working")
- No named trigger owner; no thresholds, durations, or metrics
- Triggers are interpretive ("users seem unhappy") not bounded/observable

**Example fragment (anti-pattern):**
> **Vision:** We enable solo operators to clear inbox triage in minutes. This is our north star and won't change.

**Reframe (corrected):**
> **Vision:** [as above]. **Falsification triggers:** (1) weekly retention < 35% for 4 consecutive weeks — owner: Head of Growth; (2) AI-draft acceptance rate fails to exceed 40% by end of Q3 — owner: PM, inbox. On trigger fire: report to Vision owner within 1 week → Vision review session within 2 weeks → documented confirm/revise/extend.

**Source:** `governance.md` ("Vision Falsification Protocol" — triggers must be observable, bounded, owned; 5-step process).

## 5. Values-as-aspirational

**Pattern:** Values are placed next to Vision/Mission as aspirational posters, not anchored in Architecture as structural constraints. The standard stack lumps Vision/Mission/Values together as "aspirational," so Values get no structural job — they stay on the wall instead of constraining how domains interact and how decisions are made.

**How to spot it:**
- A "Values" block sits inside or beside the Vision section
- Values are adjectives/slogans with no link to invariants, interfaces, or decision rules
- Nothing in Architecture references the values as constraints

**Example fragment (anti-pattern):**
> **Our Vision & Values:** Build delightful AI experiences. We value Customer Obsession, Boldness, and Trust.

**Reframe (corrected):**
> **Architecture (Values as invariants):** "Customer Obsession" → every skill carries a factuality + fallback contract before it ships (no confident-wrong outputs to users). "Trust" → trust-contract invariant: no skill touches user data without explicit scope. Values do their structural work as composition invariants, not as a Vision-adjacent poster.

**Source:** `standard-framework.md` ("Values treated as aspirational, not structural"); `architecture-levels.md` ("Values: anchored in Architecture").

## 6. Forcing deep composition where light fits

**Pattern:** Full VAST ceremony (rich skill library, many invariants, dedicated governance body, named per-layer commitments) is applied to work that only needs vocabulary-only or light composition. The result is overhead without value — ceremony that generates legitimate pushback and damages framework credibility in the domains where depth actually fits.

**How to spot it:**
- Heavyweight governance/invariant scaffolding around a one-off, low-AI, or experimental task
- A/B test, pricing-page tweak, or single-skill function tool wrapped in full discipline
- Composition depth is disproportionate to the work's actual AI-substrate engagement

**Example fragment (anti-pattern):**
> For the marketing team's choice of which copy-generation tool to trial, we'll stand up a composition governance body, define the full invariant set, and require signed per-layer accountability artifacts.

**Reframe (corrected):**
> This is function-scope, light composition. Use VAST vocabulary + a named accountable owner; skip the governance body and the full invariant set. Match depth to what the work requires — a tool trial doesn't need product-runtime discipline.

**Source:** `applicability.md` ("Common mistakes" — forcing deep composition where medium-or-light fits; composition-depth spectrum).

## 7. Vocabulary-only where deep is needed

**Pattern:** The inverse of #6. A doc claims VAST applies and uses the four-layer language, but no actual composition framework exists — decided via "V-A-S-T language only, no real framework." Below the minimum-viable-depth floor (named Vision triggers, named Architecture owner, framework exists in minimal form, Strategy references Architecture, ≥1 Challenge Flow instance/quarter), this is VAST vocabulary, not VAST applied — and it leads straight back to architecture-by-default.

**How to spot it:**
- Layer headings (Vision/Architecture/Strategy/Tactics) present but Architecture section is empty or hand-wavy
- No skill boundaries, no invariants, no named accountable owner
- "We use VAST" asserted but none of the 5 minimum-viable-depth conditions are observable

**Example fragment (anti-pattern):**
> We've adopted VAST for the new shared AI capability. Architecture: we'll compose the right skills as needed. Strategy: ship fast. (No skills, interfaces, invariants, or owner named.)

**Reframe (corrected):**
> A shared AI capability needs real depth. Name the Architecture owner; list skill boundaries and at least one quality + one fallback invariant; have Strategy cite which composition the framework supports. If those can't be met yet, say honestly "we're using VAST vocabulary, not applying VAST" rather than claiming application.

**Source:** `applicability.md` ("Common mistakes" — applying vocabulary-only where medium-or-deep is needed; "Minimum viable depth" 5-condition floor).

## 8. Strategy challenging Architecture instead of informing

**Pattern:** A Challenge Flow violation. Strategy tries to *challenge / override* Architecture rather than *inform* it. In VAST, challenge flows down and only Vision has downward challenge right over Architecture; Strategy feeds signals up (customer pain, adoption friction, competitive movement) and Architecture decides. Strategy overriding Architecture re-creates the diffuse, default-by-accumulation decision-making VAST exists to replace.

**How to spot it:**
- Strategy/PM section dictates composition-framework changes or vetoes invariants
- Language like "Strategy decided to drop invariant X" or "Product overrides the framework here"
- Architecture treated as downstream of Strategy rather than the constraint Strategy operates within

**Example fragment (anti-pattern):**
> Strategy review concluded the latency invariant is slowing us down, so we're removing it and Architecture will adjust to match.

**Reframe (corrected):**
> Strategy *informs*: "the latency invariant is costing us adoption in segment X — here's the data." Architecture (the accountable owner) decides whether to relax, keep, or re-engineer the invariant. Only Vision may *challenge* Architecture; Strategy feeds first-class signal, it doesn't dictate.

**Source:** `glossary.md` ("Challenge Flow" — Vision challenges, Strategy informs, Architecture self-corrects, Tactics escalates; challenge flows down, feedback flows up).

---

**Source note:** These eight are the detection-tuned subset of the canonical catalogue ([`../../../anti-patterns.md`](../../../anti-patterns.md)) — see it for the full 13 and the Kernel-principle mapping. Patterns derived from `applicability.md` ("Common mistakes"), `standard-framework.md` ("Where it breaks", "Values treated as aspirational", "OKRs conflate three levels"), `glossary.md` ("Vision", "Challenge Flow"), `governance.md` ("Vision Falsification Protocol"), and `vast.md` ("Intentional, not strict" — architecture-by-default), all @v3.3, plus `thinking/2026-04-26-vast-as-philosophy.md` failure-mode discussion. See `version-pinning.md`.
