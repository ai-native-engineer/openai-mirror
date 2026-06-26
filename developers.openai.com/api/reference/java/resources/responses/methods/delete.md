<!-- source: https://developers.openai.com/api/reference/java/resources/responses/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Responses](/api/reference/java/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a model response

responses().delete(ResponseDeleteParamsparams = ResponseDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

ResponseDeleteParams params

Optional<String> responseId

### Delete a model response

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
import com.openai.models.responses.ResponseDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.responses().delete("resp_677efb5139a88190b512bc3fef8e535d");

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

##### Returns Examples

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
