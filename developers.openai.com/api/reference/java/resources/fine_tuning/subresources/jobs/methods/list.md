<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/jobs/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

[Jobs](/api/reference/java/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning jobs

JobListPage fineTuning().jobs().list(JobListParamsparams = JobListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs

List your organization’s fine-tuning jobs

##### ParametersExpand Collapse

JobListParams params

Optional<String> after

Identifier for the last job from the previous pagination request.

Optional<Long> limit

Number of fine-tuning jobs to retrieve.

Optional<[Metadata](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/list#(resource)%20fine_tuning.jobs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20metadata%20%3E%20(schema))> metadata

Optional metadata filter. To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to indicate no metadata.

##### ReturnsExpand Collapse

class FineTuningJob:

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

String id

The object identifier, which can be referenced in the API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Optional<Error> error

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

String code

A machine-readable error code.

String message

A human-readable error message.

Optional<String> param

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

Optional<String> fineTunedModel

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

Optional<Long> finishedAt

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

Hyperparameters hyperparameters

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

Optional<BatchSize> batchSize

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

JsonValue;

long

Optional<LearningRateMultiplier> learningRateMultiplier

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

JsonValue;

double

Optional<NEpochs> nEpochs

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

JsonValue;

long

String model

The base model that is being fine-tuned.

JsonValue; object\_ "fine\_tuning.job"constant"fine\_tuning.job"constant

The object type, which is always “fine\_tuning.job”.

String organizationId

The organization that owns the fine-tuning job.

List<String> resultFiles

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

long seed

The seed used for the fine-tuning job.

Status status

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

VALIDATING\_FILES("validating\_files")

QUEUED("queued")

RUNNING("running")

SUCCEEDED("succeeded")

FAILED("failed")

CANCELLED("cancelled")

Optional<Long> trainedTokens

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

String trainingFile

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

Optional<String> validationFile

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

Optional<Long> estimatedFinish

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

Optional<List<[FineTuningJobWandbIntegrationObject](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema))>> integrations

A list of integrations to enable for this fine-tuning job.

JsonValue; type "wandb"constant"wandb"constant

The type of the integration being enabled for the fine-tuning job

[FineTuningJobWandbIntegration](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) wandb

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

String project

The name of the project that the new run will be created under.

Optional<String> entity

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

Optional<String> name

A display name to set for the run. If not set, we will use the Job ID as the name.

Optional<List<String>> tags

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<Method> method

The method used for fine-tuning.

Type type

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

SUPERVISED("supervised")

DPO("dpo")

REINFORCEMENT("reinforcement")

Optional<[DpoMethod](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema))> dpo

Configuration for the DPO fine-tuning method.

Optional<[DpoHyperparameters](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema))> hyperparameters

The hyperparameters used for the DPO fine-tuning job.

Optional<BatchSize> batchSize

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

JsonValue;

long

Optional<Beta> beta

The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

One of the following:

JsonValue;

double

Optional<LearningRateMultiplier> learningRateMultiplier

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

JsonValue;

double

Optional<NEpochs> nEpochs

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

JsonValue;

long

Optional<[ReinforcementMethod](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema))> reinforcement

Configuration for the reinforcement fine-tuning method.

Grader grader

The grader used for the fine-tuning job.

One of the following:

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

class TextSimilarityGrader:

A TextSimilarityGrader object which grades text based on similarity metrics.

EvaluationMetric evaluationMetric

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

COSINE("cosine")

FUZZY\_MATCH("fuzzy\_match")

BLEU("bleu")

GLEU("gleu")

METEOR("meteor")

ROUGE\_1("rouge\_1")

ROUGE\_2("rouge\_2")

ROUGE\_3("rouge\_3")

ROUGE\_4("rouge\_4")

ROUGE\_5("rouge\_5")

ROUGE\_L("rouge\_l")

String input

The text being graded.

String name

The name of the grader.

String reference

The text being graded against.

JsonValue; type "text\_similarity"constant"text\_similarity"constant

The type of grader.

class PythonGrader:

A PythonGrader object that runs a python script on the input.

String name

The name of the grader.

String source

The source code of the python script.

JsonValue; type "python"constant"python"constant

The object type, which is always `python`.

Optional<String> imageTag

The image tag to use for the python script.

class ScoreModelGrader:

A ScoreModelGrader object that uses a model to assign a score to the input.

List<Input> input

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

String model

The model to use for the evaluation.

String name

The name of the grader.

JsonValue; type "score\_model"constant"score\_model"constant

The object type, which is always `score_model`.

Optional<List<Double>> range

The range of the score. Defaults to `[0, 1]`.

Optional<SamplingParams> samplingParams

The sampling parameters for the model.

Optional<Long> maxCompletionsTokens

The maximum number of tokens the grader model may generate in its response.

minimum1

Optional<[ReasoningEffort](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))> reasoningEffort

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

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

Optional<Long> seed

A seed value to initialize the randomness, during sampling.

Optional<Double> temperature

A higher temperature increases randomness in the outputs.

Optional<Double> topP

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class MultiGrader:

A MultiGrader object combines the output of multiple graders to produce a single score.

String calculateOutput

A formula to calculate the output based on grader results.

Graders graders

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

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

class TextSimilarityGrader:

A TextSimilarityGrader object which grades text based on similarity metrics.

EvaluationMetric evaluationMetric

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

COSINE("cosine")

FUZZY\_MATCH("fuzzy\_match")

BLEU("bleu")

GLEU("gleu")

METEOR("meteor")

ROUGE\_1("rouge\_1")

ROUGE\_2("rouge\_2")

ROUGE\_3("rouge\_3")

ROUGE\_4("rouge\_4")

ROUGE\_5("rouge\_5")

ROUGE\_L("rouge\_l")

String input

The text being graded.

String name

The name of the grader.

String reference

The text being graded against.

JsonValue; type "text\_similarity"constant"text\_similarity"constant

The type of grader.

class PythonGrader:

A PythonGrader object that runs a python script on the input.

String name

The name of the grader.

String source

The source code of the python script.

JsonValue; type "python"constant"python"constant

The object type, which is always `python`.

Optional<String> imageTag

The image tag to use for the python script.

class ScoreModelGrader:

A ScoreModelGrader object that uses a model to assign a score to the input.

List<Input> input

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

String model

The model to use for the evaluation.

String name

The name of the grader.

JsonValue; type "score\_model"constant"score\_model"constant

The object type, which is always `score_model`.

Optional<List<Double>> range

The range of the score. Defaults to `[0, 1]`.

Optional<SamplingParams> samplingParams

The sampling parameters for the model.

Optional<Long> maxCompletionsTokens

The maximum number of tokens the grader model may generate in its response.

minimum1

Optional<[ReasoningEffort](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))> reasoningEffort

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

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

Optional<Long> seed

A seed value to initialize the randomness, during sampling.

Optional<Double> temperature

A higher temperature increases randomness in the outputs.

Optional<Double> topP

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

String name

The name of the grader.

JsonValue; type "multi"constant"multi"constant

The object type, which is always `multi`.

Optional<[ReinforcementHyperparameters](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema))> hyperparameters

The hyperparameters used for the reinforcement fine-tuning job.

Optional<BatchSize> batchSize

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

JsonValue;

long

Optional<ComputeMultiplier> computeMultiplier

Multiplier on amount of compute used for exploring search space during training.

One of the following:

JsonValue;

double

Optional<EvalInterval> evalInterval

The number of training steps between evaluation runs.

One of the following:

JsonValue;

long

Optional<EvalSamples> evalSamples

Number of evaluation samples to generate per training step.

One of the following:

JsonValue;

long

Optional<LearningRateMultiplier> learningRateMultiplier

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

JsonValue;

double

Optional<NEpochs> nEpochs

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

JsonValue;

long

Optional<ReasoningEffort> reasoningEffort

Level of reasoning effort.

One of the following:

DEFAULT("default")

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<[SupervisedMethod](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema))> supervised

Configuration for the supervised fine-tuning method.

Optional<[SupervisedHyperparameters](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema))> hyperparameters

The hyperparameters used for the fine-tuning job.

Optional<BatchSize> batchSize

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

JsonValue;

long

Optional<LearningRateMultiplier> learningRateMultiplier

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

JsonValue;

double

Optional<NEpochs> nEpochs

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

JsonValue;

long

### List fine-tuning jobs

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
import com.openai.models.finetuning.jobs.JobListPage;
import com.openai.models.finetuning.jobs.JobListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        JobListPage page = client.fineTuning().jobs().list();

  "object": "list",
  "data": [
      "object": "fine_tuning.job",
      "id": "ftjob-abc123",
      "model": "gpt-4o-mini-2024-07-18",
      "created_at": 1721764800,
      "fine_tuned_model": null,
      "organization_id": "org-123",
      "result_files": [],
      "status": "queued",
      "validation_file": null,
      "training_file": "file-abc123",
      "metadata": {
        "key": "value"
    { ... },
    { ... }
  ], "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
      "object": "fine_tuning.job",
      "id": "ftjob-abc123",
      "model": "gpt-4o-mini-2024-07-18",
      "created_at": 1721764800,
      "fine_tuned_model": null,
      "organization_id": "org-123",
      "result_files": [],
      "status": "queued",
      "validation_file": null,
      "training_file": "file-abc123",
      "metadata": {
        "key": "value"
    { ... },
    { ... }
  ], "has_more": true
