<!-- source: https://developers.openai.com/api/reference/resources/skills/subresources/versions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Skills](/api/reference/resources/skills)

[Versions](/api/reference/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a new immutable skill version.

POST/skills/{skill\_id}/versions

Create a new immutable skill version.

##### Path ParametersExpand Collapse

skill\_id: string

##### Body ParametersJSONExpand Collapse

files: array of string or string

Skill files to upload (directory upload) or a single zip file.

One of the following:

array of string

Skill files to upload (directory upload) or a single zip file.

string

Skill zip file to upload.

default: optional boolean

Whether to set this version as the default.

##### ReturnsExpand Collapse

SkillVersion object { id, created\_at, description, 4 more }

id: string

Unique identifier for the skill version.

created\_at: number

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: string

Description of the skill version.

name: string

Name of the skill version.

object: "skill.version"

The object type, which is `skill.version`.

skill\_id: string

Identifier of the skill for this version.

version: string

Version number for this skill.

### Create a new immutable skill version.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/skills/$SKILL_ID/versions \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -F files='["Example data"]'

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
