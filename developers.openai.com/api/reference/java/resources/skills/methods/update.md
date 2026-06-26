<!-- source: https://developers.openai.com/api/reference/java/resources/skills/methods/update/ -->

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

# Update the default version pointer for a skill.

[Skill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) skills().update(SkillUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/skills/{skill\_id}

Update the default version pointer for a skill.

##### ParametersExpand Collapse

SkillUpdateParams params

Optional<String> skillId

String defaultVersion

The skill version number to set as default.

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

### Update the default version pointer for a skill.

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
import com.openai.models.skills.SkillUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SkillUpdateParams params = SkillUpdateParams.builder()
            .skillId("skill_123")
            .defaultVersion("default_version")
            .build();
        Skill skill = client.skills().update(params);

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
