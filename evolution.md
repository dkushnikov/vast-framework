# Evolving VAST

How the framework itself changes — promotion, retirement, and the protection of its refusals. (This is about evolving *VAST*, not how an instance's Architecture evolves; the latter is ordinary Architecture self-correction, covered in [`vast.md`](vast.md).)

VAST governs its own evolution the way it asks adopters to govern theirs: it applies VAST to VAST. What's being governed is the [Kernel](kernel.md)'s durability layering —

**Kernel** (mandatory) → **Guides** (recommended, situational) → **Adapters** (integrations with what you already run) → **Experiments** (worth trying, expect to drop).

## The lifecycle — what moves, and how hard

| Move | When | Friction |
|---|---|---|
| **Experiment → Guide** | Proves useful across more than one real application. | Low — the expected success path. |
| **Experiment → Adapter** | Proves useful specifically as an integration with an execution substrate (Scrum, OKRs, OMIMO/P3.express). | Low — it stays substrate-coupled. |
| **Experiment → dropped** | Didn't earn its place. | None — Experiments are *expected* to drop; dropping one isn't failure. |
| **Adapter pattern → Guide** | Repeated adapters reveal a substrate-portable pattern worth recommending. | Medium — extract the *pattern* as a Guide; the Adapter itself stays an Adapter. |
| **Guide → deprecated** | A Guide is superseded, stops earning its place, or causes confusion. | Low-to-medium — document it; Guides are recommended surface. |
| **Guide → Kernel** (*canonization*) | The Guide is a true invariant (see the test below). | **High, deliberately.** Most Guides never promote — that is correct. |
| **Kernel → Guide / removed** | A core element proves optional-but-useful (→ Guide) or false (→ removed). | **Highest** — explicit steward decision; invokes self-falsification only when the core *thesis* is implicated. |

The asymmetry is the point: **promotion into the Kernel — and demotion out of it — are high-friction; retirement *outside* the Kernel is low-friction.** That keeps the Kernel small (Principle 7, minimal sufficiency) and is the structural defense against [AP-13, Kernel erosion](anti-patterns.md).

**Canonization test — a Guide promotes to the Kernel only if all hold:**

1. **Invariant** — substrate- and context-portable, not an implementation;
2. **Identity** — omitting it would violate what makes a thing *actually* VAST;
3. **Evidence** — documented usefulness across materially different real applications;
4. **Minimality** — leaving it a Guide or Adapter would be genuinely insufficient;
5. **Refusal-compatible** — it does not reverse a published non-goal (unless that refusal is explicitly reversed — see below).

## Protecting the refusals

The Kernel's published **non-goals** (a delivery cadence, a portfolio/funding model, a scaling fork, a leadership-behaviour catalogue, a certification ecosystem, a maturity ladder) are first-class commitments, not gaps waiting to be filled. The default is that the refusal holds.

**Refusal gate** — every proposed change is checked: does it make a refused thing *required*, *expected for conformance*, or the *de-facto mark of "real VAST"*? If so, the change is invalid **unless** it is a signed refusal reversal. Accretion is the real erosion vector: a refused thing rarely arrives as "let's add X" — it arrives as a Guide or Adapter that quietly becomes mandatory. A legitimate reversal record names the refused item, the evidence, why Guide/Adapter treatment is insufficient, the exact Kernel change, owner + date, and migration impact.

## VAST applied to VAST

The framework is itself a VAST instance. The recursion is explicit:

| For VAST itself… | is… |
|---|---|
| **Vision** | the framework's purpose + its self-falsification thesis |
| **Architecture** | the Kernel, the durability layering, and the refusals |
| **Strategy** | which Guides / Adapters to invest in; release priorities |
| **Tactics** | experiments, docs, the plugin, concrete edits |

From that mapping the governance falls out:

- **Vision-as-hypothesis.** VAST's purpose is a committed, falsifiable hypothesis with named triggers — the [Kernel's self-falsification criterion](kernel.md).
- **Change is Architecture self-correction, not a challenge.** A proposed change supplies evidence; it does not mutate the Kernel by fiat. **Canonization and demotion are Architecture self-correction by the steward, within the current Vision** — which is why ordinary core changes don't require proving the purpose wrong. Only a claim that VAST's *purpose* is mistaken invokes Vision-level self-falsification.
- **One accountable owner per layer.** For VAST itself the framework steward (currently Dmitry Kushnikov) holds the accountable-owner role for all four layers; any delegation must name exactly one owner per layer (the Kernel floor applies to VAST too). Each decision is signed as a named change-record — decision type, affected layer, owner, date, rationale/evidence, affected docs, refusal impact — and the version history in [`README-full.md`](README-full.md) is the audit trail.
- **Fitness on the framework.** At each release or promotion/demotion decision, the steward asks the [layer-fitness](fitness.md) questions of VAST-as-a-system: is the Kernel still minimal *and* sufficient? Are the Guides earning their place, or has the surface bloated? — not a new ritual; attached to the change work already happening.

Evolving VAST is therefore not a special process bolted on — it is VAST, run on itself. A framework that couldn't govern its own change would fail its own Principle 6.

---

**Sources:** `kernel.md` (the Kernel / Guides / Adapters / Experiments layering, non-goals, self-falsification, Principles 6–7), `anti-patterns.md` (AP-13, Kernel erosion), `fitness.md` (fitness applied to VAST-as-a-system), `governance.md` (Challenge Flow + the accountable-owner pattern), `README-full.md` (version history as the change audit trail).
