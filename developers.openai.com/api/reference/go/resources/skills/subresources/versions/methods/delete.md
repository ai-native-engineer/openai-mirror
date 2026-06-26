<!-- source: https://developers.openai.com/api/reference/go/resources/skills/subresources/versions/methods/delete/ -->

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

# Delete a skill version.

client.Skills.Versions.Delete(ctx, skillID, version) (\*[DeletedSkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)), error)

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### ParametersExpand Collapse

skillID string

version string

The skill version number.

##### ReturnsExpand Collapse

type DeletedSkillVersion struct{…}

ID string

Deleted bool

Object SkillVersionDeleted

Version string

The deleted skill version.

### Delete a skill version.

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
  deletedSkillVersion, err := client.Skills.Versions.Delete(
    context.TODO(),
    "skill_123",
    "version",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", deletedSkillVersion.ID)

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.version.deleted",
  "version": "version"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.version.deleted",
  "version": "version"
