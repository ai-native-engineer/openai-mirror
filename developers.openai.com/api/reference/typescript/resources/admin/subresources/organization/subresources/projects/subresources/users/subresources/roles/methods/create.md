<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign project role to user

client.admin.organization.projects.users.roles.create(stringuserID, RoleCreateParams { project\_id, role\_id } params, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/projects/{project\_id}/users/{user\_id}/roles

Assigns a project role to a user within a project.

##### ParametersExpand Collapse

userID: string

params: RoleCreateParams { project\_id, role\_id }

project\_id: string

Path param: The ID of the project to update.

role\_id: string

Body param: Identifier of the role to assign.

##### ReturnsExpand Collapse

RoleCreateResponse { object, role, user }

Role assignment linking a user to a role.

object: "user.role"

Always `user.role`.

role: [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: string

Identifier for the role.

description: string | null

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: Array<string>

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).

user: [OrganizationUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at?: number | null

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created?: number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona?: string | null

The developer persona metadata for the user.

email?: string | null

The email address of the user

is\_default?: boolean

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser?: boolean | null

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed?: boolean

Whether the user is managed through SCIM.

is\_service\_account?: boolean

Whether the user is a service account.

name?: string | null

The name of the user

projects?: Projects | null

Projects associated with the user, if included.

data: Array<Data>

id?: string | null

name?: string | null

role?: string | null

object: "list"

role?: string | null

`owner` or `reader`

technical\_level?: string | null

The technical level metadata for the user.

user?: User { id, object, banned, 5 more }

Nested user details.

id: string

object: "user"

banned?: boolean | null

banned\_at?: number | null

formatunixtime

email?: string | null

enabled?: boolean | null

name?: string | null

picture?: string | null

### Assign project role to user

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const role = await client.admin.organization.projects.users.roles.create('user_id', {
  project_id: 'project_id',
  role_id: 'role_id',

console.log(role.object);

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
