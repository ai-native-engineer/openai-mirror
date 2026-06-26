<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/jobs/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Fine Tuning](/api/reference/python/resources/fine_tuning)

[Jobs](/api/reference/python/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel fine-tuning

fine\_tuning.jobs.cancel(strfine\_tuning\_job\_id)  -> [FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

Immediately cancel a fine-tune job.

##### ParametersExpand Collapse

fine\_tuning\_job\_id: str

##### ReturnsExpand Collapse

class FineTuningJob: …

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

id: str

The object identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

error: Optional[Error]

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

code: str

A machine-readable error code.

message: str

A human-readable error message.

param: Optional[str]

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

fine\_tuned\_model: Optional[str]

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

finished\_at: Optional[int]

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

hyperparameters: Hyperparameters

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

batch\_size: Optional[Union[Literal["auto"], int, null]]

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

Literal["auto"]

int

learning\_rate\_multiplier: Optional[Union[Literal["auto"], float, null]]

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

Literal["auto"]

float

n\_epochs: Optional[Union[Literal["auto"], int, null]]

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

Literal["auto"]

int

model: str

The base model that is being fine-tuned.

object: Literal["fine\_tuning.job"]

The object type, which is always “fine\_tuning.job”.

organization\_id: str

The organization that owns the fine-tuning job.

result\_files: List[str]

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

seed: int

The seed used for the fine-tuning job.

status: Literal["validating\_files", "queued", "running", 3 more]

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

"validating\_files"

"queued"

"running"

"succeeded"

"failed"

"cancelled"

trained\_tokens: Optional[int]

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

training\_file: str

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

validation\_file: Optional[str]

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

estimated\_finish: Optional[int]

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

integrations: Optional[List[[FineTuningJobWandbIntegrationObject](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema))]]

A list of integrations to enable for this fine-tuning job.

type: Literal["wandb"]

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema))

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

project: str

The name of the project that the new run will be created under.

entity: Optional[str]

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

name: Optional[str]

A display name to set for the run. If not set, we will use the Job ID as the name.

tags: Optional[List[str]]

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

method: Optional[Method]

The method used for fine-tuning.

type: Literal["supervised", "dpo", "reinforcement"]

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

"supervised"

"dpo"

"reinforcement"

dpo: Optional[DpoMethod]

Configuration for the DPO fine-tuning method.

hyperparameters: Optional[DpoHyperparameters]

The hyperparameters used for the DPO fine-tuning job.

batch\_size: Optional[Union[Literal["auto"], int, null]]

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

Literal["auto"]

int

beta: Optional[Union[Literal["auto"], float, null]]

The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

One of the following:

Literal["auto"]

float

learning\_rate\_multiplier: Optional[Union[Literal["auto"], float, null]]

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

Literal["auto"]

float

n\_epochs: Optional[Union[Literal["auto"], int, null]]

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

Literal["auto"]

int

reinforcement: Optional[ReinforcementMethod]

Configuration for the reinforcement fine-tuning method.

grader: Grader

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

hyperparameters: Optional[ReinforcementHyperparameters]

The hyperparameters used for the reinforcement fine-tuning job.

batch\_size: Optional[Union[Literal["auto"], int, null]]

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

Literal["auto"]

int

compute\_multiplier: Optional[Union[Literal["auto"], float, null]]

Multiplier on amount of compute used for exploring search space during training.

One of the following:

Literal["auto"]

float

eval\_interval: Optional[Union[Literal["auto"], int, null]]

The number of training steps between evaluation runs.

One of the following:

Literal["auto"]

int

eval\_samples: Optional[Union[Literal["auto"], int, null]]

Number of evaluation samples to generate per training step.

One of the following:

Literal["auto"]

int

learning\_rate\_multiplier: Optional[Union[Literal["auto"], float, null]]

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

Literal["auto"]

float

n\_epochs: Optional[Union[Literal["auto"], int, null]]

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

Literal["auto"]

int

reasoning\_effort: Optional[Literal["default", "low", "medium", "high"]]

Level of reasoning effort.

One of the following:

"default"

"low"

"medium"

"high"

supervised: Optional[SupervisedMethod]

Configuration for the supervised fine-tuning method.

hyperparameters: Optional[SupervisedHyperparameters]

The hyperparameters used for the fine-tuning job.

batch\_size: Optional[Union[Literal["auto"], int, null]]

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

Literal["auto"]

int

learning\_rate\_multiplier: Optional[Union[Literal["auto"], float, null]]

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

Literal["auto"]

float

n\_epochs: Optional[Union[Literal["auto"], int, null]]

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

Literal["auto"]

int

### Cancel fine-tuning

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

client.fine_tuning.jobs.cancel("ftjob-abc123")

  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "gpt-4o-mini-2024-07-18",
  "created_at": 1721764800,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "result_files": [],
  "status": "cancelled",
  "validation_file": "file-abc123",
  "training_file": "file-abc123"

##### Returns Examples

  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "gpt-4o-mini-2024-07-18",
  "created_at": 1721764800,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "result_files": [],
  "status": "cancelled",
  "validation_file": "file-abc123",
  "training_file": "file-abc123"
