<!-- source: https://developers.openai.com/api/reference/go/resources/videos/methods/get_character/ -->

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

# Fetch a character.

client.Videos.GetCharacter(ctx, characterID) (\*[VideoGetCharacterResponse](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoGetCharacterResponse%20%3E%20(schema)), error)

GET/videos/characters/{character\_id}

Fetch a character.

##### ParametersExpand Collapse

characterID string

##### ReturnsExpand Collapse

type VideoGetCharacterResponse struct{…}

ID string

Identifier for the character creation cameo.

CreatedAt int64

Unix timestamp (in seconds) when the character was created.

formatunixtime

Name string

Display name for the character.

### Fetch a character.

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
  response, err := client.Videos.GetCharacter(context.TODO(), "char_123")
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
