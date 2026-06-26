<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/retrieve/ -->

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

# Retrieve ChatKit thread

[ChatKitThread](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chatkit_thread%20%3E%20(schema)) beta().chatkit().threads().retrieve(ThreadRetrieveParamsparams = ThreadRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chatkit/threads/{thread\_id}

Retrieve a ChatKit thread by its identifier.

##### ParametersExpand Collapse

ThreadRetrieveParams params

Optional<String> threadId

##### ReturnsExpand Collapse

class ChatKitThread:

Represents a ChatKit thread and its current status.

String id

Identifier of the thread.

long createdAt

Unix timestamp (in seconds) for when the thread was created.

formatunixtime

JsonValue; object\_ "chatkit.thread"constant"chatkit.thread"constant

Type discriminator that is always `chatkit.thread`.

Status status

Current status for the thread. Defaults to `active` for newly created threads.

One of the following:

JsonValue;

JsonValue; type "active"constant"active"constant

Status discriminator that is always `active`.

class Locked:

Indicates that a thread is locked and cannot accept new input.

Optional<String> reason

Reason that the thread was locked. Defaults to null when no reason is recorded.

JsonValue; type "locked"constant"locked"constant

Status discriminator that is always `locked`.

class Closed:

Indicates that a thread has been closed.

Optional<String> reason

Reason that the thread was closed. Defaults to null when no reason is recorded.

JsonValue; type "closed"constant"closed"constant

Status discriminator that is always `closed`.

Optional<String> title

Optional human-readable title for the thread. Defaults to null when no title has been generated.

String user

Free-form string that identifies your end user who owns the thread.

### Retrieve ChatKit thread

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
import com.openai.models.beta.chatkit.threads.ChatKitThread;
import com.openai.models.beta.chatkit.threads.ThreadRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatKitThread chatkitThread = client.beta().chatkit().threads().retrieve("cthr_123");

  "id": "cthr_abc123",
  "object": "chatkit.thread",
  "title": "Customer escalation",
  "items": {
    "data": [
        "id": "cthi_user_001",
        "object": "chatkit.thread_item",
        "type": "user_message",
        "content": [
            "type": "input_text",
            "text": "I need help debugging an onboarding issue."
        ],
        "attachments": []
        "id": "cthi_assistant_002",
        "object": "chatkit.thread_item",
        "type": "assistant_message",
        "content": [
            "type": "output_text",
            "text": "Let's start by confirming the workflow version you deployed."
        ]
    ],
    "has_more": false

##### Returns Examples

  "id": "cthr_abc123",
  "object": "chatkit.thread",
  "title": "Customer escalation",
  "items": {
    "data": [
        "id": "cthi_user_001",
        "object": "chatkit.thread_item",
        "type": "user_message",
        "content": [
            "type": "input_text",
            "text": "I need help debugging an onboarding issue."
        ],
        "attachments": []
        "id": "cthi_assistant_002",
        "object": "chatkit.thread_item",
        "type": "assistant_message",
        "content": [
            "type": "output_text",
            "text": "Let's start by confirming the workflow version you deployed."
        ]
    ],
    "has_more": false
