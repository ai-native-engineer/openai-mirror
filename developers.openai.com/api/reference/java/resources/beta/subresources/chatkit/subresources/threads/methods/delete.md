<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[ChatKit](/api/reference/java/resources/beta/subresources/chatkit)

[Threads](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete ChatKit thread

[ThreadDeleteResponse](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20ThreadDeleteResponse%20%3E%20(schema)) beta().chatkit().threads().delete(ThreadDeleteParamsparams = ThreadDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/chatkit/threads/{thread\_id}

Delete a ChatKit thread along with its items and stored attachments.

##### ParametersExpand Collapse

ThreadDeleteParams params

Optional<String> threadId

##### ReturnsExpand Collapse

class ThreadDeleteResponse:

Confirmation payload returned after deleting a thread.

String id

Identifier of the deleted thread.

boolean deleted

Indicates that the thread has been deleted.

JsonValue; object\_ "chatkit.thread.deleted"constant"chatkit.thread.deleted"constant

Type discriminator that is always `chatkit.thread.deleted`.

### Delete ChatKit thread

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chat_kit.threads.ThreadDeleteParams;
import com.openai.models.beta.chat_kit.threads.ThreadDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadDeleteResponse thread = client.beta().chat_kit().threads().delete("cthr_123");

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "chatkit.thread.deleted"
