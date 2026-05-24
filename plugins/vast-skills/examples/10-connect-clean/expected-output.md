# VAST Connection Report — Northwind → Inbox Assistant

**Parent:** Northwind — Company VAST Doc (company)
**Child:** Inbox Assistant — Product VAST Doc (product)
**Relationship:** parent→child confirmed — company scope (capability portfolio, org composition, CEO-owned Vision) contains product scope (composition framework, skill library, LLM substrate, PM/Eng-lead roles).

## ✅ Pass
- Scope step-down — child is exactly one recursion level below the parent: company → product. Parent operates at company scope (product-line portfolio, Shared AI platform, org invariants, CEO); child at product scope (skill library, triage flow, substrate, PM/Eng-lead). Valid single step.
- Vision lineage — child Vision explicitly refines a named parent Strategy use-case: the parent's "invest in Inbox first … the wedge product" → the child Vision *is* that wedge ("enable Northwind's small operators to clear a day's mail in minutes … the operator's wedge surface"). Same for-whom (small operators), narrowed to the mail surface. No contradiction with the parent Vision.
- Invariant inheritance — every parent org invariant is honored by a child Architecture choice: *data-residency* → child "processing stays in-region, no out-of-region cache"; *no-send-without-human* → child "drafting never sends, sending is always an operator action"; *tenant-isolation* → child "no content leaves the tenant for training"; *composition-over-rebuild* → child "all three skills built on the Shared AI platform … not re-implemented here". The child adds local more-restrictive invariants (grounded-drafts, summarize-only fallback) and its own implementations (voice-priming prompt, classifier model) — both permitted; no parent invariant relaxed, removed, or contradicted. Real Matryoshka.
- Cross-doc Challenge Flow — child informs up, parent constrains down: the child's "How this nests" section has the squad *surface* a data-residency cost "with data and lets the … company Architecture owner decide … does not change a company invariant on its own" (child informs, doesn't dictate). The parent constrains via its Architecture invariants, not via parent Tactics. Direction correct both ways.
- Strategy alignment — child Strategy advances the parent priority: parent "invest in Inbox first … prove the operator will let AI act"; child sequences "read-side before write-side … advances Northwind's 'invest in Inbox first' priority directly." Investment directions coherent across docs.

## ⚠️ Warn
- (none)

## 🚨 Fail
- (none)

## Summary
Genuinely VAST-connected — a working Matryoshka. The product child steps down exactly one level from the company parent, its Vision instantiates the parent's wedge use-case, its Architecture operates within every parent invariant (in-region, no-send, tenant-isolation, compose-on-platform) while keeping its own implementations, and Challenge Flow runs the right direction (child informs, parent constrains). No fixes needed.
