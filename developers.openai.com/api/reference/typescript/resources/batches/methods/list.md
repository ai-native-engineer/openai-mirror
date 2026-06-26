<!-- source: https://developers.openai.com/api/reference/typescript/resources/batches/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Batches](/api/reference/typescript/resources/batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List batches

client.batches.list(BatchListParams { after, limit } query?, RequestOptionsoptions?): CursorPage<[Batch](/api/reference/typescript/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)) { id, completion\_window, created\_at, 19 more } >

GET/batches

List your organization’s batches.

##### ParametersExpand Collapse

query: BatchListParams { after, limit }

after?: string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit?: number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

Batch { id, completion\_window, created\_at, 19 more }

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

status: "validating" | "failed" | "in\_progress" | 5 more

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

cancelled\_at?: number

The Unix timestamp (in seconds) for when the batch was cancelled.

formatunixtime

cancelling\_at?: number

The Unix timestamp (in seconds) for when the batch started cancelling.

formatunixtime

completed\_at?: number

The Unix timestamp (in seconds) for when the batch was completed.

formatunixtime

error\_file\_id?: string

The ID of the file containing the outputs of requests with errors.

errors?: Errors { data, object }

data?: Array<[BatchError](/api/reference/typescript/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema)) { code, line, message, param } >

code?: string

An error code identifying the error type.

line?: number | null

The line number of the input file where the error occurred, if applicable.

message?: string

A human-readable message providing more details about the error.

param?: string | null

The name of the parameter that caused the error, if applicable.

object?: string

The object type, which is always `list`.

expired\_at?: number

The Unix timestamp (in seconds) for when the batch expired.

formatunixtime

expires\_at?: number

The Unix timestamp (in seconds) for when the batch will expire.

formatunixtime

failed\_at?: number

The Unix timestamp (in seconds) for when the batch failed.

formatunixtime

finalizing\_at?: number

The Unix timestamp (in seconds) for when the batch started finalizing.

formatunixtime

in\_progress\_at?: number

The Unix timestamp (in seconds) for when the batch started processing.

formatunixtime

metadata?: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model?: string

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

output\_file\_id?: string

The ID of the file containing the outputs of successfully executed requests.

request\_counts?: [BatchRequestCounts](/api/reference/typescript/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema)) { completed, failed, total }

The request counts for different statuses within the batch.

completed: number

Number of requests that have been completed successfully.

failed: number

Number of requests that have failed.

total: number

Total number of requests in the batch.

usage?: [BatchUsage](/api/reference/typescript/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: InputTokensDetails { cached\_tokens }

A detailed breakdown of the input tokens.

cached\_tokens: number

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: OutputTokensDetails { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

### List batches

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const list = await openai.batches.list();

  for await (const batch of list) {
    console.log(batch);

main();

  "object": "list",
  "data": [
      "id": "batch_abc123",
      "object": "batch",
      "endpoint": "/v1/chat/completions",
      "errors": null,
      "input_file_id": "file-abc123",
      "completion_window": "24h",
      "status": "completed",
      "output_file_id": "file-cvaTdG",
      "error_file_id": "file-HOWS94",
      "created_at": 1711471533,
      "in_progress_at": 1711471538,
      "expires_at": 1711557933,
      "finalizing_at": 1711493133,
      "completed_at": 1711493163,
      "failed_at": null,
      "expired_at": null,
      "cancelling_at": null,
      "cancelled_at": null,
      "request_counts": {
        "total": 100,
        "completed": 95,
        "failed": 5
      "metadata": {
        "customer_id": "user_123456789",
        "batch_description": "Nightly job",
    { ... },
  ],
  "first_id": "batch_abc123",
  "last_id": "batch_abc456",
  "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
      "id": "batch_abc123",
      "object": "batch",
      "endpoint": "/v1/chat/completions",
      "errors": null,
      "input_file_id": "file-abc123",
      "completion_window": "24h",
      "status": "completed",
      "output_file_id": "file-cvaTdG",
      "error_file_id": "file-HOWS94",
      "created_at": 1711471533,
      "in_progress_at": 1711471538,
      "expires_at": 1711557933,
      "finalizing_at": 1711493133,
      "completed_at": 1711493163,
      "failed_at": null,
      "expired_at": null,
      "cancelling_at": null,
      "cancelled_at": null,
      "request_counts": {
        "total": 100,
        "completed": 95,
        "failed": 5
      "metadata": {
        "customer_id": "user_123456789",
        "batch_description": "Nightly job",
    { ... },
  ],
  "first_id": "batch_abc123",
  "last_id": "batch_abc456",
  "has_more": true
