<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Invites](/api/reference/cli/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List invites

$ openai admin:organization:invites list

GET/organization/invites

Returns a list of invites in the organization.

##### ParametersExpand Collapse

--after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

--limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

InviteListResponse: object { data, has\_more, object, 2 more }

data: array of [Invite](/api/reference/cli/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the invite was sent.

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

"member"

"owner"

role: "owner" or "reader"

`owner` or `reader`

"owner"

"reader"

status: "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

"accepted"

"expired"

"pending"

accepted\_at: optional number

The Unix timestamp (in seconds) of when the invite was accepted.

expires\_at: optional number

The Unix timestamp (in seconds) of when the invite expires.

has\_more: boolean

The `has_more` property is used for pagination to indicate there are additional results.

object: "list"

The object type, which is always `list`

first\_id: optional string

The first `invite_id` in the retrieved `list`

last\_id: optional string

The last `invite_id` in the retrieved `list`

### List invites

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:invites list \
  --admin-api-key 'My Admin API Key'

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
