<!-- source: https://developers.openai.com/api/reference/ruby/resources/evals/subresources/runs/subresources/output_items/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Evals](/api/reference/ruby/resources/evals)

[Runs](/api/reference/ruby/resources/evals/subresources/runs)

[Output Items](/api/reference/ruby/resources/evals/subresources/runs/subresources/output_items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get an output item of an eval run

evals.runs.output\_items.retrieve(output\_item\_id, \*\*kwargs) -> [OutputItemRetrieveResponse](/api/reference/ruby/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_retrieve_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more }

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

Get an evaluation run output item by ID.

##### ParametersExpand Collapse

eval\_id: String

run\_id: String

output\_item\_id: String

##### ReturnsExpand Collapse

class OutputItemRetrieveResponse { id, created\_at, datasource\_item, 7 more }

A schema representing an evaluation run output item.

id: String

Unique identifier for the evaluation run output item.

created\_at: Integer

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Hash[Symbol, untyped]

Details of the input data source item.

datasource\_item\_id: Integer

The identifier for the data source item.

eval\_id: String

The identifier of the evaluation group.

object: :"eval.run.output\_item"

The type of the object. Always “eval.run.output\_item”.

results: Array[Result{ name, passed, score, 2 more}]

A list of grader results for this output item.

name: String

The name of the grader.

passed: bool

Whether the grader considered the output a pass.

score: Float

The numeric score produced by the grader.

sample: Hash[Symbol, untyped]

Optional sample or intermediate data produced by the grader.

type: String

The grader type (for example, “string-check-grader”).

run\_id: String

The identifier of the evaluation run associated with this output item.

sample: Sample{ error, finish\_reason, input, 7 more}

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

code: String

The error code.

message: String

The error message.

finish\_reason: String

The reason why the sample generation was finished.

input: Array[Input{ content, role}]

An array of input messages.

content: String

The content of the message.

role: String

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: Integer

The maximum number of tokens allowed for completion.

model: String

The model used for generating the sample.

output: Array[Output{ content, role}]

An array of output messages.

content: String

The content of the message.

role: String

The role of the message (e.g. “system”, “assistant”, “user”).

seed: Integer

The seed used for generating the sample.

temperature: Float

The sampling temperature used.

top\_p: Float

The top\_p value used for sampling.

usage: Usage{ cached\_tokens, completion\_tokens, prompt\_tokens, total\_tokens}

Token usage details for the sample.

cached\_tokens: Integer

The number of tokens retrieved from cache.

completion\_tokens: Integer

The number of completion tokens generated.

prompt\_tokens: Integer

The number of prompt tokens used.

total\_tokens: Integer

The total number of tokens used.

status: String

The status of the evaluation run.

### Get an output item of an eval run

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

output_item = openai.evals.runs.output_items.retrieve("output_item_id", eval_id: "eval_id", run_id: "run_id")

puts(output_item)

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
