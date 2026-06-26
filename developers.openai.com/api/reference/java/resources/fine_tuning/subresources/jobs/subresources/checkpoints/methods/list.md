<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

[Jobs](/api/reference/java/resources/fine_tuning/subresources/jobs)

[Checkpoints](/api/reference/java/resources/fine_tuning/subresources/jobs/subresources/checkpoints)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning checkpoints

CheckpointListPage fineTuning().jobs().checkpoints().list(CheckpointListParamsparams = CheckpointListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

List checkpoints for a fine-tuning job.

##### ParametersExpand Collapse

CheckpointListParams params

Optional<String> fineTuningJobId

Optional<String> after

Identifier for the last checkpoint ID from the previous pagination request.

Optional<Long> limit

Number of checkpoints to retrieve.

##### ReturnsExpand Collapse

class FineTuningJobCheckpoint:

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

String id

The checkpoint identifier, which can be referenced in the API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

String fineTunedModelCheckpoint

The name of the fine-tuned checkpoint model that is created.

String fineTuningJobId

The name of the fine-tuning job that this checkpoint was created from.

Metrics metrics

Metrics at the step number during the fine-tuning job.

Optional<Double> fullValidLoss

Optional<Double> fullValidMeanTokenAccuracy

Optional<Double> step

Optional<Double> trainLoss

Optional<Double> trainMeanTokenAccuracy

Optional<Double> validLoss

Optional<Double> validMeanTokenAccuracy

JsonValue; object\_ "fine\_tuning.job.checkpoint"constant"fine\_tuning.job.checkpoint"constant

The object type, which is always “fine\_tuning.job.checkpoint”.

long stepNumber

The step number that the checkpoint was created at.

### List fine-tuning checkpoints

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
import com.openai.models.finetuning.jobs.checkpoints.CheckpointListPage;
import com.openai.models.finetuning.jobs.checkpoints.CheckpointListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CheckpointListPage page = client.fineTuning().jobs().checkpoints().list("ft-AF1WoRqd3aJAHsqc9NY7iL8F");

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
