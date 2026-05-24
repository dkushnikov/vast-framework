# VAST as Philosophy — Challenge to Standard Frameworks

_Thinking note, 2026-04-26. Needs adversarial review before promotion to canonical._

## Positioning (validated 2026-04-27)

> VAST is a sequencing philosophy, deliberately layered. It builds on what already works — Balanced Scorecard's architecture, OKRs' alignment, Wardley's situational awareness — and adds one thing: an explicit cascade from Vision through Architecture to Strategy before Tactics. When systems grow complex enough that implicit structure stops working, VAST makes it visible.

Tone: LeSS-inspired. Part of continuum (acknowledges prior art), not standalone invention. "Deliberately layered" echoes LeSS's "deliberately simple."

## The claim

VAST is not only a product framework. It's a **sequencing philosophy for complex systems**: Vision → Architecture → Strategy → Tactics. Product delivery is one instantiation. Company operating models, and other complex domains are equally valid instantiations of the same philosophy.

## The triad: Outcomes / Use Cases / Outputs

Three VAST layers below Vision map to a triad that's cleaner than standard frameworks:

| VAST layer | Triad role | What it answers |
|---|---|---|
| **Architecture** | **Outcomes** | What are we growing? What domains matter? |
| **Strategy** | **Use Cases** | Where do we work? How do we invest? |
| **Tactics** | **Outputs** | What do we concretely produce? |

## Challenge to the standard corporate framework

Standard corporate stack:
```
Vision → Mission → Values → Strategy → Roadmap → OKRs → Tasks
```

VAST:
```
Vision (= Vision + Mission + Values)
→ Architecture (= Outcomes)
→ Strategy (= Use Cases)
→ Tactics (= Outputs)
```

### The implicit layer made explicit: Architecture

The standard simplified stack (Vision → Strategy → OKRs → Tasks) jumps from "why" to "how." No explicit waypoint says: "what is the structure of the system we're optimizing?"

Architecture exists in practice — BSC, Wardley Maps, TOGAF, Beer's VSM all serve this function. But it's absent from the canonical stack most organizations actually use. VAST names this implicit practice and makes it a required waypoint, like the Agile Manifesto named iterative development that teams were already doing.

When Architecture stays implicit, two failure modes emerge:

1. **Disconnected strategies.** Companies know why (Vision) and decide what to do (Roadmap), but don't articulate the structural domains and their expected Outcomes. Strategy without explicit Architecture is guessing — optimizing without articulating what the system consists of.

2. **OKRs conflate three levels.** Objectives ≈ Outcomes (Architecture layer). Key Results ≈ mix of Outputs (Tactics) and Use Cases (Strategy). This works when Architecture is understood implicitly. When it's not — OKRs degenerate into task lists because the unnamed Architecture layer collapses Outcomes into Outputs.

## Implications for the VAST repo

The current repo is written in product language — composition frameworks, skill libraries, interfaces. This is one instantiation, not the whole thing.

Proposed conceptual split:

1. **Philosophy** — universal sequencing principle (V→A→S→T), Outcomes/Use Cases/Outputs triad, challenge to standard frameworks. Substrate-agnostic.
2. **Product application** — AI-first delivery, composition architecture, skill libraries. Current repo content.
3. **Other applications** — company operating models, other complex domains. Each instantiation maps V/A/S/T to its own vocabulary.

Philosophy is the root. Applications are instantiations.

## VAST vs standard framework: extension, not replacement

Honest mapping of the standard corporate stack onto VAST:

| Standard | VAST layer | Notes |
|---|---|---|
| Vision | Vision | Clean. Both = direction. |
| Mission | Vision | VAST compresses Vision + Mission. In practice often indistinguishable. |
| Values | **Architecture** | Standard puts Values next to Vision (aspirational). But Values are constraints on how the system is built, not direction. "Customer obsession" shapes HOW you build, not WHAT. |
| Strategy | Strategy | Clean. Both = how we win. |
| Roadmap | Strategy → Tactics | Not a separate layer. Output of Strategy, not a peer. |
| OKRs | Spans Architecture + Strategy + Tactics | Objectives ≈ Outcomes (Architecture). Key Results ≈ mix of metrics (Strategy) and outputs (Tactics). OKRs conflate three levels. |
| Tasks | Tactics | Clean. |

### The nuanced claim

The standard framework is not wrong. It works for simple systems where Architecture is implicit — a startup with one product, one market, one team all know their domains without writing them down.

**VAST says: the standard framework is incomplete for complex systems.** Architecture layer becomes necessary at a certain level of complexity. When domains multiply (multi-product company, multi-capital life), implicit Architecture becomes invisible — and invisible structure can't guide strategy. Making it explicit is what BSC, Wardley, and TOGAF do in practice; VAST makes it a named step in the canonical sequence.

### Values: anchored in Architecture

The standard framework lumps Vision, Mission, and Values as "aspirational." VAST anchors Values in Architecture — because that's where they have the most structural impact.

Values are architectural constraints: checks and balances of a complex system. Proto-institutions that define HOW decisions are made, not WHAT is optimized. They constrain the solution space for Strategy and Tactics.

Values technically cross-cut all VAST layers (they influence Vision, Strategy, Tactics too). But they're **anchored** in Architecture because that's where they do structural work: constraining how domains interact. This is a deliberate simplification — the same way Scrum is "intentionally incomplete."

This reframe explains why companies treat Values as posters on the wall: the standard framework places them in Vision (aspirational), so they stay aspirational. Anchoring them in Architecture gives them a structural job.

### OKRs: conflation by design?

OKRs bridge Architecture → Tactics in one construct. This works when Architecture is implicit and understood — everyone knows what domains matter, so Objectives naturally connect to structure. It breaks when Architecture is implicit and poorly understood — OKRs disconnect from structural understanding and degenerate into task lists. The framework isn't wrong, it just assumes a layer it doesn't name.

### Position: VAST = extension at complexity threshold

VAST doesn't replace Vision/Mission/Values/Strategy/Execution. It adds Architecture as an explicit layer for systems complex enough to need it, and reveals that Values are structural (Architecture), not aspirational (Vision). For simple systems, the standard framework is sufficient. For complex systems, it's incomplete.

## Framework properties (from Nestor review)

### Bidirectionality

V→A→S→T = logical priority, not temporal lockstep. In practice the arrows are bidirectional: Strategy reveals Architecture gaps, Tactics inform Strategy. The sequence says where to **start**, not a one-way waterfall. Strict linear V→A→S→T is an anti-pattern in volatile environments — the cascade describes commitment priority, not execution order.

### Architecture must be concrete per instantiation

"Architecture" means different things at different scopes: composition framework (product), org capabilities (company), Life Capitals (life). The abstract concept — "the structural domains of the system" — is shared. The content is scope-specific. Each instantiation must define Architecture concretely: specific domains, specific boundaries, specific interactions. Without this, Architecture risks becoming a label that sounds precise but means anything.

## Open questions for adversarial review

1. **Is "Architecture = Outcomes" the right framing?** In the product instantiation, Architecture = composition framework (structural). In other instantiations, Architecture might map to domain structure or outcome domains. Are these really the same concept, or does "Architecture" mean different things at different scopes?

2. **Does the OKR critique hold up?** OKRs have been successful at many companies. Is the claim that they "conflate three levels" fair, or is it a straw man? Maybe OKRs work *because* they compress levels, not despite it.

3. **Naming vs novelty.** BSC, capability maps, Wardley Maps already serve Architecture function. VAST's contribution = naming it as a required waypoint in the canonical stack, not discovering a new concept. Is naming sufficient value, or does VAST need to add something these tools don't?

4. **Is "sequencing principle for evolving complex systems" too broad?** If VAST applies to everything, does it apply to nothing specifically? A framework that explains all phenomena equally well may have low predictive/prescriptive power.
