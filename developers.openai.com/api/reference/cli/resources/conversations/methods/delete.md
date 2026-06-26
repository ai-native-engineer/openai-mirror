<!-- source: https://developers.openai.com/api/reference/cli/resources/conversations/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Conversations](/api/reference/cli/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a conversation

$ openai conversations delete

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### ParametersExpand Collapse

--conversation-id: string

The ID of the conversation to delete.

##### ReturnsExpand Collapse

conversation\_deleted\_resource: object { id, deleted, object }

id: string

deleted: boolean

object: "conversation.deleted"

### Delete a conversation

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai conversations delete \
  --api-key 'My API Key' \
  --conversation-id conv_123

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
