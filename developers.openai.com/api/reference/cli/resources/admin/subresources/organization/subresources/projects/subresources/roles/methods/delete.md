<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project role

$ openai admin:organization:projects:roles delete

DELETE/projects/{project\_id}/roles/{role\_id}

Deletes a custom role from a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to update.

--role-id: string

The ID of the role to delete.

##### ReturnsExpand Collapse

AdminOrganizationProjectRoleDeleteResponse: object { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

### Delete project role

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:roles delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --role-id role_id

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true
