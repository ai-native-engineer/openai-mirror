<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List group organization role assignments

admin.organization.groups.roles.list(strgroup\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/organization/groups/{group\_id}/roles

Lists the organization roles assigned to a group within the organization.

##### ParametersExpand Collapse

group\_id: str

after: Optional[str]

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing organization roles.

limit: Optional[int]

A limit on the number of organization role assignments to return.

minimum0

maximum1000

order: Optional[Literal["asc", "desc"]]

Sort order for the returned organization roles.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

class RoleListResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

### List group organization role assignments

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
page = client.admin.organization.groups.roles.list(
    group_id="group_id",
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
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
            "created_by_user_obj": {
                "id": "user_abc123",
                "name": "Ada Lovelace",
                "email": "ada@example.com"
            "metadata": {}
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
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
            "created_by_user_obj": {
                "id": "user_abc123",
                "name": "Ada Lovelace",
                "email": "ada@example.com"
            "metadata": {}
    ],
    "has_more": false,
    "next": null
