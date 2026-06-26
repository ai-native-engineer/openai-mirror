<!-- source: https://developers.openai.com/api/reference/python/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Chat](/api/reference/python/resources/chat)

[Completions](/api/reference/python/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

chat.completions.delete(strcompletion\_id)  -> [ChatCompletionDeleted](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema))

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### ParametersExpand Collapse

completion\_id: str

##### ReturnsExpand Collapse

class ChatCompletionDeleted: …

id: str

The ID of the chat completion that was deleted.

deleted: bool

Whether the chat completion was deleted.

object: Literal["chat.completion.deleted"]

The type of object being deleted.

### Delete chat completion

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

completions = client.chat.completions.list()
first_id = completions[0].id
delete_response = client.chat.completions.delete(completion_id=first_id)
print(delete_response)

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
