<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete/ -->

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

# Delete organization spend alert

admin.organization.spend\_alerts.delete(alert\_id) -> [OrganizationSpendAlertDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/spend\_alerts/{alert\_id}

Deletes an organization spend alert.

##### ParametersExpand Collapse

alert\_id: String

##### ReturnsExpand Collapse

class OrganizationSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: String

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: :"organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

### Delete organization spend alert

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

organization_spend_alert_deleted = openai.admin.organization.spend_alerts.delete("alert_id")

puts(organization_spend_alert_deleted)

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true
