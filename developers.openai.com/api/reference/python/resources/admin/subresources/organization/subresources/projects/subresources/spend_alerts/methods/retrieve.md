<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Spend Alerts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project spend alert

admin.organization.projects.spend\_alerts.retrieve(stralert\_id, SpendAlertRetrieveParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Retrieves a project spend alert.

##### ParametersExpand Collapse

project\_id: str

alert\_id: str

##### ReturnsExpand Collapse

class ProjectSpendAlert: …

Represents a spend alert configured at the project level.

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

object: Literal["project.spend\_alert"]

The object type, which is always `project.spend_alert`.

threshold\_amount: int

The alert threshold amount, in cents.

### Retrieve project spend alert

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
project_spend_alert = client.admin.organization.projects.spend_alerts.retrieve(
    alert_id="alert_id",
    project_id="project_id",
print(project_spend_alert.id)

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
