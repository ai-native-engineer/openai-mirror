<!-- source: https://developers.openai.com/api/reference/java/resources/batches/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Batches](/api/reference/java/resources/batches)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve batch

[Batch](/api/reference/java/resources/batches#(resource)%20batches%20%3E%20(model)%20batch%20%3E%20(schema)) batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/batches/{batch\_id}

Retrieves a batch.

##### ParametersExpand Collapse

BatchRetrieveParams params

Optional<String> batchId

##### ReturnsExpand Collapse

class Batch:

String id

String completionWindow

The time frame within which the batch should be processed.

long createdAt

The Unix timestamp (in seconds) for when the batch was created.

formatunixtime

String endpoint

The OpenAI API endpoint used by the batch.

String inputFileId

The ID of the input file for the batch.

JsonValue; object\_ "batch"constant"batch"constant

The object type, which is always `batch`.

Status status

The current status of the batch.

One of the following:

VALIDATING("validating")

FAILED("failed")

IN\_PROGRESS("in\_progress")

FINALIZING("finalizing")

COMPLETED("completed")

EXPIRED("expired")

CANCELLING("cancelling")

CANCELLED("cancelled")

Optional<Long> cancelledAt

The Unix timestamp (in seconds) for when the batch was cancelled.

formatunixtime

Optional<Long> cancellingAt

The Unix timestamp (in seconds) for when the batch started cancelling.

formatunixtime

Optional<Long> completedAt

The Unix timestamp (in seconds) for when the batch was completed.

formatunixtime

Optional<String> errorFileId

The ID of the file containing the outputs of requests with errors.

Optional<Errors> errors

Optional<List<[BatchError](/api/reference/java/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_error%20%3E%20(schema))>> data

Optional<String> code

An error code identifying the error type.

Optional<Long> line

The line number of the input file where the error occurred, if applicable.

Optional<String> message

A human-readable message providing more details about the error.

Optional<String> param

The name of the parameter that caused the error, if applicable.

Optional<String> object\_

The object type, which is always `list`.

Optional<Long> expiredAt

The Unix timestamp (in seconds) for when the batch expired.

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the batch will expire.

formatunixtime

Optional<Long> failedAt

The Unix timestamp (in seconds) for when the batch failed.

formatunixtime

Optional<Long> finalizingAt

The Unix timestamp (in seconds) for when the batch started finalizing.

formatunixtime

Optional<Long> inProgressAt

The Unix timestamp (in seconds) for when the batch started processing.

formatunixtime

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<String> model

Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

Optional<String> outputFileId

The ID of the file containing the outputs of successfully executed requests.

Optional<[BatchRequestCounts](/api/reference/java/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_request_counts%20%3E%20(schema))> requestCounts

The request counts for different statuses within the batch.

long completed

Number of requests that have been completed successfully.

long failed

Number of requests that have failed.

long total

Total number of requests in the batch.

Optional<[BatchUsage](/api/reference/java/resources/batches#(resource)%20batches%20%3E%20(model)%20batch_usage%20%3E%20(schema))> usage

Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

long inputTokens

The number of input tokens.

InputTokensDetails inputTokensDetails

A detailed breakdown of the input tokens.

long cachedTokens

The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

long outputTokens

The number of output tokens.

OutputTokensDetails outputTokensDetails

A detailed breakdown of the output tokens.

long reasoningTokens

The number of reasoning tokens.

long totalTokens

The total number of tokens used.

### Retrieve batch

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.batches.Batch;
import com.openai.models.batches.BatchRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Batch batch = client.batches().retrieve("batch_id");

  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/completions",
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
    "batch_description": "Nightly eval job",

##### Returns Examples

  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/completions",
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
    "batch_description": "Nightly eval job",
