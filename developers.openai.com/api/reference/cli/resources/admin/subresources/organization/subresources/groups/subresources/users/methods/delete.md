<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Remove group user

$ openai admin:organization:groups:users delete

DELETE/organization/groups/{group\_id}/users/{user\_id}

Removes a user from a group.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to update.

--user-id: string

The ID of the user to remove from the group.

##### ReturnsExpand Collapse

AdminOrganizationGroupUserDeleteResponse: object { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: boolean

Whether the group membership was removed.

object: "group.user.deleted"

Always `group.user.deleted`.

### Remove group user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups:users delete \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id \
  --user-id user_id

    "object": "group.user.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.user.deleted",
    "deleted": true
