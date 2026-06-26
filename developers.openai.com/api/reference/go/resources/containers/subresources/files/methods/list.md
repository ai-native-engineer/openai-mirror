<!-- source: https://developers.openai.com/api/reference/go/resources/containers/subresources/files/methods/list/ -->

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

# List container files

client.Containers.Files.List(ctx, containerID, query) (\*CursorPage[[ContainerFileListResponse](/api/reference/go/resources/containers#(resource)%20containers.files%20%3E%20(model)%20ContainerFileListResponse%20%3E%20(schema))], error)

GET/containers/{container\_id}/files

List Container files

##### ParametersExpand Collapse

containerID string

query ContainerFileListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Order param.Field[[ContainerFileListParamsOrder](/api/reference/go/resources/containers/subresources/files/methods/list#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const ContainerFileListParamsOrderAsc [ContainerFileListParamsOrder](/api/reference/go/resources/containers/subresources/files/methods/list#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const ContainerFileListParamsOrderDesc [ContainerFileListParamsOrder](/api/reference/go/resources/containers/subresources/files/methods/list#(resource)%20containers.files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type ContainerFileListResponse struct{…}

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

### List container files

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
  page, err := client.Containers.Files.List(
    context.TODO(),
    "container_id",
    openai.ContainerFileListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
            "object": "container.file",
            "created_at": 1747848842,
            "bytes": 880,
            "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
            "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
            "source": "user"
    ],
    "first_id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "has_more": false,
    "last_id": "cfile_682e0e8a43c88191a7978f477a09bdf5"

##### Returns Examples

    "object": "list",
    "data": [
            "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
            "object": "container.file",
            "created_at": 1747848842,
            "bytes": 880,
            "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
            "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
            "source": "user"
    ],
    "first_id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "has_more": false,
    "last_id": "cfile_682e0e8a43c88191a7978f477a09bdf5"
