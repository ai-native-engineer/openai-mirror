<!-- source: https://developers.openai.com/api/reference/go/resources/batches/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Batches](/api/reference/go/resources/batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create batch

client.Batches.New(ctx, body) (\*[Batch](/api/reference/go/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)), error)

POST/batches

Creates and executes a batch from an uploaded file of requests

##### ParametersExpand Collapse

body BatchNewParams

CompletionWindow param.Field[[BatchNewParamsCompletionWindow](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20completion_window%20%3E%20(schema))]

The time frame within which the batch should be processed. Currently only `24h` is supported.

const BatchNewParamsCompletionWindow24h [BatchNewParamsCompletionWindow](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20completion_window%20%3E%20(schema)) = "24h"

Endpoint param.Field[[BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema))]

The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, and `/v1/videos` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

const BatchNewParamsEndpointV1Responses [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/responses"

const BatchNewParamsEndpointV1ChatCompletions [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/chat/completions"

const BatchNewParamsEndpointV1Embeddings [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/embeddings"

const BatchNewParamsEndpointV1Completions [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/completions"

const BatchNewParamsEndpointV1Moderations [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/moderations"

const BatchNewParamsEndpointV1ImagesGenerations [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/images/generations"

const BatchNewParamsEndpointV1ImagesEdits [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/images/edits"

const BatchNewParamsEndpointV1Videos [BatchNewParamsEndpoint](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20endpoint%20%3E%20(schema)) = "/v1/videos"

InputFileID param.Field[string]

The ID of an uploaded file that contains requests for the new batch.

See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

Metadata param.Field[[Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

OutputExpiresAfter param.Field[[BatchNewParamsOutputExpiresAfter](/api/reference/go/resources/batches/methods/create#(resource)%20batches%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20output_expires_after%20%3E%20(schema))]Optional

The expiration policy for the output and/or error file that are generated for a batch.

Anchor CreatedAt

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created.

Seconds int64

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

type Batch struct{…}

ID string

CompletionWindow string

The time frame within which the batch should be processed.

CreatedAt int64

The Unix timestamp (in seconds) for when the batch was created.

formatunixtime

Endpoint string

The OpenAI API endpoint used by the batch.

InputFileID string

The ID of the input file for the batch.

Object Batch

The object type, which is always `batch`.

Status BatchStatus

The current status of the batch.

One of the following:

const BatchStatusValidating BatchStatus = "validating"

const BatchStatusFailed BatchStatus = "failed"

const BatchStatusInProgress BatchStatus = "in\_progress"

const BatchStatusFinalizing BatchStatus = "finalizing"

const BatchStatusCompleted BatchStatus = "completed"

const BatchStatusExpired BatchStatus = "expired"

const BatchStatusCancelling BatchStatus = "cancelling"

const BatchStatusCancelled BatchStatus = "cancelled"

CancelledAt int64Optional

The Unix timestamp (in seconds) for when the batch was cancelled.

formatunixtime

CancellingAt int64Optional

The Unix timestamp (in seconds) for when the batch started cancelling.

formatunixtime

CompletedAt int64Optional

The Unix timestamp (in seconds) for when the batch was completed.

formatunixtime

ErrorFileID stringOptional

The ID of the file containing the outputs of requests with errors.

Errors BatchErrorsOptional

Data [][BatchError](/api/reference/go/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema))Optional

Code stringOptional

An error code identifying the error type.

Line int64Optional

The line number of the input file where the error occurred, if applicable.

Message stringOptional

A human-readable message providing more details about the error.

Param stringOptional

The name of the parameter that caused the error, if applicable.

Object stringOptional

The object type, which is always `list`.

ExpiredAt int64Optional

The Unix timestamp (in seconds) for when the batch expired.

formatunixtime

ExpiresAt int64Optional

The Unix timestamp (in seconds) for when the batch will expire.

formatunixtime

FailedAt int64Optional

The Unix timestamp (in seconds) for when the batch failed.

formatunixtime

FinalizingAt int64Optional

The Unix timestamp (in seconds) for when the batch started finalizing.

formatunixtime

InProgressAt int64Optional

The Unix timestamp (in seconds) for when the batch started processing.

formatunixtime

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model stringOptional

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

OutputFileID stringOptional

The ID of the file containing the outputs of successfully executed requests.

RequestCounts [BatchRequestCounts](/api/reference/go/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema))Optional

The request counts for different statuses within the batch.

Completed int64

Number of requests that have been completed successfully.

Failed int64

Number of requests that have failed.

Total int64

Total number of requests in the batch.

Usage [BatchUsage](/api/reference/go/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema))Optional

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

InputTokens int64

The number of input tokens.

InputTokensDetails BatchUsageInputTokensDetails

A detailed breakdown of the input tokens.

CachedTokens int64

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

OutputTokens int64

The number of output tokens.

OutputTokensDetails BatchUsageOutputTokensDetails

A detailed breakdown of the output tokens.

ReasoningTokens int64

The number of reasoning tokens.

TotalTokens int64

The total number of tokens used.

### Create batch

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  batch, err := client.Batches.New(context.TODO(), openai.BatchNewParams{
    CompletionWindow: openai.BatchNewParamsCompletionWindow24h,
    Endpoint: openai.BatchNewParamsEndpointV1Responses,
    InputFileID: "input_file_id",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", batch.ID)

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
