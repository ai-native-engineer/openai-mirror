<!-- source: https://developers.openai.com/api/reference/go/resources/skills/subresources/versions/methods/retrieve/ -->

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

# Get a specific skill version.

client.Skills.Versions.Get(ctx, skillID, version) (\*[SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)), error)

GET/skills/{skill\_id}/versions/{version}

Get a specific skill version.

##### ParametersExpand Collapse

skillID string

version string

The version number to retrieve.

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

### Get a specific skill version.

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
  skillVersion, err := client.Skills.Versions.Get(
    context.TODO(),
    "skill_123",
    "version",
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
