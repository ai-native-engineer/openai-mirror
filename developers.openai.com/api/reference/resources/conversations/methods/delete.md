<!-- source: https://developers.openai.com/api/reference/resources/conversations/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Conversations](/api/reference/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a conversation

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### Path ParametersExpand Collapse

conversation\_id: string

##### ReturnsExpand Collapse

ConversationDeletedResource object { id, deleted, object }

id: string

deleted: boolean

object: "conversation.deleted"

### Delete a conversation

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/conversations/conv_123 \
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
