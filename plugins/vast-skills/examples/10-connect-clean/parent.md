# Northwind — Company VAST Doc

*(Parent doc. Company scope. The company that builds a suite of AI-first
knowledge-work products; the Inbox Assistant is one product nested under it.)*

## Vision

We believe small operators — founders, solo professionals, and teams under ten —
are underserved by knowledge-work software built for the enterprise: it assumes
support staff, admins, and IT they don't have. Northwind exists to give the small
operator the leverage of a back office they can't afford, by composing AI
capabilities into the daily tools they already live in (mail, calendar, docs).
We win by being the operator's default, not the enterprise's.

For whom: independent operators and sub-ten-person teams who run the whole
business themselves.

**Falsification triggers** (revisit the company Vision if any fires):
1. Net revenue retention among sub-ten-person accounts falls below 95% for two
   consecutive quarters — owner: CEO.
2. Enterprise (50+ seat) deals exceed 30% of new ARR for two consecutive quarters
   — a signal we are drifting up-market, away from the operator — owner: CEO.

On trigger fire: trigger owner reports to the Vision owner within 1 week → Vision
review session within 2 weeks → documented confirm / revise / extend.

## Architecture — org & capability composition framework

**Capability portfolio** (the "skills" at company scope — what product lines exist
and how they compose into the operator's day):
- **Inbox** — triage, draft, summarize the operator's mail.
- **Calendar** — scheduling and meeting prep.
- **Docs** — drafting and knowledge retrieval.
- **Shared AI platform** — the common skill substrate (model access, retrieval,
  identity, billing) every product line composes on.

**Composition interfaces** (how product lines compose):
- All product lines build on the Shared AI platform; none ships its own model
  access, identity, or billing — they consume the platform's.
- A single operator-identity and a single per-tenant data boundary span all
  product lines (one account, one data home).

**Composition invariants** (org-portable — every product line inherits these):
- **Data residency:** all customer data stays in the customer's home region. No
  product line replicates, caches, or processes customer data outside the region
  the customer was provisioned in.
- **No-send-without-human:** no product line takes an irreversible action on the
  operator's behalf (send mail, book externally, share a doc) without explicit
  human confirmation.
- **Tenant isolation:** no customer content crosses tenant boundaries, and no
  content leaves the tenant for model training.
- **Named accountability:** every product line has one named accountable owner per
  VAST layer before work starts.
- **Composition over rebuild:** product lines compose the Shared AI platform's
  skills; they do not re-implement platform capabilities locally.

**Composition implementations** (current org structure — migrates without
re-opening the invariants above): three product squads (Inbox, Calendar, Docs)
plus a Platform squad; current frontier-LLM vendor; current cloud regions
(us-east, eu-west); RACI cascade per squad.

## Strategy

Which capabilities to develop in what sequence, given the portfolio above:
1. **Invest in Inbox first** — it is the operator's highest-frequency surface and
   the wedge product; validate the operator's willingness to let AI act in their
   most-used tool here before extending the pattern.
2. Bring Calendar online once Inbox's draft/triage loop holds, reusing the same
   Shared-platform skills.
3. Defer Docs until the operator has two products in daily use (sequencing for
   retention, not breadth).

Investment rationale: depth in the wedge (Inbox) before breadth across the suite;
every product line must earn its place on the operator's daily path.

## Tactics

Execution within each squad: the Inbox squad runs its own delivery; the Platform
squad ships the shared model-access and retrieval skills the product squads consume.
