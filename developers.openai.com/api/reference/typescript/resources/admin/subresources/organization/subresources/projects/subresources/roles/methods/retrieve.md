<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project role

client.admin.organization.projects.roles.retrieve(stringroleID, RoleRetrieveParams { project\_id } params, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/projects/{project\_id}/roles/{role\_id}

Retrieves a project role.

##### ParametersExpand Collapse

roleID: string

params: RoleRetrieveParams { project\_id }

project\_id: string

The ID of the project.

##### ReturnsExpand Collapse

Role { id, description, name, 4 more }

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

### Retrieve project role

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

const role = await client.admin.organization.projects.roles.retrieve('role_id', {
  project_id: 'project_id',

console.log(role.id);

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
