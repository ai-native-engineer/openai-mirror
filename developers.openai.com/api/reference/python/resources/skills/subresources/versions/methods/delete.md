<!-- source: https://developers.openai.com/api/reference/python/resources/skills/subresources/versions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Skills](/api/reference/python/resources/skills)

[Versions](/api/reference/python/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a skill version.

skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs)  -> [DeletedSkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema))

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### ParametersExpand Collapse

skill\_id: str

version: str

The skill version number.

##### ReturnsExpand Collapse

class DeletedSkillVersion: …

id: str

deleted: bool

object: Literal["skill.version.deleted"]

version: str

The deleted skill version.

### Delete a skill version.

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
deleted_skill_version = client.skills.versions.delete(
    version="version",
    skill_id="skill_123",
print(deleted_skill_version.id)

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.version.deleted",
  "version": "version"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.version.deleted",
  "version": "version"
