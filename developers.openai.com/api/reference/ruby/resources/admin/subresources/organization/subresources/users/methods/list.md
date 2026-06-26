<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/list/ -->

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

# List users

admin.organization.users.list(\*\*kwargs) -> ConversationCursorPage<[OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more } >

GET/organization/users

Lists all of the users in the organization.

##### ParametersExpand Collapse

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

emails: Array[String]

Filter by the email address of users.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List users

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

page = openai.admin.organization.users.list

puts(page)

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false
