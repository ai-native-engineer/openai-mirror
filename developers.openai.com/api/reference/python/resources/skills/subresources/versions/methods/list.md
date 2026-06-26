<!-- source: https://developers.openai.com/api/reference/python/resources/skills/subresources/versions/methods/list/ -->

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

# List skill versions for a skill.

skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncCursorPage[[SkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))]

GET/skills/{skill\_id}/versions

List skill versions for a skill.

##### ParametersExpand Collapse

skill\_id: str

after: Optional[str]

The skill version ID to start after.

limit: Optional[int]

Number of versions to retrieve.

minimum0

maximum100

order: Optional[Literal["asc", "desc"]]

Sort order of results by version number.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

class SkillVersion: …

id: str

Unique identifier for the skill version.

created\_at: int

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: str

Description of the skill version.

name: str

Name of the skill version.

object: Literal["skill.version"]

The object type, which is `skill.version`.

skill\_id: str

Identifier of the skill for this version.

version: str

Version number for this skill.

### List skill versions for a skill.

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
page = client.skills.versions.list(
    skill_id="skill_123",
page = page.data[0]
print(page.id)

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "description": "description",
      "name": "name",
      "object": "skill.version",
      "skill_id": "skill_id",
      "version": "version"
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
      "description": "description",
      "name": "name",
      "object": "skill.version",
      "skill_id": "skill_id",
      "version": "version"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
