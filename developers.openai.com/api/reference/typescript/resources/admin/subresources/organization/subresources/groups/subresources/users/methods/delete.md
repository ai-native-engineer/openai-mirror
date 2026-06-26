<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Remove group user

client.admin.organization.groups.users.delete(stringuserID, UserDeleteParams { group\_id } params, RequestOptionsoptions?): [UserDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/users/{user\_id}

Removes a user from a group.

##### ParametersExpand Collapse

userID: string

params: UserDeleteParams { group\_id }

group\_id: string

The ID of the group to update.

##### ReturnsExpand Collapse

UserDeleteResponse { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: boolean

Whether the group membership was removed.

object: "group.user.deleted"

Always `group.user.deleted`.

### Remove group user

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

const user = await client.admin.organization.groups.users.delete('user_id', {
  group_id: 'group_id',

console.log(user.deleted);

    "object": "group.user.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.user.deleted",
    "deleted": true
