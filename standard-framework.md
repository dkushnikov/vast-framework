# VAST vs standard frameworks

_New here? Start with [quick-start.md](quick-start.md) · [What is VAST?](vast.md) · [Find your role →](guides/)_

How VAST relates to the canonical corporate stack. VAST is an extension at complexity threshold, not a replacement.

## The standard stack

Most organizations operate with some version of:

```
Vision → Mission → Values → Strategy → Roadmap → OKRs → Tasks
```

This works. For simple systems where Architecture is implicit — a startup with one product, one market, one team — everyone knows the domains, the structure is understood, and jumping from Vision to Strategy is fine.

## Where it breaks

When complexity grows (multi-product company, multi-function organization, multi-domain system), implicit Architecture becomes invisible. Strategy without explicit Architecture is guessing — optimizing without articulating what the system consists of.

Two specific failure modes:

**1. Values treated as aspirational, not structural.** The standard stack puts Values next to Vision/Mission — all "aspirational." But Values are architectural constraints: they define HOW the system operates, not WHERE it's going. "Customer obsession" shapes product architecture. "Win Together" constrains collaboration model. Values anchored in Architecture get a structural job. Values in Vision stay on posters.

**2. OKRs conflate three levels.** Objectives ≈ Outcomes (Architecture — what domains matter). Key Results ≈ mix of Use Cases (Strategy — where to invest) and Outputs (Tactics — what to produce). This compression works when Architecture is implicit and understood — everyone knows what domains matter, so Objectives naturally connect to structure. It breaks when Architecture is invisible — OKRs disconnect from structural understanding and degenerate into task lists.

## VAST mapping

| Standard | VAST layer | Notes |
|---|---|---|
| Vision | Vision | Clean mapping |
| Mission | Vision | VAST compresses Vision + Mission — in practice often indistinguishable |
| Values | **Architecture** | Anchored in Architecture as structural constraints. Cross-cut all layers, but structural home = Architecture (deliberate simplification) |
| Strategy | Strategy | Clean mapping |
| Roadmap | Strategy → Tactics | Not a separate layer — output of Strategy |
| OKRs | Spans Architecture + Strategy + Tactics | Objectives ≈ Outcomes, KRs ≈ Use Cases + Outputs |
| Tasks | Tactics | Clean mapping |

## Position: extension at complexity threshold

VAST doesn't say the standard framework is wrong. It says: **the standard framework is incomplete for complex systems.**

Architecture layer becomes necessary at a certain level of complexity. Making it explicit is what Balanced Scorecard, Wardley Maps, and TOGAF do in practice — VAST makes it a named step in the canonical sequence, like the Agile Manifesto named iterative development that teams were already doing.

For simple systems, the standard framework is sufficient. For complex systems, it's incomplete. VAST adds the explicit Architecture waypoint for systems that need it.

## Prior art

VAST is codification and synthesis of scattered expert practice, not invention:

| Prior art | What it contributes | How VAST relates |
|---|---|---|
| [Balanced Scorecard](https://en.wikipedia.org/wiki/Balanced_scorecard) (Kaplan & Norton, 1992) | 4 perspectives cascade, strategy maps | Closest Architecture + Strategy + Tactics. VAST adds explicit Vision layer |
| [Wardley Maps](https://en.wikipedia.org/wiki/Wardley_map) (Wardley) | Value chain visibility, evolution axis | Best Architecture visualization + complexity awareness. VAST adds Vision + Tactics cascade |
| [Beer's VSM](https://en.wikipedia.org/wiki/Viable_system_model) (Beer, 1972) | 5-system cybernetic model, fractal recursion | Mathematical rigor, self-regulation. VAST is simpler, less rigorous |
| [Boyd's OODA](https://en.wikipedia.org/wiki/OODA_loop) (Boyd) | Orient as mental model building | Orient ≈ Architecture. OODA = continuous loop; VAST = commitment cascade |
| [TOGAF](https://en.wikipedia.org/wiki/TOGAF) | Enterprise architecture standard | Exhaustive, certifiable. VAST is lightweight, no certification |
| [NCT](https://www.reforge.com/blog/replace-okrs-with-ncts) (Reforge) | Narrative → Commitments → Tasks | Closest 3-level split to VAST triad. Product-team scoped |
| [Ackoff's idealized design](https://en.wikipedia.org/wiki/Russell_L._Ackoff) | System redesign before strategy | "Define the system before selecting strategies" — same insight as VAST Architecture |

## Feature comparison: VAST vs business/org frameworks

✓ = explicit, △ = partial/implicit, ✗ = absent.

| Capability | **VAST** | BSC | OKRs | NCT | Wardley | Beer's VSM | OODA | TOGAF | Cynefin |
|---|---|---|---|---|---|---|---|---|---|
| **Explicit Vision layer** | ✓ | △ | △ | ✓ (Narrative) | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Explicit Architecture layer** | ✓ | ✓ (4 perspectives) | ✗ | ✗ | ✓ (value chain) | ✓ (5 systems) | △ (Orient) | ✓ (enterprise arch) | ✗ |
| **Explicit Strategy layer** | ✓ | ✓ | △ | ✓ (Commitments) | ✓ (movement) | △ (System 4) | ✗ | △ | ✗ |
| **Explicit Tactics layer** | ✓ | ✓ (initiatives) | ✓ (KRs) | ✓ (Tasks) | ✗ | △ | ✓ (Act) | ✗ | ✓ (domain response) |
| **Top-down sequencing** | ✓ (V→A→S→T) | △ (cascade) | ✗ | △ (N→C→T) | ✗ | ✗ | △ (loop, not cascade) | △ (phases) | ✗ |
| **Complexity threshold** | △ (stated, not operationalized) | ✗ | ✗ | ✗ | ✓ (evolution axis) | ✓ (variety) | ✗ | ✗ | ✓ (core purpose) |
| **Values as structural constraints** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | △ (Orient culture) | ✗ | ✗ |
| **Outcomes/Use Cases/Outputs split** | ✓ | △ | △ (O + KR) | ✓ (N + C + T) | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Proven at scale (10+ years)** | ✗ | ✓ (30+ years) | ✓ (Google, Intel) | ✗ (niche) | △ (growing) | △ (niche) | ✓ (military) | ✓ (enterprise) | ✓ (consultancy) |
| **Simplicity / adoption speed** | ✗ (4 layers) | △ | ✓ (one page) | ✓ (three words) | ✗ (steep) | ✗ (very steep) | ✓ (4 words) | ✗ (months) | △ |
| **Speed / tempo advantage** | ✗ (cascade) | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (designed for speed) | ✗ | ✗ |
| **Visual situational awareness** | ✗ | ✓ (strategy maps) | ✗ | ✗ | ✓ (landscape maps) | ✗ | ✗ | ✓ (arch diagrams) | ✓ (domain plot) |
| **Domain detection (when NOT to use)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (core purpose) |
| **Mathematical rigor** | ✗ | △ (financial) | ✗ | ✗ | ✗ | ✓ (variety engineering) | ✗ | ✗ | ✗ |
| **Recursive (same model every scale)** | △ (claimed, not proven) | ✗ | △ (team → company) | ✗ | ✗ | ✓ (fractal) | ✓ (any scope) | ✗ | ✓ (any decision) |
| **Continuous loop (not linear)** | ✗ (cascade) | ✗ | △ (quarterly batch) | ✗ | ✗ | ✓ (feedback loops) | ✓ (core design) | ✗ | ✗ |

**What each framework does that VAST cannot:**
- **BSC** — proven 30-year track record, strategy maps as visual causal chains, deep financial integration
- **OKRs** — radical simplicity. One page, everyone gets it. Quarterly cadence built-in
- **NCT** — narrative-as-storytelling. Product-team native
- **Wardley** — evolution axis shows WHERE on the commodity curve. Visual landscape before strategy
- **VSM** — mathematical rigor. Fractal recursion. Self-regulation theory
- **OODA** — speed and tempo advantage. Continuous loop. VAST is thoughtful; OODA is fast
- **TOGAF** — exhaustive, certifiable, auditable. Enterprise standard
- **Cynefin** — tells you when NOT to use a framework. Domain detection

## References

- [`vast.md`](./vast.md) — core framework definition (the triad and four layers defined here)
- [`architecture-levels.md`](./architecture-levels.md) — Architecture at three levels, Values anchored in Architecture (deeper treatment)
- [`glossary.md`](./glossary.md) — shared vocabulary
- [`why-now.md`](./why-now.md) — the economic argument that motivates VAST
- [`references/external-validation.md`](./references/external-validation.md) — independent convergence with prior art
