<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete/ -->

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

# Delete project user

admin.organization.projects.users.delete(struser\_id, UserDeleteParams\*\*kwargs)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/users/{user\_id}

Deletes a user from the project.

Returns confirmation of project user deletion, or an error if the project is
archived (archived projects have no users).

##### ParametersExpand Collapse

project\_id: str

user\_id: str

##### ReturnsExpand Collapse

class UserDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.user.deleted"]

### Delete project user

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
user = client.admin.organization.projects.users.delete(
    user_id="user_id",
    project_id="project_id",
print(user.id)

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true
