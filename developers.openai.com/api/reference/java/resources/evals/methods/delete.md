<!-- source: https://developers.openai.com/api/reference/java/resources/evals/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Evals](/api/reference/java/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an eval

[EvalDeleteResponse](/api/reference/java/resources/evals#(resource)%20evals%20%3E%20(model)%20EvalDeleteResponse%20%3E%20(schema)) evals().delete(EvalDeleteParamsparams = EvalDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/evals/{eval\_id}

Delete an evaluation.

##### ParametersExpand Collapse

EvalDeleteParams params

Optional<String> evalId

##### ReturnsExpand Collapse

class EvalDeleteResponse:

boolean deleted

String evalId

String object\_

### Delete an eval

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
import com.openai.models.evals.EvalDeleteParams;
import com.openai.models.evals.EvalDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalDeleteResponse eval = client.evals().delete("eval_id");

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"

##### Returns Examples

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"
