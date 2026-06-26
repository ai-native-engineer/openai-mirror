<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete/ -->

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

# Delete project model permissions

admin.organization.projects.model\_permissions.delete(strproject\_id)  -> [ProjectModelPermissionsDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/model\_permissions

Deletes model permissions for a project.

##### ParametersExpand Collapse

project\_id: str

##### ReturnsExpand Collapse

class ProjectModelPermissionsDeleted: …

Confirmation payload returned after deleting project model permissions.

deleted: bool

Whether the project model permissions were deleted.

object: Literal["project.model\_permissions.deleted"]

The object type, which is always `project.model_permissions.deleted`.

### Delete project model permissions

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
project_model_permissions_deleted = client.admin.organization.projects.model_permissions.delete(
    "project_id",
print(project_model_permissions_deleted.deleted)

    "object": "project.model_permissions.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.model_permissions.deleted",
    "deleted": true
