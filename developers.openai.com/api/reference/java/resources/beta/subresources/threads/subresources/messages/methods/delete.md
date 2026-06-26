<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Threads](/api/reference/java/resources/beta/subresources/threads)

[Messages](/api/reference/java/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

[MessageDeleted](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)) beta().threads().messages().delete(MessageDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### ParametersExpand Collapse

MessageDeleteParams params

String threadId

Optional<String> messageId

##### ReturnsExpand Collapse

class MessageDeleted:

String id

boolean deleted

JsonValue; object\_ "thread.message.deleted"constant"thread.message.deleted"constant

### Delete message

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
import com.openai.models.beta.threads.messages.MessageDeleteParams;
import com.openai.models.beta.threads.messages.MessageDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageDeleteParams params = MessageDeleteParams.builder()
            .threadId("thread_id")
            .messageId("message_id")
            .build();
        MessageDeleted messageDeleted = client.beta().threads().messages().delete(params);

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
