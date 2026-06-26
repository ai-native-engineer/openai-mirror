<!-- source: https://developers.openai.com/api/reference/java/resources/skills/methods/delete/ -->

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

# Delete a skill by its ID.

[DeletedSkill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)) skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### ParametersExpand Collapse

SkillDeleteParams params

Optional<String> skillId

##### ReturnsExpand Collapse

class DeletedSkill:

String id

boolean deleted

JsonValue; object\_ "skill.deleted"constant"skill.deleted"constant

### Delete a skill by its ID.

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
import com.openai.models.skills.DeletedSkill;
import com.openai.models.skills.SkillDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        DeletedSkill deletedSkill = client.skills().delete("skill_123");

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
