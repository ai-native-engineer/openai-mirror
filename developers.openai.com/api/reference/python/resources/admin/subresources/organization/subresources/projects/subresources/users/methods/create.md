<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create/ -->

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

# Create project user

admin.organization.projects.users.create(strproject\_id, UserCreateParams\*\*kwargs)  -> [ProjectUser](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

POST/organization/projects/{project\_id}/users

Adds a user to the project. Users must already be members of the organization to be added to a project.

##### ParametersExpand Collapse

project\_id: str

role: str

`owner` or `member`

email: Optional[str]

Email of the user to add.

user\_id: Optional[str]

The ID of the user.

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

### Create project user

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
project_user = client.admin.organization.projects.users.create(
    project_id="project_id",
    role="role",
print(project_user.id)

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
