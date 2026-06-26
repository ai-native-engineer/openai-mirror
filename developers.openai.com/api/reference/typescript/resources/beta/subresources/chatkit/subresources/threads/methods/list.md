<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[ChatKit](/api/reference/typescript/resources/beta/subresources/chatkit)

[Threads](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List ChatKit threads

client.beta.chatkit.threads.list(ThreadListParams { after, before, limit, 2 more } query?, RequestOptionsoptions?): ConversationCursorPage<[ChatKitThread](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more } >

GET/chatkit/threads

List ChatKit threads with optional pagination and user filters.

##### ParametersExpand Collapse

query: ThreadListParams { after, before, limit, 2 more }

after?: string

List items created after this thread item ID. Defaults to null for the first page.

before?: string

List items created before this thread item ID. Defaults to null for the newest results.

limit?: number

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

order?: "asc" | "desc"

Sort order for results by creation time. Defaults to `desc`.

One of the following:

"asc"

"desc"

user?: string

Filter threads that belong to this user identifier. Defaults to null to return all users.

minLength1

maxLength512

##### ReturnsExpand Collapse

ChatKitThread { id, created\_at, object, 3 more }

Represents a ChatKit thread and its current status.

id: string

Identifier of the thread.

created\_at: number

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

object: "chatkit.thread"

Type discriminator that is always `chatkit.thread`.

status: Active { type }  | Locked { reason, type }  | Closed { reason, type }

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

Active { type }

Indicates that a thread is active.

type: "active"

Status discriminator that is always `active`.

Locked { reason, type }

Indicates that a thread is locked and cannot accept new input.

reason: string | null

Reason that the thread was locked. Defaults to null when no reason is recorded.

type: "locked"

Status discriminator that is always `locked`.

Closed { reason, type }

Indicates that a thread has been closed.

reason: string | null

Reason that the thread was closed. Defaults to null when no reason is recorded.

type: "closed"

Status discriminator that is always `closed`.

title: string | null

Optional human-readable title for the thread. Defaults to null when no title has been generated.

user: string

Free-form string that identifies your end user who owns the thread.

### List ChatKit threads

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

const client = new OpenAI();

// Automatically fetches more pages as needed.
for await (const chatkitThread of client.beta.chatkit.threads.list()) {
  console.log(chatkitThread.id);

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
