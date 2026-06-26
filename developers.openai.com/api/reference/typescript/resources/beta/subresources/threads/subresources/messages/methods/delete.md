<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Threads](/api/reference/typescript/resources/beta/subresources/threads)

[Messages](/api/reference/typescript/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.beta.threads.messages.delete(stringmessageID, MessageDeleteParams { thread\_id } params, RequestOptionsoptions?): [MessageDeleted](/api/reference/typescript/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### ParametersExpand Collapse

messageID: string

params: MessageDeleteParams { thread\_id }

thread\_id: string

The ID of the thread to which this message belongs.

##### ReturnsExpand Collapse

MessageDeleted { id, deleted, object }

id: string

deleted: boolean

object: "thread.message.deleted"

### Delete message

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

const openai = new OpenAI();

async function main() {
  const deletedMessage = await openai.beta.threads.messages.delete(
    "msg_abc123",
    { thread_id: "thread_abc123" }
  );

  console.log(deletedMessage);

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
