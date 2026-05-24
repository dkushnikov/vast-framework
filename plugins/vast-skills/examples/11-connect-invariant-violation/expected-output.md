# VAST Connection Report — Northwind → Inbox Assistant

**Parent:** Northwind — Company VAST Doc (company)
**Child:** Inbox Assistant — Product VAST Doc (product)
**Relationship:** parent→child confirmed — company scope (capability portfolio, org composition, CEO-owned Vision) contains product scope (composition framework, skill library, LLM substrate, PM/Eng-lead roles).

## ✅ Pass
- Scope step-down — child is exactly one recursion level below the parent: company → product. Valid single step.
- Vision lineage — child Vision refines the parent's named "invest in Inbox first … the wedge product" use-case ("the operator's wedge surface, the first place Northwind earns the right to act"); same for-whom, narrowed to mail. No contradiction.
- Cross-doc Challenge Flow — no cross-doc interactions described (the child states each layer's content but does not describe informing the parent or being constrained by it). Passes by default. (Note: the data-residency override below should have been *surfaced* to the company Architecture owner as a signal rather than decided in the child — see Summary — but since no interaction is described, the violation is caught under Invariant inheritance, not here.)
- Strategy alignment — child Strategy advances the parent priority: parent "invest in Inbox first … prove the operator will let AI act"; child "read-side before write-side … advances Northwind's 'invest in Inbox first' priority." Coherent.

## ⚠️ Warn
- (none)

## 🚨 Fail
- Invariant inheritance: the child Architecture **breaks the parent's data-residency invariant**. Parent (Architecture invariant): *"all customer data stays in the customer's home region. No product line replicates, caches, or processes customer data outside the region the customer was provisioned in."* Child (Architecture invariant "Global low-latency cache"): *"the triage flow maintains a cross-region read-replica cache of thread content in our US and EU regions … An operator provisioned in the EU is served (and their thread content is replicated to) the US replica whenever US latency is lower."* This relaxes an absolute parent guarantee — replicating tenant thread content out of the home region — so it is an **invariant-tier** violation, not mere implementation divergence (a different prompt or model would be fine; cross-region replication of customer data is not). This is false Matryoshka: the child does not commit to the top-level invariant. Fix: keep all processing and caching in the operator's home region (per-region replicas only, no cross-region routing); if the latency bar genuinely requires relaxing data-residency, the child must *inform* the company Architecture owner with the data and let them decide whether to change the invariant — the child cannot override it unilaterally.

## Summary
Not VAST-connected as written — false Matryoshka. The pair cascades correctly on scope, Vision, and Strategy, but the child's "global low-latency cache" replicates tenant thread content across regions, breaking the company's absolute data-residency invariant. One fix closes it: keep data in-region (per-region replicas, no cross-region routing), and if the speed bar truly needs the invariant relaxed, route that as a signal up to the company Architecture owner rather than overriding it in the product doc.
