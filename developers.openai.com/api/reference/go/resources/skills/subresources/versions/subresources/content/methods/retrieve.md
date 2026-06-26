<!-- source: https://developers.openai.com/api/reference/go/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Skills](/api/reference/go/resources/skills)

[Versions](/api/reference/go/resources/skills/subresources/versions)

[Content](/api/reference/go/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

client.Skills.Versions.Content.Get(ctx, skillID, version) (\*Response, error)

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### ParametersExpand Collapse

skillID string

version string

The skill version number.

##### ReturnsExpand Collapse

type SkillVersionContentGetResponse interface{…}

### Download a skill version zip bundle.

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
  content, err := client.Skills.Versions.Content.Get(
    context.TODO(),
    "skill_123",
    "version",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", content)

##### Returns Examples
