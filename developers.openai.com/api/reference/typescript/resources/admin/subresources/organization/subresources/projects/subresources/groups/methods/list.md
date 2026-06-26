<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project groups

client.admin.organization.projects.groups.list(stringprojectID, GroupListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[ProjectGroup](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more } >

GET/organization/projects/{project\_id}/groups

Lists the groups that have access to a project.

##### ParametersExpand Collapse

projectID: string

query: GroupListParams { after, limit, order }

after?: string

Cursor for pagination. Provide the ID of the last group from the previous response to fetch the next page.

limit?: number

A limit on the number of project groups to return. Defaults to 20.

minimum0

maximum100

order?: "asc" | "desc"

Sort order for the returned groups.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

ProjectGroup { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" | "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

### List project groups

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

// Automatically fetches more pages as needed.
for await (const projectGroup of client.admin.organization.projects.groups.list('project_id')) {
  console.log(projectGroup.group_id);

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
