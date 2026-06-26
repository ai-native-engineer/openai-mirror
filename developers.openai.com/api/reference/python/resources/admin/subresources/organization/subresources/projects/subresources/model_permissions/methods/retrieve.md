<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Model Permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project model permissions

admin.organization.projects.model\_permissions.retrieve(strproject\_id)  -> [ProjectModelPermissions](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema))

GET/organization/projects/{project\_id}/model\_permissions

Returns model permissions for a project.

##### ParametersExpand Collapse

project\_id: str

##### ReturnsExpand Collapse

class ProjectModelPermissions: …

Represents the model allowlist or denylist policy for a project.

mode: Literal["allow\_list", "deny\_list"]

Whether the project uses an allowlist or a denylist.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: List[str]

The model IDs included in the model permissions policy.

object: Literal["project.model\_permissions"]

The object type, which is always `project.model_permissions`.

### Retrieve project model permissions

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
project_model_permissions = client.admin.organization.projects.model_permissions.retrieve(
    "project_id",
print(project_model_permissions.model_ids)

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]
