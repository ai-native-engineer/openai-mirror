<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

[Alpha](/api/reference/java/resources/fine_tuning/subresources/alpha)

[Graders](/api/reference/java/resources/fine_tuning/subresources/alpha/subresources/graders)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Run grader

[GraderRunResponse](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20GraderRunResponse%20%3E%20(schema)) fineTuning().alpha().graders().run(GraderRunParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/fine\_tuning/alpha/graders/run

Run a grader.

##### ParametersExpand Collapse

GraderRunParams params

Grader grader

The grader used for the fine-tuning job.

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

String modelSample

The model sample to be evaluated. This value will be used to populate
the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
The `output_json` variable will be populated if the model sample is a
valid JSON string.

Optional<JsonValue> item

The dataset item provided to the grader. This will be used to populate
the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.

##### ReturnsExpand Collapse

class GraderRunResponse:

Metadata metadata

Errors errors

boolean formulaParseError

boolean invalidVariableError

boolean modelGraderParseError

boolean modelGraderRefusalError

boolean modelGraderServerError

Optional<String> modelGraderServerErrorDetails

boolean otherError

boolean pythonGraderRuntimeError

Optional<String> pythonGraderRuntimeErrorDetails

boolean pythonGraderServerError

Optional<String> pythonGraderServerErrorType

boolean sampleParseError

boolean truncatedObservationError

boolean unresponsiveRewardError

double executionTime

String name

Optional<String> sampledModelName

Scores scores

Optional<Long> tokenUsage

String type

ModelGraderTokenUsagePerModel modelGraderTokenUsagePerModel

double reward

SubRewards subRewards

### Run grader

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
import com.openai.models.finetuning.alpha.graders.GraderRunParams;
import com.openai.models.finetuning.alpha.graders.GraderRunResponse;
import com.openai.models.graders.gradermodels.StringCheckGrader;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GraderRunParams params = GraderRunParams.builder()
            .grader(StringCheckGrader.builder()
                .input("input")
                .name("name")
                .operation(StringCheckGrader.Operation.EQ)
                .reference("reference")
                .build())
            .modelSample("model_sample")
            .build();
        GraderRunResponse response = client.fineTuning().alpha().graders().run(params);

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
