<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/chatkit/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[ChatKit](/api/reference/python/resources/beta/subresources/chatkit)

[Threads](/api/reference/python/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete ChatKit thread

beta.chatkit.threads.delete(strthread\_id)  -> [ThreadDeleteResponse](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20thread_delete_response%20%3E%20(schema))

DELETE/chatkit/threads/{thread\_id}

Delete a ChatKit thread along with its items and stored attachments.

##### ParametersExpand Collapse

thread\_id: str

##### ReturnsExpand Collapse

class ThreadDeleteResponse: …

Confirmation payload returned after deleting a thread.

id: str

Identifier of the deleted thread.

deleted: bool

Indicates that the thread has been deleted.

object: Literal["chatkit.thread.deleted"]

Type discriminator that is always `chatkit.thread.deleted`.

### Delete ChatKit thread

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
thread = client.beta.chat_kit.threads.delete(
    "cthr_123",
print(thread.id)

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"
