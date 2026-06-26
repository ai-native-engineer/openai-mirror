<!-- source: https://developers.openai.com/api/reference/typescript/resources/evals/subresources/runs/subresources/output_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Evals](/api/reference/typescript/resources/evals)

[Runs](/api/reference/typescript/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Output Items

Manage and run evals in the OpenAI platform.

##### [Get eval run output items](/api/reference/typescript/resources/evals/subresources/runs/subresources/output_items/methods/list)

client.evals.runs.outputItems.list(stringrunID, OutputItemListParams { eval\_id, after, limit, 2 more } params, RequestOptionsoptions?): CursorPage<[OutputItemListResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_list_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more } >

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

##### [Get an output item of an eval run](/api/reference/typescript/resources/evals/subresources/runs/subresources/output_items/methods/retrieve)

client.evals.runs.outputItems.retrieve(stringoutputItemID, OutputItemRetrieveParams { eval\_id, run\_id } params, RequestOptionsoptions?): [OutputItemRetrieveResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_retrieve_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more }

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

##### ModelsExpand Collapse

OutputItemListResponse { id, created\_at, datasource\_item, 7 more }

A schema representing an evaluation run output item.

id: string

Unique identifier for the evaluation run output item.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Record<string, unknown>

Details of the input data source item.

datasource\_item\_id: number

The identifier for the data source item.

eval\_id: string

The identifier of the evaluation group.

object: "eval.run.output\_item"

The type of the object. Always “eval.run.output\_item”.

results: Array<Result>

A list of grader results for this output item.

name: string

The name of the grader.

passed: boolean

Whether the grader considered the output a pass.

score: number

The numeric score produced by the grader.

sample?: Record<string, unknown> | null

Optional sample or intermediate data produced by the grader.

type?: string

The grader type (for example, “string-check-grader”).

run\_id: string

The identifier of the evaluation run associated with this output item.

sample: Sample { error, finish\_reason, input, 7 more }

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

finish\_reason: string

The reason why the sample generation was finished.

input: Array<Input>

An array of input messages.

content: string

The content of the message.

role: string

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: number

The maximum number of tokens allowed for completion.

model: string

The model used for generating the sample.

output: Array<Output>

An array of output messages.

content?: string

The content of the message.

role?: string

The role of the message (e.g. “system”, “assistant”, “user”).

seed: number

The seed used for generating the sample.

temperature: number

The sampling temperature used.

top\_p: number

The top\_p value used for sampling.

usage: Usage { cached\_tokens, completion\_tokens, prompt\_tokens, total\_tokens }

Token usage details for the sample.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

status: string

The status of the evaluation run.

OutputItemRetrieveResponse { id, created\_at, datasource\_item, 7 more }

A schema representing an evaluation run output item.

id: string

Unique identifier for the evaluation run output item.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Record<string, unknown>

Details of the input data source item.

datasource\_item\_id: number

The identifier for the data source item.

eval\_id: string

The identifier of the evaluation group.

object: "eval.run.output\_item"

The type of the object. Always “eval.run.output\_item”.

results: Array<Result>

A list of grader results for this output item.

name: string

The name of the grader.

passed: boolean

Whether the grader considered the output a pass.

score: number

The numeric score produced by the grader.

sample?: Record<string, unknown> | null

Optional sample or intermediate data produced by the grader.

type?: string

The grader type (for example, “string-check-grader”).

run\_id: string

The identifier of the evaluation run associated with this output item.

sample: Sample { error, finish\_reason, input, 7 more }

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

finish\_reason: string

The reason why the sample generation was finished.

input: Array<Input>

An array of input messages.

content: string

The content of the message.

role: string

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: number

The maximum number of tokens allowed for completion.

model: string

The model used for generating the sample.

output: Array<Output>

An array of output messages.

content?: string

The content of the message.

role?: string

The role of the message (e.g. “system”, “assistant”, “user”).

seed: number

The seed used for generating the sample.

temperature: number

The sampling temperature used.

top\_p: number

The top\_p value used for sampling.

usage: Usage { cached\_tokens, completion\_tokens, prompt\_tokens, total\_tokens }

Token usage details for the sample.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

status: string

The status of the evaluation run.
