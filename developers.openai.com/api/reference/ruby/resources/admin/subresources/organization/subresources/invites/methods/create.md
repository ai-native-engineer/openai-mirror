<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Invites](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create invite

admin.organization.invites.create(\*\*kwargs) -> [Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

POST/organization/invites

Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

##### ParametersExpand Collapse

email: String

Send an email to this address

role: :reader | :owner

`owner` or `reader`

One of the following:

:reader

:owner

projects: Array[Project{ id, role}]

An array of projects to which membership is granted at the same time the org invite is accepted. If omitted, the user will be invited to the default project for compatibility with legacy behavior. If empty list is passed, the user will not be invited to any projects, including the default one.

id: String

Project’s public ID

role: :member | :owner

Project membership role

One of the following:

:member

:owner

##### ReturnsExpand Collapse

class Invite { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: String

The email address of the individual to whom the invite was sent

object: :"organization.invite"

The object type, which is always `organization.invite`

projects: Array[Project{ id, role}]

The projects that were granted membership upon acceptance of the invite.

id: String

Project’s public ID

role: :member | :owner

Project membership role

One of the following:

:member

:owner

role: :owner | :reader

`owner` or `reader`

One of the following:

:owner

:reader

status: :accepted | :expired | :pending

`accepted`,`expired`, or `pending`

One of the following:

:accepted

:expired

:pending

accepted\_at: Integer

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

### Create invite

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

invite = openai.admin.organization.invites.create(email: "email", role: :reader)

puts(invite)

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
