<!-- source: https://developers.openai.com/api/reference/go/resources/skills/subresources/versions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Skills](/api/reference/go/resources/skills)

[Versions](/api/reference/go/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a new immutable skill version.

client.Skills.Versions.New(ctx, skillID, body) (\*[SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)), error)

POST/skills/{skill\_id}/versions

Create a new immutable skill version.

##### ParametersExpand Collapse

skillID string

body SkillVersionNewParams

Default param.Field[bool]Optional

Whether to set this version as the default.

Files param.Field[[SkillVersionNewParamsFilesUnion](/api/reference/go/resources/skills/subresources/versions/methods/create#(resource)%20skills.versions%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20files%20%3E%20(schema))]Optional

Skill files to upload (directory upload) or a single zip file.

type SkillVersionNewParamsFilesArray []Reader

Skill files to upload (directory upload) or a single zip file.

Reader

##### ReturnsExpand Collapse

type SkillVersion struct{…}

ID string

Unique identifier for the skill version.

CreatedAt int64

Unix timestamp (seconds) for when the version was created.

formatunixtime

Description string

Description of the skill version.

Name string

Name of the skill version.

Object SkillVersion

The object type, which is `skill.version`.

SkillID string

Identifier of the skill for this version.

Version string

Version number for this skill.

### Create a new immutable skill version.

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
  skillVersion, err := client.Skills.Versions.New(
    context.TODO(),
    "skill_123",
    openai.SkillVersionNewParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", skillVersion.ID)

200 example

  "id": "id",
  "created_at": 0,
  "description": "description",
  "name": "name",
  "object": "skill.version",
  "skill_id": "skill_id",
  "version": "version"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "description": "description",
  "name": "name",
  "object": "skill.version",
  "skill_id": "skill_id",
  "version": "version"
