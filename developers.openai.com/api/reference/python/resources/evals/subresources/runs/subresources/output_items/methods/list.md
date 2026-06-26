<!-- source: https://developers.openai.com/api/reference/python/resources/evals/subresources/runs/subresources/output_items/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Evals](/api/reference/python/resources/evals)

[Runs](/api/reference/python/resources/evals/subresources/runs)

[Output Items](/api/reference/python/resources/evals/subresources/runs/subresources/output_items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get eval run output items

evals.runs.output\_items.list(strrun\_id, OutputItemListParams\*\*kwargs)  -> SyncCursorPage[[OutputItemListResponse](/api/reference/python/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_list_response%20%3E%20(schema))]

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

Get a list of output items for an evaluation run.

##### ParametersExpand Collapse

eval\_id: str

run\_id: str

after: Optional[str]

Identifier for the last output item from the previous pagination request.

limit: Optional[int]

Number of output items to retrieve.

order: Optional[Literal["asc", "desc"]]

Sort order for output items by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

One of the following:

"asc"

"desc"

status: Optional[Literal["fail", "pass"]]

Filter output items by status. Use `failed` to filter by failed output
items or `pass` to filter by passed output items.

One of the following:

"fail"

"pass"

##### ReturnsExpand Collapse

class OutputItemListResponse: …

A schema representing an evaluation run output item.

id: str

Unique identifier for the evaluation run output item.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Dict[str, object]

Details of the input data source item.

datasource\_item\_id: int

The identifier for the data source item.

eval\_id: str

The identifier of the evaluation group.

object: Literal["eval.run.output\_item"]

The type of the object. Always “eval.run.output\_item”.

results: List[Result]

A list of grader results for this output item.

name: str

The name of the grader.

passed: bool

Whether the grader considered the output a pass.

score: float

The numeric score produced by the grader.

sample: Optional[Dict[str, object]]

Optional sample or intermediate data produced by the grader.

type: Optional[str]

The grader type (for example, “string-check-grader”).

run\_id: str

The identifier of the evaluation run associated with this output item.

sample: Sample

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

code: str

The error code.

message: str

The error message.

finish\_reason: str

The reason why the sample generation was finished.

input: List[SampleInput]

An array of input messages.

content: str

The content of the message.

role: str

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: int

The maximum number of tokens allowed for completion.

model: str

The model used for generating the sample.

output: List[SampleOutput]

An array of output messages.

content: Optional[str]

The content of the message.

role: Optional[str]

The role of the message (e.g. “system”, “assistant”, “user”).

seed: int

The seed used for generating the sample.

temperature: float

The sampling temperature used.

top\_p: float

The top\_p value used for sampling.

usage: SampleUsage

Token usage details for the sample.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

status: str

The status of the evaluation run.

### Get eval run output items

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

output_items = client.evals.runs.output_items.list(
  "egroup_67abd54d9b0081909a86353f6fb9317a",
  "erun_67abd54d60ec8190832b46859da808f7"
print(output_items)

  "object": "list",
  "data": [
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
  ],
  "first_id": "outputitem_67e5796c28e081909917bf79f6e6214d",
  "last_id": "outputitem_67e5796c28e081909917bf79f6e6214d",
  "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
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
  ],
  "first_id": "outputitem_67e5796c28e081909917bf79f6e6214d",
  "last_id": "outputitem_67e5796c28e081909917bf79f6e6214d",
  "has_more": true
