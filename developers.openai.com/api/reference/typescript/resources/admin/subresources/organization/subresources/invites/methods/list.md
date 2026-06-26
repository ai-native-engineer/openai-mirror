<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Invites](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List invites

client.admin.organization.invites.list(InviteListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more } >

GET/organization/invites

Returns a list of invites in the organization.

##### ParametersExpand Collapse

query: InviteListParams { after, limit }

after?: string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit?: number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

Invite { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: string

The email address of the individual to whom the invite was sent

object: "organization.invite"

The object type, which is always `organization.invite`

projects: Array<Project>

The projects that were granted membership upon acceptance of the invite.

id: string

Project’s public ID

role: "member" | "owner"

Project membership role

One of the following:

"member"

"owner"

role: "owner" | "reader"

`owner` or `reader`

One of the following:

"owner"

"reader"

status: "accepted" | "expired" | "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at?: number | null

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at?: number | null

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

### List invites

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
for await (const invite of client.admin.organization.invites.list()) {
  console.log(invite.id);

  "object": "list",
  "data": [
      "object": "organization.invite",
      "id": "invite-abc",
      "email": "user@example.com",
      "role": "owner",
      "status": "accepted",
      "created_at": 1711471533,
      "expires_at": 1711471533,
      "accepted_at": 1711471533
  ],
  "first_id": "invite-abc",
  "last_id": "invite-abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.invite",
      "id": "invite-abc",
      "email": "user@example.com",
      "role": "owner",
      "status": "accepted",
      "created_at": 1711471533,
      "expires_at": 1711471533,
      "accepted_at": 1711471533
  ],
  "first_id": "invite-abc",
  "last_id": "invite-abc",
  "has_more": false
