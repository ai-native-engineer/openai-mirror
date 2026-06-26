<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Threads](/api/reference/go/resources/beta/subresources/threads)

[Messages](/api/reference/go/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.Beta.Threads.Messages.Delete(ctx, threadID, messageID) (\*[MessageDeleted](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)), error)

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### ParametersExpand Collapse

threadID string

messageID string

##### ReturnsExpand Collapse

type MessageDeleted struct{…}

ID string

Deleted bool

Object ThreadMessageDeleted

### Delete message

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
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  messageDeleted, err := client.Beta.Threads.Messages.Delete(
    context.TODO(),
    "thread_id",
    "message_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", messageDeleted.ID)

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
