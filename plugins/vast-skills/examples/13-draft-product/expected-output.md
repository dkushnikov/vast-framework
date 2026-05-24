# VAST Draft — AI Meeting-Notes Summarizer for Sales (product scope)

> Fill top-down: commit Vision before investing in the layers below it. Each section gives the question to answer + what a good answer looks like. Stubs marked {to fill} are yours to author — where this scaffold left a question instead of an answer, that's deliberate: the seed didn't say, so the scaffold asks.

## Vision
**Answer:** {to fill} — the seed gives a fragment: the *enabled experience* is meeting-notes summarization, and the *for-whom* is sales teams. It states no **why** and pins no specific sales segment. Write the committed hypothesis; do not let it collapse into "summarize meetings" (that's the feature, not the Vision).
**Guiding questions:**
- What experience does this *enable* for a sales rep — what can they do after a call that they couldn't before? (e.g. never lose a commitment made on a call? walk into the next call already briefed? something else?)
- For whom, specifically — all sales teams, or a segment (SDRs vs AEs vs sales managers; SMB vs enterprise cycles)? The seed says "sales teams" broadly; narrow it.
- Why does this matter — what changes for them, and why is *summarization* the wedge rather than CRM hygiene, coaching, or forecasting?
**What good looks like:** a committed falsifiable hypothesis naming the enabled experience + the audience + why it matters — e.g. "we enable {sales segment} to {capability}, because {what they lose today}." Not a feature list (anti-pattern #1, Vision-as-Use-Case), not a slogan ("make sales more productive").
**Falsification triggers (required):** {to fill — name 2-5 conditions under which you'd revisit this Vision. Each must be **observable** (a real metric, not "reps seem happier"), **bounded** (a threshold + duration), and **owned** (a named role who monitors it). Do not skip this — a Vision with no triggers is anti-pattern #4. Shape, not a value: "{adoption/value metric} stays below {threshold} for {duration} — owner: {role}".}

## Architecture
**Answer:** {to fill} — the seed names no skills, interfaces, or invariants. Don't invent them; the questions below are the work here.
**Guiding questions (product → composition framework — answer all four sub-elements):**
- **Skill library** — what AI capabilities does this need? (a transcriber? a diarizer to split speakers? a summarizer? a commitment/action-item extractor? a CRM-field mapper?) List the atomic skills and what each is responsible for.
- **Interfaces** — how do the skills compose? (audio → transcript → speaker-labeled → summary + extracted items → CRM write?) What state does each hand to the next?
- **Invariants (substrate-portable — must always hold)** — what are the non-negotiables? (Does the bot announce itself / get consent before recording? Does anything write to the CRM without a human confirming? What's the fallback when transcription confidence is low? What must never happen with customer call data?) Name at least one quality contract and one fallback policy.
- **Implementations (substrate-coupled — will migrate)** — which model for transcription vs summarization, prompt strategy, retry/timeout values, output format. These you expect to swap as models improve; keep them out of the invariant set.
- **Who is the single accountable owner** for this Architecture (one named neck)?
**What good looks like:** a real composition framework, even if minimal — skill boundaries listed, interfaces named, ≥1 quality invariant (e.g. "every summary cites the transcript spans it came from") + ≥1 fallback invariant (e.g. "low-confidence sections are flagged, not silently dropped"), and a named owner. Not "we'll figure out the framework as we ship" (that's architecture-by-default, anti-pattern #2).

## Strategy
**Answer:** {to fill} — the seed states no sequencing.
**Guiding questions:**
- Which composition do you turn on *first* — transcription + live notes alone, before any CRM write? Which comes next, and what comes last?
- Validated with whom — which design-partner sales teams, and what signal tells you the summary is actually the one a rep would have written?
- **Why this sequence** — what makes this the right order (earn trust on read-only summaries before any write-back? dependency — search needs a corpus first)?
**What good looks like:** a sequence that references the Architecture explicitly — "we sequence {composition X} next because the framework supports skills {Y, Z}" — with validation logic (which segment, what confirms it), not an ad-hoc backlog. Strategy operates *within* the Architecture and informs it; it does not override invariants (anti-pattern #8).

## Tactics
**Answer:** {to fill} — the seed names no concrete deliverables.
**Guiding questions:**
- What are the specific outputs — the summary card layout, the action-item list, the CRM fields written, the "join call" entry point?
- For which specific users or moments — does an AE's summary differ from an SDR's? Does it personalize on the rep's past calls for tone or on the deal stage?
- What's the smallest concrete thing a design partner could use on a real call next week?
**What good looks like:** specific, dated or owned deliverables that instantiate the chosen Strategy compositions — concrete enough that an engineer could pick one up and build it.

---

## Notes
- **Scope:** detected product — the seed states "Product scope" outright and describes a product (an AI summarizer shipped to sales-team users), so scope is honored as given, not re-derived.
- **Composition depth:** deep (likely) — product scope with several plausibly-composed AI skills (transcribe / diarize / summarize / extract) operating over customer-call data, which carries consent + accuracy + human-in-loop invariants and a substrate the team will migrate. Bring a full composition framework when filling Architecture. "Likely" because the seed is one line — if it turns out to be a single wrapped summarization call with no real composition, this drops to medium; the count of composed skills under guarantees decides it.
- **What the seed already gave us:**
  - Vision: a fragment — enabled-experience (meeting-notes summarization) + a loose for-whom (sales teams). The *why* and the precise segment are left as questions.
  - Architecture / Strategy / Tactics: nothing — all stubs left as guiding questions.
- **Commit-order reminder:** commit the Vision (what experience, for which sales segment, why) before investing in the composition framework — an Architecture designed against an unsettled Vision is designed against a moving target, and the Strategy/Tactics below it sequence toward an unfixed goal.
