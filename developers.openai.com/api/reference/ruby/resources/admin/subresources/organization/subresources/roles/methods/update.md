<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/update/ -->

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

# Update organization role

admin.organization.roles.update(role\_id, \*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles/{role\_id}

Updates an existing organization role.

##### ParametersExpand Collapse

role\_id: String

description: String

New description for the role.

permissions: Array[String]

Updated set of permissions for the role.

role\_name: String

New name for the role.

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

### Update organization role

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

role = openai.admin.organization.roles.update("role_id")

puts(role)

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

##### Returns Examples

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
