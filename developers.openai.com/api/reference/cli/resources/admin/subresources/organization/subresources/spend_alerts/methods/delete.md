<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete/ -->

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

# Delete organization spend alert

$ openai admin:organization:spend-alerts delete

DELETE/organization/spend\_alerts/{alert\_id}

Deletes an organization spend alert.

##### ParametersExpand Collapse

--alert-id: string

The ID of the spend alert to delete.

##### ReturnsExpand Collapse

organization\_spend\_alert\_deleted: object { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

### Delete organization spend alert

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:spend-alerts delete \
  --admin-api-key 'My Admin API Key' \
  --alert-id alert_id

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true

##### Returns Examples

    "id": "alert_abc123",
    "object": "organization.spend_alert.deleted",
    "deleted": true
