<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/list/ -->

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

# List invites

admin.organization.invites.list(\*\*kwargs) -> ConversationCursorPage<[Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more } >

GET/organization/invites

Returns a list of invites in the organization.

##### ParametersExpand Collapse

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List invites

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

page = openai.admin.organization.invites.list

puts(page)

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
