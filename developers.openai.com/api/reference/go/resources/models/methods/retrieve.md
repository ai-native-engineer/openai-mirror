<!-- source: https://developers.openai.com/api/reference/go/resources/models/methods/retrieve/ -->

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

# Retrieve model

client.Models.Get(ctx, model) (\*[Model](/api/reference/go/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)), error)

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### ParametersExpand Collapse

model string

##### ReturnsExpand Collapse

type Model struct{…}

Describes an OpenAI model offering that can be used with the API.

ID string

The model identifier, which can be referenced in the API endpoints.

Created int64

The Unix timestamp (in seconds) when the model was created.

formatunixtime

Object Model

The object type, which is always “model”.

OwnedBy string

The organization that owns the model.

### Retrieve model

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
  model, err := client.Models.Get(context.TODO(), "gpt-4o-mini")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", model.ID)

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
