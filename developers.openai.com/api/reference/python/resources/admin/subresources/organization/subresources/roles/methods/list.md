<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/list/ -->

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

# List organization roles

admin.organization.roles.list(RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))]

GET/organization/roles

Lists the roles configured for the organization.

##### ParametersExpand Collapse

after: Optional[str]

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing roles.

limit: Optional[int]

A limit on the number of roles to return. Defaults to 1000.

minimum0

maximum1000

order: Optional[Literal["asc", "desc"]]

Sort order for the returned roles.

One of the following:

"asc"

"desc"

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

### List organization roles

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
page = client.admin.organization.roles.list()
page = page.data[0]
print(page.id)

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
