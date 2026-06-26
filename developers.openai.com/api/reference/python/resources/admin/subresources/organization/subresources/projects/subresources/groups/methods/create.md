<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add project group

admin.organization.projects.groups.create(strproject\_id, GroupCreateParams\*\*kwargs)  -> [ProjectGroup](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))

POST/organization/projects/{project\_id}/groups

Grants a group access to a project.

##### ParametersExpand Collapse

project\_id: str

group\_id: str

Identifier of the group to add to the project.

role: str

Identifier of the project role to grant to the group.

##### ReturnsExpand Collapse

class ProjectGroup: …

Details about a group’s membership in a project.

created\_at: int

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: str

Identifier of the group that has access to the project.

group\_name: str

Display name of the group.

group\_type: Literal["group", "tenant\_group"]

The type of the group.

One of the following:

"group"

"tenant\_group"

object: Literal["project.group"]

Always `project.group`.

project\_id: str

Identifier of the project.

### Add project group

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
project_group = client.admin.organization.projects.groups.create(
    project_id="project_id",
    group_id="group_id",
    role="role",
print(project_group.group_id)

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533
