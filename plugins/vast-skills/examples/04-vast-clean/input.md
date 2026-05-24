# Inbox Assistant — VAST Doc

## Vision

We believe solo operators and small teams lose hours every day to inbox triage —
reading, sorting, and drafting replies to mail that mostly follows predictable
patterns. We enable them to clear a day's mail in minutes by composing
draft / summarize / classify skills into a single triage flow, so the inbox stops
being a job and becomes a quick daily pass.

For whom: solo operators, founders, and teams under 10 who run their business out
of their inbox and have no support staff to delegate triage to.

**Falsification triggers** (revisit the Vision if any fires):
1. Median triage time fails to drop below 10 min/day for 4 consecutive weeks
   post-launch — owner: Head of Growth.
2. AI-draft acceptance rate fails to exceed 40% by end of Q3 — owner: PM, Inbox.
3. Weekly retention of activated users drops below 35% for 4 consecutive weeks —
   owner: Head of Growth.

On trigger fire: trigger owner reports to Vision owner within 1 week → Vision
review session within 2 weeks → documented confirm / revise / extend.

## Architecture — composition framework

**Skill library** (what exists):
- `summarize-thread` — condenses a mail thread to its decision/ask.
- `draft-reply` — generates a candidate reply in the user's voice.
- `classify-message` — tags a message (action / FYI / spam / waiting-on).
- `extract-action` — pulls an explicit to-do out of a thread.

**Composition interfaces** (how skills combine):
- Triage flow orchestrates classify → (summarize | draft) per message; handoff is
  a typed `Message` envelope with thread context attached.
- `draft-reply` consumes `summarize-thread` output as context; state shared via the
  thread envelope, not re-fetched.
- Error propagation: any skill returning low-confidence emits a `needs-human` flag
  that the flow surfaces rather than swallows.

**Composition invariants** (substrate-portable — change rarely, deliberately):
- Skill boundaries: `draft-reply` never sends; it only proposes. Sending is always
  a human action.
- Quality contract: every `draft-reply` output carries a confidence score and the
  source thread it was grounded in (no ungrounded drafts).
- Fallback policy: on low confidence or skill failure, the flow degrades to
  "summarize only" and flags for human — never a silent skip.
- Trust contract: no skill reads mail outside the explicitly connected account;
  no skill writes or sends without explicit user confirmation.
- Safety guarantee: no message content leaves the user's tenant for training.

**Composition implementations** (substrate-coupled — migrate as the model evolves):
- Current substrate: a frontier LLM for draft/summarize; a small classifier model
  for `classify-message`.
- Drafting uses a few-shot voice-priming prompt; will migrate to fine-tune if the
  voice match plateaus.
- Retry: 2 attempts at 8s timeout on the draft call, tuned to current latency.
- Output format: structured JSON via the model's structured-output API.

## Strategy

Within the framework above, the sequencing of which experiences to compose next:
1. Ship the classify → summarize composition first (lowest risk, immediate value),
   validate with a design-partner cohort of 20 solo operators.
2. Add `draft-reply` once summarize acceptance is steady, validate voice match with
   the same cohort before broadening.
3. Defer `extract-action` until the triage flow's core loop holds — it's additive,
   not load-bearing.

Investment rationale: front-load the read-side skills (classify/summarize) because
they earn trust without the risk of a bad outgoing draft; gate the write-side skill
behind demonstrated trust.

## Tactics

Personalized instance delivery for specific users:
- For a user with a high-volume newsletter inbox, the morning pass leads with
  classify (bulk-FYI collapse) before surfacing the 3 action threads.
- For a founder doing investor outreach, `draft-reply` primes on their last 20 sent
  replies to that thread type for voice match.
- Per-user confidence threshold tunes how aggressively the flow auto-collapses FYI
  mail vs. surfaces it.
