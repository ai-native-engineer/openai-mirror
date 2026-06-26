<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit threads

GET/chatkit/threads

List ChatKit threads with optional pagination and user filters.

##### Query ParametersExpand Collapse

after: optional string

List items created after this thread item ID. Defaults to null for the first page.

before: optional string

List items created before this thread item ID. Defaults to null for the newest results.

limit: optional number

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

order: optional "asc" or "desc"

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

"desc"

user: optional string

Filter threads that belong to this user identifier. Defaults to null to return all users.

minLength1

maxLength512

##### ReturnsExpand Collapse

data: array of [ChatKitThread](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more }

A list of items

id: string

Identifier of the thread.

created\_at: number

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: "chatkit.thread"

Type discriminator that is always `chatkit.thread`.

status: object { type }  or object { reason, type }  or object { reason, type }

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

Active object { type }

Indicates that a thread is active.

type: "active"

Status discriminator that is always `active`.

Locked object { reason, type }

Indicates that a thread is locked and cannot accept new input.

reason: string

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: "locked"

Status discriminator that is always `locked`.

Closed object { reason, type }

Indicates that a thread has been closed.

reason: string

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: "closed"

Status discriminator that is always `closed`.

title: string

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: string

Free-form string that identifies your end user who owns the thread.

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

### List ChatKit threads

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl "https://api.openai.com/v1/chatkit/threads?limit=2&order=desc" \
  -H "OpenAI-Beta: chatkit_beta=v1" \
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "data": [
      "id": "cthr_abc123",
      "object": "chatkit.thread",
      "title": "Customer escalation"
      "id": "cthr_def456",
      "object": "chatkit.thread",
      "title": "Demo feedback"
  ],
  "has_more": false,
  "object": "list"

##### Returns Examples

  "data": [
      "id": "cthr_abc123",
      "object": "chatkit.thread",
      "title": "Customer escalation"
      "id": "cthr_def456",
      "object": "chatkit.thread",
      "title": "Demo feedback"
  ],
  "has_more": false,
  "object": "list"
