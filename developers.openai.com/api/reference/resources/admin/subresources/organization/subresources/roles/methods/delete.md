<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### Path ParametersExpand Collapse

role\_id: string

##### ReturnsExpand Collapse

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

### Delete organization role

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/roles/role_01J1F8ROLE01 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true
