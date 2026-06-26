<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/update/ -->

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

# Modify user

admin.organization.users.update(user\_id, \*\*kwargs) -> [OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

POST/organization/users/{user\_id}

Modifies a user’s role in the organization.

##### ParametersExpand Collapse

user\_id: String

developer\_persona: String

Developer persona metadata.

role: String

`owner` or `reader`

role\_id: String

Role ID to assign to the user.

technical\_level: String

Technical level metadata.

##### ReturnsExpand Collapse

class OrganizationUser { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: String

The identifier, which can be referenced in API endpoints

added\_at: Integer

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: :"organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: Integer

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: Integer

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: String

The developer persona metadata for the user.

email: String

The email address of the user

is\_default: bool

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: bool

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: bool

Whether the user is managed through SCIM.

is\_service\_account: bool

Whether the user is a service account.

name: String

The name of the user

projects: Projects{ data, object}

Projects associated with the user, if included.

data: Array[Data{ id, name, role}]

id: String

name: String

role: String

object: :list

role: String

`owner` or `reader`

technical\_level: String

The technical level metadata for the user.

user: User{ id, object, banned, 5 more}

Nested user details.

id: String

object: :user

banned: bool

banned\_at: Integer

formatunixtime

email: String

enabled: bool

name: String

picture: String

### Modify user

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

organization_user = openai.admin.organization.users.update("user_id")

puts(organization_user)

    "object": "organization.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
