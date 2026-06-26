<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign organization role from user

$ openai admin:organization:users:roles delete

DELETE/organization/users/{user\_id}/roles/{role\_id}

Unassigns an organization role from a user within the organization.

##### ParametersExpand Collapse

--user-id: string

The ID of the user to modify.

--role-id: string

The ID of the organization role to remove from the user.

##### ReturnsExpand Collapse

AdminOrganizationUserRoleDeleteResponse: object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:users:roles delete \
  --admin-api-key 'My Admin API Key' \
  --user-id user_id \
  --role-id role_id

    "object": "user.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "user.role.deleted",
    "deleted": true
