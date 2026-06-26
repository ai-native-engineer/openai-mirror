<!-- source: https://developers.openai.com/api/reference/java/resources/evals/subresources/runs/subresources/output_items/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Evals](/api/reference/java/resources/evals)

[Runs](/api/reference/java/resources/evals/subresources/runs)

[Output Items](/api/reference/java/resources/evals/subresources/runs/subresources/output_items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get an output item of an eval run

[OutputItemRetrieveResponse](/api/reference/java/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20OutputItemRetrieveResponse%20%3E%20(schema)) evals().runs().outputItems().retrieve(OutputItemRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

Get an evaluation run output item by ID.

##### ParametersExpand Collapse

OutputItemRetrieveParams params

String evalId

String runId

Optional<String> outputItemId

##### ReturnsExpand Collapse

class OutputItemRetrieveResponse:

A schema representing an evaluation run output item.

String id

Unique identifier for the evaluation run output item.

long createdAt

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

DatasourceItem datasourceItem

Details of the input data source item.

long datasourceItemId

The identifier for the data source item.

String evalId

The identifier of the evaluation group.

JsonValue; object\_ "eval.run.output\_item"constant"eval.run.output\_item"constant

The type of the object. Always “eval.run.output\_item”.

List<Result> results

A list of grader results for this output item.

String name

The name of the grader.

boolean passed

Whether the grader considered the output a pass.

double score

The numeric score produced by the grader.

Optional<Sample> sample

Optional sample or intermediate data produced by the grader.

Optional<String> type

The grader type (for example, “string-check-grader”).

String runId

The identifier of the evaluation run associated with this output item.

Sample sample

A sample containing the input and output of the evaluation run.

[EvalApiError](/api/reference/java/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) error

An object representing an error response from the Eval API.

String code

The error code.

String message

The error message.

String finishReason

The reason why the sample generation was finished.

List<Input> input

An array of input messages.

String content

The content of the message.

String role

The role of the message sender (e.g., system, user, developer).

long maxCompletionTokens

The maximum number of tokens allowed for completion.

String model

The model used for generating the sample.

List<Output> output

An array of output messages.

Optional<String> content

The content of the message.

Optional<String> role

The role of the message (e.g. “system”, “assistant”, “user”).

long seed

The seed used for generating the sample.

double temperature

The sampling temperature used.

double topP

The top\_p value used for sampling.

Usage usage

Token usage details for the sample.

long cachedTokens

The number of tokens retrieved from cache.

long completionTokens

The number of completion tokens generated.

long promptTokens

The number of prompt tokens used.

long totalTokens

The total number of tokens used.

String status

The status of the evaluation run.

### Get an output item of an eval run

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
import com.openai.models.evals.runs.outputitems.OutputItemRetrieveParams;
import com.openai.models.evals.runs.outputitems.OutputItemRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        OutputItemRetrieveParams params = OutputItemRetrieveParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .outputItemId("output_item_id")
            .build();
        OutputItemRetrieveResponse outputItem = client.evals().runs().outputItems().retrieve(params);

  "object": "eval.run.output_item",
  "id": "outputitem_67e5796c28e081909917bf79f6e6214d",
  "created_at": 1743092076,
  "run_id": "evalrun_67abd54d60ec8190832b46859da808f7",
  "eval_id": "eval_67abd54d9b0081909a86353f6fb9317a",
  "status": "pass",
  "datasource_item_id": 5,
  "datasource_item": {
    "input": "Stock Markets Rally After Positive Economic Data Released",
    "ground_truth": "Markets"
  "results": [
      "name": "String check-a2486074-d803-4445-b431-ad2262e85d47",
      "sample": null,
      "passed": true,
      "score": 1.0
  ],
  "sample": {
    "input": [
        "role": "developer",
        "content": "Categorize a given news headline into one of the following topics: Technology, Markets, World, Business, or Sports.\n\n# Steps\n\n1. Analyze the content of the news headline to understand its primary focus.\n2. Extract the subject matter, identifying any key indicators or keywords.\n3. Use the identified indicators to determine the most suitable category out of the five options: Technology, Markets, World, Business, or Sports.\n4. Ensure only one category is selected per headline.\n\n# Output Format\n\nRespond with the chosen category as a single word. For instance: \"Technology\", \"Markets\", \"World\", \"Business\", or \"Sports\".\n\n# Examples\n\n**Input**: \"Apple Unveils New iPhone Model, Featuring Advanced AI Features\"  \n**Output**: \"Technology\"\n\n**Input**: \"Global Stocks Mixed as Investors Await Central Bank Decisions\"  \n**Output**: \"Markets\"\n\n**Input**: \"War in Ukraine: Latest Updates on Negotiation Status\"  \n**Output**: \"World\"\n\n**Input**: \"Microsoft in Talks to Acquire Gaming Company for $2 Billion\"  \n**Output**: \"Business\"\n\n**Input**: \"Manchester United Secures Win in Premier League Football Match\"  \n**Output**: \"Sports\" \n\n# Notes\n\n- If the headline appears to fit into more than one category, choose the most dominant theme.\n- Keywords or phrases such as \"stocks\", \"company acquisition\", \"match\", or technological brands can be good indicators for classification.\n",
        "tool_call_id": null,
        "tool_calls": null,
        "function_call": null
        "role": "user",
        "content": "Stock Markets Rally After Positive Economic Data Released",
        "tool_call_id": null,
        "tool_calls": null,
        "function_call": null
    ],
    "output": [
        "role": "assistant",
        "content": "Markets",
        "tool_call_id": null,
        "tool_calls": null,
        "function_call": null
    ],
    "finish_reason": "stop",
    "model": "gpt-4o-mini-2024-07-18",
    "usage": {
      "total_tokens": 325,
      "completion_tokens": 2,
      "prompt_tokens": 323,
      "cached_tokens": 0
    "error": null,
    "temperature": 1.0,
    "max_completion_tokens": 2048,
    "top_p": 1.0,
    "seed": 42

##### Returns Examples

  "object": "eval.run.output_item",
  "id": "outputitem_67e5796c28e081909917bf79f6e6214d",
  "created_at": 1743092076,
  "run_id": "evalrun_67abd54d60ec8190832b46859da808f7",
  "eval_id": "eval_67abd54d9b0081909a86353f6fb9317a",
  "status": "pass",
  "datasource_item_id": 5,
  "datasource_item": {
    "input": "Stock Markets Rally After Positive Economic Data Released",
    "ground_truth": "Markets"
  "results": [
      "name": "String check-a2486074-d803-4445-b431-ad2262e85d47",
      "sample": null,
      "passed": true,
      "score": 1.0
  ],
  "sample": {
    "input": [
        "role": "developer",
        "content": "Categorize a given news headline into one of the following topics: Technology, Markets, World, Business, or Sports.\n\n# Steps\n\n1. Analyze the content of the news headline to understand its primary focus.\n2. Extract the subject matter, identifying any key indicators or keywords.\n3. Use the identified indicators to determine the most suitable category out of the five options: Technology, Markets, World, Business, or Sports.\n4. Ensure only one category is selected per headline.\n\n# Output Format\n\nRespond with the chosen category as a single word. For instance: \"Technology\", \"Markets\", \"World\", \"Business\", or \"Sports\".\n\n# Examples\n\n**Input**: \"Apple Unveils New iPhone Model, Featuring Advanced AI Features\"  \n**Output**: \"Technology\"\n\n**Input**: \"Global Stocks Mixed as Investors Await Central Bank Decisions\"  \n**Output**: \"Markets\"\n\n**Input**: \"War in Ukraine: Latest Updates on Negotiation Status\"  \n**Output**: \"World\"\n\n**Input**: \"Microsoft in Talks to Acquire Gaming Company for $2 Billion\"  \n**Output**: \"Business\"\n\n**Input**: \"Manchester United Secures Win in Premier League Football Match\"  \n**Output**: \"Sports\" \n\n# Notes\n\n- If the headline appears to fit into more than one category, choose the most dominant theme.\n- Keywords or phrases such as \"stocks\", \"company acquisition\", \"match\", or technological brands can be good indicators for classification.\n",
        "tool_call_id": null,
        "tool_calls": null,
        "function_call": null
        "role": "user",
        "content": "Stock Markets Rally After Positive Economic Data Released",
        "tool_call_id": null,
        "tool_calls": null,
        "function_call": null
    ],
    "output": [
        "role": "assistant",
        "content": "Markets",
        "tool_call_id": null,
        "tool_calls": null,
        "function_call": null
    ],
    "finish_reason": "stop",
    "model": "gpt-4o-mini-2024-07-18",
    "usage": {
      "total_tokens": 325,
      "completion_tokens": 2,
      "prompt_tokens": 323,
      "cached_tokens": 0
    "error": null,
    "temperature": 1.0,
    "max_completion_tokens": 2048,
    "top_p": 1.0,
    "seed": 42
