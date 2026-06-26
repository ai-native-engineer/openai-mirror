<!-- source: https://developers.openai.com/api/reference/java/resources/models/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Models](/api/reference/java/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a fine-tuned model

[ModelDeleted](/api/reference/java/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)) models().delete(ModelDeleteParamsparams = ModelDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### ParametersExpand Collapse

ModelDeleteParams params

Optional<String> model

##### ReturnsExpand Collapse

class ModelDeleted:

String id

boolean deleted

String object\_

### Delete a fine-tuned model

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
import com.openai.models.models.ModelDeleteParams;
import com.openai.models.models.ModelDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ModelDeleted modelDeleted = client.models().delete("ft:gpt-4o-mini:acemeco:suffix:abc123");

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true

##### Returns Examples

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
