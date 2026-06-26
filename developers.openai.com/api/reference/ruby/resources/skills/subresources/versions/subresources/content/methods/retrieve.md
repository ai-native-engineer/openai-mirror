<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Skills](/api/reference/ruby/resources/skills)

[Versions](/api/reference/ruby/resources/skills/subresources/versions)

[Content](/api/reference/ruby/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

skills.versions.content.retrieve(version, \*\*kwargs) -> StringIO

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### ParametersExpand Collapse

skill\_id: String

version: String

The skill version number.

##### ReturnsExpand Collapse

StringIO

### Download a skill version zip bundle.

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

content = openai.skills.versions.content.retrieve("version", skill_id: "skill_123")

puts(content)

##### Returns Examples
