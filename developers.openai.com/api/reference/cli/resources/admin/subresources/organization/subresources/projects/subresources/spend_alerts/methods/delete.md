<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete/ -->

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

# Delete project spend alert

$ openai admin:organization:projects:spend-alerts delete

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Deletes a project spend alert.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to update.

--alert-id: string

The ID of the spend alert to delete.

##### ReturnsExpand Collapse

project\_spend\_alert\_deleted: object { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

### Delete project spend alert

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:spend-alerts delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --alert-id alert_id

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true
