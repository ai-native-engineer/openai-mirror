<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Users](/api/reference/python/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve user organization role

admin.organization.users.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/organization/users/{user\_id}/roles/{role\_id}

Retrieves an organization role assigned to a user.

##### ParametersExpand Collapse

user\_id: str

role\_id: str

##### ReturnsExpand Collapse

class RoleRetrieveResponse: …

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

### Retrieve user organization role

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
role = client.admin.organization.users.roles.retrieve(
    role_id="role_id",
    user_id="user_id",
print(role.id)

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
