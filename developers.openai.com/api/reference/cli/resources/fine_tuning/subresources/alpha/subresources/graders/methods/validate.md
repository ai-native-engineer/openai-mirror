<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/alpha/subresources/graders/methods/validate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Fine Tuning](/api/reference/cli/resources/fine_tuning)

[Alpha](/api/reference/cli/resources/fine_tuning/subresources/alpha)

[Graders](/api/reference/cli/resources/fine_tuning/subresources/alpha/subresources/graders)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Validate grader

$ openai fine-tuning:alpha:graders validate

POST/fine\_tuning/alpha/graders/validate

Validate a grader.

##### ParametersExpand Collapse

--grader: [StringCheckGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  or [TextSimilarityGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  or [PythonGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  or 2 more

The grader used for the fine-tuning job.

##### ReturnsExpand Collapse

FineTuningAlphaGraderValidateResponse: object { grader }

grader: optional [StringCheckGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  or [TextSimilarityGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  or [PythonGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  or 2 more

The grader used for the fine-tuning job.

string\_check\_grader: object { input, name, operation, 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: string

The input text. This may include template strings.

name: string

The name of the grader.

operation: "eq" or "ne" or "like" or "ilike"

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

"eq"

"ne"

"like"

"ilike"

reference: string

The reference text. This may include template strings.

type: "string\_check"

The object type, which is always `string_check`.

text\_similarity\_grader: object { evaluation\_metric, input, name, 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: "cosine" or "fuzzy\_match" or "bleu" or 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

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

input: string

The text being graded.

name: string

The name of the grader.

reference: string

The text being graded against.

type: "text\_similarity"

The type of grader.

python\_grader: object { name, source, type, image\_tag }

A PythonGrader object that runs a python script on the input.

name: string

The name of the grader.

source: string

The source code of the python script.

type: "python"

The object type, which is always `python`.

image\_tag: optional string

The image tag to use for the python script.

score\_model\_grader: object { input, model, name, 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input: array of object { content, role, type }

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

content: string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or object { text, type }  or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

Text input: string

A text input to the model.

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

Output text: object { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

Input image: object { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

type: "input\_image"

The type of the image input. Always `input_image`.

detail: optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

response\_input\_audio: object { input\_audio, type }

An audio input to the model.

input\_audio: object { data, format }

data: string

Base64-encoded audio data.

format: "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

grader\_inputs: array of string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or object { text, type }  or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

Text input: string

A text input to the model.

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

Output text: object { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

Input image: object { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

type: "input\_image"

The type of the image input. Always `input_image`.

detail: optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

response\_input\_audio: object { input\_audio, type }

An audio input to the model.

input\_audio: object { data, format }

data: string

Base64-encoded audio data.

format: "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

type: optional "message"

The type of the message input. Always `message`.

"message"

model: string

The model to use for the evaluation.

name: string

The name of the grader.

type: "score\_model"

The object type, which is always `score_model`.

range: optional array of number

The range of the score. Defaults to `[0, 1]`.

sampling\_params: optional object { max\_completions\_tokens, reasoning\_effort, seed, 2 more }

The sampling parameters for the model.

max\_completions\_tokens: optional number

The maximum number of tokens the grader model may generate in its response.

reasoning\_effort: optional "none" or "minimal" or "low" or 3 more

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

seed: optional number

A seed value to initialize the randomness, during sampling.

temperature: optional number

A higher temperature increases randomness in the outputs.

top\_p: optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

multi\_grader: object { calculate\_output, graders, name, type }

A MultiGrader object combines the output of multiple graders to produce a single score.

calculate\_output: string

A formula to calculate the output based on grader results.

graders: [StringCheckGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  or [TextSimilarityGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  or [PythonGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  or 2 more

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

string\_check\_grader: object { input, name, operation, 2 more }

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: string

The input text. This may include template strings.

name: string

The name of the grader.

operation: "eq" or "ne" or "like" or "ilike"

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

"eq"

"ne"

"like"

"ilike"

reference: string

The reference text. This may include template strings.

type: "string\_check"

The object type, which is always `string_check`.

text\_similarity\_grader: object { evaluation\_metric, input, name, 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: "cosine" or "fuzzy\_match" or "bleu" or 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

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

input: string

The text being graded.

name: string

The name of the grader.

reference: string

The text being graded against.

type: "text\_similarity"

The type of grader.

python\_grader: object { name, source, type, image\_tag }

A PythonGrader object that runs a python script on the input.

name: string

The name of the grader.

source: string

The source code of the python script.

type: "python"

The object type, which is always `python`.

image\_tag: optional string

The image tag to use for the python script.

score\_model\_grader: object { input, model, name, 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input: array of object { content, role, type }

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

content: string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or object { text, type }  or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

Text input: string

A text input to the model.

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

Output text: object { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

Input image: object { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

type: "input\_image"

The type of the image input. Always `input_image`.

detail: optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

response\_input\_audio: object { input\_audio, type }

An audio input to the model.

input\_audio: object { data, format }

data: string

Base64-encoded audio data.

format: "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

grader\_inputs: array of string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or object { text, type }  or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

Text input: string

A text input to the model.

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

Output text: object { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

Input image: object { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

type: "input\_image"

The type of the image input. Always `input_image`.

detail: optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

response\_input\_audio: object { input\_audio, type }

An audio input to the model.

input\_audio: object { data, format }

data: string

Base64-encoded audio data.

format: "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

type: optional "message"

The type of the message input. Always `message`.

"message"

model: string

The model to use for the evaluation.

name: string

The name of the grader.

type: "score\_model"

The object type, which is always `score_model`.

range: optional array of number

The range of the score. Defaults to `[0, 1]`.

sampling\_params: optional object { max\_completions\_tokens, reasoning\_effort, seed, 2 more }

The sampling parameters for the model.

max\_completions\_tokens: optional number

The maximum number of tokens the grader model may generate in its response.

reasoning\_effort: optional "none" or "minimal" or "low" or 3 more

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

seed: optional number

A seed value to initialize the randomness, during sampling.

temperature: optional number

A higher temperature increases randomness in the outputs.

top\_p: optional number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

label\_model\_grader: object { input, labels, model, 3 more }

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: array of object { content, role, type }

content: string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or object { text, type }  or 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

Text input: string

A text input to the model.

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

Output text: object { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

Input image: object { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

type: "input\_image"

The type of the image input. Always `input_image`.

detail: optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

response\_input\_audio: object { input\_audio, type }

An audio input to the model.

input\_audio: object { data, format }

data: string

Base64-encoded audio data.

format: "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

grader\_inputs: array of string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or object { text, type }  or 2 more

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

Text input: string

A text input to the model.

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

Output text: object { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

Input image: object { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

type: "input\_image"

The type of the image input. Always `input_image`.

detail: optional string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

response\_input\_audio: object { input\_audio, type }

An audio input to the model.

input\_audio: object { data, format }

data: string

Base64-encoded audio data.

format: "mp3" or "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

type: optional "message"

The type of the message input. Always `message`.

"message"

labels: array of string

The labels to assign to each item in the evaluation.

model: string

The model to use for the evaluation. Must support structured outputs.

name: string

The name of the grader.

passing\_labels: array of string

The labels that indicate a passing result. Must be a subset of labels.

type: "label\_model"

The object type, which is always `label_model`.

name: string

The name of the grader.

type: "multi"

The object type, which is always `multi`.

### Validate grader

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai fine-tuning:alpha:graders validate \
  --api-key 'My API Key' \
  --grader '{input: input, name: name, operation: eq, reference: reference, type: string_check}'

  "grader": {
    "type": "string_check",
    "name": "Example string check grader",
    "input": "{{sample.output_text}}",
    "reference": "{{item.label}}",
    "operation": "eq"

##### Returns Examples

  "grader": {
    "type": "string_check",
    "name": "Example string check grader",
    "input": "{{sample.output_text}}",
    "reference": "{{item.label}}",
    "operation": "eq"
