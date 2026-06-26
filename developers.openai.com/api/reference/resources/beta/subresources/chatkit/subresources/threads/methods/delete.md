<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Threads](/api/reference/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete ChatKit thread

DELETE/chatkit/threads/{thread\_id}

Delete a ChatKit thread along with its items and stored attachments.

##### Path ParametersExpand Collapse

thread\_id: string

##### ReturnsExpand Collapse

id: string

Identifier of the deleted thread.

deleted: boolean

Indicates that the thread has been deleted.

object: "chatkit.thread.deleted"

Type discriminator that is always `chatkit.thread.deleted`.

### Delete ChatKit thread

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/chatkit/threads/$THREAD_ID \
    -X DELETE \
    -H 'OpenAI-Beta: chatkit_beta=v1' \
    -H "Authorization: Bearer $OPENAI_API_KEY"

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"
