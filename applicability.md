# Applicability — composition depth × organizational scope

VAST applies everywhere its shape fits, but at different depths. Two axes determine how much framework to bring to a given piece of work:

1. **Composition depth** — how rich is the skill library and composition framework this work requires?
2. **Organizational scope** — is this product-engineering work, shared platform, function-level, or company-wide?

Combine the two to answer "do we apply VAST here, and how deeply?". No mode switch — single framework, varying depths.

## Composition depth — a spectrum, not a binary

Earlier versions of VAST distinguished "Strict" vs "Lite" modes. Adversarial review correctly noted this was a structural concession: if Lite mode means "shared vocabulary + relaxed sequence," it undermines the framework's force and suggests the core claim is narrower than advertised.

The revised framing: VAST applies as a spectrum of **composition depth**. Same discipline (Vision committed, Architecture intentional, Strategy within, Tactics delivers) at every depth. What varies is the richness of the composition framework:

| Depth | Composition framework characteristics | Example domains |
|-------|---------------------------------------|-----------------|
| **Deep** | Rich skill library (dozens of atomic capabilities), complex interfaces, many invariants, substantial architecture investment, dedicated framework-evolution capacity | Product engineering of core AI-first features; shared AI platform; substrate governance |
| **Medium** | Moderate skill library (a handful of capabilities), explicit interfaces, core invariants, ongoing but lighter architecture work | AI-enabled function-level work (AI-assisted CX routing, marketing content systems, finance forecasting tooling) |
| **Light** | Small library (often single-skill usage), simple interfaces, minimal formal invariants | Function-level work with minimal AI substrate dependence (HR systems, standard reporting) |
| **Vocabulary only** | No formal library. V-A-S-T used as language for planning conversations | Company-wide strategic discussions; cross-function alignment; operating-model conversations |

Decision rule: use the depth the work requires. Don't force deep composition framework for light-composition work (produces ceremony without value). Don't pretend vocabulary-only for work that genuinely requires deep composition (produces architecture-by-default, the exact dysfunction VAST prevents).

## Organizational scope axis

Perpendicular to composition depth, organizational scope answers "where in the org does VAST apply and with what teeth":

| Scope | Treatment | Why |
|-------|-----------|-----|
| **Product engineering** | Deep composition framework; full VAST discipline (accountability per layer, Challenge Flow enforced, named commitments) | Composition framework IS the defensible artifact here. Substrate volatility + personalization-by-default make intentional framework essential. |
| **Shared AI platform / substrate governance** | Deep composition framework; cross-consumer architecture decisions formalized | Multiple product domains depend on shared library + invariants. Framework mis-design affects everyone downstream. |
| **Function-level execution** (Marketing, Sales, CX, People, Finance, Legal) | Medium-to-light composition depending on AI integration level; vocabulary and explicit per-layer accountability; Challenge Flow as principle rather than enforced ceremony | AI integration at function level is usually lighter than product. Full discipline is overhead; vocabulary-level framework usually underserves. Match depth to function's actual AI substrate engagement. |
| **Company-wide execution** (annual strategy, OKR-setting, cross-function alignment) | Vocabulary only | Four-layer shape is useful shared language; full framework is out of scope. V-A-S-T as alignment tool, not governance protocol. |

### Combined decision guide

When deciding how VAST applies to specific work, answer both questions:

1. **Organizational scope.** What scope is this work — product-eng, shared platform, function, or company-wide?
2. **Composition depth.** Given that scope, what depth of composition framework does this specific work require?

The two answers combine to select the appropriate treatment. Examples:

- *"Shipping a new AI-assisted workflow in core product"* → product-eng scope, deep composition → full VAST discipline
- *"Implementing AI-drafted customer-support reply suggestions in CX"* → function scope, medium composition → VAST vocabulary + explicit accountability + core framework discipline but no dedicated governance body
- *"Setting company-wide annual OKRs"* → company-wide scope, vocabulary only → V-A-S-T shape for aligning layer-by-layer commitments, no framework overhead
- *"Redesigning pricing page layout"* → product scope, light composition → not VAST work; Growth/iterative practice is correct

## The original Growth / Core / Platform rigor axis

The original VAST boundary matrix distinguished Growth / Core Product / Platform with increasing rigor. This axis is still useful, but it is **folded into the composition-depth spectrum**:

- **Growth** work is typically light-composition or vocabulary-only. A/B tests don't need composition frameworks. Exception: when an experiment graduates into a new product surface that requires architectural capabilities, it moves into Core or Platform depth.
- **Core Product** work is medium-to-deep composition, depending on whether it's an iteration within existing framework (medium) or a new capability that extends the framework (deep).
- **Platform** work is always deep composition. Shared library components carry invariants that every consumer depends on.

## Graduation path

Discovery → validated → delivery decision → VAST at appropriate depth. Edge case to watch: **"experiment that accidentally becomes product"** — Growth tested, it worked, users now depend on it. At that moment: composition review → determine what depth the maintained version requires. Without a graduation path, successful experiments become structurally fragile because their composition-level commitments were never made.

The graduation path applies across scopes. A function-level AI experiment (medium composition) that becomes structurally load-bearing may need promotion to shared-platform concern (deep composition).

## Experimental (TTL) skills in discovery

Discovery is outside *VAST delivery governance* by design (see [`vast.md`](vast.md), "Delivery, not discovery") — **not** outside organizational risk governance. A team probing a hypothesis may stand up an **experimental skill** outside the library and its invariants **without** a VAST Architecture decision, provided it is explicitly experimental, **time- or scope-bounded** (a TTL), **non-load-bearing**, and still within the non-negotiable security / privacy / legal / safety guardrails. No probe should wait on an Architecture decision to test an idea.

The skill becomes a governance concern only at the **graduation gate**: when the probe validates, the skill either enters the library under full invariant coverage (an Architecture decision) or is **retired**. The anti-pattern this prevents is an experimental skill silently becoming load-bearing — the same shape as "experiment that accidentally becomes product," at skill granularity.

## Platform threshold

Not everything shared is Platform. Promoting work to the shared-platform layer requires:

- **Repeated use cases** — multiple consumers with structurally similar needs
- **Measurable internal demand** — consumers would pay (in budget or time) for the shared capability
- **Clear owner** — named accountable role, not a volunteer
- **Lifecycle commitment** — someone owns maintenance, deprecation, migration

Otherwise "Platform" becomes a dumping ground for orphaned skills that no one owns and no one consumes. Platform threshold is a defensive concept: it prevents the pattern where every shared utility claims platform status and inherits deep-composition overhead without corresponding value.

## Recursion threshold

Not everything nested earns its own V→A→S→T (the Matryoshka condition — see [`vast.md`](vast.md)). A scope spawns its own nested instance only if it has:

- **A distinct Vision** — its own falsifiable hypothesis, not a slice of the parent's
- **Local invariants** — guarantees of its own, beyond the parent's it inherits
- **Clean accountability** — one accountable owner per layer (one person may hold several at small scope)
- **Persistence** — a sustained scope, not a one-off effort (a one-shot is Tactics)

Fail any test → it's Strategy/Tactics *within* the parent, not a nested instance. A feature is the typical termination point. Like the Platform threshold above, this is defensive: it prevents recursion-sprawl where every team or feature claims its own framework. The bar is about Vision/invariant/ownership distinctness — not team size or LOC.

## Common mistakes

- **Forcing deep composition where medium-or-light fits.** A marketing team's content-generation tool choice does not require the depth of composition framework that the core product's AI runtime does. Applying full discipline here produces ceremony and generates legitimate pushback that damages framework credibility in domains where depth actually fits.
- **Applying vocabulary-only where medium-or-deep is needed.** A new shared AI capability decided via "V-A-S-T language only, no real framework" leads back to architecture-by-default — the dysfunction VAST exists to prevent. Keep depth proportional to what the work actually requires.
- **Confusing Platform threshold with composition-depth applicability.** Work can require deep composition without meeting Platform threshold (a single-team capability with serious architectural implications). Decision: work the composition depth, wait for cross-team promotion until platform criteria are met.
- **Mistaking light composition for "no framework at all".** Even light-composition work benefits from explicit accountability per layer. The difference between light and vocabulary-only is whether there's a real composition framework (even if small) or just shared language.

## Minimum viable depth — what counts as "VAST applied"

A common trap with composition-depth spectrums: "vocabulary-only" depth becomes a label that anyone can claim. "We use VAST" then means nothing because the claim is unfalsifiable. The framework needs a floor — observable conditions that distinguish "VAST applied" from "VAST vocabulary used."

**Two things wear the word "vocabulary" — keep them apart:**

- **Vocabulary-only *depth*** is the lightest point on the composition-depth spectrum — four-layer language for company-wide alignment, with little or no formal skill library. It is a statement about *how much composition framework* the scope carries, not a verdict on conformance.
- **VAST vocabulary, not VAST applied** is using the four-layer language while sitting *below the floor* — the failure the floor exists to catch.

These are different axes. *Depth* answers "how much composition framework does this scope carry?" The *floor* answers "is the discipline actually present?" Depth scales the framework's richness; it never lowers the floor. "We're only at vocabulary-only depth" is therefore not a licence to skip the floor — a light-depth scope still names a falsifiable Vision and one accountable owner per layer, or it is honestly *vocabulary, not applied*.

**A third axis: domain-fit — is VAST the right tool here at all?** Depth and floor both presume VAST fits the scope; whether it fits is a prior question, assessed **per domain, not per company.** VAST is a delivery framework for work whose Vision is committable and whose Architecture carries real invariants — Cynefin's Complex/Complicated. A domain that is genuinely pre-PMF, where Vision is unknown before market contact (Cynefin Chaotic), is better served by Lean Startup / MVP discovery; VAST there is over-engineered (see [README](README.md)). A single company is routinely post-PMF in one domain (apply VAST) and pre-PMF in another (don't) at the same time. Assess fit domain by domain — do not inherit one domain's verdict across the company.

Five conditions must all hold for the work to count as VAST application (at any depth):

1. **Vision is named, committed, and has falsification triggers.** Not "we make great products" or "we serve customers well." Specific experience commitment ("we enable [these experiences] for [these users]") with observable revision conditions ("revise if [this metric] crosses [this threshold] for [this duration]").
2. **Architecture has a named accountable owner.** Single neck. Makes intentional composition framework decisions, not default-by-accumulation. Owner name is publicly known.
3. **Composition framework actually exists in some minimal form.** At least: skill boundaries listed, basic interfaces named, at least one or two invariants documented (a quality contract, a fallback policy). Even at light depth, some real framework — not just "we'll figure it out as we go."
4. **Strategy decisions reference Architecture commitments explicitly.** "We're sequencing experience X because the composition framework supports skills Y and Z" — not ad-hoc Strategy in vacuum, not "Strategy decided this and Architecture will figure it out."
5. **At least one observable Challenge Flow instance per quarter.** Stated rule ≠ observed practice. In the past quarter: a Strategy signal flowed up to Architecture (informing); or Vision challenged Architecture; or Tactics escalated; or Architecture self-corrected based on a documented signal. At least one real instance documented.

**Threshold:** if all 5 hold, VAST is applied — at whatever depth the work warrants. If 4 of 5 hold, VAST is partially applied; identify which condition is missing and address it. If 3 or fewer hold, the work is using VAST vocabulary but not applying the framework — call it that honestly.

This floor is the framework's falsifiability test. Without it, "we use VAST" claims are unverifiable. With it, VAST application is observable: someone who doesn't know the team can read the artifacts and tell whether the conditions are met.

## What VAST does not cover for AI transformation

VAST is the operating-model layer of an AI transformation effort, not the full transformation playbook. Treating it as the whole solution invites disappointment and is honest grounds for legitimate pushback from executives whose responsibilities span the broader transformation.

Out of scope, requiring complementary frameworks or practices:

- **Financial discipline.** When is AI investment justified? What ROI framework applies? What are the unit economics of composition framework investment vs feature-by-feature delivery? VAST does not provide financial criteria for go/no-go decisions; CFO-led financial governance does.
- **Change management.** How do you bring people along through the transition VAST implies (middle-management sorting, authority shifts, role re-shaping)? VAST names the consequences (`references/consequences.md`) but does not provide the change-management practice. Kotter's 8 steps, ADKAR, Prosci — pick one; VAST does not substitute.
- **Talent strategy.** What new capabilities must the org hire (composition specialists, AI architects, domain-judgment owners, edge sensors)? What capabilities decline in demand (information-routing middle managers)? VAST does not provide hiring strategy; talent-leadership planning does.
- **Vendor strategy.** Build, buy, or partner — for which AI capabilities? When is in-house substrate worth the investment vs. wrapping commercial APIs? VAST is largely substrate-agnostic at the invariant level; vendor strategy is a separate discipline.
- **Risk management.** Governance, compliance, security, IP, regulatory exposure — these are mentioned as invariants but the practice of risk identification, assessment, mitigation requires dedicated frameworks (NIST AI RMF, ISO 42001, internal risk frameworks).
- **Cultural transformation.** How does the org shift mindset toward AI-first thinking — beyond structural changes? VAST does not address culture explicitly; it requires complementary work.
- **Customer / market communication.** How does the AI transformation get communicated to customers, partners, regulators, market? Outside VAST scope; PR / IR / customer-facing functions own this.

VAST positions itself as the operating-model layer that organizes how product, function, and company decisions are made and sequenced in an AI-first context. AI transformation requires VAST + financial framework + change management + talent strategy + vendor strategy + risk management + cultural work + market communication. They compose; VAST does not replace any of them.

When VAST is presented to executives as "the AI transformation framework," they correctly object that it is missing five other workstreams. The honest framing is: "VAST is the operating-model layer; here are the complementary workstreams; together they constitute the transformation playbook."

## References

- [`vast.md`](./vast.md) — core framework definition
- [`governance.md`](./governance.md) — accountability pattern scales with composition depth
- [`architecture-levels.md`](./architecture-levels.md) — Architecture content at product / org-design / WoW levels
- [`applications.md`](./applications.md) — worked function-level VAST examples
- [`references/consequences.md`](./references/consequences.md) — political implications of composition-framework authority
