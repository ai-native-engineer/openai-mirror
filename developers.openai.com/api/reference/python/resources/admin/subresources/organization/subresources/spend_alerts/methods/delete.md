<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete/ -->

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

# Delete organization spend alert

admin.organization.spend\_alerts.delete(stralert\_id)  -> [OrganizationSpendAlertDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema))

DELETE/organization/spend\_alerts/{alert\_id}

Deletes an organization spend alert.

##### ParametersExpand Collapse

alert\_id: str

##### ReturnsExpand Collapse

class OrganizationSpendAlertDeleted: …

Confirmation payload returned after deleting an organization spend alert.

id: str

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: Literal["organization.spend\_alert.deleted"]

Always `organization.spend_alert.deleted`.

### Delete organization spend alert

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
organization_spend_alert_deleted = client.admin.organization.spend_alerts.delete(
    "alert_id",
print(organization_spend_alert_deleted.id)

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true
