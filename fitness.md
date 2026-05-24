# VAST Layer Fitness

VAST disciplines the *order* of commitment; fitness asks the orthogonal question — **is each layer actually doing its job?** A layer can exist, be owned, and still be unfit: an Architecture that can't support the compositions Strategy needs, a Strategy selecting use-cases that serve no committed experience, Tactics shipping outputs nobody uses.

This is deliberately **thin** — one diagnostic question per layer, asked in the existing planning/review rhythm by the layer's accountable role. It is **not**:

- a **maturity ladder** (a [Kernel](kernel.md) non-goal) — there are no levels 1–5, only "fit / unfit-and-why";
- a **metric model** — *how* success is measured numerically is OKRs' job, not VAST's (see [`references/okrs.md`](references/okrs.md)). Fitness is the structural check OKR *scoring alone* can't give: OKRs can score green while VAST is broken — every objective met, yet Architecture still decided by default.

Fitness extends the **Vision Falsification Protocol** ([`governance.md`](governance.md)) downward: that protocol is *Vision's* fitness check (is the committed hypothesis surviving reality?); the questions below are its thin equivalents for the other three layers.

## The questions

| Layer | Fitness question | Unfit looks like |
|---|---|---|
| **Vision** | Are the falsification triggers observable, owned, and monitored — and are fired triggers reviewed to a documented outcome? | No triggers, or triggers unowned / unmonitored / fired-but-never-reviewed. *(A reviewed decision to revise or hold is healthy falsification, not unfitness.)* |
| **Architecture** | For an in-scope use-case, can the framework support the composition — or return a documented accept / defer / decline — while preserving its invariants and values-as-constraints? | Strategy routinely commits *around* Architecture; invariants quietly bypassed; implementations treated as invariants; values that constrain nothing. |
| **Strategy** | Can every active use-case name the Vision experience it serves, the Architecture support it relies on, and the signal for *why now*? | Use-cases that trace to none of the three; selection on opinion rather than evidence; constant thrash. |
| **Tactics** | Are the things we ship actually landing — used and valued by real users — with that adoption signal flowing back up? | Output without adoption; "we shipped it" treated as "it worked"; no feedback returning to Strategy. |

**Where unfit shows up:** unfit answers are where the [anti-patterns](anti-patterns.md) surface — Architecture-unfit as AP-01 (architecture-by-default), AP-04 (implementation-as-invariant), or AP-08 (values-as-posters), with bypassed invariants showing as AP-12; Strategy-unfit as AP-06 (task-lists-as-Strategy) or AP-12; Vision-unfit as AP-07. Tactics-unfit is a delivery-*effectiveness* failure — not a structural anti-pattern, but a signal that must route upward (feedback flows up).

## How to use it

- **Qualitative, not scored.** The answer is a short honest narrative ("fit, because…" / "unfit, because…"), not a number. If you want numbers, those are the layer's OKRs — a different instrument.
- **Owned by the layer's accountable role.** The same neck that owns the layer answers for its fitness.
- **Distinct from minimum-viable-depth.** [`applicability.md`](applicability.md)'s MVD floor asks *is VAST present?*; fitness asks *is it working?* A layer can pass MVD and still be unfit — that gap is what fitness surfaces.
- **An unfit answer routes; it doesn't panic.** Each failure has machinery the framework already provides:
  - **Vision-unfit** → the Vision Falsification Protocol.
  - **Architecture-unfit** → Route A of the **Challenge & Escalation Protocol** ([`governance.md`](governance.md)): Strategy supplies evidence; Architecture returns a documented accept/defer/decline preserving invariants; an unresolved committed-Vision gap is informed up to Vision.
  - **Strategy-unfit** → re-select use-cases, or Route B if the misfit is a scope change.
  - **Tactics-unfit** → fix execution, or escalate to Strategy for triage.

  Fitness is the prompt to use that machinery — not a new ceremony.

---

**Sources:** `governance.md` (Vision Falsification Protocol; Challenge & Escalation Protocol), `anti-patterns.md` (the failure modes unfit answers surface), `applicability.md` (minimum-viable-depth floor), `references/okrs.md` (why fitness ≠ OKR scoring), `kernel.md` (the maturity-ladder non-goal).
