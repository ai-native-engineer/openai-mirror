<!-- source: https://developers.openai.com/api/reference/go/resources/conversations/methods/update/ -->

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

# Update a conversation

client.Conversations.Update(ctx, conversationID, body) (\*[Conversation](/api/reference/go/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)), error)

POST/conversations/{conversation\_id}

Update a conversation

##### ParametersExpand Collapse

conversationID string

body ConversationUpdateParams

Metadata param.Field[[Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

##### ReturnsExpand Collapse

type Conversation struct{…}

ID string

The unique ID of the conversation.

CreatedAt int64

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

Metadata any

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

Object Conversation

The object type, which is always `conversation`.

### Update a conversation

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
  "github.com/openai/openai-go/conversations"
  "github.com/openai/openai-go/option"
  "github.com/openai/openai-go/shared"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  conversation, err := client.Conversations.Update(
    context.TODO(),
    "conv_123",
    conversations.ConversationUpdateParams{
      Metadata: shared.Metadata{
      "foo": "string",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", conversation.ID)

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}
