<!-- source: https://developers.openai.com/api/reference/go/resources/files/methods/content/ -->

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

# Retrieve file content

client.Files.Content(ctx, fileID) (\*Response, error)

GET/files/{file\_id}/content

Returns the contents of the specified file.

##### ParametersExpand Collapse

fileID string

##### ReturnsExpand Collapse

type FileContentResponse interface{…}

### Retrieve file content

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
  response, err := client.Files.Content(context.TODO(), "file_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response)

##### Returns Examples
