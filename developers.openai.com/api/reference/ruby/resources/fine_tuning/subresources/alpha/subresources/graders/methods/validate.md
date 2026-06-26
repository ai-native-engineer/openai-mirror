<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/alpha/subresources/graders/methods/validate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Fine Tuning](/api/reference/ruby/resources/fine_tuning)

[Alpha](/api/reference/ruby/resources/fine_tuning/subresources/alpha)

[Graders](/api/reference/ruby/resources/fine_tuning/subresources/alpha/subresources/graders)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Validate grader

fine\_tuning.alpha.graders.validate(\*\*kwargs) -> [GraderValidateResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_validate_response%20%3E%20(schema)) { grader }

POST/fine\_tuning/alpha/graders/validate

Validate a grader.

##### ParametersExpand Collapse

grader: [StringCheckGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  | [TextSimilarityGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  | [PythonGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  | 2 more

The grader used for the fine-tuning job.

One of the following:

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

class TextSimilarityGrader { evaluation\_metric, input, name, 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: :cosine | :fuzzy\_match | :bleu | 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

:cosine

:fuzzy\_match

:bleu

:gleu

:meteor

:rouge\_1

:rouge\_2

:rouge\_3

:rouge\_4

:rouge\_5

:rouge\_l

input: String

The text being graded.

name: String

The name of the grader.

reference: String

The text being graded against.

type: :text\_similarity

The type of grader.

class PythonGrader { name, source, type, image\_tag }

A PythonGrader object that runs a python script on the input.

name: String

The name of the grader.

source: String

The source code of the python script.

type: :python

The object type, which is always `python`.

image\_tag: String

The image tag to use for the python script.

class ScoreModelGrader { input, model, name, 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input: Array[Input{ content, role, type}]

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

model: String

The model to use for the evaluation.

name: String

The name of the grader.

type: :score\_model

The object type, which is always `score_model`.

range: Array[Float]

The range of the score. Defaults to `[0, 1]`.

sampling\_params: SamplingParams{ max\_completions\_tokens, reasoning\_effort, seed, 2 more}

The sampling parameters for the model.

max\_completions\_tokens: Integer

The maximum number of tokens the grader model may generate in its response.

minimum1

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

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

:none

:minimal

:low

:medium

:high

:xhigh

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class MultiGrader { calculate\_output, graders, name, type }

A MultiGrader object combines the output of multiple graders to produce a single score.

calculate\_output: String

A formula to calculate the output based on grader results.

graders: [StringCheckGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  | [TextSimilarityGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  | [PythonGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  | 2 more

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

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

class TextSimilarityGrader { evaluation\_metric, input, name, 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: :cosine | :fuzzy\_match | :bleu | 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

:cosine

:fuzzy\_match

:bleu

:gleu

:meteor

:rouge\_1

:rouge\_2

:rouge\_3

:rouge\_4

:rouge\_5

:rouge\_l

input: String

The text being graded.

name: String

The name of the grader.

reference: String

The text being graded against.

type: :text\_similarity

The type of grader.

class PythonGrader { name, source, type, image\_tag }

A PythonGrader object that runs a python script on the input.

name: String

The name of the grader.

source: String

The source code of the python script.

type: :python

The object type, which is always `python`.

image\_tag: String

The image tag to use for the python script.

class ScoreModelGrader { input, model, name, 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input: Array[Input{ content, role, type}]

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

model: String

The model to use for the evaluation.

name: String

The name of the grader.

type: :score\_model

The object type, which is always `score_model`.

range: Array[Float]

The range of the score. Defaults to `[0, 1]`.

sampling\_params: SamplingParams{ max\_completions\_tokens, reasoning\_effort, seed, 2 more}

The sampling parameters for the model.

max\_completions\_tokens: Integer

The maximum number of tokens the grader model may generate in its response.

minimum1

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

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

:none

:minimal

:low

:medium

:high

:xhigh

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

name: String

The name of the grader.

type: :multi

The object type, which is always `multi`.

##### ReturnsExpand Collapse

class GraderValidateResponse { grader }

grader: [StringCheckGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  | [TextSimilarityGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  | [PythonGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  | 2 more

The grader used for the fine-tuning job.

One of the following:

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

class TextSimilarityGrader { evaluation\_metric, input, name, 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: :cosine | :fuzzy\_match | :bleu | 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

:cosine

:fuzzy\_match

:bleu

:gleu

:meteor

:rouge\_1

:rouge\_2

:rouge\_3

:rouge\_4

:rouge\_5

:rouge\_l

input: String

The text being graded.

name: String

The name of the grader.

reference: String

The text being graded against.

type: :text\_similarity

The type of grader.

class PythonGrader { name, source, type, image\_tag }

A PythonGrader object that runs a python script on the input.

name: String

The name of the grader.

source: String

The source code of the python script.

type: :python

The object type, which is always `python`.

image\_tag: String

The image tag to use for the python script.

class ScoreModelGrader { input, model, name, 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input: Array[Input{ content, role, type}]

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

model: String

The model to use for the evaluation.

name: String

The name of the grader.

type: :score\_model

The object type, which is always `score_model`.

range: Array[Float]

The range of the score. Defaults to `[0, 1]`.

sampling\_params: SamplingParams{ max\_completions\_tokens, reasoning\_effort, seed, 2 more}

The sampling parameters for the model.

max\_completions\_tokens: Integer

The maximum number of tokens the grader model may generate in its response.

minimum1

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

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

:none

:minimal

:low

:medium

:high

:xhigh

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class MultiGrader { calculate\_output, graders, name, type }

A MultiGrader object combines the output of multiple graders to produce a single score.

calculate\_output: String

A formula to calculate the output based on grader results.

graders: [StringCheckGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  | [TextSimilarityGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  | [PythonGrader](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  | 2 more

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

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

class TextSimilarityGrader { evaluation\_metric, input, name, 2 more }

A TextSimilarityGrader object which grades text based on similarity metrics.

evaluation\_metric: :cosine | :fuzzy\_match | :bleu | 8 more

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

:cosine

:fuzzy\_match

:bleu

:gleu

:meteor

:rouge\_1

:rouge\_2

:rouge\_3

:rouge\_4

:rouge\_5

:rouge\_l

input: String

The text being graded.

name: String

The name of the grader.

reference: String

The text being graded against.

type: :text\_similarity

The type of grader.

class PythonGrader { name, source, type, image\_tag }

A PythonGrader object that runs a python script on the input.

name: String

The name of the grader.

source: String

The source code of the python script.

type: :python

The object type, which is always `python`.

image\_tag: String

The image tag to use for the python script.

class ScoreModelGrader { input, model, name, 3 more }

A ScoreModelGrader object that uses a model to assign a score to the input.

input: Array[Input{ content, role, type}]

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

model: String

The model to use for the evaluation.

name: String

The name of the grader.

type: :score\_model

The object type, which is always `score_model`.

range: Array[Float]

The range of the score. Defaults to `[0, 1]`.

sampling\_params: SamplingParams{ max\_completions\_tokens, reasoning\_effort, seed, 2 more}

The sampling parameters for the model.

max\_completions\_tokens: Integer

The maximum number of tokens the grader model may generate in its response.

minimum1

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

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

:none

:minimal

:low

:medium

:high

:xhigh

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

name: String

The name of the grader.

type: :multi

The object type, which is always `multi`.

### Validate grader

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

response = openai.fine_tuning.alpha.graders.validate(
  grader: {input: "input", name: "name", operation: :eq, reference: "reference", type: :string_check}

puts(response)

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
