<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List organization roles

admin.organization.roles.list(\*\*kwargs) -> NextCursorPage<[Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/organization/roles

Lists the roles configured for the organization.

##### ParametersExpand Collapse

after: String

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing roles.

limit: Integer

A limit on the number of roles to return. Defaults to 1000.

minimum0

maximum1000

order: :asc | :desc

Sort order for the returned roles.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class Role { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: String

Identifier for the role.

description: String

Optional description of the role.

name: String

Unique name for the role.

object: :role

Always `role`.

permissions: Array[String]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: String

Resource type the role is bound to (for example `api.organization` or `api.project`).

### List organization roles

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

page = openai.admin.organization.roles.list

puts(page)

    "object": "list",
    "data": [
            "object": "role",
            "id": "role_01J1F8ROLE01",
            "name": "API Group Manager",
            "description": "Allows managing organization groups",
            "permissions": [
                "api.groups.read",
                "api.groups.write"
            ],
            "resource_type": "api.organization",
            "predefined_role": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "role",
            "id": "role_01J1F8ROLE01",
            "name": "API Group Manager",
            "description": "Allows managing organization groups",
            "permissions": [
                "api.groups.read",
                "api.groups.write"
            ],
            "resource_type": "api.organization",
            "predefined_role": false
    ],
    "has_more": false,
    "next": null
