<!-- source: https://developers.openai.com/api/reference/java/resources/conversations/subresources/items/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Conversations](/api/reference/java/resources/conversations)

[Items](/api/reference/java/resources/conversations/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an item

[Conversation](/api/reference/java/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema)) conversations().items().delete(ItemDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/conversations/{conversation\_id}/items/{item\_id}

Delete an item from a conversation with the given IDs.

##### ParametersExpand Collapse

ItemDeleteParams params

String conversationId

Optional<String> itemId

##### ReturnsExpand Collapse

class Conversation:

String id

The unique ID of the conversation.

long createdAt

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

JsonValue metadata

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

JsonValue; object\_ "conversation"constant"conversation"constant

The object type, which is always `conversation`.

### Delete an item

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
import com.openai.models.conversations.Conversation;
import com.openai.models.conversations.items.ItemDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemDeleteParams params = ItemDeleteParams.builder()
            .conversationId("conv_123")
            .itemId("msg_abc")
            .build();
        Conversation conversation = client.conversations().items().delete(params);

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
