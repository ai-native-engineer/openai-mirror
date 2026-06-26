<!-- source: https://developers.openai.com/api/reference/go/resources/skills/methods/delete/ -->

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

# Delete a skill by its ID.

client.Skills.Delete(ctx, skillID) (\*[DeletedSkill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)), error)

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### ParametersExpand Collapse

skillID string

##### ReturnsExpand Collapse

type DeletedSkill struct{…}

ID string

Deleted bool

Object SkillDeleted

### Delete a skill by its ID.

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
  deletedSkill, err := client.Skills.Delete(context.TODO(), "skill_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", deletedSkill.ID)

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
