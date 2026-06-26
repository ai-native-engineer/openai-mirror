<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/subresources/versions/methods/create/ -->

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

# Create a new immutable skill version.

skills.versions.create(skill\_id, \*\*kwargs) -> [SkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

POST/skills/{skill\_id}/versions

Create a new immutable skill version.

##### ParametersExpand Collapse

skill\_id: String

default: bool

Whether to set this version as the default.

files: Array[String] | String

Skill files to upload (directory upload) or a single zip file.

One of the following:

UnionMember0 = Array[String]

Skill files to upload (directory upload) or a single zip file.

String = String

Skill zip file to upload.

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

### Create a new immutable skill version.

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

skill_version = openai.skills.versions.create("skill_123")

puts(skill_version)

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
