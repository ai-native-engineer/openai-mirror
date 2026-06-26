<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve/ -->

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

# Retrieve group user

admin.organization.groups.users.retrieve(user\_id, \*\*kwargs) -> [UserRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)) { id, email, is\_service\_account, 3 more }

GET/organization/groups/{group\_id}/users/{user\_id}

Retrieves a user in a group.

##### ParametersExpand Collapse

group\_id: String

user\_id: String

##### ReturnsExpand Collapse

class UserRetrieveResponse { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: String

Identifier for the user.

email: String

Email address of the user, or `null` for users without an email.

is\_service\_account: bool

Whether the user is a service account.

name: String

Display name of the user.

picture: String

URL of the user’s profile picture, if available.

user\_type: :user | :tenant\_user

The type of user.

One of the following:

:user

:tenant\_user

### Retrieve group user

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

user = openai.admin.organization.groups.users.retrieve("user_id", group_id: "group_id")

puts(user)

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

##### Returns Examples

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"
