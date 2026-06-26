<!-- source: https://developers.openai.com/api/reference/java/resources/models/methods/retrieve/ -->

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

# Retrieve model

[Model](/api/reference/java/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### ParametersExpand Collapse

ModelRetrieveParams params

Optional<String> model

##### ReturnsExpand Collapse

class Model:

Describes an OpenAI model offering that can be used with the API.

String id

The model identifier, which can be referenced in the API endpoints.

long created

The Unix timestamp (in seconds) when the model was created.

formatunixtime

JsonValue; object\_ "model"constant"model"constant

The object type, which is always “model”.

String ownedBy

The organization that owns the model.

### Retrieve model

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
import com.openai.models.models.Model;
import com.openai.models.models.ModelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Model model = client.models().retrieve("gpt-4o-mini");

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
