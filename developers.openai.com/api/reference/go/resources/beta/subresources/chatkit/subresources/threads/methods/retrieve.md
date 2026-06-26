<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[ChatKit](/api/reference/go/resources/beta/subresources/chatkit)

[Threads](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve ChatKit thread

client.Beta.ChatKit.Threads.Get(ctx, threadID) (\*[ChatKitThread](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)), error)

GET/chatkit/threads/{thread\_id}

Retrieve a ChatKit thread by its identifier.

##### ParametersExpand Collapse

threadID string

##### ReturnsExpand Collapse

type ChatKitThread struct{…}

Represents a ChatKit thread and its current status.

ID string

Identifier of the thread.

CreatedAt int64

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

Object ChatKitThread

Type discriminator that is always `chatkit.thread`.

Status ChatKitThreadStatusUnion

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

type ChatKitThreadStatusActive struct{…}

Indicates that a thread is active.

Type Active

Status discriminator that is always `active`.

type ChatKitThreadStatusLocked struct{…}

Indicates that a thread is locked and cannot accept new input.

Reason string

Reason that the thread was locked. Defaults to null when no reason is recorded.

Type Locked

Status discriminator that is always `locked`.

type ChatKitThreadStatusClosed struct{…}

Indicates that a thread has been closed.

Reason string

Reason that the thread was closed. Defaults to null when no reason is recorded.

Type Closed

Status discriminator that is always `closed`.

Title string

Optional human-readable title for the thread. Defaults to null when no title has been generated.

User string

Free-form string that identifies your end user who owns the thread.

### Retrieve ChatKit thread

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"

func main() {
  client := openai.NewClient()
  chatkitThread, err := client.Beta.ChatKit.Threads.Get(context.TODO(), "cthr_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", chatkitThread.ID)

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
