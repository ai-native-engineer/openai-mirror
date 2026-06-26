<!-- source: https://developers.openai.com/api/reference/cli/resources/batches/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Batches

Create large batches of API requests to run asynchronously.

##### [Create batch](/api/reference/cli/resources/batches/methods/create)

$ openai batches create

POST/batches

##### [Retrieve batch](/api/reference/cli/resources/batches/methods/retrieve)

$ openai batches retrieve

GET/batches/{batch\_id}

##### [Cancel batch](/api/reference/cli/resources/batches/methods/cancel)

$ openai batches cancel

POST/batches/{batch\_id}/cancel

##### [List batches](/api/reference/cli/resources/batches/methods/list)

$ openai batches list

GET/batches

##### ModelsExpand Collapse

batch: object { id, completion\_window, created\_at, 19 more }

id: string

completion\_window: string

The time frame within which the batch should be processed.

created\_at: number

The Unix timestamp (in seconds) for when the batch was created.

endpoint: string

The OpenAI API endpoint used by the batch.

input\_file\_id: string

The ID of the input file for the batch.

object: "batch"

The object type, which is always `batch`.

status: "validating" or "failed" or "in\_progress" or 5 more

The current status of the batch.

"validating"

"failed"

"in\_progress"

"finalizing"

"completed"

"expired"

"cancelling"

"cancelled"

cancelled\_at: optional number

The Unix timestamp (in seconds) for when the batch was cancelled.

cancelling\_at: optional number

The Unix timestamp (in seconds) for when the batch started cancelling.

completed\_at: optional number

The Unix timestamp (in seconds) for when the batch was completed.

error\_file\_id: optional string

The ID of the file containing the outputs of requests with errors.

errors: optional object { data, object }

data: optional array of [BatchError](/api/reference/cli/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)) { code, line, message, param }

code: optional string

An error code identifying the error type.

line: optional number

The line number of the input file where the error occurred, if applicable.

message: optional string

A human-readable message providing more details about the error.

param: optional string

The name of the parameter that caused the error, if applicable.

object: optional string

The object type, which is always `list`.

expired\_at: optional number

The Unix timestamp (in seconds) for when the batch expired.

expires\_at: optional number

The Unix timestamp (in seconds) for when the batch will expire.

failed\_at: optional number

The Unix timestamp (in seconds) for when the batch failed.

finalizing\_at: optional number

The Unix timestamp (in seconds) for when the batch started finalizing.

in\_progress\_at: optional number

The Unix timestamp (in seconds) for when the batch started processing.

metadata: optional map[string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: optional string

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

output\_file\_id: optional string

The ID of the file containing the outputs of successfully executed requests.

request\_counts: optional object { completed, failed, total }

The request counts for different statuses within the batch.

completed: number

Number of requests that have been completed successfully.

failed: number

Number of requests that have failed.

total: number

Total number of requests in the batch.

usage: optional object { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: object { cached\_tokens }

A detailed breakdown of the input tokens.

cached\_tokens: number

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: object { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

batch\_error: object { code, line, message, param }

code: optional string

An error code identifying the error type.

line: optional number

The line number of the input file where the error occurred, if applicable.

message: optional string

A human-readable message providing more details about the error.

param: optional string

The name of the parameter that caused the error, if applicable.

batch\_request\_counts: object { completed, failed, total }

The request counts for different statuses within the batch.

completed: number

Number of requests that have been completed successfully.

failed: number

Number of requests that have failed.

total: number

Total number of requests in the batch.

batch\_usage: object { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: object { cached\_tokens }

A detailed breakdown of the input tokens.

cached\_tokens: number

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: object { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.
