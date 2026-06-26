<!-- source: https://developers.openai.com/api/reference/resources/skills/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Skills](/api/reference/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a new skill.

POST/skills

Create a new skill.

##### Body ParametersJSONExpand Collapse

files: array of string or string

Skill files to upload (directory upload) or a single zip file.

One of the following:

array of string

Skill files to upload (directory upload) or a single zip file.

string

Skill zip file to upload.

##### ReturnsExpand Collapse

Skill object { id, created\_at, default\_version, 4 more }

id: string

Unique identifier for the skill.

created\_at: number

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: string

Default version for the skill.

description: string

Description of the skill.

latest\_version: string

Latest version for the skill.

name: string

Name of the skill.

object: "skill"

The object type, which is `skill`.

### Create a new skill.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/skills \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -F files='["Example data"]'

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
