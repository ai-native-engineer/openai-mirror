<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Skills](/api/reference/cli/resources/skills)

[Content](/api/reference/cli/resources/skills/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill zip bundle by its ID.

$ openai skills:content retrieve

GET/skills/{skill\_id}/content

Download a skill zip bundle by its ID.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill to download.

##### ReturnsExpand Collapse

unnamed\_schema\_4: file path

### Download a skill zip bundle by its ID.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills:content retrieve \
  --api-key 'My API Key' \
  --skill-id skill_123

##### Returns Examples
