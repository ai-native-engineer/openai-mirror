<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete/ -->

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

# Delete project spend alert

admin.organization.projects.spend\_alerts.delete(stralert\_id, SpendAlertDeleteParams\*\*kwargs)  -> [ProjectSpendAlertDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Deletes a project spend alert.

##### ParametersExpand Collapse

project\_id: str

alert\_id: str

##### ReturnsExpand Collapse

class ProjectSpendAlertDeleted: …

Confirmation payload returned after deleting a project spend alert.

id: str

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: Literal["project.spend\_alert.deleted"]

Always `project.spend_alert.deleted`.

### Delete project spend alert

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
project_spend_alert_deleted = client.admin.organization.projects.spend_alerts.delete(
    alert_id="alert_id",
    project_id="project_id",
print(project_spend_alert_deleted.id)

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true
