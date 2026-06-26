<!-- source: https://developers.openai.com/api/reference/java/resources/evals/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Evals](/api/reference/java/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List evals

EvalListPage evals().list(EvalListParamsparams = EvalListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/evals

List evaluations for a project.

##### ParametersExpand Collapse

EvalListParams params

Optional<String> after

Identifier for the last eval from the previous pagination request.

Optional<Long> limit

Number of evals to retrieve.

Optional<[Order](/api/reference/java/resources/evals/methods/list#(resource)%20evals%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for evals by timestamp. Use `asc` for ascending order or `desc` for descending order.

ASC("asc")

DESC("desc")

Optional<[OrderBy](/api/reference/java/resources/evals/methods/list#(resource)%20evals%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order_by%20%3E%20(schema))> orderBy

Evals can be ordered by creation time or last updated time. Use
`created_at` for creation time or `updated_at` for last updated time.

CREATED\_AT("created\_at")

UPDATED\_AT("updated\_at")

##### ReturnsExpand Collapse

class EvalListResponse:

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

String id

Unique identifier for the evaluation.

long createdAt

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

DataSourceConfig dataSourceConfig

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig:

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

Schema schema

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "custom"constant"custom"constant

The type of data source. Always `custom`.

class Logs:

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

Schema schema

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "logs"constant"logs"constant

The type of data source. Always `logs`.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig:

Deprecated in favor of LogsDataSourceConfig.

Schema schema

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "stored\_completions"constant"stored\_completions"constant

The type of data source. Always `stored_completions`.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

String name

The name of the evaluation.

JsonValue; object\_ "eval"constant"eval"constant

The object type.

List<TestingCriterion> testingCriteria

A list of testing criteria.

One of the following:

class LabelModelGrader:

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

List<Input> input

Content content

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class OutputText:

A text output from the model.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

class InputImage:

An image input block used within EvalItem content arrays.

String imageUrl

The URL of the image input.

formaturi

JsonValue; type "input\_image"constant"input\_image"constant

The type of the image input. Always `input_image`.

Optional<String> detail

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

List<[EvalContentItem](/api/reference/java/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))>

One of the following:

String

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

OutputText

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

InputImage

String imageUrl

The URL of the image input.

formaturi

JsonValue; type "input\_image"constant"input\_image"constant

The type of the image input. Always `input_image`.

Optional<String> detail

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Type> type

The type of the message input. Always `message`.

List<String> labels

The labels to assign to each item in the evaluation.

String model

The model to use for the evaluation. Must support structured outputs.

String name

The name of the grader.

List<String> passingLabels

The labels that indicate a passing result. Must be a subset of labels.

JsonValue; type "label\_model"constant"label\_model"constant

The object type, which is always `label_model`.

class StringCheckGrader:

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

String input

The input text. This may include template strings.

String name

The name of the grader.

Operation operation

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

EQ("eq")

NE("ne")

LIKE("like")

ILIKE("ilike")

String reference

The reference text. This may include template strings.

JsonValue; type "string\_check"constant"string\_check"constant

The object type, which is always `string_check`.

class EvalGraderTextSimilarity:

A TextSimilarityGrader object which grades text based on similarity metrics.

double passThreshold

The threshold for the score.

class EvalGraderPython:

A PythonGrader object that runs a python script on the input.

Optional<Double> passThreshold

The threshold for the score.

class EvalGraderScoreModel:

A ScoreModelGrader object that uses a model to assign a score to the input.

Optional<Double> passThreshold

The threshold for the score.

### List evals

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
import com.openai.models.evals.EvalListPage;
import com.openai.models.evals.EvalListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalListPage page = client.evals().list();

  "object": "list",
  "data": [
      "id": "eval_67abd54d9b0081909a86353f6fb9317a",
      "object": "eval",
      "data_source_config": {
        "type": "stored_completions",
        "metadata": {
          "usecase": "push_notifications_summarizer"
        "schema": {
          "type": "object",
          "properties": {
            "item": {
              "type": "object"
            "sample": {
              "type": "object"
          "required": [
            "item",
            "sample"
          ]
      "testing_criteria": [
          "name": "Push Notification Summary Grader",
          "id": "Push Notification Summary Grader-9b876f24-4762-4be9-aff4-db7a9b31c673",
          "type": "label_model",
          "model": "o3-mini",
          "input": [
              "type": "message",
              "role": "developer",
              "content": {
                "type": "input_text",
                "text": "\nLabel the following push notification summary as either correct or incorrect.\nThe push notification and the summary will be provided below.\nA good push notificiation summary is concise and snappy.\nIf it is good, then label it as correct, if not, then incorrect.\n"
              "type": "message",
              "role": "user",
              "content": {
                "type": "input_text",
                "text": "\nPush notifications: {{item.input}}\nSummary: {{sample.output_text}}\n"
          ],
          "passing_labels": [
            "correct"
          ],
          "labels": [
            "correct",
            "incorrect"
          ],
          "sampling_params": null
      ],
      "name": "Push Notification Summary Grader",
      "created_at": 1739314509,
      "metadata": {
        "description": "A stored completions eval for push notification summaries"
  ],
  "first_id": "eval_67abd54d9b0081909a86353f6fb9317a",
  "last_id": "eval_67aa884cf6688190b58f657d4441c8b7",
  "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
      "id": "eval_67abd54d9b0081909a86353f6fb9317a",
      "object": "eval",
      "data_source_config": {
        "type": "stored_completions",
        "metadata": {
          "usecase": "push_notifications_summarizer"
        "schema": {
          "type": "object",
          "properties": {
            "item": {
              "type": "object"
            "sample": {
              "type": "object"
          "required": [
            "item",
            "sample"
          ]
      "testing_criteria": [
          "name": "Push Notification Summary Grader",
          "id": "Push Notification Summary Grader-9b876f24-4762-4be9-aff4-db7a9b31c673",
          "type": "label_model",
          "model": "o3-mini",
          "input": [
              "type": "message",
              "role": "developer",
              "content": {
                "type": "input_text",
                "text": "\nLabel the following push notification summary as either correct or incorrect.\nThe push notification and the summary will be provided below.\nA good push notificiation summary is concise and snappy.\nIf it is good, then label it as correct, if not, then incorrect.\n"
              "type": "message",
              "role": "user",
              "content": {
                "type": "input_text",
                "text": "\nPush notifications: {{item.input}}\nSummary: {{sample.output_text}}\n"
          ],
          "passing_labels": [
            "correct"
          ],
          "labels": [
            "correct",
            "incorrect"
          ],
          "sampling_params": null
      ],
      "name": "Push Notification Summary Grader",
      "created_at": 1739314509,
      "metadata": {
        "description": "A stored completions eval for push notification summaries"
  ],
  "first_id": "eval_67abd54d9b0081909a86353f6fb9317a",
  "last_id": "eval_67aa884cf6688190b58f657d4441c8b7",
  "has_more": true
