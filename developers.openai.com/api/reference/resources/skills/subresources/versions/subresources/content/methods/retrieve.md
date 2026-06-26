<!-- source: https://developers.openai.com/api/reference/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Skills](/api/reference/resources/skills)

[Versions](/api/reference/resources/skills/subresources/versions)

[Content](/api/reference/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### Path ParametersExpand Collapse

skill\_id: string

version: string

The skill version number.

### Download a skill version zip bundle.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/skills/$SKILL_ID/versions/$VERSION/content \
    -H "Authorization: Bearer $OPENAI_API_KEY"

##### Returns Examples
