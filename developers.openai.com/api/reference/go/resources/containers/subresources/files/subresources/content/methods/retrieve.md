<!-- source: https://developers.openai.com/api/reference/go/resources/containers/subresources/files/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Containers](/api/reference/go/resources/containers)

[Files](/api/reference/go/resources/containers/subresources/files)

[Content](/api/reference/go/resources/containers/subresources/files/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve container file content

client.Containers.Files.Content.Get(ctx, containerID, fileID) (\*Response, error)

GET/containers/{container\_id}/files/{file\_id}/content

Retrieve Container File Content

##### ParametersExpand Collapse

containerID string

fileID string

##### ReturnsExpand Collapse

type ContainerFileContentGetResponse interface{…}

### Retrieve container file content

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
  content, err := client.Containers.Files.Content.Get(
    context.TODO(),
    "container_id",
    "file_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", content)

<binary content of the file>

##### Returns Examples

<binary content of the file>
