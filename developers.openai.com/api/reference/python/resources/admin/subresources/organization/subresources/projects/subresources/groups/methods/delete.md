<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete/ -->

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

# Remove project group

admin.organization.projects.groups.delete(strgroup\_id, GroupDeleteParams\*\*kwargs)  -> [GroupDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/groups/{group\_id}

Revokes a group’s access to a project.

##### ParametersExpand Collapse

project\_id: str

group\_id: str

##### ReturnsExpand Collapse

class GroupDeleteResponse: …

Confirmation payload returned after removing a group from a project.

deleted: bool

Whether the group membership in the project was removed.

object: Literal["project.group.deleted"]

Always `project.group.deleted`.

### Remove project group

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
group = client.admin.organization.projects.groups.delete(
    group_id="group_id",
    project_id="project_id",
print(group.deleted)

    "object": "project.group.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.group.deleted",
    "deleted": true
