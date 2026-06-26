<!-- source: https://developers.openai.com/api/reference/python/resources/batches/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Batches

Create large batches of API requests to run asynchronously.

##### [Create batch](/api/reference/python/resources/batches/methods/create)

batches.create(BatchCreateParams\*\*kwargs)  -> [Batch](/api/reference/python/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema))

POST/batches

##### [Retrieve batch](/api/reference/python/resources/batches/methods/retrieve)

batches.retrieve(strbatch\_id)  -> [Batch](/api/reference/python/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema))

GET/batches/{batch\_id}

##### [Cancel batch](/api/reference/python/resources/batches/methods/cancel)

batches.cancel(strbatch\_id)  -> [Batch](/api/reference/python/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema))

POST/batches/{batch\_id}/cancel

##### [List batches](/api/reference/python/resources/batches/methods/list)

batches.list(BatchListParams\*\*kwargs)  -> SyncCursorPage[[Batch](/api/reference/python/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema))]

GET/batches

##### ModelsExpand Collapse

class Batch: …

id: str

completion\_window: str

The time frame within which the batch should be processed.

created\_at: int

The Unix timestamp (in seconds) for when the batch was created.

formatunixtime

endpoint: str

The OpenAI API endpoint used by the batch.

input\_file\_id: str

The ID of the input file for the batch.

object: Literal["batch"]

The object type, which is always `batch`.

status: Literal["validating", "failed", "in\_progress", 5 more]

The current status of the batch.

One of the following:

"validating"

"failed"

"in\_progress"

"finalizing"

"completed"

"expired"

"cancelling"

"cancelled"

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch was cancelled.

formatunixtime

cancelling\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch started cancelling.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch was completed.

formatunixtime

error\_file\_id: Optional[str]

The ID of the file containing the outputs of requests with errors.

errors: Optional[Errors]

data: Optional[List[[BatchError](/api/reference/python/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema))]]

code: Optional[str]

An error code identifying the error type.

line: Optional[int]

The line number of the input file where the error occurred, if applicable.

message: Optional[str]

A human-readable message providing more details about the error.

param: Optional[str]

The name of the parameter that caused the error, if applicable.

object: Optional[str]

The object type, which is always `list`.

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch expired.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch failed.

formatunixtime

finalizing\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch started finalizing.

formatunixtime

in\_progress\_at: Optional[int]

The Unix timestamp (in seconds) for when the batch started processing.

formatunixtime

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[str]

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

output\_file\_id: Optional[str]

The ID of the file containing the outputs of successfully executed requests.

request\_counts: Optional[BatchRequestCounts]

The request counts for different statuses within the batch.

usage: Optional[BatchUsage]

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

class BatchError: …

code: Optional[str]

An error code identifying the error type.

line: Optional[int]

The line number of the input file where the error occurred, if applicable.

message: Optional[str]

A human-readable message providing more details about the error.

param: Optional[str]

The name of the parameter that caused the error, if applicable.

class BatchRequestCounts: …

The request counts for different statuses within the batch.

completed: int

Number of requests that have been completed successfully.

failed: int

Number of requests that have failed.

total: int

Total number of requests in the batch.

class BatchUsage: …

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input\_tokens: int

The number of input tokens.

input\_tokens\_details: InputTokensDetails

A detailed breakdown of the input tokens.

cached\_tokens: int

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: int

The number of output tokens.

output\_tokens\_details: OutputTokensDetails

A detailed breakdown of the output tokens.

reasoning\_tokens: int

The number of reasoning tokens.

total\_tokens: int

The total number of tokens used.
