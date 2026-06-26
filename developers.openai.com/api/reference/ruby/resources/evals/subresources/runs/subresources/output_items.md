<!-- source: https://developers.openai.com/api/reference/ruby/resources/evals/subresources/runs/subresources/output_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Evals](/api/reference/ruby/resources/evals)

[Runs](/api/reference/ruby/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Output Items

Manage and run evals in the OpenAI platform.

##### [Get eval run output items](/api/reference/ruby/resources/evals/subresources/runs/subresources/output_items/methods/list)

evals.runs.output\_items.list(run\_id, \*\*kwargs) -> CursorPage<[OutputItemListResponse](/api/reference/ruby/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_list_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more } >

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

##### [Get an output item of an eval run](/api/reference/ruby/resources/evals/subresources/runs/subresources/output_items/methods/retrieve)

evals.runs.output\_items.retrieve(output\_item\_id, \*\*kwargs) -> [OutputItemRetrieveResponse](/api/reference/ruby/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_retrieve_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more }

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

##### ModelsExpand Collapse

class OutputItemListResponse { id, created\_at, datasource\_item, 7 more }

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
