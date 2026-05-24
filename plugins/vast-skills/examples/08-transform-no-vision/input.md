# Q3 build list — Analytics Module

Scope of work for the new analytics module. This is the full set of things
we're shipping this quarter.

## Components to build

- **Dashboard builder** — drag-and-drop canvas where users assemble charts from
  a widget palette. Bar, line, pie, table, single-stat widgets in v1.
- **Query engine** — translates the dashboard's widget config into SQL against
  the warehouse, runs it, caches results for 15 minutes.
- **Connector framework** — adapters for Postgres, BigQuery, Snowflake, and a
  generic REST source. Each connector handles auth, schema introspection, and
  pagination.
- **Scheduler** — lets users set a dashboard to refresh on a cron and email a
  PNG snapshot to a recipient list.
- **Embed SDK** — a JS widget so customers can drop a dashboard into their own
  app with an API key.
- **Permissions layer** — row-level and column-level access rules per dashboard,
  inherited from workspace roles.

## Engineering tasks

- Build the widget rendering pipeline (canvas → spec → chart lib).
- Stand up the query cache (Redis, 15-min TTL).
- Write the four warehouse connectors + the REST adapter.
- Wire the cron scheduler to the email service.
- Ship the embed SDK to npm with versioned releases.
- Add the permissions checks to the query engine.

## Sequencing

We'll build the dashboard builder and query engine first since everything
depends on them, then the connectors, then scheduler and embed SDK in parallel,
then layer permissions on last. The REST connector can slip to Q4 if we're
tight — the three warehouse connectors are the priority.

## Non-functional

- Every query must enforce the permissions layer — no dashboard returns a row
  the viewer isn't allowed to see.
- Cached results expire at 15 minutes; no stale data past that.
- Connectors must never store warehouse credentials in plaintext.
