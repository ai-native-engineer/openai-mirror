<!-- source: https://developers.openai.com/api/reference/go/resources/skills/subresources/versions/methods/list/ -->

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

# List skill versions for a skill.

client.Skills.Versions.List(ctx, skillID, query) (\*CursorPage[[SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))], error)

GET/skills/{skill\_id}/versions

List skill versions for a skill.

##### ParametersExpand Collapse

skillID string

query SkillVersionListParams

After param.Field[string]Optional

The skill version ID to start after.

Limit param.Field[int64]Optional

Number of versions to retrieve.

minimum0

maximum100

Order param.Field[[SkillVersionListParamsOrder](/api/reference/go/resources/skills/subresources/versions/methods/list#(resource)%20skills.versions%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order of results by version number.

const SkillVersionListParamsOrderAsc [SkillVersionListParamsOrder](/api/reference/go/resources/skills/subresources/versions/methods/list#(resource)%20skills.versions%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const SkillVersionListParamsOrderDesc [SkillVersionListParamsOrder](/api/reference/go/resources/skills/subresources/versions/methods/list#(resource)%20skills.versions%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

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

### List skill versions for a skill.

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
  page, err := client.Skills.Versions.List(
    context.TODO(),
    "skill_123",
    openai.SkillVersionListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "description": "description",
      "name": "name",
      "object": "skill.version",
      "skill_id": "skill_id",
      "version": "version"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

##### Returns Examples

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "description": "description",
      "name": "name",
      "object": "skill.version",
      "skill_id": "skill_id",
      "version": "version"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
