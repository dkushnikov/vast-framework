# Proposed VAST — Analytics Module (product scope)

## Vision

⚠️ CANDIDATE (confirm): The prose states no why and no for-whom — it is a build
list, not a Vision. Derived from the deliverables (a self-serve dashboard
builder, multi-warehouse connectors, an embed SDK, per-role permissions), the
implied purpose *might be*: "enable non-technical users in a workspace to build
and share governed analytics over their own data sources without writing SQL."
This is an inference from what gets built, not a commitment the author made —
confirm or replace it before any downstream use. In particular: **for whom** is
unstated (workspace end-users? the customers embedding via the SDK? both?), and
**why this matters / what changes for them** is entirely absent.

## Architecture — composition framework

Structural content the prose does provide, lifted to the framework:

**Building blocks** (what exists):
- `dashboard-builder` — drag-and-drop canvas assembling charts from a widget palette (bar / line / pie / table / single-stat).
- `query-engine` — translates widget config → SQL → warehouse, caches results.
- `connector-framework` — adapters (Postgres / BigQuery / Snowflake / generic REST), each handling auth, schema introspection, pagination.
- `scheduler` — cron-refresh + emailed PNG snapshot.
- `embed-sdk` — JS widget for dropping a dashboard into a customer app via API key.
- `permissions-layer` — row-/column-level access per dashboard, inherited from workspace roles.

**Interfaces** (how blocks combine): canvas → spec → chart lib (rendering pipeline); widget config → SQL → cache → result (query path); permissions checks wired *into* the query engine.

**Invariants** (lifted from the "Non-functional" section — these are genuine durable guarantees, not features):
- Every query enforces the permissions layer — no dashboard returns a row the viewer isn't allowed to see.
- Cached results expire at 15 minutes — no stale data past that.
- Connectors never store warehouse credentials in plaintext.

**Note on completeness:** this is a coherent *software* architecture, but it is not an AI composition framework — there is no skill library of AI capabilities, no model substrate, no invariants/implementations split (because there's little substrate to split). That is appropriate for the work (see depth below), not a defect.

## Strategy

Sequencing the prose states:
1. `dashboard-builder` + `query-engine` first (everything depends on them).
2. Then `connector-framework` (three warehouse connectors prioritized).
3. Then `scheduler` + `embed-sdk` in parallel.
4. Then `permissions-layer` layered on last.

Investment note: the prose gives an *ordering* and a dependency rationale ("everything depends on them") but no customer/segment-validation logic — there is no "validate with whom" anywhere, because there is no stated for-whom (see Vision).

## Tactics

Concrete deliverables / engineering tasks:
- Widget rendering pipeline (canvas → spec → chart lib); Redis query cache (15-min TTL); four warehouse connectors + REST adapter; cron scheduler wired to email; embed SDK published to npm with versioned releases; permissions checks added to the query engine.

---

## Notes
- **Vision status:** ABSENT (candidate offered — confirm before use) — the prose is purely a feature/deliverable/task list with no stated purpose, audience, or enabled experience; the Vision section holds a clearly-labeled inferred candidate, not a fabricated commitment.
- **Composition depth:** light — product scope, but conventional analytics software (dashboards, SQL generation, connectors) with negligible AI-substrate engagement; no composed AI skills under guarantees. Forcing deep composition ceremony here would be anti-pattern #6.
- **Gaps surfaced:**
  - No Vision — the prose jumps straight from intent-less scope to deliverables. The single most important gap; everything below is downstream of it.
  - No for-whom and no why — even granting the candidate, the audience and the value it serves are unstated.
  - No accountable owner named for any layer.
  - Strategy has a build-order but no investment/validation rationale (no segment to validate against, because no Vision).
  - (Vision falsification triggers not flagged as a separate gap yet — there is no committed Vision to attach them to; resolve the Vision first.)
- **Open questions:**
  - Confirm or replace the candidate Vision — what experience does this enable, and for whom (workspace end-users, embedding customers, or both)?
  - Once a Vision exists: what would falsify it, and who owns each trigger?
- **Decisions deferred:**
  - REST connector may slip to Q4 — explicitly punted by the author (the three warehouse connectors are the stated priority).
