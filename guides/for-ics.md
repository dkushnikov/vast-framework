# VAST for Individual Contributors

## Does this affect your work?

Probably not day-to-day. VAST is mostly about how leaders sequence decisions. But it affects you in three ways:

**1. Fewer surprise rewrites.** When Architecture is explicit, product commitments don't accidentally assume capabilities that don't exist. You're less likely to build something that gets thrown away because "we decided to change the approach."

**2. Clearer escalation.** "This is a Tactics problem" (your lead can decide) vs "this is an Architecture gap" (needs someone higher up). Naming the level gets you faster answers.

**3. Your input matters at Architecture level.** You see implementation reality that leaders don't. "This API can't support that use case" is an Architecture signal. VAST gives that signal a name and a path upward.

## What you don't need to do

- Learn the framework in detail
- Change how you write code / design / analyze data
- Attend new meetings
- Use VAST vocabulary in your PRs

## What an Architecture document looks like

You might wonder: "what does Architecture actually produce?" Here's what you'd see:

```
Architecture: Messaging Platform (example)
├── Domains: Channels, Automation, AI, Analytics, Billing
├── Constraints: "No message sent without attribution trail"
│                "AI responses reviewed before auto-send to >1K audience"
│                "Channel-specific rate limits honored, never bypassed"
├── Interfaces: Automation → AI (intent handoff), AI → Analytics (event stream)
└── Implementations: Claude for drafting (swappable), Redis for queuing (swappable)
```

Invariants (constraints) persist across tech changes. Implementations migrate. When someone says "we're switching to a new model" — your constraints stay, your integration patterns change.

## When to care

- When your work gets thrown away → ask "was this an Architecture change?"
- When requirements feel contradictory → they might span two Architecture domains
- When you know something won't work → that's an Architecture signal, escalate it

## Next

- Quick overview → [quick-start.md](../quick-start.md)
- Full framework (if curious) → [vast.md](../vast.md)
