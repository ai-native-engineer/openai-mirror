<!-- source: https://developers.openai.com/api/reference/python/resources/evals/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Evals](/api/reference/python/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update an eval

evals.update(streval\_id, EvalUpdateParams\*\*kwargs)  -> [EvalUpdateResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema))

POST/evals/{eval\_id}

Update certain properties of an evaluation.

##### ParametersExpand Collapse

eval\_id: str

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: Optional[str]

Rename the evaluation.

##### ReturnsExpand Collapse

class EvalUpdateResponse: …

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

id: str

Unique identifier for the evaluation.

created\_at: int

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

data\_source\_config: DataSourceConfig

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig: …

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["custom"]

The type of data source. Always `custom`.

class DataSourceConfigLogs: …

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["logs"]

The type of data source. Always `logs`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig: …

Deprecated in favor of LogsDataSourceConfig.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["stored\_completions"]

The type of data source. Always `stored_completions`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the evaluation.

object: Literal["eval"]

The object type.

testing\_criteria: List[TestingCriterion]

A list of testing criteria.

One of the following:

class LabelModelGrader: …

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: List[Input]

content: InputContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

labels: List[str]

The labels to assign to each item in the evaluation.

model: str

The model to use for the evaluation. Must support structured outputs.

name: str

The name of the grader.

passing\_labels: List[str]

The labels that indicate a passing result. Must be a subset of labels.

type: Literal["label\_model"]

The object type, which is always `label_model`.

class StringCheckGrader: …

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: str

The input text. This may include template strings.

name: str

The name of the grader.

operation: Literal["eq", "ne", "like", "ilike"]

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

"ne"

"like"

"ilike"

reference: str

The reference text. This may include template strings.

type: Literal["string\_check"]

The object type, which is always `string_check`.

class TestingCriterionEvalGraderTextSimilarity: …

A TextSimilarityGrader object which grades text based on similarity metrics.

pass\_threshold: float

The threshold for the score.

class TestingCriterionEvalGraderPython: …

A PythonGrader object that runs a python script on the input.

pass\_threshold: Optional[float]

The threshold for the score.

class TestingCriterionEvalGraderScoreModel: …

A ScoreModelGrader object that uses a model to assign a score to the input.

pass\_threshold: Optional[float]

The threshold for the score.

### Update an eval

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

updated_eval = client.evals.update(
  "eval_67abd54d9b0081909a86353f6fb9317a",
  name="Updated Eval",
  metadata={"description": "Updated description"}
print(updated_eval)

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
