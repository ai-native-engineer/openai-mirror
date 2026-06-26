<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Threads](/api/reference/go/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.Beta.Threads.Update(ctx, threadID, body) (\*[Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)), error)

POST/threads/{thread\_id}

Modifies a thread.

##### ParametersExpand Collapse

threadID string

body BetaThreadUpdateParams

Metadata param.Field[[Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

ToolResources param.Field[[BetaThreadUpdateParamsToolResources](/api/reference/go/resources/beta/subresources/threads/methods/update#(resource)%20beta.threads%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20tool_resources%20%3E%20(schema))]Optional

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

CodeInterpreter BetaThreadUpdateParamsToolResourcesCodeInterpreterOptional

FileIDs []stringOptional

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

FileSearch BetaThreadUpdateParamsToolResourcesFileSearchOptional

VectorStoreIDs []stringOptional

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

##### ReturnsExpand Collapse

type Thread struct{…}

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Object Thread

The object type, which is always `thread`.

ToolResources ThreadToolResources

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

CodeInterpreter ThreadToolResourcesCodeInterpreterOptional

FileIDs []stringOptional

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

FileSearch ThreadToolResourcesFileSearchOptional

VectorStoreIDs []stringOptional

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

### Modify thread

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  thread, err := client.Beta.Threads.Update(
    context.TODO(),
    "thread_id",
    openai.BetaThreadUpdateParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", thread.ID)

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
