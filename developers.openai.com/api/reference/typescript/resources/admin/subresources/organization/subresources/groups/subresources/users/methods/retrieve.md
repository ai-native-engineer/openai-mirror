<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve/ -->

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

# Retrieve group user

client.admin.organization.groups.users.retrieve(stringuserID, UserRetrieveParams { group\_id } params, RequestOptionsoptions?): [UserRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)) { id, email, is\_service\_account, 3 more }

GET/organization/groups/{group\_id}/users/{user\_id}

Retrieves a user in a group.

##### ParametersExpand Collapse

userID: string

params: UserRetrieveParams { group\_id }

group\_id: string

The ID of the group to inspect.

##### ReturnsExpand Collapse

UserRetrieveResponse { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: string

Identifier for the user.

email: string | null

Email address of the user, or `null` for users without an email.

is\_service\_account: boolean | null

Whether the user is a service account.

name: string

Display name of the user.

picture: string | null

URL of the user’s profile picture, if available.

user\_type: "user" | "tenant\_user"

The type of user.

One of the following:

"user"

"tenant\_user"

### Retrieve group user

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

const user = await client.admin.organization.groups.users.retrieve('user_id', {
  group_id: 'group_id',

console.log(user.id);

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

##### Returns Examples

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"
