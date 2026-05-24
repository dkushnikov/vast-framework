# VAST connection heuristics — detailed

For use by `vast-connect` SKILL.md. Detail behind the condensed checks table. One section per check, anchored to match the SKILL.md detail-refs.

This skill checks whether two VAST docs in a parent→child relationship form a genuine nesting (working Matryoshka) — not whether either doc is internally well-formed (that's `vast-validate`). Throughout, **parent** = the broader/outer doc, **child** = the narrower/inner doc. Establish that direction first (see step-down below); every other check reads against it.

The five checks run conditionally: scope step-down, Vision lineage, and invariant inheritance always run; cross-doc Challenge Flow runs only if cross-doc interactions are described; Strategy alignment runs only if both docs have a Strategy layer. Skipped checks produce no report lines.

## Determining parent-vs-child direction (prerequisite)

Before any check, establish which doc contains which. This is a *scope-containment* judgment, not a "which was written first" one.

1. **Detect each doc's scope** independently using the per-scope identifying signals in `../../../references/layer-definitions.md` (company / product / function / WoW). Compressed cues:
   - **Company:** "market stance", "why this company exists", "capability portfolio", "org design", "allocation to functions and bets", "CEO / leadership team".
   - **Product:** "composition framework", "skill library", "AI substrate / model / LLM", "invariants and implementations", "which experiences to compose next", "personalized instance delivery", "CPO / CTO / PM / EM".
   - **Function:** "VP {Marketing/CX/Ops}", "the function's capability set", "tools/processes/AI integrations of a single function", domain-native framings (ATS, forecasting tooling, CX routing).
   - **WoW:** "review meetings / decision artifacts / planning cycle / retrospective", "tool migration", "async-first / decisions-as-artifacts", "cadences / 1-1s / all-hands / RFC format".
   - **Component / sub-function (narrower than product):** a single subsystem, capability, or module that names a *parent* product/library it plugs into ("operates within the platform's …", "consumes the shared X skill", "our slice of the suite"). Recursion can go below the four named scopes — a component under a product is still "one level down".

2. **Order by containment.** The doc whose scope *contains* the other's is the parent. Company contains product; product contains component/function; function contains its sub-functions/WoW for that function. The containment chain (governance.md "Recursion", vast.md "Matryoshka") is: company ⊃ product ⊃ component, with function and WoW nesting where the org places them.

3. **Classify the relationship** for the `Relationship` report line:
   - **parent→child confirmed** — one doc is unambiguously broader and contains the other's scope.
   - **direction-unclear** — both docs read at the *same* scope (two product docs, two company docs); you can't tell which contains which from scope alone. Cross-doc references ("nested under", "our parent is") may break the tie — use them if present.
   - **not-nested** — neither contains the other: two sibling products under an (absent) common parent, or two docs about unrelated systems. Containment chain has no link between them.

When direction is **direction-unclear** or **not-nested**, the remaining checks still run, but you report honestly: scope step-down will Fail (no valid step exists), and the cascade checks (Vision lineage, invariant inheritance, Strategy alignment) note that the parent→child direction could not be confirmed, so "cascade" is being assessed against an assumed (not established) direction. Do not manufacture a clean Pass for a pair that isn't actually nested.

## Scope step-down {#scope-step-down}

A working Matryoshka steps **down exactly one recursion level** from parent to child. The child is narrower; it lives inside the parent's scope.

**Valid step-downs** (parent → child):
- company → product
- company → function
- product → component / sub-function / function-within-product
- function → sub-function / WoW-for-that-function

**Test:** is the child exactly one containment level below the parent, with no missing intermediate that would be needed to bridge them?

### Severity rule for scope step-down

- **Fail — same-or-broader child:** the child is at the *same* scope as the parent (product↔product, company↔company) or *broader* than the parent (child is company-scope, parent is product-scope). There is no step-down; this is not a parent→child nesting. Report both detected scopes. Fix: identify the true parent (the doc that actually contains the other), or re-pitch the child one level narrower.
- **Fail — skipped level with nothing bridging:** the parent is company-scope and the child is team/Tactics-execution-scope with no product or function in between, and the child does not reference an intermediate that bridges them. The recursion jumps two levels; the connection has a hole. Fix: introduce (or point to) the intermediate product/function VAST that the child should actually nest under.
- **Warn — ambiguous level:** the child has a single scope-ambiguous layer (e.g. an Architecture that could read as product or as function) while the rest place it clearly one level down. Flag the ambiguous layer; ask for clarification. Note the interaction: if the child *also* fails internal scope-homogeneity, that's a `vast-validate` finding — recommend running it, don't double-count here.
- **Pass:** the child is exactly one valid recursion level below the parent.

This check is the structural precondition for the cascade checks. If it Fails because the docs aren't actually nested (same-or-broader, or not-nested), say so plainly — the Vision/invariant/Strategy checks below are then assessing cascade against a direction that wasn't established.

## Vision lineage {#vision-lineage}

The child's Vision must be a **refinement or instance** of the parent — it enables an experience that *serves one of the parent's Strategy use-cases* or *advances one of the parent's Architecture domains*. It descends from the parent Vision; it does not float free of it, and it does not contradict it.

Recall the parent's layers map to the triad (`../../../references/vast-essentials.md`): parent Architecture = the domains/outcomes that matter; parent Strategy = the use-cases / where-to-invest. A legitimate child Vision plugs into one of those: "we enable {narrower experience}" where that experience is one of the things the parent said it was investing in or optimizing for.

**Test:** can you draw an explicit line from the child Vision to a named parent Strategy use-case or parent Architecture domain? "The parent invests in {X}; the child Vision *is* {X}, made concrete one level down."

### Severity rule for Vision lineage

- **Fail — unrelated:** the child Vision serves no parent Strategy use-case and advances no parent Architecture domain — it's a different product/initiative that happens to sit in the same repo or org. Evidence: quote the child Vision and the parent's Strategy/Architecture, show there's no shared thread. Fix: either re-anchor the child Vision to an actual parent use-case/domain, or acknowledge it's not a child of this parent (it nests elsewhere, or it's a sibling).
- **Fail — contradicting:** the child Vision pursues an outcome the parent Vision explicitly excludes or opposes (parent: "we serve solo operators, never enterprise"; child Vision: "we enable enterprise IT admins to centrally manage seats"). The child contradicts the parent's for-whom or why. Fix: reconcile — either the child Vision is wrong for this parent, or the parent Vision needs to widen (a Vision-level change, owned by the parent Vision role, not decided in the child doc).
- **Warn — plausible but unthreaded:** the child Vision is *plausibly* a refinement (same broad domain) but the doc draws no explicit line to a specific parent use-case or domain — the lineage is implied, not stated. Fix: name the parent Strategy use-case or Architecture domain the child Vision serves, so the descent is explicit rather than inferred by the reader.
- **Pass:** the child Vision explicitly refines/instantiates the parent — it serves a named parent use-case or advances a named parent domain, and contradicts nothing in the parent Vision.

## Invariant inheritance {#invariant-inheritance}

**The core Matryoshka condition.** The child's Architecture operates **within the parent's Architecture invariants**. Working Matryoshka requires the child to respect the validated top-level invariants; the test (vast.md "Matryoshka") is: *does the component commit to the top-level invariants?* If the child invents its own and overrides a parent invariant, the nesting is false — autonomy delegated without the framework that makes it safe.

**How to run it:**

1. **Enumerate the parent's composition invariants** — the substrate-portable rules in the parent's Architecture (`../../../references/vast-essentials.md` §3): skill boundaries, quality contracts, fallback policies, trust contracts, observability requirements, safety guarantees. (Function/company invariants: compliance, fairness controls, audit traceability, org-portable rules.) These are the constraints the child must live inside.
2. **For each child Architecture choice**, ask: does it *operate within* this set, or does it *break* one? A child may add its own *local* invariants (more restrictive is fine) and choose its own *implementations* (substrate-coupled — LLM, prompt strategy, retry values — these are expected to differ). What it may not do is **relax, remove, or contradict a parent invariant**.
3. **Distinguish invariant-violation from implementation-divergence.** A different prompt strategy or model choice in the child is *implementation* divergence — not a violation (implementations are substrate-coupled and expected to vary). A child that ships PII cross-tenant when the parent's safety guarantee forbids it, or sends on the user's behalf when the parent's trust contract says sending is always human, is an *invariant* violation. The split (`../../../references/vast-essentials.md` §3) is the discriminator: only the substrate-portable tier (invariants) triggers a Fail; the substrate-coupled tier (implementations) does not.

**Test:** point at each parent invariant; confirm no child Architecture choice relaxes, removes, or contradicts it.

### Detecting a violation (the concrete pattern)

The clearest violation has this shape: the parent states an invariant as an absolute ("all user data stays in-region", "no skill sends without human confirmation", "every decision carries an audit trail"), and the child Architecture makes a structural choice that breaks the absolute ("the child replicates user data to a cross-region cache for latency", "the child's auto-responder sends without confirmation", "the child's fast path skips the audit log"). The break is at the *invariant* tier (a portable guarantee), not the *implementation* tier (how the guarantee is met on this substrate). When you find one, quote the parent invariant and the child choice side by side.

### Severity rule for invariant inheritance

- **Fail:** a child Architecture choice **relaxes, removes, or contradicts** a parent invariant (a substrate-portable guarantee). This is false Matryoshka — the child does not commit to the top-level invariants. Evidence: the parent invariant verbatim + the child choice that breaks it. Fix: the child must operate within the invariant; if the invariant genuinely needs to change, that is a *parent* Architecture decision (the child *informs* the parent per Challenge Flow — see `#cross-doc-challenge-flow` — it does not override unilaterally).
- **Warn:** a child choice *strains* or under-specifies against a parent invariant without explicitly reconciling it — the child doesn't clearly break the invariant but doesn't show it honors it either (e.g. parent requires every composition be observable; child adds a new skill with no stated observability hook). Fix: state how the child choice honors the parent invariant, or flag it for the parent Architecture owner.
- **Pass:** every child Architecture choice operates within the parent invariants; the child may add local (more-restrictive) invariants and its own implementations, but breaks none of the parent's. The child commits to the top-level invariants — real Matryoshka.

## Cross-doc Challenge Flow {#cross-doc-challenge-flow}

**Runs only if the docs describe cross-doc interactions.** If neither doc describes how it interacts with the other, this check passes by default — note "no cross-doc interactions described."

Challenge Flow across a nesting boundary (vast.md / glossary.md "Challenge Flow", adapted to two docs): **the child informs the parent upward; the parent constrains the child downward.** The child surfaces signals — adoption friction, execution blockers, a composition pattern that breaks at component scale — as *feedback* up to the parent. The parent's Vision and Architecture *constrain* the child (the child's Vision descends from the parent's; the child's Architecture lives within the parent's invariants). This mirrors within-doc Challenge Flow (Strategy/Tactics inform up; Vision/Architecture constrain down), projected onto the parent/child axis.

**Test:** scan every described cross-doc interaction. Does the child *inform* (feed a signal up, for the parent to decide on) — or does it *dictate* (unilaterally change the parent)? Does the parent *constrain* via Vision/Architecture — or does the parent reach *past* its proper layers into the child's internals?

### Inversions to flag (Fail)

- **Child dictating to parent** — the child doc declares a change to the parent's Vision, Architecture, or invariants as a decision ("the platform will drop its in-region invariant to unblock us", "we've updated the company Vision to include our segment"). The child may *inform* ("this invariant is costing us adoption — here's the data, parent please reconsider"); it may not *decide* for the parent. This is anti-pattern #8 projected across docs (the lower scope overriding the higher instead of informing). Fix: reframe the child's statement as a signal/request to the parent Architecture/Vision owner; the parent decides.
- **Parent Tactics reaching into child Architecture** — the parent's *Tactics* layer (the parent's lowest, execution-level layer) prescribes the child's Architecture (its invariants, skill boundaries, interfaces). The parent constrains the child through its *Vision and Architecture* (the durable, higher layers), not through parent-level execution detail. A parent Tactics item dictating child internal structure is a layer/scope inversion. Fix: if the parent needs to constrain the child's structure, that belongs in the parent's Architecture (an invariant the child inherits), not in parent Tactics.

### Severity rule for cross-doc Challenge Flow

- **Fail:** an explicit inversion — child dictating a change to the parent, or parent Tactics reaching into child Architecture.
- **Warn:** ambiguous direction — a cross-doc interaction is described but it's unclear whether the child is informing or overriding (or whether the parent is constraining via Architecture or via Tactics). Fix: state explicitly that the child informs and the parent decides, and that the parent constrains via its Architecture invariants.
- **Pass (by default):** no cross-doc interactions described, OR all described interactions follow the rule (child informs up, parent constrains down via Vision/Architecture).

See `../../../references/anti-patterns.md` #8 for the within-doc bad/good fragment pair this projects across docs.

## Strategy alignment {#strategy-alignment}

**Runs only if both docs have a Strategy layer.** The child's Strategy (which experiences/capabilities to compose next, and how to invest) must **advance — or at least not contradict — the parent's Strategy/Architecture priorities.** The parent named where it invests (parent Strategy) and what domains matter (parent Architecture = Outcomes, `../../../references/vast-essentials.md` §2); the child's sequencing should pull in the same direction, applied one level down.

**Test:** does the child's investment direction move the parent's stated priorities forward, or does it spend the child's effort on something the parent de-prioritized or directed against?

### Severity rule for Strategy alignment

- **Fail — investing against the parent:** the child's Strategy directs effort *against* the parent's stated direction — the parent prioritized domain A and de-prioritized B; the child's Strategy goes all-in on B (or actively undercuts A). The child is pulling away from the parent. Evidence: parent priority + contradicting child sequencing. Fix: re-sequence the child to advance a parent priority, or surface to the parent (via Challenge Flow — child informs) that the parent's priority should change.
- **Warn — orthogonal/unjustified:** the child's Strategy is neither clearly advancing nor clearly contradicting the parent — it's orthogonal, or its sequencing is stated with no link to the parent priorities, so alignment can't be confirmed. Fix: tie the child's sequencing to the parent priority it serves.
- **Pass:** the child's Strategy advances a parent Strategy use-case or Architecture domain; the investment directions are coherent across the two docs.

## Source

Heuristics derived from:
- `vast.md` — "Matryoshka — recursive composition" (working vs false Matryoshka; "does the component commit to the top-level invariants?"), "Challenge flow", "What the composition framework actually owns — invariants vs implementations"
- `governance.md` — "Recursion" (the levels recurse; accountability re-maps per level), "Challenge flow"
- `glossary.md` — "Matryoshka", "Challenge Flow", "Composition invariants / implementations", "The triad"
- `layer-definitions.md` (shared ref) — the 4-scope model used to detect each doc's scope and confirm the step-down
- `vast-essentials.md` (shared ref) §3 — the invariants-vs-implementations split, the discriminator for invariant-violation vs implementation-divergence

(Framework-root paths relative to the repo root.) The shared-reference paths cited inline above (`../../../references/...`) are relative to *this file's* location at `skills/vast-connect/references/`.
