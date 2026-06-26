<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/methods/create/ -->

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

# Create a new skill.

skills.create(\*\*kwargs) -> [Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills

Create a new skill.

##### ParametersExpand Collapse

files: Array[String] | String

Skill files to upload (directory upload) or a single zip file.

One of the following:

UnionMember0 = Array[String]

Skill files to upload (directory upload) or a single zip file.

String = String

Skill zip file to upload.

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

### Create a new skill.

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

skill = openai.skills.create

puts(skill)

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
