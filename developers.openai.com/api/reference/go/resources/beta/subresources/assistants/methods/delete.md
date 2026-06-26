<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/assistants/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Assistants](/api/reference/go/resources/beta/subresources/assistants)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete assistant

Deprecated

client.Beta.Assistants.Delete(ctx, assistantID) (\*[AssistantDeleted](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)), error)

DELETE/assistants/{assistant\_id}

Delete an assistant.

##### ParametersExpand Collapse

assistantID string

##### ReturnsExpand Collapse

type AssistantDeleted struct{…}

ID string

Deleted bool

Object AssistantDeleted

### Delete assistant

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
  assistantDeleted, err := client.Beta.Assistants.Delete(context.TODO(), "assistant_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", assistantDeleted.ID)

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true

##### Returns Examples

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true
