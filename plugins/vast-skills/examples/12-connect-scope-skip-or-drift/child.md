# Northstar IT Suite — Company VAST Doc

*(Presented as a child nested under Northwind. In fact it is pitched at the SAME
scope as the parent — another company-level doc — and its Vision contradicts the
parent's. This pair fails both scope step-down and Vision lineage.)*

## Vision

We will become the system of record for enterprise IT departments — the platform
through which a 5,000-seat company's IT org provisions, governs, and audits every
employee's software access. We win the enterprise: the larger and more regulated
the buyer, the better the fit. Central admin control, SSO, fleet-wide policy
enforcement, and procurement integration are the heart of the product. We exist to
be the enterprise IT department's command center.

For whom: enterprise IT administrators, CISOs, and procurement leaders at companies
of 1,000+ employees.

**Falsification triggers** (revisit the company Vision if any fires):
1. Average contract value falls below $250k for two consecutive quarters — owner: CEO.
2. Sub-1,000-employee accounts exceed 20% of new ARR — a signal we are drifting
   *down-market*, away from the enterprise — owner: CEO.

On trigger fire: trigger owner reports to the Vision owner within 1 week → review
within 2 weeks → documented confirm / revise / extend.

## Architecture — org & capability composition framework

**Capability portfolio** (company-scope product lines):
- **Access Governance** — provisioning, deprovisioning, SSO, policy enforcement
  across the enterprise's whole software fleet.
- **Audit & Compliance** — SOC2 / ISO evidence collection, access-review workflows.
- **Procurement** — vendor onboarding, contract and spend management.
- **Shared platform** — enterprise identity (SCIM/SAML), policy engine, audit log.

**Composition interfaces:** all product lines build on the Shared platform's
enterprise identity and policy engine; one admin console spans the fleet.

**Composition invariants** (org-portable):
- Every access change produces an immutable audit record.
- All policy is enforced centrally by IT admins; end users cannot override.
- Multi-region data placement is chosen per enterprise contract (data-residency is
  a negotiated SLA, not a fixed home region).
- Named accountability per VAST layer per product line.

**Composition implementations:** four product squads + a Platform squad; current
identity-provider integrations; current cloud regions.

## Strategy

Which capabilities to develop in what sequence:
1. Invest in Access Governance first — the wedge into the enterprise IT buyer.
2. Add Audit & Compliance to deepen the regulated-buyer moat.
3. Procurement last, once governance is entrenched.

Investment rationale: land the largest, most regulated IT departments first; depth
in central control before breadth.

## Tactics

Execution within each squad: the Access Governance squad runs enterprise rollouts;
the Platform squad ships the shared identity and policy engine.
