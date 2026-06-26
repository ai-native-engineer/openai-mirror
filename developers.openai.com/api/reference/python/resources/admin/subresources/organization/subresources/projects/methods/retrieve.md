<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project

admin.organization.projects.retrieve(strproject\_id)  -> [Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

GET/organization/projects/{project\_id}

Retrieves a project.

##### ParametersExpand Collapse

project\_id: str

##### ReturnsExpand Collapse

class Project: …

Represents an individual project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: Literal["organization.project"]

The object type, which is always `organization.project`

archived\_at: Optional[int]

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id: Optional[str]

The external key associated with the project.

name: Optional[str]

The name of the project. This appears in reporting.

status: Optional[str]

`active` or `archived`

### Retrieve project

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
project = client.admin.organization.projects.retrieve(
    "project_id",
print(project.id)

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project example",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"

##### Returns Examples

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project example",
    "created_at": 1711471533,
    "archived_at": null,
    "status": "active"
