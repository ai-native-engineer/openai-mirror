<!-- source: https://developers.openai.com/api/reference/go/resources/containers/subresources/files/methods/retrieve/ -->

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

# Retrieve container file

client.Containers.Files.Get(ctx, containerID, fileID) (\*[ContainerFileGetResponse](/api/reference/go/resources/containers#(resource)%20containers.files%20%3E%20(model)%20ContainerFileGetResponse%20%3E%20(schema)), error)

GET/containers/{container\_id}/files/{file\_id}

Retrieve Container File

##### ParametersExpand Collapse

containerID string

fileID string

##### ReturnsExpand Collapse

type ContainerFileGetResponse struct{…}

ID string

Unique identifier for the file.

Bytes int64

Size of the file in bytes.

ContainerID string

The container this file belongs to.

CreatedAt int64

Unix timestamp (in seconds) when the file was created.

formatunixtime

Object ContainerFile

The type of this object (`container.file`).

Path string

Path of the file in the container.

Source string

Source of the file (e.g., `user`, `assistant`).

### Retrieve container file

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
  file, err := client.Containers.Files.Get(
    context.TODO(),
    "container_id",
    "file_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", file.ID)

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file",
    "created_at": 1747848842,
    "bytes": 880,
    "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
    "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
    "source": "user"

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file",
    "created_at": 1747848842,
    "bytes": 880,
    "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
    "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
    "source": "user"
