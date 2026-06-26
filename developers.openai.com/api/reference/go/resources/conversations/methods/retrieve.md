<!-- source: https://developers.openai.com/api/reference/go/resources/conversations/methods/retrieve/ -->

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

# Retrieve a conversation

client.Conversations.Get(ctx, conversationID) (\*[Conversation](/api/reference/go/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)), error)

GET/conversations/{conversation\_id}

Get a conversation

##### ParametersExpand Collapse

conversationID string

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

### Retrieve a conversation

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
  conversation, err := client.Conversations.Get(context.TODO(), "conv_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", conversation.ID)

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
