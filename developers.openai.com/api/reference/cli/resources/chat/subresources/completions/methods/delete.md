<!-- source: https://developers.openai.com/api/reference/cli/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Chat](/api/reference/cli/resources/chat)

[Completions](/api/reference/cli/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

$ openai chat:completions delete

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### ParametersExpand Collapse

--completion-id: string

The ID of the chat completion to delete.

##### ReturnsExpand Collapse

chat\_completion\_deleted: object { id, deleted, object }

id: string

The ID of the chat completion that was deleted.

deleted: boolean

Whether the chat completion was deleted.

object: "chat.completion.deleted"

The type of object being deleted.

### Delete chat completion

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai chat:completions delete \
  --api-key 'My API Key' \
  --completion-id completion_id

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
