# The VAST Kernel

VAST is deliberately layered by **durability**. The Kernel is the small, mandatory, substrate-portable core — the invariants that make something *actually* VAST. Everything else is explicitly optional and swappable:

**Kernel** (mandatory) → **Guides** (recommended, situational) → **Adapters** (integrations with what you already run) → **Experiments** (worth trying, expect to drop).

This layering is itself VAST's invariants-vs-implementations split applied *to VAST*: the Kernel is the invariants; Guides, Adapters, and Experiments are implementations. The framework eats its own dogfood.

## VAST Principles — the reasoning core

1. **Make Architecture explicit.** When implicit structure stops scaling, name the structural domains, constraints, and values *before* committing to Strategy. — *Strategy without explicit Architecture is optimizing without saying what the system is: the dysfunction VAST exists to prevent.*

2. **Commit by priority, not by sequence.** Fix Vision and Architecture first so downstream iteration compounds; all four layers run continuously and the arrows are bidirectional. — *Logical priority of commitment — neither waterfall nor emergent-everything.*

3. **Keep Outcomes, Use-Cases, and Outputs distinct.** Architecture owns Outcomes, Strategy owns Use-Cases, Tactics owns Outputs; never collapse them. — *Their conflation — objectives written as task lists — is the most common operating dysfunction.*

4. **Separate invariants from implementations.** Name what must always hold (substrate-portable) apart from what migrates as the substrate evolves. — *This is what stays defensible when the substrate is volatile — and it applies recursively, to VAST itself.*

5. **Anchor Values in Architecture.** Treat values as structural constraints that bound the solution space, not as aspirational posters. — *Values get a structural job, or they stay on the wall.*

6. **Challenge flows down; feedback flows up.** Vision challenges Architecture (the only downward challenge right); Strategy informs Architecture; feedback and falsifying evidence flow upward — and Vision is a committed hypothesis with named revision triggers. — *Keeps the cascade honest and the Vision falsifiable.*

7. **Minimal sufficiency.** Bring only the composition depth the work requires; VAST is an extension at a complexity threshold, not a total methodology — and it states what it refuses to prescribe. — *The guard against ceremony and cargo-culting.*

## VAST Rules — the non-negotiable minimum

A thing is *VAST* only if:

- All four layers are named, each with **one accountable owner**.
- **Architecture is made explicit before Strategy commits** — not after, not by default.
- **Vision is stated as a falsifiable hypothesis** with at least one named revision trigger.
- **Invariants are separated from implementations** wherever a composition framework is claimed.

Below this floor it is VAST *vocabulary*, not VAST *applied*.

## Non-goals — what the Kernel deliberately refuses

VAST does **not** prescribe: a delivery cadence or ceremonies; a portfolio/funding model; a scaling fork (Basic/Huge); a leadership-behaviour catalogue; a certification/trainer ecosystem; or a maturity ladder. It **integrates with** execution substrates (Scrum, OMIMO/P3.express, OKRs) through Adapters — it does not become one. Publishing these refusals is part of the framework's identity.

## Self-falsification — the Kernel applies to VAST too

VAST itself is a committed hypothesis, subject to its own Principle 6.

**Falsification triggers** — owner: the framework steward (currently Dmitry Kushnikov):

- **Applied-validation:** if **≥3 documented pilots** fail to show that Architecture-first prevents the dysfunctions VAST claims (architecture-by-default; strategy-without-structure), the core thesis is revisited.
- **Felt-as-ceremony:** if adopters consistently report that the Architecture step felt like *ceremony rather than clarity* — it added process without changing a decision — the framing (not just the wording) is revisited.

---

*Status: v1 (2026-05-24). Principles extracted from `vast.md`; layering, non-goals, and self-falsification informed by a multi-model council (Nestor, deliberative) + research on OMIMO/LeSS/APOM. Reviewed: principle cut confirmed; passed a `vast-validate` dogfood (one fix applied — self-falsification trigger completed).*
