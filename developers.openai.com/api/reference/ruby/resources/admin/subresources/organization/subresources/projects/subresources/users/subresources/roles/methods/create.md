<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign project role to user

admin.organization.projects.users.roles.create(user\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/projects/{project\_id}/users/{user\_id}/roles

Assigns a project role to a user within a project.

##### ParametersExpand Collapse

project\_id: String

user\_id: String

role\_id: String

Identifier of the role to assign.

##### ReturnsExpand Collapse

class RoleCreateResponse { object, role, user }

Role assignment linking a user to a role.

object: :"user.role"

Always `user.role`.

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

user: [OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

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

### Assign project role to user

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

role = openai.admin.organization.projects.users.roles.create(
  "user_id",
  project_id: "project_id",
  role_id: "role_id"

puts(role)

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8PROJ",
        "name": "API Project Key Manager",
        "description": "Allows managing API keys for the project",
        "permissions": [
            "api.organization.projects.api_keys.read",
            "api.organization.projects.api_keys.write"
        ],
        "resource_type": "api.project",
        "predefined_role": false

##### Returns Examples

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8PROJ",
        "name": "API Project Key Manager",
        "description": "Allows managing API keys for the project",
        "permissions": [
            "api.organization.projects.api_keys.read",
            "api.organization.projects.api_keys.write"
        ],
        "resource_type": "api.project",
        "predefined_role": false
