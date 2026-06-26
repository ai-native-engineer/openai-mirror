<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/methods/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Methods

##### ModelsExpand Collapse

type DpoHyperparametersResp struct{…}

The hyperparameters used for the DPO fine-tuning job.

BatchSize DpoHyperparametersBatchSizeUnionRespOptional

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

type Auto string

int64

Beta DpoHyperparametersBetaUnionRespOptional

The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

One of the following:

type Auto string

float64

LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionRespOptional

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

type Auto string

float64

NEpochs DpoHyperparametersNEpochsUnionRespOptional

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

type Auto string

int64

type DpoMethod struct{…}

Configuration for the DPO fine-tuning method.

Hyperparameters [DpoHyperparametersResp](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_hyperparameters%20%3E%20(schema))Optional

The hyperparameters used for the DPO fine-tuning job.

type ReinforcementHyperparametersResp struct{…}

The hyperparameters used for the reinforcement fine-tuning job.

BatchSize ReinforcementHyperparametersBatchSizeUnionRespOptional

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

type Auto string

int64

ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionRespOptional

Multiplier on amount of compute used for exploring search space during training.

One of the following:

type Auto string

float64

EvalInterval ReinforcementHyperparametersEvalIntervalUnionRespOptional

The number of training steps between evaluation runs.

One of the following:

type Auto string

int64

EvalSamples ReinforcementHyperparametersEvalSamplesUnionRespOptional

Number of evaluation samples to generate per training step.

One of the following:

type Auto string

int64

LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionRespOptional

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

type Auto string

float64

NEpochs ReinforcementHyperparametersNEpochsUnionRespOptional

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

type Auto string

int64

ReasoningEffort ReinforcementHyperparametersReasoningEffortOptional

Level of reasoning effort.

One of the following:

const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"

const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"

const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"

const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"

type ReinforcementMethod struct{…}

Configuration for the reinforcement fine-tuning method.

Grader ReinforcementMethodGraderUnion

The grader used for the fine-tuning job.

One of the following:

type StringCheckGrader struct{…}

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

Input string

The input text. This may include template strings.

Name string

The name of the grader.

Operation StringCheckGraderOperation

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"

const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"

const StringCheckGraderOperationLike StringCheckGraderOperation = "like"

const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"

Reference string

The reference text. This may include template strings.

Type StringCheck

The object type, which is always `string_check`.

type TextSimilarityGrader struct{…}

A TextSimilarityGrader object which grades text based on similarity metrics.

EvaluationMetric TextSimilarityGraderEvaluationMetric

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"

const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy\_match"

const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"

const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"

const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"

const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge\_1"

const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge\_2"

const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge\_3"

const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge\_4"

const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge\_5"

const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge\_l"

Input string

The text being graded.

Name string

The name of the grader.

Reference string

The text being graded against.

Type TextSimilarity

The type of grader.

type PythonGrader struct{…}

A PythonGrader object that runs a python script on the input.

Name string

The name of the grader.

Source string

The source code of the python script.

Type Python

The object type, which is always `python`.

ImageTag stringOptional

The image tag to use for the python script.

type ScoreModelGrader struct{…}

A ScoreModelGrader object that uses a model to assign a score to the input.

Input []ScoreModelGraderInput

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

Content ScoreModelGraderInputContentUnion

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ScoreModelGraderInputContentOutputText struct{…}

A text output from the model.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

type ScoreModelGraderInputContentInputImage struct{…}

An image input block used within EvalItem content arrays.

ImageURL string

The URL of the image input.

formaturi

Type InputImage

The type of the image input. Always `input_image`.

Detail stringOptional

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

type ResponseInputAudio struct{…}

An audio input to the model.

InputAudio ResponseInputAudioInputAudio

Data string

Base64-encoded audio data.

Format string

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"

const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"

Type InputAudio

The type of the input item. Always `input_audio`.

type GraderInputs []GraderInputUnion

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type GraderInputOutputText struct{…}

A text output from the model.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

type GraderInputInputImage struct{…}

An image input block used within EvalItem content arrays.

ImageURL string

The URL of the image input.

formaturi

Type InputImage

The type of the image input. Always `input_image`.

Detail stringOptional

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

type ResponseInputAudio struct{…}

An audio input to the model.

InputAudio ResponseInputAudioInputAudio

Data string

Base64-encoded audio data.

Format string

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"

const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"

Type InputAudio

The type of the input item. Always `input_audio`.

Role string

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"

const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"

const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"

const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"

Type stringOptional

The type of the message input. Always `message`.

Model string

The model to use for the evaluation.

Name string

The name of the grader.

Type ScoreModel

The object type, which is always `score_model`.

Range []float64Optional

The range of the score. Defaults to `[0, 1]`.

SamplingParams ScoreModelGraderSamplingParamsOptional

The sampling parameters for the model.

MaxCompletionsTokens int64Optional

The maximum number of tokens the grader model may generate in its response.

minimum1

ReasoningEffort [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))Optional

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

Seed int64Optional

A seed value to initialize the randomness, during sampling.

Temperature float64Optional

A higher temperature increases randomness in the outputs.

TopP float64Optional

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

type MultiGrader struct{…}

A MultiGrader object combines the output of multiple graders to produce a single score.

CalculateOutput string

A formula to calculate the output based on grader results.

Graders MultiGraderGradersUnion

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

One of the following:

type StringCheckGrader struct{…}

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

Input string

The input text. This may include template strings.

Name string

The name of the grader.

Operation StringCheckGraderOperation

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"

const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"

const StringCheckGraderOperationLike StringCheckGraderOperation = "like"

const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"

Reference string

The reference text. This may include template strings.

Type StringCheck

The object type, which is always `string_check`.

type TextSimilarityGrader struct{…}

A TextSimilarityGrader object which grades text based on similarity metrics.

EvaluationMetric TextSimilarityGraderEvaluationMetric

The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
`gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
or `rouge_l`.

One of the following:

const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"

const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy\_match"

const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"

const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"

const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"

const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge\_1"

const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge\_2"

const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge\_3"

const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge\_4"

const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge\_5"

const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge\_l"

Input string

The text being graded.

Name string

The name of the grader.

Reference string

The text being graded against.

Type TextSimilarity

The type of grader.

type PythonGrader struct{…}

A PythonGrader object that runs a python script on the input.

Name string

The name of the grader.

Source string

The source code of the python script.

Type Python

The object type, which is always `python`.

ImageTag stringOptional

The image tag to use for the python script.

type ScoreModelGrader struct{…}

A ScoreModelGrader object that uses a model to assign a score to the input.

Input []ScoreModelGraderInput

The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

Content ScoreModelGraderInputContentUnion

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ScoreModelGraderInputContentOutputText struct{…}

A text output from the model.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

type ScoreModelGraderInputContentInputImage struct{…}

An image input block used within EvalItem content arrays.

ImageURL string

The URL of the image input.

formaturi

Type InputImage

The type of the image input. Always `input_image`.

Detail stringOptional

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

type ResponseInputAudio struct{…}

An audio input to the model.

InputAudio ResponseInputAudioInputAudio

Data string

Base64-encoded audio data.

Format string

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"

const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"

Type InputAudio

The type of the input item. Always `input_audio`.

type GraderInputs []GraderInputUnion

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type GraderInputOutputText struct{…}

A text output from the model.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

type GraderInputInputImage struct{…}

An image input block used within EvalItem content arrays.

ImageURL string

The URL of the image input.

formaturi

Type InputImage

The type of the image input. Always `input_image`.

Detail stringOptional

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

type ResponseInputAudio struct{…}

An audio input to the model.

InputAudio ResponseInputAudioInputAudio

Data string

Base64-encoded audio data.

Format string

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"

const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"

Type InputAudio

The type of the input item. Always `input_audio`.

Role string

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"

const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"

const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"

const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"

Type stringOptional

The type of the message input. Always `message`.

Model string

The model to use for the evaluation.

Name string

The name of the grader.

Type ScoreModel

The object type, which is always `score_model`.

Range []float64Optional

The range of the score. Defaults to `[0, 1]`.

SamplingParams ScoreModelGraderSamplingParamsOptional

The sampling parameters for the model.

MaxCompletionsTokens int64Optional

The maximum number of tokens the grader model may generate in its response.

minimum1

ReasoningEffort [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))Optional

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

Seed int64Optional

A seed value to initialize the randomness, during sampling.

Temperature float64Optional

A higher temperature increases randomness in the outputs.

TopP float64Optional

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

type LabelModelGrader struct{…}

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

Input []LabelModelGraderInput

Content LabelModelGraderInputContentUnion

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type LabelModelGraderInputContentOutputText struct{…}

A text output from the model.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

type LabelModelGraderInputContentInputImage struct{…}

An image input block used within EvalItem content arrays.

ImageURL string

The URL of the image input.

formaturi

Type InputImage

The type of the image input. Always `input_image`.

Detail stringOptional

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

type ResponseInputAudio struct{…}

An audio input to the model.

InputAudio ResponseInputAudioInputAudio

Data string

Base64-encoded audio data.

Format string

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"

const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"

Type InputAudio

The type of the input item. Always `input_audio`.

type GraderInputs []GraderInputUnion

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type GraderInputOutputText struct{…}

A text output from the model.

Text string

The text output from the model.

Type OutputText

The type of the output text. Always `output_text`.

type GraderInputInputImage struct{…}

An image input block used within EvalItem content arrays.

ImageURL string

The URL of the image input.

formaturi

Type InputImage

The type of the image input. Always `input_image`.

Detail stringOptional

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

type ResponseInputAudio struct{…}

An audio input to the model.

InputAudio ResponseInputAudioInputAudio

Data string

Base64-encoded audio data.

Format string

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"

const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"

Type InputAudio

The type of the input item. Always `input_audio`.

Role string

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"

const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"

const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"

const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"

Type stringOptional

The type of the message input. Always `message`.

Labels []string

The labels to assign to each item in the evaluation.

Model string

The model to use for the evaluation. Must support structured outputs.

Name string

The name of the grader.

PassingLabels []string

The labels that indicate a passing result. Must be a subset of labels.

Type LabelModel

The object type, which is always `label_model`.

Name string

The name of the grader.

Type Multi

The object type, which is always `multi`.

Hyperparameters [ReinforcementHyperparametersResp](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_hyperparameters%20%3E%20(schema))Optional

The hyperparameters used for the reinforcement fine-tuning job.

type SupervisedHyperparametersResp struct{…}

The hyperparameters used for the fine-tuning job.

BatchSize SupervisedHyperparametersBatchSizeUnionRespOptional

Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

One of the following:

type Auto string

int64

LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionRespOptional

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

One of the following:

type Auto string

float64

NEpochs SupervisedHyperparametersNEpochsUnionRespOptional

The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

One of the following:

type Auto string

int64

type SupervisedMethod struct{…}

Configuration for the supervised fine-tuning method.

Hyperparameters [SupervisedHyperparametersResp](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_hyperparameters%20%3E%20(schema))Optional

The hyperparameters used for the fine-tuning job.
