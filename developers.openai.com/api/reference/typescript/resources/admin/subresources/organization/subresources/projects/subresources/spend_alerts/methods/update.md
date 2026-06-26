<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Spend Alerts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update project spend alert

client.admin.organization.projects.spendAlerts.update(stringalertID, SpendAlertUpdateParams { project\_id, currency, interval, 2 more } params, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Updates a project spend alert.

##### ParametersExpand Collapse

alertID: string

params: SpendAlertUpdateParams { project\_id, currency, interval, 2 more }

project\_id: string

Path param: The ID of the project to update.

currency: "USD"

Body param: The currency for the threshold amount.

interval: "month"

Body param: The time interval for evaluating spend against the threshold.

notification\_channel: [NotificationChannel](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20notification_channel%20%3E%20(schema))

Body param: Email notification settings for a spend alert.

recipients: Array<string>

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix?: string | null

Optional subject prefix for alert emails.

threshold\_amount: number

Body param: The alert threshold amount, in cents.

minimum0

##### ReturnsExpand Collapse

ProjectSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

interval: "month"

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: Array<string>

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix?: string | null

Optional subject prefix for alert emails.

object: "project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

### Update project spend alert

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const projectSpendAlert = await client.admin.organization.projects.spendAlerts.update('alert_id', {
  project_id: 'project_id',
  currency: 'USD',
  interval: 'month',
  notification_channel: { recipients: ['string'], type: 'email' },
  threshold_amount: 0,

console.log(projectSpendAlert.id);

    "id": "alert_abc123",
    "object": "project.spend_alert",
    "threshold_amount": 150000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert",
    "threshold_amount": 150000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"
