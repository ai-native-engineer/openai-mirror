<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/chatkit/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[ChatKit](/api/reference/cli/resources/beta/subresources/chatkit)

[Threads](/api/reference/cli/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete ChatKit thread

$ openai beta:chatkit:threads delete

DELETE/chatkit/threads/{thread\_id}

Delete a ChatKit thread along with its items and stored attachments.

##### ParametersExpand Collapse

--thread-id: string

Identifier of the ChatKit thread to delete.

##### ReturnsExpand Collapse

BetaChatKitThreadDeleteResponse: object { id, deleted, object }

Confirmation payload returned after deleting a thread.

id: string

Identifier of the deleted thread.

deleted: boolean

Indicates that the thread has been deleted.

object: "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.

### Delete ChatKit thread

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:chatkit:threads delete \
  --api-key 'My API Key' \
  --thread-id cthr_123

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"
