<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Fine Tuning](/api/reference/ruby/resources/fine_tuning)

[Jobs](/api/reference/ruby/resources/fine_tuning/subresources/jobs)

[Checkpoints](/api/reference/ruby/resources/fine_tuning/subresources/jobs/subresources/checkpoints)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning checkpoints

fine\_tuning.jobs.checkpoints.list(fine\_tuning\_job\_id, \*\*kwargs) -> CursorPage<[FineTuningJobCheckpoint](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)) { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more } >

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

List checkpoints for a fine-tuning job.

##### ParametersExpand Collapse

fine\_tuning\_job\_id: String

after: String

Identifier for the last checkpoint ID from the previous pagination request.

limit: Integer

Number of checkpoints to retrieve.

##### ReturnsExpand Collapse

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

### List fine-tuning checkpoints

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

page = openai.fine_tuning.jobs.checkpoints.list("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(page)

  "object": "list",
  "data": [
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:96olL566:ckpt-step-2000",
      "metrics": {
        "full_valid_loss": 0.134,
        "full_valid_mean_token_accuracy": 0.874
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 2000
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
      "metrics": {
        "full_valid_loss": 0.167,
        "full_valid_mean_token_accuracy": 0.781
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 1000
  ],
  "first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:96olL566:ckpt-step-2000",
      "metrics": {
        "full_valid_loss": 0.134,
        "full_valid_mean_token_accuracy": 0.874
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 2000
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "fine_tuned_model_checkpoint": "ft:gpt-4o-mini-2024-07-18:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
      "metrics": {
        "full_valid_loss": 0.167,
        "full_valid_mean_token_accuracy": 0.781
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 1000
  ],
  "first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": true
