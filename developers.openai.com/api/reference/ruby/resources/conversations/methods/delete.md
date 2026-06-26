<!-- source: https://developers.openai.com/api/reference/ruby/resources/conversations/methods/delete/ -->

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

# Delete a conversation

conversations.delete(conversation\_id) -> [ConversationDeletedResource](/api/reference/ruby/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)) { id, deleted, object }

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### ParametersExpand Collapse

conversation\_id: String

##### ReturnsExpand Collapse

class ConversationDeletedResource { id, deleted, object }

id: String

deleted: bool

object: :"conversation.deleted"

### Delete a conversation

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

conversation_deleted_resource = openai.conversations.delete("conv_123")

puts(conversation_deleted_resource)

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
