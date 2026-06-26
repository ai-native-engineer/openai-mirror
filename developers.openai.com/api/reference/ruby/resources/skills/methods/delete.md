<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/methods/delete/ -->

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

# Delete a skill by its ID.

skills.delete(skill\_id) -> [DeletedSkill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)) { id, deleted, object }

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### ParametersExpand Collapse

skill\_id: String

##### ReturnsExpand Collapse

class DeletedSkill { id, deleted, object }

id: String

deleted: bool

object: :"skill.deleted"

### Delete a skill by its ID.

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

deleted_skill = openai.skills.delete("skill_123")

puts(deleted_skill)

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
