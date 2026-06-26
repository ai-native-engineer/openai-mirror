<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Users](/api/reference/ruby/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete user

admin.organization.users.delete(user\_id) -> [UserDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/users/{user\_id}

Deletes a user from the organization.

##### ParametersExpand Collapse

user\_id: String

##### ReturnsExpand Collapse

class UserDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.user.deleted"

### Delete user

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

user = openai.admin.organization.users.delete("user_id")

puts(user)

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true
