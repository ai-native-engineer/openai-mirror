<!-- source: https://developers.openai.com/api/reference/cli/resources/conversations/subresources/items/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Conversations](/api/reference/cli/resources/conversations)

[Items](/api/reference/cli/resources/conversations/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an item

$ openai conversations:items delete

DELETE/conversations/{conversation\_id}/items/{item\_id}

Delete an item from a conversation with the given IDs.

##### ParametersExpand Collapse

--conversation-id: string

The ID of the conversation that contains the item.

--item-id: string

The ID of the item to delete.

##### ReturnsExpand Collapse

conversation: object { id, created\_at, metadata, object }

id: string

The unique ID of the conversation.

created\_at: number

The time at which the conversation was created, measured in seconds since the Unix epoch.

metadata: unknown

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: "conversation"

The object type, which is always `conversation`.

### Delete an item

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai conversations:items delete \
  --api-key 'My API Key' \
  --conversation-id conv_123 \
  --item-id msg_abc

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
