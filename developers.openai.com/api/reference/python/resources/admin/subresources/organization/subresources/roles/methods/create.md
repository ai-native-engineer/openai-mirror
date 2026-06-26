<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create organization role

admin.organization.roles.create(RoleCreateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/organization/roles

Creates a custom role for the organization.

##### ParametersExpand Collapse

permissions: Sequence[str]

Permissions to grant to the role.

role\_name: str

Unique name for the role.

description: Optional[str]

Optional description of the role.

##### ReturnsExpand Collapse

class Role: …

Details about a role that can be assigned through the public Roles API.

id: str

Identifier for the role.

description: Optional[str]

Optional description of the role.

name: str

Unique name for the role.

object: Literal["role"]

Always `role`.

permissions: List[str]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: str

Resource type the role is bound to (for example `api.organization` or `api.project`).

### Create organization role

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
role = client.admin.organization.roles.create(
    permissions=["string"],
    role_name="role_name",
print(role.id)

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
