<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/subresources/files/methods/content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

[Files](/api/reference/go/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve vector store file content

client.VectorStores.Files.Content(ctx, vectorStoreID, fileID) (\*Page[[VectorStoreFileContentResponse](/api/reference/go/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20VectorStoreFileContentResponse%20%3E%20(schema))], error)

GET/vector\_stores/{vector\_store\_id}/files/{file\_id}/content

Retrieve the parsed contents of a vector store file.

##### ParametersExpand Collapse

vectorStoreID string

fileID string

##### ReturnsExpand Collapse

type VectorStoreFileContentResponse struct{…}

Text stringOptional

The text content

Type stringOptional

The content type (currently only `"text"`)

### Retrieve vector store file content

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
  page, err := client.VectorStores.Files.Content(
    context.TODO(),
    "vs_abc123",
    "file-abc123",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "file_id": "file-abc123",
  "filename": "example.txt",
  "attributes": {"key": "value"},
  "content": [
    {"type": "text", "text": "..."},
    ...
  ]

##### Returns Examples

  "file_id": "file-abc123",
  "filename": "example.txt",
  "attributes": {"key": "value"},
  "content": [
    {"type": "text", "text": "..."},
    ...
  ]
