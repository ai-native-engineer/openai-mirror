<!-- source: https://developers.openai.com/api/reference/java/resources/skills/subresources/versions/methods/delete/ -->

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

# Delete a skill version.

[DeletedSkillVersion](/api/reference/java/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)) skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### ParametersExpand Collapse

VersionDeleteParams params

String skillId

Optional<String> version

The skill version number.

##### ReturnsExpand Collapse

class DeletedSkillVersion:

String id

boolean deleted

JsonValue; object\_ "skill.version.deleted"constant"skill.version.deleted"constant

String version

The deleted skill version.

### Delete a skill version.

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
import com.openai.models.skills.versions.DeletedSkillVersion;
import com.openai.models.skills.versions.VersionDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VersionDeleteParams params = VersionDeleteParams.builder()
            .skillId("skill_123")
            .version("version")
            .build();
        DeletedSkillVersion deletedSkillVersion = client.skills().versions().delete(params);

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
