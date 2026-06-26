<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve/ -->

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

# Retrieve ChatKit thread

beta.chatkit.threads.retrieve(strthread\_id)  -> [ChatKitThread](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))

GET/chatkit/threads/{thread\_id}

Retrieve a ChatKit thread by its identifier.

##### ParametersExpand Collapse

thread\_id: str

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

### Retrieve ChatKit thread

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
chatkit_thread = client.beta.chatkit.threads.retrieve(
    "cthr_123",
print(chatkit_thread.id)

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
