<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/methods/delete/ -->

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

# Delete thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.Beta.Threads.Delete(ctx, threadID) (\*[ThreadDeleted](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)), error)

DELETE/threads/{thread\_id}

Delete a thread.

##### ParametersExpand Collapse

threadID string

##### ReturnsExpand Collapse

type ThreadDeleted struct{…}

ID string

Deleted bool

Object ThreadDeleted

### Delete thread

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
  threadDeleted, err := client.Beta.Threads.Delete(context.TODO(), "thread_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", threadDeleted.ID)

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
