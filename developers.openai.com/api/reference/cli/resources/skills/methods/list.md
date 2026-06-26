<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Skills](/api/reference/cli/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List all skills for the current project.

$ openai skills list

GET/skills

List all skills for the current project.

##### ParametersExpand Collapse

--after: optional string

Identifier for the last item from the previous pagination request

--limit: optional number

Number of items to retrieve

--order: optional "asc" or "desc"

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

##### ReturnsExpand Collapse

skill\_list: object { data, first\_id, has\_more, 2 more }

data: array of [Skill](/api/reference/cli/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

A list of items

id: string

Unique identifier for the skill.

created\_at: number

Unix timestamp (seconds) for when the skill was created.

default\_version: string

Default version for the skill.

description: string

Description of the skill.

latest\_version: string

Latest version for the skill.

name: string

Name of the skill.

object: "skill"

The object type, which is `skill`.

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

### List all skills for the current project.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills list \
  --api-key 'My API Key'

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
