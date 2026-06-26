<!-- source: https://developers.openai.com/api/reference/java/resources/evals/methods/update/ -->

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

# Update an eval

[EvalUpdateResponse](/api/reference/java/resources/evals#(resource)%20evals%20%3E%20(model)%20EvalUpdateResponse%20%3E%20(schema)) evals().update(EvalUpdateParamsparams = EvalUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/evals/{eval\_id}

Update certain properties of an evaluation.

##### ParametersExpand Collapse

EvalUpdateParams params

Optional<String> evalId

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<String> name

Rename the evaluation.

##### ReturnsExpand Collapse

class EvalUpdateResponse:

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

### Update an eval

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
import com.openai.models.evals.EvalUpdateParams;
import com.openai.models.evals.EvalUpdateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalUpdateResponse eval = client.evals().update("eval_id");

  "object": "eval",
  "id": "eval_67abd54d9b0081909a86353f6fb9317a",
  "data_source_config": {
    "type": "custom",
    "schema": {
      "type": "object",
      "properties": {
        "item": {
          "type": "object",
          "properties": {
            "input": {
              "type": "string"
            "ground_truth": {
              "type": "string"
          "required": [
            "input",
            "ground_truth"
          ]
      "required": [
        "item"
      ]
  "testing_criteria": [
      "name": "String check",
      "id": "String check-2eaf2d8d-d649-4335-8148-9535a7ca73c2",
      "type": "string_check",
      "input": "{{item.input}}",
      "reference": "{{item.ground_truth}}",
      "operation": "eq"
  ],
  "name": "Updated Eval",
  "created_at": 1739314509,
  "metadata": {"description": "Updated description"},

##### Returns Examples

  "object": "eval",
  "id": "eval_67abd54d9b0081909a86353f6fb9317a",
  "data_source_config": {
    "type": "custom",
    "schema": {
      "type": "object",
      "properties": {
        "item": {
          "type": "object",
          "properties": {
            "input": {
              "type": "string"
            "ground_truth": {
              "type": "string"
          "required": [
            "input",
            "ground_truth"
          ]
      "required": [
        "item"
      ]
  "testing_criteria": [
      "name": "String check",
      "id": "String check-2eaf2d8d-d649-4335-8148-9535a7ca73c2",
      "type": "string_check",
      "input": "{{item.input}}",
      "reference": "{{item.ground_truth}}",
      "operation": "eq"
  ],
  "name": "Updated Eval",
  "created_at": 1739314509,
  "metadata": {"description": "Updated description"},
