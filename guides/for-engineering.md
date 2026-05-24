# VAST for Engineering Leaders

## What this means for engineering

VAST gives engineering's architectural work a name and a seat at the table. If you've ever felt that "architecture decisions get made by default through product commitments" — VAST addresses exactly that.

## What changes

**Architecture ownership is explicit.** Engineering leadership (or whoever owns the composition framework) has named accountability for architectural decisions. No more "we built it this way because the product spec implied it."

**Invariants vs implementations split.** Your architecture has two tiers:
- **Invariants** — substrate-portable, persist across migrations (skill boundaries, quality contracts, safety guarantees)
- **Implementations** — substrate-coupled, migrate when tech changes (specific models, prompt strategies, orchestration patterns)

When a new foundation model drops, you migrate implementations. Invariants persist. This distinction makes tech transitions architectural maintenance, not existential crises.

**Clearer escalation.** "This is an implementation choice" (your call) vs "this is an invariant change" (Architecture-level decision, needs governance). Naming the level reduces ambiguity.

## What doesn't change

- How your teams ship code day-to-day
- Your existing engineering processes
- The fact that you own technical decisions

## What you get

- **Defensible pushback** against product committing to use cases that assume capabilities you don't have
- **Architecture decisions documented** with named owners and dates
- **Reduced rework** from implicit architectural drift

## Next

- Architecture at three levels → [architecture-levels.md](../architecture-levels.md)
- The invariants/implementations split → [vast.md → "What the composition framework actually owns"](../vast.md)
- Governance model → [governance.md](../governance.md)
