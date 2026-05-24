# Case Study 002 — Distributed Atlas

**Status:** placeholder. Full narrative to be drafted from internal project files (contact author for access).

<!-- Source material:
- ~/Obsidian/Atlas/Projects/Distributed Atlas/vast-draft.md
- ~/Obsidian/Atlas/Projects/Distributed Atlas/project.md
- Related session logs
-->

## To write

Structure per `case-studies/README.md`. Anticipated sections:

1. **Context** — multi-instance AI partner system (Claude-based). Personal infrastructure where substrate decisions (runtime, visibility model, perimeter, profiles) determine what the partner can do. Meta-application: VAST applied to a system that itself builds with VAST.
2. **Layers** — Vision ("one identity across contexts, bounded-context per vault"). Architecture (4 tiers, profiles, Tailscale, visibility model, 8 design decisions). Strategy (which instance runs what, how they connect). Tactics (per-instance configuration, deployment, monitoring).
3. **Challenge flow in action** — Architecture decisions (visibility model) challenged by privacy-layer requirements. Strategy informed by discovery signals (failure modes of cross-perimeter egress).
4. **What VAST prevented** — scope drift into "everywhere" without architecture defining perimeter and visibility. Premature Strategy moves (which channels, which integrations) before Architecture settled runtime substrate.
5. **Artifacts** — existing VAST draft is concrete evidence. Project file captures 8 resolved design decisions.
6. **Lessons** — VAST applied to personal infrastructure works the same way as VAST applied to company-scale product development. Matryoshka at component level (per-instance V→A→S→T) demonstrated early.
