# OKR Audit Report — Q3 OKRs — Platform Team

**Scope detected:** team (Platform)
**OKRs reviewed:** 3 Objectives, 9 Key Results

## ✅ Pass
- Objective 3 ("Establish observability standard across services") — Objective is Outcome — domain identifiable (observability standardization).
- KR1.3 — KRs split cleanly — Output (measurable: 50% incident reduction); note: this is closer to the real Outcome that Objective 1 should express.
- KR3.1 — KRs split cleanly — Output (measurable: all services emit metrics by EOQ).
- KR3.2 — KRs split cleanly — Use Case (defining taxonomy + invariants = investment direction).

## ⚠️ Warn
- Objective 2 ("Improve developer productivity") — Objective is Outcome: borderline — "Improve" with no named metric or domain target at the objective line. Reframe: "Grow deploy frequency and reduce time-to-merge across product teams."
- KR2.1 — KRs split cleanly: Mixed — contains a Use Case ("validate new CI pipeline with two product teams") AND an Output ("shipping their next 5 features through it"). Split into two KRs.
- KR3.3 ("Onboard 5 new engineers") — Scope consistency: borderline — onboarding likely belongs to the People function, not a Platform observability objective. Verify scope.

## 🚨 Fail
- Objective 1 ("Ship the new authentication service") — Objective is Outcome: Output, not Outcome ("Ship X" = deliverable). Reframe to the underlying Outcome: "Reduce auth fragmentation across services" or "Establish a unified authentication capability."
- KR1.1 ("Launch SSO integration with Okta") — Objective is Outcome: compounding — an Output rolling up under an Output-shaped Objective; the whole of Objective 1 reads as a project plan, not an OKR.
- KR1.2 ("Migrate all production services to new auth") — same compounding issue as KR1.1.

## Summary
Objective 1 is a project disguised as an OKR — reframe to the underlying Outcome (e.g. "Reduce auth fragmentation"; KR1.3 already hints at it). Objective 2's framing is too vague. KR2.1 mixes Use Case + Output. Fix Objective 1 first — it is the load-bearing correction.
