<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/list/ -->

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

# List projects

admin.organization.projects.list(ProjectListParams\*\*kwargs)  -> SyncConversationCursorPage[[Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))]

GET/organization/projects

Returns a list of projects.

##### ParametersExpand Collapse

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

include\_archived: Optional[[bool](/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/list#(resource)%20admin.organization.projects%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20include_archived%20%3E%20(schema))]

If `true` returns all projects including those that have been `archived`. Archived projects are not included by default.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List projects

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
page = client.admin.organization.projects.list()
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "id": "proj_abc",
            "object": "organization.project",
            "name": "Project example",
            "created_at": 1711471533,
            "archived_at": null,
            "status": "active"
    ],
    "first_id": "proj-abc",
    "last_id": "proj-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "id": "proj_abc",
            "object": "organization.project",
            "name": "Project example",
            "created_at": 1711471533,
            "archived_at": null,
            "status": "active"
    ],
    "first_id": "proj-abc",
    "last_id": "proj-xyz",
    "has_more": false
