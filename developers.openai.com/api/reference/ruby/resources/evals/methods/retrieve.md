<!-- source: https://developers.openai.com/api/reference/ruby/resources/evals/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Evals](/api/reference/ruby/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get an eval

evals.retrieve(eval\_id) -> [EvalRetrieveResponse](/api/reference/ruby/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema)) { id, created\_at, data\_source\_config, 4 more }

GET/evals/{eval\_id}

Get an evaluation by ID.

##### ParametersExpand Collapse

eval\_id: String

##### ReturnsExpand Collapse

class EvalRetrieveResponse { id, created\_at, data\_source\_config, 4 more }

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

id: String

Unique identifier for the evaluation.

created\_at: Integer

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

data\_source\_config: [EvalCustomDataSourceConfig](/api/reference/ruby/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_custom_data_source_config%20%3E%20(schema)) { schema, type }  | Logs{ schema, type, metadata} | [EvalStoredCompletionsDataSourceConfig](/api/reference/ruby/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_stored_completions_data_source_config%20%3E%20(schema)) { schema, type, metadata }

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig { schema, type }

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Hash[Symbol, untyped]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: :custom

The type of data source. Always `custom`.

class Logs { schema, type, metadata }

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema: Hash[Symbol, untyped]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: :logs

The type of data source. Always `logs`.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig { schema, type, metadata }

Deprecated in favor of LogsDataSourceConfig.

schema: Hash[Symbol, untyped]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: :stored\_completions

The type of data source. Always `stored_completions`.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: String

The name of the evaluation.

object: :eval

The object type.

testing\_criteria: Array[[LabelModelGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20label_model_grader%20%3E%20(schema)) { input, labels, model, 3 more }  | [StringCheckGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  | [TextSimilarityGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  & { pass\_threshold} | 2 more]

A list of testing criteria.

One of the following:

class LabelModelGrader { input, labels, model, 3 more }

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: Array[Input{ content, role, type}]

content: String | [ResponseInputText](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText{ text, type} | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

GraderInputs = Array[[GraderInputItem](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))]

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

type: :message

The type of the message input. Always `message`.

labels: Array[String]

The labels to assign to each item in the evaluation.

model: String

The model to use for the evaluation. Must support structured outputs.

name: String

The name of the grader.

passing\_labels: Array[String]

The labels that indicate a passing result. Must be a subset of labels.

type: :label\_model

The object type, which is always `label_model`.

class StringCheckGrader { input, name, operation, 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: String

The input text. This may include template strings.

name: String

The name of the grader.

operation: :eq | :ne | :like | :ilike

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

:eq

:ne

:like

:ilike

reference: String

The reference text. This may include template strings.

type: :string\_check

The object type, which is always `string_check`.

class EvalGraderTextSimilarity { pass\_threshold }

A TextSimilarityGrader object which grades text based on similarity metrics.

pass\_threshold: Float

The threshold for the score.

class EvalGraderPython { pass\_threshold }

A PythonGrader object that runs a python script on the input.

pass\_threshold: Float

The threshold for the score.

class EvalGraderScoreModel { pass\_threshold }

A ScoreModelGrader object that uses a model to assign a score to the input.

pass\_threshold: Float

The threshold for the score.

### Get an eval

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

eval_ = openai.evals.retrieve("eval_id")

puts(eval_)

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
  "name": "External Data Eval",
  "created_at": 1739314509,
  "metadata": {},

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
  "name": "External Data Eval",
  "created_at": 1739314509,
  "metadata": {},
