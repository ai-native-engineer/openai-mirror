<!-- source: https://developers.openai.com/api/reference/python/resources/skills/methods/retrieve/ -->

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

# Get a skill by its ID.

skills.retrieve(strskill\_id)  -> [Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))

GET/skills/{skill\_id}

Get a skill by its ID.

##### ParametersExpand Collapse

skill\_id: str

##### ReturnsExpand Collapse

class Skill: …

id: str

Unique identifier for the skill.

created\_at: int

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: str

Default version for the skill.

description: str

Description of the skill.

latest\_version: str

Latest version for the skill.

name: str

Name of the skill.

object: Literal["skill"]

The object type, which is `skill`.

### Get a skill by its ID.

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
skill = client.skills.retrieve(
    "skill_123",
print(skill.id)

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"
