<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update organization spend alert

$ openai admin:organization:spend-alerts update

POST/organization/spend\_alerts/{alert\_id}

Updates an organization spend alert.

##### ParametersExpand Collapse

--alert-id: string

The ID of the spend alert to update.

--currency: "USD"

The currency for the threshold amount.

--interval: "month"

The time interval for evaluating spend against the threshold.

--notification-channel: object { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

--threshold-amount: number

The alert threshold amount, in cents.

##### ReturnsExpand Collapse

organization\_spend\_alert: object { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

"USD"

interval: "month"

The time interval for evaluating spend against the threshold.

"month"

notification\_channel: object { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: array of string

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix: optional string

Optional subject prefix for alert emails.

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

### Update organization spend alert

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:spend-alerts update \
  --admin-api-key 'My Admin API Key' \
  --alert-id alert_id \
  --currency USD \
  --interval month \
  --notification-channel '{recipients: [string], type: email}' \
  --threshold-amount 0

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
