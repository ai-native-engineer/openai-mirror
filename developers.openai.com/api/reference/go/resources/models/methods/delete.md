<!-- source: https://developers.openai.com/api/reference/go/resources/models/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Models](/api/reference/go/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a fine-tuned model

client.Models.Delete(ctx, model) (\*[ModelDeleted](/api/reference/go/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)), error)

DELETE/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### ParametersExpand Collapse

model string

##### ReturnsExpand Collapse

type ModelDeleted struct{…}

ID string

Deleted bool

Object string

### Delete a fine-tuned model

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
  modelDeleted, err := client.Models.Delete(context.TODO(), "ft:gpt-4o-mini:acemeco:suffix:abc123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", modelDeleted.ID)

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true

##### Returns Examples

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
