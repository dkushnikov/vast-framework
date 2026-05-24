# VAST Anti-Patterns

The recurring ways VAST goes wrong — in how it is *documented* and in how it is *operated*. Each anti-pattern violates a specific [Kernel](kernel.md) principle, rule, or non-goal; naming them is how the framework stays refusable rather than aspirational. The catalogue is deliberately defensive: VAST is an extension applied at a complexity threshold, so most of its failure modes are either **skipping the step it exists to add** (Architecture) or **applying its ceremony where it isn't warranted**.

> **Authoritative catalogue.** This file is the source of truth for VAST anti-patterns. The `vast-skills` plugin maintains a [detection-tuned companion](plugins/vast-skills/references/anti-patterns.md) with per-document signals and example fragments for the entries it can reliably detect in a written doc (currently AP-01, AP-02, AP-05–AP-08, AP-11, AP-12). The operating-level patterns (AP-10, AP-13) and the newer doc patterns (AP-03, AP-04, AP-09) are catalogued here first.

Each entry has a stable ID, the **pattern**, the Kernel principle/rule it **violates**, and the **reframe**.

## A. Skipping or faking Architecture

The core dysfunction VAST exists to prevent: the structural layer is absent, empty, mis-cast, or filled with the wrong kind of content while iteration runs below it.

### AP-01 · Architecture-by-default
**Pattern:** Strategy selects what to build while the composition framework stays implicit, unnamed, or unowned — "we'll figure out the architecture later." Decisions accumulate into a de-facto structure no one chose.
**Violates:** Principle 1 (Make Architecture explicit); the Rule *Architecture is made explicit before Strategy commits*.
**Reframe:** Name the structural domains, constraints, and one accountable owner *before* sequencing Strategy. Strategy then selects compositions the framework supports — not the reverse.

### AP-02 · Vocabulary-only where depth is needed
**Pattern:** A doc uses the four-layer language but no real framework exists underneath — layer headings over an empty or hand-wavy Architecture. "We use VAST" is asserted while the Kernel floor goes unmet.
**Violates:** The Kernel floor — all four layers named with one accountable owner each, Architecture explicit before Strategy commits, Vision falsifiable, invariants separated from implementations — especially Principle 1.
**Reframe:** Either satisfy that floor at the depth the work requires, or say honestly "we use VAST vocabulary, not VAST applied." (*How much* depth a given scope needs is guide-level guidance — see `applicability.md` — not a Kernel rule.)

### AP-03 · Architecture mistaken for the org chart or the tech stack
**Pattern:** "Architecture" is read as the reporting structure, the system diagram, or the CTO's domain — so the *decision* architecture (how domains interact, what constrains them, what values enforce boundaries) never gets named.
**Violates:** Principle 1 (Architecture = structural domains, constraints, and values); often Principle 4 when a diagram, stack, or org mechanism is then treated as an invariant.
**Reframe:** Org charts, system diagrams, and tech stacks can *represent* or *implement* architectural choices; they are not sufficient Architecture. Name the domains, interfaces, invariants, and values-as-constraints.

### AP-04 · Implementation mistaken for invariant
**Pattern:** Architecture lists tools, vendors, models, prompts, cadences, or current stack choices as if they were durable invariants. The "what must always hold" tier fills with substrate-coupled specifics, and the framework becomes substrate-locked instead of portable.
**Violates:** Principle 4 (Separate invariants from implementations); the Rule *invariants are separated from implementations wherever a composition framework is claimed*.
**Reframe:** State the portable invariant apart from its current implementation. "Every user-facing AI response carries provenance and a fallback" is an invariant; "via model X, prompt Y, reviewed weekly" is an implementation that may migrate.

## B. Collapsing the layers

### AP-05 · Vision-as-Use-Case
**Pattern:** Vision drifts down into a feature list or roadmap — "what we will ship" instead of "what experiences we enable, for whom, why." Vision and Strategy become interchangeable.
**Violates:** Principle 3 (keep Outcomes / Use-Cases / Outputs distinct); often also the *Vision-as-falsifiable-hypothesis* Rule when no revision trigger is named.
**Reframe:** Vision states the experience and the bet; specific features are Strategy/Tactics. If you can't tell Vision from the roadmap, the layers have collapsed.

### AP-06 · OKR conflation
**Pattern:** OKRs flatten three layers into one: Objectives written as Outputs (task lists) instead of Outcomes, KRs mixing Strategy (use-cases) and Tactics (deliverables) at one level. Works while Architecture is shared and implicit; degenerates into a task list once it's invisible.
**Violates:** Principle 3 (keep Outcomes / Use-Cases / Outputs distinct).
**Reframe:** In a VAST OKR adapter, keep the Objective outcome-level and traceable to an Architecture domain; where KRs carry both use-case bets and tactical deliverables, label or split the levels rather than letting them masquerade as one.

## C. Hollow commitments

The layer's *form* is present, but nothing is actually committed, constrained, or owned.

### AP-07 · Missing Vision-falsification triggers
**Pattern:** Vision is stated as immutable — committed, but with no named, observable, owned condition under which it gets revisited. "We'll revise when needed" is not an operating commitment.
**Violates:** Principle 6 (Vision is a committed hypothesis with named revision triggers); the Rule *Vision is stated as a falsifiable hypothesis*.
**Reframe:** Name at least one observable, bounded, owned trigger and the process that fires on it. A Vision that can't be wrong can't be a hypothesis. *(Operating variant: triggers named but never monitored — the same failure, deferred.)*

### AP-08 · Values as aspirational posters
**Pattern:** Values sit beside Vision as slogans with no structural job — adjectives on the wall, unlinked to any invariant, interface, or decision rule.
**Violates:** Principle 5 (Anchor Values in Architecture).
**Reframe:** Give each value a structural job as a composition invariant or constraint (e.g. "Trust" → no skill touches user data without explicit scope). If nothing in Architecture references a value, it isn't doing work.

### AP-09 · Ownerless layers (accountability-by-committee)
**Pattern:** The four sections exist, but their owners are "the team," "leadership," "TBD," or a committee. No single person is accountable for committing or revising a layer, so challenge and evidence have no decider.
**Violates:** the Rule *each of the four layers has one accountable owner*; weakens Principle 6 (challenge/evidence flow needs a decider).
**Reframe:** Consult many, decide one. Each layer names exactly one accountable owner for its commitment and revision — distinct from the many who inform it.

## D. Miscalibrating the model

### AP-10 · VAST-as-waterfall
**Pattern:** The Vision → Architecture → Strategy → Tactics sequence is read as a one-way phase-gate — finish Vision, freeze it, then Architecture, then hand off. Big Design Up Front (BDUF) in new clothing.
**Violates:** Principle 2 (Commit by priority, *not* by sequence — all four layers run continuously; the arrows are bidirectional).
**Reframe:** The order is *commitment priority*, not temporal lockstep. Establish enough explicit Vision/Architecture to constrain downstream commitment — then keep iterating; Strategy and Tactics feed evidence back up continuously.

### AP-11 · Forcing deep composition where light fits
**Pattern:** Full VAST ceremony — rich invariant sets, governance bodies, per-layer accountability artifacts — applied to a one-off, low-AI, or experimental task. Overhead without value; the pushback it earns damages the framework where depth *does* fit.
**Violates:** Principle 7 (Minimal sufficiency — bring only the composition depth the work requires).
**Reframe:** Match depth to the work. A tool trial or a pricing-page tweak needs vocabulary + an owner, not product-runtime discipline.

## E. Eroding flow and core

### AP-12 · Strategy challenging Architecture (instead of informing)
**Pattern:** Strategy tries to override Architecture — vetoing invariants, dictating framework changes — rather than feeding signal up for Architecture to decide. Re-creates the diffuse, default-by-accumulation decision-making VAST replaces.
**Violates:** Principle 6 (Challenge flows down; only Vision challenges Architecture; Strategy *informs*).
**Reframe:** Strategy supplies first-class evidence ("this invariant is costing us adoption in segment X — here's the data"); the Architecture owner decides whether to keep, relax, or re-engineer it.

### AP-13 · Kernel erosion
**Pattern:** Over time, implementations leak into the mandatory core — a favored cadence, tool, or scaling fork starts being treated as "part of VAST" — or a published non-goal quietly becomes prescribed. The small portable core bloats into a methodology.
**Violates:** Principle 4 (Separate invariants from implementations); the Kernel's published Non-goals.
**Reframe:** Guides, Adapters, and Experiments stay outside the Kernel unless the steward deliberately promotes one. The refusals are protected, not eroded by accretion. *(The framework applying its own invariants/implementations split to itself.)*

---

**Sources** (framework v3.3): `kernel.md` (principles, rules, non-goals); `vast.md` ("Intentional, not strict" — architecture-by-default and the waterfall misread; "Composition depth"); `applicability.md` ("Common mistakes"; minimum-viable-depth as guide-level guidance); `standard-framework.md` ("Where it breaks"; OKR conflation; Values-as-aspirational); `glossary.md` ("Challenge Flow"); `governance.md` ("Vision Falsification Protocol"); `architecture-levels.md` (Values anchored in Architecture). Detection-tuned companion: `plugins/vast-skills/references/anti-patterns.md`.
