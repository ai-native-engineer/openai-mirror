<!-- source: https://developers.openai.com/api/reference/resources/skills/methods/update/ -->

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

# Update the default version pointer for a skill.

POST/skills/{skill\_id}

Update the default version pointer for a skill.

##### Path ParametersExpand Collapse

skill\_id: string

##### Body ParametersJSONExpand Collapse

default\_version: string

The skill version number to set as default.

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

### Update the default version pointer for a skill.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/skills/$SKILL_ID \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "default_version": "default_version"
        }'

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
