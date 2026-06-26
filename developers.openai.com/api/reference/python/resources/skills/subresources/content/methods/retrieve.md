<!-- source: https://developers.openai.com/api/reference/python/resources/skills/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Skills](/api/reference/python/resources/skills)

[Content](/api/reference/python/resources/skills/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill zip bundle by its ID.

skills.content.retrieve(strskill\_id)  -> BinaryResponseContent

GET/skills/{skill\_id}/content

Download a skill zip bundle by its ID.

##### ParametersExpand Collapse

skill\_id: str

##### ReturnsExpand Collapse

BinaryResponseContent

### Download a skill zip bundle by its ID.

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
content = client.skills.content.retrieve(
    "skill_123",
print(content)
data = content.read()
print(data)

##### Returns Examples
