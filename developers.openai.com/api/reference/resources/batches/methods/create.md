<!-- source: https://developers.openai.com/api/reference/resources/batches/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Batches](/api/reference/resources/batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create batch

POST/batches

Creates and executes a batch from an uploaded file of requests

##### Body ParametersJSONExpand Collapse

completion\_window: "24h"

The time frame within which the batch should be processed. Currently only `24h` is supported.

endpoint: "/v1/responses" or "/v1/chat/completions" or "/v1/embeddings" or 5 more

The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, and `/v1/videos` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

One of the following:

"/v1/responses"

"/v1/chat/completions"

"/v1/embeddings"

"/v1/completions"

"/v1/moderations"

"/v1/images/generations"

"/v1/images/edits"

"/v1/videos"

input\_file\_id: string

The ID of an uploaded file that contains requests for the new batch.

See [upload file](/docs/api-reference/files/create) for how to upload a file.

Your input file must be formatted as a [JSONL file](/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

metadata: optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

output\_expires\_after: optional object { anchor, seconds }

The expiration policy for the output and/or error file that are generated for a batch.

anchor: "created\_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created.

seconds: number

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

Batch object { id, completion\_window, created\_at, 19 more }

id: string

completion\_window: string

The time frame within which the batch should be processed.

created\_at: number

The Unix timestamp (in seconds) for when the batch was created.

formatunixtime

endpoint: string

The OpenAI API endpoint used by the batch.

input\_file\_id: string

The ID of the input file for the batch.

object: "batch"

The object type, which is always `batch`.

status: "validating" or "failed" or "in\_progress" or 5 more

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

cancelled\_at: optional number

The Unix timestamp (in seconds) for when the batch was cancelled.

formatunixtime

cancelling\_at: optional number

The Unix timestamp (in seconds) for when the batch started cancelling.

formatunixtime

completed\_at: optional number

The Unix timestamp (in seconds) for when the batch was completed.

formatunixtime

error\_file\_id: optional string

The ID of the file containing the outputs of requests with errors.

errors: optional object { data, object }

data: optional array of object { code, line, message, param }

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

formatunixtime

expires\_at: optional number

The Unix timestamp (in seconds) for when the batch will expire.

formatunixtime

failed\_at: optional number

The Unix timestamp (in seconds) for when the batch failed.

formatunixtime

finalizing\_at: optional number

The Unix timestamp (in seconds) for when the batch started finalizing.

formatunixtime

in\_progress\_at: optional number

The Unix timestamp (in seconds) for when the batch started processing.

formatunixtime

metadata: optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: optional string

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](/docs/models) to browse and compare available models.

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

usage: optional [BatchUsage](/api/reference/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: object { cached\_tokens }

A detailed breakdown of the input tokens.

cached\_tokens: number

The number of tokens that were retrieved from the cache. [More on
prompt caching](/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: object { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

### Create batch

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/batches \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-abc123",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
  }'

  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "validating",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1711471533,
  "in_progress_at": null,
  "expires_at": null,
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": null,
  "cancelled_at": null,
  "request_counts": {
    "total": 0,
    "completed": 0,
    "failed": 0
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "Nightly eval job",

##### Returns Examples

  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "validating",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1711471533,
  "in_progress_at": null,
  "expires_at": null,
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": null,
  "cancelled_at": null,
  "request_counts": {
    "total": 0,
    "completed": 0,
    "failed": 0
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "Nightly eval job",
