<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Fine Tuning](/api/reference/python/resources/fine_tuning)

[Alpha](/api/reference/python/resources/fine_tuning/subresources/alpha)

[Graders](/api/reference/python/resources/fine_tuning/subresources/alpha/subresources/graders)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Run grader

fine\_tuning.alpha.graders.run(GraderRunParams\*\*kwargs)  -> [GraderRunResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema))

POST/fine\_tuning/alpha/graders/run

Run a grader.

##### ParametersExpand Collapse

grader: [Grader](/api/reference/python/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run#(resource)%20fine_tuning.alpha.graders%20%3E%20(method)%20run%20%3E%20(params)%20default%20%3E%20(param)%20grader%20%3E%20(schema))

The grader used for the fine-tuning job.

One of the following:

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

class TextSimilarityGrader: …

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: Literal["cosine", "fuzzy\_match", "bleu", 8 more]

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

"cosine"

"fuzzy\_match"

"bleu"

"gleu"

"meteor"

"rouge\_1"

"rouge\_2"

"rouge\_3"

"rouge\_4"

"rouge\_5"

"rouge\_l"

input: str

The text being graded.

name: str

The name of the grader.

reference: str

The text being graded against.

type: Literal["text\_similarity"]

The type of grader.

class PythonGrader: …

A PythonGrader object that runs a python script on the input.

name: str

The name of the grader.

source: str

The source code of the python script.

type: Literal["python"]

The object type, which is always `python`.

image\_tag: Optional[str]

The image tag to use for the python script.

class ScoreModelGrader: …

A ScoreModelGrader object that uses a model to assign a score to the input.

input: List[Input]

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

model: str

The model to use for the evaluation.

name: str

The name of the grader.

type: Literal["score\_model"]

The object type, which is always `score_model`.

range: Optional[List[float]]

The range of the score. Defaults to `[0, 1]`.

sampling\_params: Optional[SamplingParams]

The sampling parameters for the model.

max\_completions\_tokens: Optional[int]

The maximum number of tokens the grader model may generate in its response.

minimum1

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class MultiGrader: …

A MultiGrader object combines the output of multiple graders to produce a single score.

calculate\_output: str

A formula to calculate the output based on grader results.

graders: Graders

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

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

class TextSimilarityGrader: …

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: Literal["cosine", "fuzzy\_match", "bleu", 8 more]

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

"cosine"

"fuzzy\_match"

"bleu"

"gleu"

"meteor"

"rouge\_1"

"rouge\_2"

"rouge\_3"

"rouge\_4"

"rouge\_5"

"rouge\_l"

input: str

The text being graded.

name: str

The name of the grader.

reference: str

The text being graded against.

type: Literal["text\_similarity"]

The type of grader.

class PythonGrader: …

A PythonGrader object that runs a python script on the input.

name: str

The name of the grader.

source: str

The source code of the python script.

type: Literal["python"]

The object type, which is always `python`.

image\_tag: Optional[str]

The image tag to use for the python script.

class ScoreModelGrader: …

A ScoreModelGrader object that uses a model to assign a score to the input.

input: List[Input]

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

model: str

The model to use for the evaluation.

name: str

The name of the grader.

type: Literal["score\_model"]

The object type, which is always `score_model`.

range: Optional[List[float]]

The range of the score. Defaults to `[0, 1]`.

sampling\_params: Optional[SamplingParams]

The sampling parameters for the model.

max\_completions\_tokens: Optional[int]

The maximum number of tokens the grader model may generate in its response.

minimum1

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

name: str

The name of the grader.

type: Literal["multi"]

The object type, which is always `multi`.

model\_sample: str

The model sample to be evaluated. This value will be used to populate
the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
The `output_json` variable will be populated if the model sample is a
valid JSON string.

item: Optional[[object](/api/reference/python/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run#(resource)%20fine_tuning.alpha.graders%20%3E%20(method)%20run%20%3E%20(params)%20default%20%3E%20(param)%20item%20%3E%20(schema))]

The dataset item provided to the grader. This will be used to populate
the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.

##### ReturnsExpand Collapse

class GraderRunResponse: …

metadata: Metadata

errors: MetadataErrors

formula\_parse\_error: bool

invalid\_variable\_error: bool

model\_grader\_parse\_error: bool

model\_grader\_refusal\_error: bool

model\_grader\_server\_error: bool

model\_grader\_server\_error\_details: Optional[str]

other\_error: bool

python\_grader\_runtime\_error: bool

python\_grader\_runtime\_error\_details: Optional[str]

python\_grader\_server\_error: bool

python\_grader\_server\_error\_type: Optional[str]

sample\_parse\_error: bool

truncated\_observation\_error: bool

unresponsive\_reward\_error: bool

execution\_time: float

name: str

sampled\_model\_name: Optional[str]

scores: Dict[str, object]

token\_usage: Optional[int]

type: str

model\_grader\_token\_usage\_per\_model: Dict[str, object]

reward: float

sub\_rewards: Dict[str, object]

### Run grader

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
response = client.fine_tuning.alpha.graders.run(
    grader={
        "input": "input",
        "name": "name",
        "operation": "eq",
        "reference": "reference",
        "type": "string_check",
    model_sample="model_sample",
print(response.metadata)

200 example

  "metadata": {
    "errors": {
      "formula_parse_error": true,
      "invalid_variable_error": true,
      "model_grader_parse_error": true,
      "model_grader_refusal_error": true,
      "model_grader_server_error": true,
      "model_grader_server_error_details": "model_grader_server_error_details",
      "other_error": true,
      "python_grader_runtime_error": true,
      "python_grader_runtime_error_details": "python_grader_runtime_error_details",
      "python_grader_server_error": true,
      "python_grader_server_error_type": "python_grader_server_error_type",
      "sample_parse_error": true,
      "truncated_observation_error": true,
      "unresponsive_reward_error": true
    "execution_time": 0,
    "name": "name",
    "sampled_model_name": "sampled_model_name",
    "scores": {
      "foo": "bar"
    "token_usage": 0,
    "type": "type"
  "model_grader_token_usage_per_model": {
    "foo": "bar"
  "reward": 0,
  "sub_rewards": {
    "foo": "bar"

##### Returns Examples

200 example

  "metadata": {
    "errors": {
      "formula_parse_error": true,
      "invalid_variable_error": true,
      "model_grader_parse_error": true,
      "model_grader_refusal_error": true,
      "model_grader_server_error": true,
      "model_grader_server_error_details": "model_grader_server_error_details",
      "other_error": true,
      "python_grader_runtime_error": true,
      "python_grader_runtime_error_details": "python_grader_runtime_error_details",
      "python_grader_server_error": true,
      "python_grader_server_error_type": "python_grader_server_error_type",
      "sample_parse_error": true,
      "truncated_observation_error": true,
      "unresponsive_reward_error": true
    "execution_time": 0,
    "name": "name",
    "sampled_model_name": "sampled_model_name",
    "scores": {
      "foo": "bar"
    "token_usage": 0,
    "type": "type"
  "model_grader_token_usage_per_model": {
    "foo": "bar"
  "reward": 0,
  "sub_rewards": {
    "foo": "bar"
