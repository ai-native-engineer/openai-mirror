<!-- source: https://developers.openai.com/api/reference/go/resources/containers/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Containers](/api/reference/go/resources/containers)

[Files](/api/reference/go/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container file

client.Containers.Files.Delete(ctx, containerID, fileID) error

DELETE/containers/{container\_id}/files/{file\_id}

Delete Container File

##### ParametersExpand Collapse

containerID string

fileID string

### Delete a container file

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

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  err := client.Containers.Files.Delete(
    context.TODO(),
    "container_id",
    "file_id",
  if err != nil {
    panic(err.Error())

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file.deleted",
    "deleted": true
