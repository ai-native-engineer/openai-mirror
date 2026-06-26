<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve/ -->

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

# Retrieve ChatKit thread

GET/chatkit/threads/{thread\_id}

Retrieve a ChatKit thread by its identifier.

##### Path ParametersExpand Collapse

thread\_id: string

##### ReturnsExpand Collapse

ChatKitThread object { id, created\_at, object, 3 more }

Represents a ChatKit thread and its current status.

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

### Retrieve ChatKit thread

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/chatkit/threads/cthr_abc123 \
  -H "OpenAI-Beta: chatkit_beta=v1" \
  -H "Authorization: Bearer $OPENAI_API_KEY"

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
