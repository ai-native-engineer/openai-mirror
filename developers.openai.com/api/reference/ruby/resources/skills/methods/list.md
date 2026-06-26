<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Skills](/api/reference/ruby/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List all skills for the current project.

skills.list(\*\*kwargs) -> CursorPage<[Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more } >

GET/skills

List all skills for the current project.

##### ParametersExpand Collapse

after: String

Identifier for the last item from the previous pagination request

limit: Integer

Number of items to retrieve

minimum0

maximum100

order: :asc | :desc

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class Skill { id, created\_at, default\_version, 4 more }

id: String

Unique identifier for the skill.

created\_at: Integer

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: String

Default version for the skill.

description: String

Description of the skill.

latest\_version: String

Latest version for the skill.

name: String

Name of the skill.

object: :skill

The object type, which is `skill`.

### List all skills for the current project.

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.skills.list

puts(page)

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
