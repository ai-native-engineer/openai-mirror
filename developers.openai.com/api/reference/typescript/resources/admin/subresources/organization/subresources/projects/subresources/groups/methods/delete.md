<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete/ -->

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

# Remove project group

client.admin.organization.projects.groups.delete(stringgroupID, GroupDeleteParams { project\_id } params, RequestOptionsoptions?): [GroupDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/groups/{group\_id}

Revokes a group’s access to a project.

##### ParametersExpand Collapse

groupID: string

params: GroupDeleteParams { project\_id }

project\_id: string

The ID of the project to update.

##### ReturnsExpand Collapse

GroupDeleteResponse { deleted, object }

Confirmation payload returned after removing a group from a project.

deleted: boolean

Whether the group membership in the project was removed.

object: "project.group.deleted"

Always `project.group.deleted`.

### Remove project group

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

const group = await client.admin.organization.projects.groups.delete('group_id', {
  project_id: 'project_id',

console.log(group.deleted);

    "object": "project.group.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.group.deleted",
    "deleted": true
