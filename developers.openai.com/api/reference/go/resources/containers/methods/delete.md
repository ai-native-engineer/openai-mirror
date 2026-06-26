<!-- source: https://developers.openai.com/api/reference/go/resources/containers/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Containers](/api/reference/go/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container

client.Containers.Delete(ctx, containerID) error

DELETE/containers/{container\_id}

Delete Container

##### ParametersExpand Collapse

containerID string

### Delete a container

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
  err := client.Containers.Delete(context.TODO(), "container_id")
  if err != nil {
    panic(err.Error())

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container.deleted",
    "deleted": true

##### Returns Examples

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container.deleted",
    "deleted": true
