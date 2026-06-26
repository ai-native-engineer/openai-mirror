<!-- source: https://developers.openai.com/api/reference/go/resources/conversations/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Conversations](/api/reference/go/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a conversation

client.Conversations.Delete(ctx, conversationID) (\*[ConversationDeletedResource](/api/reference/go/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)), error)

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### ParametersExpand Collapse

conversationID string

##### ReturnsExpand Collapse

type ConversationDeletedResource struct{…}

ID string

Deleted bool

Object ConversationDeleted

### Delete a conversation

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
  conversationDeletedResource, err := client.Conversations.Delete(context.TODO(), "conv_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", conversationDeletedResource.ID)

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
