<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/chatkit/subresources/threads/methods/delete/ -->

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

# Delete ChatKit thread

client.Beta.ChatKit.Threads.Delete(ctx, threadID) (\*[BetaChatKitThreadDeleteResponse](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20BetaChatKitThreadDeleteResponse%20%3E%20(schema)), error)

DELETE/chatkit/threads/{thread\_id}

Delete a ChatKit thread along with its items and stored attachments.

##### ParametersExpand Collapse

threadID string

##### ReturnsExpand Collapse

type BetaChatKitThreadDeleteResponse struct{…}

Confirmation payload returned after deleting a thread.

ID string

Identifier of the deleted thread.

Deleted bool

Indicates that the thread has been deleted.

Object ChatKitThreadDeleted

Type discriminator that is always `chatkit.thread.deleted`.

### Delete ChatKit thread

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
  thread, err := client.Beta.ChatKit.Threads.Delete(context.TODO(), "cthr_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", thread.ID)

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"
