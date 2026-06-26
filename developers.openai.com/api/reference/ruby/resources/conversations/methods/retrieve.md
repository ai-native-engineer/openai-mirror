<!-- source: https://developers.openai.com/api/reference/ruby/resources/conversations/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Conversations](/api/reference/ruby/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve a conversation

conversations.retrieve(conversation\_id) -> [Conversation](/api/reference/ruby/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) { id, created\_at, metadata, object }

GET/conversations/{conversation\_id}

Get a conversation

##### ParametersExpand Collapse

conversation\_id: String

##### ReturnsExpand Collapse

class Conversation { id, created\_at, metadata, object }

id: String

The unique ID of the conversation.

created\_at: Integer

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

metadata: untyped

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: :conversation

The object type, which is always `conversation`.

### Retrieve a conversation

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

conversation = openai.conversations.retrieve("conv_123")

puts(conversation)

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
