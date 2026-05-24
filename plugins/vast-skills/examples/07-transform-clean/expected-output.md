# Proposed VAST — Support Copilot (product scope)

## Vision

We believe front-line support agents lose most of their day to information
retrieval — hunting across five systems before they can even start a reply —
when their time should go to judgment and empathy. We enable tier-1/tier-2
support agents to spend their attention on the customer, not the lookup, by
composing retrieval / summarization / drafting skills into a copilot that does
the hunting and proposes a grounded reply the agent edits and sends. The agent
stays in control: the copilot proposes, the human decides.

For whom: the front-line support team handling tier-1 and tier-2 tickets all
day — explicitly not engineers and not the success team.

## Architecture — composition framework

**Skill library** (what exists):
- `classify-ticket` — routes a ticket (billing / technical / account) so retrieval knows where to look first.
- `retrieve-context` — searches across the five sources (help center, past tickets, billing console, changelog, runbooks) and ranks passages by relevance.
- `summarize-thread` — condenses a long ticket thread to the actual question.
- `draft-reply` — writes a candidate reply grounded in retrieved passages, in the agent's tone.

**Composition interfaces** (how skills combine):
- Front-to-back flow: `classify-ticket` → `retrieve-context` (scoped by class) → `summarize-thread` → `draft-reply`, with the drafter consuming the retriever's ranked passages and the summarizer's condensed question as grounding context.

**Composition invariants** (substrate-portable — change rarely, deliberately):
- Skill boundary: `draft-reply` never sends; sending is always the agent clicking the button.
- Quality contract: every draft cites the sources it pulled from — no ungrounded answers.
- Fallback policy: if `retrieve-context` returns nothing confident, the copilot says "no good context found" and steps back rather than hallucinating a reply.
- Safety guarantee: no customer data leaves the tenant to train anything.

**Composition implementations** (substrate-coupled — migrate as the model evolves):
- Current substrate: a frontier LLM for `draft-reply` and `summarize-thread`; a small cheap classifier model for `classify-ticket`; embeddings over a vector store for `retrieve-context`.
- Output format: JSON via the model's structured-output mode.
- Retry: 2 attempts at 8s timeout. All of the above explicitly flagged as swappable as better/cheaper options appear.

## Strategy

Within the framework above, the sequencing of which compositions to turn on next:
1. Ship the `classify-ticket` + `retrieve-context` composition alone (no drafting), in front of ten volunteer agents — validate that the surfaced context matches what they'd have hunted for.
2. Turn on `draft-reply` only once retrieval is trusted; validate tone-match with the same ten agents before opening to the floor.
3. Defer action-extraction (auto-creating follow-up tasks) — additive, not part of the core loop.

Investment rationale: front-load the read-side skills (classify/retrieve/summarize) because they earn trust without the risk of a bad outgoing reply; gate the write-side skill behind demonstrated trust.

## Tactics

Personalized instance delivery for specific agents:
- A billing-heavy agent gets `classify-ticket`/`retrieve-context` tuned to hit the billing console first.
- A technical agent's `draft-reply` primes on their last 20 replies for tone match.
- Per-agent threshold tunes how aggressively the copilot auto-collapses low-relevance context vs. shows everything.

---

## Notes
- **Vision status:** extracted — the prose states the why ("time should go to judgment and empathy, not retrieval"), the for-whom (tier-1/2 front-line agents, explicitly not eng/success), and the enabled experience (copilot does the hunting, agent stays in control).
- **Composition depth:** deep — product scope with four composed AI skills under safety/quality invariants and a substrate the team explicitly plans to migrate; the invariants-vs-implementations split is real here.
- **Gaps surfaced:**
  - Vision has no falsification triggers — needs 2-5 observable + bounded + owned revision conditions (e.g. "draft acceptance rate fails to exceed X% by date — owner: …").
  - No accountable owner named for any layer — VAST needs one named neck per layer (Vision / Architecture / Strategy / Tactics).
- **Open questions:**
  - What are the falsification thresholds and who owns each? (the prose names a validation cohort but no revision triggers)
- **Decisions deferred:**
  - Action-extraction (auto follow-up tasks) — explicitly punted by the author as a nice-to-have outside the core loop.
