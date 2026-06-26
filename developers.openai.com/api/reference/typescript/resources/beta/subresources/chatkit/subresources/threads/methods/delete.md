<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[ChatKit](/api/reference/typescript/resources/beta/subresources/chatkit)

[Threads](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete ChatKit thread

client.beta.chatkit.threads.delete(stringthreadID, RequestOptionsoptions?): [ThreadDeleteResponse](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/chatkit/threads/{thread\_id}

Delete a ChatKit thread along with its items and stored attachments.

##### ParametersExpand Collapse

threadID: string

##### ReturnsExpand Collapse

ThreadDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a thread.

id: string

Identifier of the deleted thread.

deleted: boolean

Indicates that the thread has been deleted.

object: "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.

### Delete ChatKit thread

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI();

const thread = await client.beta.chat_kit.threads.delete('cthr_123');

console.log(thread.id);

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"
