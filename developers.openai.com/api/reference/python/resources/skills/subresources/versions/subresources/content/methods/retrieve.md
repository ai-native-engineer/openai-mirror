<!-- source: https://developers.openai.com/api/reference/python/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Skills](/api/reference/python/resources/skills)

[Versions](/api/reference/python/resources/skills/subresources/versions)

[Content](/api/reference/python/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

skills.versions.content.retrieve(strversion, ContentRetrieveParams\*\*kwargs)  -> BinaryResponseContent

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### ParametersExpand Collapse

skill\_id: str

version: str

The skill version number.

##### ReturnsExpand Collapse

BinaryResponseContent

### Download a skill version zip bundle.

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
content = client.skills.versions.content.retrieve(
    version="version",
    skill_id="skill_123",
print(content)
data = content.read()
print(data)

##### Returns Examples
