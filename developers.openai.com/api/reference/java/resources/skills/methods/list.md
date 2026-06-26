<!-- source: https://developers.openai.com/api/reference/java/resources/skills/methods/list/ -->

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

# List all skills for the current project.

SkillListPage skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills

List all skills for the current project.

##### ParametersExpand Collapse

SkillListParams params

Optional<String> after

Identifier for the last item from the previous pagination request

Optional<Long> limit

Number of items to retrieve

minimum0

maximum100

Optional<[Order](/api/reference/java/resources/skills/methods/list#(resource)%20skills%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

ASC("asc")

DESC("desc")

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

### List all skills for the current project.

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
import com.openai.models.skills.SkillListPage;
import com.openai.models.skills.SkillListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SkillListPage page = client.skills().list();

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
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
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
