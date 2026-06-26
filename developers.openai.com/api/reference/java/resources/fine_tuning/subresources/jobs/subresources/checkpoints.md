<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/jobs/subresources/checkpoints/ -->

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

# Checkpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/java/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

CheckpointListPage fineTuning().jobs().checkpoints().list(CheckpointListParamsparams = CheckpointListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

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
