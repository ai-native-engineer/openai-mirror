<!-- source: https://developers.openai.com/api/reference/python/resources/conversations/subresources/items/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Conversations](/api/reference/python/resources/conversations)

[Items](/api/reference/python/resources/conversations/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an item

conversations.items.delete(stritem\_id, ItemDeleteParams\*\*kwargs)  -> [Conversation](/api/reference/python/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema))

DELETE/conversations/{conversation\_id}/items/{item\_id}

Delete an item from a conversation with the given IDs.

##### ParametersExpand Collapse

conversation\_id: str

item\_id: str

##### ReturnsExpand Collapse

class Conversation: …

id: str

The unique ID of the conversation.

created\_at: int

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

metadata: object

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: Literal["conversation"]

The object type, which is always `conversation`.

### Delete an item

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

conversation = client.conversations.items.delete("conv_123", "msg_abc")
print(conversation)

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
