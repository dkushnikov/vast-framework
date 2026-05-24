# Applications — VAST applied beyond product engineering

VAST applies to any system complex enough that implicit structure stops working. This document covers two types of applications: **cross-domain instantiations** (VAST applied to entirely different scopes) and **functional applications** (VAST applied to specific business functions).

## Cross-domain instantiations

VAST's sequencing principle (V→A→S→T) applies beyond product delivery. Each instantiation uses the same cascade with different vocabulary:

| Instantiation | Vision | Architecture | Strategy | Tactics |
|---|---|---|---|---|
| **Product** (original) | Product vision, experiences | Composition framework, skills, invariants | Which experiences to compose, sequencing | Specific compositions for specific users |
| **Company transformation** | Company vision, mission | Org capabilities + Values (constraints) + Domain structure | Strategic areas + Priorities | Goals + Projects |

Cross-domain applicability is one of VAST's distinctive claims — few sequencing frameworks use the same cascade vocabulary across product delivery and organizational design.

## Functional applications

Worked examples of how VAST applies to specific functions beyond product engineering. Each follows the same shape: Vision (what experiences this function enables), Architecture (composition framework — skills, invariants, implementations), Strategy (which compositions to sequence), Tactics (delivery patterns).

These examples are intentionally functional and AI-first. They show what the framework looks like for non-product leaders whose AI integration is increasingly load-bearing for the function's effectiveness. Vocabulary aliases ("capability framework" or "process framework" instead of "composition framework") are used where natural; the underlying shape is identical to product-engineering VAST.

## Customer Experience

**Vision (function-level).** "We enable our customers to resolve their support questions within 1 hour median, with the AI handling tier-1 issues at 70%+ self-service rate by end of next year, while preserving customer trust and willingness to recommend." Falsification triggers: tier-1 self-service rate fails to exceed 50% by Q3; customer satisfaction score on AI-handled tickets drops below 4.0/5.0 for two consecutive months.

**Architecture (CX capability framework).**
- *Skills:* ticket classifier (categorize by intent + urgency), routing engine, knowledge base retriever, response drafter (multiple voice options), escalation detector (when human needed), summarization (for context handoff to human agent), sentiment monitor.
- *Interfaces:* incoming ticket → classifier → (auto-respond | route to human | escalate). Human agent inherits AI-drafted response + summarized context. Sentiment monitor runs in parallel; spikes trigger escalation regardless of category.
- *Invariants:* response factual accuracy verifiable against knowledge base. Escalation latency under 5 minutes for high-severity. Customer-trust contract — never claim capability the system doesn't have. PII handling per regulatory requirements. Audit trail of every AI-customer interaction. Equal-treatment across customer tiers.
- *Implementations:* specific LLM (currently Claude for response drafting, smaller model for classification — migrates as cost/quality shifts), specific knowledge base retrieval system (vendor X), specific routing rules tuned to current ticket volume.

**Strategy.** Sequence: Q1 — deploy ticket classifier in shadow mode, validate accuracy. Q2 — enable auto-respond for narrow set of high-confidence categories. Q3 — expand auto-respond categories; deploy escalation detector. Q4 — full tier-1 coverage; introduce human-in-loop for edge cases.

**Tactics.** Daily ticket volume processed, escalation pattern monitoring, weekly category-by-category accuracy review, monthly customer satisfaction sampling.

**What this gets the function leader.** Explicit framework for thinking about AI-CX integration as composition system, not vendor selection. Invariants make the trust and compliance commitments first-class. Strategy sequencing is anchored against architectural capability (we can't auto-respond category X until classifier is validated for it). Tactics happen within composition framework, not against it.

## Marketing

**Vision (function-level).** "We enable the company to deliver personalized brand-coherent customer communication at every touchpoint, with AI generating 60%+ of variant content by end of next year, while maintaining brand consistency, factual accuracy, and regulatory compliance." Falsification triggers: AI-generated content cannibalizes brand differentiation (measured by brand affinity surveys); regulatory issue from AI-generated claim.

**Architecture (Marketing capability framework).**
- *Skills:* content variant generator (per channel: email, social, in-app, blog), audience segmenter, brand-voice enforcer (style/tone validation), claim verifier (factual accuracy against approved sources), attribution tracker, A/B test analyzer.
- *Interfaces:* segment definition → variant generation per channel → brand-voice validation → claim verification → publish → attribution tracking → analyzer feedback loop.
- *Invariants:* brand consistency (every output passes brand-voice validation, no exceptions). Factual accuracy (no AI claim shipped without verification against approved sources). Regulatory compliance (specific to ad regulations per geography). Attribution traceability (every published variant traceable to source content + segment). Customer-data privacy (segmentation respects consent and PII boundaries).
- *Implementations:* specific generation models (varies by channel — quality vs cost tradeoff), specific brand-voice validator (currently rule-based with LLM-judge fallback), specific attribution platform.

**Strategy.** Sequence: Q1 — deploy generator + validator for low-stakes channels (in-app notifications). Q2 — expand to email; deploy A/B at scale. Q3 — social and ad channels with stronger compliance gates. Q4 — full personalized content engine.

**Tactics.** Per-channel content velocity, brand-voice pass rate, A/B test win rate, weekly channel-by-channel performance review.

**What this gets the function leader.** Brand and compliance invariants are first-class — not afterthoughts surfacing during incidents. Strategy is sequenced by trust-building, not by vendor capability. The function explicitly owns its capability framework rather than letting AI vendors define it.

## People

**Vision (function-level).** "We enable the company to source and assess senior talent at 2× current rate while maintaining quality bar, with AI handling 80% of sourcing operations and 50% of initial screening by end of next year, with full bias-control compliance." Falsification triggers: time-to-hire for senior roles fails to halve; bias audits show statistically significant adverse impact across protected categories; candidate satisfaction with process drops below 4.0/5.0.

**Architecture (Talent Acquisition capability framework).**
- *Skills:* job description generator (role-specific from competency model), candidate matcher (against open roles), outreach drafter (personalized initial touch), screening question generator, interview-summary writer, scheduler, offer-package modeler.
- *Interfaces:* role intake → JD generation → matcher (sources candidates from internal + external) → outreach drafter → response triage → screener → human interview → summary → decision support.
- *Invariants:* bias controls — every AI step audited per protected category for adverse impact. EEOC/regional employment law compliance — no AI step makes adverse decision without human review. Candidate experience — every AI-touched candidate gets timely communication. Audit trail — every step in candidate journey logged with reasoning. Privacy — candidate data handled per applicable regulations (GDPR, CCPA, etc.).
- *Implementations:* specific LLMs for generation steps, specific bias-audit tooling (vendor or custom), specific ATS integration, specific candidate-experience tracking.

**Strategy.** Sequence: Q1 — JD generator + bias auditing process; deploy in shadow alongside existing process. Q2 — candidate matching at scale; expand sourcing capacity. Q3 — initial screening with human review; build compliance audit history. Q4 — selective automated screening for narrow categories where bias-control validated.

**Tactics.** Weekly sourcing volume, candidate response rates, screening throughput, monthly bias-audit reviews, quarterly compliance attestations.

**What this gets the function leader.** Compliance and bias invariants are framework-level, not afterthought. The function builds AI integration deliberately, not under vendor pressure. Audit trails are designed in, not retrofitted. Strategy sequencing respects regulatory readiness, not just technical capability.

## Finance

**Vision (function-level).** "We enable the company's finance operations to provide forward-looking decision support to executive team within 24 hours of any strategic question, with AI providing 70%+ of variance analysis and forecasting first-pass by end of next year, while maintaining audit trail and regulatory compliance." Falsification triggers: AI-assisted forecasts diverge from actual results by >20% beyond expected variance; auditor finds material gap in AI-assisted reporting traceability; CFO loses confidence in AI-supported recommendations.

**Architecture (Finance capability framework).**
- *Skills:* anomaly detector (transaction-level patterns), forecast generator (scenario modeling), narrative writer (variance explanations from numeric inputs), compliance checker (against accounting standards and internal policy), data-quality validator, dashboard composer.
- *Interfaces:* data warehouse → quality validator → anomaly detector flags issues → forecast generator runs scenarios → narrative writer produces explanation → compliance checker validates → dashboard composer presents → human review and decision.
- *Invariants:* audit traceability — every AI output traceable to source data + reasoning. Accounting-standard compliance (GAAP/IFRS as applicable) — no AI output bypasses standards. Data integrity — AI flags but does not modify source data. Materiality thresholds — AI escalates anything above defined materiality without auto-action. Regulatory compliance per jurisdiction.
- *Implementations:* specific models (often more conservative reasoning models for finance vs creative ones for marketing), specific data warehouse platform, specific reporting tools.

**Strategy.** Sequence: Q1 — anomaly detection in shadow; validate against historical incidents. Q2 — forecast generator for non-material areas; build trust. Q3 — variance narrative writer for executive reports; human review every output. Q4 — selective full-cycle automation for low-materiality routine analysis.

**Tactics.** Daily anomaly review, monthly forecast accuracy assessment, quarterly auditor briefing on AI-assisted process changes.

**What this gets the function leader.** Audit, compliance, and materiality invariants are framework-level — not exception-handling. Strategy sequenced by trust-building with auditors and executive team, not just by capability. CFO can answer "is our AI integration auditable?" with explicit reference to invariant set.

## Operations

**Vision (function-level).** "We enable the company to operate at scale with stable per-employee operational overhead, with AI handling 60%+ of routine operational tasks (procurement, vendor management, internal IT requests, facilities) by end of next year, while preserving service quality for internal stakeholders." Falsification triggers: per-employee operational overhead increases despite AI investment; internal stakeholder satisfaction drops; operational incident rate increases.

**Architecture (Operations process framework).**
- *Skills:* request classifier (procurement vs IT vs facilities vs other), policy checker (against approval matrices), document generator (POs, contracts, requests), vendor researcher, status tracker, escalation detector.
- *Interfaces:* request intake → classifier → policy check → automated handling (if within threshold) | human routing (if above threshold) → status tracking → completion + audit log.
- *Invariants:* approval-matrix compliance (no auto-action above defined thresholds). Audit trail for every operational decision. Vendor due-diligence requirements (security review, compliance check, financial stability before onboarding). Internal-stakeholder service-level commitments. Cost-control invariants (spending caps per category).
- *Implementations:* specific LLMs (cost-optimized for high-volume routine tasks), specific procurement system, specific approval-workflow tooling.

**Strategy.** Sequence: Q1 — request classifier + policy checker; route to humans with AI-drafted analysis. Q2 — automated handling for narrow categories within strict thresholds. Q3 — expand categories with proven track record. Q4 — selective full-cycle automation for routine high-volume requests.

**Tactics.** Daily request throughput, weekly policy-compliance audit, monthly stakeholder satisfaction tracking, quarterly cost-overhead review.

**What this gets the function leader.** Operations runs as composition framework — same shape as product, content native to ops. Invariants make compliance and stakeholder-trust commitments first-class. Strategy sequencing is anchored to risk thresholds. Tactics happen within explicit framework, not vendor-driven ad-hoc adoption.

## What these examples demonstrate

Same framework, five different domains. The pattern recurs:

1. **Vision is functional and falsifiable** — not generic ("we make customers happy") but specific and measurable, with named revision triggers.
2. **Architecture is the function's composition framework** — vocabulary varies (CX framework, Marketing framework, People framework), structure is identical (skills + interfaces + invariants + implementations).
3. **Invariants are domain-specific but always present** — for CX it's trust and accuracy; for Marketing brand and compliance; for People bias and EEOC; for Finance audit and accounting standards; for Ops policy and stakeholder-trust. Compliance / audit / fairness invariants are first-class, not engineering-only.
4. **Implementations are vendor-specific and migrate** — current LLM choices, current SaaS tools, current automation platforms. These change without changing the framework.
5. **Strategy is sequenced by trust-and-validation, not vendor capability** — every function moves AI deeper as trust builds with stakeholders (customers, candidates, auditors, internal users).
6. **Tactics happen within the framework, not against it** — per-instance delivery is high-frequency iteration; the framework constrains and enables it.

These examples are not exhaustive — every function with meaningful AI integration can be VAST-applied in the same way. What matters is the recurring structural pattern, not the specific domain choices.

## How to use this document

For function leaders considering whether VAST applies to their function: read the example closest to your domain. If the shape resonates and the invariants list seems tractable, VAST applies. Adapt the specifics; preserve the structural commitments (Vision named with triggers; Architecture explicit; Strategy sequenced by trust; Tactics within framework).

For executives building broader AI transformation: these examples show what each function's individual VAST application would look like. Cross-function shared substrate (shared LLM contracts, shared data infrastructure, shared compliance baselines) lives at the company-platform level, with function-level VAST building on top.

## References

- [`vast.md`](./vast.md) — core framework definition
- [`architecture-levels.md`](./architecture-levels.md) — Architecture at product / org-design / WoW levels (the structural recurrence these examples illustrate)
- [`applicability.md`](./applicability.md) — composition depth and minimum viable depth (applies per function)
- [`governance.md`](./governance.md) — accountability pattern at three levels (function applications use level-3 governance)
