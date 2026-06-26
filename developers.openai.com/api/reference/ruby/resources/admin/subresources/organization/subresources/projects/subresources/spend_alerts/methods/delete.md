<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Spend Alerts](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project spend alert

admin.organization.projects.spend\_alerts.delete(alert\_id, \*\*kwargs) -> [ProjectSpendAlertDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

Deletes a project spend alert.

##### ParametersExpand Collapse

project\_id: String

alert\_id: String

##### ReturnsExpand Collapse

class ProjectSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: String

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: :"project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

### Delete project spend alert

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

project_spend_alert_deleted = openai.admin.organization.projects.spend_alerts.delete("alert_id", project_id: "project_id")

puts(project_spend_alert_deleted)

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "project.spend_alert.deleted",
    "deleted": true
