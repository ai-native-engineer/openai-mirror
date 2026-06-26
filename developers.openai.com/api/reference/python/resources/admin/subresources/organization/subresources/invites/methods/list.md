<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/list/ -->

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

# List invites

admin.organization.invites.list(InviteListParams\*\*kwargs)  -> SyncConversationCursorPage[[Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))]

GET/organization/invites

Returns a list of invites in the organization.

##### ParametersExpand Collapse

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List invites

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
page = client.admin.organization.invites.list()
page = page.data[0]
print(page.id)

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
