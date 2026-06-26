<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Invites](/api/reference/python/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create invite

admin.organization.invites.create(InviteCreateParams\*\*kwargs)  -> [Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))

POST/organization/invites

Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

##### ParametersExpand Collapse

email: str

Send an email to this address

role: Literal["reader", "owner"]

`owner` or `reader`

One of the following:

"reader"

"owner"

projects: Optional[Iterable[Project]]

An array of projects to which membership is granted at the same time the org invite is accepted. If omitted, the user will be invited to the default project for compatibility with legacy behavior. If empty list is passed, the user will not be invited to any projects, including the default one.

id: str

Project’s public ID

role: Literal["member", "owner"]

Project membership role

One of the following:

"member"

"owner"

##### ReturnsExpand Collapse

class Invite: …

Represents an individual `invite` to the organization.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: str

The email address of the individual to whom the invite was sent

object: Literal["organization.invite"]

The object type, which is always `organization.invite`

projects: List[Project]

The projects that were granted membership upon acceptance of the invite.

id: str

Project’s public ID

role: Literal["member", "owner"]

Project membership role

One of the following:

"member"

"owner"

role: Literal["owner", "reader"]

`owner` or `reader`

One of the following:

"owner"

"reader"

status: Literal["accepted", "expired", "pending"]

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at: Optional[int]

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

### Create invite

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
invite = client.admin.organization.invites.create(
    email="email",
    role="reader",
print(invite.id)

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
