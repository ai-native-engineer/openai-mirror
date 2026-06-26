<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Spend Alerts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project spend alert

$ openai admin:organization:projects:spend-alerts retrieve

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Retrieves a project spend alert.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--alert-id: string

The ID of the spend alert to retrieve.

##### ReturnsExpand Collapse

project\_spend\_alert: object { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

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

object: "project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

### Retrieve project spend alert

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:spend-alerts retrieve \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --alert-id alert_id

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
