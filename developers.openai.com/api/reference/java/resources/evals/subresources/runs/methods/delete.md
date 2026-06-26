<!-- source: https://developers.openai.com/api/reference/java/resources/evals/subresources/runs/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Evals](/api/reference/java/resources/evals)

[Runs](/api/reference/java/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete eval run

[RunDeleteResponse](/api/reference/java/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20RunDeleteResponse%20%3E%20(schema)) evals().runs().delete(RunDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/evals/{eval\_id}/runs/{run\_id}

Delete an eval run.

##### ParametersExpand Collapse

RunDeleteParams params

String evalId

Optional<String> runId

##### ReturnsExpand Collapse

class RunDeleteResponse:

Optional<Boolean> deleted

Optional<String> object\_

Optional<String> runId

### Delete eval run

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
import com.openai.models.evals.runs.RunDeleteParams;
import com.openai.models.evals.runs.RunDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunDeleteParams params = RunDeleteParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .build();
        RunDeleteResponse run = client.evals().runs().delete(params);

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"

##### Returns Examples

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"
