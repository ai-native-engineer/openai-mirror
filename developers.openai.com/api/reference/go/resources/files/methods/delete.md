<!-- source: https://developers.openai.com/api/reference/go/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Files](/api/reference/go/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

client.Files.Delete(ctx, fileID) (\*[FileDeleted](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)), error)

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### ParametersExpand Collapse

fileID string

##### ReturnsExpand Collapse

type FileDeleted struct{…}

ID string

Deleted bool

Object File

### Delete file

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
  fileDeleted, err := client.Files.Delete(context.TODO(), "file_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", fileDeleted.ID)

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true
