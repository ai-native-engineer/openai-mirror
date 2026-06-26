<!-- source: https://developers.openai.com/api/reference/java/resources/skills/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Skills](/api/reference/java/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get a skill by its ID.

[Skill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}

Get a skill by its ID.

##### ParametersExpand Collapse

SkillRetrieveParams params

Optional<String> skillId

##### ReturnsExpand Collapse

class Skill:

String id

Unique identifier for the skill.

long createdAt

Unix timestamp (seconds) for when the skill was created.

formatunixtime

String defaultVersion

Default version for the skill.

String description

Description of the skill.

String latestVersion

Latest version for the skill.

String name

Name of the skill.

JsonValue; object\_ "skill"constant"skill"constant

The object type, which is `skill`.

### Get a skill by its ID.

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.Skill;
import com.openai.models.skills.SkillRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Skill skill = client.skills().retrieve("skill_123");

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
