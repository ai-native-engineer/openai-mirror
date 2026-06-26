<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[ChatKit](/api/reference/python/resources/beta/subresources/chatkit)

[Threads](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit threads

beta.chatkit.threads.list(ThreadListParams\*\*kwargs)  -> SyncConversationCursorPage[[ChatKitThread](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))]

GET/chatkit/threads

List ChatKit threads with optional pagination and user filters.

##### ParametersExpand Collapse

after: Optional[str]

List items created after this thread item ID. Defaults to null for the first page.

before: Optional[str]

List items created before this thread item ID. Defaults to null for the newest results.

limit: Optional[int]

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

order: Optional[Literal["asc", "desc"]]

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

"desc"

user: Optional[str]

Filter threads that belong to this user identifier. Defaults to null to return all users.

minLength1

maxLength512

##### ReturnsExpand Collapse

class ChatKitThread: …

Represents a ChatKit thread and its current status.

id: str

Identifier of the thread.

created\_at: int

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: Literal["chatkit.thread"]

Type discriminator that is always `chatkit.thread`.

status: Status

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

class StatusActive: …

Indicates that a thread is active.

type: Literal["active"]

Status discriminator that is always `active`.

class StatusLocked: …

Indicates that a thread is locked and cannot accept new input.

reason: Optional[str]

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: Literal["locked"]

Status discriminator that is always `locked`.

class StatusClosed: …

Indicates that a thread has been closed.

reason: Optional[str]

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: Literal["closed"]

Status discriminator that is always `closed`.

title: Optional[str]

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: str

Free-form string that identifies your end user who owns the thread.

### List ChatKit threads

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI

client = OpenAI()
page = client.beta.chatkit.threads.list()
page = page.data[0]
print(page.id)

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
