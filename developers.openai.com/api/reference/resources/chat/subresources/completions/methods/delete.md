<!-- source: https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Chat](/api/reference/resources/chat)

[Completions](/api/reference/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### Path ParametersExpand Collapse

completion\_id: string

##### ReturnsExpand Collapse

ChatCompletionDeleted object { id, deleted, object }

id: string

The ID of the chat completion that was deleted.

deleted: boolean

Whether the chat completion was deleted.

object: "chat.completion.deleted"

The type of object being deleted.

### Delete chat completion

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/chat/completions/chat_abc123 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json"

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
