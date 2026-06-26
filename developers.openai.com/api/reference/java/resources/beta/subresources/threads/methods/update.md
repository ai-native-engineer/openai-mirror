<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Threads](/api/reference/java/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

[Thread](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) beta().threads().update(ThreadUpdateParamsparams = ThreadUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}

Modifies a thread.

##### ParametersExpand Collapse

ThreadUpdateParams params

Optional<String> threadId

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<ToolResources> toolResources

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Optional<CodeInterpreter> codeInterpreter

Optional<List<String>> fileIds

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

Optional<FileSearch> fileSearch

Optional<List<String>> vectorStoreIds

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

##### ReturnsExpand Collapse

class Thread:

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

JsonValue; object\_ "thread"constant"thread"constant

The object type, which is always `thread`.

Optional<ToolResources> toolResources

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Optional<CodeInterpreter> codeInterpreter

Optional<List<String>> fileIds

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

Optional<FileSearch> fileSearch

Optional<List<String>> vectorStoreIds

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

### Modify thread

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
import com.openai.models.beta.threads.Thread;
import com.openai.models.beta.threads.ThreadUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Thread thread = client.beta().threads().update("thread_id");

  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {
    "modified": "true",
    "user": "abc123"
  "tool_resources": {}

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {
    "modified": "true",
    "user": "abc123"
  "tool_resources": {}
