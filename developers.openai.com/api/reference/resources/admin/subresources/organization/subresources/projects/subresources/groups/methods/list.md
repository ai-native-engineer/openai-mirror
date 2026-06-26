<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project groups

GET/organization/projects/{project\_id}/groups

Lists the groups that have access to a project.

##### Path ParametersExpand Collapse

project\_id: string

##### Query ParametersExpand Collapse

after: optional string

Cursor for pagination. Provide the ID of the last group from the previous response to fetch the next page.

limit: optional number

A limit on the number of project groups to return. Defaults to 20.

minimum0

maximum100

order: optional "asc" or "desc"

Sort order for the returned groups.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

data: array of [ProjectGroup](/api/reference/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

Project group memberships returned in the current page.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" or "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

has\_more: boolean

Whether additional project group memberships are available.

next: string

Cursor to fetch the next page of results, or `null` when there are no more results.

object: "list"

Always `list`.

### List project groups

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/projects/proj_abc123/groups?limit=20 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "list",
    "data": [
            "object": "project.group",
            "project_id": "proj_abc123",
            "group_id": "group_01J1F8ABCDXYZ",
            "group_name": "Support Team",
            "created_at": 1711471533
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "project.group",
            "project_id": "proj_abc123",
            "group_id": "group_01J1F8ABCDXYZ",
            "group_name": "Support Team",
            "created_at": 1711471533
    ],
    "has_more": false,
    "next": null
