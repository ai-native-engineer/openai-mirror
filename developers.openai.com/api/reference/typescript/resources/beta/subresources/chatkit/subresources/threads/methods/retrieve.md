<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve/ -->

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

# Retrieve ChatKit thread

client.beta.chatkit.threads.retrieve(stringthreadID, RequestOptionsoptions?): [ChatKitThread](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) { id, created\_at, object, 3 more }

GET/chatkit/threads/{thread\_id}

Retrieve a ChatKit thread by its identifier.

##### ParametersExpand Collapse

threadID: string

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

### Retrieve ChatKit thread

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

const chatkitThread = await client.beta.chatkit.threads.retrieve('cthr_123');

console.log(chatkitThread.id);

  "id": "cthr_abc123",
  "object": "chatkit.thread",
  "title": "Customer escalation",
  "items": {
    "data": [
        "id": "cthi_user_001",
        "object": "chatkit.thread_item",
        "type": "user_message",
        "content": [
            "type": "input_text",
            "text": "I need help debugging an onboarding issue."
        ],
        "attachments": []
        "id": "cthi_assistant_002",
        "object": "chatkit.thread_item",
        "type": "assistant_message",
        "content": [
            "type": "output_text",
            "text": "Let's start by confirming the workflow version you deployed."
        ]
    ],
    "has_more": false

##### Returns Examples

  "id": "cthr_abc123",
  "object": "chatkit.thread",
  "title": "Customer escalation",
  "items": {
    "data": [
        "id": "cthi_user_001",
        "object": "chatkit.thread_item",
        "type": "user_message",
        "content": [
            "type": "input_text",
            "text": "I need help debugging an onboarding issue."
        ],
        "attachments": []
        "id": "cthi_assistant_002",
        "object": "chatkit.thread_item",
        "type": "assistant_message",
        "content": [
            "type": "output_text",
            "text": "Let's start by confirming the workflow version you deployed."
        ]
    ],
    "has_more": false
