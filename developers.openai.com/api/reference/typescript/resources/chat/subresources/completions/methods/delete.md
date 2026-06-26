<!-- source: https://developers.openai.com/api/reference/typescript/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Chat](/api/reference/typescript/resources/chat)

[Completions](/api/reference/typescript/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

client.chat.completions.delete(stringcompletionID, RequestOptionsoptions?): [ChatCompletionDeleted](/api/reference/typescript/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### ParametersExpand Collapse

completionID: string

##### ReturnsExpand Collapse

ChatCompletionDeleted { id, deleted, object }

id: string

The ID of the chat completion that was deleted.

deleted: boolean

Whether the chat completion was deleted.

object: "chat.completion.deleted"

The type of object being deleted.

### Delete chat completion

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

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const chatCompletionDeleted = await client.chat.completions.delete('completion_id');

console.log(chatCompletionDeleted.id);

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
