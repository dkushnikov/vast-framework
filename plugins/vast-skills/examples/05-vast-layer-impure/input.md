# Inbox Assistant — VAST Doc (v0 draft)

## Vision

Ship an AI inbox assistant that drafts replies, summarizes threads, and auto-tags
messages by Q3. Then expand to calendar triage in Q4 and document drafting in Q1
next year. The assistant will support Gmail first, then Outlook, then IMAP. We'll
launch a free tier and a $12/mo Pro tier with unlimited drafts.

Roadmap:
- Q3: drafting, summarization, auto-tagging
- Q4: calendar integration, snooze, scheduled send
- Q1: document drafting, CRM sync

## Architecture

Project plan to deliver the above:

1. Stand up the auth/connect service for Gmail OAuth (eng: 2 weeks).
2. Build the message-fetch pipeline and sync loop (eng: 3 weeks).
3. Wire the drafting feature to the LLM and ship the compose UI (eng: 2 weeks).
4. Build the tagging UI and the summarize panel (eng: 2 weeks).
5. Migrate beta users onto the new pipeline (1 week).
6. Onboard 2 new backend engineers to own the sync service.
7. Set up the billing integration for the Pro tier.

Milestones:
- M1 (end of month 1): Gmail connect + fetch working.
- M2 (end of month 2): drafting + tagging shipped to beta.
- M3 (end of month 3): GA with billing.

## Strategy

Sequence the build: connect first, then fetch, then the three features in parallel,
then billing. Validate drafting quality with the beta cohort before GA.

## Tactics

- Per-user voice priming on recent sent mail for the drafting feature.
- Bulk-collapse of newsletter mail in the morning pass.
