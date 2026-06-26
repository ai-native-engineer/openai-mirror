<!-- source: https://developers.openai.com/api/reference/ruby/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Chat](/api/reference/ruby/resources/chat)

[Completions](/api/reference/ruby/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

chat.completions.delete(completion\_id) -> [ChatCompletionDeleted](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### ParametersExpand Collapse

completion\_id: String

##### ReturnsExpand Collapse

class ChatCompletionDeleted { id, deleted, object }

id: String

The ID of the chat completion that was deleted.

deleted: bool

Whether the chat completion was deleted.

object: :"chat.completion.deleted"

The type of object being deleted.

### Delete chat completion

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

chat_completion_deleted = openai.chat.completions.delete("completion_id")

puts(chat_completion_deleted)

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
