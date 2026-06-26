<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign organization role to user

POST/organization/users/{user\_id}/roles

Assigns an organization role to a user within the organization.

##### Path ParametersExpand Collapse

user\_id: string

##### Body ParametersJSONExpand Collapse

role\_id: string

Identifier of the role to assign.

##### ReturnsExpand Collapse

object: "user.role"

Always `user.role`.

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: string

Identifier for the role.

description: string

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: array of string

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).

user: [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: optional number

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: optional number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: optional string

The developer persona metadata for the user.

email: optional string

The email address of the user

is\_default: optional boolean

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: optional boolean

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: optional boolean

Whether the user is managed through SCIM.

is\_service\_account: optional boolean

Whether the user is a service account.

name: optional string

The name of the user

projects: optional object { data, object }

Projects associated with the user, if included.

data: array of object { id, name, role }

id: optional string

name: optional string

role: optional string

object: "list"

role: optional string

`owner` or `reader`

technical\_level: optional string

The technical level metadata for the user.

user: optional object { id, object, banned, 5 more }

Nested user details.

id: string

object: "user"

banned: optional boolean

banned\_at: optional number

formatunixtime

email: optional string

enabled: optional boolean

name: optional string

picture: optional string

### Assign organization role to user

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/users/user_abc123/roles \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "role_id": "role_01J1F8ROLE01"
  }'

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
        "id": "role_01J1F8ROLE01",
        "name": "API Group Manager",
        "description": "Allows managing organization groups",
        "permissions": [
            "api.groups.read",
            "api.groups.write"
        ],
        "resource_type": "api.organization",
        "predefined_role": false
