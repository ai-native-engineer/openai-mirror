<!-- source: https://developers.openai.com/api/reference/java/resources/skills/subresources/content/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Skills](/api/reference/java/resources/skills)

[Content](/api/reference/java/resources/skills/subresources/content)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Download a skill zip bundle by its ID.

HttpResponse skills().content().retrieve(ContentRetrieveParamsparams = ContentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/content

Download a skill zip bundle by its ID.

##### ParametersExpand Collapse

ContentRetrieveParams params

Optional<String> skillId

### Download a skill zip bundle by its ID.

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
import com.openai.models.skills.content.ContentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse content = client.skills().content().retrieve("skill_123");

##### Returns Examples
