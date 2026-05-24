# External validation and adjacent frameworks

VAST's structural claim — that in AI-first personalized-by-default software, the composition framework is the defensible artifact and organizing around it requires intentional commitment at Vision and Architecture layers — converges with several independent lines of thinking. This document engages with those lines explicitly, including the ones VAST draws from (genuine corroboration), the ones it is adjacent to (complementary, not overlapping), and the ones it appears to contradict but actually builds on.

Important caveat up front: adjacent framing is supporting evidence, not proof. Many operating-model frameworks cite overlapping sources; the combination does not uniquely validate VAST. Treat these references as context that confirms the direction, not unique-supporting evidence. Real validation comes from applied case studies with 12-18 month outcomes.

## Direct alignment — the composition-layer thesis

### From Hierarchy to Intelligence (Dorsey & Botha, Sequoia, 2024)

[Source](https://sequoiacap.com/article/from-hierarchy-to-intelligence/).

Jack Dorsey and Roelof Botha argue that AI makes hierarchy-based information routing redundant. Block's operational model replaces traditional middle management with an intelligence system: atomic capabilities + an AI composition layer at the edge.

This is structurally identical to VAST's composition-framework claim:

- Block's "atomic capabilities" = VAST's skill library
- Block's "AI composition layer at the edge" = VAST's Architecture (composition interfaces, invariants, orchestration patterns)
- Block's "maintain two world models (company state + customer behavior) as machine-readable artifacts" = the understanding that composition architecture codifies

Key quote relevant to VAST:

> *"What does your company understand that is genuinely hard to understand, and is that understanding getting deeper every day?"*

VAST operationalizes this at framework level: your Architecture (composition framework) codifies what your company understands. If the understanding is shallow or wrong, no amount of cheap iteration recovers — each iteration deepens commitment to the wrong codification.

Note: Dorsey and Botha argue for hierarchy *flattening*, not hierarchical sequencing. Earlier VAST formulations cited this piece as validation of strict-sequence waterfall — adversarial review correctly flagged that as cite-farming. The composition-layer reframing resolves the mismatch: VAST is not about preserving hierarchy, it is about formalizing authority for the specific artifact (composition framework) that becomes load-bearing when code commoditizes.

### Services: The New Software (Bek, Sequoia, 2026)

[Source](https://sequoiacap.com/article/services-the-new-software/).

Julien Bek argues the next trillion-dollar companies sell *work*, not tools. Intelligence (rule-following) vs judgment (experience-based decisions) is the key axis. AI automates intelligence-heavy work now; judgment follows. Autopilots (sell outcome) beat copilots (sell tool) because they capture the work budget, not just the software budget.

Key quote relevant to VAST:

> *"Today's judgment will become tomorrow's intelligence."*

This captures the commoditization argument for VAST: what your company uniquely judges now will be automatable soon. The only way to stay ahead is to continuously deepen domain understanding — which means continuously investing in the composition framework (skills that capture newly-hard judgment before it becomes tomorrow's commodity intelligence).

Both Sequoia pieces independently converge on: in cheap-AI-execution worlds, what your company uniquely understands is the moat. VAST operationalizes the observation by making Vision (what experiences we uniquely enable) and Architecture (composition framework that codifies understanding) the intentional anchors.

## Complementary frameworks — different questions, compatible answers

### Domain-Driven Design (Evans, 2003)

DDD addresses architecture-strategy interface through bounded contexts: domains have strong internal consistency and explicit interfaces at their boundaries. Each bounded context is, in VAST terms, a **skill library for a specific domain**, with its own invariants and its own composition patterns.

VAST builds on DDD at the AI-composition layer. Where DDD focuses on bounded contexts as the unit of architectural decomposition, VAST focuses on skill libraries and composition interfaces as the unit of AI-first architectural thinking. Bounded contexts translate cleanly to composition domains; DDD's aggregate boundaries translate to composition interface boundaries.

Practically: if you're using DDD, VAST adds intentional discipline about the composition layer that sits above bounded contexts (how skills from different contexts compose into user-facing experiences). If you're not using DDD, you may be reinventing it when you design composition interfaces.

### Team Topologies + Inverse Conway Maneuver (Skelton & Pais, 2019)

Team Topologies provides the structural vocabulary for modern engineering-organization design — stream-aligned teams, platform teams, enabling teams, complicated-subsystem teams. The **Inverse Conway Maneuver** is the principle most relevant to VAST: deliberately designing team structure to produce desired architecture, rather than letting organizational structure shape architecture by default.

Earlier VAST formulations cited Team Topologies as direct corroboration of strict-sequence V→A→S→T. Adversarial review correctly noted that Team Topologies actively argues for continuous organizational evolution — the opposite of strict sequencing.

The composition-layer reframing resolves the mismatch:

- Team Topologies tells you *what team structures produce a desired architecture*
- VAST tells you *what architecture is worth producing in an AI-first era* (composition framework)
- Applied together: design team types (per Team Topologies) to deliver composition framework (per VAST)

Inverse Conway still applies: if you want a coherent composition framework, design team structures that will produce it. Team Topologies and VAST operate at different layers of the same concern.

### Wardley Mapping (Wardley, ongoing)

Wardley Mapping provides situational awareness about where components in your value chain sit on the evolution curve from genesis (novel, unexplored) to commodity (standardized, undifferentiated). Components move along this curve over time.

VAST answers a different question: given that code generation is evolving toward commodity, how do you organize to build products where the defensible artifact is the composition framework sitting above commoditized substrate?

These are complementary:

- Wardley Mapping tells you *which components face commoditization pressure, in what order*
- VAST tells you *how to organize when composition-frameworks-on-commoditized-substrate becomes the product shape*

Adversarial review correctly noted that Wardley Mapping handles "where to invest architectural effort" with more situational awareness than VAST alone. The honest response: use Wardley Mapping to identify which parts of your product are under commoditization pressure; use VAST to organize the AI-composition framework that the Wardley analysis reveals you need.

### Cynefin (Snowden)

Cynefin classifies problems into Obvious / Complicated / Complex / Chaotic domains, with different appropriate responses: sense-categorize-respond / sense-analyze-respond / probe-sense-respond / act-sense-respond.

Adversarial review noted that AI-first product work often sits in Cynefin's Complex domain (probe-sense-respond), which appeared to contradict VAST's implicit Complicated-domain assumption (sense-analyze-respond with upfront design).

The composition-layer reframing resolves this:

- Individual composition outcomes are Complex — probing user behavior, sensing what works, responding with refined compositions
- The composition framework that supports this probing is Complicated (sometimes) or approaches Obvious as patterns stabilize — it has describable structure, known interfaces, explicit invariants
- VAST's Delivery vs Discovery boundary maps to Cynefin's Complicated vs Complex: Discovery is Complex probing; Delivery is Complicated composition once validated

The framework explicitly handles Cynefin's Complex domain through probe-sense-respond cycles at Strategy and Tactics layers, backed by stable Architecture at the composition framework level. Not a return to BDUF; a specific structural response to "how do you build stable composition frameworks for Complex-domain product problems."

## Claims VAST does not make

Explicitly not claiming:

- **Universal applicability across company stages.** Pre-PMF startups in domains where Vision truly is unknown before market contact — Lean Startup / MVP is the right framework, not VAST. Adversarial review emphasized this; the composition-layer reframing does not change the applicability boundary. VAST applies where the question has shifted from "what product to build" to "what composition framework supports the product we've validated."
- **Domain-universal.** VAST is tuned for software, specifically AI-first software where personalization-by-default is becoming the norm. In domains where the substrate is hardware, physical processes, regulated financial products, or other contexts where composition-framework thinking doesn't match the artifact structure, other frameworks fit better.
- **Substrate-lock.** VAST's Architecture is the composition framework, not the specific LLM choice. The framework is designed to survive substrate volatility — new models swap underneath without requiring framework rebuilds. The probabilistic-substrate objection from adversarial review is addressed in [`why-now.md`](../why-now.md).

## Practitioner signals

Beyond published frameworks, independent validation came from conversations with architects at adjacent companies during VAST's development phase (April 2026):

**Unified knowledge graph architecture** (a knowledge-graph architect). Building a unified knowledge graph combining personal and company data, this architect emphasized that *"architects must anticipate scope evolution"* — the same principle VAST applies to composition frameworks. Taxonomy and ontology, the argument went, must be shared and evolve at meta-level, not per-project. Structurally parallel to VAST's claim that the composition framework must be intentional across consumers, not accretively per-team.

**Agent framework infrastructure** (an agent-framework builder working on agentic workflow engines). Key design principle: **deterministic wrapper around non-deterministic agent node**. Agent = one node; everything around it is deterministic. Structurally parallel to VAST's composition framework: non-deterministic substrate (LLM responses) wrapped in deterministic composition (framework invariants, interface contracts, orchestration patterns).

## What this engagement accomplishes

The adversarial review raised a serious concern that VAST ignored adjacent frameworks (Wardley, DDD, Cynefin, Team Topologies) or misused them (Sequoia cite-farming). This document addresses both:

- **Misuse (Sequoia)** — resolved by the composition-layer reframing. Dorsey/Botha and Bek genuinely align with the composition-framework thesis; they do not align with strict-sequence waterfall. The new framing makes the alignment honest.
- **Ignored frameworks (Wardley, DDD, Cynefin, Team Topologies)** — engaged explicitly above. Each addresses a different question that VAST either builds on or is complementary to. None is a substitute, but several are prerequisites (DDD) or complementary (Wardley, Team Topologies, Cynefin).

Intellectual legitimacy requires this engagement. Ignoring adjacent work makes any framework look incurious. The revised VAST is built on prior frameworks where applicable and distinguishes itself where it does something different.

## References

- [`vast.md`](../vast.md) — core framework definition
- [`why-now.md`](../why-now.md) — the commoditization argument that motivates VAST
- [`case-studies/`](../case-studies/) — applied validation (ongoing)
