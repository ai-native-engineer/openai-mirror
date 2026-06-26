<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run/ -->

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

# Run grader

$ openai fine-tuning:alpha:graders run

POST/fine\_tuning/alpha/graders/run

Run a grader.

##### ParametersExpand Collapse

--grader: [StringCheckGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20string_check_grader%20%3E%20(schema)) { input, name, operation, 2 more }  or [TextSimilarityGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20text_similarity_grader%20%3E%20(schema)) { evaluation\_metric, input, name, 2 more }  or [PythonGrader](/api/reference/cli/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20python_grader%20%3E%20(schema)) { name, source, type, image\_tag }  or 2 more

The grader used for the fine-tuning job.

--model-sample: string

The model sample to be evaluated. This value will be used to populate
the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
The `output_json` variable will be populated if the model sample is a
valid JSON string.

--item: optional unknown

The dataset item provided to the grader. This will be used to populate
the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.

##### ReturnsExpand Collapse

FineTuningAlphaGraderRunResponse: object { metadata, model\_grader\_token\_usage\_per\_model, reward, sub\_rewards }

metadata: object { errors, execution\_time, name, 4 more }

errors: object { formula\_parse\_error, invalid\_variable\_error, model\_grader\_parse\_error, 11 more }

formula\_parse\_error: boolean

invalid\_variable\_error: boolean

model\_grader\_parse\_error: boolean

model\_grader\_refusal\_error: boolean

model\_grader\_server\_error: boolean

model\_grader\_server\_error\_details: string

other\_error: boolean

python\_grader\_runtime\_error: boolean

python\_grader\_runtime\_error\_details: string

python\_grader\_server\_error: boolean

python\_grader\_server\_error\_type: string

sample\_parse\_error: boolean

truncated\_observation\_error: boolean

unresponsive\_reward\_error: boolean

execution\_time: number

name: string

sampled\_model\_name: string

scores: map[unknown]

token\_usage: number

type: string

model\_grader\_token\_usage\_per\_model: map[unknown]

reward: number

sub\_rewards: map[unknown]

### Run grader

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai fine-tuning:alpha:graders run \
  --api-key 'My API Key' \
  --grader '{input: input, name: name, operation: eq, reference: reference, type: string_check}' \
  --model-sample model_sample

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
