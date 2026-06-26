<!-- source: https://developers.openai.com/api/reference/java/resources/skills/subresources/versions/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Skills](/api/reference/java/resources/skills)

[Versions](/api/reference/java/resources/skills/subresources/versions)

[Content](/api/reference/java/resources/skills/subresources/versions/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill version zip bundle.

HttpResponse skills().versions().content().retrieve(ContentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/versions/{version}/content

Download a skill version zip bundle.

##### ParametersExpand Collapse

ContentRetrieveParams params

String skillId

Optional<String> version

The skill version number.

### Download a skill version zip bundle.

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
import com.openai.core.http.HttpResponse;
import com.openai.models.skills.versions.content.ContentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContentRetrieveParams params = ContentRetrieveParams.builder()
            .skillId("skill_123")
            .version("version")
            .build();
        HttpResponse content = client.skills().versions().content().retrieve(params);

##### Returns Examples
