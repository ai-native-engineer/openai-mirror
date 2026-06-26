<!-- source: https://developers.openai.com/api/reference/typescript/resources/conversations/methods/retrieve/ -->

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

# Retrieve a conversation

client.conversations.retrieve(stringconversationID, RequestOptionsoptions?): [Conversation](/api/reference/typescript/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) { id, created\_at, metadata, object }

GET/conversations/{conversation\_id}

Get a conversation

##### ParametersExpand Collapse

conversationID: string

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

### Retrieve a conversation

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

const conversation = await client.conversations.retrieve("conv_123");
console.log(conversation);

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
