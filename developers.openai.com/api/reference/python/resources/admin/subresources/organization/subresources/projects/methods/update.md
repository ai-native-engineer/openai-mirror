<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/update/ -->

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

# Modify project

admin.organization.projects.update(strproject\_id, ProjectUpdateParams\*\*kwargs)  -> [Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

POST/organization/projects/{project\_id}

Modifies a project in the organization.

##### ParametersExpand Collapse

project\_id: str

external\_key\_id: Optional[str]

External key ID to associate with the project.

geography: Optional[str]

Geography for the project.

name: Optional[str]

The updated name of the project, this name appears in reports.

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

### Modify project

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
project = client.admin.organization.projects.update(
    project_id="project_id",
print(project.id)

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"
