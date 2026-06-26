<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

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

# Add group user

$ openai admin:organization:groups:users create

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to update.

--user-id: string

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

AdminOrganizationGroupUserNewResponse: object { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

### Add group user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups:users create \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id \
  --user-id user_id

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
