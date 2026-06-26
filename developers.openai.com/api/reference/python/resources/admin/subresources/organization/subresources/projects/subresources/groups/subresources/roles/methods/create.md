<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign project role to group

admin.organization.projects.groups.roles.create(strgroup\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/projects/{project\_id}/groups/{group\_id}/roles

Assigns a project role to a group within a project.

##### ParametersExpand Collapse

project\_id: str

group\_id: str

role\_id: str

Identifier of the role to assign.

##### ReturnsExpand Collapse

class RoleCreateResponse: …

Role assignment linking a group to a role.

group: Group

Summary information about a group returned in role assignment responses.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: str

Display name of the group.

object: Literal["group"]

Always `group`.

scim\_managed: bool

Whether the group is managed through SCIM.

object: Literal["group.role"]

Always `group.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

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

### Assign project role to group

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
role = client.admin.organization.projects.groups.roles.create(
    group_id="group_id",
    project_id="project_id",
    role_id="role_id",
print(role.group)

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
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

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
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
