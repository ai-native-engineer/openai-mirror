<!-- source: https://developers.openai.com/api/reference/go/resources/models/methods/list/ -->

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

# List models

client.Models.List(ctx) (\*Page[[Model](/api/reference/go/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema))], error)

GET/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

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

### List models

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
  page, err := client.Models.List(context.TODO())
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
      "id": "model-id-1",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner",
      "id": "model-id-2",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
  ]

##### Returns Examples

  "object": "list",
  "data": [
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
      "id": "model-id-1",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner",
      "id": "model-id-2",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
  ]
