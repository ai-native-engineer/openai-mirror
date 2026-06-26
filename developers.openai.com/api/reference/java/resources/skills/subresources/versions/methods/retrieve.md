<!-- source: https://developers.openai.com/api/reference/java/resources/skills/subresources/versions/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Skills](/api/reference/java/resources/skills)

[Versions](/api/reference/java/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get a specific skill version.

[SkillVersion](/api/reference/java/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/versions/{version}

Get a specific skill version.

##### ParametersExpand Collapse

VersionRetrieveParams params

String skillId

Optional<String> version

The version number to retrieve.

##### ReturnsExpand Collapse

class SkillVersion:

String id

Unique identifier for the skill version.

long createdAt

Unix timestamp (seconds) for when the version was created.

formatunixtime

String description

Description of the skill version.

String name

Name of the skill version.

JsonValue; object\_ "skill.version"constant"skill.version"constant

The object type, which is `skill.version`.

String skillId

Identifier of the skill for this version.

String version

Version number for this skill.

### Get a specific skill version.

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
import com.openai.models.skills.versions.SkillVersion;
import com.openai.models.skills.versions.VersionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VersionRetrieveParams params = VersionRetrieveParams.builder()
            .skillId("skill_123")
            .version("version")
            .build();
        SkillVersion skillVersion = client.skills().versions().retrieve(params);

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
