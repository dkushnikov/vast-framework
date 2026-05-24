# VAST Draft — AI in People / Recruiting (function scope)

> Fill top-down: commit Vision before investing in the layers below it. Each section gives the question to answer + what a good answer looks like. Stubs marked {to fill} are yours to author — where this scaffold left a question instead of an answer, that's deliberate: the seed didn't say, so the scaffold asks.

## Vision
**Answer:** {to fill} — the seed names a *domain* (the People function adopting AI in recruiting) but no Vision: no stated outcome for the function, no for-whom, no why. "Use AI in recruiting" is an intent to adopt a tool, not a committed hypothesis about what the function becomes.
**Guiding questions:**
- What does the *recruiting function* become with AI — what can it do, or do better, that it can't today? (Move faster through sourcing? Screen more consistently? Reduce time-to-hire? Widen the funnel? Remove bias?) Pick the stance.
- For whom — whose experience improves? Candidates (faster, fairer process)? Recruiters (less manual screening)? Hiring managers (better-matched shortlists)? Name the primary beneficiary.
- Why does this matter to the function's strategy — why AI in *recruiting* specifically, and why now?
**What good looks like:** a committed falsifiable hypothesis for the function — "the recruiting function enables {outcome} for {beneficiary}, because {what's broken/limited today}." Not "we use AI to be more efficient" (a slogan), and not a list of tools to buy (that's Tactics).
**Falsification triggers (required):** {to fill — name 2-5 conditions under which you'd revisit this stance. Each **observable** (a real recruiting metric — time-to-hire, screen-to-interview rate, offer-accept rate, adverse-impact ratio), **bounded** (threshold + duration), **owned** (a named role — likely a recruiting lead). For an AI-in-hiring context, a fairness/adverse-impact trigger is especially worth naming. Shape, not a value: "{metric} fails to {improve to threshold} within {duration} — owner: {role}".}

## Architecture
**Answer:** {to fill} — the seed names no tools, processes, or guarantees. Don't invent a tool stack; the questions below are the work.
**Guiding questions (function → capability framework — the function's capability set; "capability framework" is the function-native label for the same VAST Architecture artifact):**
- **Capability set** — which recruiting steps get AI, and which stay human? (AI-assisted sourcing? résumé screening / ranking? interview scheduling? candidate-message drafting? structured-interview scoring?) For each, what is it responsible for, and where does a human stay in the loop?
- **Interfaces / workflow** — how do these steps compose into the end-to-end hiring workflow (sourcing → screen → interview → offer), and where does the AI hand back to a person?
- **Invariants (must always hold — domain-native for recruiting)** — what are the non-negotiables? **Bias-and-compliance is the load-bearing invariant class here**: e.g. no automated reject without human review; audit trail for every AI-assisted decision; adverse-impact monitoring; candidate-data handling within policy; explainability of any ranking. Name at least one quality contract and one fallback (what happens when the model is low-confidence on a candidate).
- **Implementations** — which vendor/ATS integration, which model, prompt strategy — the substrate-coupled choices you expect to swap.
- **Who is the single accountable owner** for this capability framework (one named neck — a People ops lead or recruiting-tech owner)?
**What good looks like:** a small-but-real capability framework — the AI-assisted steps bounded, ≥1 quality invariant + ≥1 fallback, and bias/compliance invariants made explicit (this domain's "safety guarantees"), plus a named owner. Not "we'll adopt tools and see what sticks" (architecture-by-default, anti-pattern #2). Depth here is medium-to-light (see Notes), so this is a few capabilities under core invariants — *not* a full product-runtime governance body (forcing that here is anti-pattern #6).

## Strategy
**Answer:** {to fill} — the seed states no sequencing.
**Guiding questions:**
- Which capability do you invest in *first* — sourcing, screening, or scheduling? Which next?
- Validated how — which roles/req types do you pilot on, and what signal says the AI-assisted step is better (faster *and* not worse on fairness)?
- **Why this sequence** — what makes this the right order (start where volume is highest and risk is lowest? start where a human still decides, before anything candidate-facing)?
**What good looks like:** a sequence that references the capability framework explicitly — "we invest in {capability} first because the framework supports it under {invariant}" — with validation logic, not a wishlist of AI features. Strategy informs the Architecture; it does not override the bias/compliance invariants (anti-pattern #8).

## Tactics
**Answer:** {to fill} — the seed names no concrete deliverables.
**Guiding questions:**
- What are the specific deliverables — which ATS integration, which screening model live on which req, the recruiter-facing UI, the audit log?
- For which specific recruiters / req types / candidate segments does this run first?
- What's the smallest concrete thing a recruiter could use on a live req next sprint?
**What good looks like:** specific, owned deliverables that instantiate the chosen Strategy capabilities — concrete enough to assign.

---

## Notes
- **Scope:** detected function — the seed states "Function scope" and names a single function (People / recruiting) adopting AI, not a product shipped to external users or a company-wide direction. Honored as given.
- **Composition depth:** medium-to-light — function-scope AI adoption with a handful of AI-assisted recruiting steps under bias/compliance invariants. Bring a moderate capability framework (a few capabilities, explicit interfaces, core + compliance invariants, a named owner) handled in existing People-ops rhythms — **not** a dedicated governance body. Leans *medium* if screening/ranking is genuinely model-driven and high-volume (compliance risk raises the rigor); leans *light* if it's mostly scheduling/drafting assists with a human deciding everything. The count and risk of AI-assisted decision steps picks the point on that range.
- **What the seed already gave us:**
  - Scope: function (People / recruiting) — stated.
  - Domain: recruiting, which lets the scaffold name the bias/compliance invariant class concretely.
  - Vision / Architecture / Strategy / Tactics content: (none) — all stubs left as guiding questions; the seed states an intent to adopt, not any of the four layers' content.
- **Commit-order reminder:** commit the function Vision (what recruiting becomes, for whom, why) before investing in the capability framework — pick the AI tools against a settled outcome, not the other way round, or you adopt tooling that doesn't serve a stance you never fixed.
