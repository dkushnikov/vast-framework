# Inbox Assistant — Product VAST Doc

*(Child doc. Product scope. The Inbox product line nested under Northwind. This
variant cascades correctly on Vision, scope, and Strategy — but makes one
Architecture choice that breaks a parent invariant.)*

## Vision

We enable Northwind's small operators to clear a day's mail in minutes instead of
hours, by composing draft / summarize / classify skills into one triage flow — the
operator's wedge surface, the first place Northwind earns the right to act inside
the operator's daily tools.

For whom: the same independent operators and sub-ten-person teams Northwind serves,
at their highest-frequency surface (mail).

**Falsification triggers** (revisit the product Vision if any fires):
1. Median triage time fails to drop below 10 min/day for 4 consecutive weeks
   post-launch — owner: PM, Inbox.
2. AI-draft acceptance rate fails to exceed 40% by end of Q3 — owner: PM, Inbox.

On trigger fire: trigger owner reports to the product Vision owner within 1 week →
review within 2 weeks → documented confirm / revise / extend.

## Architecture — composition framework

**Skill library:**
- `summarize-thread` — condenses a mail thread to its decision/ask.
- `draft-reply` — generates a candidate reply in the operator's voice.
- `classify-message` — tags a message (action / FYI / spam / waiting-on).

**Composition interfaces:**
- Triage flow orchestrates classify → (summarize | draft) per message.
- Skills are built on Northwind's Shared AI platform (model access, retrieval,
  identity, billing consumed from the platform).

**Composition invariants** (local to the product):
- **Drafting never sends.** `draft-reply` only proposes; sending is an explicit
  operator action.
- **Global low-latency cache.** To keep the morning pass under 500ms for every
  operator regardless of where they signed up, the triage flow maintains a
  **cross-region read-replica cache of thread content** in our US and EU regions,
  and routes each request to the nearest replica. An operator provisioned in the
  EU is served (and their thread content is replicated to) the US replica whenever
  US latency is lower. This is a core part of how the product hits its speed bar.
- Quality contract: every `draft-reply` carries a confidence score and the source
  thread it was grounded in.
- Fallback: on low confidence, degrade to "summarize only" and flag for the operator.

**Composition implementations** (substrate-coupled): few-shot voice-priming prompt;
small classifier model for `classify-message`; 2 retries at 8s timeout;
structured-output API. Accountable owner: PM (Vision), Eng lead (Architecture).

## Strategy

Within the framework above:
1. Ship classify → summarize first (read-side, lowest risk), validate with a cohort
   of 20 operators.
2. Add `draft-reply` once summarize acceptance is steady.

This advances Northwind's "invest in Inbox first" priority: prove the operator will
let AI act in their highest-frequency tool, read-side before write-side.

## Tactics

Personalized instance delivery: for a newsletter-heavy operator the morning pass
leads with classify; for a founder doing outreach, `draft-reply` primes on their
last 20 sent replies for voice match.
