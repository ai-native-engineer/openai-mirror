<!-- source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

[Jobs](/api/reference/resources/fine_tuning/subresources/jobs)

[Checkpoints](/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning checkpoints

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

List checkpoints for a fine-tuning job.

##### Path ParametersExpand Collapse

fine\_tuning\_job\_id: string

##### Query ParametersExpand Collapse

after: optional string

Identifier for the last checkpoint ID from the previous pagination request.

limit: optional number

Number of checkpoints to retrieve.

##### ReturnsExpand Collapse

data: array of [FineTuningJobCheckpoint](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)) { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more }

id: string

The checkpoint identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

fine\_tuned\_model\_checkpoint: string

The name of the fine-tuned checkpoint model that is created.

fine\_tuning\_job\_id: string

The name of the fine-tuning job that this checkpoint was created from.

metrics: object { full\_valid\_loss, full\_valid\_mean\_token\_accuracy, step, 4 more }

Metrics at the step number during the fine-tuning job.

full\_valid\_loss: optional number

full\_valid\_mean\_token\_accuracy: optional number

step: optional number

train\_loss: optional number

train\_mean\_token\_accuracy: optional number

valid\_loss: optional number

valid\_mean\_token\_accuracy: optional number

object: "fine\_tuning.job.checkpoint"

The object type, which is always “fine\_tuning.job.checkpoint”.

step\_number: number

The step number that the checkpoint was created at.

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

### List fine-tuning checkpoints

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/checkpoints \
  -H "Authorization: Bearer $OPENAI_API_KEY"

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
