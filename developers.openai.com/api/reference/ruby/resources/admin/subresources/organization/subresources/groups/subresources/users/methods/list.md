<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list/ -->

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

# List group users

admin.organization.groups.users.list(group\_id, \*\*kwargs) -> NextCursorPage<[OrganizationGroupUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name } >

GET/organization/groups/{group\_id}/users

Lists the users assigned to a group.

##### ParametersExpand Collapse

group\_id: String

after: String

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

limit: Integer

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

order: :asc | :desc

Specifies the sort order of users in the list.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class OrganizationGroupUser { id, email, name }

Represents an individual user returned when inspecting group membership.

id: String

The identifier, which can be referenced in API endpoints

email: String

The email address of the user.

name: String

The name of the user.

### List group users

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

page = openai.admin.organization.groups.users.list("group_id")

puts(page)

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null
