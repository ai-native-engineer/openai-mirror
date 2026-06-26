<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/subresources/versions/methods/delete/ -->

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

# Delete a skill version.

skills.versions.delete(version, \*\*kwargs) -> [DeletedSkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)) { id, deleted, object, version }

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### ParametersExpand Collapse

skill\_id: String

version: String

The skill version number.

##### ReturnsExpand Collapse

class DeletedSkillVersion { id, deleted, object, version }

id: String

deleted: bool

object: :"skill.version.deleted"

version: String

The deleted skill version.

### Delete a skill version.

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

deleted_skill_version = openai.skills.versions.delete("version", skill_id: "skill_123")

puts(deleted_skill_version)

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
