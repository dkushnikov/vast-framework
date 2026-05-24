# Case Study 003 — Slack business-logic layer on agentic transport

**Status:** in progress. Case study narrative will be written after implementation completes.

<!-- Source material:
- Existing skill and protocol in internal project notes
- Transport layer: Atlas-Slack MCP plugin with dual-token routing, attribution middleware, PreToolUse hook
- Business-logic layer (in progress): channel registry, tone-per-channel rules, dispatch, notification cadence
-->

## Expected shape of the case study

1. **Context** — Slack interactions in a workplace have non-trivial sequencing dependencies: transport rules (token selection, attribution) must be defined before message semantics (what tone, which channel, which audience), which must be defined before the work of actually composing messages for specific people and purposes.
2. **Layers** —
   - Vision: AI partner as a collaborative presence in the workspace.
   - Architecture: dual-token transport, attribution middleware, hook-enforced discovery path, business-logic layer separation.
   - Strategy: which ways-of-working are covered (triage, weekly review, channel digest, discussions), channel-routing logic, VIP rules.
   - Tactics: per-person drafts, per-channel posts, reaction/pin/reminder workflows.
3. **Challenge flow in action** — transport-layer discovery failures (parallel session falling back to bash+curl) surfaced as signals through Tactics → escalated → Architecture updated (hook enforcement added).
4. **What VAST prevented** — designing business-logic rules (channel registry, tone matrix) before transport attribution coverage was correct would have produced messages with inconsistent attribution.
5. **Artifacts** — transport plugin commits, skill definitions, session logs.
6. **Lessons** — TBD.
