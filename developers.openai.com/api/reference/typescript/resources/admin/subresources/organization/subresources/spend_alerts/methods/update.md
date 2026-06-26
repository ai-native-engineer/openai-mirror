<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization spend alert

client.admin.organization.spendAlerts.update(stringalertID, SpendAlertUpdateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts/{alert\_id}

Updates an organization spend alert.

##### ParametersExpand Collapse

alertID: string

body: SpendAlertUpdateParams { currency, interval, notification\_channel, threshold\_amount }

currency: "USD"

The currency for the threshold amount.

interval: "month"

The time interval for evaluating spend against the threshold.

notification\_channel: [NotificationChannel](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/update#(resource)%20admin.organization.spend_alerts%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20notification_channel%20%3E%20(schema))

Email notification settings for a spend alert.

recipients: Array<string>

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix?: string | null

Optional subject prefix for alert emails.

threshold\_amount: number

The alert threshold amount, in cents.

minimum0

##### ReturnsExpand Collapse

OrganizationSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

### Update organization spend alert

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

const organizationSpendAlert = await client.admin.organization.spendAlerts.update('alert_id', {
  currency: 'USD',
  interval: 'month',
  notification_channel: { recipients: ['string'], type: 'email' },
  threshold_amount: 0,

console.log(organizationSpendAlert.id);

    "id": "alert_abc123",
    "object": "organization.spend_alert",
    "threshold_amount": 150000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert",
    "threshold_amount": 150000,
    "currency": "USD",
    "interval": "month",
    "notification_channel": {
        "type": "email",
        "recipients": ["finance@example.com"],
        "subject_prefix": "OpenAI spend alert"
