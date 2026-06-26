<!-- source: https://developers.openai.com/api/reference/go/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Chat](/api/reference/go/resources/chat)

[Completions](/api/reference/go/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

client.Chat.Completions.Delete(ctx, completionID) (\*[ChatCompletionDeleted](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)), error)

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### ParametersExpand Collapse

completionID string

##### ReturnsExpand Collapse

type ChatCompletionDeleted struct{…}

ID string

The ID of the chat completion that was deleted.

Deleted bool

Whether the chat completion was deleted.

Object ChatCompletionDeleted

The type of object being deleted.

### Delete chat completion

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
  chatCompletionDeleted, err := client.Chat.Completions.Delete(context.TODO(), "completion_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", chatCompletionDeleted.ID)

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
