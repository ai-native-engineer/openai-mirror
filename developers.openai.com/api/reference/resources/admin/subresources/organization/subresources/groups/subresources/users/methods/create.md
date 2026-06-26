<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add group user

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### Path ParametersExpand Collapse

group\_id: string

##### Body ParametersJSONExpand Collapse

user\_id: string

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

### Add group user

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ/users \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "user_id": "user_abc123"
  }'

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
