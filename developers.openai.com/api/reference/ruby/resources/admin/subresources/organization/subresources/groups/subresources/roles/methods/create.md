<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign organization role to group

admin.organization.groups.roles.create(group\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/organization/groups/{group\_id}/roles

Assigns an organization role to a group within the organization.

##### ParametersExpand Collapse

group\_id: String

role\_id: String

Identifier of the role to assign.

##### ReturnsExpand Collapse

class RoleCreateResponse { group, object, role }

Role assignment linking a group to a role.

group: Group{ id, created\_at, name, 2 more}

Summary information about a group returned in role assignment responses.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: String

Display name of the group.

object: :group

Always `group`.

scim\_managed: bool

Whether the group is managed through SCIM.

object: :"group.role"

Always `group.role`.

role: [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

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

### Assign organization role to group

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

role = openai.admin.organization.groups.roles.create("group_id", role_id: "role_id")

puts(role)

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
    "role": {
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

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
    "role": {
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
