<!-- source: https://developers.openai.com/api/reference/go/resources/skills/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Skills](/api/reference/go/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get a skill by its ID.

client.Skills.Get(ctx, skillID) (\*[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)), error)

GET/skills/{skill\_id}

Get a skill by its ID.

##### ParametersExpand Collapse

skillID string

##### ReturnsExpand Collapse

type Skill struct{…}

ID string

Unique identifier for the skill.

CreatedAt int64

Unix timestamp (seconds) for when the skill was created.

formatunixtime

DefaultVersion string

Default version for the skill.

Description string

Description of the skill.

LatestVersion string

Latest version for the skill.

Name string

Name of the skill.

Object Skill

The object type, which is `skill`.

### Get a skill by its ID.

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
  skill, err := client.Skills.Get(context.TODO(), "skill_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", skill.ID)

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"
