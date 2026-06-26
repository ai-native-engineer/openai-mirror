<!-- source: https://developers.openai.com/api/reference/java/resources/skills/subresources/versions/methods/list/ -->

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

# List skill versions for a skill.

VersionListPage skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/versions

List skill versions for a skill.

##### ParametersExpand Collapse

VersionListParams params

Optional<String> skillId

Optional<String> after

The skill version ID to start after.

Optional<Long> limit

Number of versions to retrieve.

minimum0

maximum100

Optional<[Order](/api/reference/java/resources/skills/subresources/versions/methods/list#(resource)%20skills.versions%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order of results by version number.

ASC("asc")

DESC("desc")

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

### List skill versions for a skill.

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
import com.openai.models.skills.versions.VersionListPage;
import com.openai.models.skills.versions.VersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VersionListPage page = client.skills().versions().list("skill_123");

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
