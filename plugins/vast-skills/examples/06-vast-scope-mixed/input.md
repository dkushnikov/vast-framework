# Inbox Assistant — VAST Doc

## Vision

We will become the default productivity platform for knowledge work, globally.
Our market stance is to win the category outright: every knowledge worker on the
planet should reach for our suite first. We exist to define the future of how work
gets done across the entire industry. This is our north star and it will not change.

## Architecture

The UI structure of the inbox screen:

- **Top bar:** logo on the left, search box in the center, settings gear on the right.
- **Left sidebar:** folder list (Inbox, Sent, Drafts, Archive), with unread counts.
- **Message list (center column):** sender, subject preview, timestamp; selected row
  highlights.
- **Reading pane (right column):** full message, with Reply / Reply-All / Forward
  buttons at the top and the AI draft panel docked at the bottom.
- **Compose modal:** opens centered, with To/Cc/Bcc, subject, body, and a Send button.

**Invariants:**
- Primary buttons are blue (#2563EB).
- The Send button is always bottom-right of the compose modal.
- The settings gear is always top-right.
- Font is Inter 14px for body, 16px for headings.

**Screens to build:** inbox list, reading pane, compose modal, settings page,
onboarding wizard (5 steps), billing page.

## Strategy

Roll out the inbox screen first, then settings, then billing. A/B test the blue
button against green.

## Tactics

Per-user theme preference (light/dark). Keyboard shortcuts for power users.
