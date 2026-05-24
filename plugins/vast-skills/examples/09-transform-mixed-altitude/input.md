# Pitch — Meeting Notes AI

We're going to redefine how every company on earth runs meetings. Our ambition
is to become the default operating system for organizational knowledge — the
place where every decision, every commitment, every conversation lives and
becomes searchable, actionable, permanent. We want to win this category
outright across the entire market; in five years a meeting that isn't captured
by us should feel like a meeting that didn't happen. This is a company-defining
bet, not a feature.

The wedge product is an AI meeting-notes assistant. It joins your video call,
transcribes in real time, and at the end produces a structured summary: the
decisions made, the action items with owners, and the open questions. The user
can edit any of it before it's saved.

Concretely, here's what's in the first release:
- A "Join meeting" button on the dashboard that drops the bot into a Zoom or
  Google Meet call.
- A live transcript panel that streams text as people talk, with speaker labels.
- A summary card that appears when the meeting ends, with three sections —
  Decisions, Action Items, Open Questions — each editable inline.
- An "assign owner" dropdown on each action item that pulls from the workspace
  member list.
- A search box on the dashboard that does full-text search across all past
  meeting summaries and transcripts.

Behind it there are a handful of AI pieces: a transcription service, a
diarization step that splits speakers, a summarizer that produces the three
sections, and an action-item extractor that finds commitments and guesses the
owner from context. A couple of hard rules: the bot always announces itself when
it joins (no silent recording), and nothing is saved until the user confirms the
summary — the human edits before anything persists.

For sequencing we'll get transcription and the live panel working first, then
the summary card, then search last once there's a corpus to search. We'll trial
it with a few friendly startups before a wider launch.
