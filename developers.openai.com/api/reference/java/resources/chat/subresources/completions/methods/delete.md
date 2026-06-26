<!-- source: https://developers.openai.com/api/reference/java/resources/chat/subresources/completions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Chat](/api/reference/java/resources/chat)

[Completions](/api/reference/java/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete chat completion

[ChatCompletionDeleted](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)) chat().completions().delete(ChatCompletionDeleteParamsparams = ChatCompletionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/chat/completions/{completion\_id}

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

##### ParametersExpand Collapse

ChatCompletionDeleteParams params

Optional<String> completionId

##### ReturnsExpand Collapse

class ChatCompletionDeleted:

String id

The ID of the chat completion that was deleted.

boolean deleted

Whether the chat completion was deleted.

JsonValue; object\_ "chat.completion.deleted"constant"chat.completion.deleted"constant

The type of object being deleted.

### Delete chat completion

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
import com.openai.models.chat.completions.ChatCompletionDeleteParams;
import com.openai.models.chat.completions.ChatCompletionDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletionDeleted chatCompletionDeleted = client.chat().completions().delete("completion_id");

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true

##### Returns Examples

  "object": "chat.completion.deleted",
  "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "deleted": true
