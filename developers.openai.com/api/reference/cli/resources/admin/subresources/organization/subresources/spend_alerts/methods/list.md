<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/list/ -->

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

# List organization spend alerts

$ openai admin:organization:spend-alerts list

GET/organization/spend\_alerts

Lists organization spend alerts.

##### ParametersExpand Collapse

--after: optional string

Cursor for pagination. Provide the ID of the last spend alert from the previous response to fetch the next page.

--before: optional string

Cursor for pagination. Provide the ID of the first spend alert from the previous response to fetch the previous page.

--limit: optional number

A limit on the number of spend alerts to return. Defaults to 20.

--order: optional "asc" or "desc"

Sort order for the returned spend alerts.

##### ReturnsExpand Collapse

OrganizationSpendAlertListResource: object { data, first\_id, has\_more, 2 more }

Paginated list of organization spend alerts.

data: array of [OrganizationSpendAlert](/api/reference/cli/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

Spend alerts returned in the current page.

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

first\_id: string

The ID of the first spend alert in this page.

has\_more: boolean

Whether more spend alerts are available when paginating.

last\_id: string

The ID of the last spend alert in this page.

object: "list"

Always `list`.

### List organization spend alerts

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:spend-alerts list \
  --admin-api-key 'My Admin API Key'

    "object": "list",
    "data": [
            "id": "alert_abc123",
            "object": "organization.spend_alert",
            "threshold_amount": 100000,
            "currency": "USD",
            "interval": "month",
            "notification_channel": {
                "type": "email",
                "recipients": ["finance@example.com"],
                "subject_prefix": "OpenAI spend alert"
    ],
    "first_id": "alert_abc123",
    "last_id": "alert_abc123",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "id": "alert_abc123",
            "object": "organization.spend_alert",
            "threshold_amount": 100000,
            "currency": "USD",
            "interval": "month",
            "notification_channel": {
                "type": "email",
                "recipients": ["finance@example.com"],
                "subject_prefix": "OpenAI spend alert"
    ],
    "first_id": "alert_abc123",
    "last_id": "alert_abc123",
    "has_more": false
