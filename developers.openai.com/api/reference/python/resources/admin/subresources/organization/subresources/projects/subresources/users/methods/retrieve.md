<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project user

admin.organization.projects.users.retrieve(struser\_id, UserRetrieveParams\*\*kwargs)  -> [ProjectUser](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

GET/organization/projects/{project\_id}/users/{user\_id}

Retrieves a user in the project.

##### ParametersExpand Collapse

project\_id: str

user\_id: str

##### ReturnsExpand Collapse

class ProjectUser: …

Represents an individual user in a project.

id: str

The identifier, which can be referenced in API endpoints

added\_at: int

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

object: Literal["organization.project.user"]

The object type, which is always `organization.project.user`

role: str

`owner` or `member`

email: Optional[str]

The email address of the user

name: Optional[str]

The name of the user

### Retrieve project user

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
project_user = client.admin.organization.projects.users.retrieve(
    user_id="user_id",
    project_id="project_id",
print(project_user.id)

    "object": "organization.project.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.project.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
