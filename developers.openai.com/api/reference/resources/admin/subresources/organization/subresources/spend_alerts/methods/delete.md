<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Spend Alerts](/api/reference/resources/admin/subresources/organization/subresources/spend_alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization spend alert

DELETE/organization/spend\_alerts/{alert\_id}

Deletes an organization spend alert.

##### Path ParametersExpand Collapse

alert\_id: string

##### ReturnsExpand Collapse

OrganizationSpendAlertDeleted object { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

### Delete organization spend alert

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/spend_alerts/alert_abc123 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true
