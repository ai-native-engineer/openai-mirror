<!-- source: https://developers.openai.com/api/reference/python/resources/skills/methods/list/ -->

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

# List all skills for the current project.

skills.list(SkillListParams\*\*kwargs)  -> SyncCursorPage[[Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))]

GET/skills

List all skills for the current project.

##### ParametersExpand Collapse

after: Optional[str]

Identifier for the last item from the previous pagination request

limit: Optional[int]

Number of items to retrieve

minimum0

maximum100

order: Optional[Literal["asc", "desc"]]

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

One of the following:

"asc"

"desc"

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

### List all skills for the current project.

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
page = client.skills.list()
page = page.data[0]
print(page.id)

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

##### Returns Examples

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
