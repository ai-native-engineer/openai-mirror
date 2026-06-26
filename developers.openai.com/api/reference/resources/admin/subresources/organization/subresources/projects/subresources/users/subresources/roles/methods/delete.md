<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign project role from user

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

Unassigns a project role from a user within a project.

##### Path ParametersExpand Collapse

project\_id: string

user\_id: string

role\_id: string

##### ReturnsExpand Collapse

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign project role from user

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/projects/proj_abc123/users/user_abc123/roles/role_01J1F8PROJ \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "user.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "user.role.deleted",
    "deleted": true
