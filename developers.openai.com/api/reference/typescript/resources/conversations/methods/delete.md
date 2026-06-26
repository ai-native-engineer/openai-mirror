<!-- source: https://developers.openai.com/api/reference/typescript/resources/conversations/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Conversations](/api/reference/typescript/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a conversation

client.conversations.delete(stringconversationID, RequestOptionsoptions?): [ConversationDeletedResource](/api/reference/typescript/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)) { id, deleted, object }

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### ParametersExpand Collapse

conversationID: string

##### ReturnsExpand Collapse

ConversationDeletedResource { id, deleted, object }

id: string

deleted: boolean

object: "conversation.deleted"

### Delete a conversation

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";
const client = new OpenAI();

const deleted = await client.conversations.delete("conv_123");
console.log(deleted);

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
