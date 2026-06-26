<!-- source: https://developers.openai.com/api/reference/go/resources/skills/methods/list/ -->

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

# List all skills for the current project.

client.Skills.List(ctx, query) (\*CursorPage[[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))], error)

GET/skills

List all skills for the current project.

##### ParametersExpand Collapse

query SkillListParams

After param.Field[string]Optional

Identifier for the last item from the previous pagination request

Limit param.Field[int64]Optional

Number of items to retrieve

minimum0

maximum100

Order param.Field[[SkillListParamsOrder](/api/reference/go/resources/skills/methods/list#(resource)%20skills%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

const SkillListParamsOrderAsc [SkillListParamsOrder](/api/reference/go/resources/skills/methods/list#(resource)%20skills%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const SkillListParamsOrderDesc [SkillListParamsOrder](/api/reference/go/resources/skills/methods/list#(resource)%20skills%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

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

### List all skills for the current project.

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
  page, err := client.Skills.List(context.TODO(), openai.SkillListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
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
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
