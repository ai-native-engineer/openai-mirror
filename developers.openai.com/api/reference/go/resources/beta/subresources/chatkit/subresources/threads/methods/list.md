<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list/ -->

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

# List ChatKit threads

client.Beta.ChatKit.Threads.List(ctx, query) (\*ConversationCursorPage[[ChatKitThread](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema))], error)

GET/chatkit/threads

List ChatKit threads with optional pagination and user filters.

##### ParametersExpand Collapse

query BetaChatKitThreadListParams

After param.Field[string]Optional

List items created after this thread item ID. Defaults to null for the first page.

Before param.Field[string]Optional

List items created before this thread item ID. Defaults to null for the newest results.

Limit param.Field[int64]Optional

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

Order param.Field[[BetaChatKitThreadListParamsOrder](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for results by creation time. Defaults to `desc`.

const BetaChatKitThreadListParamsOrderAsc [BetaChatKitThreadListParamsOrder](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const BetaChatKitThreadListParamsOrderDesc [BetaChatKitThreadListParamsOrder](/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/list#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

User param.Field[string]Optional

Filter threads that belong to this user identifier. Defaults to null to return all users.

minLength1

maxLength512

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

### List ChatKit threads

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
  page, err := client.Beta.ChatKit.Threads.List(context.TODO(), openai.BetaChatKitThreadListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
