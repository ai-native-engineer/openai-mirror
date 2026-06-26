<!-- source: https://developers.openai.com/api/reference/go/resources/skills/methods/update/ -->

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

# Update the default version pointer for a skill.

client.Skills.Update(ctx, skillID, body) (\*[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)), error)

POST/skills/{skill\_id}

Update the default version pointer for a skill.

##### ParametersExpand Collapse

skillID string

body SkillUpdateParams

DefaultVersion param.Field[string]

The skill version number to set as default.

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

### Update the default version pointer for a skill.

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
  skill, err := client.Skills.Update(
    context.TODO(),
    "skill_123",
    openai.SkillUpdateParams{
      DefaultVersion: "default_version",
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
