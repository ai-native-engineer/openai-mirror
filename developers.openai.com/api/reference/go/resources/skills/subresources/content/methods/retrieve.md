<!-- source: https://developers.openai.com/api/reference/go/resources/skills/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Skills](/api/reference/go/resources/skills)

[Content](/api/reference/go/resources/skills/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill zip bundle by its ID.

client.Skills.Content.Get(ctx, skillID) (\*Response, error)

GET/skills/{skill\_id}/content

Download a skill zip bundle by its ID.

##### ParametersExpand Collapse

skillID string

##### ReturnsExpand Collapse

type SkillContentGetResponse interface{…}

### Download a skill zip bundle by its ID.

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
  content, err := client.Skills.Content.Get(context.TODO(), "skill_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", content)

##### Returns Examples
