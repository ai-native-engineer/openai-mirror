<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve group organization role

client.admin.organization.groups.roles.retrieve(stringroleID, RoleRetrieveParams { group\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/groups/{group\_id}/roles/{role\_id}

Retrieves an organization role assigned to a group.

##### ParametersExpand Collapse

roleID: string

params: RoleRetrieveParams { group\_id }

group\_id: string

The ID of the group to inspect.

##### ReturnsExpand Collapse

RoleRetrieveResponse { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: Array<AssignmentSource> | null

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number | null

When the role was created.

formatunixtime

created\_by: string | null

Identifier of the actor who created the role.

created\_by\_user\_obj: Record<string, unknown> | null

User details for the actor that created the role, when available.

description: string | null

Description of the role.

metadata: Record<string, unknown> | null

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: Array<string>

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number | null

When the role was last updated.

formatunixtime

### Retrieve group organization role

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

const role = await client.admin.organization.groups.roles.retrieve('role_id', {
  group_id: 'group_id',

console.log(role.id);

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

##### Returns Examples

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null
