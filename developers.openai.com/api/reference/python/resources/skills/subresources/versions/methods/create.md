<!-- source: https://developers.openai.com/api/reference/python/resources/skills/subresources/versions/methods/create/ -->

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

# Create a new immutable skill version.

skills.versions.create(strskill\_id, VersionCreateParams\*\*kwargs)  -> [SkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))

POST/skills/{skill\_id}/versions

Create a new immutable skill version.

##### ParametersExpand Collapse

skill\_id: str

default: Optional[[bool](/api/reference/python/resources/skills/subresources/versions/methods/create#(resource)%20skills.versions%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20default%20%3E%20(schema))]

Whether to set this version as the default.

files: Optional[Union[Sequence[FileTypes], FileTypes]]

Skill files to upload (directory upload) or a single zip file.

One of the following:

Sequence[FileTypes]

Skill files to upload (directory upload) or a single zip file.

FileTypes

Skill zip file to upload.

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

### Create a new immutable skill version.

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
skill_version = client.skills.versions.create(
    skill_id="skill_123",
print(skill_version.id)

200 example

  "id": "id",
  "created_at": 0,
  "description": "description",
  "name": "name",
  "object": "skill.version",
  "skill_id": "skill_id",
  "version": "version"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "description": "description",
  "name": "name",
  "object": "skill.version",
  "skill_id": "skill_id",
  "version": "version"
