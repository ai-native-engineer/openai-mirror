<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/list/ -->

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

# List ChatKit threads

ThreadListPage beta().chatkit().threads().list(ThreadListParamsparams = ThreadListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chatkit/threads

List ChatKit threads with optional pagination and user filters.

##### ParametersExpand Collapse

ThreadListParams params

Optional<String> after

List items created after this thread item ID. Defaults to null for the first page.

Optional<String> before

List items created before this thread item ID. Defaults to null for the newest results.

Optional<Long> limit

Maximum number of thread items to return. Defaults to 20.

minimum0

maximum100

Optional<[Order](/api/reference/java/resources/beta/subresources/chatkit/subresources/threads/methods/list#(resource)%20beta.chatkit.threads%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for results by creation time. Defaults to `desc`.

ASC("asc")

DESC("desc")

Optional<String> user

Filter threads that belong to this user identifier. Defaults to null to return all users.

minLength1

maxLength512

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

### List ChatKit threads

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
import com.openai.models.beta.chatkit.threads.ThreadListPage;
import com.openai.models.beta.chatkit.threads.ThreadListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadListPage page = client.beta().chatkit().threads().list();

  "data": [
      "id": "cthr_abc123",
      "object": "chatkit.thread",
      "title": "Customer escalation"
      "id": "cthr_def456",
      "object": "chatkit.thread",
      "title": "Demo feedback"
  ],
  "has_more": false,
  "object": "list"

##### Returns Examples

  "data": [
      "id": "cthr_abc123",
      "object": "chatkit.thread",
      "title": "Customer escalation"
      "id": "cthr_def456",
      "object": "chatkit.thread",
      "title": "Demo feedback"
  ],
  "has_more": false,
  "object": "list"
