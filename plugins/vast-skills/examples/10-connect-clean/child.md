# Inbox Assistant — Product VAST Doc

*(Child doc. Product scope. The Inbox product line nested under Northwind —
the company's "invest in Inbox first" Strategy use-case, made concrete.)*

## Vision

We enable Northwind's small operators to clear a day's mail in minutes instead of
hours, by composing draft / summarize / classify skills into one triage flow — so
the inbox stops being a job and becomes a quick daily pass. This is the operator's
wedge surface: the first place Northwind earns the right to act inside the
operator's daily tools.

For whom: the same independent operators and sub-ten-person teams Northwind serves,
at their highest-frequency surface (mail).

**Falsification triggers** (revisit the product Vision if any fires):
1. Median triage time fails to drop below 10 min/day for 4 consecutive weeks
   post-launch — owner: PM, Inbox.
2. AI-draft acceptance rate fails to exceed 40% by end of Q3 — owner: PM, Inbox.

On trigger fire: trigger owner reports to the product Vision owner within 1 week →
review within 2 weeks → documented confirm / revise / extend.

## Architecture — composition framework

**Skill library** (what exists at the product layer):
- `summarize-thread` — condenses a mail thread to its decision/ask.
- `draft-reply` — generates a candidate reply in the operator's voice.
- `classify-message` — tags a message (action / FYI / spam / waiting-on).

**Composition interfaces:**
- Triage flow orchestrates classify → (summarize | draft) per message; handoff is a
  typed `Message` envelope.
- **All three skills are built on Northwind's Shared AI platform** — model access,
  retrieval, identity, and billing are consumed from the platform, not
  re-implemented here (honors the parent's *composition-over-rebuild* invariant).

**Composition invariants** (local to the product — and all operating *within* the
parent's org invariants):
- **Drafting never sends.** `draft-reply` only proposes; sending is always an
  explicit operator action (operates within the parent's *no-send-without-human*).
- **Processing stays in-region.** Triage runs entirely within the tenant's home
  region; no thread content is replicated or cached out-of-region (operates within
  the parent's *data-residency*).
- **No content leaves the tenant.** No thread is read outside the connected account;
  nothing leaves the tenant for training (operates within the parent's
  *tenant-isolation*).
- Quality contract (local, more-restrictive): every `draft-reply` carries a
  confidence score and the source thread it was grounded in.
- Fallback (local): on low confidence, degrade to "summarize only" and flag for the
  operator — never a silent skip.

**Composition implementations** (substrate-coupled — may differ from sibling
products, expected to migrate): few-shot voice-priming prompt for drafting; small
classifier model for `classify-message`; 2 retries at 8s timeout; structured-output
API for formatting. Accountable owner: PM (Vision), Eng lead (Architecture).

## Strategy

Within the framework above:
1. Ship classify → summarize first (read-side, lowest risk), validate with a cohort
   of 20 operators.
2. Add `draft-reply` once summarize acceptance is steady.

This advances Northwind's "invest in Inbox first" priority directly: prove the
operator will let AI act in their highest-frequency tool, read-side before
write-side.

## Tactics

Personalized instance delivery: for a newsletter-heavy operator the morning pass
leads with classify (bulk-FYI collapse); for a founder doing outreach, `draft-reply`
primes on their last 20 sent replies for voice match.

## How this nests under Northwind

The Inbox squad surfaces operator-adoption signal up to Northwind (the company
Strategy/Architecture owners) — e.g. if the *data-residency* invariant blocks a
latency optimization, the squad reports the cost with data and lets the Platform/
company Architecture owner decide. The squad does not change a company invariant on
its own.
