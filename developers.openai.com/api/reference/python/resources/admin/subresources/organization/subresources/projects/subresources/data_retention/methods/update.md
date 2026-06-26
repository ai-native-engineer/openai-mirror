<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update project data retention

admin.organization.projects.data\_retention.update(strproject\_id, DataRetentionUpdateParams\*\*kwargs)  -> [ProjectDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema))

POST/organization/projects/{project\_id}/data\_retention

Updates project data retention controls.

##### ParametersExpand Collapse

project\_id: str

retention\_type: Literal["organization\_default", "none", "zero\_data\_retention", 3 more]

The desired project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

##### ReturnsExpand Collapse

class ProjectDataRetention: …

Represents a project’s data retention control setting.

object: Literal["project.data\_retention"]

The object type, which is always `project.data_retention`.

type: Literal["organization\_default", "none", "zero\_data\_retention", 3 more]

The configured project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Update project data retention

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
project_data_retention = client.admin.organization.projects.data_retention.update(
    project_id="project_id",
    retention_type="organization_default",
print(project_data_retention.object)

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"
