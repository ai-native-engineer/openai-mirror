<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign project role from group

$ openai admin:organization:projects:groups:roles delete

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

Unassigns a project role from a group within a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to modify.

--group-id: string

The ID of the group whose project role assignment should be removed.

--role-id: string

The ID of the project role to remove from the group.

##### ReturnsExpand Collapse

AdminOrganizationProjectGroupRoleDeleteResponse: object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign project role from group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:groups:roles delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --group-id group_id \
  --role-id role_id

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true
