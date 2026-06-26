<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List organization spend alerts

admin.organization.spend\_alerts.list(SpendAlertListParams\*\*kwargs)  -> SyncConversationCursorPage[[OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))]

GET/organization/spend\_alerts

Lists organization spend alerts.

##### ParametersExpand Collapse

after: Optional[str]

Cursor for pagination. Provide the ID of the last spend alert from the previous response to fetch the next page.

before: Optional[str]

Cursor for pagination. Provide the ID of the first spend alert from the previous response to fetch the previous page.

limit: Optional[int]

A limit on the number of spend alerts to return. Defaults to 20.

minimum0

maximum100

order: Optional[Literal["asc", "desc"]]

Sort order for the returned spend alerts.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

class OrganizationSpendAlert: …

Represents a spend alert configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints.

currency: Literal["USD"]

The currency for the threshold amount.

interval: Literal["month"]

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel

Email notification settings for a spend alert.

recipients: List[str]

Email addresses that receive the spend alert notification.

type: Literal["email"]

The notification channel type. Currently only `email` is supported.

subject\_prefix: Optional[str]

Optional subject prefix for alert emails.

object: Literal["organization.spend\_alert"]

The object type, which is always `organization.spend_alert`.

threshold\_amount: int

The alert threshold amount, in cents.

### List organization spend alerts

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
page = client.admin.organization.spend_alerts.list()
page = page.data[0]
print(page.id)

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
