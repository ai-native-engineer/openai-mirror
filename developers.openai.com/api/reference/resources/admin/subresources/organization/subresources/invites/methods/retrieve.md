<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/invites/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Invites](/api/reference/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve invite

GET/organization/invites/{invite\_id}

Retrieves an invite.

##### Path ParametersExpand Collapse

invite\_id: string

##### ReturnsExpand Collapse

Invite object { id, created\_at, email, 6 more }

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

projects: array of object { id, role }

The projects that were granted membership upon acceptance of the invite.

id: string

Project’s public ID

role: "member" or "owner"

Project membership role

One of the following:

"member"

"owner"

role: "owner" or "reader"

`owner` or `reader`

One of the following:

"owner"

"reader"

status: "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at: optional number

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: optional number

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

### Retrieve invite

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/invites/invite-abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "organization.invite",
    "id": "invite-abc",
    "email": "user@example.com",
    "role": "owner",
    "status": "accepted",
    "created_at": 1711471533,
    "expires_at": 1711471533,
    "accepted_at": 1711471533

##### Returns Examples

    "object": "organization.invite",
    "id": "invite-abc",
    "email": "user@example.com",
    "role": "owner",
    "status": "accepted",
    "created_at": 1711471533,
    "expires_at": 1711471533,
    "accepted_at": 1711471533
