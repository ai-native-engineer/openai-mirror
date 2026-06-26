<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Skills](/api/reference/ruby/resources/skills)

[Content](/api/reference/ruby/resources/skills/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill zip bundle by its ID.

skills.content.retrieve(skill\_id) -> StringIO

GET/skills/{skill\_id}/content

Download a skill zip bundle by its ID.

##### ParametersExpand Collapse

skill\_id: String

##### ReturnsExpand Collapse

StringIO

### Download a skill zip bundle by its ID.

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

content = openai.skills.content.retrieve("skill_123")

puts(content)

##### Returns Examples
