<!-- source: https://developers.openai.com/api/reference/ruby/resources/conversations/subresources/items/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Conversations](/api/reference/ruby/resources/conversations)

[Items](/api/reference/ruby/resources/conversations/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an item

conversations.items.delete(item\_id, \*\*kwargs) -> [Conversation](/api/reference/ruby/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) { id, created\_at, metadata, object }

DELETE/conversations/{conversation\_id}/items/{item\_id}

Delete an item from a conversation with the given IDs.

##### ParametersExpand Collapse

conversation\_id: String

item\_id: String

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

### Delete an item

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

conversation = openai.conversations.items.delete("msg_abc", conversation_id: "conv_123")

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
