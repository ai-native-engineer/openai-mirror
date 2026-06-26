<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/subresources/versions/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Skills](/api/reference/ruby/resources/skills)

[Versions](/api/reference/ruby/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List skill versions for a skill.

skills.versions.list(skill\_id, \*\*kwargs) -> CursorPage<[SkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more } >

GET/skills/{skill\_id}/versions

List skill versions for a skill.

##### ParametersExpand Collapse

skill\_id: String

after: String

The skill version ID to start after.

limit: Integer

Number of versions to retrieve.

minimum0

maximum100

order: :asc | :desc

Sort order of results by version number.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class SkillVersion { id, created\_at, description, 4 more }

id: String

Unique identifier for the skill version.

created\_at: Integer

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: String

Description of the skill version.

name: String

Name of the skill version.

object: :"skill.version"

The object type, which is `skill.version`.

skill\_id: String

Identifier of the skill for this version.

version: String

Version number for this skill.

### List skill versions for a skill.

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

page = openai.skills.versions.list("skill_123")

puts(page)

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
