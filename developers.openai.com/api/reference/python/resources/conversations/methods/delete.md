<!-- source: https://developers.openai.com/api/reference/python/resources/conversations/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Conversations](/api/reference/python/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a conversation

conversations.delete(strconversation\_id)  -> [ConversationDeletedResource](/api/reference/python/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema))

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### ParametersExpand Collapse

conversation\_id: str

##### ReturnsExpand Collapse

class ConversationDeletedResource: …

id: str

deleted: bool

object: Literal["conversation.deleted"]

### Delete a conversation

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

deleted = client.conversations.delete("conv_123")
print(deleted)

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
