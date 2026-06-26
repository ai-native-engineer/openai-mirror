<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Fine Tuning

#### Fine TuningMethods

##### ModelsExpand Collapse

class DpoHyperparameters { batch\_size, beta, learning\_rate\_multiplier, n\_epochs }

The hyperparameters used for the DPO fine-tuning job.

batch\_size: :auto | Integer

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

BatchSize = :auto

Integer = Integer

beta: :auto | Float

The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

One of the following:

Beta = :auto

Float = Float

learning\_rate\_multiplier: :auto | Float

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

LearningRateMultiplier = :auto

Float = Float

n\_epochs: :auto | Integer

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

NEpochs = :auto

Integer = Integer

class DpoMethod { hyperparameters }

Configuration for the DPO fine-tuning method.

hyperparameters: [DpoHyperparameters](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema)) { batch\_size, beta, learning\_rate\_multiplier, n\_epochs }

The hyperparameters used for the DPO fine-tuning job.

class ReinforcementHyperparameters { batch\_size, compute\_multiplier, eval\_interval, 4 more }

The hyperparameters used for the reinforcement fine-tuning job.

batch\_size: :auto | Integer

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

BatchSize = :auto

Integer = Integer

compute\_multiplier: :auto | Float

Multiplier on amount of compute used for exploring search space during training.

One of the following:

ComputeMultiplier = :auto

Float = Float

eval\_interval: :auto | Integer

The number of training steps between evaluation runs.

One of the following:

EvalInterval = :auto

Integer = Integer

eval\_samples: :auto | Integer

Number of evaluation samples to generate per training step.

One of the following:

EvalSamples = :auto

Integer = Integer

learning\_rate\_multiplier: :auto | Float

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

LearningRateMultiplier = :auto

Float = Float

n\_epochs: :auto | Integer

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

NEpochs = :auto

Integer = Integer

reasoning\_effort: :default | :low | :medium | :high

Level of reasoning effort.

One of the following:

:default

:low

:medium

:high

class ReinforcementMethod { grader, hyperparameters }

Configuration for the reinforcement fine-tuning method.

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

hyperparameters: [ReinforcementHyperparameters](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema)) { batch\_size, compute\_multiplier, eval\_interval, 4 more }

The hyperparameters used for the reinforcement fine-tuning job.

class SupervisedHyperparameters { batch\_size, learning\_rate\_multiplier, n\_epochs }

The hyperparameters used for the fine-tuning job.

batch\_size: :auto | Integer

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

BatchSize = :auto

Integer = Integer

learning\_rate\_multiplier: :auto | Float

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

LearningRateMultiplier = :auto

Float = Float

n\_epochs: :auto | Integer

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

NEpochs = :auto

Integer = Integer

class SupervisedMethod { hyperparameters }

Configuration for the supervised fine-tuning method.

hyperparameters: [SupervisedHyperparameters](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema)) { batch\_size, learning\_rate\_multiplier, n\_epochs }

The hyperparameters used for the fine-tuning job.

#### Fine TuningJobs

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Create fine-tuning job](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/create)

fine\_tuning.jobs.create(\*\*kwargs) -> [FineTuningJob](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id, created\_at, error, 16 more }

POST/fine\_tuning/jobs

##### [List fine-tuning jobs](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/list)

fine\_tuning.jobs.list(\*\*kwargs) -> CursorPage<[FineTuningJob](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id, created\_at, error, 16 more } >

GET/fine\_tuning/jobs

##### [Retrieve fine-tuning job](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/retrieve)

fine\_tuning.jobs.retrieve(fine\_tuning\_job\_id) -> [FineTuningJob](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id, created\_at, error, 16 more }

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}

##### [List fine-tuning events](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/list_events)

fine\_tuning.jobs.list\_events(fine\_tuning\_job\_id, \*\*kwargs) -> CursorPage<[FineTuningJobEvent](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)) { id, created\_at, level, 4 more } >

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

##### [Cancel fine-tuning](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/cancel)

fine\_tuning.jobs.cancel(fine\_tuning\_job\_id) -> [FineTuningJob](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id, created\_at, error, 16 more }

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

##### [Pause fine-tuning](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/pause)

fine\_tuning.jobs.pause(fine\_tuning\_job\_id) -> [FineTuningJob](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id, created\_at, error, 16 more }

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/pause

##### [Resume fine-tuning](/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/resume)

fine\_tuning.jobs.resume(fine\_tuning\_job\_id) -> [FineTuningJob](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) { id, created\_at, error, 16 more }

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/resume

##### ModelsExpand Collapse

class FineTuningJob { id, created\_at, error, 16 more }

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

id: String

The object identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

error: Error{ code, message, param}

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

code: String

A machine-readable error code.

message: String

A human-readable error message.

param: String

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

fine\_tuned\_model: String

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

finished\_at: Integer

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

hyperparameters: Hyperparameters{ batch\_size, learning\_rate\_multiplier, n\_epochs}

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

batch\_size: :auto | Integer

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

BatchSize = :auto

Integer = Integer

learning\_rate\_multiplier: :auto | Float

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

LearningRateMultiplier = :auto

Float = Float

n\_epochs: :auto | Integer

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

NEpochs = :auto

Integer = Integer

model: String

The base model that is being fine-tuned.

object: :"fine\_tuning.job"

The object type, which is always “fine\_tuning.job”.

organization\_id: String

The organization that owns the fine-tuning job.

result\_files: Array[String]

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

seed: Integer

The seed used for the fine-tuning job.

status: :validating\_files | :queued | :running | 3 more

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

:validating\_files

:queued

:running

:succeeded

:failed

:cancelled

trained\_tokens: Integer

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

training\_file: String

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

validation\_file: String

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

estimated\_finish: Integer

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

integrations: Array[[FineTuningJobWandbIntegrationObject](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)) { type, wandb } ]

A list of integrations to enable for this fine-tuning job.

type: :wandb

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) { project, entity, name, tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

method\_: Method{ type, dpo, reinforcement, supervised}

The method used for fine-tuning.

type: :supervised | :dpo | :reinforcement

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

:supervised

:dpo

:reinforcement

dpo: [DpoMethod](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)) { hyperparameters }

Configuration for the DPO fine-tuning method.

reinforcement: [ReinforcementMethod](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)) { grader, hyperparameters }

Configuration for the reinforcement fine-tuning method.

supervised: [SupervisedMethod](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)) { hyperparameters }

Configuration for the supervised fine-tuning method.

class FineTuningJobEvent { id, created\_at, level, 4 more }

Fine-tuning job event object

id: String

The object identifier.

created\_at: Integer

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

level: :info | :warn | :error

The log level of the event.

One of the following:

:info

:warn

:error

message: String

The message of the event.

object: :"fine\_tuning.job.event"

The object type, which is always “fine\_tuning.job.event”.

data: untyped

The data associated with the event.

type: :message | :metrics

The type of event.

One of the following:

:message

:metrics

class FineTuningJobWandbIntegration { project, entity, name, tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

project: String

The name of the project that the new run will be created under.

entity: String

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

name: String

A display name to set for the run. If not set, we will use the Job ID as the name.

tags: Array[String]

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

class FineTuningJobWandbIntegrationObject { type, wandb }

type: :wandb

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) { project, entity, name, tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

#### Fine TuningJobsCheckpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/ruby/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

fine\_tuning.jobs.checkpoints.list(fine\_tuning\_job\_id, \*\*kwargs) -> CursorPage<[FineTuningJobCheckpoint](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)) { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more } >

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

class FineTuningJobCheckpoint { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more }

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

id: String

The checkpoint identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

fine\_tuned\_model\_checkpoint: String

The name of the fine-tuned checkpoint model that is created.

fine\_tuning\_job\_id: String

The name of the fine-tuning job that this checkpoint was created from.

metrics: Metrics{ full\_valid\_loss, full\_valid\_mean\_token\_accuracy, step, 4 more}

Metrics at the step number during the fine-tuning job.

full\_valid\_loss: Float

full\_valid\_mean\_token\_accuracy: Float

step: Float

train\_loss: Float

train\_mean\_token\_accuracy: Float

valid\_loss: Float

valid\_mean\_token\_accuracy: Float

object: :"fine\_tuning.job.checkpoint"

The object type, which is always “fine\_tuning.job.checkpoint”.

step\_number: Integer

The step number that the checkpoint was created at.

#### Fine TuningCheckpoints

#### Fine TuningCheckpointsPermissions

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List checkpoint permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

fine\_tuning.checkpoints.permissions.retrieve(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> [PermissionRetrieveResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)) { data, has\_more, object, 2 more }

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

fine\_tuning.checkpoints.permissions.list(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> ConversationCursorPage<[PermissionListResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

fine\_tuning.checkpoints.permissions.create(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> Page<[PermissionCreateResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

fine\_tuning.checkpoints.permissions.delete(permission\_id, \*\*kwargs) -> [PermissionDeleteResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

##### ModelsExpand Collapse

class PermissionRetrieveResponse { data, has\_more, object, 2 more }

data: Array[Data{ id, created\_at, object, project\_id}]

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

has\_more: bool

object: :list

first\_id: String

last\_id: String

class PermissionListResponse { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

class PermissionCreateResponse { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

class PermissionDeleteResponse { id, deleted, object }

id: String

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: bool

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

#### Fine TuningAlpha

#### Fine TuningAlphaGraders

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Run grader](/api/reference/ruby/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run)

fine\_tuning.alpha.graders.run(\*\*kwargs) -> [GraderRunResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_run_response%20%3E%20(schema)) { metadata, model\_grader\_token\_usage\_per\_model, reward, sub\_rewards }

POST/fine\_tuning/alpha/graders/run

##### [Validate grader](/api/reference/ruby/resources/fine_tuning/subresources/alpha/subresources/graders/methods/validate)

fine\_tuning.alpha.graders.validate(\*\*kwargs) -> [GraderValidateResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20grader_validate_response%20%3E%20(schema)) { grader }

POST/fine\_tuning/alpha/graders/validate

##### ModelsExpand Collapse

class GraderRunResponse { metadata, model\_grader\_token\_usage\_per\_model, reward, sub\_rewards }

metadata: Metadata{ errors, execution\_time, name, 4 more}

errors: Errors{ formula\_parse\_error, invalid\_variable\_error, model\_grader\_parse\_error, 11 more}

formula\_parse\_error: bool

invalid\_variable\_error: bool

model\_grader\_parse\_error: bool

model\_grader\_refusal\_error: bool

model\_grader\_server\_error: bool

model\_grader\_server\_error\_details: String

other\_error: bool

python\_grader\_runtime\_error: bool

python\_grader\_runtime\_error\_details: String

python\_grader\_server\_error: bool

python\_grader\_server\_error\_type: String

sample\_parse\_error: bool

truncated\_observation\_error: bool

unresponsive\_reward\_error: bool

execution\_time: Float

name: String

sampled\_model\_name: String

scores: Hash[Symbol, untyped]

token\_usage: Integer

type: String

model\_grader\_token\_usage\_per\_model: Hash[Symbol, untyped]

reward: Float

sub\_rewards: Hash[Symbol, untyped]

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
