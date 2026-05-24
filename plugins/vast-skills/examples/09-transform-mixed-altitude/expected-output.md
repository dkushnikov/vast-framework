# Proposed VAST — Meeting Notes AI (product scope)

> Scope note: the prose mixes two altitudes — a **company-level** ambition
> ("become the default OS for organizational knowledge", "win the category
> outright", "company-defining bet") and a **product-level** wedge (an AI
> meeting-notes assistant with specific features). This transform is pitched at
> **product scope**, because that is where the concrete, mappable material lives
> (the deliverables, the AI pieces, the invariants). The company-level ambition
> is recorded as an open question, not folded into the product Vision — it
> belongs in a separate company-scope Vision. See Notes.

## Vision

We enable working teams to leave a meeting with its decisions, action items, and
open questions already captured and editable — so the meeting's output is
structured knowledge, not someone's scramble to remember what was agreed. The
assistant joins the call, transcribes live, and produces a structured summary
the user edits before anything is saved; the human stays in control of the
record.

For whom: teams that run their work through video meetings (the prose trials
with "friendly startups") — stated loosely; the precise wedge segment is not
pinned down (see Open questions).

*(The prose's literal "Vision" — becoming the default OS for organizational
knowledge, winning the category across the market — is **company-scope** ambition,
not a product Vision. It is not discarded; it is surfaced as an open question
about altitude below.)*

## Architecture — composition framework

**Skill library** (the AI pieces the prose names):
- `transcribe` — real-time transcription of the call audio.
- `diarize` — splits the transcript by speaker (speaker labels).
- `summarize` — produces the three-section summary (Decisions / Action Items / Open Questions).
- `extract-action-items` — finds commitments in the transcript and guesses the owner from context.

**Composition interfaces** (how they combine): audio → `transcribe` → `diarize` (speaker-labeled stream) → `summarize` + `extract-action-items` over the labeled transcript → summary card.

**Composition invariants** (lifted from the prose's "hard rules" — genuine durable guarantees):
- Safety / consent: the bot always announces itself when it joins — no silent recording.
- Human-in-the-loop: nothing persists until the user confirms the summary — the human edits before anything is saved.

**Note on completeness:** the prose names skills + interfaces + two invariants but **no implementations** (no model choices, no substrate detail) and no further quality/fallback contracts (e.g. what happens when transcription confidence is low, what `extract-action-items` does when it can't guess an owner). Thin but real — see Gaps.

## Strategy

Sequencing the prose states:
1. `transcribe` + the live transcript panel first.
2. Then `summarize` (the summary card).
3. Then search last, once there's a corpus to search.

Validation: trial with "a few friendly startups" before a wider launch. Rationale is dependency-driven (search needs a corpus) — light on investment logic but present.

## Tactics

Concrete deliverables in the first release:
- "Join meeting" button (drops the bot into Zoom / Google Meet).
- Live transcript panel streaming speaker-labeled text.
- Summary card (Decisions / Action Items / Open Questions), each section editable inline.
- "Assign owner" dropdown on each action item, sourced from the workspace member list.
- Full-text search box across past summaries and transcripts.

---

## Notes
- **Vision status:** partially inferred — a product-scope Vision (structured meeting output, human-in-control) is extractable from the wedge description, but the prose's *explicit* Vision is at a different altitude (company scope), and the product Vision's for-whom is only loosely stated. Treated as partially inferred, not cleanly extracted.
- **Composition depth:** deep — product scope with four composed AI skills (transcribe / diarize / summarize / extract) under consent and human-in-loop invariants; this genuinely warrants a real composition framework. (The work earns deep regardless of which altitude the *Vision* sits at — depth tracks the product's AI engagement.)
- **Gaps surfaced:**
  - Altitude conflict (company ambition vs product wedge) — the dominant gap; resolve before committing the doc (see Open questions).
  - Vision has no falsification triggers — needs 2-5 observable + bounded + owned conditions.
  - Product Vision's for-whom is vague ("friendly startups" is a trial group, not a committed wedge segment).
  - Architecture states no implementations and no fallback/quality contracts beyond the two invariants (e.g. low-confidence transcription handling, owner-guess failure).
  - No accountable owner named for any layer.
- **Open questions:**
  - **Which altitude is this doc?** The company-level ambition ("default OS for organizational knowledge", win the category) and the product wedge (meeting-notes assistant) are two different VAST docs. Recommend: a company-scope Vision/Architecture for the ambition, with this product treated as the first bet *within* that company Strategy. Confirm the split, or re-pitch everything to one scope.
  - Who is the committed wedge segment for the product (beyond the startup trial cohort)?
  - What would falsify the product Vision, and who owns each trigger?
- **Decisions deferred:**
  - (none) — the prose punts nothing explicitly; the open items above are unresolved, not deliberately deferred.
