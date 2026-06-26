<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List organization spend alerts

admin.organization.spend\_alerts.list(\*\*kwargs) -> ConversationCursorPage<[OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/spend\_alerts

Lists organization spend alerts.

##### ParametersExpand Collapse

after: String

Cursor for pagination. Provide the ID of the last spend alert from the previous response to fetch the next page.

before: String

Cursor for pagination. Provide the ID of the first spend alert from the previous response to fetch the previous page.

limit: Integer

A limit on the number of spend alerts to return. Defaults to 20.

minimum0

maximum100

order: :asc | :desc

Sort order for the returned spend alerts.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class OrganizationSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints.

currency: :USD

The currency for the threshold amount.

interval: :month

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel{ recipients, type, subject\_prefix}

Email notification settings for a spend alert.

recipients: Array[String]

Email addresses that receive the spend alert notification.

type: :email

The notification channel type. Currently only `email` is supported.

subject\_prefix: String

Optional subject prefix for alert emails.

object: :"organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: Integer

The alert threshold amount, in cents.

### List organization spend alerts

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.spend_alerts.list

puts(page)

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
