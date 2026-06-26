<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/create/ -->

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

# Create invite

client.admin.organization.invites.create(InviteCreateParams { email, role, projects } body, RequestOptionsoptions?): [Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

POST/organization/invites

Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

##### ParametersExpand Collapse

body: InviteCreateParams { email, role, projects }

email: string

Send an email to this address

role: "reader" | "owner"

`owner` or `reader`

One of the following:

"reader"

"owner"

projects?: Array<Project>

An array of projects to which membership is granted at the same time the org invite is accepted. If omitted, the user will be invited to the default project for compatibility with legacy behavior. If empty list is passed, the user will not be invited to any projects, including the default one.

id: string

Project’s public ID

role: "member" | "owner"

Project membership role

One of the following:

"member"

"owner"

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

### Create invite

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

const invite = await client.admin.organization.invites.create({ email: 'email', role: 'reader' });

console.log(invite.id);

  "object": "organization.invite",
  "id": "invite-def",
  "email": "anotheruser@example.com",
  "role": "reader",
  "status": "pending",
  "created_at": 1711471533,
  "expires_at": 1711471533,
  "accepted_at": null,
  "projects": [
      "id": "project-xyz",
      "role": "member"
      "id": "project-abc",
      "role": "owner"
  ]

##### Returns Examples

  "object": "organization.invite",
  "id": "invite-def",
  "email": "anotheruser@example.com",
  "role": "reader",
  "status": "pending",
  "created_at": 1711471533,
  "expires_at": 1711471533,
  "accepted_at": null,
  "projects": [
      "id": "project-xyz",
      "role": "member"
      "id": "project-abc",
      "role": "owner"
  ]
