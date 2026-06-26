<!-- source: https://developers.openai.com/api/reference/java/resources/conversations/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Conversations](/api/reference/java/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a conversation

[ConversationDeletedResource](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation_deleted_resource%20%3E%20(schema)) conversations().delete(ConversationDeleteParamsparams = ConversationDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/conversations/{conversation\_id}

Delete a conversation. Items in the conversation will not be deleted.

##### ParametersExpand Collapse

ConversationDeleteParams params

Optional<String> conversationId

##### ReturnsExpand Collapse

class ConversationDeletedResource:

String id

boolean deleted

JsonValue; object\_ "conversation.deleted"constant"conversation.deleted"constant

### Delete a conversation

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
import com.openai.models.conversations.ConversationDeleteParams;
import com.openai.models.conversations.ConversationDeletedResource;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ConversationDeletedResource conversationDeletedResource = client.conversations().delete("conv_123");

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true

##### Returns Examples

  "id": "conv_123",
  "object": "conversation.deleted",
  "deleted": true
