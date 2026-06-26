<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

[Jobs](/api/reference/go/resources/fine_tuning/subresources/jobs)

[Checkpoints](/api/reference/go/resources/fine_tuning/subresources/jobs/subresources/checkpoints)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning checkpoints

client.FineTuning.Jobs.Checkpoints.List(ctx, fineTuningJobID, query) (\*CursorPage[[FineTuningJobCheckpoint](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema))], error)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

List checkpoints for a fine-tuning job.

##### ParametersExpand Collapse

fineTuningJobID string

query FineTuningJobCheckpointListParams

After param.Field[string]Optional

Identifier for the last checkpoint ID from the previous pagination request.

Limit param.Field[int64]Optional

Number of checkpoints to retrieve.

##### ReturnsExpand Collapse

type FineTuningJobCheckpoint struct{…}

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

ID string

The checkpoint identifier, which can be referenced in the API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

FineTunedModelCheckpoint string

The name of the fine-tuned checkpoint model that is created.

FineTuningJobID string

The name of the fine-tuning job that this checkpoint was created from.

Metrics FineTuningJobCheckpointMetrics

Metrics at the step number during the fine-tuning job.

FullValidLoss float64Optional

FullValidMeanTokenAccuracy float64Optional

Step float64Optional

TrainLoss float64Optional

TrainMeanTokenAccuracy float64Optional

ValidLoss float64Optional

ValidMeanTokenAccuracy float64Optional

Object FineTuningJobCheckpoint

The object type, which is always “fine\_tuning.job.checkpoint”.

StepNumber int64

The step number that the checkpoint was created at.

### List fine-tuning checkpoints

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.FineTuning.Jobs.Checkpoints.List(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningJobCheckpointListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
