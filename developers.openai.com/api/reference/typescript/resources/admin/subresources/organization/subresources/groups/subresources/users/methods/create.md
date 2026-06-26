<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

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

# Add group user

client.admin.organization.groups.users.create(stringgroupID, UserCreateParams { user\_id } body, RequestOptionsoptions?): [UserCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)) { group\_id, object, user\_id }

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### ParametersExpand Collapse

groupID: string

body: UserCreateParams { user\_id }

user\_id: string

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

UserCreateResponse { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

### Add group user

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

const user = await client.admin.organization.groups.users.create('group_id', {
  user_id: 'user_id',

console.log(user.group_id);

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
