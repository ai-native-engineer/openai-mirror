<!-- source: https://developers.openai.com/api/reference/go/resources/skills/methods/create/ -->

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

# Create a new skill.

client.Skills.New(ctx, body) (\*[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)), error)

POST/skills

Create a new skill.

##### ParametersExpand Collapse

body SkillNewParams

Files param.Field[[SkillNewParamsFilesUnion](/api/reference/go/resources/skills/methods/create#(resource)%20skills%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20files%20%3E%20(schema))]Optional

Skill files to upload (directory upload) or a single zip file.

type SkillNewParamsFilesArray []Reader

Skill files to upload (directory upload) or a single zip file.

Reader

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

### Create a new skill.

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
  skill, err := client.Skills.New(context.TODO(), openai.SkillNewParams{

  })
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
