<!-- source: https://developers.openai.com/api/reference/python/resources/evals/subresources/runs/subresources/output_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Evals](/api/reference/python/resources/evals)

[Runs](/api/reference/python/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Output Items

Manage and run evals in the OpenAI platform.

##### [Get eval run output items](/api/reference/python/resources/evals/subresources/runs/subresources/output_items/methods/list)

evals.runs.output\_items.list(strrun\_id, OutputItemListParams\*\*kwargs)  -> SyncCursorPage[[OutputItemListResponse](/api/reference/python/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_list_response%20%3E%20(schema))]

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

##### [Get an output item of an eval run](/api/reference/python/resources/evals/subresources/runs/subresources/output_items/methods/retrieve)

evals.runs.output\_items.retrieve(stroutput\_item\_id, OutputItemRetrieveParams\*\*kwargs)  -> [OutputItemRetrieveResponse](/api/reference/python/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_retrieve_response%20%3E%20(schema))

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

##### ModelsExpand Collapse

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

class OutputItemRetrieveResponse: …

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
