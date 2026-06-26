<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

$ openai admin:organization:roles delete

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### ParametersExpand Collapse

--role-id: string

The ID of the role to delete.

##### ReturnsExpand Collapse

AdminOrganizationRoleDeleteResponse: object { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

### Delete organization role

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:roles delete \
  --admin-api-key 'My Admin API Key' \
  --role-id role_id

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true
