<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list/ -->

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

# List group users

client.admin.organization.groups.users.list(stringgroupID, UserListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[OrganizationGroupUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name } >

GET/organization/groups/{group\_id}/users

Lists the users assigned to a group.

##### ParametersExpand Collapse

groupID: string

query: UserListParams { after, limit, order }

after?: string

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

limit?: number

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

order?: "asc" | "desc"

Specifies the sort order of users in the list.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

OrganizationGroupUser { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string | null

The email address of the user.

name: string

The name of the user.

### List group users

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
for await (const organizationGroupUser of client.admin.organization.groups.users.list('group_id')) {
  console.log(organizationGroupUser.id);

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null
