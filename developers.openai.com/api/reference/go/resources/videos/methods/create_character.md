<!-- source: https://developers.openai.com/api/reference/go/resources/videos/methods/create_character/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Videos](/api/reference/go/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a character from an uploaded video.

client.Videos.NewCharacter(ctx, body) (\*[VideoNewCharacterResponse](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoNewCharacterResponse%20%3E%20(schema)), error)

POST/videos/characters

Create a character from an uploaded video.

##### ParametersExpand Collapse

body VideoNewCharacterParams

Name param.Field[string]

Display name for this API character.

maxLength80

minLength1

Video param.Field[[Reader](/api/reference/go/resources/videos/methods/create_character#(resource)%20videos%20%3E%20(method)%20create_character%20%3E%20(params)%20default%20%3E%20(param)%20video%20%3E%20(schema))]

Video file used to create a character.

##### ReturnsExpand Collapse

type VideoNewCharacterResponse struct{…}

ID string

Identifier for the character creation cameo.

CreatedAt int64

Unix timestamp (in seconds) when the character was created.

formatunixtime

Name string

Display name for the character.

### Create a character from an uploaded video.

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
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  response, err := client.Videos.NewCharacter(context.TODO(), openai.VideoNewCharacterParams{
    Name: "x",
    Video: io.Reader(bytes.NewBuffer([]byte("Example data"))),
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response.ID)

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
