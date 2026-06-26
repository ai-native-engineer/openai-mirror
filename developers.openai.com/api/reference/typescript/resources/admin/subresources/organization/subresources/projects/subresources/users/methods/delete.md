<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project user

client.admin.organization.projects.users.delete(stringuserID, UserDeleteParams { project\_id } params, RequestOptionsoptions?): [UserDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/users/{user\_id}

Deletes a user from the project.

Returns confirmation of project user deletion, or an error if the project is
archived (archived projects have no users).

##### ParametersExpand Collapse

userID: string

params: UserDeleteParams { project\_id }

project\_id: string

The ID of the project.

##### ReturnsExpand Collapse

UserDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.user.deleted"

### Delete project user

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

const user = await client.admin.organization.projects.users.delete('user_id', {
  project_id: 'project_id',

console.log(user.id);

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true
