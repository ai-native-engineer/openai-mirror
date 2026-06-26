<!-- source: https://developers.openai.com/api/reference/ruby/resources/batches/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Batches](/api/reference/ruby/resources/batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create batch

batches.create(\*\*kwargs) -> [Batch](/api/reference/ruby/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)) { id, completion\_window, created\_at, 19 more }

POST/batches

Creates and executes a batch from an uploaded file of requests

##### ParametersExpand Collapse

completion\_window: :"24h"

The time frame within which the batch should be processed. Currently only `24h` is supported.

endpoint: :"/v1/responses" | :"/v1/chat/completions" | :"/v1/embeddings" | 5 more

The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, and `/v1/videos` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

One of the following:

:"/v1/responses"

:"/v1/chat/completions"

:"/v1/embeddings"

:"/v1/completions"

:"/v1/moderations"

:"/v1/images/generations"

:"/v1/images/edits"

:"/v1/videos"

input\_file\_id: String

The ID of an uploaded file that contains requests for the new batch.

See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

output\_expires\_after: OutputExpiresAfter{ anchor, seconds}

The expiration policy for the output and/or error file that are generated for a batch.

anchor: :created\_at

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created.

seconds: Integer

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

class Batch { id, completion\_window, created\_at, 19 more }

id: String

completion\_window: String

The time frame within which the batch should be processed.

created\_at: Integer

The Unix timestamp (in seconds) for when the batch was created.

formatunixtime

endpoint: String

The OpenAI API endpoint used by the batch.

input\_file\_id: String

The ID of the input file for the batch.

object: :batch

The object type, which is always `batch`.

status: :validating | :failed | :in\_progress | 5 more

The current status of the batch.

One of the following:

:validating

:failed

:in\_progress

:finalizing

:completed

:expired

:cancelling

:cancelled

cancelled\_at: Integer

The Unix timestamp (in seconds) for when the batch was cancelled.

formatunixtime

cancelling\_at: Integer

The Unix timestamp (in seconds) for when the batch started cancelling.

formatunixtime

completed\_at: Integer

The Unix timestamp (in seconds) for when the batch was completed.

formatunixtime

error\_file\_id: String

The ID of the file containing the outputs of requests with errors.

errors: Errors{ data, object}

data: Array[[BatchError](/api/reference/ruby/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)) { code, line, message, param } ]

code: String

An error code identifying the error type.

line: Integer

The line number of the input file where the error occurred, if applicable.

message: String

A human-readable message providing more details about the error.

param: String

The name of the parameter that caused the error, if applicable.

object: String

The object type, which is always `list`.

expired\_at: Integer

The Unix timestamp (in seconds) for when the batch expired.

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) for when the batch will expire.

formatunixtime

failed\_at: Integer

The Unix timestamp (in seconds) for when the batch failed.

formatunixtime

finalizing\_at: Integer

The Unix timestamp (in seconds) for when the batch started finalizing.

formatunixtime

in\_progress\_at: Integer

The Unix timestamp (in seconds) for when the batch started processing.

formatunixtime

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: String

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

output\_file\_id: String

The ID of the file containing the outputs of successfully executed requests.

request\_counts: [BatchRequestCounts](/api/reference/ruby/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)) { completed, failed, total }

The request counts for different statuses within the batch.

completed: Integer

Number of requests that have been completed successfully.

failed: Integer

Number of requests that have failed.

total: Integer

Total number of requests in the batch.

usage: [BatchUsage](/api/reference/ruby/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input\_tokens: Integer

The number of input tokens.

input\_tokens\_details: InputTokensDetails{ cached\_tokens}

A detailed breakdown of the input tokens.

cached\_tokens: Integer

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: Integer

The number of output tokens.

output\_tokens\_details: OutputTokensDetails{ reasoning\_tokens}

A detailed breakdown of the output tokens.

reasoning\_tokens: Integer

The number of reasoning tokens.

total\_tokens: Integer

The total number of tokens used.

### Create batch

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

batch = openai.batches.create(
  completion_window: :"24h",
  endpoint: :"/v1/responses",
  input_file_id: "input_file_id"

puts(batch)

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
