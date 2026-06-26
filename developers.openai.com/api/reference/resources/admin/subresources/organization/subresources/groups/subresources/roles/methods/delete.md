<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign organization role from group

DELETE/organization/groups/{group\_id}/roles/{role\_id}

Unassigns an organization role from a group within the organization.

##### Path ParametersExpand Collapse

group\_id: string

role\_id: string

##### ReturnsExpand Collapse

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from group

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ/roles/role_01J1F8ROLE01 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true
