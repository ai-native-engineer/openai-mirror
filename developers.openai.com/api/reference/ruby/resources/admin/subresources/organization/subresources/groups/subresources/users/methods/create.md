<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add group user

admin.organization.groups.users.create(group\_id, \*\*kwargs) -> [UserCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)) { group\_id, object, user\_id }

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### ParametersExpand Collapse

group\_id: String

user\_id: String

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

class UserCreateResponse { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: String

Identifier of the group the user was added to.

object: :"group.user"

Always `group.user`.

user\_id: String

Identifier of the user that was added.

### Add group user

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

user = openai.admin.organization.groups.users.create("group_id", user_id: "user_id")

puts(user)

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
