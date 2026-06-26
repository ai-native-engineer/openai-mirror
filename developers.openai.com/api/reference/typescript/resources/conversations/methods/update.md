<!-- source: https://developers.openai.com/api/reference/typescript/resources/conversations/methods/update/ -->

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

# Update a conversation

client.conversations.update(stringconversationID, ConversationUpdateParams { metadata } body, RequestOptionsoptions?): [Conversation](/api/reference/typescript/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) { id, created\_at, metadata, object }

POST/conversations/{conversation\_id}

Update a conversation

##### ParametersExpand Collapse

conversationID: string

body: ConversationUpdateParams { metadata }

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

##### ReturnsExpand Collapse

Conversation { id, created\_at, metadata, object }

id: string

The unique ID of the conversation.

created\_at: number

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

metadata: unknown

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: "conversation"

The object type, which is always `conversation`.

### Update a conversation

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

const updated = await client.conversations.update(
  "conv_123",
  { metadata: { topic: "project-x" } }
);
console.log(updated);

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}
