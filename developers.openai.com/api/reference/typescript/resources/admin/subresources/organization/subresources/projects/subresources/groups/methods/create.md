<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create/ -->

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

# Add project group

client.admin.organization.projects.groups.create(stringprojectID, GroupCreateParams { group\_id, role } body, RequestOptionsoptions?): [ProjectGroup](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

POST/organization/projects/{project\_id}/groups

Grants a group access to a project.

##### ParametersExpand Collapse

projectID: string

body: GroupCreateParams { group\_id, role }

group\_id: string

Identifier of the group to add to the project.

role: string

Identifier of the project role to grant to the group.

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

### Add project group

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

const projectGroup = await client.admin.organization.projects.groups.create('project_id', {
  group_id: 'group_id',
  role: 'role',

console.log(projectGroup.group_id);

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533
