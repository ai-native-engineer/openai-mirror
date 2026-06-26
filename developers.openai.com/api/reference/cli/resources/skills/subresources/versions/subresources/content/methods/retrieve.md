<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Skills](/api/reference/cli/resources/skills)

[Versions](/api/reference/cli/resources/skills/subresources/versions)

[Content](/api/reference/cli/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

$ openai skills:versions:content retrieve

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill.

--version: string

The skill version number.

##### ReturnsExpand Collapse

unnamed\_schema\_5: file path

### Download a skill version zip bundle.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills:versions:content retrieve \
  --api-key 'My API Key' \
  --skill-id skill_123 \
  --version version

##### Returns Examples
