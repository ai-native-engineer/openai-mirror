<!-- source: https://developers.openai.com/api/reference/go/resources/containers/subresources/files/methods/create/ -->

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

# Create container file

client.Containers.Files.New(ctx, containerID, body) (\*[ContainerFileNewResponse](/api/reference/go/resources/containers#(resource)%20containers.files%20%3E%20(model)%20ContainerFileNewResponse%20%3E%20(schema)), error)

POST/containers/{container\_id}/files

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

##### ParametersExpand Collapse

containerID string

body ContainerFileNewParams

File param.Field[[Reader](/api/reference/go/resources/containers/subresources/files/methods/create#(resource)%20containers.files%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20file%20%3E%20(schema))]Optional

The File object (not file name) to be uploaded.

FileID param.Field[string]Optional

Name of the file to create.

##### ReturnsExpand Collapse

type ContainerFileNewResponse struct{…}

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

### Create container file

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
  file, err := client.Containers.Files.New(
    context.TODO(),
    "container_id",
    openai.ContainerFileNewParams{

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
