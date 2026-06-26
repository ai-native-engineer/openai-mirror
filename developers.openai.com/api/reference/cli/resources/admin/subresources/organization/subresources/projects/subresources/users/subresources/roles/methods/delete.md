<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign project role from user

$ openai admin:organization:projects:users:roles delete

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

Unassigns a project role from a user within a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to modify.

--user-id: string

The ID of the user whose project role assignment should be removed.

--role-id: string

The ID of the project role to remove from the user.

##### ReturnsExpand Collapse

AdminOrganizationProjectUserRoleDeleteResponse: object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign project role from user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:users:roles delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --user-id user_id \
  --role-id role_id

    "object": "user.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "user.role.deleted",
    "deleted": true
