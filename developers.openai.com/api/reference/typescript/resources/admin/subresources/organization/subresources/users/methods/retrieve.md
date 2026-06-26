<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/users/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Users](/api/reference/typescript/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve user

client.admin.organization.users.retrieve(stringuserID, RequestOptionsoptions?): [OrganizationUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

GET/organization/users/{user\_id}

Retrieves a user by their identifier.

##### ParametersExpand Collapse

userID: string

##### ReturnsExpand Collapse

OrganizationUser { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at?: number | null

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created?: number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona?: string | null

The developer persona metadata for the user.

email?: string | null

The email address of the user

is\_default?: boolean

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser?: boolean | null

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed?: boolean

Whether the user is managed through SCIM.

is\_service\_account?: boolean

Whether the user is a service account.

name?: string | null

The name of the user

projects?: Projects | null

Projects associated with the user, if included.

data: Array<Data>

id?: string | null

name?: string | null

role?: string | null

object: "list"

role?: string | null

`owner` or `reader`

technical\_level?: string | null

The technical level metadata for the user.

user?: User { id, object, banned, 5 more }

Nested user details.

id: string

object: "user"

banned?: boolean | null

banned\_at?: number | null

formatunixtime

email?: string | null

enabled?: boolean | null

name?: string | null

picture?: string | null

### Retrieve user

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

const organizationUser = await client.admin.organization.users.retrieve('user_id');

console.log(organizationUser.id);

    "object": "organization.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
