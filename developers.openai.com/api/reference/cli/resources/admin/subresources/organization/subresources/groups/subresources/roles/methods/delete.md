<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign organization role from group

$ openai admin:organization:groups:roles delete

DELETE/organization/groups/{group\_id}/roles/{role\_id}

Unassigns an organization role from a group within the organization.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to modify.

--role-id: string

The ID of the organization role to remove from the group.

##### ReturnsExpand Collapse

AdminOrganizationGroupRoleDeleteResponse: object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups:roles delete \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id \
  --role-id role_id

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true
