<!-- source: https://learn.chatgpt.com/docs/enterprise/governance -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionAdministration

Governance for Codex activity spans interactive analytics, programmatic
reporting, related ChatGPT usage controls, and audit records. Choose the
surface that matches the question; analytics and compliance data serve
different purposes.

| If you need to | Start with |
| --- | --- |
| Understand adoption across ChatGPT | [Workspace analytics](/codex/enterprise/workspace-analytics) |
| Review Codex adoption and activity interactively | [Codex analytics](#analytics-dashboard) |
| Load aggregated Codex reporting into another system | [Analytics API](/codex/enterprise/analytics-api) |
| Export records for audit or investigation | [Compliance API](/codex/enterprise/compliance-api) |
| Review plan-dependent ChatGPT workspace credit controls | [ChatGPT usage limits and spend controls](/codex/enterprise/usage-limits) |

## Open the administration surfaces

* Open [Workspace analytics](https://chatgpt.com/admin/usage) for interactive
  workspace reporting. The [Workspace analytics guide](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  describes the current roles and views.
* Open the authenticated [Codex Analytics API reference](https://chatgpt.com/codex/cloud/settings/apireference)
  when you need scheduled, programmatic reporting.
* Open the authenticated [Admin API reference](https://chatgpt.com/admin/api-reference)
  and the [Compliance Platform guide](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)
  for audit and investigation integrations.

For example, use workspace analytics for a quick adoption check, the Analytics
API to load aggregated Codex reporting into a business intelligence system,
and the Compliance API to send auditable records to a SIEM or electronic
discovery workflow.

## Analytics dashboard

ChatGPT provides workspace-wide analytics for broad adoption and engagement.
Codex analytics focuses on Codex activity. Both are interactive reporting
surfaces, not raw audit logs.

Use [Workspace analytics](/codex/enterprise/workspace-analytics) to compare the
two experiences and find their current owner-maintained sources. You can also
open [Workspace analytics](https://chatgpt.com/admin/usage) directly. Don’t
build a durable reporting contract from dashboard labels or downloaded report
fields; those can change as the product evolves.

## Related ChatGPT usage controls

ChatGPT workspace usage controls are separate from analytics and don’t
configure feature entitlements. Depending on the plan, eligible Codex activity
can consume ChatGPT workspace credits, and exhausted limits can pause access to
eligible features. These controls don’t set a universal Codex limit or govern
Platform API billing.

See [ChatGPT usage limits and spend controls](/codex/enterprise/usage-limits)
for the durable boundary and current Help Center sources.

## Analytics API

Use the Analytics API for programmatic, aggregated Codex reporting. It’s
appropriate for data warehouses, business intelligence systems, and internal
reporting that shouldn’t depend on an interactive dashboard.

The authenticated API reference owns access requirements, routes, schemas,
fields, reporting windows, and pagination. See
[Analytics API](/codex/enterprise/analytics-api) for the conceptual integration
boundary and the canonical reference link.

## Compliance API

Use the Compliance API for security, legal, and governance workflows that need
auditable records. It’s not an adoption or productivity dashboard.

The authenticated API reference owns event coverage, schemas, permissions,
filters, retention, and request behavior. See
[Compliance API](/codex/enterprise/compliance-api) for the conceptual
integration boundary and the canonical reference link.

For rollout sequencing and verification across these surfaces, use the
[Admin rollout guide](/codex/enterprise/admin-setup).

## Related docs

* [Compliance API](/codex/enterprise/compliance-api)
