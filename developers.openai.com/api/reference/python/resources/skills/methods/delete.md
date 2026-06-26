<!-- source: https://developers.openai.com/api/reference/python/resources/skills/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Skills](/api/reference/python/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a skill by its ID.

skills.delete(strskill\_id)  -> [DeletedSkill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema))

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### ParametersExpand Collapse

skill\_id: str

##### ReturnsExpand Collapse

class DeletedSkill: …

id: str

deleted: bool

object: Literal["skill.deleted"]

### Delete a skill by its ID.

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
deleted_skill = client.skills.delete(
    "skill_123",
print(deleted_skill.id)

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
