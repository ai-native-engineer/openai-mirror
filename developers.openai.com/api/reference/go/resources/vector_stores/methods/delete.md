<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

client.VectorStores.Delete(ctx, vectorStoreID) (\*[VectorStoreDeleted](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)), error)

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### ParametersExpand Collapse

vectorStoreID string

##### ReturnsExpand Collapse

type VectorStoreDeleted struct{…}

ID string

Deleted bool

Object VectorStoreDeleted

### Delete vector store

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
  vectorStoreDeleted, err := client.VectorStores.Delete(context.TODO(), "vector_store_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", vectorStoreDeleted.ID)

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
